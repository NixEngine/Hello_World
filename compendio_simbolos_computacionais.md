# COMPÊNDIO TÉCNICO DE SÍMBOLOS COMPUTACIONAIS

---

## 1. CARACTERES DE CONTROLE (0x00-0x1F)

### Tabela Completa de Caracteres C0

| Hex | Dec | Binário | Acrônimo | Nome | CP437 | Função |
|-----|-----|---------|----------|------|-------|--------|
| 00 | 0 | 00000000 | NUL | Null | | Terminador de string, preenchimento |
| 01 | 1 | 00000001 | SOH | Start of Heading | ☺ | Início de cabeçalho |
| 02 | 2 | 00000010 | STX | Start of Text | ☻ | Início de texto |
| 03 | 3 | 00000011 | ETX | End of Text | ♥ | Fim de texto (Ctrl+C) |
| 04 | 4 | 00000100 | EOT | End of Transmission | ♦ | EOF Unix (Ctrl+D) |
| 05 | 5 | 00000101 | ENQ | Enquiry | ♣ | Solicitação de resposta |
| 06 | 6 | 00000110 | ACK | Acknowledge | ♠ | Confirmação positiva |
| 07 | 7 | 00000111 | BEL | Bell | • | Sinal sonoro |
| 08 | 8 | 00001000 | BS | Backspace | ◘ | Retrocesso |
| 09 | 9 | 00001001 | HT | Horizontal Tab | ○ | Tabulação horizontal |
| 0A | 10 | 00001010 | LF | Line Feed | ◙ | Nova linha (Unix) |
| 0B | 11 | 00001011 | VT | Vertical Tab | ♂ | Tabulação vertical |
| 0C | 12 | 00001100 | FF | Form Feed | ♀ | Nova página |
| 0D | 13 | 00001101 | CR | Carriage Return | ♪ | Início da linha |
| 0E | 14 | 00001110 | SO | Shift Out | ♫ | Conjunto alternativo |
| 0F | 15 | 00001111 | SI | Shift In | ☼ | Conjunto padrão |
| 10 | 16 | 00010000 | DLE | Data Link Escape | ► | Escape de enlace |
| 11 | 17 | 00010001 | DC1/XON | Device Control 1 | ◄ | Retomar transmissão |
| 12 | 18 | 00010010 | DC2 | Device Control 2 | ↕ | Controle de dispositivo |
| 13 | 19 | 00010011 | DC3/XOFF | Device Control 3 | ‼ | Pausar transmissão |
| 14 | 20 | 00010100 | DC4 | Device Control 4 | ¶ | Controle de dispositivo |
| 15 | 21 | 00010101 | NAK | Negative Acknowledge | § | Confirmação negativa |
| 16 | 22 | 00010110 | SYN | Synchronous Idle | ▬ | Sincronização |
| 17 | 23 | 00010111 | ETB | End of Trans. Block | ↨ | Fim de bloco |
| 18 | 24 | 00011000 | CAN | Cancel | ↑ | Cancelar |
| 19 | 25 | 00011001 | EM | End of Medium | ↓ | Fim de mídia |
| 1A | 26 | 00011010 | SUB | Substitute | → | EOF DOS (Ctrl+Z) |
| 1B | 27 | 00011011 | ESC | Escape | ← | Sequências de escape |
| 1C | 28 | 00011100 | FS | File Separator | ∟ | Separador de arquivo |
| 1D | 29 | 00011101 | GS | Group Separator | ↔ | Separador de grupo |
| 1E | 30 | 00011110 | RS | Record Separator | ▲ | Separador de registro |
| 1F | 31 | 00011111 | US | Unit Separator | ▼ | Separador de unidade |
| 7F | 127 | 01111111 | DEL | Delete | ⌂ | Apagar |

### Convenções de Final de Linha (EOL)

| Sistema | Convenção | Bytes | Representação |
|---------|-----------|-------|---------------|
| Unix/Linux/macOS | LF | 0x0A | `\n` |
| Windows/DOS | CR+LF | 0x0D 0x0A | `\r\n` |
| Classic Mac OS | CR | 0x0D | `\r` |
| Protocolos Internet | CR+LF | 0x0D 0x0A | `\r\n` |

### Caracteres de Controle C1 (0x80-0x9F)

| Hex | Dec | Nome | Equivalente 7-bit |
|-----|-----|------|-------------------|
| 80 | 128 | PAD | - |
| 81 | 129 | HOP | - |
| 84 | 132 | IND | ESC D |
| 85 | 133 | NEL | ESC E |
| 88 | 136 | HTS | ESC H |
| 8D | 141 | RI | ESC M |
| 8E | 142 | SS2 | ESC N |
| 8F | 143 | SS3 | ESC O |
| 90 | 144 | DCS | ESC P |
| 9B | 155 | CSI | ESC [ |
| 9C | 156 | ST | ESC \ |
| 9D | 157 | OSC | ESC ] |
| 9E | 158 | PM | ESC ^ |
| 9F | 159 | APC | ESC _ |

---

## 2. OPCODES x86

### Tabela de Opcodes Principais

| Opcode | Mnemônico | Categoria | Descrição |
|--------|-----------|-----------|-----------|
| 0x90 | NOP | Controle | No Operation (XCHG EAX,EAX) |
| 0xCC | INT3 | Interrupção | Breakpoint de software |
| 0xCD | INT n | Interrupção | Interrupção de software |
| 0xE8 | CALL rel32 | Controle | Chamada relativa (4 bytes offset) |
| 0xE9 | JMP rel32 | Controle | Salto relativo longo (4 bytes) |
| 0xEB | JMP rel8 | Controle | Salto relativo curto (1 byte) |
| 0xC3 | RET | Controle | Retorno de função |
| 0xC2 | RET n | Controle | Retorno com cleanup de pilha |
| 0x31 | XOR r/m,r | Lógica | XOR (destino r/m) |
| 0x33 | XOR r,r/m | Lógica | XOR (destino registrador) |
| 0x89 | MOV r/m,r | Dados | Movimentação (destino r/m) |
| 0x8B | MOV r,r/m | Dados | Movimentação (destino reg) |
| 0x84 | TEST r/m8,r8 | Lógica | Teste AND (8 bits) |
| 0x85 | TEST r/m,r | Lógica | Teste AND (16/32 bits) |
| 0x4C | DEC ESP | Aritmética | Decremento (legacy x86) |
| 0x69 | IMUL r,r/m,imm | Aritmética | Multiplicação com sinal |
| 0x92 | XCHG EDX,EAX | Dados | Troca de registradores |
| 0xFF | Grupo | Múltiplo | /2=CALL, /4=JMP, /6=PUSH |

### PUSH/POP (0x50-0x5F)

| Opcode | Instrução | Opcode | Instrução |
|--------|-----------|--------|-----------|
| 0x50 | PUSH EAX | 0x58 | POP EAX |
| 0x51 | PUSH ECX | 0x59 | POP ECX |
| 0x52 | PUSH EDX | 0x5A | POP EDX |
| 0x53 | PUSH EBX | 0x5B | POP EBX |
| 0x54 | PUSH ESP | 0x5C | POP ESP |
| 0x55 | PUSH EBP | 0x5D | POP EBP |
| 0x56 | PUSH ESI | 0x5E | POP ESI |
| 0x57 | PUSH EDI | 0x5F | POP EDI |

### Grupo 0xFF (ModR/M)

| /r | Mnemônico | Descrição |
|----|-----------|-----------|
| /0 | INC r/m | Incremento |
| /1 | DEC r/m | Decremento |
| /2 | CALL r/m | Chamada indireta |
| /4 | JMP r/m | Salto indireto |
| /6 | PUSH r/m | Push indireto |

---

## 3. OPCODES ARM

### Instruções de Branch

| Instrução | Tipo | Link | Interworking | Descrição |
|-----------|------|------|--------------|-----------|
| B label | Relativo | Não | Não | Desvio incondicional |
| BL label | Relativo | LR | Não | Branch with Link |
| BX reg | Absoluto | Não | Sim | Branch and Exchange |
| BLX reg | Absoluto | LR | Sim | Branch Link Exchange |

### Instruções de Memória

| Instrução | Operação | Exemplo |
|-----------|----------|---------|
| LDR | Load Register | `LDR r0, [r1, #4]` |
| STR | Store Register | `STR r0, [r1]` |
| LDM | Load Multiple | `LDMIA r0!, {r1-r4}` |
| STM | Store Multiple | `STMDB r0!, {r1-r4}` |

### Instruções Aritméticas/Lógicas

| Instrução | Operação |
|-----------|----------|
| ADD | Soma |
| ADC | Soma com Carry |
| SUB | Subtração |
| SBC | Subtração com Carry |
| MUL | Multiplicação 32-bit |
| SMULL | Multiplicação 64-bit (signed) |
| UMULL | Multiplicação 64-bit (unsigned) |
| AND | AND lógico |
| ORR | OR lógico |
| EOR | XOR lógico |
| BIC | Bit Clear (AND NOT) |
| CMP | Comparação (atualiza flags) |
| TST | Teste AND (atualiza flags) |

### Formato de Instrução ARM (32 bits)

```
| 31-28 | 27-21 | 20 | 19-16 | 15-12 | 11-0 |
| Cond  | Opcode| S  | Rn    | Rd    | Operand2 |
```

### Códigos de Condição

| Código | Sufixo | Condição |
|--------|--------|----------|
| 0000 | EQ | Z=1 (igual) |
| 0001 | NE | Z=0 (diferente) |
| 0010 | CS/HS | C=1 (carry set) |
| 0011 | CC/LO | C=0 (carry clear) |
| 0100 | MI | N=1 (negativo) |
| 0101 | PL | N=0 (positivo) |
| 1010 | GE | N=V (maior ou igual) |
| 1011 | LT | N≠V (menor) |
| 1100 | GT | Z=0 AND N=V |
| 1101 | LE | Z=1 OR N≠V |
| 1110 | AL | Sempre |

---

## 4. MAGIC NUMBERS

| Formato | Assinatura (Hex) | ASCII | Offset |
|---------|------------------|-------|--------|
| DOS/PE (MZ) | 4D 5A | MZ | 0 |
| ELF | 7F 45 4C 46 | .ELF | 0 |
| ZIP/PK | 50 4B 03 04 | PK.. | 0 |
| PNG | 89 50 4E 47 0D 0A 1A 0A | .PNG.... | 0 |
| JPEG | FF D8 FF | ÿØÿ | 0 |
| PDF | 25 50 44 46 | %PDF | 0 |
| GIF87a | 47 49 46 38 37 61 | GIF87a | 0 |
| GIF89a | 47 49 46 38 39 61 | GIF89a | 0 |
| RAR v1.5+ | 52 61 72 21 1A 07 00 | Rar!... | 0 |
| RAR v5.0+ | 52 61 72 21 1A 07 01 00 | Rar!.... | 0 |
| 7z | 37 7A BC AF 27 1C | 7z¼¯'. | 0 |
| TAR (UStar) | 75 73 74 61 72 | ustar | 257 |
| GZIP | 1F 8B | .. | 0 |
| BMP | 42 4D | BM | 0 |
| MP3 (ID3) | 49 44 33 | ID3 | 0 |
| MP3 (sync) | FF FB | ÿû | 0 |
| WAV | 52 49 46 46...57 41 56 45 | RIFF...WAVE | 0,8 |
| Java Class | CA FE BA BE | Êþº¾ | 0 |
| SQLite | 53 51 4C 69 74 65 20 66 6F 72 6D 61 74 20 33 00 | SQLite format 3. | 0 |
| DOCX/XLSX | 50 4B 03 04 | PK.. | 0 |

---

## 5. CODIFICAÇÕES DE CARACTERES

### Code Page 437 (DOS)

#### Caracteres Gráficos (0x00-0x1F exibidos)

| Hex | Símbolo | Hex | Símbolo | Hex | Símbolo | Hex | Símbolo |
|-----|---------|-----|---------|-----|---------|-----|---------|
| 01 | ☺ | 09 | ○ | 11 | ◄ | 19 | ↓ |
| 02 | ☻ | 0A | ◙ | 12 | ↕ | 1A | → |
| 03 | ♥ | 0B | ♂ | 13 | ‼ | 1B | ← |
| 04 | ♦ | 0C | ♀ | 14 | ¶ | 1C | ∟ |
| 05 | ♣ | 0D | ♪ | 15 | § | 1D | ↔ |
| 06 | ♠ | 0E | ♫ | 16 | ▬ | 1E | ▲ |
| 07 | • | 0F | ☼ | 17 | ↨ | 1F | ▼ |
| 08 | ◘ | 10 | ► | 18 | ↑ | 7F | ⌂ |

#### Caracteres Acentuados (0x80-0xA5)

| Hex | Char | Hex | Char | Hex | Char | Hex | Char |
|-----|------|-----|------|-----|------|-----|------|
| 80 | Ç | 8A | è | 94 | ö | 9E | ₧ |
| 81 | ü | 8B | ï | 95 | ò | 9F | ƒ |
| 82 | é | 8C | î | 96 | û | A0 | á |
| 83 | â | 8D | ì | 97 | ù | A1 | í |
| 84 | ä | 8E | Ä | 98 | ÿ | A2 | ó |
| 85 | à | 8F | Å | 99 | Ö | A3 | ú |
| 86 | å | 90 | É | 9A | Ü | A4 | ñ |
| 87 | ç | 91 | æ | 9B | ¢ | A5 | Ñ |
| 88 | ê | 92 | Æ | 9C | £ | | |
| 89 | ë | 93 | ô | 9D | ¥ | | |

#### Box Drawing (0xB0-0xDF)

| Hex | Char | Descrição | Hex | Char | Descrição |
|-----|------|-----------|-----|------|-----------|
| B0 | ░ | Light shade | C0 | └ | Up-right corner |
| B1 | ▒ | Medium shade | C1 | ┴ | Up-horizontal |
| B2 | ▓ | Dark shade | C2 | ┬ | Down-horizontal |
| B3 | │ | Vertical | C3 | ├ | Vertical-right |
| B4 | ┤ | Vertical-left | C4 | ─ | Horizontal |
| B9 | ╣ | Double vert-left | C5 | ┼ | Cross |
| BA | ║ | Double vertical | C8 | ╚ | Double up-right |
| BB | ╗ | Double down-left | C9 | ╔ | Double down-right |
| BC | ╝ | Double up-left | CA | ╩ | Double up-horiz |
| BF | ┐ | Down-left corner | CB | ╦ | Double down-horiz |
| | | | CD | ═ | Double horizontal |
| | | | CE | ╬ | Double cross |

#### Símbolos Matemáticos/Gregos (0xE0-0xFE)

| Hex | Char | Nome | Hex | Char | Nome |
|-----|------|------|-----|------|------|
| E0 | α | Alpha | F0 | ≡ | Idêntico |
| E1 | ß | Eszett | F1 | ± | Mais-menos |
| E2 | Γ | Gamma | F2 | ≥ | Maior-igual |
| E3 | π | Pi | F3 | ≤ | Menor-igual |
| E4 | Σ | Sigma maiúsculo | F4 | ⌠ | Integral sup |
| E5 | σ | Sigma minúsculo | F5 | ⌡ | Integral inf |
| E6 | µ | Micro | F6 | ÷ | Divisão |
| E7 | τ | Tau | F7 | ≈ | Aproximado |
| E8 | Φ | Phi maiúsculo | F8 | ° | Grau |
| E9 | Θ | Theta | F9 | ∙ | Bullet |
| EA | Ω | Omega | FA | · | Middle dot |
| EB | δ | Delta | FB | √ | Raiz quadrada |
| EC | ∞ | Infinito | FC | ⁿ | Expoente n |
| ED | φ | Phi minúsculo | FD | ² | Expoente 2 |
| EE | ε | Epsilon | FE | ■ | Quadrado preto |
| EF | ∩ | Interseção | | | |

### Windows-1252 vs ISO-8859-1 (Faixa 0x80-0x9F)

| Hex | Win-1252 | ISO-8859-1 |
|-----|----------|------------|
| 80 | € | (controle) |
| 82 | ‚ | (controle) |
| 83 | ƒ | (controle) |
| 84 | „ | (controle) |
| 85 | … | (controle) |
| 86 | † | (controle) |
| 87 | ‡ | (controle) |
| 88 | ˆ | (controle) |
| 89 | ‰ | (controle) |
| 8A | Š | (controle) |
| 8B | ‹ | (controle) |
| 8C | Œ | (controle) |
| 8E | Ž | (controle) |
| 91 | ' | (controle) |
| 92 | ' | (controle) |
| 93 | " | (controle) |
| 94 | " | (controle) |
| 95 | • | (controle) |
| 96 | – | (controle) |
| 97 | — | (controle) |
| 98 | ˜ | (controle) |
| 99 | ™ | (controle) |
| 9A | š | (controle) |
| 9B | › | (controle) |
| 9C | œ | (controle) |
| 9E | ž | (controle) |
| 9F | Ÿ | (controle) |

### ISO-8859 (Partes)

| Parte | Nome | Região/Idiomas |
|-------|------|----------------|
| 1 | Latin-1 | Europa Ocidental |
| 2 | Latin-2 | Europa Central |
| 3 | Latin-3 | Europa do Sul |
| 4 | Latin-4 | Europa do Norte |
| 5 | Cyrillic | Russo, Búlgaro |
| 6 | Arabic | Árabe |
| 7 | Greek | Grego moderno |
| 8 | Hebrew | Hebraico |
| 9 | Latin-5 | Turco |
| 10 | Latin-6 | Nórdico |
| 11 | Thai | Tailandês |
| 13 | Latin-7 | Báltico |
| 14 | Latin-8 | Celta |
| 15 | Latin-9 | Latin-1 + Euro (€) |
| 16 | Latin-10 | Sudeste Europeu |

### UTF-8 (Estrutura de Bytes)

| Faixa Unicode | Bytes | Formato |
|---------------|-------|---------|
| U+0000-007F | 1 | 0xxxxxxx |
| U+0080-07FF | 2 | 110xxxxx 10xxxxxx |
| U+0800-FFFF | 3 | 1110xxxx 10xxxxxx 10xxxxxx |
| U+10000-10FFFF | 4 | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx |

### BOM (Byte Order Mark)

| Codificação | BOM (Hex) |
|-------------|-----------|
| UTF-8 | EF BB BF |
| UTF-16 BE | FE FF |
| UTF-16 LE | FF FE |
| UTF-32 BE | 00 00 FE FF |
| UTF-32 LE | FF FE 00 00 |

### KOI8-R (Cirílico)

| Hex | Minúscula | Hex | Maiúscula |
|-----|-----------|-----|-----------|
| C0 | ю | E0 | А |
| C1 | б | E1 | Б |
| C2 | ц | E2 | Ц |
| C3 | д | E3 | Д |
| C4 | е | E4 | Е |
| C5 | ф | E5 | Ф |
| C6 | г | E6 | Г |
| C7 | х | E7 | Х |
| C8 | и | E8 | И |
| C9 | й | E9 | Й |
| CA | к | EA | К |
| CB | л | EB | Л |
| CC | м | EC | М |
| CD | н | ED | Н |
| CE | о | EE | О |
| CF | п | EF | П |

### EBCDIC vs ASCII (Comparação)

| Caractere | ASCII | EBCDIC (CP037) |
|-----------|-------|----------------|
| Espaço | 0x20 | 0x40 |
| 0-9 | 0x30-0x39 | 0xF0-0xF9 |
| A-I | 0x41-0x49 | 0xC1-0xC9 |
| J-R | 0x4A-0x52 | 0xD1-0xD9 |
| S-Z | 0x53-0x5A | 0xE2-0xE9 |
| a-i | 0x61-0x69 | 0x81-0x89 |
| j-r | 0x6A-0x72 | 0x91-0x99 |
| s-z | 0x73-0x7A | 0xA2-0xA9 |
| LF | 0x0A | 0x25 |
| CR | 0x0D | 0x0D |

---

## 6. PADDING CRIPTOGRÁFICO

### Esquemas de Padding para Cifras de Bloco

| Esquema | Padrão | Exemplo (4 bytes) |
|---------|--------|-------------------|
| PKCS#7 | N bytes com valor N | `04 04 04 04` |
| ISO/IEC 7816-4 | 0x80 + zeros | `80 00 00 00` |
| ANSI X.923 | Zeros + N | `00 00 00 04` |
| ISO 10126 | Random + N | `XX XX XX 04` |
| Zero Padding | Apenas zeros | `00 00 00 00` |

### PKCS#7 - Exemplos

| Dados (5 bytes) | Padding (3 bytes) | Resultado |
|-----------------|-------------------|-----------|
| `DD DD DD DD DD` | `03 03 03` | `DD DD DD DD DD 03 03 03` |
| `DD DD DD DD DD DD DD DD` | `08 08 08 08 08 08 08 08` | Bloco completo de padding |

### RSA Padding

| Esquema | Estrutura | Segurança |
|---------|-----------|-----------|
| PKCS#1 v1.5 | `02 [random] 00 [msg]` | Vulnerável a Bleichenbacher |
| OAEP | MGF + seed aleatória | IND-CCA2 (recomendado) |

---

## 7. PROTOCOLOS SERIAIS

### RS-232 - Sinais de Controle

| Sinal | Nome | Direção | Função |
|-------|------|---------|--------|
| RTS | Request to Send | DTE→DCE | Solicita transmissão |
| CTS | Clear to Send | DCE→DTE | Pronto para receber |
| DTR | Data Terminal Ready | DTE→DCE | Terminal pronto |
| DSR | Data Set Ready | DCE→DTE | Modem pronto |
| DCD | Data Carrier Detect | DCE→DTE | Portadora detectada |
| RI | Ring Indicator | DCE→DTE | Chamada recebida |

### Controle de Fluxo

| Tipo | Método | Bytes |
|------|--------|-------|
| Software | XON/XOFF | 0x11 / 0x13 |
| Hardware | RTS/CTS | Sinais elétricos |

### XMODEM - Estrutura de Pacote

| Campo | Valor | Tamanho |
|-------|-------|---------|
| SOH | 0x01 | 1 byte |
| Número do bloco | 01-FF | 1 byte |
| Complemento | ~número | 1 byte |
| Dados | | 128 bytes |
| Checksum/CRC | | 1-2 bytes |

### Caracteres de Controle XMODEM

| Caractere | Hex | Função |
|-----------|-----|--------|
| SOH | 0x01 | Início de pacote 128 bytes |
| EOT | 0x04 | Fim de transmissão |
| ACK | 0x06 | Confirmação positiva |
| NAK | 0x15 | Confirmação negativa |
| CAN | 0x18 | Cancelar (enviar 2x) |
| SUB | 0x1A | Padding de fim de arquivo |

### YMODEM - Adições

| Caractere | Hex | Função |
|-----------|-----|--------|
| STX | 0x02 | Início de pacote 1024 bytes |
| 'C' | 0x43 | Solicita modo CRC |

### ZMODEM - Caracteres Especiais

| Caractere | Hex | Função |
|-----------|-----|--------|
| ZDLE | 0x18 | Data Link Escape |
| ZRINIT | 0x2A (*) | Início de cabeçalho ZHEX |

### Comandos Hayes AT

| Comando | Função |
|---------|--------|
| AT | Teste de conexão |
| ATD[número] | Discar |
| ATH | Desligar |
| ATA | Atender |
| ATO | Retornar ao modo dados |
| ATZ | Reset |
| ATE0/ATE1 | Eco off/on |
| AT&F | Configurações de fábrica |

### Parâmetros de Comunicação Serial

| Parâmetro | Valores Comuns |
|-----------|----------------|
| Baud Rate | 300, 1200, 2400, 9600, 19200, 38400, 57600, 115200 |
| Data Bits | 5, 6, 7, 8 |
| Stop Bits | 1, 1.5, 2 |
| Paridade | None, Even, Odd, Mark, Space |

---

## 8. ANÁLISE DE ENTROPIA

### Fórmula de Shannon

```
H(X) = -Σ p(xᵢ) × log₂(p(xᵢ))
```

Onde:
- H(X) = entropia em bits
- p(xᵢ) = probabilidade do i-ésimo símbolo

### Interpretação de Entropia (para bytes)

| Entropia | Interpretação |
|----------|---------------|
| 0 bits | Dados uniformes (todos iguais) |
| < 5 bits | Texto ou dados estruturados |
| 5-7 bits | Dados comprimidos |
| > 7.5 bits | Dados criptografados ou aleatórios |
| 8 bits | Máxima aleatoriedade |

### Diferenciação Criptografia vs Compressão

| Técnica | Indicador |
|---------|-----------|
| Análise de cabeçalhos | Magic numbers de compressão |
| Entropia em blocos | Compressão: variável; Cripto: uniforme |
| Tentativa de descompressão | Sucesso indica compressão |
| Teste qui-quadrado | Uniformidade estatística |

---

## 9. ESTEGANOGRAFIA

### LSB (Least Significant Bit) em Imagens

**Fórmula de modificação:**
```
pixel_modificado = (pixel_original & 0xFE) | bit_secreto
```

**Capacidade:** 1 bit por canal de cor por pixel

### DCT em JPEG

**Processo:**
1. Divisão em blocos 8×8
2. Aplicação de DCT
3. Quantização
4. Modificação de coeficientes médios
5. Codificação

### Técnicas por Meio

| Meio | Técnica | Capacidade |
|------|---------|------------|
| Imagem (lossless) | LSB | Alta |
| JPEG | DCT | Média |
| GIF/PNG paleta | Paleta | Baixa |
| Áudio | LSB, Phase Coding | Alta |
| Vídeo | Intra/Inter-frame | Muito alta |
| Rede | Campos de cabeçalho, Timing | Baixa |
| Sistema de arquivos | Slack space, ADS | Variável |

### Metadados EXIF para Esteganografia

| Campo | Uso |
|-------|-----|
| UserComment | Texto arbitrário |
| ImageDescription | Descrição |
| XPComment | Comentário Windows |
| MakerNote | Dados proprietários |

---

## 10. SÍMBOLOS ESPECÍFICOS

### 0x00 (NUL)

| Contexto | Função |
|----------|--------|
| C/C++ | Terminador de string |
| Memória | Ponteiro nulo |
| Segurança | Null byte injection |
| Arquivos | Padding, slack space |

### 0x0A (LF)

| Sistema | Uso |
|---------|-----|
| Unix/Linux | EOL padrão |
| HTTP | Parte de CRLF |
| Programação | `\n` |
| Segurança | CRLF Injection |

### 0x1A (SUB)

| Sistema | Função |
|---------|--------|
| CP/M | Marcador EOF |
| MS-DOS | EOF em arquivos texto |
| XMODEM | Padding de pacote |
| Windows | Ctrl+Z (compatibilidade) |

### 0x1D (GS)

| Contexto | Uso |
|----------|-----|
| ASCII | Group Separator |
| GS1/EAN | Delimitador de códigos de barras |
| Dados | Separador hierárquico |

### 0x2A (*)

| Contexto | Significado |
|----------|-------------|
| ASCII | Asterisco (42 decimal) |
| Aritmética | Multiplicação |
| Shell | Wildcard (glob) |
| C/C++ | Ponteiro, desreferência |
| Regex | Kleene Star (0+ ocorrências) |

### 0x4C (L)

| Contexto | Significado |
|----------|-------------|
| ASCII | Letra 'L' (76 decimal) |
| x86 | DEC ESP (legacy) |
| x64 | Prefixo REX.W |
| C | Sufixo long literal |
| Programação | L-value |

### 0x69 (i)

| Contexto | Significado |
|----------|-------------|
| ASCII | Letra 'i' (105 decimal) |
| x86 | Opcode IMUL |
| Matemática | Unidade imaginária |

### 0x84

| Codificação | Caractere |
|-------------|-----------|
| CP437 | ä |
| Windows-1252 | „ |
| x86 | TEST r/m8,r8 |
| UTF-8 | Byte de continuação |
| C1 | IND (Index) |

### 0x92

| Codificação | Caractere |
|-------------|-----------|
| CP437 | Æ |
| Windows-1252 | ' |
| x86 | XCHG EDX,EAX |
| C1 | PU2 |

### 0xFE

| Codificação | Significado |
|-------------|-------------|
| CP437 | ■ (quadrado preto) |
| UTF-16 BE BOM | FE FF (início) |
| x86 | INC/DEC r/m8 |
| ISO-8859-1 | þ (thorn) |

---

## 11. CODIFICAÇÕES HISTÓRICAS

### Código Baudot (ITA1) - 5 bits

| Binário | Letras | Figuras |
|---------|--------|---------|
| 00001 | A | 1 |
| 00011 | E | 2 |
| 00101 | Y | 3 |
| 00111 | U | 4 |
| 01100 | O | 5 |
| 10101 | J | 6 |
| 11010 | G | 7 |
| 11001 | B | 8 |
| 10110 | C | 9 |
| 10011 | D | 0 |
| 11111 | LTRS | LTRS |
| 11011 | FIGS | FIGS |

### Shift-JIS (Japonês)

| Faixa | Tipo | Bytes |
|-------|------|-------|
| 0x00-0x7F | ASCII | 1 |
| 0xA1-0xDF | Katakana meia-largura | 1 |
| 0x81-0x9F, 0xE0-0xFC | Kanji/Hiragana | 2 |

### Big5 (Chinês Tradicional)

| Faixa Byte 1 | Faixa Byte 2 | Tipo |
|--------------|--------------|------|
| 0x00-0x7F | - | ASCII (1 byte) |
| 0xA1-0xF9 | 0x40-0x7E, 0xA1-0xFE | CJK (2 bytes) |

### GB2312 (Chinês Simplificado)

| Faixa | Tipo |
|-------|------|
| 0x00-0x7F | ASCII (1 byte) |
| 0xA1-0xFE (ambos bytes) | CJK (2 bytes) |

---

## 12. TABELA ASCII COMPLETA

### Caracteres de Controle (0-31, 127)

| Dec | Hex | Ctrl | Nome |
|-----|-----|------|------|
| 0 | 00 | ^@ | NUL |
| 1 | 01 | ^A | SOH |
| 2 | 02 | ^B | STX |
| 3 | 03 | ^C | ETX |
| 4 | 04 | ^D | EOT |
| 5 | 05 | ^E | ENQ |
| 6 | 06 | ^F | ACK |
| 7 | 07 | ^G | BEL |
| 8 | 08 | ^H | BS |
| 9 | 09 | ^I | HT |
| 10 | 0A | ^J | LF |
| 11 | 0B | ^K | VT |
| 12 | 0C | ^L | FF |
| 13 | 0D | ^M | CR |
| 14 | 0E | ^N | SO |
| 15 | 0F | ^O | SI |
| 16 | 10 | ^P | DLE |
| 17 | 11 | ^Q | DC1 |
| 18 | 12 | ^R | DC2 |
| 19 | 13 | ^S | DC3 |
| 20 | 14 | ^T | DC4 |
| 21 | 15 | ^U | NAK |
| 22 | 16 | ^V | SYN |
| 23 | 17 | ^W | ETB |
| 24 | 18 | ^X | CAN |
| 25 | 19 | ^Y | EM |
| 26 | 1A | ^Z | SUB |
| 27 | 1B | ^[ | ESC |
| 28 | 1C | ^\ | FS |
| 29 | 1D | ^] | GS |
| 30 | 1E | ^^ | RS |
| 31 | 1F | ^_ | US |
| 127 | 7F | ^? | DEL |

### Caracteres Imprimíveis (32-126)

| Dec | Hex | Char | Dec | Hex | Char | Dec | Hex | Char |
|-----|-----|------|-----|-----|------|-----|-----|------|
| 32 | 20 | (sp) | 64 | 40 | @ | 96 | 60 | ` |
| 33 | 21 | ! | 65 | 41 | A | 97 | 61 | a |
| 34 | 22 | " | 66 | 42 | B | 98 | 62 | b |
| 35 | 23 | # | 67 | 43 | C | 99 | 63 | c |
| 36 | 24 | $ | 68 | 44 | D | 100 | 64 | d |
| 37 | 25 | % | 69 | 45 | E | 101 | 65 | e |
| 38 | 26 | & | 70 | 46 | F | 102 | 66 | f |
| 39 | 27 | ' | 71 | 47 | G | 103 | 67 | g |
| 40 | 28 | ( | 72 | 48 | H | 104 | 68 | h |
| 41 | 29 | ) | 73 | 49 | I | 105 | 69 | i |
| 42 | 2A | * | 74 | 4A | J | 106 | 6A | j |
| 43 | 2B | + | 75 | 4B | K | 107 | 6B | k |
| 44 | 2C | , | 76 | 4C | L | 108 | 6C | l |
| 45 | 2D | - | 77 | 4D | M | 109 | 6D | m |
| 46 | 2E | . | 78 | 4E | N | 110 | 6E | n |
| 47 | 2F | / | 79 | 4F | O | 111 | 6F | o |
| 48 | 30 | 0 | 80 | 50 | P | 112 | 70 | p |
| 49 | 31 | 1 | 81 | 51 | Q | 113 | 71 | q |
| 50 | 32 | 2 | 82 | 52 | R | 114 | 72 | r |
| 51 | 33 | 3 | 83 | 53 | S | 115 | 73 | s |
| 52 | 34 | 4 | 84 | 54 | T | 116 | 74 | t |
| 53 | 35 | 5 | 85 | 55 | U | 117 | 75 | u |
| 54 | 36 | 6 | 86 | 56 | V | 118 | 76 | v |
| 55 | 37 | 7 | 87 | 57 | W | 119 | 77 | w |
| 56 | 38 | 8 | 88 | 58 | X | 120 | 78 | x |
| 57 | 39 | 9 | 89 | 59 | Y | 121 | 79 | y |
| 58 | 3A | : | 90 | 5A | Z | 122 | 7A | z |
| 59 | 3B | ; | 91 | 5B | [ | 123 | 7B | { |
| 60 | 3C | < | 92 | 5C | \ | 124 | 7C | \| |
| 61 | 3D | = | 93 | 5D | ] | 125 | 7D | } |
| 62 | 3E | > | 94 | 5E | ^ | 126 | 7E | ~ |
| 63 | 3F | ? | 95 | 5F | _ | | | |

---

## 13. FÓRMULAS E EQUAÇÕES

### Cálculo de Checksum (XMODEM)

```
checksum = Σ(bytes) mod 256
```

### CRC-16-CCITT

```
Polinômio: x¹⁶ + x¹² + x⁵ + 1 (0x1021)
Valor inicial: 0x0000 ou 0xFFFF
```

### Entropia Máxima

```
H_max = log₂(n)
```
Onde n = número de símbolos possíveis (256 para bytes)

### Conversão de Bases

```
Decimal → Binário: divisões sucessivas por 2
Decimal → Hex: divisões sucessivas por 16
Binário → Hex: grupos de 4 bits
```

### Offset de Instruções x86

```
Endereço_Destino = Endereço_Próxima_Instrução + Offset_Relativo
```

### Cálculo de Tamanho UTF-8

```
Se byte & 0x80 == 0: 1 byte (ASCII)
Se byte & 0xE0 == 0xC0: 2 bytes
Se byte & 0xF0 == 0xE0: 3 bytes
Se byte & 0xF8 == 0xF0: 4 bytes
```

---

*Documento consolidado a partir da Enciclopédia de Símbolos Computacionais*
*Contém apenas dados técnicos: tabelas, equações e especificações*
