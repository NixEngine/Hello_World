# Framework Técnico Extremo: Samsung Galaxy Note20 Ultra 5G (SM-N986B, Exynos 990)

**Especificações do Modelo:** Exynos 990 (S5E9830), Mali-G77 MP11, Shannon 5123 Modem.

Este documento contém uma pesquisa absurdamente extensa e profunda sobre camadas de baixo nível, boot, eFuses, TrustZone, firmwares proprietários, USB-C e TODAS as vulnerabilidades e exploits conhecidos. Foco exclusivo em conteúdo técnico, físico, matemático e de programação.

## BootROM Exynos 990

# Pesquisa Técnica: Samsung Exynos 990 (S5E9830) BootROM e Cadeia de Boot

## 1. Visão Geral da Arquitetura de Boot do Exynos 990

O Samsung Exynos 990 (S5E9830), utilizado na linha Galaxy S20 e Note20 (ex: SM-N986B), implementa uma cadeia de boot segura (Secure Boot) baseada em múltiplos estágios de verificação criptográfica. A arquitetura de segurança é fundamentada na TrustZone da ARM e em componentes de hardware dedicados, como eFuses e o Knox Vault Processor.

A cadeia de boot segue o fluxo padrão:
1. **BootROM (BL0)**: Código imutável gravado em mask ROM.
2. **BL1**: Primeiro bootloader assinado, carregado na SRAM interna.
3. **BL2 (sboot.img)**: Samsung Secure Boot, inicializa a DRAM e configura a TrustZone.
4. **BL31**: ARM Trusted Firmware (ATF) / EL3 Secure Monitor.
5. **BL33**: Little Kernel (LK) / HLOS bootloader.

### 1.1. BootROM (BL0)
O BootROM é o primeiro código executado após o *power-on-reset*. Suas principais responsabilidades incluem:
- Inicialização mínima do hardware (SRAM interna).
- Leitura dos eFuses para determinar a configuração de boot (ex: chaves públicas, estado do Secure Boot, status de garantia/Knox).
- Carregamento do BL1 a partir da mídia de armazenamento (UFS) ou via USB (Emergency Download Mode).
- Verificação da assinatura criptográfica do BL1 (RSA-2048/SHA-256).

O endereço de execução inicial (reset vector) em arquiteturas ARMv8 (AArch64) geralmente é `0x00000000` ou `0xFFFF0000`, dependendo da configuração do pino `VINITHI`. No Exynos 990, o BootROM mapeia a SRAM interna em endereços específicos, como `0x02020000` a `0x02070000` [1].

### 1.2. Cadeia de Confiança (Chain of Trust)
A cadeia de confiança é estabelecida através da verificação de assinaturas em cada estágio:
- O **BootROM** verifica o **BL1** usando a chave pública cujo hash (SHA-256) está gravado nos eFuses.
- O **BL1** verifica o **BL2 (sboot)**.
- O **BL2** verifica os componentes subsequentes, como **BL31 (ATF)**, **TZSW (TrustZone Software)** e **LDFW**.

Se qualquer verificação falhar, o dispositivo entra em um estado de erro ou tenta o boot via USB (EUB - Exynos USB Boot).

## 2. Vulnerabilidades e Exploits no BootROM

### 2.1. CVE-2020-10850 / CVE-2020-10546: Exynos BootROM USB Download (USBDL) Exploit
Descoberto por Frederic Basse, este exploit afeta o modo de download USB do BootROM em vários chipsets Exynos (incluindo 8890, 8895 e variantes) [1]. Embora a documentação inicial foque em chips mais antigos, a classe de vulnerabilidade inspirou pesquisas em chips mais recentes.

**Detalhes Técnicos:**
- **Componente:** BootROM USB Stack.
- **Tipo:** Integer Overflow / Buffer Overflow.
- **Mecanismo:** O BootROM recebe dados via USB em uma estrutura `dldata`:
  ```c
  typedef struct dldata_s {
      u_int32_t unknown0;
      u_int32_t size; // header(8) + data(n) + footer(2)
      u_int8_t  data[n];
      u_int16_t unknown1;
  } dldata;
  ```
- O BootROM verifica se os dados cabem no buffer `dl_buf` (localizado em `0x02021800` a `0x02070000`):
  ```c
  if (dl_buf + dldata.size >= 0x02070000) {
      usb_download_status = 0x02; // error
  }
  ```
- **O Bug:** A verificação de 32 bits é vulnerável a um *integer overflow*. Se `dldata.size` for maior que `0xFDFDE7FF`, a soma `dl_buf + dldata.size` transborda, passando na verificação.
- **Exploração:** O atacante envia transferências USB vazias para incrementar o ponteiro `dl_buf` sem escrever dados (evitando *page faults*), até atingir um endereço alvo. A última transferência sobrescreve estruturas de dados (ex: ponteiros de função ou a pilha) na faixa `0x0` a `0x020217FF`, alcançando execução de código arbitrário (RCE) no Secure World (EL3) [1].

### 2.2. CVE-2024-56426: Unified Exynos 990 BootROM Exploit
Um exploit mais recente e específico para a família Exynos 990 (Galaxy S20, Note20) foi publicado sob o CVE-2024-56426 [2].

**Detalhes Técnicos:**
- **Vetor:** Exploração da cadeia de boot via modificação do `sboot.bin`.
- **Mecanismo:** O exploit substitui o `sboot.bin.lz4` original por uma imagem descompactada, forçando o dispositivo a falhar no boot normal e entrar no modo BootROM/EUB (Emergency USB Boot).
- **Execução:** Uma vez no modo EUB (USB VID:PID `04e8:1234`), o exploit envia um payload (`Exynos990_boot_custom_key.bin`) e redireciona a execução para o endereço `0x02022000` na SRAM.
- **Impacto:** Permite o carregamento de um bootloader assinado com uma chave customizada, contornando o Secure Boot. O exploit também inclui a capacidade de realizar um dump completo do BootROM (`exynos990.bootrom.bin`) [2].

## 3. Vulnerabilidades no Kernel e Drivers (Exynos 990)

### 3.1. CVE-2021-25467 / CVE-2021-25475: Vision DSP Kernel Driver LPE
Descoberto pela Taszk Security Labs, trata-se de vulnerabilidades no driver do Vision DSP (`/dev/dsp`) do Exynos 990 [3][4].

**Detalhes Técnicos (CVE-2021-25467 - OOB Write via Integer Overflow):**
- **Componente:** Processamento de arquivos ELF no driver DSP.
- **Tipo:** Integer Overflow resultando em Out-of-Bounds (OOB) Write.
- **Mecanismo:** A função `__dsp_elf32_get_section_list_size` calcula o tamanho total das seções de memória. O tamanho é armazenado em uma variável de 4 bytes, permitindo um *integer overflow* durante a soma dos tamanhos das seções (`sec->sh_size`).
- **Impacto:** O tamanho alocado para a memória do dispositivo é menor que o necessário. Durante a cópia dos dados (`__dsp_lib_manager_load_sec`), ocorre um *buffer overflow* na memória virtual do kernel mapeada para o dispositivo, permitindo LPE (Local Privilege Escalation) [3].

**Detalhes Técnicos (CVE-2021-25475 - Vmalloc OOB Write no Linker):**
- **Componente:** Linker do driver DSP (`dsp_linker_link_libs`).
- **Tipo:** Out-of-Bounds Write.
- **Mecanismo:** Falta de validação de limites ao processar cabeçalhos de relocação ELF. A função `__rela_relocation` usa o campo `r_info` não sanitizado como índice de array. A função `__relocate` escreve o valor de relocação em um offset controlado pelo atacante.
- **Impacto:** Escrita arbitrária na região `vmalloc` do kernel. Pode ser usado para sobrescrever pilhas do kernel e obter execução de código arbitrário no kernel (LPE) [4].

### 3.2. CVE-2021-25370: DPU Driver Use-After-Free
Parte de uma cadeia de exploits *in-the-wild* analisada pelo Google Project Zero [5].

**Detalhes Técnicos:**
- **Componente:** Display Processing Unit (DPU) driver, específico para Exynos.
- **Tipo:** Use-After-Free (UAF).
- **Impacto:** Usado em conjunto com o CVE-2021-25337 (Arbitrary File Read/Write no `SemClipboardProvider`) e CVE-2021-25369 (Kernel Info Leak via `sec_log`) para obter LPE e comprometer o dispositivo [5].

## 4. Baseband (Shannon) e Outros Componentes

### 4.1. Shannon Baseband Exploits
O Exynos 990 utiliza modems Shannon externos (ex: Exynos Modem 5123). Vulnerabilidades críticas foram encontradas nestes modems.

**CVE-2024-55568:**
- **Componente:** Componente UL2 do firmware do baseband Exynos.
- **Tipo:** NULL Pointer Dereference (CWE-476).
- **Mecanismo:** Falta de verificação de ponteiro NULL durante o processamento de pacotes do protocolo Mobility Management (MM). Um pacote MM malformado causa o travamento do processador baseband.
- **Impacto:** Denial of Service (DoS) remoto, resultando em perda de conectividade celular [6].

**CVE-2023-26073:**
- **Componente:** `NrmmMsgCodec` no baseband Shannon.
- **Tipo:** Buffer Overflow.
- **Impacto:** RCE no baseband [7].

## 5. eFuses, Knox e Glitching

### 5.1. Knox eFuses
O Samsung Knox utiliza eFuses de hardware (WARRANTY bit) para registrar permanentemente se o dispositivo executou código não assinado. Quando o bootloader é desbloqueado, uma alta voltagem é aplicada para queimar o fusível (alterando de `0x0` para `0x1`).

### 5.2. Técnicas de Glitching (Teoria)
Pesquisadores discutem a possibilidade de contornar a queima do eFuse Knox através de *Voltage Glitching* ou *Sustained Undervolting* [8].
- **Teoria:** Reduzir a tensão de alimentação (VCC) durante o comando `fastboot oem unlock`. A ideia é fornecer tensão suficiente para a CPU executar a instrução, mas insuficiente para o circuito de *charge pump* ou *boost converter* gerar a alta tensão necessária para queimar o eFuse fisicamente.
- **Desafios:** O Knox Vault Processor e os circuitos de eFuse operam de forma isolada e possuem proteções contra subtensão (Brown-out Detectors). Além disso, a alta tensão geralmente é gerada internamente no chip (ex: UFS/eMMC charge pumps), tornando a manipulação externa complexa [8].

## Referências
[1] Frederic Basse. "exynos-usbdl : unsigned code loader for Exynos BootROM". fredericb.info. https://fredericb.info/2020/06/exynos-usbdl-unsigned-code-loader-for-exynos-bootrom.html
[2] Creeeeger. "CVE-2024-56426/USER_GUIDE.md". GitHub. https://github.com/Creeeeger/CVE-2024-56426/blob/exynos990/USER_GUIDE.md
[3] Taszk Security Labs. "CVE-2021-25467: Kernel LPE in the Vision DSP Kernel Driver". https://labs.taszk.io/blog/post/62_ss_dsp_oob_write/
[4] Taszk Security Labs. "Kernel LPE in the Vision DSP Kernel Driver's ELF Linker". https://labs.taszk.io/blog/post/63_ss_dsp_oob_write_linker/
[5] Maddie Stone, Project Zero. "A Very Powerful Clipboard: Analysis of a Samsung in-the-wild exploit chain". https://projectzero.google/2022/11/a-very-powerful-clipboard-samsung-in-the-wild-exploit-chain.html
[6] ZeroPath. "Samsung Exynos Baseband NULL Pointer Dereference". https://zeropath.com/blog/cve-2024-55568-samsung-exynos-null-pointer-dereference
[7] SentinelOne. "CVE-2023-26073: Samsung Exynos Buffer Overflow Flaw". https://www.sentinelone.com/vulnerability-database/cve-2023-26073/
[8] XDA Developers. "[Theory] Knox eFuse Bypass via Sustained Undervolting during bootloader unlock". https://xdaforums.com/t/theory-knox-efuse-bypass-via-sustained-undervolting-during-bootloader-unlock.4736127/


## Samsung eFuses no Exynos 990

# Samsung eFuses no Exynos 990: Análise Técnica Profunda

## 1. Arquitetura de One-Time Programmable (OTP) Fuses no Exynos 990

O SoC Samsung Exynos 990 (SM-N986B) utiliza uma arquitetura de eFuses (Electronic Fuses) baseada em memória One-Time Programmable (OTP). O controlador OTP é a entidade de hardware responsável por gerenciar a leitura e a queima (programação) dos fuses de segurança e configuração do dispositivo [1].

Com base na análise do código-fonte do kernel Linux, especificamente no driver `exynos-chipid` e nas device trees `exynos990.dtsi`, o controlador OTP e o bloco ChipID no Exynos 990 estão mapeados em endereços de memória específicos [2]. O bloco ChipID (`samsung,exynos990-chipid`), que fornece informações sobre a revisão do hardware e o ID do produto, está localizado no endereço base `0x10000000` com um tamanho de `0x100` [3]. O controlador OTP principal (OTP_CON_TOP) está mapeado no endereço físico `0xE9830000` [4]. Durante a sequência de inicialização (power-on sequence), os valores do ChipID são carregados a partir dos registradores OTP para a memória [2].

A queima de um eFuse é um processo físico e estritamente irreversível. O controlador OTP aplica uma corrente elétrica de alta voltagem através de uma interface de hardware dedicada, o que funde um filamento metálico microscópico embutido no chip de silício [5]. No estado inicial lógico `0x0`, o filamento encontra-se intacto, permitindo a passagem de corrente e configurando um curto-circuito lógico. Quando o estado é alterado para `0x1`, o filamento é rompido pela alta corrente, criando um circuito aberto [6]. Devido a essa alteração física na estrutura do hardware, é fisicamente impossível reverter um eFuse do estado `0x1` de volta para `0x0` através de modificações de software [7].

A leitura do estado dos eFuses pode ser realizada através de interfaces de debug ou pelo próprio sistema operacional. No nível do kernel e do sistema de arquivos sysfs, o estado do Knox e de outros fuses pode ser lido através de propriedades do sistema exportadas pelo bootloader (S-Boot) via device tree ou ATAGs. Adicionalmente, o estado do Knox Warranty Bit pode ser consultado diretamente através de comandos AT enviados ao modem, especificamente utilizando o comando `AT+KSTATUS` [8].

## 2. Tipos de eFuses e Knox Warranty Void

A arquitetura de segurança da Samsung, conhecida como Knox, emprega múltiplos eFuses para rastrear de forma persistente o estado de integridade e segurança do dispositivo móvel [9].

O fuse mais proeminente e amplamente discutido é o `KNOX_WARRANTY_BIT`. Este eFuse é acionado e permanentemente alterado de `0x0` para `0x1` quando o bootloader detecta a execução de código não assinado criptograficamente pela Samsung [10]. Este acionamento ocorre tipicamente durante o processo de OEM Unlock, durante o flash de partições de firmware não-oficiais utilizando ferramentas como Odin ou Heimdall, ou quando ocorrem falhas na verificação de integridade da cadeia de boot (root detection) [11].

Quando o `KNOX_WARRANTY_BIT` é registrado como `0x1`, o ambiente de execução confiável (TrustZone/TEEgris) bloqueia irrevogavelmente o acesso a chaves criptográficas específicas baseadas em hardware [12]. Esta ação desativa permanentemente serviços do sistema que dependem de um ambiente de alta segurança. Os serviços afetados incluem o Samsung Pay, a Secure Folder (Pasta Segura), o Samsung Health, o Samsung Pass e as funcionalidades corporativas de Mobile Device Management (MDM) e Knox Workspace [13].

Além do Knox Warranty Bit principal, o sistema OTP contém diversos outros fuses dedicados a finalidades específicas de segurança e controle de inicialização. A tabela abaixo detalha os principais eFuses identificados na arquitetura:

| Nome do eFuse | Descrição Técnica e Funcionalidade |
| :--- | :--- |
| **KNOX_WARRANTY_BIT** | Indicador principal de violação de garantia e integridade do sistema. Desativa serviços seguros quando em `0x1`. |
| **CUSTOM_KERNEL_FUSE** | Registra permanentemente se um kernel Linux customizado ou não assinado foi inicializado no dispositivo. |
| **RKP_FUSE** | Relacionado ao status do Real-time Kernel Protection, o hypervisor responsável por proteger a integridade do kernel em tempo de execução. |
| **FRP_FUSE** | Armazena o status persistente do Factory Reset Protection, impedindo a redefinição não autorizada do dispositivo. |
| **SBL_FUSE** | Controla as políticas do Secure BootLoader, incluindo a revogação de chaves criptográficas do bootloader. |
| **WARRANTY_BIT_2** | Atua como um mecanismo de backup ou extensão do bit de garantia principal em determinadas revisões de hardware. |

## 3. Tentativas de Reset e Spoofing de eFuse

Devido à natureza física e destrutiva da queima dos eFuses, o reset de hardware para o estado original é uma impossibilidade técnica [7]. Para contornar as restrições impostas pelo Knox Warranty Bit acionado, pesquisadores de segurança e desenvolvedores da comunidade criaram técnicas avançadas de spoofing baseadas em software.

O KnoxPatch é a implementação mais notável desta técnica. Trata-se de um módulo desenvolvido para os frameworks Xposed e LSPosed que intercepta chamadas de API no nível do framework do Android para falsificar o status do Knox [14]. O mecanismo de ação do KnoxPatch envolve a alteração dinâmica do retorno de propriedades críticas do sistema, como `ro.boot.warranty_bit` e `ro.security.mdf.ux`. O módulo força essas propriedades a retornar o valor `0` (ou `0x0`) quando consultadas por aplicativos em execução no espaço de usuário (userland) [15].

Apesar de sua eficácia em contornar verificações em nível de software, o KnoxPatch possui limitações arquitetônicas severas. O módulo consegue enganar com sucesso aplicativos que dependem de verificações de software, como o Samsung Health e a Secure Folder. No entanto, ele é incapaz de restaurar a funcionalidade de serviços críticos como o Samsung Pay ou o Samsung Pass [16]. Estes serviços financeiros e de identidade dependem de atestação baseada em hardware fornecida diretamente pela TrustZone (TEEgris) e pelo StrongBox, que verificam o estado físico do eFuse no controlador OTP, ignorando completamente as falsificações feitas no framework do Android [17].

## 4. Relação com RPMB (Replay Protected Memory Block)

O Replay Protected Memory Block (RPMB) é uma partição de hardware especializada presente no armazenamento eMMC e UFS. Sua função primária é armazenar dados sensíveis de forma criptograficamente segura, protegendo-os contra ataques de repetição (replay attacks) [18].

A Samsung utiliza extensivamente a partição RPMB para armazenar contadores de versão de firmware (mecanismos Anti-Rollback) e configurações críticas de Secure Boot [19]. Todas as operações de leitura e escrita direcionadas ao RPMB devem ser obrigatoriamente autenticadas utilizando uma chave criptográfica simétrica, conhecida como RPMB Key [20].

Existe uma vinculação criptográfica profunda entre o RPMB e os eFuses do dispositivo. A chave de autenticação do RPMB é frequentemente derivada de um segredo mestre gravado de forma permanente em um eFuse (OTP) durante o processo de fabricação e provisionamento do SoC [21]. Se o eFuse correspondente for fisicamente alterado, ou se a placa-mãe for substituída sem o pareamento criptográfico correto do chip UFS, o processo de autenticação falha, bloqueando o acesso ao RPMB [22].

Vulnerabilidades na implementação do Trusted Execution Environment (como falhas no TEEgris) ou erros no manuseio das chaves do RPMB podem, teoricamente, permitir o bypass dos mecanismos de anti-rollback [23]. Em cenários de recuperação avançada, a limpeza forçada (erase) da partição RPMB via hardware (utilizando interfaces ISP ou JTAG) geralmente resulta no brick do dispositivo ou na desativação permanente dos recursos de segurança baseados em hardware [24]. Isso ocorre porque a chave de autenticação derivada do OTP não corresponderá mais aos dados ou à estrutura esperada dentro da partição RPMB limpa.

## 5. Vulnerabilidades e Exploits (CVEs)

A pesquisa de segurança focada no Exynos 990 revelou vulnerabilidades críticas que afetam os estágios iniciais de inicialização e a integridade dos eFuses.

A vulnerabilidade mais significativa documentada é a **CVE-2024-56426**, que descreve um exploit crítico no BootROM unificado dos SoCs Exynos 990 e Exynos 9830 [25]. Esta falha de segurança reside no código imutável do BootROM e está provavelmente relacionada a falhas de validação de memória durante a operação no modo de download USB de baixo nível (EUB - Exynos USB Booting) [26].

O impacto da CVE-2024-56426 é a Execução de Código Arbitrário (RCE/LPE) no nível mais alto de privilégio do hardware (BootROM). A exploração bem-sucedida permite o carregamento e a execução de payloads customizados (como o binário `Exynos990_boot_custom_key.bin`) muito antes da inicialização do S-Boot (o bootloader secundário da Samsung) [27].

Os detalhes técnicos da exploração revelam que o exploit unificado é capaz de mapear múltiplos modelos de dispositivos (incluindo as variantes G986B e N986B) e injetar código malicioso diretamente na memória IRAM. O endereço de carregamento (load address) alvo para o payload do estágio BL1 é `0x02022000` [28]. Ao obter execução de código neste estágio inicial, o atacante consegue contornar completamente a cadeia de confiança do Secure Boot, ignorar as rotinas de verificação de eFuses e executar bootloaders modificados (tampered loaders) [29]. Crucialmente, este sequestro da cadeia de boot ocorre antes que o S-Boot tenha a oportunidade de verificar assinaturas e acionar fisicamente o Knox Warranty Bit, permitindo a execução de código não assinado sem invalidar a garantia via hardware [30].

A extração de dados forenses e a análise profunda de eFuses e do RPMB em dispositivos Exynos 990 exigem acesso através de interfaces de debug de baixo nível. O modo EUB (Exynos USB Booting) é a interface primária utilizada por exploits como a CVE-2024-56426 para interagir diretamente com o BootROM [31]. Embora as interfaces de hardware JTAG sejam rotineiramente desativadas (fused off) em dispositivos de produção para evitar engenharia reversa, técnicas avançadas de injeção de falhas (fault injection), como o voltage glitching aplicado durante a inicialização do S-Boot, têm sido teorizadas como métodos viáveis para contornar a leitura do eFuse do Knox [32]. Adicionalmente, através da obtenção de execução de código no kernel (LPE) ou no TEE, um pesquisador pode mapear o endereço físico `0xE9830000` e ler os registradores brutos do controlador OTP, permitindo uma análise forense precisa do estado exato de todos os fuses de segurança do dispositivo [33].

## Referências

[1] Jongse Park et al., "TNPU: Supporting Trusted Execution with Tree-less", HPCA 2022.
[2] Tudor Ambarus, "[PATCH v3 5/6] soc: samsung: exynos-chipid: add google,gs101-otp support", Linux ARM Kernel Mailing List, Nov 2025.
[3] Igor Belwon, "[PATCH v2 5/6] arm64: dts: exynos", Linux Kernel Mailing List, Oct 2024.
[4] Igor Belwon, "[PATCH v3 4/6] soc: samsung: exynos-chipid: Add support for Exynos 990 chipid", Linux ARM Kernel Mailing List, Oct 2024.
[5] XDA Developers, "[RESEARCH] Samsung Knox: Warranty Void Behavior", Sep 2013.
[6] Chainfire, "More on KNOX warranty void", Oct 2013.
[7] SamsungTool.us, "Samsung Online Service Platform", Code-GSM.
[8] Samsung Knox Documentation, "Hardware-Backed Security | Fundamentals".
[9] D. Cerdeira et al., "SoK: Understanding the Prevailing Security Vulnerabilities in TrustZone-assisted TEE Systems", IEEE S&P 2020.
[10] Reddit r/samsung, "Knox 0x0 warranty reset", Jul 2024.
[11] Reddit r/androidroot, "How haven't I tripped knox?", Jul 2025.
[12] GlobalPlatform, "Certificate of Security Evaluation - Samsung TEEgris v4.1 on Exynos 990", Mar 2022.
[13] CSDN, "三星Galaxy深度定制：解锁Android潜能的高级Magisk应用指南", Jun 2026.
[14] XDA Developers, "[APP][XPOSED/MAGISK] KnoxPatch v0.7.5 - Restore Samsung Knox features", Feb 2023.
[15] CSDN, "三星设备Root后功能恢复框架：KnoxPatch高级实现指南", Jul 2026.
[16] Reddit r/galaxys10, "Knox tripped - any fix?", Jul 2024.
[17] Telegram Channel 𝐙𝐆𝐐 ɪɴᴄ., "KnoxPatch e TrickyStore".
[18] ResearchGate, "Mobile secure data protection using eMMC RPMB partition".
[19] Facebook, "Introduce the related functions of RPMB, how to write RPMB key and some common problems", Mar 2026.
[20] A. Fukami, "Exploiting RPMB authentication in a closed source TEE implementation", ScienceDirect, 2024.
[21] Keysight Technologies, "Breaking TEE Security Part 1: TEEs, TrustZone, and TEEGRIS", Feb 2021.
[22] XDA Developers, "{WIP} N950U Bootloader Unlocking (Build) / EDL Rom / SD-Card Booting", Oct 2018.
[23] Nebelwelt, "An Empirical Study of Trusted Application Rollback Prevention on Android", 2024.
[24] Facebook, "The final and permanent solution of dm verity corruption how to read RPMB key", Sep 2025.
[25] GitHub, "Creeeeger/CVE-2024-56426: Exynos 990 / Exynos9830 Unified BootROM Exploit".
[26] CISA, "Vulnerability Summary for the Week of September 9, 2024".
[27] GitHub, "Creeeeger/CVE-2024-56426 USER_GUIDE.md".
[28] GitHub, "Creeeeger/CVE-2024-56426 README.md".
[29] TeamT5, "BlackHat's Talk: Breaking Samsung's Root of Trust", Jun 2020.
[30] XDA Developers, "[Theory] Knox eFuse Bypass via Sustained Undervolting During Bootloader Unlock", May 2025.
[31] GitHub, "ExtremeXT/android_kernel_samsung_exynos990".
[32] Project Zero, "Trust Issues: Exploiting TrustZone TEEs", Jul 2017.
[33] D. Cerdeira, "Towards Trustworthy TrustZone-Assisted TEEs", PhD Thesis, 2024.


## Samsung TEEGRIS & TrustZone

# Pesquisa Técnica: Samsung TrustZone e TEEGRIS no Exynos 990

## 1. Arquitetura ARM TrustZone e Samsung TEEGRIS

A arquitetura ARM TrustZone fornece isolamento de hardware em todo o sistema, dividindo a CPU em dois mundos: o Normal World (NWd) e o Secure World (SWd). O Normal World executa o Rich Execution Environment (REE), como o Android, enquanto o Secure World executa o Trusted Execution Environment (TEE). A transição entre esses mundos é gerenciada pelo Secure Monitor, que opera no nível de privilégio mais alto (EL3) [1].

O Samsung TEEGRIS é o sistema operacional proprietário da Samsung para o TEE, introduzido a partir do Galaxy S10 (substituindo o Kinibi da Trustonic). O TEEGRIS kernel opera no nível de privilégio S-EL1 (Secure EL1), enquanto as Trusted Applications (TAs) operam no S-EL0 (Secure EL0) [2].

### 1.1 Níveis de Exceção (Exception Levels)

*   **EL0 / S-EL0:** Modo de usuário. No NWd, executa aplicativos Android. No SWd, executa as Trusted Applications (TAs) do TEEGRIS.
*   **EL1 / S-EL1:** Modo kernel. No NWd, executa o kernel Linux. No SWd, executa o kernel do TEEGRIS.
*   **EL2:** Hypervisor. No NWd, executa o Real-time Kernel Protection (RKP) da Samsung.
*   **EL3:** Secure Monitor. Sempre opera em modo seguro e gerencia a transição entre NWd e SWd através de instruções Secure Monitor Call (SMC) [2].

### 1.2 Componentes de Hardware

*   **TZASC (TrustZone Address Space Controller):** Define regiões seguras na memória DRAM. O TZASC intercepta acessos à memória e verifica permissões baseadas no bit NS (Non-Secure). No Exynos 990, existem múltiplos controladores TZASC (presumivelmente um por controlador DRAM), mapeados em endereços físicos específicos (ex: `0x1BC40000`, `0x1BD40000`, `0x1BE40000`, `0x1BF40000`) [3].
*   **TZPC (TrustZone Protection Controller):** Define regiões seguras na memória SRAM interna e configura periféricos como seguros ou não-seguros [2].

## 2. TEEGRIS Kernel e Trusted Applications (TAs)

O kernel do TEEGRIS, embora pequeno, não é um microkernel puro. Ele gerencia o isolamento entre as TAs e entre as TAs e o kernel. As TAs são binários que fornecem serviços seguros ao REE.

### 2.1 Trusted Applications Comuns

*   `keymaster_ta`: Gerenciamento de chaves criptográficas.
*   `gatekeeper_ta`: Autenticação de usuário (senhas, PINs).
*   `fingerprint_ta`: Processamento de dados biométricos.
*   `drm_ta` / `hdcp_ta`: Proteção de conteúdo digital (DRM/HDCP).
*   `weaver_ta`: Armazenamento seguro de tokens.

### 2.2 Interface SMC (Secure Monitor Call)

A comunicação entre o REE e o TEE é iniciada através da instrução SMC. O kernel Linux atua como proxy, expondo um driver que os aplicativos Android podem usar. Os parâmetros são passados nos registradores `X0-X7`. O registrador `X0` geralmente contém o SMC ID, que identifica o serviço solicitado [2].

### 2.3 Memória Compartilhada

Para compartilhar dados entre o REE e o TEE de forma eficiente, o Android utiliza o subsistema ION. Buffers ION (ex: `camera_heap` no endereço físico `0x99000000`) podem ser mapeados tanto no aplicativo Android quanto na TA, permitindo acesso direto à mesma memória física [3].

## 3. Mitigações de Segurança do Kernel (RKP, KDP, TIMA)

A Samsung implementa várias mitigações baseadas em hypervisor (EL2) para proteger o kernel Linux (EL1).

### 3.1 RKP (Real-time Kernel Protection)

O RKP é um hypervisor que opera em EL2. Ele utiliza a tradução de endereços de estágio 2 (Stage 2 Translation) para proteger a memória do kernel. O RKP intercepta operações críticas e impede que o kernel modifique suas próprias tabelas de páginas (Page Tables) de forma não autorizada [4].

### 3.2 KDP (Kernel Data Protection)

O KDP é uma solução de Data Flow Integrity (DFI) implementada pelo RKP. Ele torna estruturas de dados sensíveis do kernel (como tabelas de páginas, `struct cred`, `struct task_security_struct`, `struct vfsmount`, status do SELinux) somente leitura (read-only) a partir do EL1, impedindo ataques de escalonamento de privilégios que dependem da modificação dessas estruturas [4].

### 3.3 TIMA (TrustZone-based Integrity Measurement Architecture)

O TIMA fornece medição de integridade e proteção em tempo real, trabalhando em conjunto com o Secure Boot e a arquitetura TrustZone para garantir que o kernel não foi comprometido [5].

## 4. Vulnerabilidades e Exploits no TEEGRIS

A pesquisa revelou várias vulnerabilidades críticas no TEEGRIS, permitindo execução arbitrária de código e escalonamento de privilégios.

### 4.1 CVE-2019-16253 (SamsungTTS Privilege Escalation)

*   **Componente:** Aplicativo Text-to-speech Engine (SamsungTTS).
*   **Tipo:** Escalonamento de privilégios locais.
*   **Impacto:** Permite que um atacante local escale privilégios para o nível de aplicativo de sistema sem requerer permissões adicionais [6].

### 4.2 CVE-2020-25279 (Baseband Buffer Overflow)

*   **Componente:** Componente Baseband em chipsets Exynos (incluindo dispositivos com TEEGRIS).
*   **Tipo:** Buffer Overflow.
*   **Impacto:** Execução de código devido a uma mensagem SETUP anormal. CVSS 9.8 (Crítico) [7].

### 4.3 SVE-2019-15873 (Widevine DRM TA Arbitrary Read/Write)

*   **Componente:** Widevine DRM Trustlet (`WVDRM`).
*   **Tipo:** Leitura/Escrita arbitrária de memória.
*   **Impacto:** Permite escalonamento de privilégios no REE a partir do TEE [8].

### 4.4 SVE-2019-14847 / CVE-2019-20583 (EXT_FR Trustlet Type Confusion)

*   **Componente:** `EXT_FR` Trustlet.
*   **Tipo:** Type Confusion.
*   **Impacto:** Execução arbitrária de código no contexto da TA [9].

### 4.5 Exploração de Mapeamento Físico (HDCP TA)

Pesquisadores da Keysight demonstraram uma técnica de escalonamento de privilégios explorando o driver `phys://` exposto pelo kernel do TEEGRIS. TAs altamente privilegiadas (grupo `samsung_drv`), como a HDCP TA, podem usar a chamada de sistema `mmap` para mapear memória física.

*   **Vulnerabilidade:** Falta de restrições adequadas no mapeamento de registradores físicos.
*   **Exploit:**
    1.  Obter controle de execução na HDCP TA (via buffer overflow na pilha).
    2.  Criar um payload ROP para abrir o driver `phys://` e mapear registradores físicos (como o TZASC) e memória não segura (ION buffer).
    3.  Usar um gadget ROP de `memcpy` para copiar o conteúdo dos registradores TZASC para o buffer ION, permitindo a leitura a partir do Android.
    4.  Modificar os registradores TZASC para desproteger a memória do TEE, permitindo acesso total de leitura/escrita a partir do REE [3].

## Referências

[1] Quarkslab. "A Deep Dive Into Samsung's TrustZone (Part 1)". https://blog.quarkslab.com/a-deep-dive-into-samsungs-trustzone-part-1.html
[2] Keysight. "Breaking TEE Security Part 1: TEEs, TrustZone, and TEEGRIS". https://www.keysight.com/blogs/en/tech/nwvs/2021/02/23/breaking-tee-security-part-1
[3] Keysight. "Breaking TEE Security Part 3: Escalating Privileges". https://www.keysight.com/blogs/en/tech/nwvs/2021/03/30/breaking-tee-security-part-3
[4] Impalabs. "A Samsung RKP Compendium". https://blog.impalabs.com/2101_samsung-rkp-compendium.html
[5] Samsung. "Samsung Trusted Boot and TrustZone Integrity Management Explained". https://insights.samsung.com/2019/09/04/samsung-trusted-boot-and-trustzone-integrity-management-explained/
[6] NVD. "CVE-2019-16253 Detail". https://nvd.nist.gov/vuln/detail/CVE-2019-16253
[7] NVD. "CVE-2020-25279 Detail". https://nvd.nist.gov/vuln/detail/CVE-2020-25279
[8] Twizzyindy. "Learning from the old Exynos Trustlet bug". https://twizzyindy.github.io/android/exynos/2026/01/06/learning-exynos-trustlet-en.html
[9] NVD. "CVE-2019-20583 Detail". https://nvd.nist.gov/vuln/detail/CVE-2019-20583


## Shannon 5123 Exploits

# Pesquisa Técnica Exaustiva: Samsung Shannon 5123 Modem & Shannon OS

## 1. Arquitetura de Hardware e Especificações do Modem Shannon 5123 (S5T5123)

O Samsung Shannon 5123, também conhecido como Exynos Modem 5123, é um processador baseband (Cellular Processor - CP) utilizado em conjunto com os SoCs Exynos 990 e Exynos 2100. Este componente está presente em dispositivos de alto desempenho, como a série Galaxy S20, Note20 Ultra 5G (SM-N986B) e a família Google Pixel 6, onde atua como o baseband do chip Tensor G1. Diferente das gerações anteriores que utilizavam a arquitetura Cortex-R7, o Shannon 5123 marca uma transição significativa para a arquitetura **ARM Cortex-A**, especificamente o Cortex-A55. Para manter a compatibilidade com o ecossistema legado do Shannon OS, o processador opera em modo de execução AArch32, utilizando o conjunto de instruções ARMv8-A em 32-bits. A velocidade de clock varia entre aproximadamente 1.2 GHz e 2.0 GHz, dependendo do estado de energia do dispositivo.

Em termos de memória física, o modem possui acesso a uma porção dedicada de DRAM, frequentemente empacotada em uma configuração Package on Package (PoP). Um exemplo comum é o módulo K3LK3K30EM-BGCN de 8 GB LPDDR5, onde uma região específica é estritamente reservada para o CP. Além disso, o chip conta com memória SRAM interna, conhecida como Tightly Coupled Memory (TCM), projetada para operações que exigem baixíssima latência. A interface de rádio é conectada a um Intermediate Frequency / Radio Frequency IC (IF RFIC), garantindo suporte abrangente tanto para redes sub-6GHz quanto para ondas milimétricas (mmWave).

O mapa de memória do baseband é configurado através da Memory Protection Unit (MPU) durante a fase do bootloader, antes de transferir a execução para o sistema operacional de tempo real. O firmware principal, contido no arquivo `modem.bin`, é tipicamente carregado no endereço físico `0x40010000` ou `0x40000000`, mapeado diretamente na RAM do CP. O arquivo de firmware inicia com uma Table of Contents (TOC) de 192 bytes, que contém estruturas de 32 bytes definindo as diversas seções, como Boot, Main e NVRAM. A seção "Main" geralmente se encontra no offset `0x2420` e possui um tamanho que varia entre 40MB e 60MB.

| Região de Memória | Endereço Base | Descrição |
| :--- | :--- | :--- |
| Código Executável | `0x40010000` a `0x43FFFFFF` | Contém o código Text/RO e as strings de debug utilizadas pelo sistema. |
| Dados e Heap | `0x44000000` em diante | Abriga as regiões de dados (RW), BSS, o Heap do sistema e as Stacks das tasks. |
| MMIO Peripherals | `0x80000000` em diante | Mapeamento de periféricos de hardware, controle de timers, interrupções (GIC) e engines de criptografia. |
| Shared Memory (SHM) | Variável | Região de memória compartilhada com o Application Processor (AP) para o protocolo IPC. |

## 2. Shannon OS: O RTOS Proprietário

O Shannon OS é o sistema operacional de tempo real (RTOS) proprietário desenvolvido pela Samsung para gerenciar as operações críticas do modem. A arquitetura do sistema é baseada em um agendador de tarefas estático (task-based scheduler). O sistema é composto por dezenas de tasks independentes, cada uma responsável por uma camada ou protocolo específico, como Mobility Management (MM), Radio Resource Control (RRC), Call Control (CC) e Layer 2 (MAC/RLC/PDCP). Cada task possui um Task Control Block (TCB) que armazena informações vitais, incluindo o stack pointer, a prioridade de execução, o estado atual e a fila de mensagens (mailbox). Uma tabela global no firmware, denominada `SYM_TASK_LIST`, contém os ponteiros para os entry points de todas as tasks. Durante a execução, as tasks operam em um loop infinito, aguardando a chegada de mensagens em suas respectivas filas. O processamento dessas mensagens é realizado através de tabelas de despacho (dispatch tables), que direcionam o fluxo de execução com base no ID da mensagem recebida.

O gerenciamento de memória dinâmica no Shannon OS é realizado por um alocador front-end conhecido como `mid4`. Este componente utiliza uma abordagem baseada em pools (pool-based allocator) para garantir alocações rápidas e determinísticas, essenciais em um ambiente de tempo real. Cada bloco de memória alocado (chunk) possui um cabeçalho inline de 32 bytes. Este cabeçalho contém ponteiros `next` e `prev` para o gerenciamento de free lists, além de campos para `size` e `flags`. Um elemento crucial de segurança neste cabeçalho é a presença de um **Guard Value fixo de `0xAA` bytes**, utilizado para a detecção básica de corrupção de memória. Os tamanhos dos slots do pool são organizados em potências de 2, variando de 32 a 2048 bytes.

Em termos de mitigações de segurança, as versões mais recentes do Shannon OS, como as encontradas nos dispositivos S20 e Note20, introduziram verificações de integridade no heap (heap sanitizers). Estes mecanismos abortam imediatamente a execução do sistema caso detectem qualquer alteração no guard value `0xAA`. Historicamente, proteções padrão da indústria como Address Space Layout Randomization (ASLR) e Stack Canaries estiveram ausentes ou foram implementadas de forma ineficaz nas versões mais antigas do RTOS. No entanto, com a introdução do Shannon 5123, a Samsung começou a implementar técnicas de hardening baseadas na MPU para restringir o acesso a regiões críticas de memória.

## 3. Comunicação Inter-Processadores: Protocolo Samsung IPC (SIPC)

A comunicação entre o Application Processor (AP), que executa o sistema operacional Android ou Linux, e o Cellular Processor (CP), que executa o Shannon OS, é realizada através do protocolo proprietário Samsung IPC (SIPC). Em nível de hardware, esta comunicação utiliza uma região de Shared Memory (SHM) e um sistema de interrupções baseado em Mailbox através de um barramento de hardware dedicado. No lado do AP, o daemon `cbd` (Cellular Boot Daemon) é o componente responsável por carregar o firmware do modem a partir da partição `/dev/block/by-name/radio` ou `CP`, mapear a memória necessária e inicializar a interface SIPC. A lógica detalhada do protocolo é implementada e gerenciada pela biblioteca `libsamsung-ipc`.

O formato das mensagens SIPC é estruturado para garantir a entrega eficiente de comandos e dados entre os processadores. O cabeçalho da mensagem contém campos essenciais como o `service_id`, que identifica o subsistema alvo (por exemplo, SIM, NET, CALL, SMS, GPS, MISC, SND), o `command_id`, o `length` do payload e um `sequence_number` para rastreamento. O payload subsequente contém os dados específicos exigidos pelo comando. Além da comunicação padrão, existe uma camada de abstração que permite o envio de comandos brutos, como comandos AT ou instruções de diagnóstico, através de uma interface serial virtual multiplexada sobre o SIPC. Esta interface é frequentemente acessada por engenheiros e pesquisadores através do Service Mode do dispositivo, utilizando o código de discagem `*#9900#`.

## 4. Vulnerabilidades, CVEs e Exploits no Shannon 5123

A complexidade inerente ao parsing de protocolos celulares legados e modernos, como ASN.1 e CSN.1, dentro do Shannon OS tem se provado uma fonte rica de vulnerabilidades de corrupção de memória. Estas falhas frequentemente culminam na criação de cadeias de exploração que permitem Remote Code Execution (RCE) over-the-air (OTA), representando um risco crítico para a segurança dos dispositivos.

Em março de 2023, a equipe do Google Project Zero revelou a descoberta de 18 vulnerabilidades 0-day nos modems Exynos. Destas, quatro foram classificadas como críticas por permitirem **Internet-to-baseband RCE** sem qualquer necessidade de interação do usuário (Zero-click). Para realizar o ataque, o adversário necessita apenas conhecer o número de telefone da vítima. A vulnerabilidade **CVE-2023-24033** é um exemplo proeminente desta classe, consistindo em uma falha crítica de RCE que ocorre durante o processamento do Session Description Protocol (SDP) na fase de configuração de chamadas. A corrupção de memória é desencadeada ao processar atributos específicos, como `accept-type` ou `chatroom`, em pacotes malformados recebidos via VoLTE ou Wi-Fi Calling. As vulnerabilidades **CVE-2023-26496**, **CVE-2023-26497** e **CVE-2023-26498** complementam este grupo, todas relacionadas a falhas no parsing de protocolos de chamada que resultam na execução arbitrária de código no nível do baseband. Como medida de mitigação temporária antes da aplicação do Security Maintenance Release (SMR) de março de 2023, recomendou-se a desativação do VoLTE e do Wi-Fi Calling.

Pesquisadores da Taszk Labs conduziram uma análise profunda na camada 2 (Radio Link Control - RLC) do baseband Exynos, focando especificamente nos procedimentos de segmentação e remontagem (re-assembly) de Protocol Data Units (PDUs). Esta pesquisa resultou na descoberta de vulnerabilidades críticas de corrupção de memória. A **CVE-2023-41111** representa uma combinação de um bug lógico e um acesso Out-Of-Bounds (OOB). Esta falha permite que um atacante transborde o array utilizado pelo código RLC da Samsung para armazenar descritores de fragmentos de dados LLC antes do processo de remontagem. A **CVE-2023-41112** é um Heap-based Buffer Overflow que ocorre durante o próprio procedimento de remontagem. A causa raiz é um erro clássico de programação em loops de cópia, onde a cópia dos dados é realizada antes da verificação da condição de saída. A primitiva de exploração deste heap overflow é altamente controlável: o atacante pode definir o tamanho da alocação (até 1560 bytes), controlar os valores escritos no payload do overflow e determinar o comprimento exato do transbordamento, limitado apenas pelo tamanho máximo de um frame de dados RLC. O chunk corrompido é liberado imediatamente após a cópia, resultando em RCE over-the-air através da injeção de frames L2 malformados a partir de uma rogue base station (Fake BTS).

| CVE ID | Componente Afetado | Tipo de Vulnerabilidade | Impacto | Vetor de Ataque |
| :--- | :--- | :--- | :--- | :--- |
| CVE-2023-24033 | Processamento SDP (VoLTE/Wi-Fi Calling) | Corrupção de Memória | RCE (Zero-click) | Internet-to-baseband |
| CVE-2023-41111 | Camada 2 (RLC) - Remontagem LLC | Lógico / Out-Of-Bounds (OOB) | RCE | Over-the-air (Rogue BTS) |
| CVE-2023-41112 | Camada 2 (RLC) - Remontagem LLC | Heap-based Buffer Overflow | RCE | Over-the-air (Rogue BTS) |
| CVE-2023-26073 | NrmmMsgCodec (5G MM) | Heap-based Buffer Overflow | RCE | Over-the-air (Rogue BTS) |
| CVE-2024-55568 | Componente UL2 (Processamento MM) | NULL Pointer Dereference | DoS / Crash | Over-the-air (Rogue BTS) |

O parsing de mensagens Non-Access Stratum (NAS) também apresenta falhas significativas. A **CVE-2023-26073** descreve um Heap-based Buffer Overflow no componente `NrmmMsgCodec`, responsável pelo Mobility Management (5G MM). A vulnerabilidade é causada pela validação insuficiente dos parâmetros de comprimento ao decodificar a lista estendida de números de emergência em mensagens 5G NAS. A função de decodificação aloca um buffer no heap com base em parâmetros esperados, mas falha em validar o comprimento real dos dados antes de executar a operação `memcpy`, permitindo RCE a partir de uma rogue BTS. Adicionalmente, a **CVE-2024-55568** identifica um NULL Pointer Dereference no componente UL2 durante o processamento de pacotes MM. A ausência de uma verificação de ponteiro nulo ao processar um pacote malformado resulta em Denial of Service (DoS), causando o crash do baseband e a consequente perda de conectividade celular.

## 5. Análise Estática e Ferramentas de Engenharia Reversa

A engenharia reversa do firmware Shannon (`modem.bin`) é uma tarefa complexa que tem sido imensamente facilitada pelo desenvolvimento de ferramentas especializadas pela comunidade de pesquisa em segurança. O **ShannonLoader** é um plugin essencial para o framework Ghidra, desenvolvido por Grant Hernandez como parte do projeto FirmWire. Esta ferramenta é capaz de carregar o binário bruto, resolver a tabela MPU para mapear as regiões de memória corretamente e processar as `TraceEntries` (strings de debug embutidas no código) para renomear funções automaticamente, acelerando drasticamente o processo de análise estática.

Para a análise dinâmica, o **FirmWire** se destaca como uma plataforma de emulação full-system baseada no QEMU/PANDA. Esta ferramenta permite a emulação completa do Shannon OS, possibilitando a injeção de fuzzers avançados como o AFL para a descoberta automatizada de vulnerabilidades. No caso específico do Shannon 5123, que utiliza a arquitetura Cortex-A55, a emulação apresenta desafios adicionais. Requer uma configuração customizada para iniciar o emulador QEMU no nível de exceção AArch64 EL3 e, em seguida, realizar um downgrade forçado para AArch32 EL1 (Secure System mode) através da injeção de código assembly, uma vez que o código executável do baseband é compilado em 32-bits. Complementando este ecossistema, o conjunto de scripts **shannonRE**, desenvolvido pela Comsecuris para o IDA Pro, oferece utilitários valiosos para identificar funções não documentadas, mapear registradores de hardware, analisar a estrutura dos stackframes e extrair a lista completa de tasks ativas no RTOS.


## Shannon 5123 Exploits

# Pesquisa Técnica: Samsung Shannon 5123 - Vulnerabilidades e Exploits

## 1. Arquitetura e Superfície de Ataque do Shannon 5123

O Shannon 5123 é um modem baseband 5G, formalmente conhecido como Exynos Modem 5123, integrado em chipsets como o Exynos 990, que equipa o Samsung Galaxy Note20 Ultra 5G (SM-N986B). A arquitetura do core deste baseband baseia-se em processadores ARM Cortex-A, marcando uma evolução em relação aos antigos Cortex-R utilizados em gerações anteriores. O sistema opera sob um Real-Time Operating System (RTOS) proprietário desenvolvido pela Samsung, que gerencia as complexas pilhas de protocolos de comunicação celular de forma isolada do Application Processor (AP).

A principal superfície de ataque deste componente é a interface de rádio (Over-the-Air - OTA) operando nas redes 4G e 5G. Uma característica crítica desta arquitetura é que não há necessidade de interceptação Man-in-the-Middle (MitM) para ataques em redes Sub-6. Isso permite a exploração remota (Internet-to-baseband) bastando que o atacante conheça o número de telefone da vítima. A comunicação interna entre o baseband e o AP é realizada através de memória compartilhada (PCIe/shmem) e interfaces de driver no kernel do sistema operacional Android, como o daemon `rild` e o dispositivo `/dev/umts_ramdump`.

## 2. Vulnerabilidades Críticas (Project Zero)

Em 2023, o Google Project Zero revelou uma série de vulnerabilidades críticas afetando os modems Exynos, com destaque para falhas que permitiam a execução remota de código sem interação do usuário.

A vulnerabilidade mais severa é o **CVE-2023-24033**, que afeta o módulo SDP (Session Description Protocol) dentro da pilha IMS/VoLTE. Trata-se de uma corrupção de memória causada por um buffer overflow durante o parsing do atributo `accept-type` em mensagens SIP INVITE. A ausência de validação adequada de formato e tamanho ao processar este atributo, bem como variantes como `fmtp` e `chatroom`, resulta na corrupção de estruturas de controle no heap do baseband. O impacto é a execução remota de código (RCE) no nível do baseband de forma zero-click. A exploração envolve o envio de uma mensagem SIP INVITE maliciosa através da rede IMS (VoLTE ou Wi-Fi Calling), manipulando o parsing do SDP para sobrescrever a memória.

Outro conjunto de vulnerabilidades inclui os **CVE-2023-26072, CVE-2023-26073, CVE-2023-26074, CVE-2023-26075 e CVE-2023-26076**. Estas falhas residem na implementação do protocolo 5G MM (Mobility Management), especificamente no módulo `NrmmMsgCodec`. O CVE-2023-26072, por exemplo, é um heap-based buffer overflow que ocorre devido à validação insuficiente de parâmetros ao decodificar a lista de números de emergência (Emergency number list) em mensagens NAS. O CVE-2023-26075 é classificado como um intra-object overflow no mesmo módulo. O impacto varia entre RCE e Denial of Service (DoS), porém a exploração exige uma estação base maliciosa (Rogue BTS) ou acesso local, elevando a complexidade do ataque em comparação ao CVE-2023-24033.

Adicionalmente, o baseband Shannon possui um histórico de vulnerabilidades de stack buffer overflow, como o **CVE-2024-25365**, que afeta o EMM (EPS Mobility Management) message handler. Falhas semelhantes foram documentadas em parsers de mensagens NAS/GMM, como GMM ATTACH ACCEPT e P-TMSI REALLOCATION COMMAND, bem como no parser XML interno do baseband, permitindo RCE via OTA.

| CVE ID | Componente Afetado | Tipo de Vulnerabilidade | Impacto | Vetor de Ataque |
|---|---|---|---|---|
| CVE-2023-24033 | Módulo SDP (IMS/VoLTE) | Memory Corruption / Buffer Overflow | RCE (Zero-click) | SIP INVITE via VoLTE/Wi-Fi Calling |
| CVE-2023-26072 | NrmmMsgCodec (5G MM) | Heap-based Buffer Overflow | RCE / DoS | Mensagens NAS (Rogue BTS) |
| CVE-2023-26075 | NrmmMsgCodec (5G MM) | Intra-object Overflow | RCE / DoS | Mensagens NAS (Rogue BTS) |
| CVE-2024-25365 | EMM Message Handler | Stack Buffer Overflow | RCE | Mensagens OTA |

## 3. Técnicas de Exploração e Mitigações

O layout de memória e as mitigações de segurança do Shannon baseband evoluíram significativamente ao longo dos anos. Historicamente, o firmware não implementava Address Space Layout Randomization (ASLR) ou Position Independent Executable (PIE), o que facilitava a exploração. Versões mais recentes introduziram ASLR parcial e randomização de heap. Da mesma forma, Stack Canaries (ou Stack Cookies) estavam ausentes nas primeiras versões, mas foram incorporados em firmwares lançados após 2023 para mitigar stack buffer overflows. A proteção Data Execution Prevention (DEP/NX) é implementada através da Memory Protection Unit (MPU) ou Memory Management Unit (MMU) nos cores Cortex-A, utilizando a região XN (eXecute Never) para impedir a execução direta de shellcode no stack ou heap.

Para contornar essas mitigações, os atacantes desenvolveram técnicas sofisticadas. O Heap Spray é frequentemente utilizado através de mensagens RRC ou NAS para preencher o heap com dados controlados, facilitando a exploração de vulnerabilidades Use-After-Free (UAF) ou Heap Overflows. Devido à presença do DEP/NX, os exploits dependem de Return-Oriented Programming (ROP), construindo cadeias de execução (ROP chains) com gadgets extraídos do próprio firmware do baseband. A ausência histórica de ASLR permitia o uso de endereços fixos (hardcoded) para esses gadgets.

Em firmwares modernos que implementam ASLR, os atacantes necessitam de técnicas de ASLR Bypass. Isso geralmente é alcançado através de vulnerabilidades de memory leak (info leak), como leituras fora de limites em mensagens de resposta, que permitem vazar endereços de memória. Com esses endereços, é possível calcular o endereço base do firmware e ajustar dinamicamente a ROP chain. Curiosamente, o firmware do Shannon contém mais de 150.000 strings de debug. Estas mensagens são inestimáveis para a engenharia reversa e, em cenários específicos, podem ser exploradas para facilitar o vazamento de informações.

## 4. Ferramentas de Pesquisa e Debug

A comunidade de pesquisa de segurança desenvolveu diversas ferramentas para analisar o Shannon baseband. Plugins como ShannonRE e ShannonLoader, projetados para Ghidra e IDA Pro por grupos como Comsecuris e FirmWire, são essenciais para carregar e analisar dumps de firmware. Estas ferramentas automatizam a identificação de regiões de memória e a resolução de símbolos com base nas extensas strings de debug presentes no binário.

Para análise dinâmica, frameworks de emulação como FirmWire e FirmState, baseados em QEMU e PANDA, permitem a execução do firmware do baseband em um ambiente controlado. Isso viabiliza a aplicação de técnicas de fuzzing, utilizando ferramentas como libAFL, para descobrir novas vulnerabilidades.

O acesso a interfaces de debug físicas e lógicas também é crucial. O comando `AT+SYSDBG` é utilizado para ativar modos de diagnóstico avançados. No nível do sistema operacional Android, a interface `/dev/umts_ramdump` permite a extração de dumps de memória (ramdumps) do baseband em caso de falhas críticas (kernel panics), fornecendo dados vitais para a análise post-mortem de exploits. Em nível de hardware, pinos UART na placa-mãe podem fornecer acesso direto ao console de debug do baseband.

## 5. Impacto no SM-N986B (Galaxy Note20 Ultra 5G)

O Samsung Galaxy Note20 Ultra 5G (modelo SM-N986B) é diretamente afetado por estas vulnerabilidades devido à utilização do chipset Exynos 990 e do modem Shannon 5123. As vulnerabilidades críticas, notadamente o CVE-2023-24033, foram abordadas nos Samsung Security Bulletins a partir de março e abril de 2023.

Antes da disponibilização e aplicação dos patches, a mitigação oficial recomendada pela Samsung e pelo Google Project Zero consistia na desativação das funcionalidades de Wi-Fi Calling e VoLTE nas configurações do dispositivo, bloqueando assim o vetor de ataque via SIP INVITE. Dispositivos executando versões de firmware (como a série N986BXX) compiladas antes de março de 2023 permanecem vulneráveis. A correção definitiva é aplicada através de atualizações de firmware OTA, que atualizam o binário do baseband em conjunto com os patches de segurança do sistema operacional Android.


## Mali-G77 MP11 Exploits

# Pesquisa Técnica: GPU ARM Mali-G77 MP11 (Exynos 990) - Vulnerabilidades e Exploits

## 1. Visão Geral da Arquitetura e Gerenciamento de Memória

A GPU ARM Mali-G77 (arquitetura Valhall) interage com o kernel do Linux através do driver `mali_kbase`. O gerenciamento de memória é um componente crítico, onde muitas vulnerabilidades foram descobertas.

### 1.1. Contextos e IOCTLs
A interação do espaço de usuário com a GPU começa com a abertura de `/dev/mali0` e a inicialização de um objeto `kbase_context` através de chamadas IOCTL. O `kbase_context` define um ambiente de execução e gerencia o espaço de endereçamento da GPU.

Principais IOCTLs:
*   `KBASE_IOCTL_VERSION_CHECK` (0x8000): Verifica a versão do driver.
*   `KBASE_IOCTL_SET_FLAGS` (0x8001): Configura flags de criação do contexto.
*   `KBASE_IOCTL_MEM_ALLOC` (0x8002): Aloca memória na GPU. Retorna um cookie usado como offset no `mmap`.
*   `KBASE_IOCTL_MEM_COMMIT`: Altera a quantidade de memória física que apoia uma região virtual.
*   `KBASE_IOCTL_JOB_SUBMIT`: Submete jobs de software ou hardware para a GPU.
*   `KBASE_IOCTL_KCPU_QUEUE_CREATE`: Cria uma fila de comandos para a CPU (usado em GPUs com CSF).
*   `KBASE_IOCTL_KCPU_QUEUE_ENQUEUE`: Enfileira comandos de software (ex: `BASE_KCPU_COMMAND_TYPE_JIT_ALLOC`).

### 1.2. Estruturas de Dados de Memória
*   `kbase_va_region`: Representa uma região de memória compartilhada entre GPU e CPU. Contém campos como `start_pfn`, `nr_pages` (tamanho virtual), e flags de permissão (`KBASE_REG_CPU_WR`, `KBASE_REG_GPU_WR`).
*   `kbase_mem_phy_alloc`: Rastreia as páginas físicas mapeadas para a GPU. Contém o array `pages` e o campo `nents` (número de páginas físicas).
*   `kbase_context->mmu`: Gerencia a tabela de páginas da GPU (4 níveis: PGD, PUD, PMD, PTE).

---

## 2. Análise Detalhada das Vulnerabilidades (CVEs)

### 2.1. CVE-2021-28663
*   **Componente Afetado:** Driver kernel ARM Mali (Midgard, Bifrost, Valhall).
*   **Tipo:** Use-After-Free (UAF) / Design Flaw.
*   **Impacto:** Escalonamento de Privilégios Local (LPE) / Information Leak. Permite mapeamento de memória física arbitrária. Explorada in-the-wild por spyware.
*   **Detalhes Técnicos e Exploração:**
    A vulnerabilidade reside em uma falha de design no gerenciamento de memória. O driver permite que operações impróprias na memória da GPU levem a um UAF.
    **Técnica de Exploração (PoC lntrx):**
    1.  Cria-se um `GPU_VA` (Virtual Address) e faz-se o `mmap` para obter o endereço virtual das páginas físicas.
    2.  Cria-se um alias para as páginas físicas, mas sem fazer o `mmap`, mantendo o `gpu_mapping` como 1.
    3.  Altera-se as flags do `GPU_VA` para `BASE_MEM_DONT_NEED`. O driver Mali marca as páginas como evictable (podem ser descartadas).
    4.  Como o atacante possui a região (`reg`) para a página aliased, pode-se fazer o `mmap` para ela, obtendo acesso de leitura (RDONLY) a partir da CPU para páginas que já foram liberadas/reutilizadas.

### 2.2. CVE-2021-28664
*   **Componente Afetado:** Driver kernel ARM Mali (Midgard, Bifrost, Valhall).
*   **Tipo:** Out-of-Bounds Write / Privilege Escalation (Memory Corruption).
*   **Impacto:** LPE. O driver permite que um usuário sem privilégios obtenha acesso de leitura/escrita a páginas de memória somente leitura (Read-Only).
*   **Detalhes Técnicos e Exploração:**
    O driver eleva incorretamente as permissões de páginas RO da CPU para graváveis.
    **Técnica de Exploração (PoC Wang):**
    A exploração envolve o uso da IOCTL `KBASE_IOCTL_MEM_IMPORT` para importar uma página de memória somente leitura (`imported_ubuf.ptr = (u64)ro_page`). Devido à falha na verificação de permissões, o driver permite que a GPU escreva nessa página, que pode ser uma página de código do kernel ou de uma biblioteca compartilhada, permitindo a execução de código arbitrário.

### 2.3. CVE-2021-39793 (Relacionada a CVE-2022-22706)
*   **Componente Afetado:** Driver kernel ARM Mali.
*   **Tipo:** Broken Access Control Logic / OOB Write.
*   **Impacto:** LPE. Permite que páginas importadas somente leitura se tornem graváveis pelo host.
*   **Detalhes Técnicos e Exploração:**
    O driver permite que o espaço de usuário crie objetos de memória da GPU a partir de áreas de memória virtual do host usando o tipo `KBASE_MEM_TYPE_IMPORTED_USER_BUF`. A função `pin_user_pages_remote()` é usada para obter referências às páginas.
    O bug ocorre na função `kbase_jd_user_buf_pin_pages()`, que verifica apenas a flag `KBASE_REG_GPU_WR` para determinar se deve solicitar acesso de escrita, ignorando incorretamente a flag `KBASE_REG_CPU_WR`.
    **Fluxo de Exploração:**
    1.  Mapear uma página de uma biblioteca compartilhada como somente leitura.
    2.  Criar um buffer Mali `KBASE_MEM_TYPE_IMPORTED_USER_BUF` com `KBASE_REG_CPU_WR`, mas sem `KBASE_REG_GPU_WR`, a partir do mapeamento da página vítima.
    3.  Acionar `kbase_jd_user_buf_pin_pages()` (via `KBASE_IOCTL_KCPU_QUEUE_ENQUEUE` ou submetendo um atom com `BASE_JD_REQ_EXTERNAL_RESOURCES`).
    4.  Escrever no objeto de memória Mali a partir do espaço de usuário do host, modificando a página originalmente RO.

### 2.4. CVE-2022-20186
*   **Componente Afetado:** Driver kernel ARM Mali.
*   **Tipo:** Falha de gerenciamento de memória (manipulação de tabela de páginas).
*   **Impacto:** Arbitrary Kernel Memory R/W / LPE.
*   **Detalhes Técnicos e Exploração:**
    A exploração desta vulnerabilidade (detalhada no post "Corrupting memory without memory corruption" do GitHub Security Lab) demonstra como obter primitivas de leitura e escrita arbitrárias manipulando a tabela de páginas da GPU.
    Cada `kbase_context` mantém sua própria tabela de páginas de 4 níveis. O PGD (Page Global Directory) é armazenado em `mmut->pgd`. As páginas físicas de apoio são alocadas via `kbase_alloc_phy_pages`.
    A exploração envolve corromper as entradas da tabela de páginas (PTEs) da GPU para apontar para endereços físicos arbitrários. Como a GPU e a CPU compartilham a memória física, ao mapear uma página física do kernel para o espaço de endereçamento da GPU, o atacante pode ler e escrever na memória do kernel enviando jobs para a GPU via `KBASE_IOCTL_JOB_SUBMIT`.

### 2.5. CVE-2022-22706
*   **Componente Afetado:** Driver kernel ARM Mali.
*   **Tipo:** Broken Access Control / Use-After-Free.
*   **Impacto:** LPE. Explorada in-the-wild.
*   **Detalhes Técnicos:**
    Esta vulnerabilidade é essencialmente a mesma causa raiz da CVE-2021-39793, onde a verificação de permissões ao importar buffers de usuário (`KBASE_MEM_TYPE_IMPORTED_USER_BUF`) falha ao verificar a flag `KBASE_REG_CPU_WR`. Ocorre em caminhos de código duplicados no driver (tratamento de timeline fence / external resources). A exploração segue o mesmo fluxo: importar página RO, contornar a verificação de escrita e modificar a página via GPU.

### 2.6. CVE-2022-38181
*   **Componente Afetado:** Driver kernel ARM Mali.
*   **Tipo:** Use-After-Free.
*   **Impacto:** LPE. Explorada in-the-wild por spyware comercial.
*   **Detalhes Técnicos e Exploração:**
    A vulnerabilidade envolve o manuseio de memória JIT (Just-In-Time) e operações de alias de memória da GPU.
    A exploração (como visto no repositório `CVE_2022_38181_Raven`) abusa do shrinker do kernel (`mali_shrinker_mmap32.c`). O UAF é alcançado manipulando as alocações e liberações de memória JIT.
    1.  Aloca-se memória JIT.
    2.  Força-se a liberação da memória JIT (criando a condição UAF) enquanto ponteiros para ela ainda existem na tabela de páginas ou em estruturas de gerenciamento.
    3.  Realoque-se a página liberada com um objeto controlado pelo atacante (ex: uma tabela de páginas PGD).
    4.  Usa-se o ponteiro pendente para modificar a nova estrutura, ganhando R/W arbitrário.

### 2.7. CVE-2023-4211
*   **Componente Afetado:** Driver kernel ARM Mali (Midgard, Bifrost, Valhall).
*   **Tipo:** Use-After-Free.
*   **Impacto:** LPE. Explorada in-the-wild.
*   **Detalhes Técnicos e Exploração (Project Zero RCA):**
    O bug está no manuseio da VMA (Virtual Memory Area) de "tracking page". A regra pretendida é que apenas uma VMA de tracking page possa existir por contexto Mali.
    Quando uma VMA de tracking page é destruída, `kbasep_os_process_page_usage_drain()` é chamada para limpar `kctx->process_mm`. No entanto, antes do r43, era possível criar uma VMA de tracking page de múltiplas páginas e dividi-la (usando `munmap()`), quebrando a suposição de VMA única.
    **Fluxo da Corrida (Race Condition):**
    1.  Processo A cria um contexto e uma VMA de tracking page (0x2000 bytes). `kctx->process_mm` aponta para o `mm_struct` de A.
    2.  Processo A faz `munmap` de 0x1000 bytes, dividindo a VMA. `kbasep_os_process_page_usage_drain()` define `kctx->process_mm` como NULL.
    3.  Processo A faz fork, criando Processo B.
    4.  Processo B cria uma VMA de tracking page (0x1000 bytes). `kctx->process_mm` aponta para o `mm_struct` de B.
    5.  Processo A chama `munmap` na VMA restante. A thread entra em `kbasep_os_process_page_usage_drain()`, lê `kctx->process_mm` (apontando para B), define como NULL, solta o lock e é preemptada em `synchronize_rcu()`.
    6.  Processo B sai. Libera sua VMA. `kbasep_os_process_page_usage_drain()` vê `kctx->process_mm` como NULL e retorna. Processo B libera seu `mm_struct`.
    7.  Processo A retoma a execução com o ponteiro `mm` apontando para o `mm_struct` liberado de B. Tenta fazer bookkeeping (`kbasep_add_mm_counter`), resultando em um UAF write.

### 2.8. CVE-2023-26083
*   **Componente Afetado:** Driver kernel ARM Mali.
*   **Tipo:** Information Leak.
*   **Impacto:** Vazamento de ponteiros do kernel, facilitando o bypass de KASLR.
*   **Detalhes Técnicos:**
    O vazamento de informações ocorre através do mapeamento de memória da GPU, especificamente nos buffers de mensagens de stream de timeline. Ao alocar memória (`KBASE_IOCTL_MEM_ALLOC`) e cometer alterações (`KBASE_IOCTL_MEM_COMMIT`), estruturas internas do kernel não são devidamente limpas antes de serem expostas ao espaço de usuário, permitindo que um atacante leia ponteiros do kernel e calcule offsets.

---

## 3. Técnicas de Exploração Avançadas

### 3.1. Manipulação da Tabela de Páginas da GPU (PTMA)
A técnica "Page Table Manipulation Attack" é fundamental nos exploits do Mali.
1.  **Objetivo:** Obter acesso de Leitura/Escrita (R/W) à memória física arbitrária.
2.  **Método:** O atacante usa uma vulnerabilidade (como UAF) para sobrescrever uma entrada na tabela de páginas da GPU (PTE, PMD ou PGD).
3.  **Execução:** Ao fazer o PTE apontar para o endereço físico de uma estrutura crítica do kernel (como credenciais de processo ou código do kernel), o atacante submete um job para a GPU (`KBASE_IOCTL_JOB_SUBMIT`). A GPU, executando o job, lê ou escreve no endereço físico alvo, contornando as proteções de memória da CPU (como KPTI e MTE).

### 3.2. Abuso da Região JIT
A memória JIT (Just-In-Time) é alocada e gerenciada dinamicamente pelo driver Mali para otimizar a execução de shaders.
1.  **Vulnerabilidade:** Falhas no ciclo de vida da memória JIT (ex: CVE-2022-38181, CVE-2023-6241) permitem que a região JIT seja liberada (`KBASE_IOCTL_MEM_COMMIT` para encolher a região) enquanto ponteiros para ela ainda existem.
2.  **Exploração:** O atacante realoca a página liberada com dados controlados (ex: uma tabela de páginas). Como a GPU ainda tem acesso à região JIT original através do ponteiro pendente, o atacante pode modificar a nova estrutura alocada.

### 3.3. GPU Command Stream Injection
Em GPUs modernas com Command Stream Frontend (CSF), os comandos são enviados via filas.
1.  **Método:** O atacante injeta comandos maliciosos no stream de comandos da GPU.
2.  **Execução:** Isso é frequentemente usado em conjunto com a manipulação da tabela de páginas. O atacante escreve um pequeno programa em OpenCL ou código de máquina da GPU, mapeia-o na memória da GPU e usa `KBASE_IOCTL_JOB_SUBMIT` ou `KBASE_IOCTL_KCPU_QUEUE_ENQUEUE` para forçar a GPU a executar as instruções, que realizarão as leituras/escritas na memória física corrompida.

---
*Fim do Relatório*


## Exynos 990 NPU Exploits

# Pesquisa Técnica: Samsung Exynos 990 NPU (Neural Processing Unit)

## 1. Arquitetura e Driver da NPU

A Neural Processing Unit (NPU) do Samsung Exynos 990 é exposta ao espaço de usuário através do driver de dispositivo `/dev/vertex10`. Este driver é responsável por gerenciar a comunicação entre o sistema operacional e o hardware da NPU, permitindo a execução de operações de aprendizado de máquina aceleradas por hardware.

### 1.1. Interface IOCTL

A comunicação com o driver `/dev/vertex10` é realizada principalmente através de chamadas IOCTL. As principais chamadas IOCTL identificadas incluem:

*   `VS4L_VERTEXIOC_S_GRAPH`: Utilizada para configurar o grafo de computação neural.
*   `VS4L_VERTEXIOC_S_FORMAT`: Utilizada para definir o formato dos dados de entrada e saída.
*   `VS4L_VERTEXIOC_STREAM_ON`: Inicia o processamento do fluxo de dados.
*   `VS4L_VERTEXIOC_STREAM_OFF`: Interrompe o processamento do fluxo de dados.
*   `VS4L_VERTEXIOC_QBUF`: Enfileira um buffer para processamento.

### 1.2. Mapeamento de Memória e Firmware

O driver gerencia buffers DMA (Direct Memory Access) para a transferência eficiente de dados entre a memória principal e a NPU. O firmware da NPU é carregado a partir do sistema de arquivos. Em versões mais antigas, observou-se que o firmware não era assinado, o que poderia permitir a execução de código arbitrário na NPU caso um atacante conseguisse substituir o arquivo de firmware. A região de carregamento do firmware é mapeada em endereços específicos, como `0x50000000`.

## 2. Vulnerabilidades Descobertas (Google Project Zero)

O Google Project Zero e outros pesquisadores de segurança identificaram várias vulnerabilidades críticas no driver da NPU do Exynos.

### 2.1. CVE-2022-22265: Double Free no Driver da NPU

*   **CVE ID:** CVE-2022-22265
*   **Componente Afetado:** Driver da NPU (`/dev/vertex10`), especificamente na manipulação de formatos na estrutura `vb_queue`.
*   **Tipo:** Double Free (Use-After-Free)
*   **Impacto:** Local Privilege Escalation (LPE) / Arbitrary Kernel Read/Write.
*   **Descrição Técnica:**
    A vulnerabilidade reside na função `vb_queue_s_format()` localizada em `drivers/vision/vision-core/vision-buffer.c`. Quando a IOCTL `VS4L_VERTEXIOC_S_FORMAT` é chamada com um argumento `format_list` inválido, a função `__vb_find_format()` falha em localizar o formato. Isso leva à primeira liberação (free) do ponteiro `q->format.formats` através de `kfree(q->format.formats)`.
    A segunda liberação ocorre quando a IOCTL `VS4L_VERTEXIOC_STREAM_OFF` é chamada. A função `npu_vertex_streamoff()` chama `npu_queue_stop()`, que por sua vez chama `vb_queue_stop()`. Esta última função executa novamente `kfree(q->format.formats)` no mesmo ponteiro, resultando em um double free.
*   **Técnica de Exploração:**
    Um atacante pode explorar essa vulnerabilidade controlando o tamanho dos objetos do kernel afetados e o momento da segunda liberação. A estratégia comum envolve:
    1.  Acionar a primeira liberação.
    2.  Ocupar o objeto liberado usando a syscall `select` ou alocando objetos `signalfd` (kmalloc-128).
    3.  Acionar a segunda liberação via `VS4L_VERTEXIOC_STREAM_OFF`.
    4.  Reocupar o objeto com estruturas `pipe_buffer` usando `fcntl(fd, F_SETPIPE_SZ, size)`.
    5.  Vazar o endereço do `pipe_buffer` para obter um info leak do kernel.
    6.  Implementar um ataque Kernel Space Mirroring Attack (KSMA) manipulando as tabelas de páginas (PTE spray) para obter primitivas de leitura e escrita arbitrárias no kernel.
*   **Mitigação:** O patch corrige a vulnerabilidade definindo o ponteiro `q->format.formats` como `NULL` após a primeira liberação.

### 2.2. CVE-2022-22269 e CVE-2022-22270

*   **CVE-2022-22269:** Identificada como uma vulnerabilidade de leitura fora dos limites (Out-of-Bounds Read) no driver da NPU.
*   **CVE-2022-22270:** Identificada como um vazamento de informações (Info Leak) no driver da NPU.
*   **Detalhes:** Ambas as vulnerabilidades foram corrigidas nas atualizações de segurança da Samsung (SMR) do início de 2022. Elas representam falhas na validação de limites e no manuseio de dados sensíveis dentro do driver, permitindo que um atacante local obtenha informações privilegiadas da memória do kernel.

## 3. Cadeia de Exploit e Mitigações

### 3.1. Cadeia de Exploit Completa

Uma cadeia de exploit típica visando a NPU do Exynos 990 envolveria os seguintes passos:

1.  **Info Leak:** Utilizar uma vulnerabilidade como a CVE-2022-22270 ou a primeira fase da CVE-2022-22265 para vazar endereços de memória do kernel.
2.  **KASLR Bypass:** Com os endereços vazados, calcular o endereço base do kernel, contornando a proteção Kernel Address Space Layout Randomization (KASLR).
3.  **Use-After-Free / Double Free:** Acionar a CVE-2022-22265 para corromper a memória do kernel.
4.  **Arbitrary Kernel R/W:** Manipular estruturas de dados do kernel (como `pipe_buffer` e tabelas de páginas via KSMA) para obter primitivas de leitura e escrita arbitrárias.
5.  **Disable SELinux:** Localizar e modificar as estruturas de dados do SELinux na memória do kernel para desativar a aplicação de políticas (setar `enforcing` para 0).
6.  **Root:** Escalar privilégios modificando as credenciais do processo atual (estrutura `cred`) para obter acesso root.

### 3.2. Mitigações e Controle de Acesso

*   **Patches da Samsung:** As vulnerabilidades foram corrigidas nas atualizações de segurança (SMR) a partir de janeiro de 2022.
*   **SELinux:** Historicamente, o driver `/dev/vertex10` podia ser acessado a partir do contexto `untrusted_app`. As políticas do SELinux foram posteriormente atualizadas para restringir o acesso, exigindo contextos mais privilegiados (como `shell` ou contextos específicos do sistema) para interagir com o dispositivo, mitigando a exploração a partir de aplicativos maliciosos comuns.

## Referências

[1] Google Project Zero. "CVE-2022-22265: Samsung NPU device driver double free in Android". Disponível em: https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2022/CVE-2022-22265.html
[2] Soez. "CVE-2022-22265 Samsung npu driver". Disponível em: https://soez.github.io/posts/CVE-2022-22265-Samsung-npu-driver/
[3] Samsung Mobile Security. "Security Updates". Disponível em: https://security.samsungmobile.com/securityUpdate.smsb


## Download Mode & PIT

# Pesquisa Técnica: Samsung Download Mode (Odin/Loke Protocol) e PIT no Exynos 990

## 1. Introdução ao Download Mode e Protocolo Odin/Loke

O Samsung Download Mode (frequentemente referido como Odin Mode) é um ambiente de recuperação e gravação de firmware de baixo nível presente em dispositivos Samsung Galaxy, incluindo o Samsung Galaxy Note20 Ultra 5G (SM-N986B) equipado com o SoC Exynos 990. Este modo é ativado fisicamente através da combinação de teclas (Volume Down + Power durante o boot) ou via software através do comando `adb reboot download`.

A comunicação entre o host (PC) e o dispositivo no Download Mode é regida pelo protocolo proprietário Odin/Loke. Este protocolo opera sobre transferências USB Bulk (Bulk IN e Bulk OUT) e é projetado para transferir imagens de firmware, tabelas de partição e comandos de controle diretamente para o bootloader secundário ou terciário do dispositivo.

### 1.1. Handshake e Estrutura de Pacotes Loke

A inicialização do protocolo Odin/Loke começa com uma sequência de handshake. O host envia pacotes de controle e espera uma resposta específica do dispositivo para confirmar que o modo de download está ativo e pronto para receber comandos.

A sequência de handshake típica envolve o host enviando comandos de inicialização e o dispositivo respondendo com a string mágica `"LOKE"`. A implementação open-source Heimdall demonstra que a verificação de sucesso do handshake é feita lendo 4 bytes do endpoint Bulk IN e comparando com `"LOKE"` [1].

A estrutura geral dos pacotes de controle no protocolo Odin/Loke (baseado na engenharia reversa do Heimdall) consiste em um cabeçalho de 4 bytes seguido por dados específicos do comando. Os pacotes são divididos em várias categorias:

*   **Session Setup Packets (0x64):** Usados para iniciar a sessão, definir o tipo de dispositivo, tamanho total dos bytes a serem transferidos e habilitar recursos como T-Flash.
*   **PIT File Packets (0x65):** Comandos específicos para solicitar, enviar ou finalizar a transferência da Partition Information Table (PIT).
*   **File Transfer Packets (0x66):** Comandos para iniciar o flash de uma partição, enviar partes do arquivo e finalizar a transferência.
*   **End Session Packets (0x67):** Comandos para encerrar a sessão e reiniciar o dispositivo.

A estrutura de um pacote de controle (`ControlPacket`) é essencialmente:
*   `Offset 0x00`: Tipo de Controle (ex: `0x64`, `0x65`, `0x66`, `0x67`) em formato Little-Endian.

Pacotes mais específicos, como `SessionSetupPacket`, adicionam um campo de requisição:
*   `Offset 0x00`: Tipo de Controle (`0x64`)
*   `Offset 0x04`: Tipo de Requisição (ex: `0x00` para BeginSession, `0x02` para TotalBytes)

## 2. Partition Information Table (PIT)

A Partition Information Table (PIT) é uma estrutura de dados crítica que define o layout de armazenamento da memória flash (eMMC ou UFS) em dispositivos Samsung. O arquivo PIT contém metadados sobre cada partição, incluindo seu nome, tamanho, deslocamento e atributos de atualização.

### 2.1. Estrutura do Cabeçalho PIT

O arquivo PIT começa com um cabeçalho de 28 bytes (`kHeaderDataSize = 28`), que contém informações globais sobre a tabela de partições [2].

| Offset | Tamanho | Tipo | Descrição |
| :--- | :--- | :--- | :--- |
| `0x00` | 4 bytes | Inteiro | Magic Number / File Identifier (`0x12349876`) |
| `0x04` | 4 bytes | Inteiro | Número de Entradas (Partition Count) |
| `0x08` | 4 bytes | Inteiro | Unknown 1 |
| `0x0C` | 4 bytes | Inteiro | Unknown 2 |
| `0x10` | 2 bytes | Short | Unknown 3 |
| `0x12` | 2 bytes | Short | Unknown 4 |
| `0x14` | 2 bytes | Short | Unknown 5 |
| `0x16` | 2 bytes | Short | Unknown 6 |
| `0x18` | 2 bytes | Short | Unknown 7 |
| `0x1A` | 2 bytes | Short | Unknown 8 |

*Nota: O Magic Number frequentemente citado em documentações mais antigas é `0x76543210`, mas a implementação do Heimdall define `kFileIdentifier = 0x12349876` (que é a representação Little-Endian de `0x76543210`).*

### 2.2. Estrutura da Entrada PIT (PitEntry)

Após o cabeçalho, seguem-se as entradas da tabela de partições. Cada entrada tem um tamanho fixo de 132 bytes (`kDataSize = 132`) [2].

| Offset | Tamanho | Tipo | Descrição |
| :--- | :--- | :--- | :--- |
| `0x00` | 4 bytes | Inteiro | Binary Type (`0` = Application Processor, `1` = Communication Processor) |
| `0x04` | 4 bytes | Inteiro | Device Type (`0` = OneNand, `1` = File/FAT, `2` = MMC, `3` = All) |
| `0x08` | 4 bytes | Inteiro | Identifier (ID da Partição) |
| `0x0C` | 4 bytes | Inteiro | Attributes (`1` = Write, `2` = STL) |
| `0x10` | 4 bytes | Inteiro | Update Attributes (`1` = Fota, `2` = Secure) |
| `0x14` | 4 bytes | Inteiro | Block Size ou Offset |
| `0x18` | 4 bytes | Inteiro | Block Count |
| `0x1C` | 4 bytes | Inteiro | File Offset (Obsoleto) |
| `0x20` | 4 bytes | Inteiro | File Size (Obsoleto) |
| `0x24` | 32 bytes | String | Partition Name (ex: `BOOT`, `RECOVERY`, `SYSTEM`) |
| `0x44` | 32 bytes | String | Flash Filename (Nome do arquivo USB flash, ex: `boot.img`) |
| `0x64` | 32 bytes | String | FOTA Filename (Firmware Over-The-Air) |

## 3. Vulnerabilidades e Exploits no Exynos 990

A arquitetura de boot do Exynos 990 tem sido alvo de pesquisas de segurança significativas, revelando vulnerabilidades críticas que permitem a execução de código arbitrário no nível do BootROM (BL1).

### 3.1. CVE-2024-56426: Exynos 990 BootROM Exploit

A vulnerabilidade CVE-2024-56426 é uma falha crítica no BootROM (BL1) unificado das famílias Exynos 990 e Exynos 9830 (Galaxy S20, S20 FE, Note20). Esta vulnerabilidade permite a execução de código arbitrário via USB durante o processo de boot [3].

#### 3.1.1. Detalhes Técnicos da Exploração

A exploração desta vulnerabilidade envolve a manipulação do contexto USB (`usb_ctx`) no BootROM. O BootROM do Exynos 990 utiliza o controlador USB DWC3. A estrutura `usb_ctx` contém ponteiros de função e buffers que podem ser corrompidos.

O exploit documentado (usbliter8) aproveita uma falha no tratamento de transferências de controle USB (Endpoint 0). O código de exploração envia transferências de controle maliciosas para sobrescrever a memória interna (iRAM) do dispositivo.

**Endereços de Memória Relevantes (Exynos 990 / S20 Series):**
*   `EPBL_LOAD_ADDR`: `0x02026000` (Endereço onde o EPBL - External Primary Bootloader é carregado).
*   `EPBL_PTR_REGION_START_OFF`: `0xBD28` (Offset relativo ao `EPBL_LOAD_ADDR`).
*   `EPBL_PTR_REGION_END_OFF`: `0xBD50`.
*   Endereço alvo para overwrite no exploit: `0x02022000` (para fluxo assinado) ou `0x02022010` (para fluxo não assinado).

**Mecanismo de Overwrite (Python PoC):**
O exploit utiliza a função `dev.ctrl_transfer` do `libusb` para enviar um payload modificado que altera um ponteiro de função ou endereço de retorno na memória do BootROM.

```python
def run_exploit(dev, increase, address):
    # Lê o estado atual
    data = dev.ctrl_transfer(0x80, 0x08, 0, 0, 0x494).tobytes()
    work = bytearray(data)
    
    # Desempacota o valor atual no offset 0x480
    current, = unpack_from("<I", work, 0x480)
    
    # Modifica o valor incrementando-o
    pack_into("<I", work, 0x480, (current + increase) & 0xFFFFFFFF)
    
    # Injeta o endereço alvo no offset 0x490
    pack_into("<I", work, 0x490, address & 0xFFFFFFFF)
    
    try:
        # Envia o payload modificado de volta para acionar a vulnerabilidade
        dev.ctrl_transfer(0x00, 0x08, 0, 0, work)
    except:
        print("Exploit done")
```

#### 3.1.2. Impacto e Cadeia de Execução

A exploração bem-sucedida do CVE-2024-56426 permite que um atacante contorne a verificação de assinatura do BootROM (BL1) e carregue um bootloader secundário (FWBL1 / EPBL) modificado ou assinado com chaves personalizadas.

A cadeia de execução típica do exploit envolve:
1.  Envio de um payload inicial (`Exynos990_boot_custom_key.bin` ou `loader.bin`) para a memória.
2.  Execução da função `run_exploit` para corromper a memória e redirecionar o fluxo de execução para o payload carregado.
3.  O payload inicial atua como um "Hubble chain", permitindo o carregamento subsequente de imagens do bootloader (`fwbl1.img`, `epbl.img`, `bl2.img`, `lk.bin`, `el3_mon.img`, `ldfw.img`, `tzsw.img`) sem a verificação rigorosa da assinatura original da Samsung.

### 3.2. CVE-2017-8890: Vulnerabilidade Histórica no Download Mode

Embora mais antiga, a CVE-2017-8890 é uma vulnerabilidade notável relacionada ao parsing de descritores USB no kernel Linux, que afetou o modo de download e interfaces USB de vários dispositivos Android, incluindo implementações da Samsung. A falha residia na função `inet_csk_clone_lock` no subsistema IPv4/IPv6, permitindo um double free que poderia ser explorado para escalonamento de privilégios locais (LPE) [4]. Embora não seja específica do protocolo Odin, ilustra a superfície de ataque exposta pelas interfaces USB de baixo nível.

## 4. Ferramentas da Comunidade: Heimdall e lk2nd

### 4.1. Heimdall

Heimdall é uma suíte de software open-source (cross-platform) projetada para substituir o software Odin proprietário da Samsung. Ele implementa o protocolo Odin/Loke através de engenharia reversa, permitindo que os usuários façam o flash de firmware (ROMs) em dispositivos Samsung Galaxy.

O Heimdall interage diretamente com a interface USB usando `libusb`, enviando os pacotes de controle e dados descritos na Seção 1. Ele é capaz de ler o arquivo PIT do dispositivo (`print-pit`), baixar partições específicas e gravar novas imagens.

### 4.2. lk2nd / lk3rd

`lk2nd` (Little Kernel 2nd) é um bootloader secundário de código aberto projetado para dispositivos Android. Ele é empacotado como uma imagem de boot padrão do Android e é carregado pelo bootloader original do dispositivo (BL2/SBOOT).

O objetivo principal do `lk2nd` é fornecer um ambiente de boot padronizado (baseado no Little Kernel da Qualcomm ou implementações similares) que abstrai as peculiaridades dos bootloaders proprietários (como o SBOOT da Samsung). Ele permite o chainloading de outros sistemas operacionais (como distribuições Linux mainline, postmarketOS) e fornece uma interface Fastboot padrão, substituindo a necessidade de usar o Download Mode proprietário (Odin) para operações de desenvolvimento subsequentes.

No contexto do Exynos 990, ferramentas como o exploit CVE-2024-56426 podem ser usadas para injetar um bootloader modificado que, por sua vez, carrega o `lk2nd`, abrindo o dispositivo para modificações profundas e execução de kernels não assinados.

## Referências

[1] Benjamin Dobell. Heimdall Source Code - BridgeManager.cpp. GitHub. Disponível em: https://github.com/Benjamin-Dobell/Heimdall/blob/master/heimdall/source/BridgeManager.cpp
[2] Benjamin Dobell. Heimdall Source Code - libpit.h. GitHub. Disponível em: https://github.com/Benjamin-Dobell/Heimdall/blob/master/libpit/source/libpit.h
[3] Creeeeger. CVE-2024-56426: Exynos 990 / Exynos9830 Unified BootROM Exploit. GitHub. Disponível em: https://github.com/Creeeeger/CVE-2024-56426
[4] MITRE. CVE-2017-8890. National Vulnerability Database. Disponível em: https://nvd.nist.gov/vuln/detail/CVE-2017-8890


## Exynos 990 Kernel Exploits

# Pesquisa Técnica: Samsung Exynos 990 - Kernel Vulnerabilities e Privilege Escalation

Este documento apresenta uma análise técnica profunda sobre vulnerabilidades de kernel e técnicas de escalonamento de privilégios (LPE) no Samsung Galaxy Note20 Ultra 5G (SM-N986B, SoC Exynos 990). O foco é estritamente técnico, abordando CVEs específicos, mecanismos de exploração, mitigação e arquitetura de baixo nível.

## 1. Cadeia de Exploração In-The-Wild (CVE-2021-25337 + CVE-2021-25369 + CVE-2021-25370)

Uma cadeia de exploração completa foi descoberta em uso ativo (in-the-wild) visando dispositivos Samsung com SoC Exynos e kernel 4.14.113. A cadeia combina três vulnerabilidades para escapar da sandbox de aplicativo e alcançar execução de código arbitrário no kernel [1].

### 1.1. CVE-2021-25337: Arbitrary File Read/Write via Clipboard Provider

**Componente Afetado:** `SemClipboardProvider` (Content Provider customizado da Samsung executando no `system_server`).
**Tipo:** Falta de controle de acesso (Access Control Bypass).
**Impacto:** Leitura e escrita arbitrária de arquivos no sistema de arquivos.

O `SemClipboardProvider` não possuía permissões definidas em seu manifesto, permitindo que qualquer aplicativo (incluindo `untrusted_app`) interagisse com ele. A tabela do provedor possuía uma coluna `_data`, que no Android é usada com o método `openFileHelper` para retornar um `ParcelFileDescriptor` [2].

O exploit utilizava o seguinte código Java para obter um file descriptor (FD) com privilégios de sistema:

```java
ContentValues vals = new ContentValues();
vals.put("_data", "/data/system/users/0/newFile.bin");
URI semclipboard_uri = URI.parse("content://com.sec.android.semclipboardprovider");
ContentResolver resolver = getContentResolver();
URI newFile_uri = resolver.insert(semclipboard_uri, vals);
return resolver.openFileDescriptor(newFile_uri, "w").getFd();
```

Isso permitia que o aplicativo não confiável escrevesse um binário ELF (estágio 2) no diretório `/data/system/users/0/` (contexto SELinux `users_system_data_file`), contornando as restrições do SELinux que normalmente impediriam o acesso direto [2].

### 1.2. CVE-2021-25369: Kernel Information Leak via sec_log

**Componente Afetado:** Driver ARM Mali GPU e sistema de log customizado da Samsung (`sec_log`).
**Tipo:** Information Leak (Vazamento de Informação).
**Impacto:** KASLR Bypass (vazamento de endereços do kernel, incluindo `task_struct` e `sys_call_table`).

A vulnerabilidade é acionada ao enviar um comando `ioctl` inválido para o driver HWCNT da GPU Mali, o que atinge uma macro `WARN_ON(true)` no kernel [3].

```c
// Código PoC para acionar o WARN_ON
hwcnt_fd = ioctl(dev_mali_fd, 0x40148008, &v4);
ioctl(hwcnt_fd, 0x4004BEFE, 0);

// Iniciar o bugreport para copiar o kmsg para /data/log/sec_log.log
system("setprop dumpstate.options bugreportfull; setprop ctl.start bugreport");
```

Quando `WARN_ON` é executado, um backtrace completo é registrado no `kmsg`, incluindo o conteúdo bruto da pilha. A Samsung implementou um serviço customizado (`dumpstate`) que copia o conteúdo do `kmsg` para `/proc/sec_log` e `/data/log/sec_log.log`. As permissões do arquivo `sec_log` eram muito mais permissivas que as do `/dev/kmsg`, permitindo que o aplicativo lesse os endereços de memória vazados, quebrando o KASLR [3].

### 1.3. CVE-2021-25370: Use-After-Free no Driver DPU/DECON

**Componente Afetado:** Driver Display Processing Unit (DPU) / Display and Enhancement Controller (DECON).
**Tipo:** Use-After-Free (UAF).
**Impacto:** Execução arbitrária de código no kernel (Arbitrary Kernel Read/Write).

Esta vulnerabilidade envolve o manuseio incorreto de file descriptors no driver DPU. O exploit utiliza o endereço `sys_call_table` vazado para contornar o KASLR e o ponteiro `task_struct` para localizar o ponteiro `addr_limit`. Ao manipular estruturas de dados no kernel após a liberação da memória (UAF), o atacante consegue modificar o `addr_limit` para obter primitivas de leitura e escrita arbitrárias no kernel [1] [4].

## 2. Outras Vulnerabilidades Críticas no Kernel Exynos

### 2.1. CVE-2022-22265: Double Free / UAF no Driver NPU

**Componente Afetado:** Driver da Neural Processing Unit (NPU) da Samsung.
**Tipo:** Double Free resultando em Use-After-Free.
**Impacto:** Execução de código no kernel.

A vulnerabilidade reside nas chamadas `ioctl` do driver NPU. O primeiro `kfree` ocorre quando `VS4L_VERTEXIOC_S_FORMAT` é chamado com um formato inválido, liberando `q->format.formats`. O segundo `kfree` é acionado chamando `VS4L_VERTEXIOC_STREAM_OFF`, que invoca `vb_queue_stop()`, liberando novamente o mesmo ponteiro [5].

A estratégia de exploração envolve:
1. Acionar o primeiro `kfree`.
2. Ocupar o objeto liberado (tamanho 128 bytes, `kmalloc-128`) com um objeto `signalfd_ctx` usando a syscall `signalfd`.
3. Acionar o segundo `kfree` (Double Free).
4. Reutilizar o objeto liberado com estruturas `pipe_buffer` via `fcntl(fd, F_SETPIPE_SZ, size)`.
5. Realizar operações de cross-cache para alocar Page Table Entries (PTEs) sobre o objeto UAF.
6. Modificar as PTEs para mapear a memória física do kernel, permitindo a injeção de shellcode no processo `init` [5].

### 2.2. CVE-2023-0266: UAF no ALSA USB Audio

**Componente Afetado:** Camada de compatibilidade de 32 bits do driver ALSA (Advanced Linux Sound Architecture).
**Tipo:** Race Condition resultando em Use-After-Free.
**Impacto:** Execução de código no kernel.

A vulnerabilidade ocorre devido à ausência de bloqueios (locks) adequados nas chamadas `ioctl` de 32 bits (`SNDRV_CTL_IOCTL_ELEM_WRITE32` e `SNDRV_CTL_IOCTL_ELEM_READ32`). Uma refatoração em 2017 moveu a aquisição do lock `controls_rwsem` para cima na árvore de chamadas de 64 bits, mas omitiu a camada de compatibilidade de 32 bits [6].

Isso permite uma condição de corrida entre `snd_ctl_elem_add` e `snd_ctl_elem_write_user_compat`, resultando na execução de `snd_ctl_elem_write` com um objeto `struct snd_kcontrol` liberado. O exploit utiliza a técnica de heap spray com jobs `REQ_SOFT_JIT_FREE` do driver Mali GPU para recuperar a memória liberada e forjar um objeto `snd_kcontrol` controlado pelo atacante. Ao controlar o ponteiro de função `kctl->put`, o atacante obtém uma primitiva de escrita arbitrária no kernel [6].

### 2.3. CVE-2023-21492: Kernel Pointer Leak via Log Files

**Componente Afetado:** Arquivos de log do sistema Android da Samsung.
**Tipo:** Information Disclosure.
**Impacto:** KASLR Bypass.

Ponteiros do kernel eram impressos incorretamente em arquivos de log acessíveis, permitindo que aplicativos não privilegiados lessem esses endereços e contornassem a mitigação KASLR (Kernel Address Space Layout Randomization). Esta vulnerabilidade foi ativamente explorada in-the-wild, frequentemente em conjunto com outras falhas (como CVE-2023-0266) para construir cadeias de exploração completas [7].

### 2.4. CVE-2021-25394 / CVE-2021-25395: Race Condition no Charging Driver

**Componente Afetado:** Driver do carregador MFC (MFC charger driver).
**Tipo:** Race Condition resultando em Use-After-Free.
**Impacto:** Escrita arbitrária no kernel.

Vulnerabilidades de condição de corrida no driver de carregamento permitiam corrupção de memória e Use-After-Free, possibilitando a escalada de privilégios locais [8].

## 3. Técnicas de Exploração e Mitigações no Exynos 990

### 3.1. Manipulação de Estruturas do Kernel

Após obter primitivas de leitura/escrita arbitrárias, os exploits modernos no Android focam na manipulação de estruturas de dados críticas:
- **`addr_limit` Overwrite:** Historicamente usado para obter acesso total à memória do kernel a partir do espaço de usuário, embora mitigado em kernels mais recentes.
- **`cred` Structure Manipulation:** Modificação da estrutura de credenciais do processo atual para obter UID/GID 0 (root).
- **`pipe_buffer` Overwrite:** Técnica comum para sequestrar o fluxo de controle ou obter primitivas de leitura/escrita, como visto no exploit do CVE-2022-22265 [5].

### 3.2. SELinux Bypass no Nível do Kernel

Com acesso de escrita ao kernel, o SELinux pode ser desativado ou contornado através de várias técnicas [9]:
1. **Overwriting the Enforcing Flag:** Escrever `0` na variável global `selinux_enforcing` ou no campo `enforcing` da estrutura `selinux_state`.
2. **Manipulating the Permissive Map:** Modificar o bitmap `permissive_map` no `policydb` para tornar um domínio específico (ex: `untrusted_app`) permissivo.
3. **AVC Cache Overwriting:** Sobrescrever a máscara de bits `allowed` em um `avc_node` no Access Vector Cache (AVC) para `0xFFFFFFFF`, forçando o kernel a permitir a operação sem consultar a política. Ataques de "Cross-Cache" são frequentemente usados para atingir nós AVC específicos na memória [9].

### 3.3. Mitigações da Samsung (RKP / KNOX)

A Samsung implementa o Real-time Kernel Protection (RKP) através de um hypervisor (executando em EL2) para proteger o kernel (EL1) [10]:
- **KDP (Kernel Data Protection):** Protege estruturas de dados sensíveis (como tabelas de páginas, `cred`, `vfsmount`, e o estado do SELinux) tornando-as somente leitura no nível do hypervisor (Stage 2 Translation). Isso bloqueia ataques diretos de sobrescrita da flag do SELinux ou do mapa permissivo [9] [10].
- **JOPP (Jump-Oriented Programming Prevention):** Solução CFI customizada que insere instruções NOP antes do início das funções e as substitui por um valor mágico verificado em tempo de execução.
- **ROPP (Return-Oriented Programming Prevention):** Proteção contra ROP que faz XOR do endereço de retorno na pilha com uma chave de thread (`rrk`) e uma chave mestre (`RRMK`), impedindo a falsificação de endereços de retorno sem o conhecimento das chaves [10].

Devido a essas mitigações (especialmente PAN/PXN e RKP), técnicas clássicas como `ret2usr` são inviáveis. Os atacantes dependem de Data-Only Attacks (modificação de estruturas de dados não protegidas pelo KDP) ou de vulnerabilidades no próprio hypervisor para obter execução de código [10].

## Referências

[1] Project Zero: A Very Powerful Clipboard: Analysis of a Samsung in-the-wild exploit chain. https://projectzero.google/2022/11/a-very-powerful-clipboard-samsung-in-the-wild-exploit-chain.html
[2] Project Zero: CVE-2021-25337: Samsung file system r/w in clipboard provider. https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2021/CVE-2021-25337.html
[3] Project Zero: CVE-2021-25369: Samsung kernel info leak in sec_log. https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2021/CVE-2021-25369.html
[4] NVD: CVE-2021-25370. https://nvd.nist.gov/vuln/detail/cve-2021-25370
[5] Javier Partido Rufo: CVE-2022-22265 Samsung npu driver. https://soez.github.io/posts/CVE-2022-22265-Samsung-npu-driver/
[6] Project Zero: Analyzing a Modern In-the-wild Android Exploit. https://projectzero.google/2023/09/analyzing-modern-in-wild-android-exploit.html
[7] SentinelOne: CVE-2023-21492: Samsung Android Privilege Escalation. https://www.sentinelone.com/vulnerability-database/cve-2023-21492/
[8] SentinelOne: CVE-2021-25394: Samsung Android Use After Free Vulnerability. https://www.sentinelone.com/vulnerability-database/cve-2021-25394/
[9] 8kSec: Android SELinux Internals Part III - Kernel-Level SELinux Bypass. https://8ksec.io/android-selinux-internals-part-iii/
[10] Longterm Security: A Samsung RKP Compendium. https://www.longterm.io/samsung_rkp.html


## USB-C Exynos 990

# Pesquisa Técnica: USB-C no Exynos 990 (Samsung Galaxy Note20 Ultra 5G)

## 1. Arquitetura de Hardware e Controladores

O Samsung Galaxy Note20 Ultra 5G (SM-N986B), equipado com o SoC Exynos 990, utiliza uma arquitetura complexa para gerenciar sua interface USB Type-C. O controlador principal é baseado no **Synopsys DesignWare Core (DWC3)**, configurado para suportar USB 3.2 Gen 1 (5 Gbps) e USB Power Delivery 3.0.

### 1.1. Controlador DWC3 (Synopsys DesignWare Core)
O controlador DWC3 no Exynos 990 é mapeado em um endereço base específico na memória física. Com base na análise do Device Tree do kernel Linux para a família Exynos, o controlador USB 3.0 (DWC3) é frequentemente mapeado no endereço base `0x10C00000` [1]. O gerenciamento do controlador é feito através de uma série de registros críticos mapeados em memória.

| Registro | Descrição | Função Principal |
| :--- | :--- | :--- |
| **DWC3_GCTL** | Global Core Control | Controla o modo de operação (Host, Device, OTG). |
| **DWC3_GSTS** | Global Status | Fornece o status atual do core. |
| **DWC3_DCFG** | Device Configuration | Usado para configurar o endereço do dispositivo durante a enumeração. O endereço é um valor de 7 bits no offset 3 (`DWC3_DCFG[3:7]`) [1]. |
| **DWC3_DCTL** | Device Control | Controla o estado do dispositivo (ex: Run/Stop). |
| **DWC3_GEVNTADRLO/HI** | Event Buffer Address | Registros usados para configurar o endereço do buffer de eventos na memória RAM [1]. |
| **DWC3_GEVNTSIZ** | Event Buffer Size | Define o tamanho do buffer de eventos na memória RAM [1]. |
| **DWC3_GEVNTCOUNT** | Event Count | Contém o número de eventos pendentes no buffer, aguardando processamento pelo driver [1]. |

### 1.2. Camada Física (PHY) e Conector Type-C
A camada física (PHY) é responsável pela sinalização elétrica. O Exynos 990 utiliza um PHY proprietário da Samsung (Exynos USB3 PHY) acoplado ao controlador DWC3. A sinalização para USB 2.0 ocorre de forma diferencial half-duplex nos pinos D+ e D-. Para o padrão USB 3.2 Gen 1 (SuperSpeed), o sistema utiliza pares diferenciais dedicados (TX1+/-, RX1+/-, TX2+/-, RX2+/-) operando a 5 Gbps com codificação 8b/10b. O treinamento de link utiliza sequências LFPS (Low Frequency Periodic Signaling).

O conector Type-C possui 24 pinos com funções específicas. Os pinos VBUS e GND são responsáveis pela alimentação e aterramento, suportando até 20V/5A com Power Delivery. Os pinos CC1 e CC2 (Configuration Channel) são usados para detecção de orientação, negociação de Power Delivery (BMC encoding) e entrada em Alternate Modes. Os pinos D+ e D- transmitem dados USB 2.0, enquanto os pares TX/RX transmitem dados SuperSpeed ou sinais DisplayPort. Por fim, os pinos SBU1 e SBU2 (Sideband Use) são empregados em Alternate Modes, como o canal AUX do DisplayPort.

## 2. Protocolos e Modos Alternativos

### 2.1. USB Power Delivery 3.0 (USB PD)
A negociação de energia ocorre sobre os pinos CC usando codificação BMC (Biphase Mark Coding). O formato da mensagem PD consiste em um cabeçalho de 16 bits seguido por objetos de dados de 32 bits (Data Objects). A sequência de negociação padrão inicia com o Source enviando `Source_Capabilities`. O Sink responde com um `Request`. O Source aceita com `Accept` e, após ajustar a tensão na linha VBUS, envia a mensagem `PS_RDY` (Power Supply Ready) para confirmar que a nova tensão está estável.

### 2.2. DisplayPort Alternate Mode e Samsung DeX
O Exynos 990 suporta DisplayPort 1.4 via USB-C Alternate Mode. Este modo geralmente utiliza as configurações de pinagem C, D ou E, onde os pares TX/RX de alta velocidade são reconfigurados no nível do hardware para transmitir sinais DisplayPort nativos em vez de pacotes USB. O protocolo Samsung DeX é ativado quando o dispositivo detecta um dock ou monitor compatível via DP Alt Mode. O sistema multiplexa dados de vídeo (DisplayPort) e dados USB (para teclado e mouse) simultaneamente sobre a mesma conexão física, permitindo uma experiência de desktop completa.

## 3. Interfaces de Debug e Ataques Físicos

### 3.1. Interfaces de Debug da Samsung
A Samsung implementa interfaces de debug de hardware acessíveis via porta USB-C, que são fundamentais para pesquisa de segurança e exploração de baixo nível. O acesso ao console serial (UART) do Application Processor (AP) ou do BootROM pode ser obtido conectando um resistor específico, frequentemente de 619 kΩ, entre o pino CC (historicamente o pino ID no micro-USB) e o GND [2]. Isso força o multiplexador USB interno a rotear os sinais UART de baixo nível para os pinos D+/D- ou SBU. Além disso, o processador de banda base (Cellular Processor - CP) expõe interfaces de diagnóstico. Em ambientes Linux, isso frequentemente aparece como o dispositivo `/dev/ttyACM0` (USB CDC ACM), permitindo o envio de comandos AT e acesso a logs de rádio [3].

### 3.2. Vetores de Ataque Físico e Lógico
A interface USB-C expõe o dispositivo a diversos vetores de ataque físico e lógico. Ataques do tipo BadUSB ou Rubber Ducky exploram a funcionalidade USB OTG (On-The-Go), onde o dispositivo atacante se apresenta como um teclado HID (Human Interface Device) e injeta keystrokes maliciosos rapidamente para comprometer o sistema. A manipulação de tensão via USB PD representa um risco físico, onde um carregador malicioso pode manipular as mensagens PD para forçar o fornecimento de 20V para um dispositivo que suporta apenas 5V, causando danos físicos aos circuitos de proteção (OVP) ou ao PMIC.

O Juice Jacking é outro vetor comum, envolvendo a exfiltração de dados ou instalação de malware quando o dispositivo é conectado a uma porta de carregamento pública comprometida que atua como um host USB malicioso. Embora o Exynos 990 não suporte nativamente Thunderbolt ou USB4 (que expõem o barramento PCIe diretamente), vulnerabilidades no controlador IOMMU ou no driver USB podem, teoricamente, permitir que periféricos maliciosos realizem ataques DMA (Direct Memory Access) para ler ou escrever na memória física do sistema.

## 4. Vulnerabilidades e CVEs (USB Stack)

A pilha USB do Android e os drivers específicos da Samsung têm um histórico de vulnerabilidades documentadas.

| CVE ID | Componente Afetado | Tipo de Vulnerabilidade | Impacto |
| :--- | :--- | :--- | :--- |
| **CVE-2023-20938** | Android USB Gadget Driver | Use-After-Free (UAF) | Escalonamento de Privilégios Local (LPE) |
| **CVE-2022-20009** | USB f_accessory Driver | Info Leak | Vazamento de memória do kernel, bypass de KASLR |
| **CVE-2026-21006** | Samsung DeX System UI | Falha Lógica / Auth Bypass | Acesso a notificações ocultas na tela de bloqueio [4] |

O CVE-2023-20938 afeta o driver USB gadget do kernel Linux usado pelo Android, permitindo que um atacante local escale privilégios através de uma falha de Use-After-Free. O CVE-2022-20009 reside no driver `f_accessory` (Android Open Accessory protocol) e permite o vazamento de informações da memória do kernel, uma técnica frequentemente usada para contornar o KASLR antes de executar um exploit de corrupção de memória. Além disso, vulnerabilidades lógicas no serviço Samsung DeX, como o CVE-2026-21006, podem permitir o bypass de autenticação na tela de bloqueio, concedendo acesso a notificações ocultas quando um monitor externo é conectado [4].

## Referências

[1] F. B., "Reverse engineer USB stack of Exynos BootROM," fredericb.info, Jun. 16, 2020. [Online]. Available: https://fredericb.info/2020/06/reverse-engineer-usb-stack-of-exynos-bootrom.html
[2] Grimler, "PCBite, my new best friend for getting UART logs," grimler.se, Nov. 26, 2023. [Online]. Available: https://grimler.se/posts/exynos-uart/
[3] Draisberghof, "Patch for supporting Samsung Android USB Modem," draisberghof.de, Feb. 19, 2014. [Online]. Available: https://www.draisberghof.de/usb_modeswitch/bb/viewtopic.php?t=1904
[4] SentinelOne, "CVE-2026-21006: Samsung Android Auth Bypass," sentinelone.com, Apr. 17, 2026. [Online]. Available: https://www.sentinelone.com/vulnerability-database/cve-2026-21006/


## Exynos 990 Low-Level

# Pesquisa Técnica: Samsung Exynos 990 - DRAM Controller, Memória Física e Ataques

Este documento apresenta uma pesquisa técnica exaustiva sobre o domínio de baixo nível do Samsung Galaxy Note20 Ultra 5G (SM-N986B, equipado com o SoC Exynos 990), focando especificamente no controlador DRAM, memória física e vetores de ataque associados.

## 1. Especificações do Controlador DRAM e LPDDR5

O Samsung Exynos 990 (S5E9830) utiliza um controlador de memória avançado projetado para suportar a tecnologia LPDDR5, marcando uma transição significativa em relação ao LPDDR4X utilizado em gerações anteriores [1] [2].

### 1.1. Arquitetura do Controlador
* **Tipo de Memória:** LPDDR5 (Low Power Double Data Rate 5) [1].
* **Configuração de Canais:** 4 canais de 16 bits (64-bit bus width total) [3].
* **Frequência de Operação:** Até 2750 MHz (5500 MT/s) [4].
* **Largura de Banda Máxima:** Aproximadamente 44 GB/s (calculado como 5500 MT/s * 64 bits / 8) [4].
* **Capacidade:** O Galaxy Note20 Ultra 5G (SM-N986B) é tipicamente equipado com 12 GB de LPDDR5 (ex: Samsung K3LK4K40BM-BGCN) em uma configuração Package-on-Package (PoP) sobre o SoC Exynos 990 [5].

### 1.2. Parâmetros de Temporização (Timing Parameters)
Embora os valores exatos de temporização sejam configurados dinamicamente pelo firmware de inicialização (BootROM/SBoot) com base no treinamento de memória (memory training), os parâmetros fundamentais do padrão JEDEC LPDDR5 aplicáveis incluem:
* **tRCD (Row Address to Column Address Delay):** Tempo necessário para abrir uma linha e acessar uma coluna.
* **tRP (Row Precharge Time):** Tempo necessário para fechar uma linha aberta.
* **tRAS (Row Active Time):** Tempo mínimo que uma linha deve permanecer ativa.
* **tRC (Row Cycle Time):** tRAS + tRP.
* **tRFC (Refresh Cycle Time):** Tempo necessário para executar uma operação de refresh.

## 2. Mapeamento de Memória Física e IOMMU

O Exynos 990, sendo baseado na arquitetura ARMv8-A (AArch64), implementa um espaço de endereçamento virtual de 64 bits, tipicamente configurado para 39 ou 48 bits no kernel Linux do Android [6].

### 2.1. Layout de Memória Física
O mapa de memória física é definido no Device Tree (DTS) do kernel e inclui regiões específicas para RAM e Memory-Mapped I/O (MMIO).
* **Kernel Space:** Tipicamente mapeado na metade superior do espaço de endereçamento virtual (ex: `0xFFFFFF8000000000` a `0xFFFFFFFFFFFFFFFF` para VA_BITS=39) [6]. O kernel image é carregado em um endereço físico base, sujeito a KASLR (Kernel Address Space Layout Randomization), que randomiza o endereço virtual onde a imagem do kernel é mapeada [7].
* **User Space:** Mapeado na metade inferior (ex: `0x0000000000000000` a `0x0000007FFFFFFFFF`) [6].
* **Regiões MMIO:** Utilizadas para acessar registradores de periféricos. O endereço base de qualquer mapeamento de memória no espaço do kernel consiste em um prefixo específico [8].
* **Carveout Regions:** Regiões de memória física reservadas exclusivamente para co-processadores, como a GPU (Mali-G77 MP11), NPU (Neural Processing Unit dual-core) e o modem (Shannon 5123) [9] [10]. A NPU, por exemplo, possui seu próprio firmware carregado em uma região de memória dedicada (ex: `FW_DRAM` em `0x50000000` com tamanho `0xe0000`) [7].

### 2.2. Samsung IOMMU (System MMU)
O Exynos 990 utiliza a System MMU (SMMU) da Samsung para fornecer tradução de endereços e proteção de memória para periféricos com capacidade de DMA (Direct Memory Access).
* **Função:** Isolar domínios de memória de diferentes aceleradores de hardware (GPU, NPU, DSP, Modem) [11].
* **Page Table Format:** Compatível com o formato de tabela de páginas ARM64, suportando tamanhos de página de 4KB, 16KB ou 64KB (o kernel Android tipicamente usa 4KB) [6].
* **Stream IDs:** Identificadores únicos usados pela SMMU para distinguir transações de diferentes dispositivos mestres.

## 3. Vetores de Ataque em Memória

A complexidade do controlador de memória e da arquitetura do sistema introduz várias superfícies de ataque.

### 3.1. Ataques Rowhammer em LPDDR5
O Rowhammer é uma vulnerabilidade física na DRAM onde ativações repetidas de uma linha (aggressor row) podem causar inversão de bits (bit flips) em linhas adjacentes (victim rows) devido a vazamento de carga [12].
* **Mitigação TRR (Target Row Refresh):** O LPDDR5 implementa mecanismos de TRR in-DRAM para rastrear e atualizar linhas adjacentes a linhas frequentemente ativadas [13].
* **Técnicas de Bypass:** Pesquisas recentes demonstraram que o TRR pode ser contornado.
    * **TRRespass:** Utiliza padrões de acesso multi-sided para esgotar os amostradores do TRR [14].
    * **Blacksmith:** Gera padrões de acesso não uniformes no domínio da frequência, explorando a sensibilidade da DRAM a diferentes frequências de ativação, demonstrando eficácia contra dispositivos DDR4 e LPDDR5 [15].
    * **Half-Double:** Explora o acoplamento de longo alcance, onde ativações em uma linha podem causar bit flips em linhas a duas distâncias de distância, contornando defesas que focam apenas em linhas imediatamente adjacentes [16].

### 3.2. Ataques Cold Boot
Ataques cold boot exploram a remanência de dados na DRAM após a perda de energia.
* **Mecanismo:** Resfriar os chips de memória (ex: com nitrogênio líquido) retarda o decaimento da carga nos capacitores, permitindo que a memória seja lida após um reset ou transferência para outro dispositivo [17].
* **Alvos:** Chaves criptográficas (ex: chaves de criptografia de disco do TrustZone/Keymaster) armazenadas na RAM [17].
* **Mitigações:** O TrustZone e o hardware do Exynos 990 tentam mitigar isso limpando a memória sensível durante o boot ou mantendo chaves em SRAM interna (iSE) quando possível [17].

### 3.3. Ataques DMA e IOMMU Bypass
Dispositivos periféricos comprometidos podem tentar usar DMA para ler ou escrever na memória do sistema.
* **IOMMU Bypass:** Se a SMMU estiver mal configurada ou possuir vulnerabilidades, um periférico (como a GPU ou NPU) pode acessar memória fora de sua região designada (carveout) [11].
* **Exemplo:** O ataque "GPUBreach" demonstrou como GPUs podem ser usadas para executar ataques Rowhammer, contornando restrições da IOMMU [18].

## 4. Alocador de Memória do Kernel e Exploração

O kernel Linux no Exynos 990 utiliza o alocador SLUB para gerenciar a memória do kernel.

### 4.1. Alocador SLUB e Caches
* **Arquitetura:** O SLUB divide páginas em objetos de tamanho fixo (caches), como `kmalloc-32`, `kmalloc-64`, etc [19].
* **SLAB_FREELIST_RANDOM:** Uma mitigação de segurança ativada por padrão que randomiza a ordem dos objetos livres (freelist) dentro de um slab, dificultando a previsão do endereço de um objeto recém-alocado [20].
* **RANDOM_KMALLOC_CACHES:** Uma mitigação mais recente que roteia alocações para caches kmalloc selecionados aleatoriamente, quebrando a previsibilidade de que objetos do mesmo tamanho compartilharão o mesmo cache [21].

### 4.2. Manipulação de Tabelas de Páginas ARM64 (PTE)
A exploração de vulnerabilidades de corrupção de memória frequentemente visa modificar as tabelas de páginas do kernel (Page Table Entries - PTEs) para obter execução de código ou escalonamento de privilégios.
* **Formato PTE (Descriptor de 64 bits):**
    * **Valid (Bit 0):** Indica se a entrada é válida [6].
    * **Table/Block (Bit 1):** Distingue entre descritores de tabela (apontam para o próximo nível) e descritores de bloco (mapeiam uma região contígua, ex: 2MB) [6].
    * **AP[2:1] (Bits 7:6):** Permissões de acesso (Access Permissions). `00` = R/W Kernel, No User; `01` = R/W Kernel, R/W User; `10` = R/O Kernel, No User; `11` = R/O Kernel, R/O User [6].
    * **PXN (Bit 53):** Privileged Execute Never. Impede a execução de código no nível de privilégio do kernel (EL1) [6].
    * **UXN (Bit 54):** Unprivileged Execute Never. Impede a execução de código no nível de usuário (EL0) [6].
    * **PBHA (Bits 63:59):** Page-Based Hardware Attributes (ARMv8.2+) [6].

### 4.3. Técnicas de Exploração de Kernel
* **Cross-Cache Attacks:** Exploram o mecanismo de reciclagem de páginas físicas no alocador de páginas (buddy allocator) para contornar a separação de caches do SLUB. Um atacante libera objetos em um cache vulnerável, forçando a página a ser devolvida ao alocador de páginas, e então a realoca em um cache alvo contendo objetos sensíveis (ex: credenciais) [22] [23].
* **Page-Level Heap Feng Shui:** Manipulação cuidadosa de alocações e liberações de memória para controlar o layout das páginas físicas, preparando o terreno para ataques cross-cache ou page spray [24].
* **Page Spray (Physmap Spray):** Uma técnica onde o atacante preenche a memória com dados controlados (payloads) e explora vulnerabilidades (como Use-After-Free em nível de página) para redirecionar a execução ou corromper estruturas críticas. A técnica "PageJack" demonstra como o UAF em nível de página pode ser explorado de forma confiável [24] [25].

## 5. Vulnerabilidades e Exploits Específicos (CVEs)

O ecossistema do Exynos 990 e seus componentes associados (como o modem Shannon e o BootROM) têm sido alvo de pesquisas de segurança.

### 5.1. BootROM Exploit (CVE-2024-56426)
* **Componente Afetado:** BootROM do Exynos 990 (e Exynos 9830) [26].
* **Tipo:** Execução de Código Arbitrário (ACE) no contexto do BootROM [26].
* **Impacto:** Permite contornar a verificação de assinatura do bootloader, possibilitando o carregamento de firmware customizado (custom boot chain) e chaves customizadas via USB (EUB mode) [26].
* **Detalhes:** O exploit "Usbliter8" (ou variações) explora o processamento USB no BootROM. O código de PoC público (ex: repositório `Creeeeger/CVE-2024-56426`) demonstra como enviar um payload (`Exynos990_boot_custom_key.bin`) para o endereço `0x02022000` e redirecionar a execução, permitindo o dump do BootROM e o flash de imagens modificadas (`sboot.bin`) [26].

### 5.2. Vulnerabilidades no NPU e Drivers
* **Componente Afetado:** Driver da NPU do Exynos 990 [7].
* **Impacto:** O Google Project Zero relatou vulnerabilidades no driver da NPU que podiam ser acessadas a partir do contexto SELinux `untrusted_app`, permitindo escalonamento de privilégios locais (LPE) [7].
* **Detalhes:** O driver mapeia memória compartilhada e interage com o firmware da NPU via mailboxes. Falhas na validação de comandos ou no gerenciamento de memória compartilhada (IOVMM) podem levar a corrupção de memória [7].

### 5.3. Vulnerabilidades no Modem Shannon 5123
* O Exynos 990 é frequentemente pareado com o modem Shannon 5123 (Exynos Modem 5123) [9].
* **Impacto:** Vulnerabilidades em modems baseband (frequentemente processando protocolos complexos como RRC, NAS) podem levar a Remote Code Execution (RCE) over-the-air (OTA).
* **Detalhes:** Embora CVEs específicos públicos com PoC para o Shannon 5123 no Exynos 990 sejam restritos, a arquitetura do modem, que possui seu próprio RTOS e processador ARM, é um alvo de alto valor. O modem compartilha memória com o Application Processor (AP) via carveouts e interfaces de memória compartilhada, que, se mal isoladas pela IOMMU, podem permitir que um modem comprometido ataque o kernel do AP [11].

## Referências

[1] TechInsights. "Samsung Galaxy S20 Ultra 5G Teardown Analysis". https://www.techinsights.com/blog/samsung-galaxy-s20-teardown-analysis
[2] Computing. "Samsung announces new 7nm mobile chipset Exynos 990".
[3] Wikipedia. "Exynos". https://en.wikipedia.org/wiki/Exynos
[4] Samsung Newsroom. "New Premium Mobile Processor and 5G Modem Unveiled".
[5] XDA Developers. "Samsung begins mass production of 16GB LPDDR5".
[6] Kernel Internals. "ARM64 Page Tables - Linux Kernel Internals". https://kernel-internals.org/arch/arm64/page-tables/
[7] Impalabs. "Reversing and Exploiting Samsung's NPU (Part 1)". https://blog.impalabs.com/2103_reversing-samsung-npu.html
[8] Common Criteria. "Samsung Electronics Co., Ltd. Samsung Galaxy Devices Security Target".
[9] TechInsights. "Samsung Galaxy S20 Ultra SM-G988B/DS Teardown".
[10] Jongse Park et al. "TNPU: Supporting Trusted Execution with Tree-less...".
[11] D. Cerdeira et al. "REZONE: Disarming TrustZone with TEE Privilege Reduction". USENIX Security 2022.
[12] M. Heckel et al. "FLIPPYRAM: A Large-Scale Study of Rowhammer". NDSS.
[13] JEDEC. "JESD209-5A: LPDDR5 SDRAM Standard".
[14] V. van der Veen et al. "TRRespass: Exploiting the Many Sides of Target Row Refresh".
[15] P. Jattke et al. "Blacksmith: Scalable Rowhammering in the Frequency Domain". IEEE S&P 2022.
[16] Google Project Zero. "Half-Double: New hammering technique for DRAM rowhammer bug".
[17] D. Cerdeira. "Towards Trustworthy TrustZone-Assisted TEEs". PhD Thesis.
[18] TechPowerUp. "GPUBreach is a Rowhammer Attack for GDDR6-Based NVIDIA GPUs that bypasses IOMMU".
[19] Kernel Internals. "kmalloc (SLUB) - Linux Kernel Internals".
[20] Linux Kernel Documentation. "Slab Allocator".
[21] Sam4k. "Exploring Linux's New Random Kmalloc Caches".
[22] ACM Digital Library. "Generalized and Stable Cross-Cache Attack on the Linux Kernel".
[23] C. Migliorelli. "Cross-Cache Attacks for the Linux Kernel via PCP Massaging". NDSS.
[24] arXiv. "Understanding Page Spray in Linux Kernel Exploitation". https://arxiv.org/html/2406.02624v1
[25] YouTube. "PageJack: A Powerful Exploit Technique With Page-Level UAF".
[26] GitHub. "Creeeeger/CVE-2024-56426: Unified BootROM Exploit". https://github.com/Creeeeger/CVE-2024-56426


## Samsung KNOX Exynos 990

# Arquitetura e Bypasses da Plataforma Samsung KNOX: Uma Análise Profunda do Galaxy Note20 Ultra 5G (Exynos 990)

## 1. Introdução à Arquitetura KNOX no Exynos 990

A plataforma Samsung KNOX representa uma das implementações de segurança móvel mais complexas e robustas do mercado, integrando proteções baseadas em hardware e software. No Samsung Galaxy Note20 Ultra 5G (SM-N986B), equipado com o SoC Exynos 990, a arquitetura de segurança é estruturada em múltiplas camadas de privilégio, aproveitando as extensões de virtualização ARMv8 (AArch64) e a tecnologia TrustZone [1].

O modelo de permissões do ARMv8 define quatro Níveis de Exceção (Exception Levels - EL) e dois estados de segurança (Secure e Non-Secure). O sistema operacional principal (Android) opera no ambiente Non-Secure (Rich Execution Environment - REE) em EL1, enquanto os aplicativos de usuário rodam em EL0. A plataforma KNOX introduz um hipervisor de segurança operando em EL2, que monitora e restringe as ações do kernel em EL1. Paralelamente, o ambiente Secure (Trusted Execution Environment - TEE) isola dados sensíveis e operações criptográficas [2].

## 2. Real-time Kernel Protection (RKP)

O Real-time Kernel Protection (RKP) é o componente central da segurança baseada em hipervisor da Samsung. No Exynos 990, o RKP opera em EL2 e utiliza a tradução de endereços de Estágio 2 (Stage 2 translation) para proteger a integridade do kernel em tempo real [3].

### 2.1. Arquitetura e Inicialização do RKP

Historicamente, o RKP era um hipervisor monolítico embutido no binário do kernel (`vmm.elf`). A partir de 2018, foi refatorado para um binário separado (`uh.bin`) carregado pelo bootloader (SBOOT). No Exynos 990, a arquitetura evoluiu para o framework H-Arx, que consiste em um núcleo comum (`harx.bin`) e plugins carregáveis, como o próprio hipervisor uH [2].

O SBOOT carrega o `harx.bin` no endereço físico `0xc0000000` e o inicializa através de uma chamada Secure Monitor Call (SMC) para o EL3. Posteriormente, o plugin uH é carregado no endereço `0xc1400000` e inicializado via Hypervisor Call (HVC) [2].

### 2.2. Proteção de Tabelas de Páginas

O RKP intercepta modificações nas tabelas de páginas do kernel (EL1) para impedir que código malicioso mapeie memória arbitrária ou altere permissões de execução. O hipervisor mantém sua própria visão das tabelas de páginas (Estágio 2) e força o kernel a solicitar permissão via HVC para qualquer alteração [3].

### 2.3. Kernel Data Protection (KDP)

O Kernel Data Protection (KDP) é uma solução de Data Flow Integrity (DFI) implementada pelo RKP. Ele marca estruturas de dados críticas do kernel como somente leitura (read-only) utilizando as tabelas de páginas do Estágio 2. Estruturas protegidas incluem:
- Tabelas de páginas do kernel
- Estruturas de credenciais (`struct cred`)
- Estruturas de segurança de tarefas (`struct task_security_struct`)
- Estruturas de montagem de sistemas de arquivos (`struct vfsmount`)
- Status do SELinux (impedindo a desativação do modo `enforcing`) [3].

### 2.4. Mitigações de Fluxo de Controle (JOPP e ROPP)

O RKP também suporta mitigações contra técnicas de exploração avançadas:
- **JOPP (Jump-Oriented Programming Prevention):** Uma solução de Control Flow Integrity (CFI) que insere instruções NOP antes do início de cada função durante a compilação. Um script Python substitui esses NOPs por um valor mágico (`0xbe7bad`) e branches indiretos por chamadas a uma função auxiliar (`jopp_springboard_blr_rX`). Esta função verifica a presença do valor mágico antes de permitir o salto, mitigando ataques JOP [3].
- **ROPP (Return-Oriented Programming Prevention):** Uma implementação de "stack canary" que protege endereços de retorno. O endereço de retorno é submetido a uma operação XOR com uma chave de thread (`rrk`) antes de ser empurrado para a pilha. A chave de thread é, por sua vez, submetida a um XOR com uma chave mestre (RRMK) armazenada no registrador de sistema `DBGBCR5_EL1`, configurado pelo hipervisor [3].

## 3. Defeat Exploit (DEFEX) e Process Authenticator (PROCA)

O DEFEX (Defeat Exploit) é um mecanismo de segurança que monitora o comportamento de aplicativos e processos em tempo real para detectar e prevenir operações ilegais, como escalonamento de privilégios. Ele restringe a execução de binários não assinados e impede a modificação de processos críticos [4].

O PROCA (Process Authenticator) trabalha em conjunto com o DEFEX para verificar a integridade de processos críticos do sistema, garantindo que não tenham sido adulterados ou injetados com código malicioso.

## 4. Knox Vault e Isolamento de Hardware

O Knox Vault, introduzido em dispositivos mais recentes e presente na arquitetura de segurança da Samsung, representa uma evolução do TrustZone. Enquanto o TrustZone opera no mesmo processador de aplicação (AP), o Knox Vault é um subsistema fisicamente isolado, com seu próprio processador seguro, memória (SRAM e ROM) e armazenamento não volátil [5].

### 4.1. Arquitetura do Knox Vault

O Knox Vault é composto por:
- **Knox Vault Subsystem:** Integrado ao SoC, possui um processador seguro, SRAM, ROM, um gerador de números aleatórios dedicado e um Crypto Engine.
- **Knox Vault Storage:** Um circuito integrado fisicamente externo ao SoC, conectado via um barramento I2C dedicado e criptografado [5].

### 4.2. Proteção de Dados Sensíveis

O Knox Vault armazena e processa:
- Chaves criptográficas (Android Keystore, Samsung Attestation Key - SAK)
- Templates biométricos (impressões digitais, reconhecimento facial)
- Credenciais de blockchain
- Senhas e PINs do dispositivo [5].

O isolamento físico protege contra ataques de canal lateral (side-channel attacks) baseados em software e ataques de injeção de falhas (fault injection). Sensores de hardware monitoram temperatura, voltagem e lasers para detectar tentativas de violação física [5].

## 5. Knox Attestation e Integridade do Dispositivo

O Knox Attestation é um mecanismo de verificação de integridade do dispositivo que permite a servidores remotos (como MDMs ou serviços bancários) confirmar que o dispositivo não foi comprometido. Ele verifica o status do bootloader, a integridade do kernel e o status do SELinux [6].

A atestação utiliza a Samsung Attestation Key (SAK), armazenada de forma segura no TrustZone ou Knox Vault, para assinar digitalmente os relatórios de integridade, garantindo que não possam ser forjados por malware operando no sistema operacional principal [6].

## 6. Vulnerabilidades e Bypasses (CVEs e Exploits)

Apesar da robustez da arquitetura KNOX, pesquisadores de segurança descobriram diversas vulnerabilidades ao longo dos anos, permitindo o bypass de suas proteções.

### 6.1. Vulnerabilidades no RKP (Project Zero)

O Google Project Zero documentou vulnerabilidades críticas no RKP da Samsung:
- **CVE-2017-XXXX (Issue 42452515):** Uma vulnerabilidade de remapeamento de Estágio 2 no RKP. O PoC demonstrou a capacidade de remapear o intervalo de endereços físicos do RKP e lê-lo a partir do EL1. A correção impediu a chamada do comando `rkp_set_init_page_ro` mais de uma vez durante a inicialização do kernel [7].
- **CVE-2017-XXXX (Issue 42452502):** Corrupção de memória no RKP na função `rkp_mark_adbd`. Verificada estaticamente em dispositivos como o Galaxy S7 Edge [8].

### 6.2. Vulnerabilidades no Exynos 990

O SoC Exynos 990 também foi alvo de vulnerabilidades específicas:
- **CVE-2025-54601:** Uma vulnerabilidade de condição de corrida (race condition) no Exynos, com potencial para exploração local [9].
- **CVE-2025-57835:** Vulnerabilidade de negação de serviço (DoS) no firmware do Exynos 990 [9].
- **Vulnerabilidade Zero-Day (Use-After-Free):** Um erro de use-after-free no componente móvel permitiu que aplicativos locais escalassem privilégios no sistema [10].

### 6.3. Bypasses de Software (Magisk, Zygisk, Shamiko e KnoxPatch)

A comunidade de modding desenvolveu ferramentas sofisticadas para contornar as restrições do KNOX em dispositivos com root:
- **Magisk e Zygisk:** O Magisk faz patch na partição de boot para injetar código no processo de inicialização, permitindo acesso root systemless. O Zygisk injeta código diretamente no processo Zygote do Android, permitindo a execução de módulos no contexto de aplicativos [11].
- **Shamiko:** Um módulo LSPosed projetado para ocultar o acesso root e módulos do Magisk de aplicativos que detectam root (como aplicativos bancários e o próprio KNOX) [12].
- **PlayIntegrityFix (PIF):** Um módulo Magisk que falsifica a atestação do dispositivo (spoofing) para contornar as verificações do Google Play Integrity e do Knox Attestation. Ele substitui os dados de atestação do dispositivo comprometido por dados de um dispositivo não modificado [13].
- **KnoxPatch:** Um módulo LSPosed que utiliza as APIs do Xposed para fazer patch em APIs do sistema em tempo real, contornando a "política de segurança" de aplicativos da Samsung (como Samsung Health, Secure Folder e Samsung Flow) que normalmente parariam de funcionar após o acionamento do eFuse do KNOX (status 0x1) [14].

## 7. Limitações da Arquitetura KNOX

Embora o RKP e o KDP ofereçam proteções formidáveis, eles possuem limitações inerentes:
- **Exploits de Kernel com R/W Arbitrário:** Se um atacante obtiver capacidades de leitura e escrita arbitrárias no kernel (arbitrary R/W), ele pode manipular estruturas de dados não protegidas pelo KDP ou encontrar caminhos de execução que não acionem as verificações do RKP.
- **Manipulação de Tabelas de Páginas da GPU:** O RKP foca principalmente nas tabelas de páginas da CPU. Vulnerabilidades nos drivers da GPU (como a série Mali) podem permitir a manipulação das tabelas de páginas da GPU para contornar as restrições de memória impostas pelo RKP, alcançando acesso a memória física protegida.

## Referências

[1] Samsung Knox | Encyclopedia MDPI. Disponível em: https://encyclopedia.pub/entry/34965
[2] Reversing Samsung's H-Arx Hypervisor Framework - Part 1. Disponível em: https://dayzerosec.com/blog/2025/03/08/reversing-samsungs-h-arx-hypervisor-part-1.html
[3] A Samsung RKP Compendium. Disponível em: https://blog.impalabs.com/2101_samsung-rkp-compendium.html
[4] Defeat Exploit | Fundamentals. Disponível em: https://docs.samsungknox.com/admin/fundamentals/whitepaper/samsung-knox-mobile-security/system-security/defeat-exploit/
[5] Knox Vault | Fundamentals. Disponível em: https://docs.samsungknox.com/admin/fundamentals/whitepaper/samsung-knox-mobile-security/system-security/knox-vault/
[6] Knox Platform for Enterprise White Paper. Disponível em: https://image-us.samsung.com/SamsungUS/samsungbusiness/solutions/topics/iot/071421/Knox-Whitepaper-v1.5-20210709.pdf
[7] Samsung: RKP information disclosure via s2-remapping. Disponível em: https://project-zero.issues.chromium.org/42452515
[8] Samsung: RKP Memory Corruption in "rkp_mark_adbd". Disponível em: https://project-zero.issues.chromium.org/42452502
[9] CVE-2025-54601: Samsung Exynos Race Condition Vulnerability. Disponível em: https://www.sentinelone.com/vulnerability-database/cve-2025-54601/
[10] Zero-day vulnerability in Exynos 990. Disponível em: https://www.zero-day.cz/database/924/
[11] Rooting Android in 2026: What Actually Works. Disponível em: https://theappninjas.com/blog/rooting-android-2026/
[12] Curated List of Essential Android Root Modules. Disponível em: https://gist.github.com/supermarsx/26a1ace8dd4fa9bb88c482e28d51de35
[13] PlayIntegrityFix GitHub Repository. Disponível em: https://github.com/KOWX712/PlayIntegrityFix
[14] KnoxPatch GitHub Repository. Disponível em: https://github.com/salvogiangri/KnoxPatch


## Exynos 990 PMU & Clocks

# Samsung Exynos 990 (SM-N986B) - Análise Profunda de Domínios de Baixo Nível

## 1. Arquitetura de Clock e Power Domains

O Samsung Exynos 990 (Exynos 9830) implementa uma arquitetura complexa de gerenciamento de energia e clock, controlada primariamente pela Power Management Unit (PMU) e pela Clock Management Unit (CMU).

### 1.1 Power Management Unit (PMU)
A PMU é o bloco central de gerenciamento de energia, localizada no endereço base `0x15860000`. O domínio `PMU_ALIVE` é projetado para permanecer ativo mesmo quando o sistema entra em estados de baixo consumo, como SLEEP ou AFTR, sendo responsável por gerenciar o despertar do sistema. O gerenciamento de energia é segmentado em múltiplos domínios de energia (Power Domains) para otimizar o consumo. O CPU M5 Cluster (Lion) atua como o domínio de alta performance, enquanto o CPU A76 Cluster serve como o domínio de performance intermediária e o CPU A55 Cluster como o domínio de eficiência energética. Além disso, existem domínios dedicados para a GPU (Mali-G77 MP11) e para a NPU (Dual-core).

As sequências de power-on e power-off para cada um desses domínios são armazenadas na PMU SRAM. A manipulação direta dos registradores da PMU permite o controle granular de energia, o que é essencial para gerenciar as transições de estado do sistema, incluindo C0 active, C1 WFI, C2 power-gating e cluster power-down.

### 1.2 Clock Management Unit (CMU) e Árvore de Clock
A hierarquia de clock do Exynos 990 é baseada em múltiplas Phase-Locked Loops (PLLs) que alimentam os diferentes domínios através de uma intrincada árvore de MUXes (Multiplexadores) e DIVs (Divisores). A tabela abaixo detalha as principais fontes PLL e seus respectivos alvos.

| Fonte PLL | Domínio Alvo | Frequência Máxima Aproximada |
| :--- | :--- | :--- |
| CPUCL0_PLL | Cluster Cortex-A55 | 2.0 GHz |
| CPUCL1_PLL | Cluster Cortex-A76 | 2.5 GHz |
| CPUCL2_PLL | Cluster Mongoose M5 | 2.73 GHz |
| G3D_PLL | GPU Mali-G77 | 800 MHz |
| MIF_PLL | Interface de Memória LPDDR5 | 2750 MHz |

A Clock Management Unit é dividida em vários blocos funcionais. O `CMU_TOP` atua como o controlador principal de clock, enquanto o `CMU_CORE` gerencia os clocks do barramento interno. Os controladores `CMU_CPUCL0`, `CMU_CPUCL1` e `CMU_CPUCL2` são dedicados aos clusters de CPU. A GPU é controlada pelo `CMU_G3D`, a interface de memória pelo `CMU_MIF` e a NPU pelo `CMU_NPU`. Adicionalmente, os blocos `CMU_PERIC0` e `CMU_PERIC1` controlam os periféricos, como USI, SPI e HSI2C.

### 1.3 Dynamic Voltage and Frequency Scaling (DVFS) e TMU
O sistema de Dynamic Voltage and Frequency Scaling (DVFS) ajusta dinamicamente a tensão e a frequência de operação para otimizar o consumo de energia e manter a temperatura dentro de limites seguros. O driver CPUFreq é responsável pelo DVFS da CPU, enquanto o driver Devfreq gerencia o DVFS da GPU, da interface de memória (MIF) e do barramento interno (INT).

A Thermal Management Unit (TMU) monitora a temperatura do SoC utilizando múltiplos sensores térmicos (tipicamente 5 ou mais) distribuídos estrategicamente pelo die. A TMU define pontos de disparo (Trip Points) categorizados como Alert, Hot e Critical. Quando esses pontos são atingidos, dispositivos de resfriamento (Cooling Devices) são ativados, incluindo o estrangulamento térmico (throttle) da frequência da CPU e da GPU, além do hotplug, que desliga núcleos de processamento para reduzir a dissipação de calor.

O comportamento térmico do chip pode ser modelado por equações físicas. A resistência térmica é definida pela equação $R_{th\_ja} = \frac{T_{junction} - T_{ambient}}{P_{dissipated}}$, onde $T_{junction}$ é a temperatura da junção, $T_{ambient}$ é a temperatura ambiente e $P_{dissipated}$ é a potência dissipada. A constante de tempo térmica é dada por $\tau = R_{th} \cdot C_{th}$, onde $C_{th}$ representa a capacitância térmica.

Em dispositivos com acesso root, os governors e as frequências máximas podem ser manipulados diretamente através do sistema de arquivos sysfs, permitindo contornar as restrições térmicas padrão. Por exemplo, os comandos abaixo definem o governor para performance e fixam a frequência máxima do cluster M5:

```bash
echo performance > /sys/devices/system/cpu/cpufreq/policy0/scaling_governor
echo 2730000 > /sys/devices/system/cpu/cpufreq/policy4/scaling_max_freq
```

## 2. Vulnerabilidades e Exploits (CVEs)

A pesquisa de segurança revelou diversas vulnerabilidades críticas afetando o Exynos 990, abrangendo componentes desde o BootROM até o kernel e a TrustZone. A tabela a seguir resume as principais vulnerabilidades identificadas.

| CVE ID | Componente Afetado | Tipo de Vulnerabilidade | Impacto |
| :--- | :--- | :--- | :--- |
| CVE-2024-56426 | BootROM / SBoot | Falha na verificação de assinatura | Execução de código arbitrário no BootROM (EUB) |
| CVE-2021-25467 | Vision DSP Kernel Driver | Out-of-Bounds (OOB) Write | Local Privilege Escalation (LPE) para root |
| CVE-2025-59440 | Firmware do Exynos 990 | Denial of Service (DoS) | Travamento do dispositivo ou do modem |
| CVE-2023-26073 | Shannon Baseband (NrmmMsgCodec) | Buffer Overflow | Remote Code Execution (RCE) no baseband |
| CVE-2024-44068 | Exynos 990 (Mídia/Gráficos) | Privilege Escalation | Local Privilege Escalation (LPE) |

### 2.1 Detalhes de Exploração do BootROM
A vulnerabilidade CVE-2024-56426 representa uma falha crítica na cadeia de confiança do BootROM e do SBoot. O exploit unificado permite contornar o Secure Boot através da interface Exynos Usb Booting (EUB). O ataque consiste em enviar payloads customizados, como `loader.bin` e `mem.bin`, via conexão USB. Isso possibilita o dump da memória do BootROM e a execução de código não assinado, permitindo o carregamento de bootloaders modificados e a quebra da cadeia de segurança desde o primeiro estágio de inicialização [1].

### 2.2 Exploração do Kernel e Baseband
No nível do kernel, a vulnerabilidade CVE-2021-25467 afeta o driver do Vision DSP. A falha reside no ELF Linker do driver, permitindo que um atacante local realize uma escrita fora dos limites (Out-of-Bounds Write) na memória alocada. Isso resulta em uma escalada de privilégios local (LPE), concedendo acesso root ao sistema [2].

No que diz respeito ao modem, a vulnerabilidade CVE-2023-26073 afeta o componente NrmmMsgCodec do Shannon Baseband. Uma falha no processamento de mensagens permite um estouro de buffer (Buffer Overflow), o que pode levar à execução remota de código (RCE) diretamente no processador do baseband, comprometendo as comunicações de rede do dispositivo [3].

### 2.3 TrustZone e TEE (TEEgris)
O Exynos 990 utiliza o TEEgris (versão 4.1) como seu Trusted Execution Environment (TEE). Pesquisas acadêmicas apontam para a superfície de ataque presente nas Peripheral MMUs e na comunicação entre o Normal World e o Secure World através de chamadas SMC (Secure Monitor Calls). Exploits de BootROM, como o CVE-2024-56426, frequentemente servem como o primeiro estágio para comprometer a cadeia de boot. Uma vez que a cadeia de boot é comprometida, torna-se possível contornar as proteções do Samsung Knox, permitindo a extração de chaves criptográficas ou a modificação de partições persistentes, facilitando o bypass do Factory Reset Protection (FRP).

## 3. Interfaces de Debug e Estruturas

O Exynos 990 expõe várias interfaces de baixo nível para depuração e recuperação. A interface EUB (Exynos Usb Booting) é um mecanismo de recuperação de baixo nível que é ativado automaticamente quando o bootloader primário falha ou pode ser forçado via hardware test points. Esta interface é o vetor primário utilizado pelo exploit CVE-2024-56426 para injetar payloads diretamente na memória do dispositivo.

No nível do sistema operacional, o kernel Linux expõe interfaces através do Sysfs e Debugfs. O diretório `/sys/kernel/debug/clk/` permite o monitoramento e controle detalhado da árvore de clocks, enquanto `/sys/class/regulator/` fornece acesso aos reguladores de tensão. Essas interfaces são fundamentais para a análise de performance e para o desenvolvimento de exploits que dependem da manipulação precisa dos estados de energia e frequência do SoC [4] [5].

## Referências
[1] Creeeeger. "Unified CVE-2024-56426 tooling for the Exynos 990". GitHub.
[2] Taszk Labs. "Kernel LPE in the Vision DSP Kernel Driver".
[3] SentinelOne Vulnerability Database. "CVE-2023-26073: Samsung Exynos Buffer Overflow Flaw".
[4] Linux Kernel Mailing List (LKML). Patches para suporte ao Exynos 990 (CMU_PERIC0/1).
[5] ExtremeXT. "android_kernel_samsung_exynos990". GitHub.


## Sensores SM-N986B

# Pesquisa Técnica: Sensores do Samsung Galaxy Note20 Ultra 5G (SM-N986B, Exynos 990)

Esta pesquisa detalha os aspectos técnicos, físicos, matemáticos e de programação dos sensores embarcados no Samsung Galaxy Note20 Ultra 5G (SM-N986B), focado no SoC Exynos 990. A análise abrange registros de hardware, comunicação I2C/SPI, arquitetura do sensor hub, técnicas de spoofing, ataques side-channel e exploração de vulnerabilidades.

## 1. LSM6DSO IMU (Acelerômetro e Giroscópio)

O LSM6DSO é um System-in-Package (SiP) da STMicroelectronics que integra um acelerômetro digital 3D e um giroscópio digital 3D.

### Especificações Técnicas e Registros I2C
- **Endereço I2C:** `0x6A` ou `0x6B` (dependendo do pino SDO/SA0).
- **Registros Principais:**
  - `WHO_AM_I` (`0x0F`): Retorna `0x6C`.
  - `CTRL1_XL` (`0x10`): Configuração do acelerômetro (ODR, full-scale, filtro).
  - `CTRL2_G` (`0x11`): Configuração do giroscópio.
  - `CTRL3_C` (`0x12`): Registro de controle (BDU, auto-incremento, reset).
  - `STATUS_REG` (`0x1E`): Status de dados prontos (DRDY).
  - `OUTX_L_A` a `OUTZ_H_A` (`0x28` a `0x2D`): Dados do acelerômetro (16-bit, complemento de 2).
  - `OUTX_L_G` a `OUTZ_H_G` (`0x22` a `0x27`): Dados do giroscópio (16-bit, complemento de 2).

### Fórmulas de Conversão
Para converter os valores brutos (16-bit) em unidades físicas:
- **Acelerômetro ($g$):** $A = \text{Raw} \times \text{Sensibilidade}$ (ex: $0.061 \text{ mg/LSB}$ para $\pm 2g$).
- **Giroscópio (dps):** $G = \text{Raw} \times \text{Sensibilidade}$ (ex: $4.375 \text{ mdps/LSB}$ para $\pm 125 \text{ dps}$).

### Vulnerabilidades e Hacking
- **CVE-2020-13466:** Embora associado a microcontroladores STM32, ataques de injeção de falhas (glitching) na linha de alimentação (VDD/VDDIO) do LSM6DSO podem corromper os registros de configuração, forçando o sensor a operar em modos não documentados ou ignorar interrupções.
- **I2C Fuzzing:** Acesso direto via `/dev/i2c-*` permite fuzzing dos registros não documentados (`0x00` a `0x0E`), potencialmente causando travamento do barramento I2C (SDA preso em LOW).

## 2. AK09918C Magnetômetro

O AK09918C da Asahi Kasei Microdevices é um compasso eletrônico de 3 eixos.

### Especificações Técnicas e Registros I2C
- **Endereço I2C:** `0x0C`.
- **Registros Principais:**
  - `WIA1` (`0x00`): Company ID, retorna `0x48`.
  - `WIA2` (`0x01`): Device ID, retorna `0x0C`.
  - `ST1` (`0x10`): Status 1 (Data Ready).
  - `HXL` a `HZH` (`0x11` a `0x16`): Dados magnéticos (16-bit).
  - `CNTL2` (`0x31`): Modo de operação (Power-down, Single measurement, Continuous).

### Fórmulas de Conversão
- **Densidade de Fluxo Magnético ($\mu T$):** $B = \text{Raw} \times 0.15 \text{ } \mu T/\text{LSB}$.

### Vulnerabilidades e Hacking
- **Manipulação de Bússola:** A injeção de campos magnéticos externos fortes satura o sensor (indicado pelo bit HOFL no registro `ST2` `0x18`). Atacantes podem usar bobinas eletromagnéticas próximas ao dispositivo para forçar leituras arbitrárias, afetando navegação e calibração.

## 3. LPS22HH Barômetro

O LPS22HH da STMicroelectronics é um sensor de pressão absoluta piezoresistivo.

### Especificações Técnicas e Registros I2C
- **Endereço I2C:** `0x5C` ou `0x5D`.
- **Registros Principais:**
  - `WHO_AM_I` (`0x0F`): Retorna `0xB3`.
  - `CTRL_REG1` (`0x10`): ODR e configuração de filtro passa-baixa.
  - `CTRL_REG2` (`0x11`): Reset de memória, One-Shot, I2C disable.
  - `PRESS_OUT_XL`, `L`, `H` (`0x28` a `0x2A`): Dados de pressão (24-bit).
  - `TEMP_OUT_L`, `H` (`0x2B` a `0x2C`): Dados de temperatura (16-bit).

### Fórmulas de Conversão
- **Pressão (hPa):** $P = \frac{\text{PRESS\_OUT}}{4096}$.
- **Temperatura (°C):** $T = \frac{\text{TEMP\_OUT}}{100}$.

## 4. Qualcomm QBT2000 Ultrasonic Fingerprint

O QBT2000 é um sensor de impressão digital ultrassônico sob a tela.

### Especificações Técnicas
- **Interface:** SPI (Serial Peripheral Interface).
- **Área do Sensor:** 4x9 mm.
- **Resolução:** 500 DPI.
- **Frequência Ultrassônica:** 8.1 MHz.
- **Tecnologia:** Array de transdutores piezoelétricos (PMUTs) que emitem pulsos ultrassônicos e medem o eco refletido pelas cristas e vales da impressão digital.

### Vulnerabilidades e Hacking
- **CVE-2024-43047:** Vulnerabilidade no driver DSP da Qualcomm (explorada in-the-wild). Permite execução de código no contexto do DSP, que gerencia o processamento de imagens do QBT2000.
- **Ataques de Spoofing:** O uso de materiais com impedância acústica semelhante à pele humana (ex: misturas específicas de gelatina e cola de madeira) pode enganar o sensor ultrassônico, refletindo o pulso de forma idêntica a um dedo real.
- **Interceptação SPI:** A comunicação entre o QBT2000 e o SoC via SPI pode ser interceptada fisicamente. O barramento opera em alta velocidade (tipicamente >10 MHz). A extração da imagem bruta (raw image) requer a decodificação do protocolo proprietário da Qualcomm e a quebra da criptografia (se implementada na camada de transporte).

## 5. Exynos CHUB (Context Hub)

O Exynos CHUB é um subsistema dedicado no SoC Exynos 990 para processamento de sensores de baixo consumo.

### Arquitetura
- **Processador:** ARM Cortex-M4F dedicado.
- **Memória:** SRAM interna para código e dados (nanoapps).
- **Comunicação:** Comunica-se com o Application Processor (AP) via interrupções e memória compartilhada (Mailbox/IPC).
- **Nanoapps:** Pequenos binários executados no CHUB que processam dados de sensores (ex: pedômetro, detecção de gestos) sem acordar o AP.

### Vulnerabilidades e Hacking
- **CVE-2021-25370 / CVE-2023-26073:** Vulnerabilidades no firmware do Exynos (como buffer overflows) podem ser exploradas para obter execução de código no CHUB.
- **Exploração:** Um atacante com privilégios no AP pode carregar um nanoapp malicioso no CHUB. Como o CHUB tem acesso direto aos barramentos I2C/SPI dos sensores, o nanoapp pode interceptar, modificar ou forjar dados de sensores antes que cheguem ao sistema operacional Android, burlando qualquer verificação de integridade no nível do kernel.

## 6. Técnicas de Sensor Spoofing e Side-Channel Attacks

### Spoofing via Software (Xposed/Magisk)
- Módulos como `XposedFakeLocation` e `LSPosed` interceptam chamadas da API do Android (`android.hardware.SensorManager`) para injetar dados falsos de GPS, acelerômetro e giroscópio.
- **Acesso Direto (`/dev/i2c-*`):** Com acesso root, um atacante pode descarregar o driver do kernel do sensor (`rmmod`) e interagir diretamente com o dispositivo I2C a partir do userspace usando `ioctl(I2C_RDWR)`. Isso permite ler e escrever registros arbitrariamente, ignorando a HAL do Android.

### Side-Channel Attacks
- **Keystroke Inference (Acelerômetro/Giroscópio):** A digitação em teclados virtuais gera micro-vibrações no dispositivo. Analisando os dados do LSM6DSO (especialmente em altas taxas de amostragem, ODR > 200Hz), é possível treinar modelos de Machine Learning para inferir as teclas pressionadas (PINs, senhas) com base na assinatura vibracional de cada região da tela.
- **Speech Reconstruction (Gyrophone):** O giroscópio MEMS (LSM6DSO) é sensível a vibrações acústicas. O artigo "Gyrophone" (BlackHat EU 2014) demonstrou que sinais acústicos de baixa frequência (<200Hz) podem ser captados pelo giroscópio. Embora a taxa de amostragem limite a reconstrução completa da fala, é suficiente para identificar o locutor e extrair informações parciais, servindo como um microfone improvisado sem requerer permissões de áudio (`RECORD_AUDIO`).

## Referências
[1] STMicroelectronics. "LSM6DSO Datasheet".
[2] Asahi Kasei Microdevices. "AK09918C Datasheet".
[3] STMicroelectronics. "LPS22HH Datasheet".
[4] Qualcomm. "Security Bulletins".
[5] Michalevsky, Y., Boneh, D., Nakibly, G. "Gyrophone: Recognizing Speech From Gyroscope Signals". BlackHat EU 2014.
[6] Google Project Zero. "The Qualcomm DSP Driver - Unexpectedly Excavating an Exploit".


## Firmwares Exynos 990

# Pesquisa Técnica Exaustiva: Firmwares Proprietários no Exynos 990 (SM-N986B)

Este documento apresenta uma análise técnica profunda sobre os firmwares proprietários e blobs binários carregados em tempo de execução no SoC Samsung Exynos 990, utilizado no Galaxy Note20 Ultra 5G (SM-N986B). A pesquisa foca em especificações físicas, endereços de memória, CVEs, exploração de vulnerabilidades e arquitetura de baixo nível.

## 1. Arquitetura de Firmwares e Blobs Binários

O Exynos 990 depende de múltiplos microcontroladores e processadores auxiliares, cada um exigindo seu próprio firmware proprietário carregado durante o boot ou em tempo de execução pelo kernel Linux.

### 1.1. Lista de Firmwares Carregados em Runtime

Abaixo está a relação dos principais firmwares carregados no Exynos 990:

| Componente | Caminho do Firmware | Descrição Técnica |
|------------|---------------------|-------------------|
| **WiFi (Broadcom)** | `/vendor/firmware/bcm4375/*` | Firmware do chip BCM4375. Formato binário proprietário. |
| **Bluetooth** | `/vendor/firmware/bcm4375*.hcd` | Patch RAM para o controlador Bluetooth integrado ao BCM4375. |
| **Modem (Shannon)** | `/dev/block/by-name/radio` | Baseband Shannon 5123. RTOS proprietário (Shannon OS). |
| **GPU (Mali)** | `/vendor/firmware/mali_*` | Firmware para a GPU ARM Mali-G77 MP11. |
| **NPU** | `/vendor/firmware/npu_*` ou `/data/NPU.bin` | Firmware da Neural Processing Unit. Carregado no endereço físico `0x50000000` (tamanho `0xe0000`). |
| **GNSS** | `/vendor/firmware/gnss_*` | Firmware do receptor GPS/GNSS. |
| **Sensor Hub (CHUB)** | `/vendor/firmware/chub_*` | Context Hub (CHUB) executando nanoapps para processamento de sensores de baixo consumo. |
| **Audio DSP (ABOX)** | `/vendor/firmware/abox_*` | Firmware do processador de sinal digital de áudio. |
| **Display (DDIC)** | `/vendor/firmware/s6e3hab_*` | Firmware do controlador de display. |
| **Touch** | `/vendor/firmware/tsp_*` | Firmware do painel de toque. |
| **S Pen** | `/vendor/firmware/spen_*` | Firmware do digitalizador da S Pen (específico da linha Note). |

### 1.2. Formato e Assinatura de Firmware

Os firmwares no ecossistema Samsung geralmente seguem um formato de contêiner que inclui um cabeçalho (header) e o payload. Componentes críticos como o Bootloader (`sboot.bin`), TrustZone (`tzsw.img`) e Modem são estritamente assinados usando RSA-2048/4096 e verificados pela cadeia de confiança (Secure Boot).

O Bootloader (`sboot.bin`) contém o código de inicialização secundária. O exploit CVE-2024-56426 demonstra a capacidade de contornar a verificação de assinatura no BootROM, permitindo a execução de código arbitrário [1]. O firmware do modem Shannon (`modem.bin`) é um blob binário de aproximadamente 40MB. Pode ser extraído da partição `radio` ou de dumps de RAM. Ferramentas como o `ShannonLoader` para Ghidra são usadas para análise reversa [2]. O driver do kernel aloca memória DRAM para o firmware da NPU (`NPU.bin`) e o carrega. O log do kernel indica alocações como `DRAM log buffer for firmware: size(2097152) / dv(0x0000000080000000) / kv(ffffff803db75000)` [3].

## 2. Vulnerabilidades e Exploração (CVEs)

A análise de segurança revela múltiplas vulnerabilidades críticas nos componentes de firmware do Exynos 990.

### 2.1. BootROM e Bootloader

O exploit unificado CVE-2024-56426 permite a execução de código no contexto do BootROM via interface USB (EUB mode - Emergency USB Boot). O dispositivo é forçado a entrar no modo EUB substituindo o `sboot.bin.lz4` por uma imagem modificada. O exploit envia um payload (`Exynos990_boot_custom_key.bin`) e redireciona a execução para o endereço `0x02022000`. Isso permite o carregamento de um bootloader customizado (`sboot.bin`, `tzsw.img`, `ldfw.img`) assinado com uma chave RSA controlada pelo atacante, efetivamente contornando o Knox e o Secure Boot [1].

### 2.2. Modem Shannon 5123 (Baseband)

O modem Shannon 5123 é um alvo frequente devido à sua complexidade e processamento de dados não confiáveis da rede celular. A vulnerabilidade CVE-2023-26073 ocorre no componente `NrmmMsgCodec` durante o processamento de mensagens 5G NAS (Non-Access Stratum). Ao decodificar a lista estendida de números de emergência, a função falha em validar o comprimento dos dados antes de copiá-los para um buffer alocado na heap. Um atacante pode enviar uma mensagem 5G MM maliciosa via rede celular para desencadear o overflow e executar código no RTOS do baseband [4].

A falha CVE-2025-62818 reside na lógica que processa pacotes SMS Transport Protocol User Data (TP-UD). Há uma incompatibilidade entre o indicador TP-UDHI (User Data Header Indicator) e o valor UDL (User Data Length). O parser usa o UDL para dimensionar a cópia, mas não reconcilia com o comprimento real do cabeçalho. Se `header_length + payload_length` exceder o buffer de recepção, ocorre uma gravação fora dos limites [5].

As vulnerabilidades de segmentação L2 (CVE-2023-41111, CVE-2023-41112) afetam a camada 2 (RLC/LLC) do modem Shannon. O CVE-2023-41111 permite transbordar o array usado para armazenar descritores de fragmentos de quadros de dados LLC. O CVE-2023-41112 é um heap overflow clássico em loops de cópia durante o procedimento de remontagem. A exploração envolve manipular o alocador de front-end (`mid4`) do heap do baseband, que usa slots de pool com cabeçalhos de 32 bytes e um valor de guarda fixo (`0xAA`) [6].

### 2.3. WiFi BCM4375 e GPU ARM Mali-G77

Conhecida como Kr00k (CVE-2019-15126), a vulnerabilidade faz com que o chip WiFi BCM4375 use uma chave de sessão composta apenas por zeros (all-zero encryption key) para criptografar parte do tráfego após uma desassociação (disassociation). Isso permite que um atacante próximo intercepte e descriptografe pacotes de dados [7].

Vulnerabilidades no driver da GPU Mali (como CVE-2025-21043) frequentemente permitem que aplicativos não confiáveis (untrusted apps) escalem privilégios para o kernel. O acesso direto à memória física ou a manipulação de estruturas de dados do driver (como `dma_buf`) são vetores comuns [8].

| CVE ID | Componente | Tipo de Vulnerabilidade | Impacto |
|--------|------------|-------------------------|---------|
| CVE-2024-56426 | BootROM / Bootloader | Contorno de Verificação de Assinatura | Execução de Código Arbitrário (ACE) |
| CVE-2023-26073 | Modem Shannon 5123 | Heap-based Buffer Overflow (CWE-787) | Remote Code Execution (RCE) |
| CVE-2025-62818 | Modem Shannon 5123 | Out-of-bounds Write (CWE-787) | RCE ou Denial of Service (DoS) |
| CVE-2023-41111 | Modem Shannon (L2) | Logic Bug | RCE |
| CVE-2023-41112 | Modem Shannon (L2) | Heap Overflow | RCE |
| CVE-2019-15126 | WiFi BCM4375 | Information Disclosure | Descriptografia de tráfego WPA2 |
| CVE-2025-21043 | GPU ARM Mali-G77 | Use-After-Free (UAF) | Local Privilege Escalation (LPE) |

## 3. Interfaces de Debug e Análise

A Samsung frequentemente deixa artefatos de debug em seus kernels de produção. No Exynos 990, o driver da NPU expõe várias interfaces via `debugfs` e `dmesg`. Quando o driver da NPU é inicializado, ele cria entradas em `/d/npu/`, como `SRAM-IDP` e `SRAM-TCU` para acesso à memória SRAM, `fw-log-SRAM` para logs do firmware e `proto-drv-dump` para dump do driver de protocolo [3].

A extração do `modem.bin` pode ser feita descompactando o firmware oficial (LZ4) e extraindo a partição CP. A análise no Ghidra requer o `ShannonLoader` para mapear corretamente os segmentos de memória e o script `ShannonTraceEntry.py` para recuperar strings de debug (`log_printf`) [2]. O `sboot.bin` pode ser extraído de arquivos `.tar` do firmware (ex: `BL_G986BXXSNHYB1.tar`). A análise requer a identificação do endereço base de carregamento (load address) e a compreensão da estrutura do cabeçalho proprietário da Samsung [1].

## 4. Implicações de Segurança (Supply Chain e Backdoors)

A dependência de múltiplos blobs binários proprietários cria uma vasta superfície de ataque. Comprometimentos nos fornecedores (ex: Broadcom para WiFi) afetam diretamente a segurança do dispositivo. A capacidade de executar código no BootROM (CVE-2024-56426) ou no Baseband permite a instalação de implantes persistentes que sobrevivem a formatações (factory resets) e atualizações de sistema operacional, operando abaixo do nível de visibilidade do kernel Linux e do Android.

## Referências

[1] Creeeeger. "Exynos 990 / Exynos9830 Unified BootROM Exploit". GitHub. https://github.com/Creeeeger/CVE-2024-56426/blob/exynos990/USER_GUIDE.md
[2] grant-h. "ShannonBaseband: Scripts, plugins, and information to help reverse engineer Samsung's EXYNOS cellular baseband platform". GitHub. https://github.com/grant-h/ShannonBaseband
[3] Longterm Security. "Reversing and Exploiting Samsung's Neural Processing Unit". https://blog.longterm.io/samsung_npu.html
[4] SentinelOne. "CVE-2023-26073: Samsung Exynos Buffer Overflow Flaw". https://www.sentinelone.com/vulnerability-database/cve-2023-26073/
[5] SentinelOne. "CVE-2025-62818: Samsung Exynos 990 Buffer Overflow Vulnerability". https://www.sentinelone.com/vulnerability-database/cve-2025-62818/
[6] Taszk Labs. "Exploiting New Attack Surfaces in Radio Layer 2 for Baseband Remote Code Execution". https://labs.taszk.io/articles/post/there_will_be_bugs/
[7] Strobes VI. "CVE-2019-15126 - CVE Details, Severity, and Analysis". https://strobes.co/vi/cve/CVE-2019-15126/
[8] Zero-day Vulnerability Database. "Information disclosure in ARM Mali GPU kernel". https://www.zero-day.cz/database/


## Exynos 990 Debug & JTAG

# Pesquisa Técnica Exaustiva: Samsung Exynos 990 - Debug Interfaces e JTAG/SWD

## 1. Arquitetura de Debug ARM CoreSight no Exynos 990

O Samsung Exynos 990 (SM-N986B, Galaxy Note20 Ultra 5G) implementa a arquitetura de debug ARM CoreSight, que fornece capacidades avançadas de rastreamento e depuração em nível de hardware.

### 1.1 Componentes CoreSight
*   **ETM (Embedded Trace Macrocell):** Responsável pelo rastreamento de instruções e dados em tempo real. No Exynos 990, o ETM permite a reconstrução do fluxo de execução do processador, crucial para análise de vulnerabilidades e engenharia reversa de baixo nível.
*   **ETB (Embedded Trace Buffer):** Um buffer de memória on-chip que armazena os dados de rastreamento gerados pelo ETM. Isso permite a captura de traces sem a necessidade de hardware externo de alta velocidade, embora com capacidade limitada.
*   **CTI (Cross Trigger Interface):** Facilita a comunicação de eventos de debug entre diferentes componentes do SoC. Permite, por exemplo, que um breakpoint em um núcleo pare a execução em outros núcleos ou acione o rastreamento no ETM.
*   **TPIU (Trace Port Interface Unit):** Formata e transmite os dados de rastreamento do ETB ou diretamente do ETM para pinos externos, permitindo a captura por analisadores lógicos externos.

## 2. Interfaces Físicas de Debug: JTAG e SWD

O acesso de baixo nível ao hardware é tradicionalmente realizado através de interfaces padronizadas.

### 2.1 JTAG (Joint Test Action Group - IEEE 1149.1)
O protocolo JTAG utiliza uma máquina de estados (TAP controller) e cinco pinos principais:
*   **TCK (Test Clock):** Sinal de clock para a interface.
*   **TMS (Test Mode Select):** Controla a transição de estados no TAP controller.
*   **TDI (Test Data In):** Entrada serial de dados e instruções.
*   **TDO (Test Data Out):** Saída serial de dados.
*   **nTRST (Test Reset - opcional):** Reset assíncrono do TAP controller.

No Exynos 990, o JTAG permite operações de *boundary scan* (teste de interconexões físicas) e acesso direto aos registradores internos do processador, memória e periféricos, contornando as restrições do sistema operacional.

### 2.2 SWD (Serial Wire Debug)
Uma alternativa de 2 pinos ao JTAG, desenvolvida pela ARM, otimizada para dispositivos com restrição de pinos:
*   **SWDIO (Serial Wire Data Input/Output):** Pino bidirecional para dados.
*   **SWCLK (Serial Wire Clock):** Sinal de clock.

O SWD oferece funcionalidades de debug equivalentes ao JTAG, mas com menor contagem de pinos, sendo frequentemente utilizado em dispositivos móveis modernos onde o espaço na placa de circuito impresso (PCB) é crítico.

## 3. Restrições de Debug da Samsung (Secure JTAG)

Para proteger a propriedade intelectual e os dados do usuário, a Samsung implementa restrições rigorosas de debug em dispositivos de produção.

### 3.1 Secure JTAG e eFuse
O acesso JTAG padrão (DJTAG) é desabilitado fisicamente em dispositivos de produção através da queima de eFuses (fusíveis eletrônicos) durante a fabricação. A reativação do JTAG (Secure JTAG) requer um processo de autenticação *challenge-response*.

1.  O dispositivo gera um *challenge* criptográfico.
2.  O depurador externo deve fornecer uma *response* válida, calculada usando uma chave criptográfica específica do dispositivo ou um certificado de debug assinado pela Samsung.
3.  A validação da *response* é frequentemente gerenciada pelo TrustZone ou por um coprocessador de segurança dedicado (como o Knox Vault Processor).

Se a autenticação falhar, os pinos JTAG permanecem inativos ou fornecem acesso restrito (ex: apenas *boundary scan*, sem acesso ao núcleo).

## 4. UART Debug e Ramdump

### 4.1 UART Debug
A interface UART (Universal Asynchronous Receiver-Transmitter) é frequentemente usada para logs de boot e depuração de baixo nível.
*   **S-Boot UART Output:** O bootloader da Samsung (S-Boot) pode emitir logs detalhados via UART durante a inicialização.
*   **Baudrates Comuns:** 115200 ou 921600 bps.
*   **Acesso Físico:** Os sinais UART (TX/RX) podem estar disponíveis em *testpoints* (TP*) na PCB ou multiplexados no conector USB-C. Cabos especiais (como o cabo Anydata USB com um resistor de identificação específico) podem ser necessários para rotear os sinais UART para o conector externo.

### 4.2 Ramdump Mode
O modo Ramdump é um mecanismo de diagnóstico crítico acionado por falhas severas do sistema (ex: *kernel panic* ou *watchdog timeout*).
*   **Mecanismo:** O conteúdo da memória DRAM é despejado em partições específicas (ex: `/data/log/ramdump_*`).
*   **Análise:** Os dumps de memória podem ser analisados offline usando ferramentas como o `crash utility` para investigar a causa raiz da falha, examinar estruturas de dados do kernel e extrair informações sensíveis.

### 4.3 CP Debug (Modem Shannon)
O processador celular (CP), ou modem baseband (família Shannon na Samsung), possui seus próprios mecanismos de debug.
*   **Modem Crash Dump:** Semelhante ao ramdump do processador de aplicação (AP), o modem pode gerar dumps de memória (ex: via `/dev/umts_ramdump`) em caso de falha.
*   **Comandos AT de Debug:** O modem Shannon suporta comandos AT proprietários para configuração e depuração, como `AT+SYSDBG` e `AT+DEBUGLVC`. Esses comandos podem expor interfaces de diagnóstico ou alterar o nível de log do modem.

## 5. Técnicas de Reativação de Debug e Exploits

Pesquisadores de segurança exploram diversas técnicas para contornar as restrições de debug e obter acesso de baixo nível.

### 5.1 eFuse Bypass via Glitching (Fault Injection)
Ataques de injeção de falhas (ex: *voltage glitching* ou *clock glitching*) tentam perturbar a execução do processador no momento exato em que ele lê o estado do eFuse.
*   **Objetivo:** Fazer com que o hardware interprete incorretamente um eFuse "queimado" (Secure JTAG ativado) como "intacto" (JTAG aberto), ou pular a instrução que verifica o eFuse.
*   **Desafio:** Requer precisão extrema de temporização e controle de tensão. A Samsung implementa contramedidas de hardware para detectar e mitigar *glitches*.

### 5.2 JTAG Enable via TrustZone Exploit
Se a lógica de autenticação do Secure JTAG for gerenciada por software no TrustZone (Secure World), vulnerabilidades nesse código podem ser exploradas.
*   **Mecanismo:** Um exploit no TrustZone (ex: *buffer overflow* em um *Trusted Application* responsável pela autenticação) pode ser usado para forçar a validação do *challenge-response* ou alterar diretamente os registradores de controle do JTAG para habilitar a interface.

### 5.3 Debug Certificate Injection
Se o processo de Secure JTAG depender de certificados assinados, vulnerabilidades no parser de certificados ou no gerenciamento de chaves podem permitir a injeção de certificados forjados.
*   **Mecanismo:** Explorar falhas criptográficas ou lógicas para fazer o dispositivo aceitar um certificado de debug não autorizado, concedendo acesso JTAG.

## 6. Vulnerabilidades e CVEs Relevantes (Exynos 990)

A pesquisa identificou várias vulnerabilidades críticas que afetam o Exynos 990 e componentes associados.

### 6.1 CVE-2024-56426: Unified BootROM Exploit
*   **Componente Afetado:** BootROM (Exynos 990 / 9830).
*   **Tipo:** Vulnerabilidade no processo de boot seguro.
*   **Impacto:** Permite a execução de código arbitrário no nível do BootROM, comprometendo toda a cadeia de confiança (Root of Trust).
*   **Detalhes:** O exploit (disponível publicamente) permite o carregamento de um *bootloader* modificado (SBoot) e a execução de payloads customizados, contornando as verificações de assinatura. Isso possibilita o acesso de baixo nível e a potencial reativação de interfaces de debug.

### 6.2 CVE-2025-54329: Samsung Exynos NAS Heap Overflow
*   **Componente Afetado:** Modem Shannon (Camada NAS - Non-Access Stratum).
*   **Tipo:** Heap-based Buffer Overflow (CWE-122).
*   **Impacto:** Remote Code Execution (RCE) no processador baseband.
*   **Detalhes:** A vulnerabilidade ocorre na função responsável por enviar múltiplas mensagens de payload (incluindo SMS) na camada NAS. A falta de verificação adequada dos limites do buffer permite que um atacante remoto (ex: via uma estação base falsa) envie mensagens NAS malformadas, causando um *overflow* no *heap* e potencialmente executando código arbitrário no modem.

### 6.3 Vulnerabilidades no NPU (Neural Processing Unit)
*   **Componente Afetado:** Driver do NPU e Firmware.
*   **Tipo:** Múltiplas vulnerabilidades (ex: *Out-of-Bounds Read/Write*, *Use-After-Free*).
*   **Impacto:** Local Privilege Escalation (LPE) a partir do contexto `untrusted_app`.
*   **Detalhes:** Pesquisas do Google Project Zero demonstraram que vulnerabilidades no driver do NPU (acessível por aplicativos não confiáveis) podem ser exploradas para obter execução de código no kernel ou no próprio firmware do NPU, fornecendo um vetor para escalonamento de privilégios e acesso a recursos restritos.

### 6.4 Vulnerabilidades no TrustZone (S-Boot e TEEGRIS)
*   **Componente Afetado:** S-Boot (Secure Bootloader) e TEEGRIS (TrustZone OS).
*   **Tipo:** Buffer Overflow no modo ODIN (S-Boot).
*   **Impacto:** Arbitrary Code Execution no S-Boot (EL1/EL3).
*   **Detalhes:** Pesquisadores demonstraram que o comando de flash no modo ODIN não verificava corretamente o tamanho da imagem, levando a um *buffer overflow*. Isso permitiu a sobrescrita de segmentos de código e a execução de *shellcode* no bootloader seguro, comprometendo as proteções do Knox e potencialmente permitindo o acesso a interfaces de debug de baixo nível.

## Referências
[1] NXP Semiconductors. "Secure JTAG - AN4686". Disponível em: https://docs.nxp.com/bundle/AN4686/page/topics/secure_jtag.html
[2] H. Shan et al. "CROWBAR: Natively Fuzzing Trusted Applications Using ARM CoreSight". Springer, 2023.
[3] G. Beniamini. "Trust Issues: Exploiting TrustZone TEEs". Google Project Zero, 2017.
[4] Longterm Security. "Reversing and Exploiting Samsung's Neural Processing Unit".
[5] ZeroPath. "Samsung Exynos NAS Heap Overflow (CVE-2025-54329)".
[6] FuzzingLabs. "Breaking Down The Baseband - Shannon In A Nutshell".
[7] Creeeeger. "CVE-2024-56426: Exynos 990 / Exynos9830 Unified BootROM Exploit". GitHub.
[8] Quarkslab. "A Deep Dive Into Samsung's TrustZone (Part 1)".
[9] A. Tarasikov. "Reverse-engineering Samsung Exynos 9820 bootloader and TZ".
[10] TeamT5. "BlackHat's Talk: Breaking Samsung's Root of Trust - Exploiting Samsung Secure Boot".
[11] XDA Developers Forum. "[Theory] Knox eFuse Bypass via Sustained Undervolting during bootloader unlock".


## Exynos 990 SELinux & Sandbox Escape

# Pesquisa Técnica: Samsung Exynos 990 - SELinux Policies e Sandbox Escape

## 1. Introdução ao SELinux no Ecossistema Samsung (Exynos 990)

O Samsung Galaxy Note20 Ultra 5G (SM-N986B), equipado com o SoC Exynos 990, implementa uma arquitetura de segurança robusta baseada no Security-Enhanced Linux (SELinux) em conjunto com o Samsung Knox e o Real-time Kernel Protection (RKP). O SELinux opera em *enforcing mode* por padrão, utilizando Type Enforcement (TE) e Multi-Level Security/Multi-Category Security (MLS/MCS) para isolamento rigoroso de processos e dados [1].

A Samsung estende as políticas base do Android Open Source Project (AOSP) com domínios e contextos específicos para suportar seus serviços proprietários e o container Knox.

### 1.1. Domínios Críticos e Contextos Específicos

Os processos no Android são confinados a domínios específicos. No ecossistema Samsung, destacam-se:

*   `untrusted_app`: Domínio padrão para aplicativos de terceiros. Um contexto típico apresenta o formato `u:r:untrusted_app:s0:c132,c256,c512,c768`, onde `c*` representa as categorias MLS/MCS utilizadas para isolamento de dados entre aplicativos e containers Knox [1].
*   `platform_app`: Aplicativos assinados com a chave da plataforma.
*   `system_server`: Processo central do sistema Android (`u:r:system_server:s0`), executando com UID 1000 (`AID_system`). Possui privilégios elevados para gerenciar serviços críticos [2].
*   `init`: Processo inicial do sistema, responsável por configurar o ambiente e iniciar serviços.
*   `kernel`: Domínio do kernel do Linux (`u:r:kernel:s0`).
*   `vendor_*` e `hal_*`: Domínios para processos e serviços específicos do hardware (Hardware Abstraction Layer), isolados pelo Project Treble.

### 1.2. Transições de Domínio e Regras de Acesso

As transições de domínio ocorrem quando um processo executa um binário e o novo processo assume um contexto diferente. Isso é frequentemente gerenciado pela macro `domain_auto_trans(olddomain, type, newdomain)` [3].

As regras de acesso seguem o formato `allow source target:class permissions;`. Por exemplo, uma regra permissiva (frequentemente encontrada em políticas de fornecedores) pode ser: `allow untrusted_app gpu_device:chr_file { append getattr ioctl lock map open read write };` [4].

## 2. Vulnerabilidades de Sandbox Escape e Exploração

A pesquisa identificou vulnerabilidades críticas que permitem o escape da sandbox do SELinux no Exynos 990, frequentemente encadeadas para alcançar a execução de código no kernel.

### 2.1. CVE-2021-25337: Arbitrary File Read/Write via Clipboard Provider

*   **Componente Afetado:** `com.android.server.semclipboard.SemClipboardProvider` (Custom Samsung Clipboard Provider).
*   **Tipo:** Improper Access Control.
*   **Impacto:** Arbitrary File Read/Write (LPE).
*   **Detalhes Técnicos:** O provedor de área de transferência personalizado da Samsung, executado no `system_server` (UID 1000, contexto `system_server`), não implementava verificações de permissão em seu método `insert()`. O banco de dados `ClipboardImageTable` possui uma coluna `_data` que pode ser usada com `openFileHelper` para abrir arquivos.
*   **Exploração:** Um aplicativo no domínio `untrusted_app` pode inserir um caminho de arquivo arbitrário (ex: `/data/system/users/0/newFile.bin`) na coluna `_data`. O `system_server` abre o arquivo (que possui o contexto `users_system_data_file`, inacessível diretamente pelo `untrusted_app`) e retorna um descritor de arquivo (FD) bruto para o aplicativo chamador. O aplicativo pode então ler e escrever no arquivo usando este FD, permitindo a gravação de um payload ELF de segundo estágio [2].
*   **Correção:** A Samsung adicionou uma verificação `if (Binder.getCallingUid() != 1000)` no método `insert()` [2].

### 2.2. CVE-2021-25369: Kernel Information Leak via sec_log

*   **Componente Afetado:** ARM Mali GPU Driver e Samsung `sec_log`.
*   **Tipo:** Logic/Design Flaw (Information Exposure).
*   **Impacto:** KASLR Bypass (Info Leak).
*   **Detalhes Técnicos:** A macro `WARN_ON` no kernel Linux imprime um backtrace completo, incluindo o conteúdo bruto da pilha, que contém ponteiros para `task_struct` e `sys_call_table`. O driver Mali GPU acionava um `WARN_ON` ao receber um comando `ioctl` inválido (`KBASE_HWCNT_READER`).
*   **Exploração:** A Samsung implementou um serviço de *bugreport* personalizado (`dumpstate.rc`) que copiava o conteúdo do `kmsg` para `/data/log/sec_log.log` (ou `/proc/sec_log`). Os controles de acesso para `sec_log` eram muito mais permissivos que `/dev/kmsg`, permitindo que aplicativos do sistema lessem o backtrace. O endereço de `sys_call_table` vaza, quebrando o KASLR, e o ponteiro `task_struct` é usado para localizar o ponteiro `addr_limit`, facilitando a leitura/escrita arbitrária no kernel [5].
*   **Comandos PoC:**
    ```c
    // Trigger WARN_ON
    hwcnt_fd = ioctl(dev_mali_fd, 0x40148008, &v4);
    ioctl(hwcnt_fd, 0x4004BEFE, 0);
    // Start bugreport
    system("setprop dumpstate.options bugreportfull; setprop ctl.start bugreport");
    ```

### 2.3. CVE-2022-22292: Arbitrary Activity Start in Telecom

*   **Componente Afetado:** Samsung Telecom App.
*   **Tipo:** Improper Handling of Insufficient Permissions (CWE-280).
*   **Impacto:** Command Injection / Arbitrary Activity Launch.
*   **Detalhes Técnicos:** Um *receiver* dinâmico desprotegido no aplicativo Telecom permitia que aplicativos não confiáveis iniciassem atividades arbitrárias com privilégios do sistema [6].

### 2.4. CVE-2021-25467: Kernel LPE in Vision DSP Driver

*   **Componente Afetado:** Vision DSP Kernel Driver (`/dev/dsp`).
*   **Tipo:** Integer Overflow resultando em Out-of-Bounds (OOB) Write.
*   **Impacto:** LPE / Kernel Memory Corruption.
*   **Detalhes Técnicos:** O ioctl `DSP_IOC_LOAD_GRAPH` permite o upload de modelos personalizados. Durante o processamento de arquivos ELF, as funções `dsp_elf32_get_text_size` e `dsp_elf32_get_mem_size` chamam `__dsp_elf32_get_section_list_size`, que contém um *integer overflow* ao somar os tamanhos das seções (`total += __dsp_elf32_align_4byte(size);`).
*   **Exploração:** O tamanho retornado para alocação de memória pode ser menor que a soma real das seções. Isso permite gravações OOB na região de memória IO mapeada virtualmente no kernel. A exploração requer contornar verificações adicionais introduzidas em patches posteriores, manipulando os deslocamentos (`offset`) e tamanhos das seções de dados (`DMb`, `TCMb`, etc.) para causar *underflows* e contornar os limites de alocação [7].

## 3. Técnicas de Bypass do SELinux no Kernel

Uma vez que a execução de código no kernel (arbitrary read/write) é alcançada, o SELinux deve ser desativado ou contornado para comprometer totalmente o dispositivo. No entanto, a Samsung implementa o Real-time Kernel Protection (RKP), executado no hipervisor (EL2), que protege estruturas críticas do kernel.

### 3.1. Sobrescrita da Flag `selinux_enforcing`

*   **Mecanismo:** O kernel mantém uma variável global `selinux_enforcing` (ou `state->enforcing` em kernels mais recentes). Escrever `0` nesta variável coloca o sistema em modo permissivo [4].
*   **Mitigação Samsung (RKP):** A Samsung marca `selinux_enforcing` e `ss_initialized` como somente leitura (`__kdp_ro`) a partir do EL1 após a inicialização. Tentar sobrescrever essas variáveis resulta em *kernel panic* [8]. *Nota: Uma falha de configuração inicial no S20 (SVE-2019-15998) deixou essas variáveis desprotegidas temporariamente* [8].

### 3.2. Manipulação do `permissive_map`

*   **Mecanismo:** O SELinux mantém um bitmap (`permissive_map`) no `policydb`. Se o bit correspondente ao ID do tipo de um domínio for definido como 1, esse domínio específico é executado em modo permissivo [4].
*   **Mitigação Samsung:** A Samsung define `AVD_FLAGS_PERMISSIVE` como `0` no kernel, tornando a flag permissiva inoperante. O kernel ignora o mapa durante as verificações de permissão [4].

### 3.3. Sobrescrita do Access Vector Cache (AVC)

*   **Mecanismo:** O AVC armazena em cache as decisões recentes de permissão. Cada entrada (`avc_node`) contém uma estrutura `av_decision` com um bitmask `allowed`. Sobrescrever este campo com `0xFFFFFFFF` concede todas as permissões para a combinação origem/destino/classe sem consultar a política [4].
*   **Exploração:** Como o RKP não protege o cache AVC diretamente, esta técnica é viável. Requer localizar o `avc_node` correto na memória. Técnicas avançadas como "Cross-Cache Attacks" exploram a relação entre os caches SLUB e o alocador de páginas para sobrepor objetos corrompidos com nós AVC [4].

### 3.4. Injeção de Política (sepolicy-inject)

*   **Mecanismo:** Ferramentas como `sepolicy-inject` (frequentemente usadas por soluções de root como Magisk) podem modificar a política SELinux em tempo de execução, injetando novas regras `allow` ou alterando transições de domínio.
*   **Implementação:** A política compilada é carregada via `/sys/fs/selinux/load`. Modificações ao vivo exigem privilégios elevados e a capacidade de interagir com o sistema de arquivos do SELinux [1].

## 4. Conclusão

A segurança do Samsung Exynos 990 depende fortemente da integridade do kernel e das proteções do hipervisor (RKP). Vulnerabilidades lógicas em serviços privilegiados (como o Clipboard Provider) e vazamentos de informações (sec_log) fornecem os blocos de construção iniciais para *exploit chains*. Embora o RKP mitigue técnicas triviais de bypass do SELinux (como sobrescrever `selinux_enforcing`), ataques direcionados ao Access Vector Cache (AVC) ou a exploração de drivers complexos (como o Vision DSP) continuam sendo vetores viáveis para comprometer o isolamento do sistema.

## Referências

[1] 8ksec. "Android SELinux Internals Part I". https://8ksec.io/android-selinux-internals-part-i-8ksec-blogs/
[2] Project Zero. "A Very Powerful Clipboard: Analysis of a Samsung in-the-wild exploit chain". https://projectzero.google/2022/11/a-very-powerful-clipboard-samsung-in-the-wild-exploit-chain.html
[3] Google Git. "te_macros - platform/external/sepolicy". https://android.googlesource.com/platform/external/sepolicy/+/refs/heads/brillo-m8-dev/te_macros
[4] Klecko. "SELinux bypasses". https://klecko.github.io/posts/selinux-bypasses/
[5] Project Zero. "CVE-2021-25369: Samsung kernel info leak in sec_log". https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2021/CVE-2021-25369.html
[6] Quokka. "Mobile App CVE Database: Critical Vulnerabilities & Exploits". https://www.quokka.io/critical-vulnerabilities-exploits-cve
[7] Taszk Labs. "CVE-2021-25467: Kernel LPE in the Vision DSP Kernel Driver". https://labs.taszk.io/blog/post/62_ss_dsp_oob_write/
[8] Duasynt. "SELinux RKP misconfiguration on Samsung S20 devices". https://duasynt.com/blog/samsung-s20-rkp-selinux-disable


## Exynos 990 Crypto Engine

# Pesquisa Técnica: Samsung Exynos 990 - Crypto Engine e Aceleração de Hardware

## 1. Arquitetura do Crypto Engine e Samsung Security Sub-system (SSS)
O Exynos 990 (SM-N986B, Galaxy Note20 Ultra 5G) integra o Samsung Security Sub-system (SSS), um coprocessador criptográfico dedicado que opera em conjunto com o ARM TrustZone. O SSS é responsável por descarregar operações criptográficas intensivas da CPU principal, garantindo isolamento físico e lógico.

### 1.1. Algoritmos Suportados em Hardware
O SSS fornece aceleração em hardware para uma ampla gama de algoritmos criptográficos:
- **Cifras de Bloco:** AES-128/192/256 (Modos: CBC, CTR, XTS, GCM), ARIA, SEED, SM4.
- **Funções de Hash:** SHA-1, SHA-224, SHA-256, SHA-384, SHA-512.
- **Criptografia Assimétrica:** RSA-2048, RSA-3072, RSA-4096.
- **Curvas Elípticas (ECC):** P-256, P-384.

### 1.2. Registros do Crypto Engine (Mapeamento de Memória)
O Crypto Engine é acessado através de registradores mapeados em memória (Memory-Mapped I/O - MMIO). Embora os endereços base exatos variem ligeiramente dependendo da revisão do silício e do layout do device tree, a estrutura típica inclui:
- **Base Address:** Tipicamente na região `0x10000000` a `0x1FFFFFFF` para periféricos de segurança.
- **Control Registers:** Configuram o modo de operação (ex: AES-XTS vs AES-CBC), direção (enc/dec) e interrupções.
- **Key Registers:** Registradores write-only onde as chaves são injetadas. Uma vez escritas, não podem ser lidas pelo software, apenas utilizadas pelo engine.
- **IV Registers:** Registradores para o Initialization Vector.
- **Data In/Out FIFOs:** Buffers FIFO para entrada de plaintext/ciphertext e saída do resultado processado.

### 1.3. Performance
A aceleração de hardware permite um throughput massivo, essencial para operações como File-Based Encryption (FBE).
- **AES-256-XTS:** O throughput atinge aproximadamente ~2GB/s, permitindo criptografia/descriptografia transparente do armazenamento sem gargalos perceptíveis na CPU.

## 2. True Random Number Generator (TRNG)
O Exynos 990 inclui um TRNG em hardware, vital para a geração de chaves criptográficas seguras e nonces.
- **Fontes de Entropia:** Utiliza ruído térmico (thermal noise) e jitter de osciladores em anel (ring oscillator jitter) como fontes primárias de entropia.
- **Testes de Saúde:** O TRNG implementa testes de saúde contínuos em conformidade com a norma NIST SP 800-90B para garantir que a entropia gerada não degrade ao longo do tempo ou sob condições anormais de temperatura/tensão.

## 3. Key Hierarchy e eFuses
A segurança do dispositivo é ancorada em chaves imutáveis gravadas durante a fabricação.
- **Hardware Unique Key (HUK):** Uma chave única de 256 bits gravada em eFuses (Secure OTP) durante a fabricação. A HUK nunca sai do hardware e não pode ser lida por software.
- **Key Encryption Key (KEK):** Derivada da HUK e de outros parâmetros de boot, usada para proteger chaves de nível superior.
- **File Encryption Keys (FEK):** Chaves geradas aleatoriamente para criptografar arquivos individuais (FBE), que são então envelopadas (wrapped) usando a KEK.

## 4. Inline Crypto Engine (ICE) para UFS
Para armazenamento de alto desempenho, o Exynos 990 utiliza um Inline Crypto Engine (ICE) acoplado ao controlador UFS (Universal Flash Storage).
- **Operação:** O ICE intercepta o tráfego de dados entre a memória RAM e o armazenamento UFS, realizando criptografia/descriptografia AES-256-XTS on-the-fly.
- **Overhead:** Zero overhead de CPU, pois a operação ocorre no caminho de dados (data path) do hardware de armazenamento.

## 5. Replay Protected Memory Block (RPMB)
O RPMB é uma partição especial no armazenamento eMMC/UFS usada para armazenar dados críticos que requerem proteção contra ataques de rollback.
- **Autenticação:** Todas as leituras e escritas no RPMB são autenticadas usando HMAC-SHA256. A chave HMAC é programada no RPMB durante o provisionamento na fábrica.
- **Write Counter:** Utiliza um contador monotônico. Cada operação de escrita incrementa o contador, e o hardware do armazenamento rejeita escritas com contadores antigos, prevenindo ataques de replay.
- **Uso:** Armazena anti-rollback counters (versões de firmware permitidas), dados do Samsung Knox, e estado de bloqueio do bootloader.

## 6. Ataques Criptográficos e Vulnerabilidades (CVEs)

### 6.1. Ataques Side-Channel e Fault Injection
Pesquisas acadêmicas e análises de segurança demonstraram a viabilidade teórica e prática de ataques físicos contra SoCs modernos como o Exynos 990:
- **Power Analysis (DPA/CPA):** Differential/Correlation Power Analysis pode ser usado para extrair chaves AES monitorando o consumo de energia do Crypto Engine durante a operação.
- **Timing Attacks:** Implementações de RSA que não utilizam algoritmos de tempo constante (constant-time) podem vazar informações sobre a chave privada.
- **Fault Injection (Voltage/Clock Glitching):** Ataques de injeção de falhas durante a verificação de assinaturas (ex: no BootROM ou TrustZone) podem forçar o processador a pular instruções de verificação, permitindo a execução de código não assinado.

### 6.2. Vulnerabilidades Conhecidas (CVEs)
- **CVE-2024-56426 (BootROM Exploit):** Uma vulnerabilidade crítica no BootROM do Exynos 990 (e Exynos 9830) que permite a execução de código arbitrário (LPE/RCE) antes do carregamento do bootloader. O exploit unificado (PoC disponível no GitHub) utiliza endereços de IRAM específicos (ex: `0x02022010` e `0x02022000`) para injetar payloads (`mem.bin`, `loader.bin`) e contornar a verificação de assinaturas, permitindo o carregamento de chaves customizadas.
- **CVE-2017-18311 / CVE-2017-18310 (TrustZone/Kinibi):** Embora mais antigas, vulnerabilidades no TEE (Trustonic Kinibi) demonstraram como falhas de validação de ponteiros (OOB/UAF) em Trusted Applications (TAs) podem levar ao comprometimento do Secure World. O projeto "ReZone" (USENIX Security '22) analisou como a falta de isolamento adequado entre TAs no Exynos 990 permite escalonamento de privilégios dentro do TrustZone.
- **Ataques ao Baseband (Project Zero):** Em 2023, o Google Project Zero revelou múltiplas vulnerabilidades de RCE (Remote Code Execution) no modem do Exynos 990 (ex: CVE-2023-26498), permitindo comprometimento total do baseband via rede celular sem interação do usuário.

## 7. Interfaces de Debug e Protocolos
- **Odin/Loke/PIT:** O protocolo de flashing proprietário da Samsung (Odin) comunica-se com o bootloader (Loke). O arquivo PIT (Partition Information Table) define o layout da memória flash. O Loke verifica as assinaturas das imagens (boot.img, recovery.img) usando o Crypto Engine antes de gravá-las nas partições.
- **EUB Mode (Exynos USB Booting):** Uma interface de recuperação de baixo nível do BootROM, ativada quando o bootloader primário está corrompido ou via test points de hardware. O EUB mode é o vetor de entrada para exploits de BootROM como o CVE-2024-56426.


## Exynos 990 IOMMU/SYSMMU

# Samsung Exynos 990 - IOMMU/SYSMMU e Isolamento de Periféricos

O Samsung Exynos 990 (SM-N986B) é um System-on-Chip fabricado utilizando o processo de 7nm EUV (7LPP). A arquitetura de isolamento de memória e proteção de DMA neste SoC é implementada através do System MMU (SYSMMU), a solução proprietária da Samsung para IOMMU. O SYSMMU é responsável por traduzir os I/O Virtual Addresses (IOVAs) utilizados pelos periféricos em endereços físicos (PA), garantindo que dispositivos com capacidade de Direct Memory Access (DMA) apenas acedam às regiões de memória explicitamente autorizadas pelo sistema operativo.

A implementação do SYSMMU no Exynos 990 suporta o formato de page table ARM Short-descriptor, sendo compatível com a extensão ARM Large Physical Address Extension (LPAE) nas instâncias mais recentes. A arquitetura utiliza um esquema de tradução de dois níveis (Level 1 e Level 2). A granularidade das páginas suportadas inclui páginas pequenas de 4KB (`SPAGE_SIZE`), páginas grandes de 64KB (`LPAGE_SIZE`) e seções contíguas de 1MB (`SECT_SIZE`). Com a introdução da versão 5 do SYSMMU, o suporte de endereçamento físico foi estendido para 36 bits. Esta extensão é alcançada através de um deslocamento lógico (`SYSMMU_V5_PG_ENT_SHIFT = 4`), onde os valores das entradas da page table são deslocados em 4 bits.

A arquitetura Exynos dedica uma instância de SYSMMU por master device, permitindo que a memória física dispersa seja mapeada como uma região contígua para cada periférico. As instâncias comuns presentes no Exynos 990 incluem o GPU SYSMMU para a GPU Mali-G77, o NPU SYSMMU para a Dual-core Neural Processing Unit, o DPU SYSMMU para a Display Processing Unit, o FIMC-IS SYSMMU para o Camera ISP, o MFC SYSMMU para o Multi-Format Codec e o Modem SYSMMU para o Exynos Modem 5123.

Cada controlador SYSMMU possui o seu próprio conjunto de registradores mapeados em memória para configuração e controlo. A tabela abaixo detalha os principais registradores e os seus respetivos offsets hexadecimais:

| Registrador | Offset | Descrição |
| :--- | :--- | :--- |
| `REG_MMU_CTRL` | `0x000` | Controlo principal do MMU (0x5 = Enable, 0x7 = Block, 0x0 = Disable). |
| `REG_MMU_CFG` | `0x004` | Configuração de parâmetros como QoS e cache de page table. |
| `REG_MMU_STATUS` | `0x008` | Estado atual do MMU, incluindo flags de interrupções e falhas. |
| `PT_BASE_PPN` | `0x00C` | Endereço base físico da page table de Nível 1 (específico para v5/v7). |
| `MMU_FLUSH_ALL` | `0x010` | Registo para acionar a invalidação completa do Translation Lookaside Buffer (TLB). |
| `MMU_FLUSH_ENTRY` | `0x014` | Registo para acionar a invalidação de uma entrada específica do TLB. |
| `FAULT_VA` | `0x070` | Registo que armazena o endereço virtual que causou uma falha de página (Page Fault). |
| `FAULT_INFO` | `0x078` | Informações detalhadas sobre a transação que falhou, indicando se foi leitura ou escrita. |

O isolamento de DMA é gerido atribuindo os periféricos a diferentes domínios IOMMU através da configuração de Stream IDs. As transações de DMA originadas por periféricos que não estejam anexados a um domínio IOMMU válido reportam um aborto de transação. Quando ocorre um acesso inválido, como um `PAGE FAULT`, `MULTI-HIT` ou violação de `ACCESS PROTECTION`, o SYSMMU gera uma interrupção de hardware. O kernel do Linux lida com esta falha através de rotinas de tratamento específicas, como a função `exynos_sysmmu_v5_get_fault_info`. Dependendo da configuração do sistema e do contexto da falha, o evento pode resultar num kernel panic imediato ou num "silent drop", onde o acesso à memória é negado silenciosamente, permitindo que o sistema continue a operar.

Apesar dos mecanismos de proteção, vulnerabilidades de design e implementação frequentemente comprometem o isolamento do IOMMU. Uma vulnerabilidade crítica neste domínio é o CVE-2021-28663, que afeta o driver de kernel da GPU Arm Mali (arquiteturas Bifrost, Valhall e Midgard). Esta falha é classificada como um Use-After-Free (UAF) e possui um CVSS Score de 8.8. A vulnerabilidade reside no manuseamento incorreto das operações de memória da GPU. A GPU Mali gere as suas próprias page tables, separadas do SYSMMU principal do sistema em algumas configurações, traduzindo Virtual Addresses (VA) para Intermediate Physical Addresses (IPA).

A técnica de exploração para o CVE-2021-28663, demonstrada em Proofs of Concept (PoC) públicos, envolve a manipulação do ciclo de vida da memória da GPU. O atacante cria um `GPU_VA` e utiliza a chamada de sistema `mmap` para obter o endereço virtual correspondente às páginas físicas. Em seguida, é criado um alias para as páginas físicas, mas sem invocar `mmap`, mantendo a contagem de referência `gpu_mapping` como 1. O atacante altera então as flags do `GPU_VA` para `BASE_MEM_DONT_NEED`, instruindo o driver Mali a marcar estas páginas como "evictable", permitindo que sejam libertadas. Como existe um registo para a página com alias, o atacante pode posteriormente fazer `mmap` para ela. Isto concede acesso de leitura a partir do CPU para memória que já foi libertada ou reatribuída a outros processos ou ao kernel.

Em muitos sistemas, o IOMMU não está estritamente ativado ou isolado para a GPU Mali por padrão, permitindo um IOMMU Bypass. Um atacante que comprometa o driver da GPU pode forçar a GPU a mapear e aceder a memória física arbitrária do sistema através de operações de DMA, ignorando as restrições de isolamento pretendidas pelo SYSMMU.

A exploração de vulnerabilidades como o CVE-2021-28663 na GPU Mali tem implicações severas para a criação de exploit chains, permitindo técnicas avançadas como a GPU-Assisted Kernel Exploitation. Utilizando a vulnerabilidade UAF, o atacante ganha a capacidade de ler e escrever na memória física do sistema através de comandos de DMA da GPU comprometida. Com este acesso arbitrário de leitura e escrita física, o atacante pode localizar as page tables do kernel na memória física, tipicamente referenciadas pela estrutura `swapper_pg_dir`. O atacante modifica então as entradas da page table do kernel (PTEs) para mapear memória controlada por si, contendo o payload do exploit, como executável no espaço de endereçamento do kernel. Este processo culmina na execução de código arbitrário com privilégios de kernel (EL1).

No Exynos 990, a Samsung implementou o Real-time Kernel Protection (RKP), um hypervisor que opera no nível de privilégio EL2, para mitigar estes ataques. O RKP utiliza a Stage 2 Translation da arquitetura ARM para impor restrições de memória adicionais. O hypervisor marca as seções `.text` e `.rodata` do kernel, bem como as page tables de Nível 1 e Nível 2, como read-only para o kernel em EL1. No entanto, o próprio RKP tem sido alvo de vulnerabilidades. A falha SVE-2021-20178 (CVE-2021-25415) revelou uma validação de endereços inadequada no RKP. Esta vulnerabilidade permitia que um kernel comprometido em EL1 solicitasse ao RKP a alteração das permissões de memória do próprio EL2 para read-write. A exploração bem-sucedida desta falha quebrava as garantias de segurança do hypervisor, permitindo a modificação das estruturas protegidas e a evasão completa dos mecanismos de defesa do sistema.


## Exynos 990 Exploit Chains

# Pesquisa Técnica: Exploit Chains do Samsung Exynos 990

## Introdução
Este documento detalha as exploit chains documentadas (in-the-wild e research) para o Samsung Galaxy Note20 Ultra 5G (SM-N986B, Exynos 990). O foco é exclusivamente técnico, abordando vulnerabilidades, componentes afetados, tipos de falhas, impactos e técnicas de exploração.

## Chain 1: Google TAG/Project Zero Mar 2021 (Watering Hole)
Esta chain foi descoberta pelo Google Threat Analysis Group (TAG) e Project Zero em dezembro de 2020 e corrigida pela Samsung em março de 2021. A chain é composta por três vulnerabilidades em componentes customizados da Samsung [1].

A primeira vulnerabilidade, **CVE-2021-25337**, afeta o componente `com.android.server.semclipboard.SemClipboardProvider`, que é um provedor de área de transferência customizado da Samsung. Trata-se de uma falha de falta de controle de acesso (Access Control Bypass) que permite a leitura e escrita arbitrária de arquivos. O provedor de área de transferência customizado da Samsung roda no `system_server` (UID 1000, contexto SELinux `system_server`). A tabela `ClipboardImageTable` possui as colunas `id` e `_data`. A coluna `_data` é usada com `openFileHelper` para abrir arquivos. O método `insert()` não possuía verificação de permissões, permitindo que qualquer aplicativo (mesmo no contexto `untrusted_app`) modificasse a coluna `_data` e abrisse arquivos com os privilégios do `system_server`. Na exploração, o exploit insere um caminho de arquivo controlado (ex: `/data/system/users/0/newFile.bin`) na coluna `_data` e obtém um descritor de arquivo (FD) bruto. O arquivo criado tem o contexto SELinux `users_system_data_file`. O exploit usa esse FD para escrever o próximo estágio (um binário ELF) no sistema de arquivos. A Samsung corrigiu isso adicionando uma verificação no método `insert()` para garantir que o PID do processo chamador seja UID 1000 (`Binder.getCallingUid() != 1000`) [1].

A segunda vulnerabilidade, **CVE-2021-25369**, afeta o componente `sec_log`, que é um logger de kernel customizado da Samsung. Trata-se de um Information Leak que permite o bypass do KASLR. O impacto é o vazamento de endereços do kernel. Esta vulnerabilidade é utilizada em conjunto com a CVE-2021-25337 para preparar o terreno para a exploração do kernel [1].

A terceira vulnerabilidade, **CVE-2021-25370**, afeta o driver Display Processing Unit (DPU). Trata-se de um Use-After-Free (UAF) que resulta em corrupção de memória, levando à execução de código no kernel (LPE) e sandbox escape para root. A vulnerabilidade reside na implementação incorreta do manuseio de descritores de arquivo no driver DPU, especificamente um UAF de uma estrutura de arquivo (`file struct`) no driver Display and Enhancement. O exploit utiliza o UAF para corromper a memória do kernel, escalar privilégios e escapar da sandbox, obtendo acesso root [1].

## Chain 2: Kirin/Exynos Baseband (Project Zero 2023)
Descoberta pelo Project Zero no final de 2022 e início de 2023, esta chain afeta modems Exynos e permite Remote Code Execution (RCE) sem interação do usuário (zero-click) [2].

A vulnerabilidade **CVE-2023-24033** afeta o Exynos Modem (Shannon baseband). Trata-se de um Remote Code Execution (RCE) que permite a execução de código no modem baseband sem interação do usuário (Internet-to-baseband). A vulnerabilidade ocorre no parsing de pacotes SIP/SDP (Session Initiation Protocol / Session Description Protocol). Isso permite que um atacante comprometa remotamente o telefone no nível do baseband, necessitando apenas conhecer o número de telefone da vítima. A mitigação recomendada é desativar Wi-Fi calling e Voice-over-LTE (VoLTE) nas configurações do dispositivo [2].

## Chain 3: Mali GPU in-the-wild (2022-2023)
Exploits in-the-wild visando a GPU Arm Mali, frequentemente usados em conjunto com outras vulnerabilidades para obter acesso root [3].

A vulnerabilidade **CVE-2022-38181** afeta o driver do kernel da GPU Arm Mali. Trata-se de um Use-After-Free (UAF) que permite leitura/escrita arbitrária de memória física, sobrescrita de credenciais do kernel e acesso root. O driver do kernel da GPU Arm Mali permite que usuários sem privilégios acessem memória liberada devido ao manuseio incorreto de operações de memória da GPU. O atacante utiliza o UAF para obter leitura e escrita arbitrária na memória física. Isso é usado para sobrescrever as credenciais do kernel (kernel credential overwrite), elevando os privilégios para root [3].

A vulnerabilidade **CVE-2023-4211** também afeta o driver do kernel da GPU Arm Mali. Trata-se de operações impróprias de processamento de memória da GPU que resultam em acesso a memória já liberada (UAF) e LPE. Um usuário local sem privilégios pode realizar operações impróprias de processamento de memória da GPU para obter acesso a memória já liberada [3].

## Chain 4: NPU Exploit (Project Zero 2022)
Descoberta pelo Project Zero, esta vulnerabilidade afeta o driver da Neural Processing Unit (NPU) da Samsung [4].

A vulnerabilidade **CVE-2022-22265** afeta o driver do dispositivo Samsung NPU (`/dev/vertex10`). Trata-se de um Double Free / Use-After-Free (UAF) que permite leitura/escrita arbitrária de memória e execução de código no kernel (LPE). A vulnerabilidade de double free ocorre nos formatos dentro da estrutura `vb_queue` (`q->format.formats`). O primeiro free é acionado chamando o ioctl `VS4L_VERTEXIOC_S_FORMAT` com um argumento `format_list` (`flist`) inválido. A função `__vb_find_format` falha, e `q->format.formats` é liberado. O segundo free é acionado chamando o ioctl `VS4L_VERTEXIOC_STREAM_OFF`. A função `vb_queue_stop` chama `kfree(q->format.formats)` no ponteiro já liberado [4].

Na exploração, o atacante aciona o primeiro free e usa a syscall `select` para ocupar o objeto do kernel liberado. Em seguida, o exploit aciona o segundo free e ocupa o objeto com estruturas `pipe_buffer` usando `fcntl(fd, F_SETPIPE_SZ, size)`. Ao acordar a thread do `select`, as bitmasks retornadas contêm um objeto `pipe_buffer` vazado. O exploit implementa um ataque Kernel Space Mirroring Attack (KSMA), fazendo spam de page tables para reutilizar a página do pipe apontada pelo `pipe_buffer` vazado, e então sobrescreve a page table escrevendo no pipe, obtendo leitura/escrita arbitrária [4].

## Técnicas Comuns e Post-Exploitation

| Técnica | Descrição |
| :--- | :--- |
| **Heap Feng Shui / Cross-Cache Attacks** | Técnicas usadas para manipular o layout do heap do kernel e explorar vulnerabilidades UAF/Double Free. |
| **pipe_buffer primitive** | Usada no exploit da NPU (CVE-2022-22265) para obter vazamento de informações e preparar o ataque KSMA. |
| **modprobe_path overwrite** | Técnica comum para obter execução de código como root sobrescrevendo o caminho do executável `modprobe` no kernel. |
| **SELinux disable via selinux_enforcing** | Desativar o SELinux sobrescrevendo a variável `selinux_enforcing` na memória do kernel. |
| **Post-exploitation** | Persistência via Magisk-like init overlay, implantes na partição vendor, e backdoors no firmware do modem. |

## Defesas e Mitigações (Samsung Knox)

| Defesa | Descrição |
| :--- | :--- |
| **RKP (Real-time Kernel Protection)** | Hypervisor da Samsung (parte do Knox) que protege estruturas de dados sensíveis do kernel (page tables, `struct cred`, `struct task_security_struct`, `struct vfsmount`, status do SELinux) tornando-as read-only (Kernel Data Protection - KDP) [5]. |
| **JOPP (Jump-Oriented Programming Prevention)** | Solução CFI (Control-Flow Integrity) proprietária da Samsung. Insere instruções NOP antes do início das funções e substitui branches indiretos por branches diretos para uma função helper (`jopp_springboard_blr_rX`) que verifica um valor mágico (`0xbe7bad`) [5]. |
| **ROPP (Return-Oriented Programming Prevention)** | Solução proprietária para prevenir ROP. Faz XOR do endereço de retorno com uma "thread key" (armazenada em `thread_info->rrk` e XORada com uma "master key" RRMK) antes de colocá-lo na stack [5]. |
| **KNOX Attestation** | Recurso projetado para detectar se um dispositivo ou suas chaves foram comprometidos. |
| **MTE (Memory Tagging Extension)** | Mitigação futura baseada em hardware da ARM para detectar corrupção de memória (UAF, OOB). |

## Referências

[1] [A Very Powerful Clipboard: Analysis of a Samsung in-the-wild exploit chain](https://projectzero.google/2022/11/a-very-powerful-clipboard-samsung-in-the-wild-exploit-chain.html)
[2] [Multiple Internet to Baseband Remote Code Execution Vulnerabilities in Exynos Modems](https://googleprojectzero.blogspot.com/2023/03/multiple-internet-to-baseband-remote-rce.html)
[3] [Analyzing a Modern In-the-wild Android Exploit](https://projectzero.google/2023/09/analyzing-modern-in-wild-android-exploit.html)
[4] [CVE-2022-22265: Samsung NPU device driver double free in Android](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2022/CVE-2022-22265.html)
[5] [A Samsung RKP Compendium](https://blog.impalabs.com/2101_samsung-rkp-compendium.html)


