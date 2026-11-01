#!/usr/bin/env python3
"""
teegris_fido_pass_tlv_fuzzer.py
Suite de Auditoria Defensiva e Verificacao de Invariantes para Parsers TLV
baseada nas estruturas de diagnostico documentadas nos Trustlets FIDO/Pass:
  - _decodeTlvData / _decodeTlvDataWithExactLength
  - _checkBasicDecodeResult / _checkDecodeResultWithExactLength
  - offsetoverflow (TAG_WRAPPED_DATA_CHALLENGE input:x offset:d length:d)
  - rutdecapsulatefailitisnoterror / encapforesefailitisnoterror
  - E:sd:wrongtag:expected:xactualx (TAG_PASS_WRAP_NW_DATA_COMMAND / UNWRAP)
  - DecapsulatedchallengeisdifferedfromFinalchallengeincommand
"""

import struct
from dataclasses import dataclass
from typing import List, Tuple, Optional, Dict


# ============================================================================
# 1. Tabela de Tags FIDO UAF e Samsung Pass (Padrão Little-Endian 16-bit TLV)
# ============================================================================
TAG_UAFV1_REGISTER_CMD = 0x3401
TAG_UAFV1_SIGN_CMD = 0x3402
TAG_UAFV1_DEREGISTER_CMD = 0x3403
TAG_UAFV1_OPEN_SETTINGS_CMD = 0x3406

TAG_AUTHENTICATOR_INDEX = 0x2E0D
TAG_APPID = 0x2E04
TAG_FINAL_CHALLENGE = 0x2E0A
TAG_USERNAME = 0x2E06
TAG_ATTESTATION_TYPE = 0x2E07
TAG_KEYHANDLE_ACCESS_TOKEN = 0x2E05
TAG_USERVERIFY_TOKEN = 0x2E09
TAG_KEYHANDLE = 0x2E01
TAG_EXTENSION = 0x3E11
TAG_EXTENSION_ID = 0x2E13
TAG_EXTENSION_DATA = 0x2E14

# Sub-tags internas de pBlobWrappedData
TAG_WRAPPED_DATA_CHALLENGE = 0x1001
TAG_WRAPPED_DATA_ENROLL_ID = 0x1002
TAG_WRAPPED_DATA_MATCHER_DATA = 0x1003
TAG_WRAPPED_DATA_APP_ID = 0x1004
TAG_WRAPPED_DATA_TEMPLATE_DATA = 0x1005
TAG_WRAPPED_DATA_USER_VERIFICATION = 0x1007

# Tags de comandos Samsung Pass / KMX
TAG_PASS_WRAP_NW_DATA_COMMAND = 0x5001
TAG_PASS_UNWRAP_NW_DATA_COMMAND = 0x5002
TAG_PASS_PLAIN_DATA = 0x5010
TAG_PASS_KEY_TYPE = 0x5011
TAG_PASS_AUTH_VERIFY_TOKEN = 0x5012
TAG_PASS_WRAPPED_KEY = 0x5020
TAG_PASS_PROVISION_ASSERTION_PSK = 0x5021

UINT32_MAX = 0xFFFFFFFF


@dataclass
class TlvRecord:
    tag: int
    length: int
    value_offset: int
    raw_value: bytes


@dataclass
class ParserAuditReport:
    test_name: str
    vulnerable_parser_status: str
    hardened_parser_status: str
    diagnostic_log: str
    security_invariant_preserved: bool


def pack_tlv_16le_32len(tag: int, value: bytes, override_length: Optional[int] = None) -> bytes:
    """
    Empacota um registro TLV com Tag de 16 bits e Length de 32 bits (little-endian)
    para testar verificações de limite de cursor em arquiteturas de 32 bits.
    """
    declared_len = len(value) if override_length is None else (override_length & UINT32_MAX)
    return struct.pack("<HI", tag & 0xFFFF, declared_len) + value


class TrustletTlvParserSimulator:
    """
    Simula lado a lado:
      (A) Uma implementação ingênua em 32 bits sem verificação de overflow na soma
          (offset + length) e com tratamento fail-open ('itisnoterror').
      (B) Uma implementação endurecida (hardened) com aritmética livre de overflow
          e validação estrita fail-closed.
    """

    @staticmethod
    def decode_tlv_vulnerable_32bit(blob: bytes, initial_offset: int = 0) -> Tuple[str, int, int]:
        """
        Modela o bug clássico de wrap-around em uint32_t:
          uint32_t next_offset = (offset + 6 + length) & 0xFFFFFFFF;
          if (next_offset <= blob_size) -> FALSO POSITIVO quando length ~ 2^32!
        """
        blob_size = len(blob) & UINT32_MAX
        if initial_offset + 6 > blob_size:
            return "decodeerror:header_oob", initial_offset, 0

        tag, declared_len = struct.unpack_from("<HI", blob, initial_offset)
        # Soma aritmética truncada em 32 bits (simula uint32_t sem __builtin_add_overflow)
        data_offset = (initial_offset + 6) & UINT32_MAX
        wrapped_end = (data_offset + declared_len) & UINT32_MAX