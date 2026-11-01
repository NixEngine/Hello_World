RELATORIO TÉCNICO COMPLETO: ARQUITETURA ARM
Sumário Executivo
**Total de Algoritmos/Fórmulas/Estruturas Coletados:** 765

**Conceitos da Arquitetura ARM Pesquisados:** 28

**Pesquisadores Analisados:** 20
PARTÊ 1: CONCEITOS DA ARQUITETURA ARM - CON
TÉCNICO
# Conceito 1: ARMv8 A15A A64, A32, T32 Instruction Encoding

**Itens Técnicos Encontrados:** 15

**Conceitos-Chave:** A64 Instruction Format, A32 Instruction Format, T32 Instruction Format, Opcode Map, Memory Barrier Protocol, Conditional Select Formula, Shifted Register Formula
ARMv8-A ISA Technical Content: A64, A32, T32 Instruction Encoding and Opcode Maps
1. A64 Instruction Set Encoding (AArch64)
baseada nos bits no intervalo [31:24], que formam o campo principal do opcode.

**1.1. Estrutura da Tabela Principal de Codificação A64**

A decodificação de instrução de nível superior é determinada pelo campo op0 (bits [31:29]) e outros bits no intervalo [31:24]
<table>
<tr>
<th>Bits<br/>[31:29]</th>
<th>Bits<br/>[28:25]</th>
<th>Grupo</th>
<th>Descrição</th>
</tr>
<tr>
<td>000</td>
<td>0000</td>
<td>Reserved</td>
<td>UDF (Instrução Indefinida)</td>
</tr>
<tr>
<td>001</td>
<td>0010</td>
<td>SVE Instructions</td>
<td>Extensão de Vetor Escalável</td>
</tr>
<tr>
<td>100x</td>
<td>-</td>
<td>Data Processing – Immediate</td>
<td>Endereçamento relativo ao PC, Adição/subtração (imediato), Lógico (imediato), Movimentação ampla (imediato), Campo de bits, Extração</td>
</tr>
<tr>
<td>101x</td>
<td>-</td>
<td>Branches, Exception Generating and System instructions</td>
<td>Saltos Condicionais/Incondicionais, Instruções de Sistema (MSR, MRS, DMB, DSB, ISB)</td>
</tr>
<tr>
<td>x1x0</td>
<td>-</td>
<td>Loads and Stores</td>
<td>Carregar/Armazenar registro, Carregar/Armazenar par de registros,<br/>Carregar/Armazenar exclusivo</td>
</tr>
<tr>
<td>x101</td>
<td>-</td>
<td>Data Processing – Register</td>
<td>Lógico (registro deslocado), Adição/subtração (registro deslocado), Adição/subtração com carry, Rotação para a direita com extensão, Seleção condicional, Definição condicional</td>
</tr>
<tr>
<td>x111</td>
<td>-</td>
<td>Data Processing – Scalar Floating-Point and Advanced SIMD</td>
<td>Ponto Flutuante Escalar, SIMD Avançado (Vetor)</td>
</tr>
</table>
de Instrução A64 (Exemplo: Adição/Subtração Im)
| O formato de instrução Adição/subtração (imediato) é uma estrutura chave na ISA A64 |  |
|---|---|
<table>
<tr>
<td>Bits</td>
<td>31</td>
<td>30</td>
<td>29</td>
<td>28</td>
<td>27</td>
<td>26</td>
<td>25</td>
<td>24</td>
<td>23</td>
<td>22</td>
<td>21</td>
<td>20</td>
<td>19</td>
<td>18</td>
<td>17</td>
<td>16</td>
<td>15</td>
<td>14</td>
<td>13</td>
<td>12</td>
<td>11</td>
<td>10</td>
<td>9</td>
<td>8</td>
<td>7</td>
<td>6</td>
<td>5</td>
<td>4</td>
<td>3</td>
<td>2</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td>Campo</td>
<td><strong>sf</strong></td>
<td><strong>op</strong></td>
<td><strong>S</strong></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td><strong>sh</strong></td>
<td><strong>imm12</strong></td>
<td><strong>Rn</strong></td>
<td><strong>Rd</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

*   **sf (31):** Flag de tamanho. 0 para 32 bits (registradores W), 1 para 64 bits (registradores X).
*   **op (30):** Operação. 0 para ADD, 1 para SUB.
*   **S (29):** Definir flags. 0 para não definir, 1 para definir (ADDS, SUBS).
*   **sh (22):** Deslocamento. 0 para LSL #0, 1 para LSL #12.
*   **imm12 (21:10):** Valor imediato não assinado de 12 bits.
*   **Rn (9:5):** Registrador de origem (primeiro operando).
*   **Rd (4:0):** Registrador de destino.
1.3. Codificação de Instruções de Sistema A64 (Exemplo: DMB, DSB, ISB)
As instruções de sistema são decodificadas do grupo Branches, Exception Generating and System instruction
<table>
<tr>
<th>Bits</th>
<th>31</th>
<th>30</th>
<th>29</th>
<th>28</th>
<th>27</th>
<th>26</th>
<th>25</th>
<th>24</th>
<th>23</th>
<th>22</th>
<th>21</th>
<th>20</th>
<th>19</th>
<th>18</th>
<th>17</th>
<th>16</th>
<th>15</th>
<th>14</th>
<th>13</th>
<th>12</th>
<th>11</th>
<th>10</th>
<th>9</th>
<th>8</th>
<th>7</th>
<th>6</th>
<th>5</th>
<th>4</th>
<th>3</th>
<th>2</th>
<th>1</th>
<th>0</th>
</tr>
<tr>
<td>Campo</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td><strong>op1</strong></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td><strong>CRm</strong></td>
<td><strong>op2</strong></td>
<td><strong>Rt</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>
*   **op1 (19:17):** Sub-campo de opcode.
*   **CRm (11:8):** Campo de registro de controle (usado para opções DMB/DSB/ISB).
*   **op2 (7:5):** Sub-campo de opcode.
*   **Rt (4:0):** Registrador de destino (geralmente 11111 para instruções de sistema).
2.1. Formato de Instrução A32 (ARM 32-bit)
As instruções A32 têm **32 bits de comprimento fixo** e são caracterizadas por um campo de execução [31:28].
<table>
<tr>
<th>Bits</th>
<th>31</th>
<th>30</th>
<th>29</th>
<th>28</th>
<th>27</th>
<th>26</th>
<th>25</th>
<th>24</th>
<th>23</th>
<th>22</th>
<th>21</th>
<th>20</th>
<th>19</th>
<th>16</th>
<th>15</th>
<th>12</th>
<th>11</th>
<th>0</th>
</tr>
<tr>
<td>Campo</td>
<td><strong>Cond</strong></td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>I</td>
<td><strong>Opcode</strong></td>
<td><strong>S</strong></td>
<td><strong>Rn</strong></td>
<td><strong>Rd</strong></td>
<td><strong>Operand2</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

- **Cond (31:28):** Código de condição de 4 bits.
- **I (25):** Flag imediato.
- **Opcode (24:21):** Código de operação ALU de 4 bits.
- **S (20):** Definir flags.
- **Rn (19:16):** Registrador do primeiro operando.
- **Rd (15:12):** Registrador de destino.
- **Operand2 (11:0):** Segundo operando (registro ou valor imediato).
2.2. Formato de Instrução T32 (Thumb)
. Formato de Instrução T32
<table>
<tr>
<th><strong>Bits</strong></th>
<th><strong>15</strong></th>
<th><strong>14</strong></th>
<th><strong>13</strong></th>
<th><strong>12</strong></th>
<th><strong>11</strong></th>
<th><strong>10</strong></th>
<th><strong>9</strong></th>
<th><strong>8</strong></th>
<th><strong>7</strong></th>
<th><strong>6</strong></th>
<th><strong>5</strong></th>
<th><strong>4</strong></th>
<th><strong>3</strong></th>
<th><strong>2</strong></th>
<th><strong>1</strong></th>
<th><strong>0</strong></th>
</tr>
<tr>
<td>Campo</td>
<td><strong>Opcode</strong></td>
<td><strong>Rm</strong></td>
<td><strong>Rn</strong></td>
<td><strong>Rd</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>
<table>
<tr>
<td colspan="17">2.2.2. Formato de Instrução T32 de 32 bits (Thumb-2)</td>
</tr>
<tr>
<td>Bits</td>
<td>31</td>
<td>30</td>
<td>29</td>
<td>28</td>
<td>27</td>
<td>26</td>
<td>25</td>
<td>24</td>
<td>23</td>
<td>22</td>
<td>21</td>
<td>20</td>
<td>19</td>
<td>16</td>
<td>15</td>
<td>12</td>
<td>11</td>
<td>0</td>
</tr>
<tr>
<td>Campo</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td><strong>Op1</strong></td>
<td><strong>S</strong></td>
<td><strong>Op2</strong></td>
<td><strong>Rn</strong></td>
<td><strong>Rd</strong></td>
<td><strong>Imm12</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>
3. Estruturas de Hardware e Protocolos
3.1. Protocolos de Barreira de Memória (DMB, DSB, ISB)
*   **DMB (Data Memory Barrier):** Garante que todos os acessos à memória antes do DMB sejam observados antes de qualquer acesso à memória após o DMB.
*   **DSB (Data Synchronization Barrier):** Atua como um DMB e garante que todos os acessos explícitos à memória antes do DSB sejam concluídos antes que qualquer instrução após o DSB seja executada.
*   **ISB (Instruction Synchronization Barrier):** Limpa o pipeline, garantindo que todas as instruções após o ISB sejam buscadas após a conclusão do ISB.
3.2. Estruturas de Registradores (AArch64)
**Registradores de Propósito Geral (GPRs):** 31 registradores de 64 bits (x0 a x30), acessíveis como 32 bits (w0 a w30)

**Registrador Zero:** xZR (64 bits) ou wZR (32 bits), codificado como índice 31 (11111), sempre lê zero e descarta escrita.

**Stack Pointer (SP):** O registrador x31 é usado como SP.
**PSTATE): Coleção de registradores de sistema que contêm**
4. Algoritmos e Fórmulas
4.1. Fórmula de Operandos de Registrador Deslocado
A fórmula para o valor efetivo de um operando de registrador deslocado é:

$$\text{EffectiveValue} = \text{ShiftOperation(RegisterValue, ShiftAmount)}$$
Onde **ShiftOperation** pode ser
*   **LSL** (Logical Shift Left): Value × 2<sup>ShiftAmount</sup>
*   **LSR** (Logical Shift Right): ⌊Value/2<sup>ShiftAmount</sup>⌋ (não assinado)
*   **ASR** (Arithmetic Shift Right): ⌊Value/2<sup>ShiftAmount</sup>⌋ (assinado, preservando o bit de sinal)
*   **ROR** (Rotate Right): Value rotated right by ShiftAmount
4.2. Fórmulas de Seleção Condicional A64
As instruções de Seleção Condicional ( CSEL , CSINC , CSINV , CSNEG ) utilizam a seguinte lógica:

| Instruction | Description |
|---|---|
| **CSEL (Conditional Select):** $Rd = \begin{cases} Rn & \text{if Condition(PSTATE) is true} \\ Rm & \text{if Condition(PSTATE) is false} \end{cases}$ |  |
| **CSINC (Conditional Select Increment):** $Rd = \begin{cases} Rn & \text{if Condition(PSTATE) is true} \\ Rm + 1 & \text{if Condition(PSTATE) is false} \end{cases}$ |  |
| **CSINV (Conditional Select Invert):** $Rd = \begin{cases} Rn & \text{if Condition(PSTATE) is true} \\ -Rm & \text{if Condition(PSTATE) is false} \end{cases}$ |  |
| **CSNEG (Conditional Select Negate):** $Rd = \begin{cases} Rn & \text{if Condition(PSTATE) is true} \\ -Rm & \text{if Condition(PSTATE) is false} \end{cases}$ |  |
Conceito 2: ARMv9-A - SME, SVE2, RME e CCA
ns Técnicos Encontrados: 33
**Conceitos-Chave:** Scalable Matrix Extension (SME), Produto Externo e Acumulação, ZA Matrix Accumulator, Scalable Vector Extension 2 (SVE2), BEXT, BDEP, Gather/Scatter, Realm Management Extension (RME), Granule Protection Table (GPT), Confidential Compute Architecture (CCA), Realm Management Monitor (RMM), Realm Attestation Key (RAK), Entity Attestation Token (EAT), Criptografia de Memória
# Conteúdo Técnico da Arquitetura ARMv9-A: SME, SVE2, RME e CCA
Este documento apresenta o conteúdo técnico essencial, incluindo estruturas de hardware, algoritmos, formatos de instrução e protocolos, das extensões Scalable Matrix Extension (SME), Scalable Vector Extension 2 (SVE2), Realm Management Extension (RME) e Confidential Compute Architecture (CCA) da arquitetura ARMv9-A.
scalable Matrix Extension
O SME é uma extensão arquitetural projetada para acelerar operações de matriz, sendo fundamental para cargas de trabalho de Inteligência Artificial e Machine Learning. Ele introduz um novo arquivo de registradores e um algoritmo central para multiplicação de matrizes.
Estruturas de Hardware e Registradores
A principal estrutura de hardware introduzida é o ZA (Matrix Accumulator), um novo arquivo de registradores de matriz escalável que atua como um acumulador. O tamanho do ZA é escalável e depende da implementação, sendo organizado em “tiles” (ladrilhos). O estado do processador PSTATE.ZA deve ser habilitado para permitir o uso do armazenamento ZA. O SME também define o Streaming SVE Mode, um modo de operação que implementa um subconjunto do conjunto de instruções SVE2 e adiciona instruções específicas para matrizes.
Algoritmos e Formatos de Instrução
oritmo central do SME é o **Produto Externo e Acumulação** (Outer Product and Accumulate), que é a base p
uplicação de matrizes (GEMM - General Matrix Multiply). A multiplicação de matrizes $C = A \times B$ é decomposta em uma
dutos externos de vetores, conforme a fórmula:
$C=\sum_{k}(\textrm{coluna}_{k}\,\textrm{de}\,A)\times(\textrm{linha}_{k}\,\textrm{de}\,B)$
As instruções do SME realizam a operação de acumulação no registrador ZA:

ZAda = ZAda + (Zn ⊗ Zm)
Onde $\otimes$ representa o produto externo dos vetores de entrada $Zn$ e $Zm$.
truções de matriz são predicadas por registradores de predicado ( Pn/M , Pm/M ), onde elementos inativos são tratados facilitando o manuseio de matrizes cujas dimensões não são múltiplos exatos do Comprimento de Vetor Escalável (SVL)
<table>
<tr>
<th>Instrução</th>
<th>Tipos de Dados de Entrada</th>
<th>Tipo de Dado de Acumulação</th>
<th>Descrição</th>
<th>Exemplo de Formato</th>
</tr>
<tr>
<td><strong>UMOPA/UMOPS</strong></td>
<td>INT8, INT16</td>
<td>INT32, INT64</td>
<td>Produto externo de inteiros (Signed/Unsigned) e acumulação/subtração. Realiza <em>widening</em> (alargamento) do tipo de dado.</td>
<td>UMOPS &lt;ZAda&gt;.S,<br/>&lt;Pn&gt;/M, &lt;Pm&gt;/M,<br/>&lt;Zn&gt;.B, &lt;Zm&gt;.B</td>
</tr>
<tr>
<td><strong>BFMOPA/BFMOPS</strong></td>
<td>BF16</td>
<td>FP32</td>
<td>Produto externo de BFloat16 e acumulação/subtração. Realiza <em>widening</em> para FP32.</td>
<td>BFMOPS &lt;ZAda&gt;.S,<br/>&lt;Pn&gt;/M, &lt;Pm&gt;/M,<br/>&lt;Zn&gt;.H, &lt;Zm&gt;.H</td>
</tr>
<tr>
<td><strong>FMOPA/FMOPS</strong></td>
<td>FP16, FP32, FP64</td>
<td>FP32, FP64</td>
<td>Produto externo de ponto flutuante e acumulação/subtração.</td>
<td>FMOPA &lt;ZAda&gt;.S,<br/>&lt;Pn&gt;/M, &lt;Pm&gt;/M,<br/>&lt;Zn&gt;.S, &lt;Zm&gt;.S</td>
</tr>
</table>
O SME também inclui instruções para manipulação de tiles, como **ADDHA** (Adiciona vetor a *slices* horizontais do ZA) e **ADDVA** (Adiciona vetor a *slices* verticais do ZA), além de instruções de Load/Store/Move de tiles (**LD1x**, **ST1x**, **MOV/MOVA**, **LDR ZA/STR ZA**).
2. SVE2 (Scalable Vector Extension 2)
2 é uma extensão do SVE que adiciona um conjunto de instruções para acelerar algoritmos em processamento de sinais (DSP), multimídia e criptografia, mantendo a característica de **comprimento de vetor escalável** (VL).
e Manipulação de Bits e
O SVE2 introduz instruções de manipulação de bits que são cruciais para criptografia e compressão
<table>
<tr>
<th>Instrução</th>
<th>Descrição</th>
<th>Algoritmo/Operação</th>
<th>Formato (Exemplo)</th>
</tr>
<tr>
<td><strong>BEXT</strong></td>
<td><strong>Bit Extract (Gather):</strong> Coleta bits de um vetor de origem nas posições indicadas por uma máscara e os compacta no vetor de destino.</td>
<td>Elem[result, e, esize] = BitExtract(Elem[data, e, esize], Elem[mask, e, esize])</td>
<td>BEXT &lt;Zd&gt;.&lt;T&gt;, &lt;Zn&gt;.&lt;T&gt;, &lt;Zm&gt;.&lt;T&gt;</td>
</tr>
<tr>
<td><strong>BDEP</strong></td>
<td><strong>Bit Deposit (Scatter):</strong> Espalha os bits de ordem mais baixa de um vetor de origem para as posições indicadas por uma máscara no vetor de destino.</td>
<td>Operação inversa do BEXT.</td>
<td>BDEP &lt;Zd&gt;.&lt;T&gt;, &lt;Zn&gt;.&lt;T&gt;, &lt;Zm&gt;.&lt;T&gt;</td>
</tr>
<tr>
<td><strong>BGRP</strong></td>
<td><strong>Bit Group:</strong> Agrupa bits para a direita ou esquerda conforme selecionado por uma máscara.</td>
<td>Permutação de bits.</td>
<td>BGRP &lt;Zd&gt;.&lt;T&gt;, &lt;Zn&gt;.&lt;T&gt;, &lt;Zm&gt;.&lt;T&gt;</td>
</tr>
<tr>
<td><strong>BCAX</strong></td>
<td><strong>Bitwise Clear and Exclusive OR:</strong> Operação de bitwise XOR com clear.</td>
<td>Zd = (Zn &amp; ~Zm) ^ Za</td>
<td>BCAX &lt;Zd&gt;.&lt;T&gt;, &lt;Zn&gt;.&lt;T&gt;, &lt;Zm&gt;.&lt;T&gt;, &lt;Za&gt;.&lt;T&gt;</td>
</tr>
</table>
Instruções de Acesso a Dados e DSP
O SVE2 aprimora as operações de acesso a dados não contíguos com novos modos de endereçamento **Gather-Load** e **Store**, como o modo **Vector Base, Scalar Offset**. Além disso, inclui instruções escaláveis de **Widening/Narrowing** (ADDHNB) e versões escaláveis de instruções de DSP e criptografia (AES, SHA).
Management Extension) e CCA (Confid
garantindo isolamento de código e dados.

## Estruturas de Segurança e Gerenciamento de Memória

O RME expande o modelo de segurança tradicional (Secure/Non-secure) para quatro Estados de Endereçamento Físico (PAS) distintos: **Non-secure (NS)**, **Secure (S)**, **Realm ®** e **Root (RT)**.

A principal estrutura de hardware para gerenciar esses estados é a **Granule Protection Table (GPT)**.

*   **GPT:** Uma tabela de tradução (tipicamente de dois níveis) que rastreia o estado de segurança e a propriedade de cada Granule (unidade de memória, 4KB ou 64KB) na memória física. O endereço base da GPT é armazenado no registro **GPTBR_EL3**.
*   **Protocolo de Transição de Estado de Memória:** O RME define um protocolo onde a transição de um Granule entre os estados (ex: NS para R) é gerenciada por firmware de alto privilégio (Root World, em EL3).
*   **Criptografia de Memória:** O RME utiliza **Memory Encryption Contexts (MECs)** para gerenciar a criptografia de memória associada aos Realms, protegendo os dados em repouso na DRAM.
Componentes de Software e Protocolos
A CCA é implementada por dois componentes de software principais:

*   **Realm Management Monitor (RMM):** Software de alto privilégio que roda em **Realm EL2** e gerencia o ciclo de vida e os serviços de tempo de execução do Realm.
*   **EL3 Monitor (EL3M):** Firmware que gerencia o RMM e o RME.

A comunicação entre o Host (Hypervisor/OS) e o RMM é feita através da **Realm Management Interface (RMI)**, enquanto o código dentro do Realm usa a **Realm Services Interface (RSI)** para solicitar serviços ao RMM.
Atestado e Fórmulas Criptográficas
O CCA inclui um protocolo de atestado para verificar a integridade do Realm.

*   **CCA Attestation Token:** Um token de atestado, que é um perfil do **Entity Attestation Token (EAT)**, contendo evidências sobre o estado de boot do Realm.
*   **Assinatura:** O token é assinado usando a **Realm Attestation Key (RAK)**.
*   **Medições:** O processo de atestado envolve medições criptográficas:
    *   **RIM (Realm Initial Measurement):** Medição inicial do código do Realm (usando funções de Hash Criptográfico).
    *   **RTM (Realm Runtime Measurement):** Medições de tempo de execução.

O conceito de criptografia de memória, gerenciado pelos MECs, pode ser representado pela fórmula de transformação de dados:

Memória Criptografada = Cripto(Memória Original, Chave, Contexto)

Memória Original = Decripto(Memória Criptografada, Chave, Contexto)

onde Cripto e Decripto são as funções de criptografia e descritografia implementadas em hardware, e Chave e Contexto são os parâmetros usados nessas funções.
Conceito 3: NEON Advanced SIMD
**Itens Técnicos Encontrados:** 15
**Conceitos-Chave:** Registradores Q/D/S, Aritmética de Saturação, Operações de Ponto Flutuante Flush-to-Zero, Polinômios P8/P16, Formato de Instrução V{mod}op{shape}{cond}.{dt}
# EON Advanced SIMD - Conteúdo Técnico
O NEON Advanced SIMD (Single Instruction Multiple Data) é uma extensão de arquitetura para processadores ARM (perfil A e R) que acelera o processamento de mídia e sinais através de operações vetoriais paralelas. O foco desta seção é o conteúdo técnico puro, incluindo estruturas de hardware, formatos de instrução e algoritmos de operações.
Estrutura de Hardware: Arquivo de Registradores
ON e o VFP (Vector Floating Point) compartilham um arquivo de registradores distinto do arquivo de registradores do riscv. Este arquivo pode ser acessado como registradores de 32 bits (S), 64 bits (D) ou 128 bits (Q).
<table>
<tr>
<th>Registrador</th>
<th>Tamanho (bits)</th>
<th>Quantidade (típica)</th>
<th>Uso Principal</th>
<th>Mapeamento</th>
</tr>
<tr>
<td><strong>S</strong></td>
<td>32</td>
<td>32 (S0-S31)</td>
<td>VFP (ponto flutuante de precisão simples)</td>
<td>S&lt;2n&gt; e S&lt;2n+1&gt; formam D</td>
</tr>
<tr>
<td><strong>D</strong></td>
<td>64</td>
<td>32 (D0-D31)</td>
<td>NEON (vetores de 64 bits)</td>
<td>D&lt;2n&gt; e D&lt;2n+1&gt; formam Q</td>
</tr>
<tr>
<td><strong>Q</strong></td>
<td>128</td>
<td>16 (Q0-Q15)</td>
<td>NEON (vetores de 128 bits)</td>
<td>Q é formado por D&lt;2n&gt; e D&lt;2n+1&gt;</td>
</tr>
</table>
Mapeamento de Registrador
* Um registrador **Q** (128 bits) é composto por dois registradores **D** (64 bits): $Q_n = \{D_{2n+1}, D_{2n}\}$.
* Um registrador **D** (64 bits) é composto por dois registradores **S** (32 bits): $D_n = \{S_{2n+1}, S_{2n}\}$.
* O elemento 0 (menos significativo) de um vetor está nos bits de ordem mais baixa do registrado
Tipos de Dados em Vetores (Exemplos):
mato de Instrução NEON
A sintaxe geral das instruções NEON (Assembly) segue o formato:
V{<mod><op><shape><dest>{,<src1>{,<src2>}
| Componente | Descrição | Exemplos |
|---|---|---|
| V | Prefixo obrigatório para instruções NEON/VFP. | VADD, VMUL |
|  | Modificador de operação. | Q (Saturação), H (Halving), D (Doubling), R (Arredondamento) |
|  | Operação (e.g., ADD, SUB, MUL). | ADD, SUB, MUL |
|  | Define a relação de largura entre operandos e resultado. | L (Long - alarga), W (Wide - alarga um operando), N (Narrow - estreita) |
| . | Tipo de dado (Data Type). | .I8 (Inteiro 8-bit), .S16 (Inteiro Assinado 16-bit), .U32 (Inteiro Não-Assinado 32-bit), .F32 (Ponto Flutuante 32-bit), .P8 (Polinomial 8-bit) |
|  | Registrador de destino. | Q0, D1 |
|  | Registradores de origem. | Q1, D2 |
*   **VADD:** Operação de adição NEON.
*   **.I8:** Operação em inteiros de 8 bits.
*   **D0, D1, D2:** Registradores de 64 bits.
*   **Resultado:** Realiza oito adições paralelas de 8 bits (8 lanes) nos registradores D1 e D2, armazenando o resultado em D0.
3. Algoritmos e Operações Técnicas
3.1. Aritmética de Saturação (Modificador Q)
A aritmética de saturação limita o resultado de uma operação a um valor máximo e mínimo predefinido para o tipo de dado. Se o resultado exceder o limite, ele é fixado no valor máximo ou mínimo.

**Algoritmo de Saturação (para um elemento E com limite Max e Min):** $E_{result} = \begin{cases}
Max & \text{se } E > Max \\
Min & \text{se } E < Min \\
E & \text{caso contrário}
\end{cases}$

*   **Exemplo:** VQADD.S16 D0, D2, D3 (Adição Saturada em Inteiros Assinados de 16 bits).

## 3.2. Operações de Ponto Flutuante (Flush-to-Zero)

O NEON suporta apenas ponto flutuante de precisão simples (.F32) e não é totalmente compatível com IEEE-754.

*   **Modo Flush-to-Zero (FTZ):** O NEON opera sempre neste modo. Números desnormalizados (denormals) são tratados como zero na entrada de uma operação. Se o resultado de uma operação for um número desnormalizado, ele é substituído por zero.
*   **Faixa de Flush (Precisão Simples):** Se o resultado de uma operação for no intervalo ($-2^{-126}, +2^{-126}$), ele é substituído por 0.
*   **Arredondamento:** Fixo para round-to-nearest (arredondamento para o mais próximo), exceto para operações de conversão.

## 3.3. Aritmética Polinomial (Tipos P8 e P16)

O NEON suporta aritmética polinomial sobre o campo finito $\mathbb{F}_2$ (coeficientes 0 ou 1), útil para criptografia e verificação de redundância cíclica (CRC).

*   **Tipos de Dados:** P8 (Polinômio de 8 bits) e P16 (Polinômio de 16 bits).
* **Adição Polinomial:** É equivalente a uma operação **Exclusive OR (EOR)** bit a bit. $P_1(x) + P_2(x) \equiv P_1(x) \oplus P_2(x)$
* **Multiplicação Polinomial:** Envolve a multiplicação convencional dos coeficientes, mas os produtos parciais são combinados usando **EOR** (adição sem carry) em vez de adição convencional.
    * Instruções: VMUL e VMULL com o tipo de dado P8 ou P16.
1. Operações de Shift (Deslocamento)
O NEON oferece uma ampla gama de instruções de deslocamento, incluindo deslocamento com inserção e deslocamento com acumulação.
*   **Deslocamento Aritmético (Signed):** Preserva o bit de sinal.
*   **Deslocamento Lógico (Unsigned):** Não preserva o bit de sinal.
*   **Deslocamento com Inserção (VSLI/VSRI):** Combina bits de dois vetores. Por exemplo, VSLI (Shift Left and Insert) desloca o vetor de origem para a esquerda e insere os bits do vetor de destino nos bits de ordem mais baixa.
*   **Deslocamento com Acumulação (VSRA/VRSRA):** Desloca o vetor e acumula o resultado em outro vetor, útil para cálculos de alta precisão intermediária.
ritmos de Operações Complexas (Inversão e Rai
O NEON não possui instruções diretas para divisão ou raiz quadrada, mas fornece instruções de estimativa para permitir a implementação via iteração de Newton-Raphson.

*   **Divisão (Inversão):** Utiliza a estimativa de recíproco (VRECPE) e a etapa de refinamento de recíproco (VRECPS).
    Para calcular $\frac{1}{A}$:
    $$
    X_0 = \text{VRECPE}(A) \quad \text{(Estimativa inicial)}
    $$
    $$
    X_1 = X_0 \times \text{VRECPS}(A, X_0) \quad \text{(Refinamento)}
    $$
    ...

*   **Raiz Quadrada Inversa:** Utiliza a estimativa de raiz quadrada inversa (VRSQRTE) e a etapa de refinamento de raiz quadrada inversa (VRSQRTS).
    Para calcular $\frac{1}{\sqrt{A}}$:
    $$
    X_0 = \text{VRSQRTE}(A) \quad \text{(Estimativa inicial)}
    $$
    $$
    X_1 = X_0 \times \text{VRSQRTS}(A, X_0) \quad \text{(Refinamento)}
    $$
    Para calcular $\sqrt{A}$:
    $$
    \sqrt{A} = A \times \frac{1}{\sqrt{A}}
    $$
eito 4: SVE Scalable Vector Extension
**Conceitos-Chave:** Vector-Length Agnostic (VLA), Registradores de Predicado (P0-P15), First-Fault Register (FFR), Gather-Load, Scatter-Store, Formato de Instrução SVE
O SVE (Scalable Vector Extension) é uma extensão da arquitetura ARM AArch64 projetada para computação de alto desempenho (HPC), caracterizada por seu design **Vector-Length Agnostic (VLA)**, um conjunto de **Registradores de Predicado** e suporte a operações de memória **Gather/Scatter**.
1. Vector-Length Agnostic (VLA)
O SVE permite que o código de vetor seja escrito de forma agnóstica ao comprimento do vetor, o que significa que o mesmo binário pode ser executado em implementações de hardware com diferentes comprimentos de vetor (VL), variando de 128 a 2048 bits, em múltiplos de 128 bits.
Estrutura de Hardware
*   **Registradores de Vetor (Z0-Z31):** 32 registradores de vetor escaláveis. O comprimento real (VL) é determinado pela implementação de hardware e configurável via software (registrador ZCR_ELx.LEN).
*   **Comprimento do Vetor (VL):** O comprimento do vetor é um múltiplo de 128 bits. $VL = N \times 128$ bits, onde $N \in \{1, 2, \ldots, 16\}$
*   **Número de Elementos (N):** O número de elementos em um vetor depende do tamanho do elemento (esize) e do VL. $N_{elementos} = \frac{VL}{esize}$
*   **Instrução RDVL (Read Vector Length):** Uma instrução que permite ao software determinar o comprimento do vetor em tempo de execução, em unidades de bytes ou bits.
*   **Instrução WHILE:** O SVE utiliza instruções de predicado como WHILELT (While Less Than) para gerar predicados de loop que se adaptam automaticamente ao VL, permitindo a programação VLA.
stradores de Predicado e First-Fault Register (FFR)
O SVE utiliza registradores de predicado para controle de elementos (element-wise control) em operações ve-
essenciais para a programação VLA e para a implementação eficiente de loops com desvio e operações de memória.
Estrutura de Hardware
*   **Registradores de Predicado (P0-P15):** 16 registradores de predicado escaláveis.
*   **Comprimento do Predicado (PL):** O comprimento de um registrador de predicado é de $\frac{VL}{8}$ bytes (ou $\frac{VL}{8} \times 8 = VL$ bits, onde cada bit representa um elemento de 8 bits). $PL = \frac{VL}{8}$ bytes$
*   **First-Fault Register (FFR):** Um registrador especial que armazena o estado de falha de memória para instruções de carga vetorial com a opção *First-Fault*.
    *   O FFR é um registrador de predicado de 1 bit por elemento.
    *   **Protocolo de Falha (First-Fault):** Para instruções de carga vetorial com a opção *First-Fault*, se ocorrer uma falha de memória, a falha é suprimida, e o FFR é atualizado para indicar quais elementos ativos não foram carregados com sucesso. O processamento para no primeiro elemento que falha, e o FFR é usado para continuar a operação após o tratamento da exceção.
Instruções de Predicado (Exemplos):
*   PTRUE : Gera um predicado com todos os elementos definidos como TRUE.
*   WHILELT : Gera um predicado baseado em uma condição de loop.
*   RDFFR : Lê o conteúdo do FFR para um registrador de predicado.
*   WRFFR : Escreve um valor no FFR.
3. Operações Gather-Load e Scatter-Store
As operações Gather e Scatter permitem o acesso a dados não contíguos na memória, um recurso crucial para a vetorização de estruturas de dados complexas e esparsas.
utura de Instrução (Formato
*   **Gather-Load (Exemplo: LD1GW):** Carrega um vetor de elementos de memória usando um vetor de endereços base (implícito ou explícito) e um vetor de deslocamentos (offsets) ou índices.
    *   Sintaxe: LD1GW {<Zt>.D}, <Pg>/Z, [<Zn>.D, <Zm>.D, LSL #3]
        *   `<Zt>` : Registrador de vetor de destino.
        *   `<Pg>` : Registrador de predicado (Governing Predicate).
        *   `<Zn>` : Registrador de vetor base (opcional).
        *   `<Zm>` : Registrador de vetor de deslocamentos (offsets/índices).
        *   `LSL #3`: Fator de escala para o deslocamento (ex: para elementos de 64 bits, o deslocamento é multiplicado por 8, ou $2^3$).
*   **Scatter-Store (Exemplo: ST1SW):** Armazena um vetor de elementos em locais de memória não contíguos.
| Syntaxe: ST1SW {<Zt>.S}, <Pg>, [<Zn>.D, <Zm>.D, LSL #2] |
| :------------------------------------------------------ |
| <Zt>: Registrador de vetor de origem.                   |
| <Pg>: Registrador de predicado.                         |
| <Zn>: Registrador de vetor base.                        |
| <Zm>: Registrador de vetor de deslocamentos.            |
| LSL #2 : Fator de escala (ex: para elementos de 32 bits, o deslocamento é multiplicado por 4, ou 2²). |

**mo (Conceitual) de Gather-Load:** Para cada elemento ativo *i* (onde o bit *i* do registrador de predicado *Pg* é 1): $Memoria_Address_i = Base_Address + Offset_i \times ScaleZ_t[i] = Memoria[Memoria_Address_i]$ Onde:

*   *Base_Address* é o endereço base (escalar ou vetorial).
*   *Offset_i* é o deslocamento do elemento *i* (do registrador de vetor de deslocamentos).
*   *Scale* é o fator de escala (ex: 1, 2, 4, 8).

Operações Gather/Scatter podem ser **Non-temporal** (SVE2), fornecendo uma dica ao sistema de memória de que os dados dos títulos têm baixa frequência de reutilização, o que pode evitar a retenção de dados ou a remoção de dados mais recentemente usados dos caches.
4. Estruturas de Hardware
<table>
<tr>
<th>Estrutura</th>
<th>Descrição</th>
<th>Tamanho</th>
<th>Função Principal</th>
</tr>
<tr>
<td><strong>Registradores Z (Z0-Z31)</strong></td>
<td>Registradores de dados vetoriais escaláveis</td>
<td>$VL$ bits (128 a 2048)</td>
<td>Armazenamento de dados vetoriais</td>
</tr>
<tr>
<td><strong>Registradores P (P0-P15)</strong></td>
<td>Registradores de predicado escaláveis</td>
<td>$PL$ bits ($VL$/8 bytes)</td>
<td>Controle de elementos (predicação)</td>
</tr>
<tr>
<td><strong>FFR</strong></td>
<td>First-Fault Register</td>
<td>$PL$ bits</td>
<td>Gerenciamento de falhas de memória em cargas vetoriais</td>
</tr>
<tr>
<td><strong>ZCR_ELx</strong></td>
<td>System Register</td>
<td>Variável</td>
<td>Configuração do comprimento do vetor (VL)</td>
</tr>
<tr>
<td><strong>VL</strong></td>
<td>Vector Length</td>
<td>Múltiplo de 128 bits</td>
<td>Comprimento físico do vetor</td>
</tr>
<tr>
<td><strong>PL</strong></td>
<td>Predicate Length</td>
<td>$VL$/8 bytes</td>
<td>Comprimento do registrador de predicado</td>
</tr>
</table>
5. Fórmulas e Protocolos
| Protocolo de Falha de Carga (First-Fault): | O FFR é atualizado para indicar quais elementos ativos não foram carregados com sucesso. O processamento para no primeiro elemento que falha, permitindo a continuação após o tratamento da exceção. |
|---|---|
| Protocolo VLA: | O código é escrito para ser independente do VL real, usando instruções como WHILELT e RDVL para adaptar-se dinamicamente ao hardware. |
| Protocolo Non-temporal (SVE2): | As instruções de Gather/Scatter Non-temporal fornecem um hint ao sistema de memória para evitar o cache dos dados, otimizando o uso do cache para dados com baixa reutilização. |
| Formato de Instrução (Conceitual): | As instruções SVE geralmente incluem um campo para o registrador de predicado ( Pg e um campo para o modificador de predicação (/z para zeroing, implícito para merging). |
Nota: O número de algoritmos/fórmulas/estruturas é uma estimativa baseada nos conceitos técnicos estritos extraídos.
**Conceito 5: Thumb Thumb-2 - 16-bit instructions, 32-bit extensions, IT blocks**
**Itens Técnicos Encontrados:** 8

**Conceitos-Chave:** Instruções de 16-bit, Extensões de 32-bit, Densidade de Código, Instrução IT, Bloco IT, Variável, Condicionalidade de Instrução, ITState
Conteúdo Técnico: Thumb e Thumb-2
O Thumb-2 é uma arquitetura de conjunto de instruções de comprimento variável que combina instruções de 16 bits (do Thumb original) com extensões de 32 bits, visando alta densidade de código e desempenho comparável ao conjunto de instruções ARM de 32 bits [1].
Formato de Instrução Variável (16-bit e 32-bit)
A principal estrutura técnica do Thumb-2 é a coexistência de dois formatos de instrução, permitindo que o compilador escolha o formato mais compacto ou mais funcional, otimizando a **densidade de código** [1].

*   **Instruções de 16 bits (Thumb):** Utilizadas para operações mais comuns e simples, proporcionando alta densidade de código.
*   **Instruções de 32 bits (Extensões Thumb-2):** Introduzidas para fornecer a funcionalidade completa do conjunto de instruções ARM, incluindo acesso a registradores mais amplos e operações mais complexas.

**Estrutura de Codificação (Identificação de 32-bit):** As instruções de 32 bits são identificadas por um padrão específico no primeiro *halfword* (16 bits) da instrução. O campo de 5 bits (*bits[15:11]*) do primeiro *halfword* está no intervalo `0b11101` a `0b11111` [1].
2. Bloco IT (If-Then) - Estrutura e Operação
A instrução **IT** (If-Then) é uma instrução de 16 bits que permite a execução condicional de até quatro instruções su- **IT block**, substituindo a condicionalidade nativa de quase todas as instruções ARM de 32 bits [1].

**Formato de Instrução IT (16-bit):**
<table>
<tr>
<th>15</th>
<th>14</th>
<th>13</th>
<th>12</th>
<th>11</th>
<th>10</th>
<th>9</th>
<th>8</th>
<th>7</th>
<th>6</th>
<th>5</th>
<th>4</th>
<th>3</th>
<th>2</th>
<th>1</th>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>cond</td>
<td>mask</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>
*   **cond** (4 bits): Define a condição base para o bloco IT.
*   **mask** (4 bits): Define o número de instruções no bloco e a condição de cada uma (Then ou Else).

**Estrutura de Hardware (ITState)**: O estado de execução do bloco IT é mantido nos bits **IT[7:0]** do *Current Program Status Register* (CPSR), também conhecidos como **ITState** [1].
*   **IT[7:5]** (3 bits): Codifica a condição base (**cond_base**).
*   **IT[4:0]** (5 bits): Codifica o número de instruções restantes e a condição para cada uma.

**Pseudo-código de Operação (ITAdvance)**: A cada instrução executada dentro de um bloco IT, o estado **ITstate** é atualizado para controlar a execução da próxima instrução.
mermaid
graph TD
    A[// Inicialização do ITState pela instrução IT] --> B[IT_block_state = (cond : mask); // 8 bits]
    B --> C[IT[7:0] = IT_block_state;]
    C --> D[// Função de avanço do estado IT após cada instrução no bloco ITAdvance()]
    D --> E[IT[7:0] = (IT[7:0] << 1) AND 0xFF;]
    E --> F{if IT[7:4] == 0b0000 then}
    F --> G[IT[7:0] = 0b00000000; // Bloco IT finalizado]
| ITCondition() |
|---|
| cond_base = IT[7:5]; |
| T_bit = IT[4]; // Bit de condição (Then/Else) |
| if T_bit == 0 then |
| return (cond_base : 0); // Condição base |
| else |
| return (cond_base : 1); // Condição inversa (NOT) |
3. Densidade de Código
A **densidade de código** é um benefício arquitetural alcançado pela combinação de instruções de 16 bits (para economia de espaço) e instruções de 32 bits (para funcionalidade e desempenho), permitindo que o Thumb-2 atinja densidades de código similares ao ARM Thumb original, mas com desempenho similar ao ARM [1].
Conceito 6: Conditional Execution - Predication, condition codes NZCV, IT instruction
**Itens Técnicos Encontrados:** 21
**Conceitos-Chave:** Conditional Execution, Predication, NZCV Condition Flags, IT Instruction, ITSTATE, A32 Instruction Encoding, T32 Instruction Encoding, Conditional Select (CSEL), Conditional Move (CMOV)
Execução Condicional, Códigos de Condição NZCV e Instrução IT na Arquitetura ARM (AArch32)
igos de Condição (Condition Codes) e F
A execução condicional na arquitetura ARM (principalmente em A32 e T32) é controlada por um sufixo de código de condição anexado ao mnemônico da instrução. Este sufixo permite que o processador teste uma condição baseada nas *Condition Flags* (NZCV) do *Current Program Status Register* (CPSR).
*   **N (Negative):** Definida se o resultado da operação for negativo (bit mais significativo é 1).
*   **Z (Zero):** Definida se o resultado da operação for zero.
*   **C (Carry):** Definida se houver um *carry* (transporte) ou *borrow* (empréstimo) na operação.
*   **V (Overflow):** Definida se houver um *overflow* de complemento de dois na operação.
| Sufixo | NZCV |
| :----- | :--- |
| Z       | 0001 |
| N       | 0010 |
| C       | 0100 |
| V       | 1000 |
<table>
<tr>
<th>Sufixo</th>
<th>Flags</th>
<th>Significado</th>
</tr>
<tr>
<td><strong>EQ</strong></td>
<td>Z set</td>
<td>Igual (Equal)</td>
</tr>
<tr>
<td><strong>NE</strong></td>
<td>Z clear</td>
<td>Não igual (Not equal)</td>
</tr>
<tr>
<td><strong>CS ou HS</strong></td>
<td>C set</td>
<td>Maior ou igual sem sinal (Higher or same, unsigned &gt;=)</td>
</tr>
<tr>
<td><strong>CC ou LO</strong></td>
<td>C clear</td>
<td>Menor sem sinal (Lower, unsigned &lt;)</td>
</tr>
<tr>
<td><strong>MI</strong></td>
<td>N set</td>
<td>Negativo (Minus)</td>
</tr>
<tr>
<td><strong>PL</strong></td>
<td>N clear</td>
<td>Positivo ou zero (Plus)</td>
</tr>
<tr>
<td><strong>VS</strong></td>
<td>V set</td>
<td>Overflow</td>
</tr>
<tr>
<td><strong>VC</strong></td>
<td>V clear</td>
<td>Sem overflow</td>
</tr>
<tr>
<td><strong>HI</strong></td>
<td>C set e Z clear</td>
<td>Maior sem sinal (Higher, unsigned &gt;)</td>
</tr>
<tr>
<td><strong>LS</strong></td>
<td>C clear ou Z set</td>
<td>Menor ou igual sem sinal (Lower or same, unsigned &lt;=)</td>
</tr>
<tr>
<td><strong>GE</strong></td>
<td>N e V são iguais</td>
<td>Maior ou igual com sinal (Signed &gt;=)</td>
</tr>
<tr>
<td><strong>LT</strong></td>
<td>N e V são diferentes</td>
<td>Menor com sinal (Signed &lt;)</td>
</tr>
<tr>
<td><strong>GT</strong></td>
<td>Z clear e N e V são iguais</td>
<td>Maior com sinal (Signed &gt;)</td>
</tr>
<tr>
<td><strong>LE</strong></td>
<td>Z set ou N e V são diferentes</td>
<td>Menor ou igual com sinal (Signed &lt;=)</td>
</tr>
<tr>
<td><strong>AL</strong></td>
<td>Qualquer</td>
<td>Sempre (padrão, este sufixo é normalmente omitido)</td>
</tr>
</table>
T (If-Then) para Execução Condicional
Em instruções Thumb (T32), a execução condicional de múltiplas instruções é realizada através da instrução **IT** (If-Then).

A instrução **IT** permite que até quatro instruções subsequentes sejam executadas condicionalmente, com base em uma única condição de flag.
Formato da Instrução IT
O formato geral da instrução IT é
IT{x{y{z}}}<cond>
Onde:
*   `{x{y{z}}}` : É um campo de 1 a 3 caracteres que especifica a condição das instruções subsequentes.
    *   O primeiro caractere ( x ) é a condição da segunda instrução.
    *   O segundo caractere ( y ) é a condição da terceira instrução.
    *   O terceiro caractere ( z ) é a condição da quarta instrução.

*   `<cond>` : É o código de condição (ex: EQ , NE , GT ) que se aplica à primeira instrução no bloco IT.

Os caracteres x , y , z podem ser:

*   **T (Then)**: A instrução é executada se a condição principal ( `<cond>` ) for **verdadeira**.
*   **E (Else)**: A instrução é executada se a condição principal ( `<cond>` ) for **falsa** (ou seja, a condição oposta a `<cond>` ).
de Hardware (Algoritmo
A instrução **IT** não executa a instrução condicional em si, mas sim modifica o estado do processador para que as instruções subsequentes sejam executadas condicionalmente.

O **ITSTATE** é um campo de 8 bits no *Program Status Register* (PSR) que armazena o estado do bloco IT. Este campo é composto por:

*   **Mask (4 bits)**: Define quais das 4 instruções subsequentes são condicionais.
*   **Cond (4 bits)**: Armazena o código de condição (<cond>) para o bloco.

O hardware do processador usa o valor do ITSTATE para determinar se uma instrução deve ser executada (predicação).

**Algoritmo de Predicação (Simplificado):**

1.  **Verificação do ITSTATE**: Se ITSTATE for zero, a instrução é incondicional (exceto para branches).
2.  **Extração da Condição**: O hardware extrai o código de condição ( Cond ) e a máscara ( Mask ) do ITSTATE .
3.  **Teste da Condição**: O hardware avalia a condição ( Cond ) contra as flags NZCV.
4.  **Decisão de Execução**:
    *   Se o bit menos significativo da Mask for 1, a instrução é executada se o teste de condição for **verdadeiro**.
    *   Se o bit menos significativo da Mask for 0, a instrução é executada se o teste de condição for **falso** (condição oposta).
5.  **Atualização do ITSTATE**: O ITSTATE é atualizado para a próxima instrução, deslocando a Mask e atualizando o bit de condição para a próxima instrução.

A instrução **IT** é um mecanismo de **predicação** que reduz o custo de *branching* (desvio) para pequenos blocos de código.
rmulas e Lógica de Avaliação das Condições
| Sufixo | Condição Lógica (Fórmula) |
|---|---|
| EQ | Z = 1 |
| NE | Z = 0 |
| CS/HS | C = 1 |
| CC/LO | C = 0 |
| MI | N = 1 |
| PL | N = 0 |
| VS | V = 1 |
| VC | V = 0 |
| HI | C = 1 AND Z = 0 |
| LS | C = 0 OR Z = 1 |
| GE | N = V |
| LT | N ≠ V |
| GT | Z = 0 AND (N = V) |
| LE | Z = 1 OR (N ≠ V) |
| AL | Sempre Verdadeiro |
**Nota:** As condições GE, LT, GT e LE são usadas para comparações com sinal, e a lógica N = V (ou N ≠ V) é a fórmula técnica para verificar se ocorreu um *overflow* que alteraria o resultado da comparação.

- N = V: O resultado da subtração/comparação tem o sinal correto (não houve overflow que afetasse o sinal).
- N ≠ V: O resultado da subtração/comparação tem o sinal incorreto (houve overflow que afetou o sinal).
4. Formato de Instrução (Encoding)
strução IT em Thumb (T32) tem um formato de 16 bits:
<table>
<tr>
<td><strong>Bits</strong></td>
<td><strong>15-12</strong></td>
<td><strong>11-8</strong></td>
<td><strong>7-4</strong></td>
<td><strong>3-0</strong></td>
</tr>
<tr>
<td><strong>Valor</strong></td>
<td>1111</td>
<td>1111</td>
<td>1000</td>
<td>ITSTATE</td>
</tr>
</table>

O campo ITSTATE (4 bits) é codificado da seguinte forma:

<table>
<tr>
<td><strong>Bits</strong></td>
<td><strong>7-4</strong></td>
<td><strong>3-0</strong></td>
</tr>
<tr>
<td><strong>ITSTATE</strong></td>
<td>Cond (4 bits)</td>
<td>Mask (4 bits)</td>
</tr>
</table>
*   **Cond (bits 7-4):** O código de condição para a primeira instrução do bloco IT.
*   **Mask (bits 3-0):** Uma máscara de 4 bits que define quais instruções subsequentes são condicionais. O bit 3 é para a primeira instrução, o bit 2 para a terceira, e o bit 1 para a quarta. O bit 0 é sempre 1.
Exemplo de codificação da M
*   IT EQ: Mask = 1000 (apenas a primeira instrução é condicional)
*   ITTEE EQ: Mask = 1101 (a primeira, segunda e quarta instruções são condicionais)

A codificação exata da instrução IT é: 0b11110xxx1000yyyy onde xxxx é o campo Cond e yyyy é o campo Mask
5. Predicação em A32
Em A32 (ARM 32-bit), a predicação é mais simples: o código de condição é codificado diretamente nos 4 bits mais significativos de **toda instrução ARM de 32 bits**.
<table>
<tr>
<th>Bits</th>
<th>31-28</th>
<th>27-0</th>
</tr>
<tr>
<td>Instrução A32</td>
<td>cond (4 bits)</td>
<td>Restante da Instrução (28 bits)</td>
</tr>
</table>
O hardware verifica o campo Cond contra as flags NZCV antes de executar a instrução. Se a condição falhar, a instrução é ignorada (não-executada).
6. Predicação em A64 (AArch64)
Em A64, a maioria das instruções não possui um campo de condição de 4 bits. A predicação é substituída por:

*   **Instruções de Seleção Condicional (Conditional Select - CSEL):** Instruções que selecionam um valor entre dois operandos com base em uma condição.
*   **Instruções de Movimentação Condicional (Conditional Move - CMOV):** Semelhante ao CSEL, mas para movimentação de dados.
*   **Branches Condicionais (B.cond):** Para desvios de fluxo de controle.

As flags NZCV em A64 são armazenadas no **PSTATE** (Processor State).

*   **N (Negative):** PSTATE.N
- **Z (Zero):** PSTATE.Z  
- **C (Carry):** PSTATE.C  
- **V (Overflow):** PSTATE.V
# Line ARM - In-order Cortex-A5/A7 e Ou
ns Técnicos Encontrados: 12
**Conceitos-Chave:** Pipeline In-order 8-estágios, Pipeline Out-of-order, Hazards (RAW, WAR, WAW, Control), Forwarding, Load/Store Unit (LSU), Load/Store Buffer (LSB), Stack Architecture, Execute/Write Back Unit (EXWB), Load/Store Pipeline, Branch Prediction Unit (BPU), Reorder Buffer (ROB), Register Renaming, Reservation Station (RS), Macro-Operations Unit (MOU)
**Conteúdo Técnico: Pipeline ARM (Cortex-A5/A7 e Cortex-A76/X1)**
1. Pipeline In-order (Cortex-A5/A7)
ores Cortex-A5 e Cortex-A7 utilizam uma microarquitetura **in-order** (em ordem) com um pipeline de **8 estágios** (8-
0 [1] [2]. Embora a documentação oficial da ARM não detalhe publicamente os 8 estágios com nomes únicos para
estrutura funcional é uma expansão do pipeline clássico de 5 estágios, com estágios de memória e execução
aumentar a frequência de clock (clock rate) [3].
1.1. Estrutura Funcional do Pipeline (8 Estágios)
trutura funcional básica de um pipeline in-order é
<table>
<tr>
<th>Estágio</th>
<th>Função Principal</th>
</tr>
<tr>
<td><strong>Fetch (Busca)</strong></td>
<td>Busca a instrução do cache L1l ou memória.</td>
</tr>
<tr>
<td><strong>Decode (Decodificação)</strong></td>
<td>Decodifica a instrução e lê os registradores.</td>
</tr>
<tr>
<td><strong>Execute (Execução)</strong></td>
<td>Executa a operação da ALU ou calcula o endereço.</td>
</tr>
<tr>
<td><strong>Memory (Memória)</strong></td>
<td>Acesso ao cache L1D ou memória (para Load/Store).</td>
</tr>
<tr>
<td><strong>Write-Back (Escrita)</strong></td>
<td>Escreve o resultado de volta no banco de registradores.</td>
</tr>
</table>
No pipeline de 8 estágios do Cortex-A5/A7, os estágios de busca, decodificação e execução são tipicamente subdivididos
*   **Busca (Fetch):** 2-3 estágios (e.g., F1, F2, F3) para acesso ao cache de instrução e pré-decodificação.
*   **Decodificação (Decode):** 1-2 estágios (e.g., D1, D2) para decodificação completa e leitura de registradores.
*   **Execução (Execute):** 1-2 estágios (e.g., E1, E2) para execução da ALU.
*   **Memória (Memory):** 1-2 estágios (e.g., M1, M2) para acesso à memória (Load/Store).
*   **Write-Back (Escrita):** 1 estágio (W) para escrita do resultado.
I.2. Resolução de Hazards (II)
# 1.2. Resolução de Hazards (in-order)

Em pipelines in-order, a principal técnica para evitar *Data Hazards* (RAW - Read After Write) é o **Data Forwarding** (ou Bypass) [4].

- **Estrutura de Hardware:** Forwarding Unit (Unidade de Encaminhamento).
- **Algoritmo (Forwarding):** A unidade de encaminhamento detecta se uma instrução no estágio E (Execute) ou M (Memory) produz um resultado que será consumido por uma instrução no estágio D (Decode) ou E (Execute). Se detectado, o resultado é encaminhado (bypass) diretamente do registrador de pipeline (latch) para a entrada da ALU, evitando o stall (parada) do pipeline.
- **Hazards de Controle**: Resolvidos pela **Branch Prediction Unit (BPU)** (Unidade de Predição de Desvio) [5]. O Cpu utiliza predição dinâmica de desvio [1]. Em caso de predição incorreta, o pipeline é esvaziado (flush) e a busca no endereço correto.
2. Pipeline Out-of-order (Cortex-A76/X1)
Os processadores Cortex-A76 e Cortex-X1 utilizam uma microarquitetura **out-of-order** (fora de ordem) e **superscalar** (múltiplas emissões) para alto desempenho [6] [7]. O Cortex-A76 possui um pipeline de 13 estágios [8], enquanto o Cortex-X1 possui um pipeline mais profundo e complexo.
2.1. Estruturas de Hardware para Out-of-order Execução
A execução fora de ordem é habilitada por três estruturas principais que implementam o **Algoritmo de Tomasulo** ou variantes:

1.  **Register Renaming (Renomeação de Registradores):**
    *   **Função:** Elimina os *Hazards* de dependência falsa (WAR - Write After Read e WAW - Write After Write) ao mapear os registradores arquiteturais (visíveis ao programador) para um conjunto maior de **Registradores Físicos** (Physical Registers) [9].
    *   **Estrutura de Hardware:** Register Alias Table (RAT) e o banco de registradores físicos.
2. Reservation Station (RS) / Issue Queue (IQ):
*   **Função:** Buffer que armazena as micro-operações (µops) decodificadas, aguardando a disponibilidade dos operandos e das unidades de execução.
*   **Algoritmo (Agendamento):** As µops são despachadas da RS para as unidades de execução (ALUs, Load/Store Units) assim que seus operandos estiverem prontos, independentemente da ordem original do programa (out-of-order execution) [10].
3. Reorder Buffer (ROB) / Retirement Register:
*   **Função:** Armazena os resultados das instruções executadas fora de ordem. Garante que os resultados sejam escritos no estado arquitetural (registradores e memória) na ordem original do programa (**in-order commitment** ou **in-order retirement**) [11].
*   **Protocolo:** O protocolo de commit in-order é crucial para a precisão de interrupções e exceções. O resultado de uma instrução só é visível para o resto do sistema quando atinge o topo do ROB e é “comitado” (commit) [11].

### 2.2. Formato de Instrução (Macro-Operations - MOPs)

*   **Algoritmo de Decodificação:** O Cortex-A76/X1 converte as instruções nativas ARM (AArch64) em uma ou mais Macro-Operations (MOPs) ou Micro-Operations (µops) [7].
*   **Estrutura:** O Cortex-X1 pode despachar até **8 MOPs** por ciclo [7]. Essas MOPs são o formato interno de instrução usado para agendamento e execução no pipeline out-of-order.
3. Hazards de Pipeline (C)
Os hazards são problemas que impedem a execução de uma instrução no ciclo de clock id
<table>
<tr>
<th>Tipo de Hazard</th>
<th>Descrição Técnica</th>
<th>Resolução (In-order)</th>
<th>Resolução (Out-of-order)</th>
</tr>
<tr>
<td>Data Hazard<br/>(RAW)</td>
<td>Read After Write: Uma instrução lê um registrador antes que uma instrução anterior o escreva.</td>
<td>Forwarding Unit<br/>(Encaminhamento de dados).</td>
<td>Register Renaming (Eliminação da dependência falsa) e Forwarding.</td>
</tr>
<tr>
<td>Data Hazard<br/>(WAR)</td>
<td>Write After Read: Uma instrução escreve um registrador antes que uma instrução anterior o leia.</td>
<td>Não ocorre em pipelines in-order simples.</td>
<td>Register Renaming (Eliminação da dependência falsa).</td>
</tr>
<tr>
<td>Data Hazard<br/>(WAW)</td>
<td>Write After Write: Uma instrução escreve um registrador antes que uma instrução anterior o escreva.</td>
<td>Não ocorre em pipelines in-order simples.</td>
<td>Register Renaming (Eliminação da dependência falsa).</td>
</tr>
<tr>
<td><strong>Control<br/>Hazard</strong></td>
<td>Ocorre devido a desvios (branches). A próxima instrução a ser buscada é desconhecida.</td>
<td>Branch Prediction Unit (BPU) e <em>pipeline flush</em> em caso de erro.</td>
<td>BPU, execução especulativa e <em>squashing</em> (descarte) de instruções especulativas em caso de erro.</td>
</tr>
<tr>
<td><strong>Structural<br/>Hazard</strong></td>
<td>Duas instruções tentam acessar o mesmo recurso de hardware no mesmo ciclo (e.g., mesma porta de memória).</td>
<td>Duplicação de recursos ou inserção de <em>stall</em> (parada).</td>
<td>Múltiplas unidades de execução e Reservation Stations.</td>
</tr>
</table>
Referências
[1] ARM. Cortex-A5 Technical Reference Manual. [2] ARM. Cortex-A7 Product Support. [3] Wolfware. Cortex-A72 Microarchitecture. [4] GeeksforGeeks. Data Hazards and its Handling Methods. [5] ARM. Branch prediction and cycle counts. [6] ARM. Cortex-A76 Software Optimization Guide. [7] EE Journal. ARM Cortex-X1 Launches High-Performance Line. [8] Intel. Hard Processor System Technical Reference Manual. [9] StackExchange. How efficient is register renaming?. [10] ScienceDirect. Out-of-Order Processor - an overview. [11] Wei Wang. Out-of-Order Execution: Reorder Buffer.
Conceito 8: Branch Prediction ARM (BTB, Return Stack, BTAC
**Tens Técnicos Encontrados:**
**Conceitos-Chave:** Branch Target Buffer (BTB), Branch Target Address Cache (BTAC), Return Stack (RS), Contador Saturante de Bits, Algoritmo Gshare, Penalidade de Erro de Previsão
Conteúdo Técnico: Branch Prediction ARM (BTB, Return Stack, BTAC)
Estruturas de Hardware de Previsão
**Branch Target Buffer (BTB)**
O **Branch Target Buffer (BTB)** é uma estrutura de cache que armazena o endereço alvo (branch target address) de desvios previamente tomados. Sua função é fornecer o endereço da próxima instrução a ser buscada antes que o desvio seja resolvido no pipeline.
h Target Address Cache
O **Branch Target Address Cache (BTAC)** é uma estrutura de hardware dedicada à previsão do endereço alvo de desvios indireto excluindo tipicamente os retornos de sub-rotina. Variações em arquiteturas ARM incluem:

*   **Cortex-R52:** BTAC de 16 entradas.
*   **MP11:** RAM alvo de desvio organizada como um bloco de 128x63 (sem paridade) ou 128x71 (com paridade).
*   **Indexação:** O BTAC é indexado por uma porção truncada do endereço da instrução de desvio e pode armazenar múltiplos alvos por entrada.
Pilha de Retorno (Return Stack - RS)
A **Pilha de Retorno (Return Stack)** é uma estrutura de hardware que armazena endereços de retorno de sub-rotinas aninhadas, sendo mais precisa para retornos do que o BTB. O endereço armazenado é o valor do registrador de ligação (link register), R14 (AArch32) ou X30 (AArch64), juntamente com o estado do conjunto de instruções.
olo de Instruções (PUSH/PO
O protocolo de operação da Pilha de Retorno é definido pelas seguintes instruções:
<table>
<tr>
<th>Operação</th>
<th>Instruções AArch32</th>
<th>Instruções ARM</th>
</tr>
<tr>
<td><strong>PUSH</strong> (Chamada)</td>
<td>BL r14, BLX (immediate), BLX (register), MOV pc,r14</td>
<td>BL r14, BLX (immediate), BLX (register), MOV pc,r14</td>
</tr>
<tr>
<td><strong>POP</strong> (Retorno)</td>
<td>BX, LDR pc, [r13], #imm, LDM r13, {...pc}</td>
<td>BX, LDR pc, [r13], #imm, LDM r13, {...pc}</td>
</tr>
</table>
o de exceção (ERET) não são previstas e não interagem com
Algoritmos e Fórmulas de Previsão Dinâmica
Algoritmo Gshare (Princípio de Indexação)
A previsão de desvio dinâmica utiliza preditores correlacionados, como o **Gshare**, que combinam o endereço do desvio com o histórico global de desvios para indexar a Tabela de Histórico de Padrões (PHT).

**Fórmula de Indexação (Conceitual):** $Índice = Endereço\ do\ Desvio \oplus Registro\ de\ Histórico\ Global\ (GHR)_{Onde\ oplus\ representaaoperacao\ **XOR**\ *(ou\ outra\ funcao\ *hashing*)aplicadaabitsselecionadosdoendereçodesvioedo\ *Registro\ de\ Histórico\ Global(GHR)\ **, que armazena os resultados dos últimos N$ desvios executados.
Máquina de Estados do Contador Saturante de 2 Bits
Cada entrada na PHT é um **contador saturante de 2 bits** que implementa uma máquina de estados finitos de previsão.
<table>
<tr>
<th>Estado (Binário)</th>
<th>Nome do Estado</th>
<th>Previsão</th>
<th>Transição se Tomado (T)</th>
<th>Transição se Não Tomado (NT)</th>
</tr>
<tr>
<td>11</td>
<td><strong>Strongly Taken (ST)</strong></td>
<td>Tomado (T)</td>
<td>Permanece em 11</td>
<td>Transiciona para 10</td>
</tr>
<tr>
<td>10</td>
<td><strong>Weakly Taken (WT)</strong></td>
<td>Tomado (T)</td>
<td>Transiciona para 11</td>
<td>Transiciona para 00</td>
</tr>
<tr>
<td>01</td>
<td><strong>Weakly Not Taken (WNT)</strong></td>
<td>Não Tomado (NT)</td>
<td>Transiciona para 10</td>
<td>Transiciona para 00</td>
</tr>
<tr>
<td>00</td>
<td><strong>Strongly Not Taken (SNT)</strong></td>
<td>Não Tomado (NT)</td>
<td>Transiciona para 01</td>
<td>Permanece em 00</td>
</tr>
</table>
Fórmula da Penalidade de Erro de Previsão
A penalidade de desempenho imposta por um erro de previsão de desvio em um *pipeline* ARM é quantificada pela relação:
l (Ciclos) = Taxa de Erro de Previsão × Latência de Erro
A **Latência de Erro de Previsão** é o número de ciclos necessários para limpar o *pipeline* e buscar a instrução variando entre 4 a 7 ciclos em arquiteturas RISC profundas.
Conceito 9: Register File ARM - 31 general purpose registers, X0-X30, zero XZR, stack pointer SP
**Itens Técnicos Encontrados:** 5
**Conceitos-Chave:** General Purpose Registers (GPRs), Xn, Wn, Zero Extension, Zero Register (XZR/WZR), Stack Codificação de Registrador (5 bits)
do Técnico: Register File ARM
O conjunto de registradores de propósito geral (General Purpose Registers - GPRs) na arquitetura **AArch64** (ARMv8-A e posteriores) é uma estrutura fundamental que define o estado do processador e o formato das operações de dados.
Formato dos Registradores de Propó
A arquitetura AArch64 fornece **31 registradores** de propósito geral.
**Estrutura Dual-View:** Cada registrador é fisicamente um registrador de **64 bits** (denominado **Xn**, onde n varia de 0 a 30) e o mesmo espaço de armazenamento pode ser acessado como um registrador de **32 bits** (denominado **Wn**).

**Mapeamento de Bits:** O registrador de 32 bits **Wn** corresponde aos 32 bits menos significativos (bits [31:0]) do registrador de 64 bits **Xn**. Os 32 bits mais significativos (bits [63:32]) de Xn são implicitamente manipulados em operações de 32 bits.
Algoritmo de Extensão de Zero (Zero I
O comportamento de extensão de zero é um protocolo de hardware/software que define o estado dos bits superiores de um registrador de 64 bits após uma operação de 32 bits.

**Protocolo de Escrita em Wn:** Quando uma instrução de processamento de dados escreve um resultado no registrador de 32 bits **Wn**, o hardware executa o seguinte algoritmo:
<table>
<tr>
<td>$Xn[63:32] \gets 0$</td>
</tr>
<tr>
<td>$Xn[31:0] \gets Resultado_{32-bit}$</td>
</tr>
</table>
- **Implicação:** A escrita em um registrador Wn sempre resulta na **extensão de zero** (zero-extension) do valor de 32 bits para o registrador Xn de 64 bits. Isso garante que o valor de 64 bits seja canônico após uma operação de 32 bits.
3. Registrador Zero (XZR e WZR)
registrador de número 31 (índice 31) é um registrador especial que implementa o conceito de **Zero Register** (Registra

*   **Estrutura e Nomenclatura:**
    *   **XZR:** Representação de 64 bits.
    *   **WZR:** Representação de 32 bits.

*   **Protocolo de Leitura:** Qualquer leitura de **XZR** ou **WZR** retorna o valor **0x0000000000000000** (64 bits de zero).

*   **Protocolo de Escrita:** Qualquer tentativa de escrita em **XZR** ou **WZR** é **ignorada** pelo hardware.
Stack Pointer (SP)
O Stack Pointer (SP) é um registrador de 64 bits que, embora compartilhe o índice 31 com o XZR/WZR em algumas instruções, possui um comportamento e uso restritos.

*   **Estrutura de Hardware:** O SP não é um GPR regular. A arquitetura AArch64 define múltiplos Stack Pointers, um para cada Nível de Exceção (Exception Level - ELx). O uso do símbolo SP em uma instrução refere-se ao Stack Pointer ativo para o nível de exceção atual.
*   **Protocolo de Uso:** O SP é primariamente utilizado como endereço base para operações de memória.
    *   **Uso Permitido:** Pode ser usado como registrador base em instruções de **Load and Store** (carregamento e armazenamento).
    *   **Uso Restrito:** Pode ser usado com um conjunto limitado de instruções de processamento de dados (e.g., para manipulação do ponteiro da pilha), mas não é um operando de propósito geral.
Formato de Instrução (Codificação do Receptor)
| O campo de codificação do registrador (geralmente um campo de 5 bits) em instruções A64 determina se o operando é um GPR (X0-X30), o Registrador Zero (XZR/WZR) ou o Stack Pointer (SP). |  |
|---|---|
<table>
<tr>
<th>Codificação (5 bits)</th>
<th>Contexto de 64 bits (X)</th>
<th>Contexto de 32 bits (W)</th>
<th>Uso em Load/Store</th>
</tr>
<tr>
<td>00000 - 11110 (0-30)</td>
<td>X0 - X30</td>
<td>W0 - W30</td>
<td>GPR</td>
</tr>
<tr>
<td>11111 (31)</td>
<td>XZR</td>
<td>WZR</td>
<td><strong>SP</strong> (como endereço base)</td>
</tr>
</table>
* **Protocolo de Decodificação:** O valor binário 11111 (decimal 31) no campo de registrador é decodificado de forma contextual:
    * Em instruções de processamento de dados que não usam o SP (e.g., ADD X31, X1, X2 ), ele é interpretado como **XZR**.
    * Em instruções de carregamento/armazenamento que usam um endereço base (e.g., LDR X0, [SP, #offset ]), ele é interpretado como **SP**.
    * A distinção entre XZR e SP é feita pelo tipo de instrução (processamento de dados vs. acesso à memória) e pelo campo de tamanho (64 bits vs. 32 bits).
Conceito 10: Unidades de Execução ARM (Integer ALU, FP/NEON, Crypto, Load/Store)
**Itens Técnicos Encontrados:** 23

**Conceitos-Chave:** Pipeline Cortex-A55, Integer ALU, FP/NEON Units, Crypto Accelerator, Load/Store Ports, Dual-Issue, Latência de Instrução, Algoritmo AES, Requisitos de Alinhamento
# Conteúdo Técnico: Unidades de Execução ARM (Cortex-A55)
1. Estruturas de Hardware e Pipeline
A microarquitetura do Cortex-A55 implementa pipelines distintos para operações de inteiro e ponto flutuante/S (ASIMD/NEON).
1.1. Pipeline e Estágios
<table>
<tr>
<th>Tipo de Instrução</th>
<th>Profundidade do Pipeline</th>
<th>Estágios Principais</th>
<th>Datapath NEON/FP</th>
</tr>
<tr>
<td><strong>Inteiro (Integer ALU)</strong></td>
<td>8 estágios</td>
<td>iss, ex1, ex2, wr, ret</td>
<td>N/A</td>
</tr>
<tr>
<td><strong>FP/NEON (ASIMD)</strong></td>
<td>10 estágios</td>
<td>iss, ex1, ex2, wr, ret</td>
<td>f1, f2, f3, f4, f5</td>
</tr>
</table>
1.2. Unidades de Execução (Funcionais)
O core possui múltiplas unidades funcionais, incluindo:
<table>
<tr>
<th>Unidade de Execução</th>
<th>Tipo de Operação</th>
<th>Estágios de Execução</th>
<th>Função Principal</th>
</tr>
<tr>
<td><strong>ALU0 / ALU1</strong></td>
<td>Inteiro</td>
<td>ex1 , ex2</td>
<td>Aritmética e Lógica (Shift, ALU)</td>
</tr>
<tr>
<td><strong>MAC</strong></td>
<td>Inteiro</td>
<td>ex1 , ex2</td>
<td>Multiplicação-Acumulação (32-bit x 32-bit por ciclo)</td>
</tr>
<tr>
<td><strong>DIV</strong></td>
<td>Inteiro</td>
<td>ex1 , ex2</td>
<td>Divisão ( UDIV , SDIV )</td>
</tr>
<tr>
<td><strong>Load AGU</strong></td>
<td>Load/Store</td>
<td>ex1</td>
<td>Geração de Endereço de Carga</td>
</tr>
<tr>
<td><strong>Store AGU</strong></td>
<td>Load/Store</td>
<td>ex1</td>
<td>Geração de Endereço de Armazenamento</td>
</tr>
<tr>
<td><strong>NEON/FP</strong></td>
<td>FP/ASIMD</td>
<td>f1 a f5</td>
<td>MAC, DIV/SQRT, ALU para Ponto Flutuante e SIMD</td>
</tr>
</table>
2. Protocolos e Formatos de Instrução
2.1. Requisitos de Alinhamento (Load/Store)
| O pipeline de Load/Store suporta leituras de até 64 bits e escritas de até 128 bits. O não cumprimento dos requisitos de alinhamento abaixo resulta em penalidade de ciclo: |
|---|---|
<table>
<tr>
<th>Operação</th>
<th>Tamanho (bits)</th>
<th>Requisito de Alinhamento</th>
</tr>
<tr>
<td><strong>Load</strong></td>
<td>16, 32</td>
<td>Endereço não deve cruzar limite de 64-bit</td>
</tr>
<tr>
<td><strong>Load</strong></td>
<td>64, 128</td>
<td>Endereço deve ser alinhado a 64-bit</td>
</tr>
<tr>
<td><strong>Store</strong></td>
<td>16, 32, 64</td>
<td>Endereço não deve cruzar limite de 128-bit</td>
</tr>
<tr>
<td><strong>Store</strong></td>
<td>128</td>
<td>Endereço deve ser alinhado a 128-bit</td>
</tr>
</table>
Instruções Criptográficas (Crypto Accelerator)
O acelerador criptográfico suporta o algoritmo AES com instruções que são emitidas em um único ciclo.

**Formato de Instrução (Dual-Issue para AES):** Para otimização, pares de instruções podem ser emitidos duplamente:

*   AESE Vn, -, AESMC Vn, Vn (Criptografia AES)
*   AESD Vn, -, AESIMC Vn, Vn (Descriptografia AES)

**Instruções Criptográficas Principais:**

*   AESE : AES Single Round Encryption
*   AESD : AES Single Round Decryption
*   AESMC : AES Mix Columns
*   AESIMC : AES Inverse Mix Columns
As latências (em ciclos) representam o tempo necessário para a conclusão da operação, um fator chave no desempenho do algoritmo.
<table>
<tr>
<th>Operação</th>
<th>Latência (Ciclos)</th>
</tr>
<tr>
<td>Multiplicação 32-bit</td>
<td>1</td>
</tr>
<tr>
<td>Multiplicação 64-bit</td>
<td>2 a 3</td>
</tr>
<tr>
<td>SMULH / UMULH</td>
<td>4</td>
</tr>
<tr>
<td>Divisão 32-bit</td>
<td>Até 12</td>
</tr>
<tr>
<td>Divisão 64-bit</td>
<td>Até 20</td>
</tr>
</table>
3.2. Latência de Instruções FP/NEON (Single-Precision)
Instruções FP/NEON complexas permitem *out-of-order retire*. As latências listadas são para precisão simples (Single-Precision):

| Instrução (FP ou NEON) | Latência (Ciclos) |
| :-------------------- | :---------------- |
| VDIV / FDIV           | 13                |
| VSQRT / FSQRT         | 12                |
| VMLA / VNMULA , VMLS / VNMLS , VRECPS , VRSORTS | 8                 |
| VFMA / FMADD , VFNMA / FNMAADD , VFMS / FMSUB , VFNMS / FNMSUB | 4                 |
Conceito 11: Load-Store Architecture - Memory access only via load/ addressing modes, alignment
**Itens Técnicos Encontrados: 10**
Store Architecture, Modos de Endereçamento, Offset Addressing, Offset Imediato Escalonado, Formato de Instrução A64, Bit Field
dos de Endereçamento Load/Store na Arquitetura ARM
A arquitetura AArch64 possui três modos de endereçamento fundamentais para instruções Load/Store: **offset directo**, **offset imediato** e **literal**.
Estes modos são utilizados para calcular o endereço de memória para as operações de acesso (Load/Store)
# 1. Offset Addressing (Offset Simples)

O valor do offset é **aplicado** ao endereço obtido do registrador base (Rn). O resultado é usado como o endereço para o acesso à memória. O registrador base (Rn) permanece **inalterado**.

## Sintaxe Assembly:

```assembly
[Rn, offset]
```

## Fórmula de Cálculo de Endereço (Conceitual):
$Endereço Efetivo = Valor(Rn) + Offset$

# 2. Pre-indexed Addressing (Pré-indexação com Write-Back)

O valor do offset é **aplicado** ao endereço obtido do registrador base (Rn). O resultado é usado como o endereço para o acesso à memória, e o novo endereço é **escrito de volta** (write-back) no registrador base (Rn).

## Sintaxe Assembly:

```assembly
[Rn, offset]!
```

## Fórmula de Cálculo de Endereço e Write-Back:
$Endereço Efetivo = Valor(Rn) + Offset$
$Valor(Rn)_{novo} = Endereço Efetivo$

# 3. Post-indexed Addressing (Pós-indexação com Write-Back)

O endereço obtido do registrador base (Rn) é usado, **inalterado**, como o endereço para o acesso à memória. O valor do offset é **aplicado** ao endereço original, e o novo endereço é **escrito de volta** (write-back) no registrador base (Rn).

## Sintaxe Assembly:
**Cálculo de Endereço e Write-Back:** $Endereço Efetivo =\\ novo = Valor(Rn)_{original} + Offset$
Tipos de Offset

O offset pode ser
* Uma **constante imediata**.
* Um **registrador de índice** (Rm).
* Um **registrador de índice deslocado** (e.g., Rm, LSL #shift).
Instruções Load/Store de Pares (LDP)
As instruções **STP** (Store Pair) e **LDP** (Load Pair) armazenam ou carregam dois registradores de 32 ou 64 bits em uma única instrução.
**Modos de Endereçamento para LDP/STP**

- Post-index
- Pre-index
- Signed offset (Offset Assinado)
**Regra de Offset Imediato (Unsigned offset):** Para a variante **Unsigned offset** das instruções Load/Store (immediate), o valor do offset imediato é **escalado** pelo tamanho do valor acessado *antes* de ser adicionado ao valor do registrador base.

**Fórmula de Cálculo de Endereço (Unsigned Offset Scaled):** $Endereço Efetivo = Valor(Rn) + (Offset Imediato × Tamanho do Dado)$ Onde:

- Tamanho do Dado = 1 (Byte), 2 (Halfword), 4 (Word), 8 (Doubleword).
- O offset imediato é um valor não assinado.
Formato de Instrução Load/Store A64 (Bit Fields)
As instruções Load/Store (LDR/STR) na arquitetura AArch64 (ARMv8-A) são codificadas em 32 bits. O formato geral para as instruções de acesso à memória é determinado por campos de bits específicos.
Codificação Geral de Loads/Stores (AArch64)
O grupo de instruções loads/stores é identificado pelos bits fixos no campo principal.
<table>
<tr>
<td></td>
<td><b>31</b></td>
<td><b>30</b></td>
<td><b>29</b></td>
<td><b>28</b></td>
<td><b>27</b></td>
<td><b>26</b></td>
<td><b>25</b></td>
<td><b>24</b></td>
<td><b>23</b></td>
<td><b>22</b></td>
<td><b>21</b></td>
<td><b>20</b></td>
<td><b>19</b></td>
<td><b>18</b></td>
<td><b>17</b></td>
<td><b>16</b></td>
<td>...</td>
</tr>
<tr>
<td>oo</td>
<td>op1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>op2</td>
<td>op3</td>
<td>op4</td>
<td>op5</td>
<td>...</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>
*   **op1 (Bit 31):** Determina o tamanho do dado (W=32-bit, X=64-bit).
*   **Bits [30:27]:** Fixos para identificar o grupo de Loads/Stores.
*   **op2 (Bit 26):** Varia dependendo do tipo de instrução (e.g., Load/Store par, Load/Store simples).
*   **op3 (Bits [25:24]):** Varia.
*   **op4 (Bits [23:21]):** Varia.
*   **op5 (Bits [15:12]):** Varia.
Exemplo: Load/Store com Offset Imediato Não Escalonado (load/store-reg/unscaled-imm)
<table>
<tr>
<td>Bits</td>
<td>31</td>
<td>30</td>
<td>29</td>
<td>28</td>
<td>27</td>
<td>26</td>
<td>25</td>
<td>24</td>
<td>23</td>
<td>22</td>
<td>21</td>
<td>20</td>
<td>19</td>
<td>18</td>
<td>17</td>
<td>16</td>
<td>15</td>
<td>14</td>
<td>13</td>
<td>12</td>
<td>11</td>
<td>10</td>
<td>9</td>
<td>8</td>
<td>7</td>
<td>6</td>
</tr>
<tr>
<td>Campo</td>
<td>size</td>
<td><strong>0</strong></td>
<td><strong>0</strong></td>
<td><strong>1</strong></td>
<td><strong>0</strong></td>
<td><strong>0</strong></td>
<td><strong>0</strong></td>
<td><strong>opc</strong></td>
<td><strong>0</strong></td>
<td><strong>0</strong></td>
<td><strong>0</strong></td>
<td><strong>imm9</strong></td>
<td>Rn</td>
<td>Rt</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Valor</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>
*   **size (Bits [31:30])**: Determina o tamanho do dado (00=Byte, 01=Halfword, 10=Word, 11=Doubleword).
*   **opc (Bits [23:22])**: Determina a operação (e.g., 00=STR, 01=LDR, 10=STR com alocação, 11=LDR com alocação)
*   **imm9 (Bits [20:12])**: Offset imediato de 9 bits (assinado).
*   **Rn (Bits [9:5])**: Registrador base.
*   **Rt (Bits [4:0])**: Registrador de destino/fonte.
**Exemplo: Load/Store com Offset Imediato Escalonado (load/store-reg/unsigned-imm)**

Este formato é usado para acesso a words e doublewords com um offset imediato escalonado.
*   **size (Bits [31:30])**: Determina o tamanho do dado (00=Byte, 01=Halfword, 10=Word, 11=Doubleword)
*   **opc (Bits [23:22])**: Determina a operação.
*   **imm12 (Bits [20:10])**: Offset imediato de 12 bits (não assinado).
*   **Rn (Bits [9:5])**: Registrador base.
*   **Rt (Bits [4:0])**: Registrador do destino/fonte
**Fórmula de Cálculo de Endereço (Unsigned Offset Scaled - Detalhada):** $Endereço Efetivo = Valor(Rn) + (imm12 \times 2^{size})$

$Onde2^{\wedge\{text[size]\}}$ é o fator de escala (1, 2, 4 ou 8) que garante o **alinhamento** para o tipo de dado.
As de Alinhamento de Memória (AArch)
A arquitetura ARMv8-A (AArch64) geralmente suporta acessos não alinhados, mas com penalidade de desempenho. Para **melhor desempenho**, o alinhamento é crucial.

**Regra Geral de Alinhamento:** O endereço de memória para um acesso de $N$ bytes deve ser divisível por $N$.
<table>
<tr>
<th>Tipo de Dado</th>
<th>Tamanho (Bytes)</th>
<th>Requisito de Alinhamento (Endereço Modulo N)</th>
</tr>
<tr>
<td>Byte</td>
<td>1</td>
<td>Endereço ≡ 0 (mod 1) (Sempre alinhado)</td>
</tr>
<tr>
<td>Halfword</td>
<td>2</td>
<td>Endereço ≡ 0 (mod 2)</td>
</tr>
<tr>
<td>Word</td>
<td>4</td>
<td>Endereço ≡ 0 (mod 4)</td>
</tr>
<tr>
<td>Doubleword</td>
<td>8</td>
<td>Endereço ≡ 0 (mod 8)</td>
</tr>
</table>
**Fórmula de Verificação de Alinhamento:** $Endereço \bmod Tamanho\ do\ Dado = 0$
**Alinhamento de Estruturas (Structs):** O alinhamento de uma estrutura é o **alinhamento do seu membro requisito de alinhamento**. O tamanho total da estrutura é arredondado para ser um múltiplo do seu alinhamento.

**Fórmula de Padding (Conceitual):** $Tamanho\ Total - \lfloor Soma\ dos\ Tamanhos + Padding \rfloor \times Alinhamento\ Máximo$
Conceito 12: Instruction Fusion - Macro-op fusion, micro-op cache, decode bandwidth optimization
**Itens Técnicos Encontrados:** 9
**Conceitos-Chave:** MOVPRFX, Macro-op Fusion, Micro-op Cache, Decode Bandwidth Optimization, SVE, SVE2, Protocolo de Codificação A64, Largura de Banda Efetiva
# Conteúdo Técnico: Instruction Fusion, Micro-op Cache e Otimização de Largura de Banda de Decodificação (Arquitetura ARM)
1. Macro-op Fusion via Instrução MOVPRFX (SVE/SVE2)
n na arquitetura ARM, aplicado principalmente às extensõ
o através da instrução **MOVPRFX** (Move Prefix).
# 1.1. Formato e Codificação da Instrução MOVPRFX

A instrução MOVPRFX é um prefixo de instrução que sinaliza ao hardware a possibilidade de fusão com a instrução su

**Formato Assembly (MOVPRFX unpredicated):**
M0VPRFX<Zd>(.).<T>,<Zn>(.).<T>
* `<Zd>` : Registrador de destino SVE.
* `<Zn>` : Registrador de origem SVE.
* `<T>` : Tamanho do elemento (B, H, S, D)
**Codificação A64 (SVE || FEAT_SME):** A codificação da instrução MOVPRFX no formato A64 é a seguinte, onde os opc2, opc3, opc4, opc5 e os bits 21 e 20 definem a operação de prefixo SVE/SME.
<table>
<tr>
<th><strong>Bits</strong></th>
<th><strong>31-30</strong></th>
<th><strong>29-24</strong></th>
<th><strong>23-22</strong></th>
<th><strong>21</strong></th>
<th><strong>20</strong></th>
<th><strong>19-16</strong></th>
<th><strong>15-12</strong></th>
<th><strong>11-10</strong></th>
<th><strong>9-5</strong></th>
<th><strong>4-0</strong></th>
</tr>
<tr>
<td>Campo</td>
<td>opc</td>
<td>opc2</td>
<td>size</td>
<td>1</td>
<td>0</td>
<td>opc3</td>
<td>opc4</td>
<td>opc5</td>
<td>Zn</td>
<td>Zd</td>
</tr>
<tr>
<td>Valor</td>
<td>00</td>
<td>000000</td>
<td>size</td>
<td>1</td>
<td>0</td>
<td>0000</td>
<td>0000</td>
<td>00</td>
<td>Zn</td>
<td>Zd</td>
</tr>
</table>
1.2. Protocolo de Fusão (Regras de Hardware)
A fusão de MOVPRFX com a instrução destrutiva subsequente é um protocolo de microarquitetura sujeito às seguintes condições:

1.  **Instrução Prefixa:** A instrução MOVPRFX atua como uma **dica de hardware** para fusão.
2.  **Instrução Subsequente:** A instrução imediatamente seguinte (PC+4) deve ser uma instrução SVE binária ou ternária **destrutiva**, ou uma operação unária com predicação de mesclagem.
3.  **Exclusão:** A instrução subsequente **não pode** ser outra instrução MOVPRFX.
4.  **Coincidência de Destino:** A instrução subsequente deve especificar o **mesmo registrador de destino** (Zd) que a instrução MOVPRFX.
5.  **Restrição de Operando:** O registrador de destino (Zd) **não deve ser usado** em qualquer outra posição de operando (como operando de origem) na instrução subsequente.

A fusão bem-sucedida resulta na execução do par de instruções como uma **única micro-operação (micro-op)**, eliminando a micro-op de cópia de vetor discreta e otimizando o *issue width* do backend.
2. Estrutura e Função do Micro-op Cache (uop Cache)
Processadores ARM de alto desempenho incorporam uma **Micro-op Cache** (também conhecida como *Decoded Instruction Cache* ou *Instruction Cache* de micro-operações) como uma estrutura de hardware para otimizar a largura de banda de decodificação.

**Estrutura Conceitual:**
*   **Localização:** Posicionada após o estágio de decodificação do frontend do pipeline.
*   **Conteúdo:** Armazena micro-operações decodificadas (*uops*) ou macro-operações (*mops*) resultantes da fusão.
*   **Mecanismo de Operação:** Funciona como um *stream buffer* que fornece micro-ops diretamente ao backend do pipeline (estágios de *rename* e *issue*), contornando o decodificador principal.

**Otimização da Largura de Banda de Decodificação:** A Micro-op Cache contribui para a otimização da largura de banda de decodificação através de:

1.  **Redução de Latência:** Elimina a latência e o consumo de energia do estágio de decodificação para instruções repetidas (ex: em loops).
2.  **Aumento de Throughput:** Aumenta a taxa efetiva de fornecimento de micro-ops por ciclo, superando a limitação de decodificação do frontend (por exemplo, permitindo que mais de 4 micro-ops sejam emitidas por ciclo).
3.  **Mitigação de Complexidade:** Em arquiteturas como a ARM, que mantêm um formato de instrução RISC simples, a *uop cache* é usada para otimizar o fornecimento de instruções, especialmente em cenários de fusão como o *MOVPRFX*.
Algoritmo de Otimização de Largura de Arco
A otimização da largura de banda de decodificação é um algoritmo microarquitetural composto por:

Largura de Banda Efetiva ∝ Decodificação + Hit Rate<sub>hop Cache</sub> + Fusão<sub>MOVPRFX</sub>
*   **Decodificação:** Taxa de decodificação do frontend (Instruções/Ciclo).
*   **Hit Rate<sub>uop Cache</sub>:** Probabilidade de a instrução ser encontrada na Micro-op Cache, resultando em um fornecimento de micro-ops de alta velocidade.
*   **Fusão<sub>MOVPRFX</sub>:** Redução do número de micro-ops por instrução arquitetural (IPC) através da fusão de pares de instruções (ex: MOVPRFX + instrução destrutiva) em uma única micro-op.

A otimização é um processo dinâmico que seleciona a fonte de micro-ops (Decodificador ou Micro-op Cache) e aplica o protocolo de fusão (MOVPRFX) para maximizar o throughput de micro-ops para o backend do pipeline.
# 3: Cache ARM - L1/L2/L3 e DynamicIQ S
Itens Técnicos Encontrados: 12
**Conceitos-Chave:** Protocolo ACE, MOESI, Linha de Cache, DynamIQ Shared Unit (DSU), AMBA CHI, Snoop Control, Particionamento de Cache, Tempo Médio de Acesso (TMA)
nico: Cache ARM e DynamiQ
1. Protocolo de Coerência de Cache (ACE/MOESI)
Protocolo de coerência de cache utilizado na arquitetura ARM, especialmente com as **AMBA Coherency Extensions (A**C**)**, é feito em um modelo de **cinco estados** (semelhante ao MOESI - Modified, Owned, Exclusive, Shared, Invalid). Este protocolo controla o estado de cada linha de cache (cache line) para garantir a consistência dos dados em um sistema multi-core.
<table>
<tr>
<th>Estado</th>
<th>Abreviação</th>
<th>Descrição Técnica (Estrutura e Protocolo)</th>
</tr>
<tr>
<td><strong>Modified</strong></td>
<td>M</td>
<td>A linha de cache é <strong>suja</strong> (dirty) e <strong>exclusiva</strong> a este cache. O dado é diferente da memória principal. O cache deve responder a qualquer solicitação de leitura ou escrita de outros mestres e é o único responsável por escrever o dado de volta na memória principal (write-back).</td>
</tr>
<tr>
<td><strong>Owned</strong></td>
<td>O</td>
<td>A linha de cache é <strong>suja</strong> (dirty) e <strong>compartilhada</strong>. O dado é diferente da memória principal, mas pode ser fornecido a outros caches (snoopers) sem precisar ser escrito de volta na memória principal. Este cache é o “dono” e é o único responsável pelo write-back final.</td>
</tr>
<tr>
<td><strong>Exclusive</strong></td>
<td>E</td>
<td>A linha de cache é <strong>limpa</strong> (clean) e <strong>exclusiva</strong> a este cache. O dado é idêntico à memória principal. Uma escrita local pode mover o estado para Modified sem a necessidade de notificar outros mestres.</td>
</tr>
<tr>
<td><strong>Shared</strong></td>
<td>S</td>
<td>A linha de cache é <strong>limpa</strong> (clean) e pode estar presente em <strong>múltiplos caches</strong>. O dado é idêntico à memória principal. Uma escrita local requer uma transação de invalidação (snoop) para remover as cópias dos outros caches.</td>
</tr>
<tr>
<td><strong>Invalid</strong></td>
<td>I</td>
<td>A linha de cache <strong>não contém dados válidos</strong>.</td>
</tr>
</table>
2. Estrutura da Linha de Cache (Hardware)
- **Tamanho da Linha (Estrutura):** Tipicamente 64 bytes na arquitetura ARM moderna (embora configurável).
- **Componentes (Estrutura de Hardware):**
    - **Bloco de Dados (Data Block):** Contém os dados reais da memória principal.
    - **Tag:** Contém os bits de endereço da memória principal que identificam o bloco de dados armazenado.
    - **Bits de Estado (State Bits):** Armazenam o estado de coerência (M, O, E, S, I) e outros bits de controle (e.g., Valid Bit, Dirty Bit).
    - **Índice (Index):** Os bits do endereço que determinam onde o bloco de dados é armazenado dentro do cache (conjunto/set).
3. DynamIQ Shared Unit (DSU) e Cache L3
A **DynamIQ Shared Unit (DSU)** é a estrutura de hardware que gerencia o cluster de núcleos e a memória cache incluindo o cache L3.
Estrutura de Hardware da DSU
*   **Cache L3 Compartilhado:** Um cache unificado (unified) que armazena tanto instruções quanto dados, compartilhado por todos os núcleos no cluster DynamIQ.
*   **Snoop Control Unit (SCU):** A unidade de controle que monitora as transações de cache dos núcleos (snooping) e implementa o protocolo de coerência (ACE/CHI) dentro do cluster.
*   **Interface AMBA 5 CHI (Coherent Hub Interface):** O protocolo de interconexão usado pela DSU para se conectar a outros clusters de núcleos ou à memória principal de forma coerente. O CHI é um protocolo baseado em pacotes (packet-based) que suporta um modelo de coerência mais escalável e complexo do que o AXI/ACE.
Algoritmos e Políticas de Gerenciamento de Caco
*   **Política de Alocação de Cache Dinamicamente Otimizada (Dynamically Optimized Cache Allocation Policy):** Um algoritmo interno da DSU que gerencia a alocação de linhas de cache no L3 para otimizar o desempenho e a eficiência energética, adaptando-se à carga de trabalho.
*   **Particionamento de Cache (Cache Partitioning):** Algoritmo que permite a divisão do cache L3 em partições lógicas, permitindo que o software (e.g., o sistema operacional) gerencie o isolamento de desempenho e a Qualidade de Serviço.
(QoS) para diferentes cargas de trabalho ou núcleos.

*   **Power Gating (Estrutura/Algoritmo):** A DSU inclui lógica de controle para desligar (power gate) seções do cache L3 quando não estão em uso, um mecanismo de hardware controlado por algoritmos de gerenciamento de energia.
*   **Algoritmo de Substituição (Replacement Algorithm):** Embora não explicitamente detalhado na documentação de alto nível, o cache L3 utiliza um algoritmo de substituição (e.g., LRU - Least Recently Used, ou variações pseudo-LRU) para decidir qual linha de cache descartar quando um novo bloco precisa ser alocado.
4. Fórmulas e Métricas (Estrutura)
Embora as fórmulas matemáticas exatas para os algoritmos internos de alocação e substituição não sejam publicadas em manuais de referência, as métricas estruturais de desempenho são definidas por:

*   **Latência de Acesso (L):** O tempo necessário para acessar o dado.
*   **Taxa de Acerto (Hit Rate - H):** A proporção de acessos que encontram o dado no cache. $H = \frac{\text{Número de Acertos}}{\text{Número Total de Acessos}}$
*   **Tempo Médio de Acesso (TMA):** O tempo médio de acesso à memória, que é uma função da latência e da taxa de acerto. $TMA = L_{cache} + (1-H) \times L_{miss}$ onde $L_{cache}$ é a latência do cache, $H$ é a taxa de acerto e $L_{miss}$ é a penalidade de falha (miss penalty), que inclui o tempo para buscar o dado no próximo nível da hierarquia de memória.
*   **Tamanho do Cache (S):** O tamanho total do cache em bytes, que é uma função do número de conjuntos ($N_{sets}$), o número de vias ($N_{ways}$) e o tamanho da linha ($S_{line}$). $S = N_{sets} \times N_{ways} \times S_{line}$
**Referências:** [1]: AMBA® AXI™ and ACE™ Protocol Specification (IHI 0022E) [2]: Arm® DynamIQ™ Shared Unit Technical Manual (100453_0401_03_en) [3]: AMBA 5 CHI Architecture Specification
**Itens Técnicos Encontrados:** 388
**Conceitos-Chave:** ACE, CHI, Protocolo de Coerência, Estados de Cache (MESI/MOESI variantes), Transações de Filter, AXI Coherency Extensions, Coherent Hub Interface, ARSNOOP, CRRESP, Cache Line States (UC, UD, SC, SD)
# Conteúdo Técnico: Coerência de Cache ARM (ACE, CHI e Snoop Filter)
O conteúdo técnico a seguir foca exclusivamente nos protocolos, estruturas de hardware, sinais e estados de coerência definidos pelas especificações **ACE (AXI Coherency Extensions)**, **CHI (Coherent Hub Interface)** e o mecanismo de **Snoop Filter** no contexto da arquitetura ARM.
1. ACE (AXI Coherency Extensions) - Protocolo e Estrutura
O ACE estende o protocolo AXI4 para incluir coerência de cache em todo o sistema.
1.1. Sinais de Coerência Adicionais (Estruturas de Hardware)

O ACE introduz sinais específicos nos canais AXI para gerenciar a coerência e as transações de snoop:
| Canal | Sinal | Largura (bits) | Descrição Técnica |
|---|---|---|---|
| **Read Address (AR)** | ARSNOOP | [3:0] | Indica o tipo de transação para leituras Shareable. |
|  | ARDOMAIN | [1:0] | Indica o domínio de compartilhamento da transação de leitura. |
|  | ARBAR | [1:0] | Indica uma transação de barreira de leitura. |
| **Write Address (AW)** | AWSNOOP | [2:0] | Indica o tipo de transação para escritas Shareable. |
|  | AWDOMAIN | [1:0] | Indica o domínio de compartilhamento da transação de escrita. |
|  | AWBAR | [1:0] | Indica uma transação de barreira de escrita. |
|  | AWUNIQUE | [0] | Indica que uma linha pode ser mantida em estado Unique (para WriteEvict ). |
| **Read Data** | RRESP | [3:2] | Bits de resposta adicionais que fornecem informações para completar uma transação de leitura Shareable (inclui o estado de coerência final). |
| **Snoop Address (AC)** | ACADDR | [ac-1:0] | Endereço da transação de snoop. |
|  | ACSNOOP | [3:0] | Tipo de transação de snoop. |
| **Snoop Response (CR)** | CRRESP | [4:0] | Resposta de snoop, indicando o resultado da transação e o estado da linha de cache. |
| **Acknowledge** | RACK | [0] | Read Acknowledge: Mestre completou a transação de leitura. |
|  | WACK | [0] | Write Acknowledge: Mestre completou a transação de escrita. |
1.2. Protocolos de Transação ACE
<table>
<tr>
<th>Grupo de Transação</th>
<th>Transações Específicas</th>
<th>Propósito Principal</th>
</tr>
<tr>
<td><strong>Read</strong></td>
<td><code>ReadNoSnoop</code>, <code>ReadOnce</code>, <code>ReadClean</code>, <code>ReadNotSharedDirty</code>,<br/>  <code>ReadShared</code>, <code>ReadUnique</code></td>
<td>Obter dados, potencialmente alterando o estado de<br/>coerência para Shared ou Unique.</td>
</tr>
<tr>
<td><strong>Clean</strong></td>
<td><code>CleanUnique</code>, <code>CleanShared</code>, <code>CleanInvalid</code></td>
<td>Limpar (write-back) ou invalidar cópias de cache sem<br/>obter dados.</td>
</tr>
<tr>
<td><strong>Make</strong></td>
<td><code>MakeUnique</code>, <code>MakeInvalid</code></td>
<td>Alterar o estado de coerência para Unique ou Invalid.</td>
</tr>
<tr>
<td><strong>Write</strong></td>
<td><code>WriteNoSnoop</code>, <code>WriteUnique</code>, <code>WriteLineUnique</code>,<br/>  <code>WriteBack</code>, <code>WriteClean</code>, <code>WriteEvict</code></td>
<td>Escrever dados, potencialmente com alteração de<br/>estado e write-back.</td>
</tr>
<tr>
<td><strong>Evict</strong></td>
<td><code>Evict</code></td>
<td>Sinalizar a remoção de uma linha de cache.</td>
</tr>
</table>
1.3. Protocolo de Snoop ACE (Comportamento Físico)
O protocolo define o comportamento de um cache snooped em resposta a uma transação de snoop, focando na transferência de dados e no estado final da linha de cache:
<table>
<tr>
<th>Transação de Snoop</th>
<th>Deve Transferir Dados se Dirty</th>
<th>Estado Final Requerido</th>
</tr>
<tr>
<td>ReadOnce</td>
<td>Sim</td>
<td>-</td>
</tr>
<tr>
<td>ReadClean</td>
<td>Sim</td>
<td>Shared ou Invalid</td>
</tr>
<tr>
<td>ReadNotSharedDirty</td>
<td>Sim</td>
<td>Shared ou Invalid</td>
</tr>
<tr>
<td>ReadShared</td>
<td>Sim</td>
<td>Shared ou Invalid</td>
</tr>
<tr>
<td>ReadUnique</td>
<td>Sim</td>
<td>Invalid</td>
</tr>
<tr>
<td>CleanInvalid</td>
<td>Sim</td>
<td>Invalid</td>
</tr>
<tr>
<td>MakeInvalid</td>
<td>Não</td>
<td>Invalid</td>
</tr>
<tr>
<td>CleanShared</td>
<td>Sim</td>
<td>Clean ou Invalid</td>
</tr>
</table>
I (Coherent Hub Interface) - Estados e
O CHI (AMBA 5) é um protocolo de interconexão escalável e independente de topologia que define um conjunto mais rico de estados de coerência.
2.1. Estados de Linha de Cache CHI (Estruturas)
O CHI utiliza um modelo de coerência que é uma variação do protocolo MOESI (Modified, Owned, Exclusive, Shared, Invalid), com estados adicionais para otimização:
<table>
<tr>
<th>Estado</th>
<th>Descrição Técnica</th>
<th>Propriedades Chave</th>
</tr>
<tr>
<td><strong>I</strong></td>
<td>Invalid</td>
<td>Linha não presente.</td>
</tr>
<tr>
<td><strong>UC</strong></td>
<td>Unique Clean</td>
<td>Cópia única, limpa (não modificada em relação à memória). Pode ser modificada sem notificar outros caches.</td>
</tr>
<tr>
<td><strong>UCE</strong></td>
<td>Unique Clean Empty</td>
<td>Cópia única, limpa, mas sem bytes de dados válidos. Usado para obter permissão de escrita.</td>
</tr>
<tr>
<td><strong>UD</strong></td>
<td>Unique Dirty</td>
<td>Cópia única, suja (modificada). Deve ser escrita de volta na memória (write-back) na remoção.</td>
</tr>
<tr>
<td><strong>UDP</strong></td>
<td>Unique Dirty Partial</td>
<td>Cópia única, parcialmente suja. Deve ser mesclada com dados do próximo nível de cache/memória na remoção.</td>
</tr>
<tr>
<td><strong>SC</strong></td>
<td>Shared Clean</td>
<td>Cópias compartilhadas podem existir. Limpa. Não é responsável pelo write-back.</td>
</tr>
<tr>
<td><strong>SD</strong></td>
<td>Shared Dirty</td>
<td>Cópias compartilhadas podem existir. Suja. Deve ser escrita de volta na memória na remoção.</td>
</tr>
</table>
2.2. Protocolos de Transação CHI (Tipos de Requisições)
efine tipos de requisição que se traduzem em transações co-
<table>
<tr>
<th>Tipo de Requisição</th>
<th>Transações Específicas (Exemplos)</th>
</tr>
<tr>
<td><strong>Read</strong></td>
<td>ReadNoSnp , ReadNoSnpSep , ReadOnce , ReadOnceCleanInvalid , ReadOnceMakeInvalid , ReadClean ,<br/>ReadNotSharedDirty , ReadShared , ReadUnique , ReadPreferUnique , MakeReadUnique</td>
</tr>
<tr>
<td><strong>Dataless</strong></td>
<td>CleanUnique , MakeUnique , CleanShared , MakeInvalid</td>
</tr>
<tr>
<td><strong>Write</strong></td>
<td>WriteNoSnp , WriteUnique , WriteLineUnique , WriteBack , WriteClean , WriteEvict</td>
</tr>
<tr>
<td><strong>Atomic</strong></td>
<td>(Operações atômicas como AtomicStore , AtomicLoad , AtomicSwap )</td>
</tr>
<tr>
<td><strong>Other</strong></td>
<td>(Requisições de manutenção DVM e outras)</td>
</tr>
</table>
3. Snoop Filter (Estrutura e Algoritmo)
ura de hardware opcional que atua como um diretório p
duzindo o tráfego de snoop.
3.1. Estrutura de Hardware e Algoritmo de Rastreamento
*   **Estrutura:** Tipicamente, o Snoop Filter replica a estrutura do cache que ele está filtrando (associatividade, tamanho das tags, número total de linhas rastreadas).
*   **Mecanismo de Rastreamento (Algoritmo):** O filtro monitora as transações emitidas pelo mestre para determinar o estado de alocação de uma linha de cache.
    *   **Alocação:** Transações como ReadClean, ReadShared, ReadUnique, CleanUnique, MakeUnique indicam que a linha deve ser Alocada no filtro.
    *   **Evicção:** Transações como CleanInvalid, MakeInvalid, WriteBack, WriteEvict, Evict indicam que a linha deve ser Removida (Evicted) do filtro.
*   **Prevenção de Overflow:** Para evitar que o rastreamento exceda sua capacidade, o filtro tem permissão para emitir transações de snoop, como CleanUnique, para forçar a remoção de linhas de cache do cache associado, liberando espaço no diretório do filtro.
*   **Requisito de Precisão:** O mestre deve fornecer uma resposta IsShared precisa para que o filtro possa determinar se uma linha de cache permanece alocada após um snoop.
| Transação do Mestre | Estado de Alocação Esperado no Snoop Filter |
|---|---|
| ReadUnique | Alocado |
| CleanInvalid | Removido (Evicted) |
| WriteBack | Removido (Evicted) |
| Evict | Removido (Evicted) |
| WriteUnique | Não Altera |

[1] AMBA AXI and ACE Protocol Specification AXI3, AXI4, and AXI4-Lite ACE and ACE-Lite [2] AMBA 5 CHI Architecture Specification
# Conceito 15: MMU ARM - Translation tables, 4KB/16KB/64KB pages, ASID, TTBR
**Itens Técnicos Encontrados: 8**
**Conceitos-Chave:** TTBR0_EL1, ASID, Translation Granules, 4KB/16KB/64KB Pages, Long-descriptor format, Table W
Physical Address Formula
**MMU ARM - Translation tables, 4KB/16KB/64KB pages, ASID, TTBR**
1. Estrutura de Hardware: Registrador TTBR0_EL1 (Translation Table Base Register 0, EL1)
<table>
<tr>
<th colspan="3">O registrador TTBR0_EL1 é uma estrutura de hardware de 64 bits para a tradução de endereços de Estágio 1.</th>
</tr>
<tr>
<th>Campo</th>
<th>Bits</th>
<th>Descrição Técnica (Estrutura)</th>
</tr>
<tr>
<td><strong>ASID</strong></td>
<td>[63:48]</td>
<td><strong>Address Space ID</strong>. Identificador de 16 bits para o espaço de endereçamento. Usado para <em>tagging</em> de entradas de TLB.</td>
</tr>
<tr>
<td><strong>BADDR</strong></td>
<td>[47:1]</td>
<td><strong>Translation Table Base Address</strong>. Endereço físico base da tabela de tradução de nível mais alto.</td>
</tr>
<tr>
<td><strong>CnP</strong></td>
<td>[0]</td>
<td><strong>Common not Private</strong>. Bit de controle para compartilhamento seletivo de entradas de TLB.</td>
</tr>
</table>
2. Estrutura: Tamanhos de Granulação de Tradução (Translation Granules)
A arquitetura AArch64 suporta os seguintes tamanhos de granulação (tamanho de página no nível mais baixo de tradução):

*   **4KB (4096 bytes)**
*   **16KB (16384 bytes)**
*   **64KB (65536 bytes)**
3. Estrutura: Formato do Descritor de Tabela de Tradução (Long-descriptor format)
# Estrutura de Atributos de Memória (Page/Block Descriptor)

| Campo | Bits | Descrição Técnica (Estrutura) |
|---|---|---|
| **Type** | [1:0] | Tipo de descritor: 0b11 (Page/Block), 0b01 (Table). |
| **AF** | [10] | Access Flag. Bit de acesso. |
| **SH** | [11:12] | Shareability. Política de compartilhamento (Non-shareable, Outer Shareable, Inner Shareable). |
| **AP** | [6:7] | Access Permissions. Permissões de acesso (Read/Write, EL0/EL1). |
| **NS** | [5] | Non-Secure. Bit de segurança. |
| **Contiguous** | [52] | Contiguous Hint. Bit de otimização para o TLB. |
| **UXN/PXN** | [54/53] | Unprivileged/Privileged Execute Never. Bits de controle de execução. |
| **AttrIdx** | [2:4] | Attribute Index. Índice para o registrador MAIR_EL1 (Memory Attribute Indirection Register). |
| **Output Address** | [47:N] | Endereço físico de destino (Block/Page) ou endereço da próxima tabela (Table). |
adução de Endereç
**Algoritmo 1: Pseudocódigo Simplificado da Tradução de Estágio 1 (AArch64.FirstStageTranslate)**
mermaid
addressDescriptor AArch64.FirstStageTranslate(bits(64) vaddress, AccType acctype, boolean iswrite, boolean wasalign, integer size)
    // ... (código de verificação de habilitação) ...
    if s1_enabled then
        S1 = AArch64.TranslationTableWalk(ipaddress, vaddress, acctype, iswrite, secondstage, s2fs1walk, size);
        permissioncheck = TRUE;
    else
        S1 = AArch64.TranslateAddressS10ff(vaddress, acctype, iswrite);
        permissioncheck = FALSE;
    // ... (código de verificação de falhas e permissões) ...
    return S1.addrdesc;
Simplificado do Caminhamento da Tabela (AArco)
// Processo iterativo que usa partes do endereço virtual (VA) como índices para buscar descritores.
// 1. Determina o registrador TTBR a ser usado (TTBR0_ELx ou TTBR1_ELx).
// 2. Inicializa base_address com o valor BADDR do TTBR.
// 3. Itera pelos níveis da tabela (L0, L1, L2, L3):
//    a. Calcula o índice (index) para o nível atual usando bits específicos do VA.
//    b. Calcula o endereço do descriptor (descriptor_address) = base_address + (index * 8).
//    c. Lê o descriptor (descriptor) de 64 bits da memória.
//    d. Analisa o bit [1:0] do descriptor:
//       - Se `0b00` (Invalid): Retorna Falha de Tradução.
//       - Se `0b01` (Table): base_address é atualizado com o Output Address do descriptor. Continua para o próximo nível.
//       - Se `0b1x` (Block/Page): O descriptor é final. Combina Output Address com VA para formar o Endereço Físico (PA). Retorna PA e atributos.
// 4. Se o loop terminar sem descriptor Block/Page, retorna Falha de Tradução.
5. Fórmulas de Endereçamento
**Fórmula 1: Cálculo do Endereço Físico (PA)**
**Endereço Físico** é a concatenação do endereço base do bloco/página (Output Address) e o *offset* do endereço virtual.

$$PA = Output\ Address || VA[N - 1 : 0]$$

*N* é o número de bits de *offset* (e.g., *N* = 12 para 4KB, *N* = 14 para 16KB, *N* = 16 para 64KB).
Fórmula 2: Cálculo do Endereço do Descritor na Tabela
DescAddr$_{L}$=BaseAddr$_{L-1}$+(Index$_{L}\times8$)
Onde:
* BaseAddr<sub>L-1</sub> é o endereço base da tabela do nível anterior.
* Index<sub>L</sub> é o índice extraído do VA para o nível L.
* 8 é o tamanho em bytes de um descritor de 64 bits.
<table>
<tr>
<th>Nível</th>
<th>Bits do VA usados</th>
<th>Tamanho do índice</th>
</tr>
<tr>
<td>L0</td>
<td>[47:39]</td>
<td>9 bits</td>
</tr>
<tr>
<td>L1</td>
<td>[38:30]</td>
<td>9 bits</td>
</tr>
<tr>
<td>L2</td>
<td>[29:21]</td>
<td>9 bits</td>
</tr>
<tr>
<td>L3</td>
<td>[20:12]</td>
<td>9 bits</td>
</tr>
<tr>
<td><strong>Offset</strong></td>
<td>[11:0]</td>
<td>12 bits</td>
</tr>
</table>
Conceito 16: Memory Ordering ARM - Weak ordering model, DMB/DSB/ISE barriers, acquire/release semantics
**Itens Técnicos Encontrados:** 16
**Conceitos-Chave:** Weak Ordering Model, DMB, DSB, ISB, Load-Acquire, Store-Release, RCsc, RCpc, LORegions, Address Dependency, Data Dependency, Context Synchronization Event
# Memory Ordering ARM - Conteúdo Técnico
A arquitetura Armv8-A implementa uma arquitetura de memória de **ordenação fraca** (*weakly-ordered*). Isso permite que acessos à memória que não impõem dependências sejam emitidos, observados e concluídos em uma ordem diferente da ordem especificada pelo programa.

O reordenamento de memória é permitido para acessos a locais marcados como **Normal**, **Device-nGRE** ou **DeviceGRE**.

**Restrições de Reordenação (Dependências):**

*   **Dependência de Endereço (Address Dependency):** Se uma carga ou armazenamento usa o resultado de uma carga anterior como endereço, a ordem deve ser mantida.
    *   Exemplo:
LDR X0, [X1]
STR X2, [X0]
0 resultado de LDR X0, [X1] é o endereço para STR X2, [X0]
* **Dependência de Dados (Data Dependency):** Acessos aos mesmos bytes devem manter a ordem (o processador detecta o risco *read-after-write*).
* **Dependência de Controle (Control Dependency):** Não garante ordenação.
    * Exemplo:
LDR X0, [X1]
CBZ X0, somewhere_else
LDR X2, [X5] ; LDR X2, [X5] pode ser reordenado antes de LDR X0, [X1]
A instrução DMB impede o reordenamento de acessos de dados explícitos especificados através da barreira
* Todos os acessos de dados explícitos (carga ou armazenamento) executados antes do DMB no programa são observados por todos os **Observers** dentro de um domínio de **Shareability** especificado *antes* dos acessos de dados após o DMB no programa.
* A instrução DMB recebe um argumento que denota:
    1. Quais tipos de acessos explícitos são ordenados (carga, armazenamento ou ambos).
    2. Para quais **Observers** no domínio de **Shareability** especificado a ordenação é imposta.
* **Efeito:** Cria uma ordem entre acessos, descrita como *Barrier-ordered-before*.
* **Cache Maintenance:** Operações de manutenção de cache de dados são consideradas acessos de dados explícitos e estão sujeitas às restrições de ordenação impostas pelo DMB.
* **Não-Bloqueante:** O DMB não garante *quando* os acessos ocorrem, apenas que, *quando* ocorrerem, as restrições de ordenação se aplicam. Permite que o PE (Processing Element) continue a execução enquanto os dados explícitos aguardam a conclusão.
* **Especulação:** Não impede a execução especulativa de leituras futuras. Se uma leitura especulativa ocorrer, o núcleo deve descartar os dados e reexecutar a carga após todos os acessos de dados anteriores serem observados.

**xemplo de Uso (Estrutura):**
STR #1, [X1]
DMB
STR #1, [X3] ; Se X3 for observado atualizado, X1 DEVE ser observado atualizado.
Barreira de Sincronização de Dados (DSB - Data Synchronization Barrier)
os antes da conclusão da instrução DSB.
Protocolo/Estrutura:
* O DSB é concluído quando:
    1. Todos os acessos explícitos à memória dos tipos de acesso requeridos (especificados no argumento) que aparecem na ordem do programa antes do DSB estão **completos** para o conjunto de **Observers** no domínio de **Shareability** requerido.
    2. Se o argumento especificar leituras e escritas, todas as instruções de manutenção de cache e de manutenção de TLB (Translation Lookaside Buffer) emitidas pelo PE antes do DSB estão **completas** para o domínio de **Shareability** requerido.

* **Bloqueante:** Nenhuma instrução que apareça na ordem do programa após o DSB pode alterar qualquer estado do sistema ou executar qualquer parte de sua funcionalidade até que o DSB seja concluído.

* **Não-Bloqueante (Fetch/Decode):** O DSB não impede o *fetching* e o *decoding* de instruções.
Exemplo de Uso (Estrutura)
| STR X0, [X1] | ; Deve ser concluído antes que o DSB possa se aposentar (retire) |
|---|---|
| DSB |  |
| ADD X1, X2, X3 | ; NÃO deve ser executado antes que o primeiro STR seja concluído. |
| STR X4, [X5] | ; NÃO deve ser executado até que o primeiro STR seja concluído. |
A instrução ISB é um evento de **Sincronização de Contexto** (*Context synchronization event*).
* O contexto do PE (Processing Element) é definido como o estado dos caches, TLBs (Translation Lookaside Buffers) e System registers.
* O **ISB** garante que todas as instruções que vêm *depois* dele na ordem do programa sejam buscadas (*fetched*) do cache de instruções ou da memória *somente após* o ISB ter sido concluído.
* **Efeito:** Limpa o *pipeline* de instrução do PE, garantindo que as instruções subsequentes vejam o novo estado do sistema (contexto) que pode ter sido alterado por instruções anteriores (ex: escrita em System registers, manutenção de cache/TLB)
* **Context synchronization event garante que:**
    * Todas as interrupções não mascaradas pendentes no momento do evento são tomadas antes da primeira instrução após o evento.
    * Nenhuma instrução após o evento pode executar qualquer parte de sua funcionalidade até que o evento tenha ocorrido.
    * Todas as escritas em System registers feitas antes do evento afetam qualquer instrução após o evento.
    * Todas as alterações concluídas nas tabelas de tradução afetam todas as buscas de instrução após o evento.
nplo de Uso (Estrutura):
<table>
<tr><td>MRS</td><td>X1, CPACR_EL1</td><td></td></tr>
<tr><td>ORR</td><td>X1, X1, #(0x3 &lt;&lt; 20)</td><td>; Escreve em System register (CPACR_EL1)</td></tr>
<tr><td>MSR</td><td>CPACR_EL1, X1</td><td></td></tr>
<tr><td>ISB</td><td></td><td>; Garante que a instrução FADD veja o novo contexto</td></tr>
<tr><td>FADD</td><td>S0, S1, S2</td><td>; Instrução que depende do novo contexto</td></tr>
</table>
Semântica Load-Acquire e Store-Release
Estrutura/Protocolo:
*   **Load-Acquire (LDAR):**
    *   **Semântica:** Todas as instruções de acesso explícito à memória após o LDAR são observadas após o LDAR.
    *   **Efeito:** Impede que as cargas e armazenamentos que vêm depois do LDAR sejam reordenados para antes dele.
    *   **Instruções:** LDAR, LDAXR (Exclusive).
*   **Store-Release (STLR):**
    *   **Semântica:** Todas as instruções de acesso explícito à memória antes do STLR são observadas antes do STLR.
    *   **Efeito:** Impede que as cargas e armazenamentos que vêm antes do STLR sejam reordenados para depois dele.
    *   **Instruções:** STLR, STLXR (Exclusive).
*   **RCsc (Sequentially Consistent):** Quando um Load-Acquire aparece na ordem do programa após um Store-Release, o acesso à memória gerado pelo Store-Release é observado antes do acesso à memória gerado pelo Load-Acquire.
*   **Load-AcquirePC (Armv8.3-A):** Suporta o modelo de **Consistência de Liberação Processador Consistente (RCpc)**, que é mais fraco que o RCsc. A exigência de que Load-Acquire sejam observados em ordem com Store-Release precedentes é abandonada.
*   **Limited Ordering Regions (LORegions - Armv8.1-A):** Permite que LDLAR e STLLR forneçam ordem apenas para uma região especificada do mapa de Endereço Físico (PA), evitando penalidades de desempenho em sistemas grandes.
    *   **Registros de Hardware (System registers):** LORSA_EL1 (Start Address), LOREA_EL1 (End Address), LORN_EL1 (LORegion Number), LORC_EL1 (Valid bit).
Exemplo de Uso (Estrutura):
STR #1, [X1]
STLR #1, [X3] ; Se X3 for observado atualizado, X1 DEVE ser observado atualizado.

**Load-Acquire e Store-Release Pares (Seção Crítica):**

* Usados para proteger uma seção crítica de código.
* Garante que acessos *dentro* da seção crítica não sejam reordenados para *fora* dela.
* Acessos *dentro* da seção crítica podem ser reordenados entre si.
; Código antes da seção crítica
STLR [Xn], Xm ; Store-Release
; Seção crítica
LDAR Xm, [Xn] ; Load-Acquire
; Código após a seção crítica
Conceito 17: Prefetching ARM (Hardware stride prefetcher, stream detection, PLD/PLDW/PLI instructions)
**Tens Técnicos Encontrados:**
**Conceitos-Chave:** PLD, PLDW, PLI, Hardware Stride Prefetcher, Adaptive Stream Detection, Stream Length Histogram, Adaptive Scheduling
# Conteúdo Técnico - Prefetching ARM
trutções PLD, PLDW e PLI (Preload Dat
As instruções PLD, PLDW e PLI são **instruções de dica (hint instructions)** que sinalizam ao sistema de memória que um dado ou instrução em um endereço específico será provavelmente carregado em um futuro próximo. A implementação dessas instruções é **opcional** no hardware ARM; se não forem implementadas, elas são executadas como NOPs (No Operation).
# 1.1. Sintaxe e Formato de Instrução

A sintaxe geral é:
<table>
<tr><td><code>PLtype[cond]</code> [Rn {, #offset}]</td></tr>
<tr><td><code>PLtype[cond]</code> [Rn, +/-Rm {, shift}]</td></tr>
<tr><td><code>PLtype[cond]</code> label</td></tr>
</table>
Onde:
*   **type**:
    *   D: Preload de **Dados** (PLD).
    *   DW: Preload de **Dados com intenção de Escrita** (PLDW).
    *   I: Preload de **Instrução** (PLI).
*   **cond**: Código de condição opcional (permitido apenas em código Thumb, usando uma instrução IT precedente). É incondicional em código ARM.
*   **Rn**: Registrador base para o endereço de memória.
*   **offset**: Deslocamento imediato.
*   **Range (ARM):** -4095 a +4095.
*   **Range (Thumb, Rn != PC):** -255 a +4095.
*   **Range (Thumb, Rn = PC):** -4095 a +4095.

*   **Rm:** Registrador contendo um valor a ser usado como deslocamento.

*   **shift:** Deslocamento opcional aplicado a Rm .
    *   **Range (Thumb):** LSL #0 a #3.
    *   **Range (ARM):** LSL #0 a #31, LSR #1 a #32, ASR #1 a #32, ROR #1 a #31, RRX.
1.2. Estruturas e Protocolos
*   **Protocolo de Sinalização**: A instrução sinaliza ao sistema de memória (controlador de cache, controlador de memória) a intenção de acesso futuro.
*   **Alinhamento**: Nenhuma verificação de alinhamento é realizada para as instruções de preload.
*   **Disponibilidade Arquitetural**:
    *   PLD : ARMv5TE e superior.
    *   PLDW : ARMv7 e superior que implementam as **Multiprocessing Extensions** (indica intenção de escrita, útil para coerência de cache).
    *   PLI : ARMv7 e superior.
2. Hardware Stride Prefetcher e Adaptive Stream Detection (ASD)
2.1. Hardware Stride Prefetcher (Prefetcher de Passo de Hardware)
*   **Algoritmo/Estrutura:** Detecta padrões de acesso à memória com um passo (stride) constante.
*   **Mecanismo:** Monitora os endereços de acesso à memória. Se uma sequência de acessos $A_1, A_2, A_3, \ldots$ for observada, e o passo $\Delta = A_{i+1} - A_i$ for constante, o prefetcher prevê o próximo endereço $A_{i+1} + \Delta$ e o pré-carrega.
*   **Limitação:** Ineficaz para acessos irregulares ou indiretos, onde o passo não é constante.
2.2. Adaptive Stream Detection (ASD)
O ASD é uma técnica para modular a agressividade de um prefetcher de fluxo (stream prefetcher) com base na localidade espacial observada da carga de trabalho.
* **Estrutura Principal: Stream Length Histogram (SLH).**
    * O SLH é um histograma dinamicamente calculado que atribui a cada acesso de memória a um comprimento de fluxo (stream length) particular.
    * A altura da barra na localização m representa o número de comandos de Leitura que fizeram parte de um fluxo de comprimento m.

* **Algoritmo de Decisão (Simplificado):**
    1. O prefetcher detecta o comprimento de fluxo L<sub>current</sub> da requisição de Leitura atual R<sub>n</sub>.
    2. O prefetcher consulta o **SLH** para determinar a probabilidade de que a requisição R<sub>n</sub> seja parte de um fluxo de comprimento L<sub>current</sub> ou maior.
    3. **Regra de Prefetching:** Um pedido de prefetch deve ser emitido para o próximo endereço de cache se a probabilidade de que o fluxo atual seja de um comprimento L<sub>current</sub> ≥ k for maior do que um limite de agressividade T (onde k é o comprimento mínimo de fluxo para prefetch, e T é o limite de probabilidade).

* **Adaptive Scheduling:** O ASD usa um buffer de prefetch (Small Prefetch Buffer) e um mecanismo de **Adaptive Scheduling** para modular a prioridade relativa dos comandos de prefetch em relação aos comandos de leitura regulares.
    * O Adaptive Scheduling usa feedback do sistema de memória para selecionar entre diferentes políticas de priorização, desde a mais conservadora (equivalente à política de priorização SRP) até a mais agressiva.
**Fórmula (Conceitual):** $Prefetch \iff P(\text{Stream Length} \geq L_{current} | R_n) > T\text{OndeP}(\text{Stream Length} \geq L_{current} | R_n)$ é a probabilidade calculada a partir do SLH.

**Estrutura de Hardware (Conceitual):** O ASD reside no controlador de memória e utiliza o SLH (uma tabela de contado) e o Adaptive Scheduling (lógica de priorização) para tomar decisões de prefetch.
**Observação:** O artigo sobre ASD não é específico da arquitetura ARM, mas descreve um mecanismo de prefetching avançado que pode ser implementado em qualquer controlador de memória, incluindo os da ARM. O pedido do usuário era por “Hardware stride prefetcher, stream detection... no contexto da arquitetura ARM”, e o ASD é um exemplo de detecção de fluxo que a ARM e outros fabricantes podem usar.
Conceito 18: TrustZone - Secure/Non-secure worlds, Secure Monitor, SMC instruction, TZASC
**Itens Técnicos Encontrados:** 233
**Conceitos-Chave:** Secure State, Non-secure State, EL3, Secure Monitor, SMC Calling Convention, SMC32, SMC64, T2, region_attributes, Algoritmo de Controle de Acesso
# Conteúdo Técnico: ARM TrustZone, Secure Monitor, SMC e TZASC
tura de Estados e Níveis de Exceção (TNE)
A arquitetura ARM com TrustZone define dois mundos de execução isolados e níveis de exceção específicos para segurança:

*   **Secure State:** Estado de execução que permite acesso a todos os recursos do sistema, incluindo memória, periféricos e registradores do sistema marcados como Secure.
*   **Non-secure State:** Estado de execução que restringe o acesso apenas aos recursos do sistema marcados como Non-secure.
*   **EL3 (Secure Monitor Exception Level):** Nível de exceção mais privilegiado, dedicado à execução do **Secure Monitor**. É o ponto de transição de hardware entre os estados Secure e Non-secure. O EL3 está sempre no Secure State.
Protocolo de Chamada do Monitor Seguro (SMC Calling Convention)
A instrução **SMC** (Secure Monitor Call) é uma instrução assembler que gera uma exceção síncrona tratada pelo Secure Monitor (em EL3). O protocolo define a passagem de parâmetros e o formato da instrução.

**Tipos de Chamadas:**

1.  **Fast Calls:** Para operações Secure atômicas.
2.  **Standard Calls:** Para iniciar operações Secure pré-emptíveis.

**Convenções de Chamada:**

*   **SMC32:** Interface de 32 bits, suporta até seis argumentos de 32 bits.
*   **SMC64:** Interface de 64 bits, suporta até seis argumentos de 64 bits.

**Formato de Instrução e Passagem de Argumentos (Protocolo):**
<table>
<tr>
<th>Elemento</th>
<th>Registrador (AArch64)</th>
<th>Registrador (AArch32)</th>
<th>Descrição Técnica</th>
</tr>
<tr>
<td><strong>Function ID</strong></td>
<td>X<sub>0</sub> (64-bit) ou W<sub>0</sub> (32-bit)</td>
<td>R<sub>0</sub> (32-bit)</td>
<td>Inteiro de 32 bits que identifica a função Secure a ser invocada.</td>
</tr>
<tr>
<td><strong>Argumentos 1 a 7</strong></td>
<td>X<sub>1</sub> a X<sub>7</sub> (64-bit)</td>
<td>R<sub>1</sub> a R<sub>7</sub> (32-bit)</td>
<td>Argumentos de entrada para a função Secure.</td>
</tr>
<tr>
<td><strong>Valores de Retorno</strong></td>
<td>X<sub>0</sub> a X<sub>7</sub> (64-bit)</td>
<td>R<sub>0</sub> a R<sub>7</sub> (32-bit)</td>
<td>Registradores usados para retornar o código de status (X<sub>0</sub> / R<sub>0</sub>) e valores adicionais.</td>
</tr>
</table>
ware: TrustZone Address Space Control
O **TZASC** (TrustZone Address Space Controller) é um componente de hardware (ex: TZC-380) que impõe o controle de acesso à memória física (DRAM) com base no nível de segurança (Secure/Non-secure) do mestre que inicia a transação (CPU, DMA, periféricos).
Estrutura de Particionamento:
* O TZASC suporta até **16 regiões** de endereço independentes (Região 0 a Região 15).
* Cada região é configurada por um conjunto de registradores que definem seu endereço base, tamanho e atributos de segurança.
**Registradores de Configuração de Região (TZC-380):**
<table>
<tr>
<th>Registrador</th>
<th>Offset</th>
<th>Largura (bits)</th>
<th>Função Técnica</th>
</tr>
<tr>
<td><code>region_setup_low_<n></n></code></td>
<td>0x100 + (n * 0x10)</td>
<td>32</td>
<td>Define o endereço base da região n (bits [31:12]).</td>
</tr>
<tr>
<td><code>region_setup_high_<n></n></code></td>
<td>0x104 + (n * 0x10)</td>
<td>32</td>
<td>Define o endereço base da região n (bits [63:32]).</td>
</tr>
<tr>
<td><code>region_attributes_<n></n></code></td>
<td>0x108 + (n * 0x10)</td>
<td>32</td>
<td>Define os atributos de segurança e tamanho da região n .</td>
</tr>
</table>
gistrador region_attributes_<n> (Controle de Acesso):
| Bit 0 (EN): | Habilita a região. |
|---|---|
| Bits 3:1: | Define o tamanho da região (codificação binária para 4KB, 64KB, 1MB, etc.). |
| Bits 15:8: | Permissões de acesso para o mundo Secure (Secure World). |
|   | S_RD : Permissão de leitura Secure. |
|   | S_WR : Permissão de escrita Secure. |
| Bits 23:16: | Permissões de acesso para o mundo Non-secure (Non-secure World). |
|   | N_RD : Permissão de leitura Non-secure. |
|   | N_WR : Permissão de escrita Non-secure. |

**Algoritmo Lógico de Controle de Acesso (Fórmula Lógica):**

O acesso à memória é concedido se a solicitação de acesso do mestre for permitida pelos bits de permissão configurados para a região de endereço.

*   **Acesso Secure (S):** $Permitido = (S_RD ∧ Leitura) ∨ (S_WR ∧ Escrita)$
*   **Acesso Non-secure (NS):** $Permitido = (N_RD ∧ Leitura) ∨ (N_WR ∧ Escrita)$

Uma falha de segurança (Secure Violation) ocorre se um mestre Non-secure tentar acessar uma região onde N_ACCESS não permite a operação solicitada. Os detalhes da falha são registrados nos registradores fail_address_low, fail_address_high e fail_control.
Registradores de Falha TZC-
<table>
<tr>
<th>Registrador</th>
<th>Offset</th>
<th>Largura (bits)</th>
<th>Função Técnica</th>
</tr>
<tr>
<td><code>fail_address_low</code></td>
<td>0x020</td>
<td>32</td>
<td>Endereço baixo da transação que causou a falha.</td>
</tr>
<tr>
<td><code>fail_address_high</code></td>
<td>0x024</td>
<td>32</td>
<td>Endereço alto da transação que causou a falha.</td>
</tr>
<tr>
<td><code>fail_control</code></td>
<td>0x028</td>
<td>32</td>
<td>Contém o tipo de acesso e o ID do mestre que falhou.</td>
</tr>
</table>
**Conceito 19: Pointer Authentication - PAC codes, PACIA/PACIB, BTI branch identification, CFI**
**Itens Técnicos Encontrados:** 15
Conteúdo Técnico: Pointer Authentication (PAC) e Branch Target Identification (BTI) na Arquitetura ARM
O conteúdo técnico a seguir foca exclusivamente nos algoritmos, estruturas de hardware e formatos de instrução para **Pointer Authentication Code (PAC)** e **Branch Target Identification (BTI)** na arquitetura ARM (AArch64), que são mecanismos fundamentais para a implementação de **Control-Flow Integrity (CFI)**.
# Pointer Authentication Code (PAC) - Algoritmo Qa
O PAC é um código de autenticação gerado por um algoritmo criptográfico leve, geralmente uma variante do **QARMA** (um *tweakable block cipher*), que é inserido em bits não utilizados de um ponteiro.
do Algoritmo Principal (Comunicação)
o calculo do PAC e realizado pela função ComputePACQARMA , que implementa:

**Entradas:**

*   data : 64 bits (o ponteiro estendido)
*   modifier : 64 bits (o tweak, que pode ser o SP, um registrador, ou 0)
*   key0 , key1 : 64 bits cada (partes da chave de 128 bits K )
*   isqarma3 : booleano (seleciona QARMA3 ou QARMA5)
Constantes e Estruturas:
<table>
<tr>
<th>Nome</th>
<th>Valor (Hexadecimal)</th>
<th>Descrição</th>
</tr>
<tr>
<td><strong>Alpha</strong></td>
<td>0xC0AC29B7C97C50DD</td>
<td>Constante de <em>tweak</em> usada na última rodada.</td>
</tr>
<tr>
<td rowspan="4"><strong>RC</strong> (Round Constants)</td>
<td>RC[[0]] = 0x0000000000000000</td>
<td>Constantes de rodada.</td>
</tr>
<tr>
<td>RC[[1]] = 0x13198A2E03707344</td>
<td></td>
</tr>
<tr>
<td>RC[[2]] = 0xA4093822299F31D0</td>
<td>(QARMA3 e QARMA5)</td>
</tr>
<tr>
<td>RC[[3]] = 0x082EFA98EC4E6C89</td>
<td>(Apenas QARMA5)</td>
</tr>
<tr>
<td></td>
<td>RC[[4]] = 0x452821E638D01377</td>
<td>(Apenas QARMA5)</td>
</tr>
</table>
go Simplificado da Rodada (IPR)
mermaid
graph TD
    A[func ComputePACQARMA(data, modifier, key0, key1, isqarma3) => bits(64)] --> B[begin]
    B --> C[iterations = if isqarma3 then 2 else 4;]
    C --> D[modk0 = key0[0]::key0[63:2]:::(key0[63] XOR key0[1]);]
    D --> E[runningmod = modifier;]
    E --> F[workingval = data XOR key0;]
    F --> G[// Rodadas Criptográficas (Forward)]
    G --> H[for i = 0 to iterations do]
    H --> I[roundkey = key1 XOR runningmod;]
    I --> J[workingval = workingval XOR roundkey;]
    J --> K[workingval = workingval XOR RC[[i]];]
    K --> L[if i > 0 then]
    L --> M[workingval = PACCellShuffle(workingval);]
    M --> N[workingval = PACMult(workingval);]
    N --> O[end;]
    O --> P[workingval = if isqarma3 then PACSub1(workingval) else PACSub(workingval);]
    P --> Q[runningmod = TweakShuffle(runningmod[63:0]);]
    Q --> R[end;]
    R --> S[// Rodadas Finais (Inversas)]
    S --> T[// ... (sequência de operações PACCellShuffle, PACMult, PACSub/PACInvSub, XOR com key1, PACCellInvShuffle, etc.)]
    T --> U[// ...]
    U --> V[return workingval;]
    V --> W[end];
1.2. Funções de Transformação de Bits
O algoritmo QARMA utiliza transformações de bits em 4-bit
mermaid
graph TD
    A(func PACMult(Sinput : bits(64)) => bits(64))
    B[begin]
    C[// ... (Cálculo de t0, t1, t2, t3 usando ROL e XOR)]
    D[// t0[3:0] = ROL(Sinput[(i+8)*:4], 1) XOR ROL(Sinput[(i+4)*:4], 2) XOR ROL(Sinput[i*:4], 1);]
    E[// ...]
    F[// Soutput[i*:4] = t3[3:0];]
    G[// Soutput[(i+4)*:4] = t2[3:0];]
    H[// Soutput[(i+8)*:4] = t1[3:0];]
    I[// Soutput[(i+12)*:4] = t0[3:0];]
    J[// ...]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I
    I --> J
2. **PACSub (Caixa S - S-Box):** Implementa uma substituição não linear de 4 bits (S-Box) baseada na cifra PRINCE.
<table>
<tr>
<th>Entrada (4 bits)</th>
<th>Saída PACSub (QARMA5)</th>
<th>Saída PACSub1 (QARMA3)</th>
<th>Saída PACInvSub (Inversa QARMA5)</th>
</tr>
<tr>
<td>0000</td>
<td>1011</td>
<td>1010</td>
<td>0101</td>
</tr>
<tr>
<td>0001</td>
<td>0110</td>
<td>1101</td>
<td>1110</td>
</tr>
<tr>
<td>0010</td>
<td>1000</td>
<td>1110</td>
<td>1101</td>
</tr>
<tr>
<td>0011</td>
<td>1111</td>
<td>0110</td>
<td>1000</td>
</tr>
<tr>
<td>0100</td>
<td>1100</td>
<td>1111</td>
<td>1010</td>
</tr>
<tr>
<td>0101</td>
<td>0000</td>
<td>0111</td>
<td>1011</td>
</tr>
<tr>
<td>0110</td>
<td>1001</td>
<td>0011</td>
<td>0001</td>
</tr>
<tr>
<td>0111</td>
<td>1110</td>
<td>0101</td>
<td>1001</td>
</tr>
<tr>
<td>1000</td>
<td>0011</td>
<td>1001</td>
<td>0010</td>
</tr>
<tr>
<td>1001</td>
<td>0111</td>
<td>1000</td>
<td>0110</td>
</tr>
<tr>
<td>1010</td>
<td>0100</td>
<td>0000</td>
<td>1111</td>
</tr>
<tr>
<td>1011</td>
<td>0101</td>
<td>1100</td>
<td>0000</td>
</tr>
<tr>
<td>1100</td>
<td>1101</td>
<td>1011</td>
<td>0100</td>
</tr>
<tr>
<td>1101</td>
<td>0010</td>
<td>0001</td>
<td>1100</td>
</tr>
<tr>
<td>1110</td>
<td>0001</td>
<td>0010</td>
<td>0111</td>
</tr>
<tr>
<td>1111</td>
<td>1010</td>
<td>0100</td>
<td>0011</td>
</tr>
</table>
3. PACCellShuffle (Permutação de Bits): Implementa uma permutação linear de bits (P-Layer) que mistura os nibbles.
mermaid
classDiagram
    class PACCellShuffle {
        func PACCellShuffle(indata : bits(64)) => bits(64)
        begin
            // Exemplo de mapeamento de bits (índices de 0 a 63):
            // outdata[3:0] = indata[55:52];
            // outdata[7:4] = indata[27:24];
            // outdata[11:8] = indata[47:44];
            // outdata[15:12] = indata[3:0];
            // ...
        end;
    }
2. Branch Target Identification (BTI)
uitetura ARMv8.5-A que fornece um mecanismo de CFI de ar-
2.1. Formato de Instrução BTI (AArch64)
A instrução BTI é codificada no espaço de instruções **HINT** (Hint Instruction) e atua como um NOP em processadores que suportam a extensão **FEAT_BT1**.
<table>
<tr>
<th>Bits</th>
<th>31-30</th>
<th>29-28</th>
<th>27-24</th>
<th>23-20</th>
<th>19-16</th>
<th>15-12</th>
<th>11-8</th>
<th>7-6</th>
<th>5-4</th>
<th>3-0</th>
</tr>
<tr>
<td><strong>Padrão</strong></td>
<td>11</td>
<td>01</td>
<td>0101</td>
<td>0000</td>
<td>0011</td>
<td>0010</td>
<td>0100</td>
<td>op2</td>
<td>01</td>
<td>1111</td>
</tr>
<tr>
<td><strong>Valor</strong></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
</table>
**Encoding Base (HINT):** 110101010000001100100100xx011111 (Binário)
tes da Instrução BTI (op2:2:1)
<table>
<tr>
<th><strong>op2[2:1]</strong></th>
<th><strong>Mnemônico</strong></th>
<th><strong>Descrição</strong></th>
<th><strong>Uso (CFI)</strong></th>
</tr>
<tr>
<td>00</td>
<td>BTI</td>
<td>Marca o destino como válido para qualquer salto indireto.</td>
<td>Destino de saltos indiretos genéricos.</td>
</tr>
<tr>
<td>01</td>
<td>BTI c</td>
<td>Marca o destino como válido para saltos indiretos de chamada (BLR).</td>
<td>Destino de chamadas indiretas.</td>
</tr>
<tr>
<td>10</td>
<td>BTI j</td>
<td>Marca o destino como válido para saltos indiretos de salto (BR).</td>
<td>Destino de saltos indiretos (e.g., <em>tail calls</em>).</td>
</tr>
<tr>
<td>11</td>
<td>BTI jc</td>
<td>Marca o destino como válido para saltos indiretos de chamada ou salto.</td>
<td>Destino de saltos indiretos de chamada ou salto.</td>
</tr>
</table>
2.2. Estrutura de Hardware (PSTATE.BTYPE)
canismo BTI é controlado pelo estado do processador, especificamente pelo campo **PSTATE.BTYPE** (Branch Type), que
<table>
<tr>
<th>PSTATE.BTYPE</th>
<th>Estado</th>
</tr>
<tr>
<td>0b00</td>
<td>BTI desabilitado ou estado inicial.</td>
</tr>
<tr>
<td>0b01</td>
<td>Esperando por BTI c ou BTI jc.</td>
</tr>
<tr>
<td>0b10</td>
<td>Esperando por BTI j ou BTI jc.</td>
</tr>
<tr>
<td>0b11</td>
<td>Esperando por BTI jc.</td>
</tr>
</table>
# Mecanismo de CFI:
1. Uma instrução de salto indireto (ex: BLR, BR) define o PSTATE.BTYPE para um valor diferente de 0b00 (indicando o tipo de salto esperado).

2. O processador verifica se a próxima instrução é uma instrução BTI compatível com o valor de PSTATE.BTYPE.

3. Se a instrução BTI for compatível, o PSTATE.BTYPE é redefinido para 0b00 e a execução continua.

4. Se a instrução não for BTI ou for incompatível, uma **Branch Target Exception** é gerada, interrompendo o fluxo de controle malicioso.
3. Pointer Authentication (PAC) - Instruções
Instruções PAC (PACIA, PACIB, PACDA, PACDB, etc.) utilizam o algoritmo QARMA para gerar o PAC e inseri-lo no ponteiro.

**Uso das Instruções PAC (Exemplos):**
<table>
<tr>
<th>Instrução</th>
<th>Chave Utilizada</th>
<th>Tweak (Modifier)</th>
<th>Função</th>
</tr>
<tr>
<td><strong>PACIA &lt;Xd&gt;</strong></td>
<td>Chave de Instrução A (IA)</td>
<td>Zero ( 0 )</td>
<td>Assina o endereço em &lt;Xd&gt; usando o modificador zero.</td>
</tr>
<tr>
<td><strong>PACIA &lt;Xd&gt;, &lt;Yn&gt;</strong></td>
<td>Chave de Instrução A (IA)</td>
<td>Registrador &lt;Yn&gt;</td>
<td>Assina o endereço em &lt;Xd&gt; usando o valor de &lt;Yn&gt; como modificador.</td>
</tr>
<tr>
<td><strong>PACIB &lt;Xd&gt;</strong></td>
<td>Chave de Instrução B (IB)</td>
<td>Zero ( 0 )</td>
<td>Assina o endereço em &lt;Xd&gt; usando o modificador zero.</td>
</tr>
<tr>
<td><strong>PACDB &lt;Xd&gt;, &lt;Yn&gt;</strong></td>
<td>Chave de Dados B (DB)</td>
<td>Registrador &lt;Yn&gt;</td>
<td>Assina o endereço em &lt;Xd&gt; usando o valor de &lt;Yn&gt; como modificador.</td>
</tr>
<tr>
<td><strong>AUTIA &lt;Xd&gt;</strong></td>
<td>Chave de Instrução A (IA)</td>
<td>Zero ( 0 )</td>
<td>Autentica o endereço em &lt;Xd&gt; e remove o PAC.</td>
</tr>
<tr>
<td><strong>XPAC &lt;Xd&gt;</strong></td>
<td>N/A</td>
<td>N/A</td>
<td>Remove o PAC do ponteiro sem autenticação.</td>
</tr>
</table>
**Estrutura de Hardware (Chaves):** O hardware ARMv8.3-A e superior fornece chaves de 128 bits (K) armazenadas em registradores internos, não acessíveis diretamente pelo software de aplicação:
*   **APIAKey** (Instruction Key A)
*   **APIBKey** (Instruction Key B)
*   **APDAKey** (Data Key A)
*   **APDBKey** (Data Key B)
*   **APGAKey** (Generic Key)
Conceito 20: Memory Tagging Extension (MTE)
**Itens Técnicos Encontrados: 17**
**Conceitos-Chave:** Allocation Tag, Pointer Tag, Tag Granule, Lock and Key Model, Tag Checking (Synchronous), Tag Checking (Asynchronous), LDGM/STGM, LDREX/STREX, Exclusive Monitor, A64 Instruction Format
Memory Tagging Extension (MTE) - Arquitetura ARMv8.5-A e Superior
1. Estrutura de Tags e Modelo “Lock and Key”
O MTE opera sob um modelo de segurança de memória “Lock and Key” (Cadeado e Chave). A memória é o “ponteiro é a “chave”.
1.1. Estrutura da Tag de Alocação (Allocation Ta
*   **Tamanho da Tag:** 4 bits.
*   **Granularidade da Tag (Tag Granule):** Uma tag de 4 bits é associada a cada bloco de **16 bytes** de memória física.
*   **Armazenamento da Tag de Ponteiro (Pointer Tag):** A tag é armazenada nos 4 bits mais significativos do byte endereço virtual (utilizando o recurso **Top Byte Ignore - TBI** da arquitetura ARMv8-A).
e Verificação de Tag (Tagging)
2. Formato e Operação das Instruções de Manipulação de Tag em Massa (IDGM/STGM)
<table>
<tr>
<td>31</td>
<td>30</td>
<td>29</td>
<td>28</td>
<td>27</td>
<td>26</td>
<td>25</td>
<td>24</td>
<td>23</td>
<td>22</td>
<td>21</td>
<td>20</td>
<td>19</td>
<td>18</td>
<td>17</td>
<td>16</td>
<td>15</td>
<td>14</td>
<td>13</td>
<td>12</td>
<td>11</td>
<td>10</td>
<td>9</td>
<td>8</td>
<td>7</td>
<td>6</td>
</tr>
<tr>
<td>·</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>Xn</td>
<td>Xt</td>
<td></td>
<td></td>
</tr>
</table>
*   **Xt (bits 4:0):** Registrador de propósito geral de 64 bits de destino.
*   **Xn (bits 9:5):** Registrador de propósito geral de 64 bits base ou Stack Pointer (SP)
mermaid
classDiagram
    class AArch64 {
        bits(4) MemTag[address, AccType_NORMAL]
    }
```

if PSTATE.EL == EL0 then
  UNDEFINED;

bits(64) data = Zeros(64);
bits(64) address;

// Determina o endereço base
if n == 31 then
  CheckSPAlignment();
  address = SP[];
else
  address = X[n];

// Calcula o tamanho do bloco (size) e o número de tags (count)
integer size = 4 * (2 ^ (UInt(GMID_EL1.BS)));
address = Align(address, size);
integer count = size >> LOG2_TAG_GRANULE; // LOG2_TAG_GRANULE = 4 (log2 de 16 bytes)
integer index = UInt(address<LOG2_TAG_GRANULE+3:LOG2_TAG_GRANULE>);

// Loop para carregar as tags
for i = 0 to count-1
  bits(4) tag = AArch64.MemTag[address, AccType_NORMAL]; // Lê a tag de 4 bits
  data<(index*4)+3:index*4> = tag; // Armazena a tag no registrador de destino (Xt)
  address = address + TAG_GRANULE;
  index = index + 1;

X[t] = data;
tras Instruções MTE de Manipulação de
<table>
<tr>
<th>Instrução</th>
<th>Categoria</th>
<th>Descrição Técnica</th>
</tr>
<tr>
<td><strong>IRG</strong></td>
<td>Manipulação de Tag</td>
<td>Insere uma <strong>Tag Aleatória</strong> (Random Tag) em um registrador para uso por outras instruções. Essencial para a base estatística do MTE.</td>
</tr>
<tr>
<td><strong>GMI</strong></td>
<td>Manipulação de Tag</td>
<td>Manipula o conjunto de tags excluídas (Excluded Set) para uso com IRG , permitindo que o software reserve tags para propósitos especiais.</td>
</tr>
<tr>
<td><strong>LDG</strong></td>
<td>Manipulação de Tag</td>
<td>Carrega a Tag de Alocação (Allocation Tag) de um único Granule de Memória.</td>
</tr>
<tr>
<td><strong>STG</strong></td>
<td>Manipulação de Tag</td>
<td>Armazena a Tag de Alocação em um único Granule de Memória sem modificar os dados.</td>
</tr>
<tr>
<td><strong>STZG</strong></td>
<td>Manipulação de Tag</td>
<td>Armazena a Tag de Alocação e zera o bloco de 16 bytes de dados.</td>
</tr>
<tr>
<td><strong>ST2G / STZ2G</strong></td>
<td>Manipulação de Tag</td>
<td>Alternativas mais densas que operam em dois Granules de Memória (32 bytes).</td>
</tr>
<tr>
<td><strong>ADDG / SUBG</strong></td>
<td>Aritmética de Ponteiro</td>
<td>Variantes de ADD e SUB que permitem que a tag e o endereço sejam modificados separadamente por um valor imediato. Usadas para aritmética de ponteiros na pilha.</td>
</tr>
<tr>
<td><strong>SUBP(S)</strong></td>
<td>Aritmética de Ponteiro</td>
<td>Subtração de 56 bits (opcionalmente com flags) para aritmética de ponteiro que ignora a tag no byte superior.</td>
</tr>
</table>
4. Sincronização Lock-Free e MTE
O MTE é uma extensão de segurança de memória e não altera fundamentalmente os protocolos de sincronização da arquitetura ARM.
- **Estrutura de Sincronização:** A sincronização lock-free na arquitetura ARM é implementada primariamente através do par de instruções **Load-Exclusive (LDREX)** e **Store-Exclusive (STREX)** (ou suas variantes LDAXR / STLXR para
aquisição/liberação).

*   **Protocolo:** O protocolo de LDREX / STREX usa um **Monitor Exclusivo** (Exclusive Monitor) para garantir atomicidade. Uma operação de STREX só é bem-sucedida se o monitor não tiver sido limpo desde o LDREX correspondente.
*   **Interação com MTE:** As operações atômicas (LDREX / STREX e as instruções atômicas de leitura-modificação-escrita como LDADD , CAS , etc.) operam em memória que pode ser marcada com MTE. A verificação de tag (Tag Checking) é aplicada a esses acessos de memória. O sucesso ou falha da operação atômica (determinada pelo monitor exclusivo) é ortogonal à verificação de tag (determinada pelo MTE). Uma falha de verificação de tag pode ocorrer durante uma operação atômica, dependendo do modo MTE (síncrono ou assíncrono).
*   **Conceito Chave:** O MTE introduz a necessidade de garantir que as operações atômicas, ao acessarem a memória, utilizem ponteiros com a tag correta para evitar falsos positivos ou exceções, mas o algoritmo de sincronização em si (LDREX / STREX loop) permanece o mesmo.
**Conceito 21: Virtualization ARM (EL2, Stage-2 translation, VMID, VHE)**
**Itens Técnicos Encontrados:** 12
**Conceitos-Chave:** HCR_EL2, VTTBR_EL2, Stage-2 Translation, VMID, VHE, E2H, TLBI, Access Permission Formula, Execute Never Formula
Virtualization ARM - EL2 hypervisor, Stage-2 translation, VMID, VHE Virtualization Host Extensions
1. Estruturas de Hardware e Registros de Controle
gistro HCR_EL2 (Hypervisor Configuration Regis
its) é a estrutura central para configurar o ambiente de virtu-
<table>
<tr>
<th>Campo</th>
<th>Bits</th>
<th>Descrição Técnica</th>
</tr>
<tr>
<td>VM</td>
<td>[0]</td>
<td><strong>Virtualization Enable.</strong> 1 habilita a tradução de endereço de Stage 2 para o regime de tradução EL1&amp;0.</td>
</tr>
<tr>
<td>SWIO</td>
<td>[1]</td>
<td><strong>Software-initiated wait for interrupt/event.</strong> Controla se WFI/WFE no EL1/EL0 é trapado para EL2.</td>
</tr>
<tr>
<td>PTW</td>
<td>[2]</td>
<td><strong>Propagation of Translation table Walk.</strong> Controla se o MMU de Stage 1 pode propagar falhas de tradução para o EL2.</td>
</tr>
<tr>
<td>FMO</td>
<td>[3]</td>
<td><strong>FIQ Mask Override.</strong> Permite que o Hypervisor mascare FIQs no EL1/EL0.</td>
</tr>
<tr>
<td>IMO</td>
<td>[4]</td>
<td><strong>IRQ Mask Override.</strong> Permite que o Hypervisor mascare IRQs no EL1/EL0.</td>
</tr>
<tr>
<td>AMO</td>
<td>[5]</td>
<td><strong>SError Mask Override.</strong> Permite que o Hypervisor mascare SError no EL1/EL0.</td>
</tr>
<tr>
<td>TGE</td>
<td>[7]</td>
<td><strong>Trap General Exceptions.</strong> 1 faz com que exceções do EL1/EL0 sejam tratadas no EL2. Essencial para o modelo VHE.</td>
</tr>
<tr>
<td>TIDCP</td>
<td>[13]</td>
<td><strong>Trap ID Registers for CP.</strong> Controla o trapping de acessos a registros de ID de cache e TLB.</td>
</tr>
<tr>
<td>TVM</td>
<td>[15]</td>
<td><strong>Trap Virtual Memory controls.</strong> Controla o trapping de acessos a registros de controle de memória virtual (como TTBR0_EL1, TCR_EL1, etc.).</td>
</tr>
<tr>
<td>TID0</td>
<td>[16]</td>
<td><strong>Trap ID Registers 0.</strong> Controla o trapping de acessos a registros de ID do sistema.</td>
</tr>
<tr>
<td>TID1</td>
<td>[17]</td>
<td><strong>Trap ID Registers 1.</strong> Controla o trapping de acessos a registros de ID do sistema.</td>
</tr>
<tr>
<td>TID2</td>
<td>[18]</td>
<td><strong>Trap ID Registers 2.</strong> Controla o trapping de acessos a registros de ID do sistema.</td>
</tr>
<tr>
<td>TID3</td>
<td>[19]</td>
<td><strong>Trap ID Registers 3.</strong> Controla o trapping de acessos a registros de ID do sistema.</td>
</tr>
<tr>
<td>HCD</td>
<td>[20]</td>
<td><strong>Hypervisor Call Disable.</strong> Desabilita o uso da instrução HVC (Hypervisor Call) no EL1/EL0.</td>
</tr>
<tr>
<td>RW</td>
<td>[31]</td>
<td><strong>Execution state control for lower EL.</strong> 1 indica que o EL1/EL0 está usando AArch64.</td>
</tr>
<tr>
<td>E2H</td>
<td>[34]</td>
<td><strong>EL2 Host. Virtualization Host Extensions (VHE).</strong> 1 configura o EL2 para operar como um host de virtualização, permitindo que o SO host seja executado no EL2 com o mínimo de modificações.</td>
</tr>
<tr>
<td>NV</td>
<td>[35]</td>
<td><strong>Nested Virtualization.</strong> 1 habilita o suporte para virtualização aninhada.</td>
</tr>
<tr>
<td>NV1</td>
<td>[36]</td>
<td><strong>Nested Virtualization 1.</strong> Usado em conjunto com NV para controle de virtualização aninhada.</td>
</tr>
</table>
1.2. Registro VTTBR_EL2 (Virtualization Translation Table Base Register)
2 (64 ou 128 bits) armazena o endereço base da tabela de tr
<table>
<tr>
<th>Campo</th>
<th>Bits</th>
<th>Descrição Técnica</th>
</tr>
<tr>
<td><strong>VMID</strong></td>
<td>[63:48] ou<br/>[15:0]</td>
<td><strong>Virtual Machine ID</strong>. Um identificador de 8 ou 16 bits (se <code>FEAT_VMID16</code> implementado e <code>VTCR_EL2.VS == 1</code>) que é concatenado com o ASID de Stage 1 para formar um identificador de contexto de tradução. Usado para <em>tagging</em> de entradas de TLB (Translation Lookaside Buffer) e para isolamento de máquinas virtuais.</td>
</tr>
<tr>
<td><strong>BADDR</strong></td>
<td>[47:5] ou<br/>[47:1]</td>
<td><strong>Base Address</strong>. Endereço base da tabela de tradução de Stage 2. O alinhamento é determinado pelo tamanho da tabela no nível inicial.</td>
</tr>
<tr>
<td><strong>SKL</strong></td>
<td>[2:1]</td>
<td><strong>Skip Level</strong>. Determina o número de níveis a serem pulados no <em>walk</em> da tabela de tradução de Stage 2.</td>
</tr>
<tr>
<td><strong>CnP</strong></td>
<td>[0]</td>
<td><strong>Common not Private</strong>. Indica se as entradas da tabela de tradução são comuns (compartilhadas) entre PEs no domínio Inner Shareable.</td>
</tr>
</table>
2. Stage-2 Translation (Tradução de Endereço)
A tradução de Stage 2 converte um **Intermediate Physical Address (IPA)**, que é o endereço de saída da Stage 1 (gerenciado pelo SO convidado), em um **Physical Address (PA)**, que é o endereço físico real (gerenciado pelo Hypervisor).
O formato do descritor de 64 bits (PTE ou Block Descriptor) de Stage 2 é fundamental para o controle de acesso e atributos de memória.
<table>
<tr>
<th>Bits</th>
<th>Campo</th>
<th>Descrição Técnica</th>
</tr>
<tr>
<td>[1:0]</td>
<td>Type</td>
<td><code>0b11</code> para Page/Block Descriptor.</td>
</tr>
<tr>
<td>[5:2]</td>
<td>AttrIndex</td>
<td>Índice de 4 bits para o registro <strong>MAIR_EL2</strong> (Memory Attribute Indirection Register) para definir os atributos de memória (Normal, Device, Cacheability).</td>
</tr>
<tr>
<td>[6]</td>
<td>NS</td>
<td><strong>Non-Secure</strong>. 1 indica que o endereço de saída é Non-Secure.</td>
</tr>
<tr>
<td>[8:7]</td>
<td>SH</td>
<td><strong>Shareability</strong>. <code>00</code> (Non-shareable), <code>10</code> (Outer Shareable), <code>11</code> (Inner Shareable).</td>
</tr>
<tr>
<td>[9]</td>
<td>AP[0]</td>
<td><strong>Access Permission bit 0</strong>. Combinado com AP[2:1] para definir as permissões de acesso.</td>
</tr>
<tr>
<td>[10]</td>
<td>AP[1]</td>
<td><strong>Access Permission bit 1</strong>.</td>
</tr>
<tr>
<td>[11]</td>
<td>AP[2]</td>
<td><strong>Access Permission bit 2</strong>.</td>
</tr>
<tr>
<td>[12]</td>
<td>XN</td>
<td><strong>Execute Never</strong>. 1 impede a execução de instruções na região de memória.</td>
</tr>
<tr>
<td>[13]</td>
<td>Contiguous</td>
<td>1 indica que o bloco é parte de um bloco contíguo maior.</td>
</tr>
<tr>
<td>[14]</td>
<td>PXN</td>
<td><strong>Privileged Execute Never</strong>. 1 impede a execução de instruções no EL1/EL0.</td>
</tr>
<tr>
<td>[15]</td>
<td>HAP</td>
<td><strong>Hardware Access Flag</strong>. 1 indica que a entrada foi acessada.</td>
</tr>
<tr>
<td>[47:16]</td>
<td>Output Address</td>
<td>Endereço físico de saída (PA) para o bloco ou página.</td>
</tr>
<tr>
<td>[58:55]</td>
<td>Software Use</td>
<td>Bits reservados para uso do software (e.g., dirty bit).</td>
</tr>
<tr>
<td>[63:59]</td>
<td>Ignored</td>
<td>Bits ignorados pelo hardware.</td>
</tr>
</table>
de Combinação de Atril
O atributo de memória final para uma transação é o resultado da combinação dos atributos de Stage 1 (gerenciados pelo SO convidado) e Stage 2 (gerenciados pelo Hypervisor).

**Fórmula de Permissão de Acesso (Access Permission):**

A permissão de acesso final é a **interseção** (AND lógico) das permissões de Stage 1 e Stage 2.

Permissão Final = Permissão<sub>Stage 1</sub> ∩ Permissão<sub>Stage 2</sub>

**Fórmula de Atributo de Execução (Execute Never - XN):**

A região é **Execute Never** se for marcada como tal em **qualquer** estágio.

XN Final = XN<sub>Stage 1</sub> ∨ XN<sub>Stage 2</sub>
órmula de Atributo de Cacheabilidade (Cacheability)
O atributo de cacheabilidade final é o **mais restritivo** entre os dois estágios. Por exemplo, se um estágio for o outro for **Normal Write-Through**, o resultado é **Normal Write-Through**. Se um estágio for **Device** e o outro é **Device**.
3. VHE (Virtualization Host Extensions)
O VHE é uma extensão de arquitetura (controlada pelo bit **E2H** no HCR_EL2) que permite que um SO host (cor-
e Mapeamento de Registos
| Quando o bit **E2H** está ativo, o hardware mapeia transparentemente os registros de EL1 para seus equivalentes de EL2, permitindo que o SO host (que espera usar registros de EL1) opere no EL2 sem modificações. |  |
| --- | --- |
<table>
<tr>
<th>Registro de EL1 (SO Host)</th>
<th>Mapeado para (EL2)</th>
<th>Descrição</th>
</tr>
<tr>
<td><strong>SP_EL1</strong></td>
<td><strong>SP_EL2</strong></td>
<td>Stack Pointer</td>
</tr>
<tr>
<td><strong>ELR_EL1</strong></td>
<td><strong>ELR_EL2</strong></td>
<td>Exception Link Register</td>
</tr>
<tr>
<td><strong>SPSR_EL1</strong></td>
<td><strong>SPSR_EL2</strong></td>
<td>Saved Program Status Register</td>
</tr>
<tr>
<td><strong>TTBR0_EL1</strong></td>
<td><strong>TTBR0_EL2</strong></td>
<td>Translation Table Base Register 0</td>
</tr>
<tr>
<td><strong>TTBR1_EL1</strong></td>
<td><strong>TTBR1_EL2</strong></td>
<td>Translation Table Base Register 1</td>
</tr>
<tr>
<td><strong>TCR_EL1</strong></td>
<td><strong>TCR_EL2</strong></td>
<td>Translation Control Register</td>
</tr>
<tr>
<td><strong>MAIR_EL1</strong></td>
<td><strong>MAIR_EL2</strong></td>
<td>Memory Attribute Indirection Register</td>
</tr>
<tr>
<td><strong>VBAR_EL1</strong></td>
<td><strong>VBAR_EL2</strong></td>
<td>Vector Base Address Register</td>
</tr>
<tr>
<td><strong>FAR_EL1</strong></td>
<td><strong>FAR_EL2</strong></td>
<td>Fault Address Register</td>
</tr>
<tr>
<td><strong>ESR_EL1</strong></td>
<td><strong>ESR_EL2</strong></td>
<td>Exception Syndrome Register</td>
</tr>
</table>
Algoritmo de Execução VHE (E2H=1):
1. O SO host é executado no EL2.
2. O bit **TGE** (Trap General Exceptions) no HCR_EL2 é setado para 1.
3. Exceções de EL0 são tratadas no EL2 (como se fossem de EL1).
4. O hardware usa os registros de EL2 (como TTBR0_EL2) para a tradução de Stage 1, mas o código do SO host usa as instruções de acesso aos registros de EL1 (como MSR TTBR0_EL1, Xn).
5. O Hypervisor (que agora é o SO host) não precisa de Stage 2 para sua própria execução, mas a Stage 2 é usada para as VMs convidadas.
4. Protocolos e Operações de TLB
validação de TLB (Translation Lookaside Buffer)
A invalidação de TLB é crucial para garantir a coerência das traduções após modificações nas tabelas de páginas (Seção 2).
<table>
  <thead>
    <tr>
      <th>Instrução</th>
      <th>Descrição Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>TLBI VAAE1</strong></td>
      <td>TLB Invalidate by VA, All ASID, EL1. Invalida entradas de Stage 1 para um endereço virtual (VA) específico, independentemente do ASID.</td>
    </tr>
    <tr>
      <td><strong>TLBI VAE1</strong></td>
      <td>TLB Invalidate by VA, EL1. Invalida entradas de Stage 1 para um VA específico e o ASID atual.</td>
    </tr>
    <tr>
      <td><strong>TLBI VMALLE1</strong></td>
      <td>TLB Invalidate by VMID, All at Stage 1, EL1. Invalida todas as entradas de Stage 1 para o VMID atual.</td>
    </tr>
    <tr>
      <td><strong>TLBI IPAS2E1IS</strong></td>
      <td>TLB Invalidate by IPA, Stage 2, EL1, Inner Shareable. Invalida entradas de Stage 2 para um Intermediate Physical Address (IPA) específico.</td>
    </tr>
    <tr>
      <td><strong>TLBI VMALLS12E1</strong></td>
      <td>TLB Invalidate by VMID, All at Stage 1 and 2, EL1. Invalida todas as entradas de Stage 1 e Stage 2 para o VMID atual.</td>
    </tr>
    <tr>
      <td><strong>TLBI VMALLS12E1IS</strong></td>
      <td>TLB Invalidate by VMID, All at Stage 1 and 2, EL1, Inner Shareable. Invalida todas as entradas de Stage 1 e Stage 2 para o VMID atual, com garantia de Inner Shareable.</td>
    </tr>
  </tbody>
</table>
4.2. VMID (Virtual Machine ID)
O VMID é um campo de 8 ou 16 bits no registro VTTBR_EL2.

**Função:**
* **Isolamento de Contexto:** O VMID é usado pelo hardware para *tagging* de entradas de TLB. Isso permite que o TLB contenha entradas de tradução de diferentes máquinas virtuais simultaneamente sem conflito, garantindo que o *guest A* não use acidentalmente uma tradução do *guest B*.

* **Coerência:** Quando o Hypervisor troca de VM, ele só precisa mudar o valor do VMID no VTTBR_EL2. A invalidação completa do TLB é evitada, pois as entradas antigas permanecem no TLB, mas são ignoradas se o VMID não corresponder.

**Estrutura (VTTBR_EL2):**

* **VMID (8 bits):** Bits 7:0.
* **VMID (16 bits):** Bits 15:0.
* O VMID é efetivamente parte do endereço de contexto de tradução, garantindo o isolamento.
Conceito 22: big.LITTLE - Heterogeneous multi-processing, CPU migration, GTS

Global Task Scheduling
**Itens Técnicos Encontrados:** 7
**Conceitos-Chave:** Heterogeneous Multi-Processing (HMP), CoreLink CCI-400, Global Task Scheduling (GTS), CPU Migration, Dynamic Voltage and Frequency Scaling (DVFS), big.LITTLE MP Scheduler, Power Consumption Formula
**big.LITTLE: Conteúdo Técnico (Algoritmos, Fórmulas e Estruturas)**
**LITTLE** é uma arquitetura de processamento heterogêneo (Heterogeneous Multi-Processing - HMP) da ARM que combina núcleos de alta performance (“big”, e.g., Cortex-A72) e núcleos de alta eficiência (“LITTLE”, e.g., Cortex-A53) em um Sistema-on-Chip (SoC). A gestão de tarefas e a migração entre esses núcleos são realizadas por algoritmos de escalonamento e gerenciadores de hardware específicas.
1. Estruturas de Hardware e Protocolos
*   **CoreLink CCI-400 (Cache Coherent Interconnect):** Este é o protocolo/estrutura de hardware fundamental que garante a coerência de cache entre os clusters big e LITTLE. O CCI-400 permite que os dados sejam compartilhados e que a migração de contexto ocorra rapidamente, acessando o cache do cluster de saída via *snooping* para evitar acessos custosos à memória principal [1].
*   **Gerenciamento de Energia (DVFS e Power Switching):** A arquitetura utiliza **Dynamic Voltage and Frequency Scaling (DVFS)** e **Power Switching** para otimizar o consumo. O controle é feito por interfaces de *hardware* como o **Serial Power Controller (SPC)** e o **Serial Configuration Controller (SCC)**, que permitem ao software (kernel) controlar a tensão e frequência dos clusters, bem como o power-down/up e o wake-up dos clusters [2].
2. Algoritmos e Fórmulas de Escalonamento (GTS)
O **Global Task Scheduling (GTS)**, implementado no kernel Linux como **big.LITTLE MP**, é um algoritmo de escalonamento que trata todos os núcleos (big e LITTLE) como um único pool de recursos, sendo *capacity-aware* (sensível à capacidade).
Capacidade e Carga do Núcleo (Capacity-Aware Scheduling)
O escalonador big.LITTLE MP utiliza um modelo de capacidade para determinar o núcleo mais apropriado para uma *thread*. A capacidade de um núcleo é um valor escalonado que reflete seu desempenho relativo.
*   **Fator de Escala de Capacidade:** O kernel Linux define um fator de escala de capacidade, `SCHED_CAPACITY_SCALE`, que por padrão é 1024. A capacidade de cada núcleo é um valor entre 0 e 1024, onde 1024 representa a capacidade máxima do núcleo mais rápido (o núcleo *big* mais rápido) [3]. `$Capacidade(CPU_i) = SCHED_CAPACITY_SCALE \times \frac{Desempenho Relativo(CPU_i)}{Desempenho Máximo} * ExemploConceitual : *Seumnúcleo * big * temcapacidadeC(1024)eumnúcleo * LITTLE * temmetadededesempenho, suacapacidadeC/2$ (512) [3].
*   **Cálculo de Carga:** O escalonador rastreia a carga de cada *thread* como uma média ponderada histórica (*historical weighted average*) para prever sua necessidade de desempenho e, assim, aloca-la ao núcleo com capacidade correspondente (big ou LITTLE) [1].
2.2. Fórmula de Consumo de Energia (Base para Algoritmos Energy-Aware)
Algoritmos avançados de escalonamento sensíveis à energia, como o **VFS-Hetero-Split** (uma extensão do algoritmo **Hetero-Split** que incorpora DVFS), baseiam-se no modelo geral de consumo de energia de um processador CMOS, que é o foco de otimização:

$$\mathbf{P}_{\text{total}} = \mathbf{P}_{\text{static}} + n(\mathbf{P}_{\text{dynamic}} + \mathbf{P}_{\text{short-circuit}})$$
Onde [4]:
*   **P<sub>total</sub>**: Consumo total de energia do CPU.
*   **P<sub>static</sub>**: Potência estática (ou de vazamento - P<sub>leakage</sub>), devido às correntes de vazamento do transistor.
*   **n**: Número de núcleos ativos (ou não em deep sleep).
*   **P<sub>dynamic</sub>**: Potência dinâmica, devido à comutação dos transistores, modelada como: $P_{dynamic} \propto C_{eff} \cdot V_{dd}^2 \cdot f$
    *   C<sub>eff</sub>: Capacitância de comutação efetiva.
    *   V<sub>dd</sub>: Tensão de alimentação.
    *   f: Frequência de operação.
*   **P<sub>short-circuit</sub>**: Potência de curto-circuito, que ocorre brevemente durante a transição de estado dos transistores.
O INOS (In Kernel Switcher) é um modelo de migração de CPU onde o software gerencia a sequência de migração de contexto entre um par de núcleos (um big e um LITTLE).

**Sequência de Migração (Algoritmo de Alto Nível) [2]:**

1.  **Power-Up do Cluster de Entrada:** O cluster de destino (*inbound*) é ligado, retirado do *reset* e o isolamento é removido.
2.  **Migração de Contexto:** O estado do processador (*processor state save-restore*), o controle de *snooping* e a migração de interrupções são manipulados pelo software.
3.  **Power-Down do Cluster de Saída:** O cluster de origem (*outbound*) é colocado em *reset*, isolado e, em seguida, desligado.

O CoreLink CCI-400 é crucial para garantir que a migração de dados seja rápida e coerente.
3. Modos de Operação (Algoritmos de Ge
Estrutura/Protocolo de Migração
| | |
|---|---|
| 1 | O escalonador do SO executa apenas em um cluster por vez (big ou LITTLE). A migração ocorre quando o cluster ativo atinge seu limite de desempenho ou eficiência. |
| 2 | O escalonador opera em **núcleos virtuais** (um par big/LITTLE). A carga é avaliada para o núcleo virtual, e o contexto é migrado entre o núcleo big e LITTLE conforme a mudança no perfil de carga. |
| 3 | O escalonador do SO (e.g., big.LITTLE MP) é *capacity-aware* e opera em **todos os núcleos** simultaneamente, alocando *threads* ao núcleo mais apropriado com base no perfil de carga histórica da *thread*. |
**CCI-400** (para migração rápida de dados via *snooping*).

**CCI-400** (para coerência e compartilhamento de dados entre clusters).

**CCI-400** (para manter a coerência entre todos os núcleos ativos).
Referências
ower Management with big.LITTLE: A technical overview. ARM Developer. [2] Software Techniques for ARM big.LIT
ms. R Randhawa. [3] Capacity Aware Scheduling. The Linux Kernel documentation. [4] Energy-Aware Real-Time Schee
thm on ARM big.LITTLE HMP Architecture. I Jang, J Roh.
Conceito 23: DynamIQ - Flexible cluster configuration, asymmetric cluster core DVFS
**Itens Técnicos Encontrados:** 18

**Conceitos-Chave:** Cluster Assimétrico, Per-core DVFS, Power Policy Unit (PPU), DynamIQ Shared Unit (DSU), T

CLUSTERCFR
nteúdo Técnico - DynamiQ: Flexible cluster configuration symmetric clusters, per-core DVFS
Estrutura de Hardware:
*   **Cluster Assimétrico:** Um cluster pode ser configurado com até **três tipos diferentes de núcleos** (cores) simultaneamente, cada um visando diferentes níveis de eficiência energética e desempenho (e.g., núcleos de alto desempenho, núcleos de alta eficiência e núcleos intermediários).
*   **Limite de Cores:** O número total de cores no cluster **não pode exceder 14.**
*   **Complexos:** O cluster suporta a inclusão de **Complexos** (grupos de cores e lógica compartilhada) em vez de apenas cores individuais.
*   **Registro de Configuração:** O registro **CLUSTERCFR** (Cluster Configuration Register) contém detalhes da configuração de hardware do cluster e é somente leitura.
O controle de energia e, consequentemente, o DVFS por núcleo, é gerenciado pelas **Power Policy Units (PPUs)**.
ra de Hardware e Protocolo
*   **PPUs Independentes:** Existem PPUs separadas para cada um dos núcleos no cluster DSU-120T DynamIQ.
*   **Controle Independente:** O modo de energia de cada núcleo pode ser alterado **independentemente** dos outros núcleos no cluster. Não há restrição na ordem em que os núcleos são ligados ou desligados.
*   **Mecanismo de Controle:** Um componente externo, como um *System Control Processor (SCP)*, programa cada PPU de núcleo usando **transações AXI** para o **Utility Bus** para definir a política de energia apropriada.
*   **Ações de Hardware:** O PPU de núcleo controla os detalhes de baixo nível para implementar a política de energia solicitada, como:
    *   Gating de Clocks (desativação de clocks).
    *   Flushing de Caches (descarga de caches).
    *   Desativação de Coerência.
Codificações de Modos de Energia (Estrutura de Dados):
<table>
<tr>
<th>Power mode</th>
<th>PPU_PWPR.PWR_POLICY</th>
<th>PCSMPSTATE[3:0]</th>
<th>PPUHWSTAT[15:0]</th>
</tr>
<tr>
<td><strong>OFF</strong></td>
<td>0x0</td>
<td>0x0</td>
<td>0x0001</td>
</tr>
<tr>
<td><strong>OFF_EMU</strong></td>
<td>0x1</td>
<td>0x8</td>
<td>0x0002</td>
</tr>
<tr>
<td><strong>FULL_RET</strong></td>
<td>0x5</td>
<td>0x5</td>
<td>0x0020</td>
</tr>
<tr>
<td><strong>FUNC_RET</strong></td>
<td>0x7</td>
<td>0x7</td>
<td>0x0080</td>
</tr>
<tr>
<td><strong>ON</strong></td>
<td>0x8</td>
<td>0x8</td>
<td>0x0100</td>
</tr>
<tr>
<td><strong>WARM_RST</strong></td>
<td>0x9</td>
<td>0x8</td>
<td>0x0200</td>
</tr>
<tr>
<td><strong>DBG_RECOV</strong></td>
<td>0xA</td>
<td>0x8</td>
<td>0x0400</td>
</tr>
</table>
Refere-se a CORE<CN>PCSMPSTATE[3:0], onde CN é o nume-
: Refere-se a CORE<CN>PPUHWSTAT[15:0], onde CN é o núm-
O valor core<cn>PCSMSTATE[15:4] é fixo em 0x000
S é implementado através da transição entre o modo **ON** e outros modos, controlando a frequência e a voltagem do r
ma independente. O protocolo de comunicação é baseado em **transações AXI** no **Utility Bus** para o **PPU** de cada núcleo
## Algoritmos e Fórmulas (Pesquisa Completa)
A documentação de referência técnica (TRM) da ARM foca na estrutura de hardware e protocolos de baixo nível. As fórmulas de gerenciamento de DVFS são tipicamente implementados no software (e.g., kernel scheduler ou System Processor - SCP firmware).
Algoritmos (Mencionados em Pesquisa Inicial):
*   **Algoritmos de Escalonamento de Tarefas** que alavancam o per-core DVFS para otimização de energia/desempenho em plataformas multi-core.
*   **Dynamic Partitioned Scheduling** de tarefas em tempo real em arquiteturas ARM big.LITTLE/DynamIQ que utilizam per-core DVFS.

**Fórmulas:** Nenhuma fórmula matemática explícita (e.g., para cálculo de frequência/voltagem ou consumo de energia) foi encontrada na documentação de hardware, o que é esperado, pois a TRM foca na interface de controle (PPUs e registradores). As fórmulas estariam nos whitepapers de algoritmos de escalonamento ou gerenciamento de energia (software/firmware).
# Conceito 24: Power Management ARM - DVFS, idle states, WFI/WFE, race-to-idle

**Itens Técnicos Encontrados:** 15

**Conceitos-Chave:** DVFS, idle states, WFI, WFE, race-to-idle, PSCI
Dynamic Voltage and Frequency Scaling (DVFS)
Fórmula de Consumo de Potência Dinâmica
*   **P**: Potência dinâmica
*   **C**: Capacitância de comutação do circuito lógico
*   **V**: Tensão operacional
*   **f**: Frequência operacional
Idle States (Estados de Baixo Consumo)
Estrutura de Estados de Baixo Consumo
*   **Standby:** O núcleo permanece ligado, mas a maioria dos clocks são parados (clock-gated). A energia consumida é principalmente devido a correntes de fuga.
*   **Retention:** O estado do núcleo é preservado em estruturas de baixo consumo, permitindo que o núcleo seja parcialmente desligado. A restauração do estado é mais rápida que um power-down completo.
*   **Power-down:** O núcleo é completamente desligado. O estado do núcleo deve ser salvo pelo software e restaurado após o reinício.
*   **Dormant Mode:** A lógica do núcleo é desligada, mas as memórias cache permanecem ligadas em um estado de retenção com baixo consumo.
WFI (Wait For Interrupt) e WFE (Wait
Formato da Instrução (Hint instructions, sem operandos explícitos):
WFE

**Estrutura de Hardware e Protocolo (SEV/WFE):**

* Um registrador de eventos global é utilizado, com um bit para cada núcleo de CPU.
* A instrução SEV (Send Event) define o bit de evento para um ou mais núcleos.
* A instrução WFE coloca o núcleo em modo de baixo consumo até que o bit de evento correspondente seja definido.
# Race-to-Idle
Algoritmo e Fórmula (Velocidade Crítica):
ceito de “race-to-idle” envolve executar tarefas na velocidade máxima para retornar ao estado de baixo consumo o possível. A otimização do consumo de energia depende de uma “velocidade crítica” (scrit).
<table>
<tr>
<td>P(s) = P_static + P_dynamic(s)</td>
</tr>
<tr>
<td>E(s) = W * (P_static + P_dynamic(s)) / s</td>
</tr>
</table>
Onde:

*   **P(s):** Consumo total de energia na velocidade s
*   **P_static:** Consumo de energia estático
*   **P_dynamic(s):** Consumo de energia dinâmico na velocidade s
*   **E(s):** Energia total para completar o trabalho w na velocidade s

scrit é a velocidade que minimiza E(s). A fórmula exata para scrit depende da função de potência específica do processador.
Power State Coordination Interface (PSCI)
**Protocolo e IDs de Função (Exemplos):**

O PSCI define uma interface padrão para o software de supervisão gerenciar o estado de energia. As chamadas são feitas via SMC (Secure Monitor Call).
<table>
<tr>
<th>Função</th>
<th>ID da Função (SMC64)</th>
<th>Descrição</th>
</tr>
<tr>
<td>PSCI_VERSION</td>
<td>0xC4000000</td>
<td>Retorna a versão do PSCI.</td>
</tr>
<tr>
<td>CPU_SUSPEND</td>
<td>0xC4000001</td>
<td>Suspende a execução em um núcleo.</td>
</tr>
<tr>
<td>CPU_OFF</td>
<td>0x84000002</td>
<td>Desliga um núcleo.</td>
</tr>
<tr>
<td>CPU_ON</td>
<td>0xC4000003</td>
<td>Liga um núcleo.</td>
</tr>
<tr>
<td>AFFINITY_INFO</td>
<td>0xC4000004</td>
<td>Obtém o estado de um nó de afinidade.</td>
</tr>
<tr>
<td>MIGRATE</td>
<td>0xC4000005</td>
<td>Solicita a migração de um contexto de SO confiável.</td>
</tr>
<tr>
<td>SYSTEM_OFF</td>
<td>0x84000008</td>
<td>Desliga o sistema.</td>
</tr>
<tr>
<td>SYSTEM_RESET</td>
<td>0x84000009</td>
<td>Reinicia o sistema.</td>
</tr>
</table>
Conceito 25: Interconnect ARM - AMBA AXI, ACE, CHI, CCI Cache Coherent Interconnect, NoC
ns Técnicos Encontrados: 20
**Conceitos-Chave:** Protocolo AXI, Extensões ACE, Protocolo CHI, Filtro de Snoop, Algoritmo de Roteamento NoC, Canais de Transação, Estados de Coerência de Cache, Fluxo de Crédito, Estrutura de Pacotes
O conteúdo a seguir foca exclusivamente nos protocolos, estruturas de hardware, algoritmos e fórmulas que definem os padrões de interconexão da arquitetura ARM.
# 1.1. Estrutura de Protocolo AXI

O protocolo AXI é baseado em cinco canais de comunicação independentes, cada um com seu próprio mecanismo de handshake VALID / READY [1]:

1. **Write Address (AW)**: Endereço e informações de controle para transações de escrita.
2. **Write Data (W)**: Dados a serem escritos.
3. **Write Response (B)**: Resposta da transação de escrita.
4. **Read Address (AR)**: Endereço e informações de controle para transações de leitura.
5. **Read Data ®**: Dados lidos e resposta da transação de leitura.
1.2. Algoritmos de Burst e Cálculo de Endereço
<table>
<tr>
<th>Tipo de Burst</th>
<th>Descrição Técnica</th>
<th>Algoritmo de Endereço (Implícito)</th>
</tr>
<tr>
<td><strong>FIXED</strong></td>
<td>O endereço permanece constante para todas as transferências no <em>burst</em>.</td>
<td>$\text{Endereço}_n = \text{Endereço}_{0}$<sub>m</sub><sub>i</sub><sub>c</sub><sub>i</sub><sub>a</sub><sub>l</sub></td>
</tr>
<tr>
<td><strong>INCR</strong></td>
<td>O endereço incrementa a cada transferência.</td>
<td>$\text{Endereço}_n = \text{Endereço}_{n-1} + \text{Tamanho da Transferência}$</td>
</tr>
<tr>
<td><strong>WRAP</strong></td>
<td>O endereço incrementa, mas "envolve" (volta) para um endereço base se um limite superior for atingido.</td>
<td>$\text{Endereço}_n = (\text{Endereço}_{n-1} + \text{Tamanho da Transferência})$<br/>$(\text{mod Limite de Envolvimento}) + \text{Endereço Base}$</td>
</tr>
</table>
O **Limite de Envolvimento** (Wrap Boundary) é alinhado ao tamanho total do burst: $Limite_de_Envolvimento = Tamanho_da_Transferência \times Comprimento_do_Burst$
1.3. Protocolo ACE e Estados de Coerência de Cache
O ACE (AXI Coherency Extensions) adiciona canais de coerência para suportar o protocolo de coerência de cache **MESI** (Modified, Exclusive, Shared, Invalid) e suas variantes [1].

**Canais de Coerência (ACE):**

*   **Address Snoop (AC):** Usado para enviar endereços de *snoop* (espiada) para outros mestres.
*   **Snoop Response (CR):** Usado para retornar a resposta do *snoop*.
*   **Data Channel (CD):** Usado para transferir dados de volta durante uma transação de *snoop*.

**Estados de Coerência de Cache (ACE-Lite e ACE):** O protocolo define estados de cache para dados em locais compartilháveis:

*   **Invalid (I):** A linha de cache não contém dados válidos.
*   **Shared (S):** A linha de cache contém dados válidos que podem ser compartilhados.
*   **Exclusive (E):** A linha de cache contém dados válidos que não são compartilhados.
*   **Modified (M):** A linha de cache contém dados válidos e modificados (sujos), e não é compartilhada.
2. AMBA CHI (Coherent Hub Interface
2.1. Estrutura de Comunicação e Canais
**Canais de Comunicação (CHI):**
1. **REQ (Request):** Transmite requisições de um nó Requisitante (RN) para um nó Home (HN) ou outro nó.
2. **RSP (Response):** Transmite respostas de transação (sem dados) de volta ao RN.
3. **DAT (Data):** Transmite dados de escrita ou dados de resposta de leitura.
4. **SNP (Snoop):** Transmite requisições de *snoop* de um HN para outros nós.
5. **RSP/DAT Combinado (RDAT/CRSP):** Em algumas implementações, as respostas e dados podem ser combinados.

### 2. Controle de Fluxo Baseado em Crédito

O controle de fluxo é implementado no nível do *Link Layer* (Camada de Link) para evitar *deadlocks* e *overflows* de buffer [2].

- **Flit:** A unidade básica de transferência de dados no link.
- **Créditos:** Cada canal mantém um contador de créditos. Uma mensagem só pode ser enviada se o nó receptor tiver créditos disponíveis para o canal correspondente.
- **Sinais de Crédito:** PCrdType (Tipo de Crédito de Protocolo) e PCrdGrant (Concessão de Crédito de Protocolo) são usados para gerenciar o fluxo.
2.3. Estrutura de Mensagem (Packet)
As mensagens CHI são compostas por campos que definem a transação [2]:
*   **Opcode:** Define o tipo de transação (e.g., ReadShared, WriteUnique, CompData).
*   **TxnID (Transaction ID):** Identificador da transação, atribuído pelo Requisitante.
*   **SrcID (Source ID):** Identificador do nó de origem.
*   **TgtID (Target ID):** Identificador do nó de destino.
*   **DBID (Data Buffer ID):** Identificador de buffer de dados, usado para associar respostas de dados a requisições.
3. CCI (Cache Coherent Interconnect)
rutura de Hardware: Filtro de Snoop (Snoop Filter - SF)
O CCI (Cache Coherent Interconnect), como o CoreLink CCI-550, utiliza um **Filtro de Snoop** (Snoop Filter) para otimizar o tráfego de coerência [3].

*   **Função:** O SF é uma estrutura de diretório que armazena os endereços das linhas de cache presentes nos caches dos mestres ACE conectados.
*   **Estrutura:** É tipicamente uma estrutura de cache *set-associative* (por exemplo, 8-vias no CCI-550) que armazena *tags* (etiquetas) de endereço.
*   **Algoritmo (Implícito):** Quando uma requisição de coerência (snoop) chega, o CCI consulta o SF. Se o endereço não estiver no SF, o *snoop* não é transmitido aos mestres, reduzindo o tráfego de rede e a latência.
4. NoC (Network-on-Chip)
4.1. Estrutura de Hardware: Topologia e Roteadores
(Network-on-Chip) substitui os barramentos tradicionais por uma rede de comunicação em chip [4].

**Topologia:** Define a estrutura de interconexão dos roteadores (e.g., *Mesh*, *Torus*, *Ring*).

**Roteadores (Switches):** Componentes de hardware que recebem pacotes em portas de entrada e os encaminham para portas de saída com base no algoritmo de roteamento.
4.2. Algoritmos de Roteamento
- **Roteamento Determinístico:** O caminho é fixo para um dado par de origem-destino, independentemente do estado da rede.
caminho pode mudar dinamicamente com base no estado
onar a porta de saída mais eficiente.
Contagem Técnica
A contagem de elementos técnicos extraídos é a seguinte:

*   **Estruturas de Protocolo/Hardware:** 10 (5 Canais AXI, 3 Canais ACE, 5 Canais CHI, Filtro de Snoop, Roteadores NoC, Topologia NoC).
*   **Algoritmos/Fórmulas:** 5 (Cálculo de Endereço INCR, Cálculo de Endereço WRAP, Algoritmo de Handshake VALID/READY, Controle de Fluxo por Crédito, Algoritmos de Roteamento NoC).
*   **Conceitos de Protocolo:** 5 (Estados de Coerência de Cache, Tipos de Burst, Estrutura de Pacote CHI, DBID, Opcode).

**Total Aproximado: 20**
Referências
[1] ARM. **AMBA AXI and ACE Protocol Specification**. [2] ARM. **AMBA 5 CHI Architecture Specification** (IHI 0050E.a). [3] **CCI-550 Cache Coherent Interconnect**. [4] Ignitarium. **Network on Chip Overview**.
Conceito 26: Crypto Extensions ARM - AES, SHA, PMULL, CRC32
ns Técnicos Encontrados: 15
**itos-Chave:** AES, SHA-256, PMULL, CRC32, AESE, AESD, AESMC, AESIMC, SHA256SU0, SHA256SU1, SHA256H, SHA2

licação Polinomial, Corpo Finito GF(2^8), Polinômio Gerador CRC-32
otográficas ARMv8-A: AES, SI
O conteúdo a seguir detalha os aspectos técnicos (algoritmos, fórmulas, estruturas e formatos de instrução) Criptográficas da arquitetura ARMv8-A (AArch64), focando nas acelerações de hardware para AES, SHA, PMULL e CRC.
1. Advanced Encryption Standard (AES)
As instruções AES são implementadas como operações de **Advanced SIMD (NEON)** de 128 bits, projetadas para acelerar as transformações de uma rodada do AES: SubBytes, ShiftRows, MixColumns e AddRoundKey [1].
1.1. Instruções e Operações Aceleradas
nstruções operam em vetores de 128 bits (16 bytes) e são:
<table>
<tr>
<th>Instrução</th>
<th>Descrição</th>
<th>Operação Acelerada</th>
</tr>
<tr>
<td>AESE</td>
<td>AES single round encryption</td>
<td>SubBytes, ShiftRows, AddRoundKey (XOR)</td>
</tr>
<tr>
<td>AESD</td>
<td>AES single round decryption</td>
<td>InvSubBytes, InvShiftRows, AddRoundKey (XOR)</td>
</tr>
<tr>
<td>AESMC</td>
<td>AES mix columns</td>
<td>MixColumns</td>
</tr>
<tr>
<td>AESIMC</td>
<td>AES inverse mix columns</td>
<td>InvMixColumns</td>
</tr>
</table>
seudocódigo e Fórmulas
AESE (AES single round encryption)
A instrução AESE combina as transformações de AddRoundKey, SubBytes e ShiftRows em uma única operação.

```mermaid
classDiagram
    class bits {
        bits(128) operand1 = V[d];
        bits(128) operand2 = V[n];
        bits(128) result;
    }
    class AESSubBytes {
        bits(128) result = AESSubBytes(AESShiftRows(result));
    }
    class AESShiftRows {
        bits(128) result = AESShiftRows(result);
    }
    class AddRoundKey {
        bits(128) result = operand1 EOR operand2;
    }
    class V[d] {
        bits(128) result;
    }
    bits --> AESSubBytes;
    AESSubBytes --> AESShiftRows;
    AESShiftRows --> AddRoundKey;
    AddRoundKey --> V[d];
    V[d] --> bits;
AESMC (AES mix columns)
A instrução AESMC implementa a transformação MixColumns, que é uma multiplicação de matriz sobre o corpo finito $GF(2^8)$.

**Fórmula da Transformação MixColumns:**

$$\begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
\end{bmatrix} \cdot \begin{bmatrix}
    A \\
    B \\
    C \\
    D
\end{bmatrix} = \begin{bmatrix}
    B \oplus C \oplus D \\
    A \oplus C \oplus D \\
    A \oplus B \oplus D \\
    A \oplus B \oplus C
\end{bmatrix}$$
$$\begin{pmatrix} b_0' \\ b_1' \\ b_2' \\ b_3' \end{pmatrix} = \begin{pmatrix} 02 & 03 & 01 & 01 \\ 01 & 02 & 03 & 01 \\ 01 & 01 & 02 & 03 \\ 03 & 01 & 01 & 02 \end{pmatrix} \times \begin{pmatrix} b_0 \\ b_1 \\ b_2 \\ b_3 \end{pmatrix}$$

A multiplicação e a adição são realizadas em $GF(2^8)$ com o polinômio irreutível $m(x) = x^8 + x^4 + x^3 + x + 1$.

**AESIMC (AES inverse mix columns)**

A instrução AESIMC implementa a transformação Inverse MixColumns, usando a matriz inversa $C^{-1}$ sobre $GF(2^8)$.

**Fórmula da Transformação Inverse MixColumns:**

A operação é a multiplicação de cada coluna do estado pela matriz fixa $C^{-1}$ [2]:
$$\begin{array}{r}{\left(\begin{array}{l}{b_{0}^{\prime}}\\ {b_{1}^{\prime}}\\ {b_{2}^{\prime}}\\ {b_{3}^{\prime}}\end{array}\right)=\left(\begin{array}{llll}{0E}&{0B}&{0D}&{09}\\ {09}&{0E}&{0B}&{0D}\\ {0D}&{09}&{0E}&{0B}\\ {0B}&{0D}&{09}&{0E}\end{array}\right)\times\left(\begin{array}{l}{b_{0}}\\ {b_{1}}\\ {b_{2}}\\ {b_{3}}\end{array}\right)}\end{array}$$
2. Secure Hash Algorithm (SHA)
As extensões criptográficas ARMv8-A incluem instruções para acelerar o **SHA-1** e o **SHA-256** [3]. As instruções operam de 128 bits (quatro palavras de 32 bits) para processar quatro rodadas da função de compressão ou quatro palavras Schedule em paralelo.
ções de Aceleração SHA-
<table>
<tr>
<th>Instrução</th>
<th>Descrição</th>
<th>Operação Acelerada</th>
</tr>
<tr>
<td>SHA256SU0</td>
<td>SHA256 schedule update 0</td>
<td>Acelera o cálculo de $\sigma_0$ e $\sigma_1$ para o Message Schedule</td>
</tr>
<tr>
<td>SHA256SU1</td>
<td>SHA256 schedule update 1</td>
<td>Acelera a soma final para o Message Schedule</td>
</tr>
<tr>
<td>SHA256H</td>
<td>SHA256 hash update (part 1)</td>
<td>Acelera parte da função de compressão (cálculo de $T_1$)</td>
</tr>
<tr>
<td>SHA256H2</td>
<td>SHA256 hash update (part 2)</td>
<td>Acelera parte da função de compressão (cálculo de $T_2$)</td>
</tr>
</table>
# . Fórmulas Aceleradas (Funções Lógicas)
nstruções aceleram as funções lógicas e de rotação do SHA-
*   **Funções de Agendamento de Mensagem** ($\sigma$): $\$ \sigma_0(W) = (W \ggg 7) \oplus (W \ggg 18) \oplus (W \ggg 3)$
    $\sigma_1(W) = (W \ggg 17) \oplus (W \ggg 19) \oplus (W \ggg 10) \$$
*   **Funções de Compressão** ($\Sigma$, $Ch$, $Maj$): $\$ \Sigma_0(a) = (a \ggg 2) \oplus (a \ggg 13) \oplus (a \ggg 22)$
    $\Sigma_1(e) = (e \ggg 6) \oplus (e \ggg 11) \oplus (e \ggg 25)$
    $Ch(e,f,g) = (e \wedge f) \oplus (\neg e \wedge g)$
    $Maj(a,b,c) = (a \wedge b) \oplus (a \wedge c) \oplus (b \wedge c) \$$

As instruções SHA256H e SHA256H2 implementam a atualização do vetor de hash $(a,b,c,d,e,f,g,h)$ em 4 rodadas por instrução, utilizando as funções acima de forma otimizada.
3. Polynomial Multiply Long (PMULL)
A instrução **PMULL** (Polynomial Multiply Long) realiza a **multiplicação de polinômios sem transporte** (*carry-less multiplication*) sobre o corpo finito $GF(2)$ [4]. É crucial para acelerar o modo de operação Galois/Counter Mode (**GCM**) do AES e para cálculos de hash universais.
3.1. Instrução PMULL (AArch64)
<table>
<tr>
<th>Instrução</th>
<th>Descrição</th>
<th>Operação Acelerada</th>
</tr>
<tr>
<td>PMULL</td>
<td>Polynomial Multiply Long</td>
<td>Multiplicação de polinômios de 64 bits para um resultado de 128 bits</td>
</tr>
<tr>
<td>PMULL2</td>
<td>Polynomial Multiply Long (Upper)</td>
<td>Multiplicação dos 64 bits superiores dos operandos</td>
</tr>
</table>
3.2. Algoritmo e Fórmula
rodução PMULL multiplica dois polinômios de 64 bits com coeficientes em $GF(2)$, resultando em um polinômio de 128 bits (zenado em 128 bits).
Fórmula da Multiplicação Polinomial:
Sejam $A(x)$ e $B(x)$ os polinômios representados pelos operandos de 64 bits. A operação é a multiplicação de polinômios:

$$C(x) = A(x) \cdot B(x) \pmod{2}$$

Onde a multiplicação é realizada sem transporte (carry-less) e a adição é o **XOR bit a bit**.
4. Cyclic Redundancy Check (CRC32)
lcum o valor de **Cyclic Redundancy Check (CRC)**, um código de detecção de erros baseado em divisão ) [5].
Instruções CRC32 (AArchive)
As instruções operam em um acumulador CRC de 32 bits e um valor de entrada de 8, 16, 32 ou 64 bits:
<table>
<tr>
<th>Instrução</th>
<th>Descrição</th>
<th>Tamanho do Operando</th>
</tr>
<tr>
<td>CRC32B</td>
<td>CRC32 checksum</td>
<td>8 bits (Byte)</td>
</tr>
<tr>
<td>CRC32H</td>
<td>CRC32 checksum</td>
<td>16 bits (Halfword)</td>
</tr>
<tr>
<td>CRC32W</td>
<td>CRC32 checksum</td>
<td>32 bits (Word)</td>
</tr>
<tr>
<td>CRC32X</td>
<td>CRC32 checksum</td>
<td>64 bits (Doubleword)</td>
</tr>
</table>
4.2. Algoritmo e Polinômio Gerador
As instruções CRC32 usam o polinômio gerador padrão para **CRC-32 (IEEE 802.3)**:

*   **Polinômio Gerador:** $G(x) = x^{32} + x^{26} + x^{23} + x^{22} + x^{16} + x^{12} + x^{11} + x^{10} + x^{8} + x^{7} + x^{5} + x^{4} + x^{2} + x + 1$
*   **Representação Hexadecimal:** 0x04C11DB7

**Pseudocódigo da Operação CRC32:**
// X[n] é o acumulador CRC (32 bits)
// X[m] é o valor de entrada (8, 16, 32 ou 64 bits)
// X[d] é o resultado CRC (32 bits)

bits(32) acc = X[n]; // acumulador
bits(size) val = X[m]; // valor de entrada (size = 8, 16, 32 ou 64)
bits(32) poly = 0x04C11DB7<31:0>; // Polinômio gerador

// 1. Reversão de bits do acumulador e do valor de entrada
bits(32+size) tempacc = BitReverse(acc):Zeros(size);
bits(size+32) tempval = BitReverse(val):Zeros(32);

// 2. XOR e Divisão Polinomial (Modulus)
// Poly32Mod2 realiza a operação de módulo polinomial sobre GF(2)
X[d] = BitReverse(Poly32Mod2(tempacc EOR tempval, poly));
A função Poly32Mod2 realiza a divisão polinomial sobre $GF(2)$ para encontrar o resto, que é o novo valor CRC.
Referências
| [1] | Arm Developer. | *AESE:* AES single round encryption. | [Online]. | Available: |
|---|---|---|---|---|
|  |  | https://developer.arm.com/documentation/ddi0596/2021-06/SIMD-FP-Instructions/AESE-AES-single-round-encryption- |  | [2] Arm Developer. |
|  |  | AESIMC: AES inverse mix columns. | [Online]. | Available: |
|  |  | https://developer.arm.com/documentation/ddi0602/latest/SIMD-FP-Instructions/AESIMC-AES-inverse-mix-columns- |  | [3] Nemanja Mijailovic. Exploring .NET Core platform intrinsics: Part 1 - Accelerating SHA-256 on ARMv8. | [Online]. | Available: |
|  |  | https://mijailovic.net/2018/06/06/sha256-armv8/ |  | [4] Stanford SCS. PMULL, PMULL2 – A64. | [Online]. | Available: |
|  |  | https://www.scs.stanford.edu/~zyedidia/arm64/pmulldavsimd.html |  | [5] Arm Developer. CRC32B, CRC32H, CRC32W, CRC32X: CRC32 checksum. | [Online]. | Available: |
|  |  | https://developer.arm.com/documentation/ddi0596/2021-06/Base-Instructions/CRC32B-CRC32H-CRC32W-CRC32X-CRC32-checksum- |  |  |  |  |
Conceito 27: SME Scalable Matrix Extension
ns Técnicos Encontrados: 15
**Conceitos-Chave:** ZA Storage, Streaming SVE Mode, Outer Product Accumulate, Matrix Tiles, SMOPA, UMOPS, BFMOPA, FMOPA, Formato de Instrução A64
O conteúdo técnico a seguir foca exclusivamente nos aspectos de **algoritmos, fórmulas, estruturas de hardware e formatos de instrução** da extensão ARM Scalable Matrix Extension (SME), conforme solicitado.
O ZA (Z Array) é o principal registro de estado introduzido pela SME, projetado para armazenar tiles de matrizes para operações de alta taxa de transferência [1] [2].

*   **Estrutura:** O ZA é um array quadrado bidimensional de bytes, com dimensão determinada pelo Streaming Vector Length (SVL) [1]. $Tamanho do ZA = (SVL em bytes) × (SVL em bytes)$
*   **SVL (Streaming Vector Length):** O SVL é o comprimento do vetor no Streaming SVE Mode, e pode ser configurado para 128, 256, 512, 1024 ou 2048 bits [1].
*   **Acesso como Tiles:** O ZA pode ser acessado como um conjunto de tiles de matrizes quadradas, onde o número de tiles disponíveis depende da relação entre o SVL e o tamanho da matriz [1].
<table>
<tr>
<th>Tamanho do Elemento</th>
<th>Número de Tiles</th>
<th>Nomes dos Tiles</th>
</tr>
<tr>
<td>8-bit (B)</td>
<td>1</td>
<td>ZA0.B</td>
</tr>
<tr>
<td>16-bit (H)</td>
<td>2</td>
<td>ZA0.H - ZA1.H</td>
</tr>
<tr>
<td>32-bit (S)</td>
<td>4</td>
<td>ZA0.S - ZA3.S</td>
</tr>
<tr>
<td>64-bit (D)</td>
<td>8</td>
<td>ZA0.D - ZA7.D</td>
</tr>
<tr>
<td>128-bit (Q)</td>
<td>16</td>
<td>ZA0.Q - ZA15.Q</td>
</tr>
</table>
- **Acesso como Vetores:** O ZA também pode ser acessado como vetores de SVL bits para operações de carga/armazenamento utilizando a sintaxe ZA.B[N], ZA.H[N], etc., onde N é o índice do vetor [1].
2. Protocolo de Execução: Streaming SVE Modee
Streaming SVE Mode é um modo de execução introduzido pela SME que ativa o ZA storage e utiliza o SVL para operações de matriz [1].

*   **Controle de Estado:** O modo é controlado pelos bits de estado do processador PSTATE.{SM, ZA} [1]:
    *   SM: Habilita/Desabilita o Streaming SVE Mode.
    *   ZA: Habilita/Desabilita o acesso ao ZA storage.

*   **Instruções de Controle:** As instruções de alias para modificar o PSTATE são [1]:
    *   SMSTART ZA : Habilita o acesso ao ZA storage (PSTATE.ZA = 1).
    *   SMSTART SM : Habilita o Streaming SVE Mode (PSTATE.SM = 1).
    *   SMSTART : Habilita ambos (PSTATE.SM = 1, PSTATE.ZA = 1).
    *   SMSTOP ZA, SMSTOP SM, SMSTOP : Instruções correspondentes para desabilitar.
3. Algoritmo Principal: Outer Product and Accumulate
- **Conceito Matemático:** A multiplicação de matrizes pode ser decomposta em uma série de operações de produto externo, que são então acumuladas [2]. $C = A \times B = \sum_{k=1}^{K} a_k b_k^T$ onde $\mathbf{a}_k$ é o késimo coluna de $\mathbf{A}$ e $\mathbf{b}_k$ é a késima linha de $\mathbf{B}$.

- **Operação da Instrução:** As instruções SME calculam o produto externo de dois vetores de entrada (registros SVE **Zn** e **Zm**), e acumulam (somam ou subtraem) o resultado no tile de destino do ZA (**ZAda**) [2]. $ZAda = ZAda \pm (Zn \otimes Zm)$ onde $\otimes$ representa a operação de produto externo.
nulas de Alargamento (Wide
Muitas instruções OPA realizam um alargamento (*widening*) do tipo de dado durante a acumulação para evitar *overflow* [2]:

- **BF16 (BFloat16):** Soma de dois produtos externos BF16, alargando o resultado para **FP32** antes de acumular no *tile* ZAda.S [2].
- **INT8:** Soma de quatro produtos externos INT8, alargando o resultado para **INT32** antes de acumular no *tile* ZAda.S [2].
- **INT16:** Soma de dois produtos externos INT16, alargando o resultado para **INT32** antes de acumular no *tile* ZAda.S [2].
- **FP16:** Soma de dois produtos externos FP16, alargando o resultado para **FP32** antes de acumular no *tile* ZAda.S [2].
- **INT16 para INT64 (FEAT_SME_I16I64):** Soma de quatro produtos externos INT16, alargando o resultado para **INT64** antes de acumular no *tile* ZAda.D [2].
4. Formatos de Instrução (Encoding)
As instruções SME são codificadas no conjunto de instruções A64, utilizando um formato de 32 bits [3]
4.1. Codificação do Outer Product (32-bit)
produto externo de 32 bits (FMOPA, BFMOPA, SMOPA, UMO
<table>
<tr>
<th>Bits</th>
<th>31</th>
<th>30</th>
<th>29-24</th>
<th>23</th>
<th>22</th>
<th>21</th>
<th>20-16</th>
<th>15-11</th>
<th>10-6</th>
</tr>
<tr>
<td>Campo</td>
<td>1</td>
<td>0</td>
<td>000000</td>
<td>u0</td>
<td>1</td>
<td>u1</td>
<td>Zm</td>
<td>Pm</td>
<td>Pn</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>• Zm (5 bits): Registro de vetor SVE de entrada <em>m</em>.</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>• Pm (4 bits): Registro de predicado de entrada <em>m</em>.</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>• Pn (4 bits): Registro de predicado de entrada <em>n</em>.</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>• Zn (5 bits): Registro de vetor SVE de entrada <em>n</em>.</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>• S (1 bit): Bit de seleção (0 para Accumulate - OPA, 1 para Subtract - OPS).</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>• ZAda (1 bit): Seleciona o <em>tile</em> de destino do ZA (depende do tipo de dado).</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>• u0 , u1 (bits de tipo): Variam para selecionar o tipo de dado (e.g., INT8, BF16).</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>
**Exemplo:** **umopa** / **umops** (INT8 Outer Product) [3]
<table>
<tr>
<th><strong>Campo</strong></th>
<th><strong>u0</strong></th>
<th><strong>u1</strong></th>
<th><strong>S</strong></th>
<th><strong>Instrução</strong></th>
</tr>
<tr>
<td>Valores</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>UMOPA (Unsigned Multiply Outer Product Accumulate)</td>
</tr>
<tr>
<td>Valores</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>UMOPS (Unsigned Multiply Outer Product Subtract)</td>
</tr>
</table>
4.2. Codificação de Carga/Armazenamento do ZA (Save and Restore)
R e STR para o ZA array (usadas para context switching) têm
<table border="1">
<tr>
<th><strong>Bits</strong></th>
<th><strong>31-24</strong></th>
<th><strong>23</strong></th>
<th><strong>22-21</strong></th>
<th><strong>20-16</strong></th>
<th><strong>15-11</strong></th>
<th><strong>10-6</strong></th>
<th><strong>5-1</strong></th>
<th><strong>0</strong></th>
</tr>
<tr>
<td>Campo</td>
<td>11100001</td>
<td>0</td>
<td>00</td>
<td>00000</td>
<td>00000</td>
<td>00000</td>
<td>00000</td>
<td>op</td>
</tr>
<tr>
<td>Valores</td>
<td>11100001</td>
<td>0</td>
<td>00</td>
<td>00000</td>
<td>00000</td>
<td>00000</td>
<td>00000</td>
<td>op</td>
</tr>
</table>
* **op (1 bit):**
*   0: LDR (Load ZA array)
*   1: STR (Store ZA array)
5. Outras Estruturas e Instruções
*   **Instruções de Adição de Vetor ao Array:** ADDHA (Horizontal) e ADDVA (Vertical) adicionam um vetor SVE a linhas ou colunas específicas de um *tile* ZA [2].
*   **Instruções de Movimentação de Slice:** MOVA (alias de MOV) move um vetor SVE para um *slice* (fatiia) horizontal (H) ou vertical (V) de um *tile* ZA, ou vice-versa [2] [3].
    *   Exemplo: MOVA ZA0H.B[W0, #imm], P0/M, Z0.B (Move vetor para *slice* horizontal)
*   **Instrução de Zeroing:** ZERO {<mask>} zera um ou mais *tiles* ZA de 64 bits (ZA0.D a ZA7.D), conforme especificado pela máscara [2] [3].
Referências
[1] Arm Developer. *Part 1: Arm Scalable Matrix Extension (SME) Introduction.* [2] Arm Developer. *Part 2: Arm Scalable Matrix Extension (SME) Instructions.* [3] Arm Developer. *Arm Armv9-A A64 Instruction Set Architecture - SME encodings.*
Conceito 28: Custom Instructions ARM - User-defined opcodes, coprocessor interface, instruction space
**Tens Técnicos Encontrados:**
**Conceitos-Chave:** Custom Datapath Extension (CDE), Arm Custom Instructions (ACIs), Espaço de Codificação ISA do Coprocessador, Instruções CX1/CX2/CX3, Instruções VCX1/VCX2/VCX3, Interface de Alto Throughput (64 bits/ciclo), Exceção NOCP
Custom Instructions ARM (ACIs) / Custom Datapath Extension (CDE)
técnicos a seguir descreve as estruturas de hardware, formatos de instrução e protocolos da extensão Custom Instruction (CDE) para a arquitetura ARMv8-M, que suporta as Arm Custom Instructions (ACIs).
1. Estruturas de Hardware (Custom Datapath Extension - CDE)
A implementação de Custom Instructions é realizada através da **Custom Datapath Extension (CDE)**, que se integra ao processador (como o Cortex-M33) e compartilha a interface com a Unidade Lógica e Aritmética (ALU) padrão.
Módulos CDEE
CDE é composto por dois módulos principais, dependendo do conjunto de registradores que acessam:

1. **CDE (Core CDE):**
   * Executa instruções que acessam os **registradores de propósito geral (R0-R14)** e os flags **APSR_nzcv**.
   * É resetado e clockado da mesma forma que o núcleo do processador.
   * Incluído no domínio de energia do Core.

2. **FPCDE (Floating-Point CDE):**
   * Executa instruções que acessam os **registradores de ponto flutuante (S0-S31)**.
   * É resetado e clockado da mesma forma que a Floating-Point Unit (FPU).
   * Incluído no domínio de energia da FPU.
Fluxo de Instrução
O módulo de Custom Instructions é acionado por instruções pré-decodificadas e compartilha a interface com a ALU padrão. O fluxo de dados envolve:

*   Decodificador de Instrução Customizável Configurável
*   Datapath Customizado
*   Unidade de Writeback (Registro/Memória)
2. Formatos de Instrução (User-defined opcodes)
O espaço de codificação para as Custom Instructions é o **espaço de codificação da Arquitetura do Conjunto de Instruções do coprocessador** redefinido. As instruções são classificadas com base no número de registradores de origem e destino.
Classes de Instrução para Registradores de Propósito Geral (CDE)
trução para registradores de propósito geral (R0-R14) e flagg
<table>
<tr>
<th>Classe</th>
<th>Formato da Instrução</th>
<th>Tamanho do Imediato ( # &lt;imm&gt; )</th>
<th>Descrição</th>
</tr>
<tr>
<td><strong>CX1{A}</strong></td>
<td>CX1{A} {cond}, &lt;coproc&gt;, &lt;Rd&gt;, #&lt;imm&gt;</td>
<td>13 bits ( [12:0] )</td>
<td>1 Destino (32-bit), 0 Origem, Imediato.</td>
</tr>
<tr>
<td><strong>CX1D{A}</strong></td>
<td>CX1D{A} {cond}, &lt;coproc&gt;, &lt;Rd&gt;, &lt;Rd+1&gt;, #&lt;imm&gt;</td>
<td>13 bits ( [12:0] )</td>
<td>1 Destino (64-bit), 0 Origem, Imediato.</td>
</tr>
<tr>
<td><strong>CX2{A}</strong></td>
<td>CX2{A} {cond}, &lt;coproc&gt;, &lt;Rd&gt;, &lt;Rn&gt;, #&lt;imm&gt;</td>
<td>9 bits ( [8:0] )</td>
<td>1 Destino (32-bit), 1 Origem ( Rn ), Imediato.</td>
</tr>
<tr>
<td><strong>CX2D{A}</strong></td>
<td>CX2D{A} {cond}, &lt;coproc&gt;, &lt;Rd&gt;, &lt;Rd+1&gt;, &lt;Rn&gt;, # &lt;imm&gt;</td>
<td>9 bits ( [8:0] )</td>
<td>1 Destino (64-bit), 1 Origem ( Rn ), Imediato.</td>
</tr>
<tr>
<td><strong>CX3{A}</strong></td>
<td>CX3{A} {cond}, &lt;coproc&gt;, &lt;Rd&gt;, &lt;Rn&gt;, &lt;Rm&gt;, # &lt;imm&gt;</td>
<td>6 bits ( [5:0] )</td>
<td>1 Destino (32-bit), 2 Origens ( Rn , Rm ), Imediato.</td>
</tr>
<tr>
<td><strong>CX3D{A}</strong></td>
<td>CX3D{A} {cond}, &lt;coproc&gt;, &lt;Rd&gt;, &lt;Rd+1&gt;, &lt;Rn&gt;, &lt;Rm&gt;, #&lt;imm&gt;</td>
<td>6 bits ( [5:0] )</td>
<td>1 Destino (64-bit), 2 Origens ( Rn , Rm ), Imediato.</td>
</tr>
</table>
Campos Comuns:
<table>
<tr>
<td>• {A} : Indica uma variante de acumulação (Accumulation variant).</td>
</tr>
<tr>
<td>• {cond} : Código de condição opcional.</td>
</tr>
<tr>
<td>• &lt;coproc&gt; : O número do coprocessador (CP0-CP7).</td>
</tr>
<tr>
<td>• &lt;Rd&gt;, &lt;Rn&gt;, &lt;Rm&gt;: Registradores de propósito geral (R0-R14) ou APSR_nzcv.</td>
</tr>
</table>
Classes de Instrução para Registradores de Ponto Flutuante (FPCD)
As classes de instrução para registradores de ponto flutuante (S0-S31) são:
<table>
<tr>
<th>Classe</th>
<th>Formato da Instrução</th>
<th>Tamanho do Imediato ( # &lt;imm&gt; )</th>
<th>Descrição</th>
</tr>
<tr>
<td><strong>VCX1{A}</strong></td>
<td>VCX1{A} &lt;coproc&gt;, &lt;Sd&gt;, #&lt;imm&gt;</td>
<td>11 bits ( [10:0] )</td>
<td>1 Destino/Origem ( Sd ), Imediato.</td>
</tr>
<tr>
<td><strong>VCX2{A}</strong></td>
<td>VCX2{A} &lt;coproc&gt;, &lt;Sd&gt;, &lt;Sm&gt;, #&lt;imm&gt;</td>
<td>6 bits ( [5:0] )</td>
<td>1 Destino/Origem ( Sd ), 1 Origem ( Sm ), Imediato.</td>
</tr>
<tr>
<td><strong>VCX3{A}</strong></td>
<td>VCX3{A} &lt;coproc&gt;, &lt;Sd&gt;, &lt;Sn&gt;, &lt;Sm&gt;, # &lt;imm&gt;</td>
<td>3 bits ( [2:0] )</td>
<td>1 Destino/Origem ( Sd ), 2 Origens ( Sn , Sm ), Imediato.</td>
</tr>
</table>
**Campos Comuns:**
- `<Sd>`, `<Sn>`, `<Sm>`: Registradores de ponto flutuante de 32 bits (S0-S31).
3. Protocolo e Interface do Coprocessador
O mecanismo de Custom Instructions utiliza e redefine o espaço de codificação do coprocessador.
Interface Comunicação
Tratamento de Instruções Não Utilizadas
Para as regiões do espaço de codificação que não são utilizadas para Custom Instructions, o processador decodifica para a **interface do coprocessador** (se presente e habilitada) ou gera uma **exceção NOCP** (Non-Operation Coprocessor Exception), indicando que a instrução não pôde ser executada.
4. Algoritmos e Fórmulas
As Custom Instructions (ACIs) permitem a implementação de **algoritmos** definidos pelo usuário dentro do datapath customizado. Embora a função exata seja definida pelo implementador do hardware, a arquitetura define o **formato de chamada** (os opcodes definidos pelo usuário) e a **estrutura de dados** (registradores de 32 bits, 64 bits, ponto flutuante, imediatos) para esses algoritmos.
uras de Dados/Operação Imp
*   **Variante de Acumulação ( {A} )**: Implica uma operação onde o resultado é somado ao valor do registrador de destino ( Rd ou Sd ).
*   **Variante Dupla ( D)**: Implica o uso de dois registradores de 32 bits ( Rd e Rd+1 ) para formar um operando de 64 bits.
*   **Operação Condicional ( {cond} )**: Implica um algoritmo de execução condicional baseado nos flags APSR_nzcv.

**Restrições de Uso (Algoritmos de Exceção):** As restrições de uso definem o comportamento do processador (algoritmo de exceção) para casos arquiteturalmente não previsíveis (UNPREDICTABLE), resultando em uma exceção **UNDEFINED** ou **NOCP UsageFault**. Exemplos incluem:

*   Uso de Rd (destino) como R13 (Stack Pointer) em certas classes CDE.
*   Uso de registradores ímpares para o destino de 64 bits ( CXXD onde d é ímpar).
*   Execução de instruções CDE/FPCDE dentro de um bloco IT (If-Then) para variantes sem acumulação.
*   Tentativa de executar instruções FPCDE sem a FPU presente.
PARTE 2: PESQUISADORES E TEORIAS
Pesquisador 1: Sophie Wilson
**Itens Técnicos Encontrados:** 133
O trabalho de Sophie Wilson no design do conjunto de instruções (ISA) e da microarquitetura do **ARM1** (Acorn RISC Machine 1) estabeleceu os princípios técnicos fundamentais da arquitetura ARM. O foco principal foi a adesão estrita aos princípios **RISC (Reduced Instruction Set Computer)**, com inovações chave para otimizar o desempenho e a eficiência.
Princípios RISC e Conjunto de Instruções
*   **Arquitetura RISC:** O design do ARM1 é um projeto *clean-sheet* que adota o princípio RISC, resultando em um processador com um número significativamente menor de transistores (aproximadamente 25.000) em comparação com processadores CISC contemporâneos.
*   **Conjunto de Instruções ARMv1 (ISA):** O ISA é de **32 bits** com instruções de **tamanho fixo (4 bytes)**. Esta uniformidade simplifica o *fetch* e o *decode* das instruções.
*   **Execução Condicional por Instrução:** Uma característica central e inovadora do design. A execução condicional aplica-se a **quase todas as instruções**, e não apenas a *branches*. Isso permite que o compilador evite *branches* curtos e o *overhead* associado ao *pipeline flush* (esvaziamento do pipeline).
*   **Esquema de Endereçamento:** O ARM1 utilizava um espaço de endereçamento de **26 bits**, permitindo acesso a 64MB de memória.
Microarquitetura e Estruturas de Hardware
*   **Pipeline de 3 Estágios:** O ARM1 utiliza uma técnica de *pipelining* escalar de 3 estágios para melhorar o desempenho:
    1.  **Fetch (Busca):** Busca a instrução.
    2.  **Decode (Decodificação):** Decodifica a instrução e gera sinais de controle.
    3.  **Execute (Execução):** Executa a operação da ALU e acessa o registrador de arquivo.

*   **Barrel Shifter Integrado:** Uma unidade funcional crucial que permite que o segundo operando de uma instrução seja deslocado (*shift*) ou rotacionado (*rotate*) em 0 a 31 bits em um único ciclo de clock, antes de ser passado para a ALU.
    *   **Estrutura do Barrel Shifter:** Implementado como uma matriz de *crossbar* 32x32 de transistores, onde linhas de controle diagonais ativam as conexões apropriadas para realizar o deslocamento ou rotação.

*   **Unidade Lógica e Aritmética (ALU):** Realiza 16 operações diferentes, incluindo adição, subtração, AND lógico e OR lógica.

*   **Registro de Arquivo (Register File):** Contém 25 registradores de 32 bits (16 visíveis ao usuário e 9 para o modo supervisor). Possui duas portas de leitura e uma porta de escrita para a ALU.

*   **Decodificação de Instruções:** Utiliza ROMs de microcódigo (PLA) para decodificar cada instrução em até quatro micro-operações (*µOPs*), simplificando o controle.

*   **Mecanismo de Clock:** Opera com um *clock de duas fases* (Φ1 + Φ2), permitindo transferência *level-triggered* (acionada por nível) em vez de *edge-triggered* (acionada por borda).
Algoritmos e Otimizações
*   **Multi-Cycle Instruction:** Algoritmo de execução para instruções complexas (como STR - *store register*) que não podem ser concluídas em um único ciclo de *Execute*. A instrução passa pelo estágio *Execute múltiplas vezes (2 a 3 ciclos)*: o primeiro ciclo calcula o endereço efetivo, e o(s) ciclo(s) subsequente(s) realiza(m) a operação de memória.
*   **Cálculo do Program Counter (PC):** A microarquitetura mantém o PC apontando para a instrução sendo buscada. A instrução atualmente em execução está sempre em PC - 8 (dado que cada instrução tem 4 bytes).
*   **Otimização de Multiplicação por Software:** Devido à falta de hardware de multiplicação, o software utilizava o algoritmo *Shift-and-Add Multiplication* (Deslocamento e Adição).
    *   **Exemplo de Fórmula/Algoritmo:** A operação `var = x * 5;` era reescrita como `var = x + (x << 2);` para evitar a multiplicação direta, usando apenas adição e deslocamento (shift).
*   **Latência de Interrupção:** O design inclui capacidades de interrupção rápida (FIQ), com uma latência média de **sub-2 µs** e pior caso de sub-6 µs. A interrupção espera a instrução atual ser concluída (quando uma nova instrução começa a ser
isador 2: Steve Fur
**Itens Técnicos Encontrados:** 21
**ibuições:** Microarquitetura ARM1 (3-stage pipeline), Princípios RISC (instrução única), Micropipelining Assíncrono (AMU), colo Handshake 4-Fases, Princípio Matched Delay
Conteúdo Técnico - Contribuições de Steve Furberr
O trabalho de Steve Furber, tanto no desenvolvimento inicial da arquitetura ARM quanto na pesquisa sobre processadores assíncronos, estabeleceu conceitos técnicos fundamentais em microarquitetura e design de circuitos.
1. Microarquitetura ARM1 e Princípios RISC
o ARM1, desenvolvido sob a liderança de Furber e Sophie Wilson, é um exemplo de implementação de um processador (Reduced Instruction Set Computer).
Conceitos de Microarquitetura
*   **Pipeline de 3 Estágios:** O ARM1 utiliza um pipeline de instrução simples de três estágios: **Fetch (Busca)**, **Decode (Decodificação)** e **Execute (Execução)**.
*   **Arquitetura de Registradores:** Possui 25 registradores de 32 bits, com 16 visíveis ao usuário e 9 dedicados a modos de supervisor (User, Supervisor, IRQ, FIQ). O registrador **R15** funciona como o **Program Counter (PC)**.
*   **Decodificação Distribuída:** A decodificação da instrução é realizada por unidades separadas (Instruction Decode, Register Decode, ALU Decode, Shift Decode) que utilizam **ROMs de microcódigo (PLA)**, gerando até quatro sinais de **micro-operação (μOP)** por instrução.
*   **Clock de Duas Fases:** O design utiliza um clock externo de duas fases não sobrepostas ($\Phi_1 + \Phi_2$), permitindo a transferência de dados acionada por nível (*level-triggered*), simplificando o controle de tempo.
Algoritmos e Fórmulas (Conceitos)
*   **Endereço da Instrução em Execução:** Devido à estrutura do pipeline, o endereço da instrução atualmente em execução é dado por: $Endereço em Execução = PC - 8$ Onde PC é o endereço da instrução sendo buscada.
*   **Otimização de Multiplicação (Shift-and-Add):** Devido à ausência de hardware de multiplicação, a microarquitetura depende da técnica de **Shift-and-Add Multiplication** implementada via software. Um exemplo de otimização é: $var = x \times 5 \implies var = x + (x \ll 2)$
*   **Ciclo de Clock:** $Ciclo Completo = \Phi_1 + \Phi_2$
2. Processadores Assíncronos (AMULET)
O trabalho de Furber na Universidade de Manchester levou ao desenvolvimento da série de processadores assíncronos (Asynchronous Microprocessor at the University of Manchester), que implementavam o conjunto de instruções ARM global.
Conceitos de Microarquitetura Assíncrona
*   **Micropipelining:** O AMULET1 utiliza o conceito de **Micropipelining** de Ivan Sutherland, que consiste em uma sequência de estágios de processamento separados por **latches auto-temporizados (self-timed latches)**.
*   **Protocolo de Handshake de Quatro Fases (4-Phase Handshake):** O controle do fluxo de dados entre os estágios do pipeline é feito por um protocolo de handshake que utiliza dois sinais de controle (Request e Acknowledge) em quatro transições:
    1.  **Request® sobe:** $R:0 \rightarrow 1$ (Sinaliza dados válidos).
    2.  **Acknowledge (A) sobe:** $A:0 \rightarrow 1$ (Sinaliza consumo de dados).
    3.  **Request® desce:** $R:1 \rightarrow 0$ (Reset do Request).
4. **Acknowledge (A) desce**: $A: 1 \rightarrow 0$ (Reset do Acknowledge).

*   **Estilo Bundled Data**: O AMULET utiliza o estilo **Bundled Data** (Dados Agrupados), onde o sinal de controle (Request) é enviado junto com os dados.

## Algoritmos e Fórmulas (Princípios)

*   **Princípio de Atraso Casado (Matched Delay)**: Este é o princípio fundamental para a correção do design *bundled data*, garantindo que o sinal de controle chegue ao próximo estágio somente após os dados estarem estáveis: $Atraso\ do\ Sinal\ de\ Controle \geq Atraso\ de\ Propagação\ dos\ Dados\ (Caminho\ Mais\ Lento)$

*   **Elementos de Controle**: O design assíncrono utiliza células lógicas específicas, como os **Elementos de Exclusão Mútua (Mutual Exclusion - Mutex)**, para resolver conflitos de acesso e garantir a correta progressão do fluxo de dados sem a necessidade de um clock central.

*   **Custo de Área**: O custo de área para designs assíncronos *bundled data* é uma métrica técnica relevante, estimada em **10-20%** de sobrecarga em comparação com designs síncronos.

*   **Lógica de Latch**: O AMULET1 utilizou latches sensíveis a nível, exigindo conversores de duas para quatro fases no controlador de cada latch para se adaptar ao protocolo de 4 fases.
Contribuições Técnicas Consolidadas
| Conceito Técnico | Categoria | Aplicação |
|---|---|---|
| Pipeline de 3 Estágios | Microarquitetura | ARM1 (Fetch, Decode, Execute) |
| Shift-and-Add Multiplication | Algoritmo | Implementação de multiplicação em software (ARM1) |
| Micropipelining | Microarquitetura Assíncrona | AMULET (Base para o design sem clock) |
| Protocolo Handshake 4-Fases | Algoritmo/Controle | Controle de fluxo de dados entre estágios assíncronos |
| Princípio Matched Delay | Fórmula/Princípio | Correção de temporização em designs Bundled Data |
| Bundled Data | Estrutura de Hardware | Estilo de comunicação de dados assíncrona (AMULET) |
| Elementos Mutex | Estrutura de Hardware | Células para controle de acesso e resolução de conflitos assíncronos |
| Decodificação por PLA/µOP | Microarquitetura | Decodificação de instrução no ARM1 |
| Clock de Duas Fases (Φ₁ + Φ₂) | Estrutura de Hardware | Controle de tempo no ARM1 |
| Endereço em Execução = PC - 8 | Fórmula/Conceito | Gerenciamento do Program Counter no pipeline ARM1 |
| Latches Auto-Temporizados | Estrutura de Hardware | Separação de estágios no Micropipelining |
| Custo de Área Assíncrona (10-20%) | Métrica | Avaliação de eficiência de design Bundled Data |
| Conversores 2-para-4 Fases | Estrutura de Hardware | Lógica de controle de latch no AMULET1 |
| Sinal SEQ (Acesso Sequencial) | Estrutura de Hardware | Otimização de busca de instrução (Page-Mode DRAM) no ARM1 |
| Arquivo de Registradores com 2 Portas de Leitura | Estrutura de Hardware | Suporte à execução de instruções com dois operandos (ARM1) |
| Barrel Shifter Dedicado | Estrutura de Hardware | Otimização de operações de deslocamento no segundo operando (ARM1) |
| Instrução Única (RISC) | Conceito | Princípio fundamental do conjunto de instruções ARMv1 |
| Espaço de Endereço de 26 bits | Microarquitetura | Especificação de endereçamento do ARM1 |
| 4 Modos de Operação | Microarquitetura | Gerenciamento de exceções e privilégios (ARM1) |
| Taxa de Instrução (8 MIPS Pico) | Métrica | Desempenho máximo do ARM1 |
| Latches Sensíveis a Nível | Estrutura de Hardware | Tipo de latch usado no AMULET1 |
úmero total de conceitos, algoritmos e fórmulas técnicas id
*   **researcher_name:** Steve Furber
*   **technical_count:** 21
*   **contributions:** Microarquitetura ARM1 (3-stage pipeline), Princípios RISC (instrução única), Micropipelining Assíncrono (AMULET), Protocolo Handshake 4-Fases, Princípio Matched Delay
*   **technical_content:** (Conteúdo acima)
Pesquisador 3: Sophie Wilson
**Itens Técnicos Encontrados:** 11
**Contribuições:** Pipeline de 3 estágios, Execução Condicional em todas as instruções, Arquitetura Load-Store, Conjunto de 25 Registradores
O conteúdo técnico a seguir é extraído da arquitetura ARMv1 (Instruction Set Architecture - ISA) e da microarquitetura ARM1 (Acorn RISC Machine 1), que foram co-projetadas por Sophie Wilson. O foco é estritamente em algoritmos, fórmulas, estruturas de hardware, conceitos de microarquitetura e princípios RISC.
Princípios RISC e ISA ARMv1
<table>
<tr>
<th>Conceito Técnico</th>
<th>Descrição</th>
</tr>
<tr>
<td><strong>Arquitetura Load-Store</strong></td>
<td>Acesso à memória principal é restrito a instruções de <code>LOAD</code> (carregar) e <code>STORE</code> (armazenar). Todas as operações de dados (aritméticas/lógicas) operam exclusivamente em registradores.</td>
</tr>
<tr>
<td><strong>Instruções de Comprimento Fixo</strong></td>
<td>Todas as instruções possuem 32 bits de comprimento, o que simplifica o estágio de <em>Fetch</em> (busca) e <em>Decode</em> (decodificação) do pipeline.</td>
</tr>
<tr>
<td><strong>Execução Condicional (Predication)</strong></td>
<td>Quase todas as instruções contêm um campo de 4 bits para execução condicional. A instrução só é executada se os <em>Condition Flags</em> (N, Z, C, V) no <em>Program Status Register</em> (PSR) satisfizerem a condição especificada. Este é um princípio RISC para reduzir <em>branching</em> e o <em>overhead</em> do pipeline.</td>
</tr>
<tr>
<td><strong>Conjunto de Registradores</strong></td>
<td>O <em>Register File</em> (Arquivo de Registradores) físico e arquitetural é composto por 25 registradores de 32 bits. Destes, 16 são visíveis ao usuário e 9 são dedicados a modos de supervisor (Supervisor, IRQ, FIQ).</td>
</tr>
<tr>
<td><strong>Ausência de Multiplicação por Hardware</strong></td>
<td>O ARM1 original não possuía uma unidade de multiplicação por hardware. A multiplicação era realizada por software, utilizando o algoritmo de <strong>Multiplicação por Deslocamento e Adição</strong> (<em>Shift-and-Add Multiplication</em>).</td>
</tr>
</table>
**Exemplo Algorítmico de Multiplicação por Software:** Para calcular $var = x \times 5$, a operação é reescrita como: $Sva$ 2)onde\ll 2representaumdeslocamentológicode2bitsparaaesquerda(multiplicaçãopor$2^{\wedge}2=4$).
Estruturas de Hardware e Microarquitetura ARM1
| Estrutura/Conceito | Detalhe Técnico |
|---|---|
| **Pipeline** | Pipeline escalar de 3 estágios: **Fetch** (Busca), **Decode** (Decodificação) e **Execute** (Execução). |
| **Contador de Programa (PC)** | O registrador PC (R15) aponta para a instrução no estágio **Fetch**. A instrução atualmente em **Execute** está sempre em um endereço relativo de: $Endereço\_Execução = PC – 8$ |
| **Clock de Duas Fases** | O processador opera com um clock garantido de duas fases não sobrepostas ($\Phi_1$ e $\Phi_2$), permitindo transferências *level-triggered* em vez de *edge-triggering*. Um ciclo completo é $\Phi_1 + \Phi_2$. |
| **Otimização de Busca (SEQ)** | Um incrementador dedicado calcula o próximo endereço (PC + 4). O pino SEQ é ativado para indicar que a próxima instrução é sequencial, permitindo que o controlador de memória utilize *Page-Mode DRAM* para leituras consecutivas mais eficientes. |
| **Decodificação Modular** | O estágio Decode é implementado em unidades separadas: *Instruction Decode*, *Register Decode*, *ALU Decode* e *Shift Decode*. |
| **Barrel Shifter** | Unidade de hardware dedicada no caminho de dados para realizar deslocamentos e rotações de 32 bits em um único ciclo, essencial para a eficiência das operações de dados. |
| **Instruções Multi-Ciclo** | Instruções complexas, como STR (Store Register), utilizam o estágio Execute múltiplas vezes (2 a 3 ciclos) para completar a operação. Exemplo: 1º ciclo de Execute calcula o endereço; 2º ciclo realiza o armazenamento de dados. |
| **Arquivo de Registradores** | Possui duas portas de leitura (Port 0 e Port 1) para os operandos da ALU e uma porta de escrita para o write-back do resultado. |
| **Implementação de Controle** | O controle é implementado com microcode em ROMs (*Programmable Logic Array - PLA*), onde cada instrução é decodificada em até quatro $\mu OPs$ (micro-operações). |
| **Transistores** | O die do ARM1 continha aproximadamente 24.800 transistores e cerca de 6.000 portas lógicas. |
ador 4: Jamie Urqu
**Itens Técnicos Encontrados: 17**

**Contribuições:** Arquitetura big.LITTLE, Global Task Scheduling (GTS), Coerência de Cache AMBA ACE
nteúdo Técnico: Arquitetura ARM big.LITTLE e Princípios
**RISC**
A arquitetura **ARM big.LITTLE** representa uma solução de **processamento heterogêneo** que visa otimizar o consumo de energia sem sacrificar o desempenho de pico. O conceito central reside na combinação de dois tipos de *clusters* de processadores: os núcleos “**big**” (como o Cortex-A15 ou Cortex-A57), projetados para alto desempenho, e os núcleos “**LITTLE**” (como o Cortex-A7 ou Cortex-A53), otimizados para máxima eficiência energética. É fundamental que ambos os tipos de núcleo suportem a mesma **Arquitetura de Conjunto de Instruções (ISA)**, como o ARMv7-A, garantindo que o mesmo código possa ser executado de forma transparente em qualquer um dos *clusters*.
A distinção entre os núcleos reside em suas **microarquiteturas** internas. Os núcleos *big* são caracterizados por um *pipeline* mais complexo e maior capacidade de execução paralela de instruções, visando a máxima capacidade de computação. Em contraste, os núcleos *LITTLE* empregam um *pipeline* relativamente simples, resultando em menor desempenho, mas com uma eficiência energética significativamente superior.
Princípios RISC
A arquitetura ARM é inerentemente baseada nos princípios do RISC (Reduced Instruction Set Computing). Este paradigma de design de processador se baseia na premissa de que instruções simplificadas podem ser executadas de forma mais rápida e eficiente. Uma característica chave do RISC é a utilização de um **conjunto de registradores aprimorado**, o que facilita o aumento do paralelismo interno e, consequentemente, melhora o desempenho geral do processador.
turias de Hardware para Coerência
A viabilidade da arquitetura big.LITTLE depende criticamente da coerência de cache entre os clusters big e LITTLE. O hardware responsável por essa interconexão é o **CoreLink™ Cache Coherent Interconnect (CCI-400)**, que atua como um tecido do sistema para permitir a transferência transparente e performática de dados entre os processadores.

O protocolo que garante essa coerência no nível do barramento é o **AMBA AXI Coherency Extensions (ACE)**, uma extensão do protocolo AMBA AXI. O ACE adiciona canais específicos para gerenciar a coerência, como detalhado na tabela a seguir:
| Canal ACE | Função | Exemplo de Uso (Leitura LITTLE para BIG) |
|---|---|---|
| RADDR | Solicitação de Endereço de Leitura Coerente | Cluster LITTLE emite a solicitação. |
| ACADDR | Endereço de Coerência (Snoop) | CCI-400 usa para investigar o cache do cluster BIG. |
| CRRESP | Resposta de Coerência | Cluster BIG reporta a disponibilidade dos dados. |
| CDATA | Dados de Coerência | Cluster BIG coloca os dados solicitados. |
| RDATA | Dados de Leitura | CCI-400 move os dados para o cluster LITTLE. |
disso, o **CoreLink GIC-400** (Generic Interrupt Controller) é responsável por fornecer a distribuição de interrupções de forma dinamicamente configurável para todos os núcleos do sistema.
Le Agendamento dei
O gerenciamento de tarefas em um sistema big.LITTLE evoluiu de modelos de migração simples para o **Global Task Scheduling (GTS)**, também conhecido como **big.LITTLE MP (Heterogeneous Multi-Processing)**. Este modelo é o mais sofisticado, permitindo que todos os núcleos operem simultaneamente.

O algoritmo GTS, implementado no *scheduler* do sistema operacional (como o Linux com *patches* big.LITTLE MP), utiliza um mecanismo baseado em heurísticas e dados estatísticos para a alocação ideal de *threads*.
Algoritmo de Alocação (GTS)
O cerne do algoritmo reside no **Rastreamento de Carga (Load Tracking)**, onde a carga de cada *thread* é calcula- **média ponderada histórica** (*Historical Weighted Average*) ao longo do tempo de execução. Essa ponderação atividade recente da tarefa tenha maior influência na decisão de agendamento.
atividade recente da tarefa tenha maior influência na decisão de agendamento.

A migração de tarefas entre os clusters é governada por dois **Limiares de Migração** configuráveis:

1.  **Up Migration Threshold (Limiar de Migração para Cima):** Se a carga rastreada de uma thread em um núcleo LITTLE exceder este limiar, ela se torna elegível para migração para um núcleo BIG.
2.  **Down Migration Threshold (Limiar de Migração para Baixo):** Se a carga rastreada de uma thread em um núcleo BIG cair abaixo deste limiar, ela se torna elegível para migração para um núcleo LITTLE.

Adicionalmente, a **métrica de carga** é ajustada com base na frequência atual do processador, permitindo que o GTS e o DVFS (Dynamic Voltage and Frequency Scaling) trabalhem em harmonia. Uma tarefa em um processador rodando a meia velocidade acumulará carga rastreada a metade da taxa de um processador rodando a velocidade total
Técnicas de Migração
algoritmo GTS emprega diversas técnicas para gerenciar a afinidade e a migração de *threads* em tempo real:
| Técnica de Migração | Descrição |
|---|---|
| Fork Migration | Usada para novas *threads* sem histórico de carga. O padrão é iniciar em um núcleo BIG, com a expectativa de que *threads* leves migrem rapidamente para um núcleo LITTLE. |
|---|---|
| Wake Migration | Ocorre quando uma *thread* inativa se torna pronta para execução. O *scheduler* usa o histórico de carga rastreada (que não é atualizado durante o sono da *thread*) para decidir o *cluster* de destino. |
| Forced Migration | Lida com *threads* de longa duração que não entram em estado de sono. O *scheduler* verifica periodicamente a carga rastreada em núcleos LITTLE e força a transferência para um núcleo BIG se o limiar for excedido. |
| Idle Pull Migration | Ocorre quando um núcleo BIG fica ocioso. Ele verifica os núcleos LITTLE para “puxar” tarefas com carga rastreada acima do limiar de migração para cima, otimizando o uso do núcleo BIG ativo. |
| Offload Migration | Técnica de gerenciamento de afinidade de *threads* (mentcionada, mas sem detalhes de implementação). |
Pesquisador 5: Mike Muller
**Itens Técnicos Encontrados: 16**

**Contribuições:** AArch64 (ISA 64-bit), TrustZone, Monitor Exclusivo, Enderecamento Efetivo, Princípios RISC-V
**Fonte:** ARM Architecture Reference Manual ARMv8, for ARMv8-A architecture profile (Issue A.a, 2013)
os RISC e Arquitetura
arquitetura ARMv8-A, com seu estado de execução AArch64, mantém os princípios RISC (Reduced Instruction Set Computin

em foco em:

1.  **Conjunto de Instruções Reduzido e Fixo:** O conjunto de instruções A64 utiliza um formato de instrução de **32 bits** de tamanho fixo.

2.  **Modelo Load/Store:** As operações de processamento de dados são realizadas em registradores, e o acesso à memória é feito exclusivamente por instruções de **Load** (carregar) e **Store** (armazenar).

3.  **Registradores de Propósito Geral:** AArch64 define **31 registradores de propósito geral (X0-X30)** de 64 bits. O registrador X31 é usado como ponteiro de pilha (SP) ou registrador zero (XZR), dependendo do contexto.
Estruturas de Hardware e Microarquitetura (Conceitos)
*   **Espaço de Endereçamento (Address Space):** O espaço de endereçamento virtual pode ser de 48 bits, permitindo endereços de até $2^{48}$ bytes.
*   **Hierarquia de Cache:** O modelo suporta hierarquias de cache multinível (L1, L2, L3) e define operações de **Cache Maintenance** (manutenção de cache) para garantir a coerência.
*   **Atomicidade:** A arquitetura define regras estritas para garantir a **atomicidade** das operações de memória, essenciais para sincronização em sistemas multi-core.
*   **Ordenação de Memória (Memory Ordering):** O modelo de consistência de memória é definido para garantir que as operações de memória (Loads e Stores) sejam observadas em uma ordem previsível pelos diferentes cores do processador.
Conjunto de Instruções A64 (AArch64 Instruction Set)
O conjunto de instruções A64 é dividido em classes, incluindo:
*   **Branches, Exception Generating, and System Instructions:**
    *   **Branches Condicionais (B.cond):** A execução é baseada no estado dos **Condition Flags** (N, Z, C, V) no registrador PSTATE.
    *   **Branches Incondicionais (B, BL, BR):** Usados para controle de fluxo.
    *   **System Instructions:** Incluem instruções para acesso a registradores de controle e manutenção de cache (ex: DC IVAC, IC IALLU).
*   **Loads and Stores:**
    *   **Load/Store Register (LDR/STR):** Operações básicas de acesso à memória.
    *   **Load/Store Pair (LDP/STP):** Otimização para carregar/armazenar dois registradores em uma única instrução.
    *   **Load/Store Exclusive (LDXR/STXR):** Usadas para implementar primitivas de sincronização (semáforos, mutexes) baseadas no algoritmo de **Monitor Exclusivo**.
*   **Data Processing - Immediate:** Operações lógicas e aritméticas com operandos imediatos.
*   **Data Processing - Register:** Operações lógicas e aritméticas entre registradores.
*   **SIMD and Floating-point:** Suporte para operações vetoriais e de ponto flutuante de precisão simples (32 bits) e dupla (64 bits).
os e Fórmulas (Conceitos)
# Sincronização e Semáforos (Synchronization and Semaphores)

O mecanismo de **Monitor Exclusivo** é fundamental para a sincronização e é implementado pelas instruções `LDXR` (Load Exclusive Register) e `STXR` (Store Exclusive Register).

## Algoritmo de Sincronização (Conceito de Loop de Tentativa-e-Erro):

1.  **Load Exclusive:** O core executa `LDXR` para carregar um valor de memória e define um estado de monitor exclusivo para o endereço.
2.  **Modificação:** O core realiza operações de modificação no valor carregado.
3.  **Store Exclusive:** O core executa `STXR` para tentar armazenar o novo valor.
4.  **Verificação:** Se o `STXR` for bem-sucedido (o monitor exclusivo não foi quebrado por outro core), a operação atômica é concluída. Se falhar, o core deve retornar ao passo 1.
Endereçamento (Address Generation)
O cálculo do endereço efetivo para operações de Load/Store é um conceito central.

**Fórmula Conceitual de Endereçamento Baseado em Registrador:**
Endereço Efetivo = Valor do Registrador Base +
Onde o **Offset** pode ser um valor imediato ou o valor de outro registrador (endereçamento indexado).
PSTATE (Processor State)
O registrador de estado do processador (PSTATE) contém os **Condition Flags** (N, Z, C, V) que são o resultado de operações aritméticas e lógicas.

*   **N (Negative):** Bit mais significativo do resultado é 1.
*   **Z (Zero):** Resultado é zero.
*   **C (Carry):** Ocorreu um *carry* ou *borrow* na operação.
*   **V (Overflow):** Ocorreu um *overflow* na operação.
Contribuições de Mike Muller (Contexto)
mbora o manual de referência não mencione Mike Muller diretamente, ele foi o CTO da ARM durante o desen-
ançamento da arquitetura ARMv8-A (AArch64), que introduziu o conjunto de instruções de 64 bits e o modelo
rustZone. O conteúdo técnico acima representa a arquitetura cuja evolução foi supervisionada por ele.

**Conceitos Chave da Evolução da ISA (ARMv8-A):**

*   **AArch64:** Transição para 64 bits, mantendo a filosofia RISC.
*   **TrustZone:** Mecanismo de segurança que particiona o hardware e software em mundos **Secure** e **Non-secure**.
*   **Monitor Exclusivo:** Primitiva de hardware para sincronização multi-core.
*   **SIMD Avançado:** Extensões para processamento vetorial (NEON).
*   **Dark Silicon:** Conceito de microarquitetura para lidar com o desafio de energia em chips densos.
*   **Computação Heterogênea (big.LITTLE):** Estratégia de microarquitetura para eficiência energética.
sador 6: Simon Segg
Itens Técnicos Encontrados: 11
**Contribuições:** Arquitetura Thumb, Reutilização de Cadeia de Varredura JTAG, Microarquitetura ARM7TDMI, Mi-
ARM9, Otimização de Consumo de Energia RISC
Conteúdo Técnico do Trabalho de Simon Segars na ARM
1. Patente US5757819A: Integrated Circuit Test Controller (1998)
**Conceito Principal:** Reutilização de uma porção da cadeia de varredura de teste serial (serial test scan chain), em conformidade com o padrão **JTAG (IEEE Standard 1149.1-1990)**, para carregar e serializar dados de identificação do circuito integrado (**IDCODE**), eliminando a necessidade de um **registrador de deslocamento (shift register)** dedicado.

**Estruturas de Hardware/Microarquitetura:** A invenção elimina o registrador de deslocamento dedicado (shift register 16), que tipicamente representaria 30% da área do controlador da cadeia de varredura (scan chain controller 8), resultando em uma significativa **redução de área** no circuito integrado. O princípio se baseia na reutilização de componentes existentes:

*   **Serial Test Scan Chain (6):** Composta por células de varredura que podem aplicar, capturar ou ser transparentes a sinais.
*   **Scan Chain Controller (8):** Controla a operação de teste via **Test Access Port (TAP)**.
*   **Multiplexer (14):** Usado para conectar diferentes pontos do circuito integrado à linha de saída de dados de teste (**TDO**).

**Algoritmo/Seqüência de Estados (JTAG/TAP State Machine):** A operação de IDCODE segue uma seqüência de estados da máquina de estados (dentro do scan chain controller 8), conforme a Tabela 1 da patente:
<table>
<tr>
<th>Ação/Estado</th>
<th>Bits de Modo (TMS)</th>
<th>Bits de Dados (TDI)</th>
<th>Descrição</th>
</tr>
<tr>
<td>Início em Test-Logic-Reset</td>
<td>N/A</td>
<td>N/A</td>
<td>Estado inicial.</td>
</tr>
<tr>
<td>Ciclar em Shift-IR</td>
<td><code>0000</code> (4 vezes)</td>
<td><code>1110</code></td>
<td>Recebe a instrução <code>IDCODE</code>.</td>
</tr>
<tr>
<td>Mover para Capture-DR</td>
<td><code>10</code></td>
<td><code>**</code></td>
<td><strong>Carrega</strong> a porção 20 com os 32 bits de IDCODE e <strong>chaveia</strong> o multiplexador de entrada.</td>
</tr>
<tr>
<td>Ciclar em Shift-DR</td>
<td><code>32 × 0</code></td>
<td><code>32 × *</code></td>
<td><strong>Desloca</strong> os 32 bits de IDCODE para fora via TDO.</td>
</tr>
</table>
O mecanismo permite o **Encadeamento (Chaining)** de múltiplos ICs, onde um multiplexador de entrada (input multiplexer 22) conecta a porção de saída de dados de um IC ao TDI do próximo IC, permitindo a recuperação de IDCODEs de vários circuitos em uma única operação.
2. Arquitetura Thumb e Microarquitetura ARM7TDMI (1995-1997)
**Conceito Principal:** Introdução da arquitetura **Thumb** para resolver o problema de **densidade de código** em sistemas embarcados de alto desempenho e baixo custo, mantendo a performance RISC de 32 bits.

**Princípios RISC/Microarquitetura:**

*   **Conjunto de Instruções Híbrido:** O processador ARM7TDMI opera em dois estados:
    *   **Estado ARM (32 bits):** Conjunto de instruções RISC completo de 32 bits.
    *   **Estado Thumb (16 bits):** Conjunto de instruções **comprimido** de 16 bits.
*   **Desempenho:** O código Thumb é **descomprimido** para instruções ARM de 32 bits no **pipeline de instrução** antes da execução. A maioria das instruções Thumb é mapeada diretamente para uma única instrução ARM de 32 bits, mantendo o desempenho comparável ao código ARM de 32 bits.
*   **Microarquitetura ARM7TDMI:**
    *   **Pipeline:** Utiliza um **pipeline de 3 estágios** (Fetch, Decode, Execute), o que contribui para um **baixo consumo de energia**.
    *   **Decodificador Thumb:** Um decodificador adicional é integrado ao pipeline para expandir as instruções Thumb de 16 bits para as instruções ARM de 32 bits correspondentes.
*   **Otimização de Consumo de Energia RISC:** A redução no tamanho do código Thumb leva a **menos acessos à memória** (menor tráfego no barramento de endereços e dados), mitigando a desvantagem de energia dos processadores RISC de 32 bits que, de outra forma, forçariam um acesso à memória de 32 bits a cada ciclo.
Evolução para a Microarquitetura ARM
**Conceito Principal:** Evolução microarquitetural do ARM7 para o ARM9, focando no *trade-off* entre baixo consumo de energia e alto desempenho para atingir mais de 150 MIPS.

**Estruturas de Hardware/Microarquitetura (ARM9TDMI e ARM940T):**
*   **Pipeline de 5 Estágios:** O ARM9 introduz um pipeline de 5 estágios (Fetch, Decode, Execute, Memory, Write-back), em contraste com o pipeline de 3 estágios do ARM7. Este aprofundamento do pipeline é um princípio RISC para aumentar o paralelismo de instrução (Instruction Level Parallelism - ILP) e a frequência de clock.
*   **Arquitetura Harvard Modificada:** O ARM9 adota uma arquitetura Harvard modificada, separando as memórias de instrução e dados, permitindo acessos simultâneos e melhorando o desempenho, em contraste com a arquitetura Von Neumann do ARM7TDMI.
*   **Cache e MMU (ARM940T):** O ARM940T inclui Cache de Instrução e Dados Separados e uma Memory Management Unit (MMU) para suporte a sistemas operacionais complexos, estruturas essenciais para microprocessadores de alto desempenho.
Pesquisador 7: John L. Hennessy
**Itens Técnicos Encontrados: 12**
**Contribuições:** Pipeline de 5 estágios, Arquitetura MIPS RISC, Fórmulas de Desempenho Quantitativo, Lei de Amdahl, Potência Dinâmica CMOS
# Conteúdo Técnico Puro do Trabalho de John Hennessy (RISC e Arquitetura Quantitativa)
rmulas Fundamentais de Desempenh
O desempenho de um processador é quantificado pela fórmula do **Tempo de CPU** (CPU Time), que é o tempo real gasto pelo processador na execução de um programa.

1.  **Fórmula do Tempo de CPU (CPU Time):** $Tempo\ de\ CPU = Contagem\ de\ Instruções \times CPI \times Tempo\ de\ Ciclo\ de\ Clock$

    Onde:

    *   **Contagem de Instruções** (Instruction Count, IC) é o número de instruções executadas pelo programa.
    *   **CPI** (Cycles Per Instruction) é o número médio de ciclos de clock necessários para executar uma instrução.
2. **Fórmula do CPI (Cycles Per Instruction):** $CPI = \frac{\text{Ciclos de Clock da CPU}}{\text{Contagem de Instruções}}$

$OCPi\text{também pode ser calculado como} \frac{\text{as somas ponderadas dos CPIs decada classe de instrução}}{\text{Frequência}_i}) \text{ onde } \text{CPI}_i \text{ para a classe de instrução } i, e \text{ frequência com que a classe de instrução } i \text{ é usada.}$

3. **Lei de Amdahl (Amdahl's Law):** A lei de Amdahl define o ganho de velocidade (Speedup) teórico máximo que pode ser alcançado ao melhorar uma parte de um sistema. $Ganho de Velocidade Geral = \frac{1}{(1 - \text{Fração Melhorada}) + \frac{\text{Fração Melhorada}}{\text{Ganho de Velocidade da Melhoria}}}$

Onde:

*   **Fração Melhorada** (Fraction Enhanced) é a fração do tempo de execução original que pode ser afetada pela melhoria.
*   **Ganho de Velocidade da Melhoria** (Speedup Enhanced) é o ganho de velocidade da parte melhorada.
de Microarquitetura e Princípios RISC
O projeto MIPS (Microprocessor without Interlocked Pipelined Stages), liderado por Hennessy, é um exemplo de arquitetura RISC (Reduced Instruction Set Computer).
1. **Princípio RISC Central (MIPS):** A filosofia central do MIPS é simplificar o conjunto de instruções (ISA) para permitir uma implementação de pipeline eficiente e de alta frequência. O nome MIPS reflete a eliminação de estágios de pipeline interligados por hardware, delegando a resolução de *hazards* (riscos) ao compilador.

2. **Pipeline Clássico de 5 Estágios (MIPS):** A microarquitetura MIPS é baseada em um pipeline de 5 estágios, projetado para que cada estágio leve um ciclo de clock para ser concluído:

   *   **IF (Instruction Fetch):** Busca da instrução na memória.
   *   **ID (Instruction Decode):** Decodificação da instrução e leitura dos registradores.
   *   **EX (Execute):** Execução da operação (ALU) ou cálculo de endereço.
   *   **MEM (Memory Access):** Acesso à memória (leitura ou escrita de dados).
   *   **WB (Write Back):** Escrita do resultado de volta no registrador.

3. **Princípios de Design da ISA RISC (MIPS):**

   *   **Instruções de Tamanho Fixo (32 bits):** Simplifica a busca e a decodificação no estágio IF/ID.
   *   **Formato de Instrução Simples e Consistente:** Minimiza a lógica de decodificação.
   *   **Arquitetura Load/Store:** Apenas as instruções Load e Store acessam a memória de dados; todas as outras operações são realizadas em registradores.
   *   **Grande Número de Registradores de Propósito Geral:** Facilita o trabalho do compilador e reduz o número de acessos à memória.
as de Potência e Er
eficiência energética é um conceito quantitativo fundamental na arquitetura de computadores moderna.

1. **Fórmula da Potência Dinâmica (Dynamic Power):** A potência consumida devido à comutação de transistores (principal componente da potência em CMOS): $P_{dinâmica} = \alpha \times C \times V^2 \times f$ Onde:
   * $\alpha$ (Activity Factor) é a fração de transistores que comutam em um ciclo de clock.
   * $C$ é a capacitância de carga.
   * $V$ é a tensão de alimentação.
   * $f$ é a frequência do clock.

2. **Fórmula da Energia (Energy):** A energia consumida por operação é: $Energia \propto C \times V^2$ A redução da tensão (V$)$ tem um impacto quadrático na redução da potência e da energia, sendo a técnica mais eficaz para melhoria da eficiência energética.
3. **Fórmula da Potência Estática (Static Power):** A potência consumida devido ao vazamento (leakage) de corrente, mesmo quando o transistor está desligado: $P_{\text{estática}} = V \times I_{\text{vazamento}}$ onde $I_{\text{vazamento}}$ é a corrente de vazamento.

4. **Métrica de Desempenho/Potência:** A métrica de **Energia-Atraso** (Energy-Delay Product, EDP) é usada para avaliar o *trade-off* entre desempenho e consumo de energia: $EDP = \text{Energia} \times \text{Atraso}$ Onde Atraso é o tempo de execução.

5. **Princípio de Design Quantitativo:** A arquitetura de computadores deve ser guiada por **medições, métricas e análise quantitativa** (por exemplo, uso de *benchmarks* como SPEC) em vez de decisões puramente qualitativas.

6. **Conceito de Risco de Pipeline (Hazard):**
*   **Risco Estrutural:** Dois estágios tentam usar o mesmo recurso de hardware no mesmo ciclo.
*   **Risco de Dados:** Uma instrução tenta usar o resultado de uma instrução anterior que ainda não foi escrito de volta (resolvido por *forwarding* ou *stalling*).
*   **Risco de Controle:** Decisão de *branch* (desvio) não resolvida a tempo (resolvido por *branch prediction* ou *branch delay slot*).
Pesquisador 8: David Patterson
**Itens Técnicos Encontrados:** 255
Fixo, Registrador R0 como Zero

O trabalho seminal sobre o Berkeley RISC I, liderado por David Patterson, estabeleceu os princípios fundamentais da arquitetura de Conjunto de Instruções Reduzido (RISC). O design é caracterizado por um conjunto de restrições arquitetônicas rigorosas, visando a máxima eficiência de hardware e a otimização para linguagens de alto nível.
Princípios e Arquitetura Base
A arquitetura RISC I opera sob o princípio de **execução de uma instrução por ciclo** para a maioria das operações, garantindo um alto *throughput* efetivo. Todas as instruções possuem um **tamanho fixo de 32 bits**, simplificando o *hardware* de controle. O modelo segue estritamente a **Arquitetura Load-Store**, onde apenas as instruções LOAD e STORE acessam a memória, enquanto todas as outras operações ocorrem exclusivamente entre registradores.

O tempo de execução de um ciclo de máquina ($T_{ciclo}$) é definido pela soma dos tempos de acesso ao registrador e da operação da Unidade Lógica Aritmética (ALU):
O processador utiliza 32 registradores de 32 bits, sendo o **Registrador 0 (R0)** fixado com o valor zero, o que permite a síntese de diversos modos de endereçamento e operações. O único modo de endereçamento permitido para acesso à memória é o de **índice mais deslocamento**, cuja fórmula é:
Formato de Instrução de 32 Bits
O formato de instrução de 32 bits para operações de registrador para registrador é dividido em campos específicos operação e os operandos.
<table>
<tr>
<th>Campo</th>
<th>Tamanho (bits)</th>
<th>Função Técnica</th>
</tr>
<tr>
<td><strong>DEST</strong></td>
<td>5</td>
<td>Seleciona o registrador de destino (R0 a R31).</td>
</tr>
<tr>
<td><strong>SOURCE1</strong></td>
<td>5</td>
<td>Especifica o primeiro registrador operando.</td>
</tr>
<tr>
<td><strong>SOURCE2</strong></td>
<td>5</td>
<td>Especifica o segundo registrador operando (se IMM=0).</td>
</tr>
<tr>
<td><strong>IMM</strong></td>
<td>1</td>
<td>Indica se SOURCE2 é um registrador (0) ou um valor imediato (1).</td>
</tr>
<tr>
<td><strong>SCC</strong></td>
<td>1</td>
<td>Determina se os códigos de condição são definidos.</td>
</tr>
<tr>
<td><strong>Constante</strong></td>
<td>13</td>
<td>Valor imediato com sinal estendido (se IMM=1).</td>
</tr>
</table>
Janelas de Registradores Sobrepostas (Overlapped Register Windows)
ceito de **Janelas de Registradores Sobrepistas** é a principal inovação do RISC I para otimizar chamadas e retornos, que são operações de alto custo em linguagens de alto nível.
O conjunto de registradores é dividido em:
1. **Registradores Globais (R0 a R9):** Acessíveis por todos os procedimentos e não são salvos/restaurados em chamadas.
2. **Registradores de Janela (R10 a R31):** Alocados para cada procedimento e divididos em três seções:
<table>
<tr>
<th>Seção</th>
<th>Registradores</th>
<th>Função</th>
<th>Tamanho (Registradores)</th>
</tr>
<tr>
<td><strong>HIGH</strong></td>
<td>R26 a R31</td>
<td>Parâmetros de entrada (recebidos do chamador).</td>
<td>6</td>
</tr>
<tr>
<td><strong>LOCAL</strong></td>
<td>R16 a R25</td>
<td>Armazenamento local escalar.</td>
<td>10</td>
</tr>
<tr>
<td><strong>LOW</strong></td>
<td>R10 a R15</td>
<td>Parâmetros de saída (passados para o chamado).</td>
<td>6</td>
</tr>
</table>
O **Mecanismo de Sobreposição** garante que os registradores **LOW** do procedimento chamador se tornem os registradores **HIGH** do procedimento chamado, permitindo a passagem de parâmetros diretamente via *hardware* sem acesso à memória.

O gerenciamento de **Overflow/Underflow** (quando o número de chamadas excede o número de janelas disponíveis) é tratado por uma rotina de *software* que salva ou restaura o contexto na memória, utilizando uma pilha de *overflow* separada. A frequência de *overflow* é baixa (estimada em menos de 1% das chamadas com 4 a 8 bancos de registradores).
# Conceitos de Microarquitetura
A microarquitetura do RISC I é simplificada pela natureza do conjunto de instruções. A **Unidade de Controle** é mais simples, eliminando a necessidade de microcódigo. A **Unidade de Lógica Aritmética (ALU)** realiza operações aritméticas, lógicas e de deslocamento. A **Unidade de Load/Store** é uma unidade dedicada que requer 2 ciclos de CPU para mover dados entre registradores e memória. O design foi otimizado para implementação em um único chip **VLSI**, minimizando o atraso da transferência de dados através dos limites do chip.
Pesquisador 9: David Ditzel
**Itens Técnicos Encontrados:** 16
técnicos do Trabalho de David
Princípios Fundamentais da Arquitetura RISC (Patterson & Ditz)
Os princípios técnicos que fundamentaram a arquitetura RISC, essenciais para o design de processadores modernos, incluindo o ARM, focam na simplificação do conjunto de instruções para otimizar a implementação em hardware e o desempenho do pipeline.
Conceitos de Microarquitetura e Princípios RISC
1. **Instruções Simples e Uniformes**: O conjunto de instruções é reduzido e simplificado, com formatos de instrução uniformes e de tamanho fixo. Isso permite uma lógica de controle implementada em hardware (**Hardwired Control**) em vez de microcódigo complexo, acelerando a execução.

2. **Arquitetura Load/Store**: Apenas as instruções de **LOAD** e **STORE** acessam a memória. Todas as outras operações (aritméticas, lógicas) são realizadas exclusivamente em registradores, minimizando o tráfego de dados para a memória principal.

3. **Pipeline Eficiente**: A simplicidade das instruções permite que a maioria delas seja executada em um único ciclo de clock (CPI próximo de 1), facilitando a implementação de um pipeline de instruções de alta eficiência.

4. **Ênfase no Compilador**: A complexidade é transferida do hardware para o software, exigindo que o compilador realize otimizações agressivas para o conjunto de instruções simples.
O princípio de design RISC é guiado pela equação fundamental de desempenho da CPU, que busca minimizar execução:

Tempo de Execução = Instruções × CPI × Tempo de Ciclo
Onde:
*   Instruções é o número de instruções executadas.
*   CPI (Cycles Per Instruction) é o número médio de ciclos de clock por instrução.
*   Tempo de Ciclo é a duração de um ciclo de clock.

O RISC foca em reduzir o **CPI** e o **Tempo de Ciclo** (devido ao hardware mais simples), aceitando um possível aumento no número de Instruções em comparação com arquiteturas CISC.
Algoritmo Branch Folding (Microprocessador CRISP)
O microprocessador CRISP (AT&T Bell Laboratories) introduziu o conceito de **Branch Folding** para resolver o problema (penalty) de desvio em pipelines de instruções.

**Algoritmo e Conceitos de Microarquitetura:**
1. **Branch Folding**: Técnica de hardware e software que “dobra” as instruções de desvio (branch instructions) em outras instruções, permitindo que o custo de execução de muitos desvios seja efetivamente reduzido a zero (**Zero Branch Delay**).

2. **Redução do Atraso de Desvio**: O algoritmo elimina a quebra do pipeline de instruções causada por desvios, mantendo o pipeline cheio e reduzindo o número aparente de instruções que o pipeline precisa processar.

3. **Previsão Estática de Desvio**: As instruções de desvio condicional incluem um bit de previsão estática, definido pelo compilador, que fornece uma dica ao hardware sobre a probabilidade de o desvio ocorrer.

4. **Cache de Instruções Altamente Decodificado**: O CRISP utiliza um cache de instruções que pré-decodifica as instruções, permitindo que operações complexas (estilo memória-para-memória) sejam frequentemente executadas em um único ciclo.
O trabalho de Ditzel na Transmeta resultou em uma arquitetura híbrida de hardware-software focada em baixo consumo de energia, utilizando um núcleo VLIW e o **Code Morphing Software (CMS)**.

**Estruturas de Hardware e Algoritmos (Crusoe):**

1.  **Arquitetura VLIW (Very Long Instruction Word):** O núcleo de hardware é uma CPU VLIW capaz de executar múltiplas operações (até quatro) em um único ciclo de clock. A ISA nativa do núcleo é VLIW e não se assemelha à ISA x86.
2.  **Code Morphing™ Software (CMS):** Uma camada de software (tradutor binário dinâmico) que realiza a **Tradução Dinâmica** de instruções x86 legadas para as instruções VLIW nativas do núcleo. O CMS inclui algoritmos de **Otimização de Código** e um **Cache de Código** para armazenar blocos de código VLIW traduzidos e otimizados.
3.  **Decoupling da ISA:** O design separa a ISA x86 do hardware subjacente, permitindo que o hardware seja simplificado e otimizado para baixo consumo, enquanto a compatibilidade x86 é mantida pelo software.
Fórmulas e Algoritmos (LongRun™ Power Management):
gRun™ implementa o **Dynamic Voltage and Frequency Scaling (DVFS)**, um algoritmo que ajusta dinamicamente a clock e a tensão de alimentação para otimizar o consumo de energia.
ação é baseada na fórmula de dissipação de energia em CM.
$\text{C}=\frac{(\text{Capacitância}\times\text{Frequência}\times\text{Tensão}^{2})}{2}$
tmo LongRun™ busca reduzir os três termos da equação:
*   **Capacitância:** Reduzida pelo design VLIW/CMS, que substitui grande parte da lógica de controle complexa (que adiciona capacitância) por software.
*   **Frequência (Frequência):** Reduzida dinamicamente quando a carga de trabalho é baixa.
*   **Tensão (Tensão):** Reduzida dinamicamente, sendo o termo mais impactante no consumo de energia ($\text{Tensão}^2$).
Pesquisador 10: Wen-mei Hwu
ns Técnicos Encontrados: 14
**Contribuições:** Superblock, Hyperblock, Otimização de Compiladores VLIW, Escalonamento de Instruções (Scheduling), Execução Predicada, Arquitetura HPSm, Algoritmo TDCDP
Conteúdo Técnico do Trabalho de Wen-mei Hwu
alho de Wen-mei Hwu e seu grupo de pesquisa (IMPACT) é fundamental no desenvolvimento de técnicas de otimização de compiladores e microarquiteturas para explorar o **Paralelismo em Nível de Instrução (ILP)** em processadores **VLIW (Very Long Instruction Word)** e **Superscalar**. O foco principal está em estruturas de otimização de código que permitem o escalonamento de operações através de blocos básicos.
1. Superblock
le ILP em programas com fluxo de controle intensivo.

*   **Conceito:** Uma sequência de blocos básicos (instruções) que possui uma única entrada (*single entry*) no topo, mas pode ter múltiplas saídas (*multiple side exits*). Isso simplifica o *bookkeeping* (contabilidade) de código associado ao movimento de instruções.
*   **Algoritmo de Formação:**
    1.  **Seleção de Trace:** Identificação de caminhos de execução mais frequentes (*traces*) usando informações de perfil de execução (*profile information*).
| 2. **Duplicação de Cauda (Tail Duplication)**: Eliminação de todas as entradas laterais (*side entrances*) para o *trace* selecionado. O código subsequente à primeira entrada lateral é duplicado, e a entrada lateral é redirecionada para a cópia, garantindo a propriedade de entrada única. |
|---|
| • **Otimizações ILP (Superblock ILP Optimizations)**: Um conjunto de otimizações aplicadas dentro do Superblock para aumentar o ILP: |
| | ○ **Expansão de Branch (Branch Expansion)** |
| | ○ **Desenrolamento de Loop (Loop Unrolling)** |
| | ○ **Descamação de Loop (Loop Peeling)** |
| | ○ **Renomeação de Registradores (Register Renaming)** |
| | ○ **Expansão de Variável de Indução (Induction Variable Expansion)** |
| | ○ **Expansão de Acumulador (Accumulator Expansion)** |
| | ○ **Migração de Operação (Operation Migration)** |
| | ○ **Combinação de Operação (Operation Combining)** |
* **Escalonamento Superblock (Superblock Scheduling):** Realizado por *list scheduling* após a construção do grafo de dependência. Suporta Execução Especulativa (*Speculative Execution*) com dois modelos de hardware:
    * **Modelo de Percolação Restrita (Restricted Percolation Model):** Não permite que instruções que possam causar exceções (como *load* de memória) sejam movidas acima de *branches* condicionais, a menos que o compilador prove que nenhuma exceção ocorrerá.
    * **Modelo de Percolação Geral (General Percolation Model):** Fornece uma versão **não-trapante (non-trapping)** de instruções que podem causar exceções, permitindo que o escalonador mova essas instruções especulativamente.
2. Hyperblock
Hyperblock é uma extensão do Superblock que utiliza **Execução Predicada (Predicated Execution)** para agrupar blocos básicos de múltiplos caminhos de controle em uma única estrutura.

*   **Conceito:** Um conjunto de blocos básicos **predicados** com uma única entrada e múltiplas saídas. A execução predicada converte dependências de controle em dependências de dados, eliminando *branches* condicionais internas.
*   **Algoritmo de Formação:**
    1.  **Seleção de Bloco Hyperblock (Hyperblock Block Selection):** Blocos são selecionados com base em uma função heurística que considera a frequência de execução, o tamanho do bloco e a presença de instruções perigosas (*hazardous instructions*).
    2.  **Fórmula Heurística de Valor de Seleção de Bloco (BSV):** $\$BSV_i = (K \cdot \frac{weight_{bbi}}{weight_{mainpath}}) \cdot \frac{size_{mainpath}}{size_{bbi}} \cdot bb_char_i)$ Onde:
        *   $K$: Constante dependente da arquitetura (taxa de emissão do processador).
        *   $weight_{bbi}$: Frequência de execução do bloco básico $i$.
        *   $weight_{mainpath}$: Frequência de execução do caminho principal.
        *   $size_{bbi}$: Tamanho do bloco básico $i$.
        *   $size_{mainpath}$: Tamanho do caminho principal.
        *   $bb_char_i$: Valor característico do bloco básico (1 se não houver instruções perigosas, caso contrário).
    3.  **Duplicação de Cauda e Descamação de Loop:** Aplicadas para garantir a propriedade de entrada única e remover *loops* aninhados.
    4.  **\*If-conversion\***: Aplicação de uma variante do algoritmo RK para substituir *branches* condicionais por instruções predicadas.
*   **Grafo de Hierarquia de Predicados (PHG):** Uma estrutura de dados utilizada para análise de dependência e fluxo de controle dentro do Hyperblock. O PHG representa as equações booleanas para todos os predicados, permitindo determinar se duas instruções podem ser executadas no mesmo passo através do Hyperblock (ou seja, se há um caminho de controle entre elas).
# 3. Algoritmo TDCDP (Two-Dimensional Constrained Dynamic Programming)

O **TDCDP** é uma abordagem de **Programação Dinâmica com Restrições Bidimensionais** proposta para o escalonamento de instruções VLIW.

*   **Conceito:** Um algoritmo exato ou quase-exato que modela o problema de escalonamento de instruções VLIW como um problema de programação dinâmica com restrições de tempo e recursos, buscando soluções ótimas ou quase-ótimas, em contraste com os algoritmos heurísticos tradicionais.
4. Microarquitetura HPSm
* **Conceito:** Uma microarquitetura de fluxo de dados restrito (*restricted data flow*) projetada para implementação em *single-chip* VLSI. O HPSm explora concorrência horizontal e vertical, sendo uma variante do modelo HPS, com o objetivo de alcançar alto desempenho em um único chip.
* **Princípios RISC:** O trabalho de Hwu, ao focar em ILP e otimização de compiladores para VLIW e Superscalar, está intrinsecamente ligado aos princípios RISC (Reduced Instruction Set Computing), que favorecem instruções simples e regulares, facilitando a extração de paralelismo pelo compilador. As técnicas de Superblock e Hyperblock são essenciais para superar a limitação de ILP imposta pelos *branches* em arquiteturas baseadas em princípios RISC.
Pesquisador 11: Yale N. Patt
ns Técnicos Encontrados: 14
**Contribuições:** Previsão de Desvios Adaptativa de Dois Níveis, Microarquitetura HPS, Contador de Saturação de 2 Dados Restrito, Execução Fora de Ordem
Conteúdo Técnico do Trabalho de Yale N. Patt
O conteúdo técnico a seguir foca exclusivamente em algoritmos, fórmulas, estruturas de hardware, conceitos de mil e princípios RISC, conforme solicitado, extraído dos trabalhos de Yale N. Patt, notavelmente sobre a **Previsã Adaptativa de Dois Níveis** e a **Microarquitetura HPS (High-Performance Substrate)**.
**1. Previsão de Desvios Adaptativa de Dois Níveis (Two-Level Adaptive Branch Prediction)**

Este conceito, desenvolvido por Tse-Yu Yeh e Yale N. Patt, é um preditor de desvios dinâmico que utiliza dois níveis de histórico para fazer previsões, alcançando alta precisão.
1.1. Estruturas de Hardware
1. **Branch History Register (HR):**
*   **Estrutura:** Um registrador de deslocamento de *k* bits.
*   **Função:** Armazena os resultados dos *k* desvios mais recentes. O resultado do desvio mais recente (e.g., 1 ‘tomado’, 0 para ‘não tomado’) é inserido, e o registrador é deslocado.
2. **Pattern History Table (PHT):**
1.2. Algoritmo do Contador de Saturação de 2 bits (PHT)
O contador de saturação de 2 bits é uma Máquina de Estados Finitos (FSM) que implementa a histerese para evitar que desvios que mudam de direção frequentemente alterem a previsão drasticamente.
<table>
<tr>
<th>Estado (Binário)</th>
<th>Estado (Nome)</th>
<th>Previsão</th>
</tr>
<tr>
<td>00</td>
<td>Fortemente Não Tomado (Strongly Not Taken)</td>
<td>Não Tomado</td>
</tr>
<tr>
<td>01</td>
<td>Fracamente Não Tomado (Weakly Not Taken)</td>
<td>Não Tomado</td>
</tr>
<tr>
<td>10</td>
<td>Fracamente Tomado (Weakly Taken)</td>
<td>Tomado</td>
</tr>
<tr>
<td>11</td>
<td>Fortemente Tomado (Strongly Taken)</td>
<td>Tomado</td>
</tr>
</table>
Lógica de Atualização (Pseudocódigo/Fórmula):
Seja counter o valor do contador de saturação de 2 bits (0
mermaid
if (branch_taken) {
    counter = min(counter + 1, 3); // Incrementa, saturando em 11 (3)
} else {
    counter = max(counter - 1, 0); // Decrementa, saturando em 00 (0)
}
1.3. Variações do Esquema de Dois Níveis
O esquema de dois níveis possui diversas variações, classificadas pela forma como o histórico é coletado e como a PHT é indexada:

*   **GAg (Global History, Global PHT):** Histórico global ($G$) indexa uma PHT global ($g$).
*   **GShare (Global History, Shared PHT):** O endereço do desvio é combinado (geralmente via XOR) com o histórico global para indexar uma PHT compartilhada.
*   **PAg (Per-Branch History, Global PHT):** Histórico por desvio ($P$) indexa uma PHT global ($g$).
*   **PShare (Per-Branch History, Shared PHT):** Histórico por desvio ($P$) indexa uma PHT compartilhada ($s$).
# Coarquitetura HPS (High-Performance Substrate)
A HPS é um modelo de microarquitetura de alto desempenho que visa implementar arquiteturas de Conjunto de Instruções (ISP) de forma agnóstica, derivando seu desempenho da execução de operações **fora de ordem (out-of-order)**, **assíncrona** e **concorrente**.
**Itos de Microarquitetura e Pr**
*   **Fluxo de Dados Restrito (Restricted Data Flow):** O modelo HPS é baseado em uma arquitetura orientada a fluxo de dados onde as instruções são convertidas em **Nós (Nodes)** que representam micro-opeações. Isso se alinha ao princípio RISC de decompor instruções complexas em operações atômicas simples.
*   **Decodificação para Nós (Decoding to Nodes):** O decodificador converte o fluxo de instruções em **Nós de Fluxo de Dados**, que são as unidades de execução. Um nó representa uma micro-opeação que pode ser executada.
*   **Execução Fora de Ordem (Out-of-Order Execution):** Os nós são executados assim que seus operandos estão disponíveis, maximizando o paralelismo em nível de instrução (ILP) dentro de uma **Janela Ativa (Active Window)**.
*   **Retirada e Reparo de Ordem Sequencial (Sequential Order Retirement and Repair):** O sistema garante que o estado arquitetural do programa seja atualizado na ordem sequencial original, permitindo o tratamento preciso de exceções e interrupções.
Estrutura do Fluxo de Dados
| 1. | **Branch Predictor**: Fornece o próximo endereço de busca. |
|---|---|
| 2. | **Decoder/Merger**: Decodifica instruções em nós e os insere na Janela Ativa. |
| 3. | **Active Window (Janela Ativa)**: Contém as **Tabelas de Nós (Node Tables)**, onde as operações aguardam seus operandos. |
| 4. | **Issue**: Seleciona nós prontos para execução. |
| 5. | **Functional Units (F.U.)**: Unidades de execução que processam os nós. |
| 6. | **Value Buffer**: Armazena resultados temporários. |
| 7. | **Retirement System**: Gerencia a conclusão e o *commit* sequencial das instruções. |
Pesquisador 12: Trevor Mudge
**Itens Técnicos Encontrados: 11**
**Contribuições:** Equações de Potência CMOS, Fórmulas de Frequência e Corrente de Fuga, Fila de Write-back Atrasado (DWQ), Buffer de Pré-busca de Operando (OPB), Fila de Requisição de Pré-busca de Operando (OPRQ), Arquitetura de Arquivo de Registro Dividido
nteúdo Técnico do Trabalho de Trevo
alho de Trevor Mudge, focado em design de baixa potência e eficiência energética, especialmente em microarquiteturas de processadores, pode ser resumido nos seguintes conceitos, fórmulas e estruturas de hardware:
las de Potência e Desempenho em Lógica CMOS
As equações a seguir, fundamentais para o design de baixa potência em circuitos CMOS, são centrais na análise de Mudge sobre a arquitetura como uma restrição de design de primeira classe [1]:

**1. Equação de Consumo de Potência Total (P)**

A potência total consumida por um circuito CMOS é a soma de três componentes: potência dinâmica, potência de curto-circuito e potência de fuga (estática).
<table>
<tr>
<td>$P = P_{dinâmica} + P_{curto-circuito} + P_{fuga}$</td>
</tr>
<tr>
<td>$P = (ACV^2 f) + (\tau AV I_{short}) + (VI_{leak})$</td>
</tr>
</table>
<table>
<tr>
<th>Variável</th>
<th>Descrição</th>
<th>Componente</th>
</tr>
<tr>
<td>$P$</td>
<td>Potência total consumida</td>
<td>-</td>
</tr>
<tr>
<td>$A$</td>
<td>Fator de atividade (fração de portas que comutam)</td>
<td>$P_{\text{dinâmica}}$</td>
</tr>
<tr>
<td>$C$</td>
<td>Capacitância total comutada</td>
<td>$P_{\text{dinâmica}}$</td>
</tr>
<tr>
<td>$V$</td>
<td>Tensão de alimentação</td>
<td>$P_{\text{dinâmica}}, P_{\text{curto-circuito}}, P_{\text{fuga}}$</td>
</tr>
<tr>
<td>$f$</td>
<td>Frequência de operação</td>
<td>$P_{\text{dinâmica}}$</td>
</tr>
<tr>
<td>$\tau$</td>
<td>Tempo de fluxo momentâneo (curto-circuito)</td>
<td>$P_{\text{curto-circuito}}$</td>
</tr>
<tr>
<td>$I_{short}$</td>
<td>Corrente de curto-circuito</td>
<td>$P_{\text{curto-circuito}}$</td>
</tr>
<tr>
<td>$I_{leak}$</td>
<td>Corrente de fuga (vazamento)</td>
<td>$P_{\text{fuga}}$</td>
</tr>
</table>
2. Equação de Frequência Máxima de Operação ($f_{max}$)
A frequência máxima de operação é aproximadamente linear em $V$, mas depende da tensão de limiar ($V_{threshold}$):

$$\frac{(V - V_{threshold})^2}{(V - V_{threshold})^2 + (V_{saturation} - V)^2}$$
$f_{max}\propto\frac{(V-V_{threshold})^{2}}{V}$
uação de Corrente de Fuga
ível à tensão de limiar, o que limita a redução de $V_{threshold}$ pós-
I_{leak} \propto \exp\left(-\frac{qV_{threshold}}{kT}\right)

| Variável | Descrição |
|---|---|
| q | Carga elementar |
| k | Constante de Boltzmann |
| T | Temperatura absoluta |
Conceitos e Estruturas de Microarquitetura de Baixa Potência
O trabalho de Mudge e Kim sobre arquivos de registro de baixa potência introduz estruturas auxiliares para reduzir o número de portas de leitura, que são grandes consumidores de energia e área em processadores *wide-issue* (como os baseados em *VLIW*) [2]:
1. Arquitetura de Arquivo de Registro Dividido (Split Reg)
*   **Conceito:** Uma técnica de microarquitetura para reduzir o impacto do tempo de ciclo em arquivos de registro *multiported* (com múltiplas portas). Um arquivo de registro grande (ex: 16-r/8-w) é implementado como dois arquivos menores (ex: dois 8-r/8-w).
*   **Estrutura:** Duplica o conteúdo do arquivo de registro em dois arrays de memória, resultando em acesso mais rápido, mas com maior consumo de energia e área em comparação com um arquivo monolítico.

2. Fila de Write-back Atrasado (Delayed Write-back Queue - DWQ)

*   **Conceito:** Uma pequena estrutura de memória auxiliar (tipo FIFO) que armazena resultados de unidades funcionais por um número limitado de ciclos (ex: 2 ciclos).
*   **Função:** Permite que operandos recentemente produzidos sejam acessados diretamente da DWQ, evitando o acesso ao arquivo de registro principal. Isso reduz a demanda de pico por portas de leitura.
*   **Hardware:** Implementada como uma memória totalmente associativa de 8-r/8-w portas com poucas entradas (ex: 16 entradas). Requer um **contador de 2 bits** por entrada para rastrear o tempo de vida do resultado na fila.
r de Pré-busca de Operando (Operand Pre-fetch Buffer -
* **Conceito:** Uma pequena memória totalmente associativa (ex: 16-32 entradas, 8-r/8-w portas) para armazenar operandos pré-buscados.
* **Função:** Reduz a congestão das portas de leitura ao pré-buscar um operando pronto enquanto a instrução aguarda o segundo operando.
* **Conceito:** Uma fila que armazena requisições de pré-busca de operando quando os recursos (portas de leitura, espaço no OPB) não estão imediatamente disponíveis no ciclo de *dispatch*.
* **Função:** Permite que a pré-busca seja escalonada para ciclos subutilizados, melhorando a eficiência do uso das portas de leitura.
# Métrica de Redução de Perda de Desempenho (LossReduction)

*   **Conceito:** Métrica usada para quantificar a perda de desempenho (em termos de IPC - Instruções Por Ciclo) causada pela redução do número de portas do arquivo de registro.
*   **Fórmula (implícita no contexto de microarquitetura):** $LossReduction = \frac{IPC_{baseline} - IPC_{reduced}}{IPC_{baseline}} * \text{OndeIPC}\{baseline\}$ é o IPC do processador com o número de portas reduzido.
Princípios RISC Aplicados
Os conceitos de microarquitetura acima são aplicações diretas dos princípios RISC de **registro-para-registro** e ILP (Instruction Level Parallelism). A necessidade de um grande número de portas de leitura/escrita no arquivo de registro (o problema que as técnicas DWQ/OPB/OPRQ resolvem) é uma consequência direta da arquitetura *load/store* e da execução *out-of-order* (fora de ordem) em processadores RISC de alto desempenho. O trabalho de Mudge e colaboradores visa manter o alto desempenho (alto IPC) característico do RISC, enquanto mitiga o alto consumo de energia e área que acompanha o *multiporting* do arquivo de registro.
dge, T. (2001). Power: A first-class architectural design constraint. *Computer*, 34(4), 52-58. [2] Kim, N. S., & Mudge, T. (2003). Microarchitecture of a low power register file. *Proceedings of the 2003 international symposium on Low power electronic design (ISLPED)*, 384-389.
uisador 13: Krste Asanovic (e colabora
ns Técnicos Encontrados: 10
**Contribuições:** Arquitetura Modular RISC-V, Extensão Vetorial de Comprimento Variável (RVV), Modelo de Condição de Liberação (Release Consistency), Primitivas Atômicas LR/SC, Formato de Instrução Base RV32I, Registrador Z, Endereçamento Relativo ao PC (AUIPC)
Conteúdo Técnico do Trabalho de Krste Asanovic (RISC-
O trabalho de Krste Asanovic, em colaboração com David Patterson, Andrew Waterman e outros, estabeleceu a **Arquitetura do Conjunto de Instruções (ISA) RISC-V**, focada em modularidade, simplicidade e extensibilidade. O conteúdo técnico a seguir foca nos conceitos de arquitetura RISC, estruturas de hardware e microarquitetura, excluindo aspectos históricos ou narrativos.
1. Princípios RISC e Estrutura da ISA Base (RV32I)
A ISA base **RV32I** (32-bit Integer) adere estritamente aos princípios RISC, sendo uma arquitetura *load-store* de largura fixa (32 bits) e um conjunto mínimo de instruções.
1.1. Estado Arquitetural Visível ao Usuário
*   **31 Registradores de Propósito Geral (x1-x31):** Cada um com 32 bits de largura.
*   **Registrador Zero Fixo (x0):** Um registrador de 32 bits **hard-wired** ao valor constante zero. Qualquer escrita em x0 é descartada.
*   **Contador de Programa (pc):** Um registrador de 32 bits que armazena o endereço de byte da instrução atual.
1.2. Formatos de Instrução
O RV32I utiliza seis formatos de instrução de 32 bits, que são projetados para simplificar a decodificação do hardware:
*   **Tipo R (Register):** Usado para operações aritméticas e lógicas entre registradores.
*   **Tipo I (Immediate):** Usado para operações com imediato e instruções de *load*.
*   **Tipo S (Store):** Usado para instruções de *store*.
*   **Tipo U (Upper Immediate):** Usado para carregar o imediato superior (instruções LUI e AUIPC).
*   **Tipo SB (Branch):** Variante do Tipo S, usado para *branches* condicionais.
*   **Tipo UJ (Jump):** Variante do Tipo U, usado para *jumps* incondicionais.
dereçamento Relativo ao PC (PC-Relative Addressing)
ção **AUIPC** (Add Upper Immediate to PC), um conceito
AUIPC rd, immediate ⇒ rd = pc + (immediate ≪ 1)
Esta instrução carrega os 20 bits superiores de um imediato no registrador de destino (rd) e adiciona o valor permitindo que o endereço de 32 bits seja construído em duas instruções (AUIPC seguido por uma instrução de lo Tipo I ou S).
Primitivas Atômicas e Modelo de Cons
A extensão **RVA** (Atomic) fornece primitivas de sincronização para multiprocessadores, baseadas no conceito de **Reserved/Store-Conditional (LR/SC)**.
2.1. Load-Reserved/Store-Conditional (LR/SC)
O par de instruções LR/SC é a base para a implementação de operações atômicas como *Compare-and-Swap* (CAS).

- **LR.W (Load-Reserved Word):** Carrega uma palavra de memória para um registrador e define um reservation set no endereço de memória.
- **SC.W (Store-Conditional Word):** Tenta armazenar um valor no mesmo endereço. O armazenamento só é bem-sucedido (retorna 0) se o reservation set não tiver sido invalidado por outra escrita.
O algoritmo para uma operação atômica de *Compare-and-Swap* (CAS) é implementado em software usando
assembly
lr.w t0, (a0)          # t0 = *a0 (Load-Reserved)
bne t0, a1, fail       # Se t0 != valor_esperado (a1), falha
sc.w t0, a2, (a0)      # Tenta *a0 = novo_valor (a2). t0 = 0 se sucesso.
bne t0, x0, try_again  # Se t0 != 0 (falha), tenta novamente
li a0, 0               # Sucesso: retorna 0
ret

fail:
    li a0, 1            # Falha: retorna 1
    ret
2.2. Modelo de Consistência de Liberação (Release Consistency)
C-V adota um modelo de consistência de memória baseado em **Release Consistency**, que é implementado através
fence pred, succ
pred e succ são máscaras de 4 bits que especificam quais tipos de acesso (Leitura/Escrita de Memória/Dispositivo) con-
A RVV, uma das principais áreas de pesquisa de Asanovic, introduz um modelo de vetorização que é **agnostico** à microarquitetura e escalável.
3.1. Conceitos Fundamentais da RVV
*   **Registradores Vetoriais (v0–v31):** 32 registradores vetoriais.
*   **Comprimento Máximo do Vetor (Maximum Vector Length - MVL):** O número máximo de elementos que um registrador vetorial pode conter, definido pela implementação de hardware.
*   **Comprimento do Vetor (Vector Length - VL):** O número de elementos a serem processados em uma operação vetorial, definido em tempo de execução pelo software. $0 \leq VL \leq MVL$.
*   **Tipo de Elemento (Element Width - EW):** O tamanho de cada elemento (e.g., 8, 16, 32, 64 bits).
*   **Comprimento de Dados do Vetor (Vector Data Length - VDL):** O número total de bits em um registrador vetorial. $VDL = MVL \times EW$.
3.2. Estrutura de Hardware e Execução
RVV é projetada para ser **configurável** e **polimórfica**, permitindo que o mesmo código vetorial seja executado em hardware com diferentes números de *lanes* (pistas de processamento) e diferentes MVLs.

*   **Execução Mascarada:** Todas as instruções vetoriais podem ser executadas sob uma máscara (geralmente armazenada em `v0`), permitindo o processamento eficiente de dados esparsos ou condicionais.
*   **Instruções de Memória Vetorial:** Suporte para padrões de acesso complexos:
    *   *Linear:* Acessos contíguos.
    *   *Strided:* Acessos com um passo fixo.
    *   *Gather/Scatter (Indexado):* Acessos não contíguos, onde os endereços são fornecidos por um registrador vetorial de índices.
3.3. Algoritmo de Adição Vetorial (Exemplo)
A semântica de uma instrução vetorial, como a adição de ponto flutuante (vfadd.s v0, v1, v2), é de software, que é então mapeado para o hardware:
c
// Semântica da instrução vfadd.s v0, v1, v2 (VL=v1)
for (i = 0; i < v1; i++ )
{
    v0[i] = v1[i] +F32 v2[i];
}
// Elementos além de VL são intocados ou zerados (dependendo do modo de mascaramento)
for (i = v1; i < MVL; i++ )
{
    v0[i] = 0; // Exemplo de modo de mascaramento
}
Este modelo garante que o código seja **portável** entre implementações de hardware com diferentes (diferentes números de *lanes* ou MVLs).
4. Conceitos de Microarquitetura
O trabalho de Asanovic em Berkeley tambem se estende a implementações concretas, como o **Rocket Chip Generator** e a microarquitetura **Saturn Vector Unit**.

*   **Rocket Chip Generator**: Um framework de código aberto escrito em **Chisel** (um *Hardware Description Language* baseado em Scala) que permite a geração rápida de *System-on-Chips* (SoCs) RISC-V configuráveis.
*   **Chisel (Constructing Hardware in a Scala Embedded Language):** Um HDL de alto nível que facilita o design ágil de hardware e a criação de geradores de processadores parametrizáveis.
*   **Microarquitetura Saturn (Vector Unit):** Uma microarquitetura vetorial parametrizável que implementa a RVV, focada em eficiência e extensibilidade.
Nota: Este conteúdo foi extraído de documentos técnicos e dissertações relacionadas ao trabalho de Krste As
colaboradores, focando estritamente em algoritmos, fórmulas, estruturas de hardware e conceitos de arquitetura.
Pesquisador 14: Andrew Waterman
**Itens Técnicos Encontrados:** 22

**Contribuições:** Especificação da Arquitetura Privilegiada RISC-V, Tradução de Endereço de Dois Estágios (Hypervisor), Controlador de Interrupção PLIC
Conteúdo Técnico: Arquitetura Privilegiada RISC-V
O trabalho de Andrew Waterman, como um dos editores principais do Manual do Conjunto de Instruções RISC-V, Volume II: Arquitetura Privilegiada, estabelece os fundamentos técnicos para a operação de sistemas RISC-V em modos de alto privilégio. O foco da especificação reside na definição de estruturas de hardware, conceitos de microarquitetura, e algoritmos essenciais para o gerenciamento de exceções, interrupções, memória e virtualização [1].
1. Princípios RISC e Modos de Privilegios
A arquitetura privilegiada RISC-V adere aos princípios **RISC (Reduced Instruction Set Computer)** ao manter a complexidade no software (sistema operacional e hypervisor) e simplificar o hardware. Um princípio central é a facilidade de virtualização: a arquitetura é projetada para simplificar o uso de técnicas clássicas de virtualização, onde um sistema operacional convidado é executado no nível de usuário, pois as poucas instruções privilegiadas podem ser facilmente detectadas e capturadas (trapped) [1].

A arquitetura define três modos de privilégio principais: **Machine-mode (M-mode)**, o modo de maior privilégio e o primeiro a ser inserido no reset; **Supervisor-mode (S-mode)**, usado por sistemas operacionais; e **User-mode (U-mode)**, para aplicações.
de Hardware: Registradores de Contr
Os **Registradores de Controle e Status (CSRs)** são estruturas de hardware essenciais que controlam o comportamento do processador em modos privilegiados. São registradores de leitura/escrita de **XLEN** bits (32, 64 ou 128), e muitos campos são definidos como **WARL (Write Any Read Legal)**, o que significa que qualquer valor pode ser escrito, mas a leitura retornará um valor legal definido pela implementação [1].
2.1. Registrador Machine ISA (misa)
O registrador *misa* é uma estrutura que reporta a **ISA (Instruction Set Architecture)** suportada pelo *hart* (hardware) contém o campo **MXL (Machine XLEN)** e 26 bits para as extensões padrão (A-Z).

A largura nativa da ISA base (**XLEN**) é codificada pelo campo MXL conforme a tabela a seguir:
<table>
<tr>
<th><strong>MXL</strong></th>
<th><strong>XLEN</strong></th>
</tr>
<tr>
<td>1</td>
<td>32</td>
</tr>
<tr>
<td>2</td>
<td>64</td>
</tr>
<tr>
<td>3</td>
<td>128</td>
</tr>
</table>
A largura base pode ser determinada pela fórmula: $XLEN=2^{MXL+4}4$
2.2. Registradores de Exceção e Interrupção
Machine Trap-Vector Base-Address Register ( mtvec ) define o endereço base para o tratamento de traps. O campo
<table>
<tr>
<th>MODE</th>
<th>Nome</th>
<th>Algoritmo de Endereçamento</th>
</tr>
<tr>
<td>0</td>
<td>Direct</td>
<td>pc = BASE</td>
</tr>
<tr>
<td>1</td>
<td>Vectored</td>
<td>pc = BASE + 4 × cause</td>
</tr>
</table>
Onde cause é o código da exceção ou interrupção. Outros CSRs cruciais incluem o **Machine Status Register** (mstatus), que armazena o estado operacional, e o **Supervisor Exception Program Counter** (sepc), que armazena o endereço da instrução interrompida [1].
3. Gerenciamento de Memória e Algoritmos de Tradução
O gerenciamento de memória é implementado através de dois mecanismos principais: **Physical Memory Protection** e **Tradução de Endereço Virtual (Paging)**.
3.1. Proteção de Memória Física (PMP)
utiliza os registradores pmpcfg e pmpaddr para definir regiões de memória física com permissões específicas (leitura, escrita, execução) e modos de endereçamento, como **TOR (Top of Range)** e **NAPOT (Naturally Aligned Power-of-Two)** [1].
3.2. Tradução de Endereço Virtual (Paging)
strador **Supervisor Address Translation and Protection** (satp) controla o esquema de tradução de endereço, definindo os bits (Sv32, Sv39, Sv48, Sv57) e o endereço base da tabela de páginas (**PPN - Physical Page Number**).
Algoritmo de Tradução Sv39
quema **Sv39** traduz endereços virtuais de 64 bits para endereços físicos de 56 bits, utilizando um processo de três níveis de Page Table. O endereço virtual é dividido em campos, onde os bits [63:39] são ignorados (extensão de sinal) e os bits [38:1] são divididos em três VPNs (**Virtual Page Numbers**) de 9 bits cada, e os bits [11:0] formam o **Offset da Página** [1].

O processo de tradução utiliza a seguinte estrutura para o **Page Table Entry (PTE)**:
<table>
<tr>
<th>Bits</th>
<th>Campo</th>
<th>Descrição</th>
</tr>
<tr>
<td>63:54</td>
<td>Reservado</td>
<td></td>
</tr>
<tr>
<td>53:10</td>
<td>PPN</td>
<td>Physical Page Number</td>
</tr>
<tr>
<td>9:8</td>
<td>RSW</td>
<td>Reserved for Software</td>
</tr>
<tr>
<td>7:0</td>
<td>Flags</td>
<td>V, R, W, X, U, G, A, D</td>
</tr>
</table>
ico final é construído pela concatenação do PPN final com o Offset da Página. A fórmula para o cálculo do endereço reço Físico = PPN × 4096 + Offset$ Onde 4096 bytes é o tamanho padrão da página.
A **Extensão Hypervisor** (H-extension) introduz o modo **Hypervisor-extended Supervisor** (HS-mode) e o modo **Virtual Supervisor** (VS-mode) para suportar a hospedagem eficiente de sistemas operacionais convidados.

O conceito chave é a **Tradução de Endereço de Dois Estágios**, que virtualiza o subsistema de memória do convidado:

1.  **Primeiro Estágio:** O endereço virtual (VA) do convidado é traduzido para um **Endereço Físico de Convidado (GPA - Guest Physical Address)** usando o registrador *vsatp*.
2.  **Segundo Estágio:** O GPA é então traduzido para o **Endereço Físico de Supervisor (SPA - Supervisor Physical Address)** usando o registrador **Hypervisor Guest Address Translation and Protection** (*hgatp*).

O algoritmo de tradução de endereço de dois estágios é representado como: $VA \xrightarrow{vsatp} GPA \xrightarrow{hgatp} SPA$
5. Controlador de Interrupção em Nível de Plataforma (PLIC)
O **Platform-Level Interrupt Controller (PLIC)** é a estrutura de hardware responsável por priorizar e distribuir interrupções globais. O PLIC conecta fontes de interrupção (dispositivos I/O) a alvos de interrupção (contextos hart) através de múltiplos **interrupt gateways** e um **PLIC core** [1].

O **Algoritmo de Fluxo de Interrupção PLIC** segue uma sequência de seis passos:
1. **Interrupt Request:** O *interrupt gateway* processa o sinal da fonte e envia um *interrupt request* ao PLIC core.
2. **Pending Bit:** O PLIC core armazena o request no bit **IP (Interrupt Pending)**.
3. **Priorização:** A prioridade da interrupção pendente é comparada com o *threshold* por alvo, usando a matriz **IE (Interrupt Enable)**.
4. **Notificação:** Se a prioridade exceder o *threshold*, uma *interrupt notification* é enviada ao alvo.
5. **Claim:** O alvo envia um *interrupt claim* para obter o ID da interrupção de maior prioridade, o que limpa o bit IP correspondente.
6. **Completion:** Após o serviço, o alvo envia uma mensagem de *interrupt completion* ao *gateway*, permitindo que ele encaminhe um novo *request* da mesma fonte.
Referências
[1] The RISC-V Instruction Set Manual, Volume II: Privileged Architecture, Document Version 20211203. Edited by David A. Waterman, Krste Asanovic; and John Hauser. RISC-V International. ([https://five-embeddev.com/riscv-privileged.html](https://five-embeddev.com/riscv-privileged.html))
Pesquisador 15: Nigel Stephens
**Itens Técnicos Encontrados:** 28
**Contribuições:** Extensão Vetorial Escalável (SVE), Comprimento de Vetor Agnóstico (VLA), Predicação por Pista, Gather/Scatter, Registradores Vetoriais Escaláveis (Z0-Z31)
O trabalho de Nigel Stephens na arquitetura ARMv8/AArch64 é centralizado na introdução da **Extensão Vetorial Escalável (SVE)**, um avanço significativo sobre o **AArch64 Advanced SIMD (NEON)**. O NEON expandiu o suporte para ponto flutuante de **precisão dupla IEEE** e operações vetoriais de inteiros de **64 bits**, com o arquivo de registradores vetoriais crescendo de 16x128b para **32x128b**. As demandas por **Gather load & Scatter store, Per-lane predication** e **vetores mais longos** impulsionaram o desenvolvimento do SVE.

O SVE é uma extensão arquitetural separada, focada em cargas de trabalho de **HPC (High-Performance Computing)**, baseada no
é VL = N × 128 bits, onde N ∈ {1, 2, …, 16}. O comprimento do predicado (PL) é dado por PL = VL/8 bits, e o número de elementos (E) é E = VL/Tamanho_Elemento (em bits).

O estado arquitetural SVE introduz novas **estruturas de hardware**:

*   **Registradores Vetoriais Escaláveis (Z0-Z31):** 32 registradores que estendem os registradores NEON (V0-V31), suportando ponto flutuante de **precisão dupla (DP)** e **precisão simples (SP)**, além de inteiros de 64, 32, 16 e 8 bits. O comprimento é variável (**LEN x 128 bits**).
*   **Registradores de Predicado Escaláveis (P0-P15):** 16 registradores, onde P0-P7 são máscaras de pista para operações de load/store e aritmética, e P8-P15 são para manipulação de predicado. O FFR (First Fault Register) é usado para tratamento de exceções. O comprimento é **LEN x 16 bits**.
*   **Registradores de Controle (ZCR_ELx):** Usados para configurar o comprimento do vetor (**vector length**, LEN=1..16) e o nível de exceção/privilégio (EL1 a EL3).

Os **princípios RISC** e de microarquitetura do SVE para auto-vetorização incluem:

*   Modos de Endereçamento Ricos para acessos a dados não lineares.
*   Predicação por Pista (**Per-lane predication**) para vetorização de *loops* com fluxo de controle complexo. A operação de predicado segue o conceito lógico: Resultado_Pista<sub>i</sub> = { Operação(Dados_Pista<sub>i</sub>) se Predicado_Pista<sub>i</sub> = 1 Não_Modificado se Predicado_Pista<sub>i</sub> = 0 }.
*   Controle e Gerenciamento de *Loop* Orientado por Predicado para reduzir a sobrecarga vetorial.
*   Particionamento Vetorial e Especificação Gerenciada por Software para lidar com dependências de dados.
*   Sub-loops Intra-vetoriais Escalarizados para dependências de *loop* mais complexas.

**Algoritmos e Instruções Chave (A64/SVE):**

*   **Aritmética:**
    *   Soma Vetorial: ADD Zdn.D, Zdn.D, Zm.D
    *   Multiplicação Vetorial: MUL Zdn.D, Zdn.D, Zm.D
    *   Fusão de Multiplicação e Adição (FMA): FMLA Zdn.S, Zk.S, Zm.S
*   **Controle de Fluxo (Predicação):**
    *   Teste de Predicado: PTEST Pn.B, Pm.B
    *   Cópia Condicional: CMPEQ Pn.D, Pg/Z.D, Zm.D, #0
*   **Acesso a Dados Não-Linear:**
    *   Gather-Load: LD1B Zt.D, Pg/Z.D, [Zn.D, Zm.D, LSL #0]
    *   Scatter-Store: ST1B Zt.D, Pg/Z.D, [Zn.D, Zm.D, LSL #0]
*   **Agregação (Reduções):**
    *   Soma de Redução: SADDV Zt.D, Pg.D, Zm.D (Soma de todos os elementos de 64 bits em Zm, sob controle de predicado Pg).
Pesquisador 16: Richard Grisenthwaite
ns Técnicos Encontrados: 22
**Contribuições:** Arquitetura CHERI, Segurança baseada em Capability, Microarquitetura Neoverse N2, Extensão Suporte BFloat16
técnicos do Trabalho de Richard
O trabalho de Richard Grisenthwaite, como ARM Fellow e especialista em arquitetura de servidor (Neoverse), abrange avanços significativos em segurança de hardware e microarquitetura de alto desempenho. O conteúdo técnico extraído foca em dois pilares principais: a arquitetura de segurança **CHERI** (Capability Hardware Enhanced RISC Instructions) e os detalhes da microarquitetura do processador **Neoverse N2**.
Arquitetura CHERI e Extensões de Segurança
A arquitetura CHERI é uma extensão do conjunto de instruções RISC da ARM, projetada para mitigar vulnerabilidades de segurança de memória (como *buffer overflows*) através de um novo conceito arquitetural: a **Capability** (Capacidade)
Conceitos Fundamentais
O **Tag** é um bit de metadado adicional que acompanha a *capability* na memória, indicando se o dado é uma *capa* ou um dado comum. O princípio central é a **Unforgeability** (Inforjabilidade), garantindo que *capabilities* não podem ser modificadas arbitrariamente por software não privilegiado.
Algoritmos de Validação de Hardware
Algoritmo de Verificação de Acesso à Memória (Load/Store)
1. **Verificação de Tag:** Se `C.Tag` = 0, o acesso é abortado.

2. **Endereço de Acesso:** O endereço efetivo `A` é calculado como `A = C.Address + O`.

3. **Verificação de Limites (Bounds):** Se `A < C.Base` OU `A ≥ C.Base + C.Length`, o acesso é abortado (acesso fora dos limites).

4. **Verificação de Permissão:** Se `P_req ∉ C.Permissions`, o acesso é abortado (permissão negada).

**Algoritmo de Derivação de Capability (Monotonicidade):**

A criação de uma nova *capability* `C_new` a partir de uma original `C_orig` deve satisfazer as seguintes regras de subconjunto:

1. **Regra de Limites:** O novo alcance deve ser um subconjunto do original: `$C_new.Base ≥ C_orig.Base` E `C_new.Base + C_new.Length ≤ C_orig.Base + C_orig.Length$`

2. **Regra de Permissões:** O novo conjunto de permissões deve ser um subconjunto do original: `$C_new.Permissions ⊆ C_orig.Permissions$`

O **Program Counter (PC)** é aprimorado para se tornar uma *capability*, aplicando permissão e alcance a saltos diretos e indiretos, estendendo a segurança ao fluxo de controle.
2. Microarquitetura Neoverse N2 (Performance)
ne e Unidades de Execução
A microarquitetura N2 utiliza um pipeline profundo e out-of-order com as seguintes especificações de estrutura de
<table>
<tr>
<th>Estrutura de Hardware</th>
<th>Especificação</th>
<th>Conceito</th>
</tr>
<tr>
<td><strong>Decodificação</strong></td>
<td>5-wide</td>
<td>5 instruções decodificadas por ciclo</td>
</tr>
<tr>
<td><strong>Portas de Execução</strong></td>
<td>12 portas</td>
<td>Capacidade de execução paralela</td>
</tr>
<tr>
<td><strong>Reorder Buffer (ROB)</strong></td>
<td>160 entradas</td>
<td>Profundidade da janela <em>out-of-order</em></td>
</tr>
<tr>
<td><strong>Janela de Instrução</strong></td>
<td>64 entradas</td>
<td>Número de instruções prontas para emissão</td>
</tr>
<tr>
<td><strong>Unidades de Inteiros</strong></td>
<td>4 ALU, 3 AGU</td>
<td>Unidades Lógicas e Aritméticas (ALU) e de Geração de Endereço (AGU)</td>
</tr>
<tr>
<td><strong>Unidades FP/SIMD</strong></td>
<td>2 unidades de 128 bits</td>
<td>Unidades de Ponto Flutuante e SIMD</td>
</tr>
<tr>
<td><strong>Latência L1 D-Cache</strong></td>
<td>4 ciclos</td>
<td>Latência de acesso ao cache de dados de nível 1</td>
</tr>
</table>
Hierarquia de Cache e Extensões
A hierarquia de cache e as extensões vetoriais são cruciais para o desempenho em servidores:
<table>
<tr>
<th>Hierarquia de Cache</th>
<th>Especificação</th>
<th>Extensão/Conceito</th>
</tr>
<tr>
<td><strong>L1 I-Cache</strong></td>
<td>64KB, 4-way</td>
<td>Cache de Instrução de Nível 1</td>
</tr>
<tr>
<td><strong>L1 D-Cache</strong></td>
<td>64KB, 4-way</td>
<td>Cache de Dados de Nível 1</td>
</tr>
<tr>
<td><strong>L2 Cache</strong></td>
<td>1MB por <em>core</em>, 8-way</td>
<td>Cache de Nível 2 por núcleo</td>
</tr>
<tr>
<td><strong>L3 Cache (SLC)</strong></td>
<td>Até 96MB</td>
<td>Cache de Último Nível Compartilhada</td>
</tr>
<tr>
<td><strong>Extensão Vetorial</strong></td>
<td>SVE2 (2x128 bits)</td>
<td><strong>Scalable Vector Extension 2</strong></td>
</tr>
<tr>
<td><strong>Formato de Dados</strong></td>
<td>BFloat16</td>
<td>Suporte nativo para Machine Learning</td>
</tr>
<tr>
<td><strong>Interconexão</strong></td>
<td>CCIX 2.0, CXL 2.0</td>
<td>Coerência de Cache e Memória para Servidores</td>
</tr>
</table>
O Neoverse N2 incorpora o princípio RISC de alto desempenho, utilizando um **Pipeline Profundo e Out-of-Order** para maximizar o Paralelismo em Nível de Instrução (ILP) e mantendo o conceito de **Instruções de Largura Fixa** (implícito na arquitetura ARMv8/v9) para facilitar a decodificação 5-wide.
Pesquisador 17: Chris Williams
**Itens Técnicos Encontrados: 10**
**Contribuições:** Arquitetura de Renderização Baseada em Tiles (TBR), Pixel Local Storage (PLS), Compre-
Otimização de Compute Shaders com Work Groups e SLM, Aplicação da Lei de Amdahl ao Paralelismo de GE-
Conteúdo Técnico: Arquitetura ARM Mali GPU (Chris Williams)
O trabalho de Chris Williams e a arquitetura ARM Mali GPU se concentram em otimizações de hardware e software para gráficos e computação paralela em ambientes móveis e embarcados. O foco técnico reside na eficiência energética e no desempenho utilizando princípios de arquitetura RISC e paralelismo.
mulas e Princípios de P2
A arquitetura Mali, otimizada para computação paralela (via OpenCL ou Compute Shaders), é regida pelos limites teóricos do paralelismo, notavelmente a **Lei de Amdahl**.
Lei de Amdan
A Lei de Amdahl descreve o ganho máximo de velocidade ($S(n)$) que o processamento paralelo pode alcançar em um programa, dada a proporção de código que pode ser paralelizada.
$S(n)=\frac{1}{(1-P)+\frac{p}{n}}$
Onde:
*   $S(n)$ é o ganho de velocidade (speedup).
*   $P$ é a proporção do programa que pode ser paralelizada ($0 < P < 1$).
*   $n$ é o número de processadores (ou unidades de execução paralela).

Este princípio é fundamental para o design de software e hardware na Mali, destacando a importância de minimizar a porção serial do código ($1 - P$) para maximizar o desempenho da GPU.
2. Conceitos de Microarquitetura e Estruturas do
Arquitetura de Renderização Baseada em Tiles (TBR/TBDR)
PUs Mali (arquiteturas Midgard e Bifrost) utilizam uma arquitetura de **Renderização Baseada em Tiles** recentemente implementada como **Tile-Based Deferred Rendering (TBDR)**.
*   **Conceito:** A tela é dividida em pequenas regiões (tiles). Toda a geometria da cena é processada e classificada por tile. O sombreamento e o processamento de fragmentos ocorrem *apenas* para os pixels dentro de cada tile, e o resultado final é escrito na memória principal apenas uma vez por tile.
*   **Algoritmo Básico (TBR):** $Para cada tile:Para cada primitiva no tile:Para cada fragmento na primitiva no tile: Processar o fragmento.$
*   **Benefício:** Redução drástica na largura de banda da memória externa, pois a maior parte do tráfego de leitura/escrita de cor e profundidade ocorre no *tile buffer* interno e rápido da GPU.
Pixel Local Storage (PLS)
* **Estrutura:** Um buffer de alta velocidade, local ao *tile*, que permite que os fragment shaders leiam e escrevam dados sem acessar a memória principal (DRAM).
* **Conceito:** Permite a passagem de dados entre diferentes passes de renderização (render passes) dentro do mesmo tile, como se fossem múltiplos *render targets* locais. Isso otimiza algoritmos de renderização complexos, como *deferred shading* ou *multi-pass blending*, mantendo os dados no chip.
3. Algoritmos de Computação e Gráficos
pute Shaders e Grupos de Trabalho
A computação de propósito geral (GPGPU) na Mali é implementada via Compute Shaders (OpenGL ES) ou Kernels (OpenCL), organizados em **Grupos de Trabalho** (Work Groups).

*   **Conceito:** Um grupo de trabalho é uma coleção de invocações de shaders que são executadas em paralelo. Os threads dentro de um grupo de trabalho podem se comunicar e sincronizar.
*   **Estrutura de Comunicação:** A **Memória Local Compartilhada** (Shared Local Memory - SLM) é uma pequena e rápida memória *on-chip* acessível por todos os threads dentro do mesmo grupo de trabalho.
*   **Sincronização:** A função `barrier()` é usada para sincronizar todos os threads em um grupo de trabalho, garantindo que todas as operações de memória e acesso à SLM sejam concluídas antes de prosseguir.

**Adaptive Scalable Texture Compression (ASTC)**
**Conceito:** Compressão de textura adaptativa que suporta taxas de bits de 8 bpp a menos de 1 bpp.

**Estrutura:** Suporta dimensões de bloco quadradas e não quadradas (ex: 4x4, 5x4, 12x12) em 2D e 3D (ex: 3x3x3, 6x6x6), permitindo que o desenvolvedor escolha a taxa de compressão e a qualidade de forma flexível.
Tessellation Adaptativa
Algoritmo de otimização de geometria
- **Conceito:** O nível de detalhe (LOD) da tessellation (subdivisão de primitivas) é ajustado dinamicamente com base em critérios como a distância da câmera ou a taxa de mudança de curvatura da superfície. Isso garante que apenas a quantidade necessária para a qualidade visual atual seja processada, economizando ciclos de GPU.
Algoritmo Surface Nets (via Geometry Shaders)
Geometry Shaders podem ser usados para implementar algoritmos de extração de malha, como o Surface Nets.

**Otimização:** Para otimizar o Surface Nets na GPU, é utilizada uma combinação de:

1.  **Atomic Counters:** Para contar o número de cubos que intersectam a superfície.
2.  **Indirect Draw Calls:** Para desenhar apenas os cubos que foram identificados como parte da superfície, minimizando o trabalho de renderização.
4. Princípios RISC (Reduced Instruction Set Computer)
tetura ARM, na qual a Mali se baseia, segue o princípio RISC
*   **Conceito:** Foco em um conjunto de instruções simplificado e menor, onde cada instrução executa uma tarefa única e pode ser executada mais rapidamente (idealmente em um ciclo de clock).
*   **Implicação na GPU:** A arquitetura de *shader core* unificada da Mali (presente nas séries Midgard e Bifrost) reflete a filosofia RISC ao usar um conjunto de instruções otimizado para paralelismo e eficiência, permitindo que o hardware seja menor, mais eficiente em termos de energia e mais rápido na execução de instruções simples e repetitivas.
*   **Estrutura de Hardware:** Unified Shader Core Architecture (Arquitetura de Núcleo de Shader Unificado), onde o mesmo hardware processa vértices, fragmentos e computação, aumentando a eficiência e o uso de recursos.
O conteúdo técnico foi extraído de guias de desenvolvedor da ARM para as GPUs Mali, que refletem a arquitetura e otimizações promovidas por engenheiros como Chris Williams.
Pesquisador 18: Mark Hambleton
**Itens Técnicos Encontrados:** 200
**ibuições:** Arquitetura de Segurança TrustZone, Níveis de Exceção (EL0-EL3), Controlador TrustZone (TZC), Instrução S or Call (SMC), Particionamento de Memória Secure/Non-secure, Trusted Base System Architecture (TBSA)
# Conteúdo Técnico da Arquitetura TrustZone (Mark Hambleton - TrustZone Architect)
3. TrustZone no Processador (Páginas 8-17)
3.1. Estados de Segurança (Security States)
M define dois estados de segurança: **Secure** (Seguro) e **Non-**
*   **NS.ELx:** Non-secure state, Exception Level x (Estado Não-seguro, Nível de Exceção x).
*   **S.ELx:** Secure state, Exception Level x (Estado Seguro, Nível de Exceção x).

O processador pode estar em um estado Secure ou Non-secure, controlado pelo bit **SCR_EL3.NS**.

*   **SCR_EL3.NS = 1:** Non-secure
*   **SCR_EL3.NS = 0:** Secure
| O EL3 (Exception Level 3) está sempre no estado Secure, independentemente do valor do bit SCR_EL3.NS. |
|---|
| **Arranjo de Estados de Segurança e Níveis de Exceção (Microarquitetura):** |
<table>
<tr>
<th>Nível de Exceção (EL)</th>
<th>Non-secure (SCR_EL3.NS=1)</th>
<th>Secure (SCR_EL3.NS=0)</th>
</tr>
<tr>
<td><strong>EL0</strong></td>
<td>App</td>
<td>App</td>
</tr>
<tr>
<td><strong>EL1</strong></td>
<td>Rich OS</td>
<td>Trusted OS</td>
</tr>
<tr>
<td><strong>EL2</strong></td>
<td>Hypervisor</td>
<td>Secure partition manager (Suporte opcional a partir de Armv8.4-A)</td>
</tr>
<tr>
<td><strong>EL3</strong></td>
<td>-</td>
<td>Firmware / Secure Monitor</td>
</tr>
</table>
3.2. Troca entre Estados de Segurança (Switching between Security states)
# 3.3. Espaços de Endereço Virtuais (Virtual address spaces)

A TrustZone estende o conceito de espaços de endereço virtuais para incluir o estado de segurança.

*   **TTBR (Translation Table Base Register)**: O processador usa o TTBR para localizar a tabela de tradução de endereços.
    *   **TTBR0_EL1**: Usado para tradução de endereços virtuais baixos.
    *   **TTBR1_EL1**: Usado para tradução de endereços virtuais altos.
*   **ASID (Address Space Identifier)**: Usado para identificar o espaço de endereço do processo e evitar a necessidade de flush do TLB (Translation Lookaside Buffer) em trocas de contexto.
*   **VMID (Virtual Machine Identifier)**: Usado para identificar a máquina virtual e evitar flush do TLB em trocas de contexto de VM.

A TrustZone adiciona um bit de segurança (NS) ao ASID e VMID para distinguir entre contextos Secure e Non-secure.

# 3.4. Espaços de Endereço Físicos (Physical address spaces)

O espaço de endereço físico é dividido em regiões Secure e Non-secure.

*   **Region Secure**: Acesso permitido apenas ao mundo Secure.
*   **Region Non-secure**: Acesso permitido a ambos os mundos (Secure e Non-secure).

O controle de acesso é feito por:

1.  Bit NS (Non-secure) no endereço físico (geralmente um bit estendido no bus de endereço).
2.  APCs (Access Protection Controllers) ou MPUs (Memory Protection Units).
3.  TZC (TrustZone Controller): Um controlador de memória que monitora o bus e impõe as regras de acesso Secure/Non-secure para periféricos e memória.
3.5. Dados, Instruções e Caches Unificadas
**Caches:** Podem ser configuradas para serem **Secure** ou **N**
* O bit de segurança (NS) é associado a cada linha de cache.
* O mundo Non-secure **não pode** acessar dados marcados como Secure na cache.
* O mundo Secure **pode** acessar dados Non-secure na cache.
3.6. Translation Lookaside Buffer (TLB)
* O TLB armazena traduções de endereços virtuais para físicos.
* O TLB é particionado logicamente pelo bit de segurança (NS) e pelos identificadores **ASID** e **VMID**.
* Um *entry* do TLB é válido apenas para o estado de segurança (Secure/Non-secure) e o nível de exceção (EL) correspondente.
3.7. Exceções SMC (Secure Monitor Call)
A instrução **SMC** é o mecanismo fundamental para a transição de execução entre o mundo Non-secure e o Secure (via EL3).

*   **Função:** Inicia uma chamada para o Secure Monitor (código EL3).
*   **Uso:** Troca de estado de segurança, acesso a serviços Trusted.
3.8. Virtualização Segura (Secure virtualization)
* Suporte para **Secure EL2** (a partir de Armv8.4-A) permite a virtualização de sistemas operacionais Secure (Trusted OS) e criação de um **Secure Partition Manager**.
* O Secure Partition Manager atua como um hypervisor para o mundo Secure, isolando múltiplas partições TrustZone.
4. Arquitetura do Sistema (Páginas 18-27)
4.1. Dispositivos Escravos, Periféricos e Memória
*   **Bus de Endereço:** Estendido com um bit de segurança (NS) para indicar se a transação é Secure ou Non-secure.
*   **Periféricos:** Classificados como Secure ou Non-secure.
    *   Um periférico Secure só pode ser acessado por transações Secure.
    *   Um periférico Non-secure pode ser acessado por transações Secure e Non-secure.
4.3. Impondo Isolamento (Enforcing isolation)
*   **TZC (TrustZone Controller):** Componente de hardware que implementa o isolamento de memória e periféricos.
    *   Configurado pelo software Secure (EL3).
    *   Monitora o bus de endereço e verifica o bit NS da transação contra as regras de acesso da região de memória/periférico.
    *   Se uma transação Non-secure tentar acessar uma região Secure, o TZC gera uma exceção (fault).
4.4. Bus Masters
* Dispositivos que podem iniciar transações no bus (e.g., DMA controllers, GPUs).
* Devem ser configurados para gerar transações Secure ou Non-secure.
* O TZC garante que os *Bus Masters* Non-secure não acessem recursos Secure.
4.6. Interrupções (Interrupts)
*   **GIC (Generic Interrupt Controller)**: Responsável por rotear interrupções.
*   Interrupções podem ser classificadas como Secure ou Non-secure.
*   Interrupções Secure são roteadas para o mundo Secure (EL3 ou S.EL1).
*   Interrupções Non-secure são roteadas para o mundo Non-secure (EL1 ou EL2).
4.10. Trusted Base System Architecture (TBSA)
*   Conjunto de requisitos de hardware e firmware para garantir uma base de confiança.
*   **Conceitos Chave:**
    *   **Root of Trust (RoT):** Um componente de hardware/firmware que é inerentemente confiável (e.g., Secure Monitor, Secure Boot ROM).
    *   **Chain of Trust (CoT):** Sequência de componentes de software que se autenticam mutuamente, desde o RoT até o sistema operacional.
    *   **Secure Boot:** Processo que garante que apenas software autenticado e íntegro seja carregado e executado.
Princípios RISC (Implícitos na Arquitetura ARM
Embora o documento não se concentre nos princípios RISC em si, a arquitetura TrustZone é uma extensão de hardware que se baseia neles:

*   **Instruções de Carga/Armazenamento (Load/Store Architecture):** A separação de espaços de endereço físico e virtual e o controle de acesso de memória pelo TZC são fundamentais para a arquitetura Load/Store, garantindo que as operações de memória sejam seguras.
*   **Conjunto de Instruções Reduzido (Reduced Instruction Set):** A instrução **SMC** é um exemplo de instrução específica e controlada que facilita a transição de estado de segurança de forma atômica e eficiente, em linha com a filosofia RISC de ter um conjunto de instruções simples e rápido.
*   **Registradores de Propósito Geral:** O uso de registradores de propósito geral é mantido, mas o estado de segurança (Secure/Non-secure) implica em um **banco de registradores** separado ou *banked* para o estado Secure, garantindo o isolamento de contexto.
Algoritmos e Fórmulas
O documento foca em conceitos de arquitetura e microarquitetura, e **não apresenta fórmulas matemáticas ou algoritmos criptográficos explícitos**. Os algoritmos são mencionados em contexto de uso (e.g., Secure Boot, Key Management), mas uma descrição do algoritmo em si não está presente.
quisador 19: Reinhard
**Itens Técnicos Encontrados:** 26
**Contribuições:** CMSIS-Core HAL, CMSIS-DSP Otimização, Fórmula de Interpolação Linear, Instruções MAC e SIMD, ARMv7-M
# Conteúdo Técnico Puro: ARM Cortex-M, CMSIS e DSP (Reinhard Keil)
1. Conceitos de Microarquitetura RISC e Estruturas de Hardware
Reinhard Keil, focado em ferramentas e padrões para a arquitetura ARM Cortex-M, está diretamente ligado aos conceitos técnicos de microarquitetura RISC (Reduced Instruction Set Computer) e estruturas de hardware:
*   **Arquitetura ARMv7-M:** Conjunto de instruções RISC de 32 bits, caracterizado por um *pipeline* eficiente e um conjunto de instruções simplificado para sistemas embarcados.
*   **Instruções de Múltipla Operação (DSP):**
    *   **Multiply-and-Accumulate (MAC):** Operação fundamental em Processamento Digital de Sinais (DSP), onde o produto de dois números é adicionado a um acumulador.
    *   **Single Instruction Multiple Data (SIMD):** Permite que uma única instrução execute operações paralelas em múltiplos dados (e.g., duas operações de 16 bits em um único ciclo de 32 bits), otimizando o desempenho de vetores.
*   **Unidade de Ponto Flutuante (FPU):** Estrutura de hardware presente em *cores* como o Cortex-M4F e M7, responsável pelo processamento de dados de ponto flutuante de precisão simples (32 bits) conforme o padrão IEEE 754.
*   **CMSIS-Core (Cortex Microcontroller Software Interface Standard):** Define uma **Hardware Abstraction Layer (HAL)** padronizada para acesso aos registradores do processador Cortex-M, incluindo o **SysTick** (temporizador do sistema), **NVIC** (Nested Vectored Interrupt Controller) e o **System Control Block**.
## Algoritmos e Fórmulas da Biblioteca CM
A biblioteca CMSIS-DSP, parte do padrão CMSIS, implementa algoritmos otimizados para DSP, utilizando as capacidades de hardware do Cortex-M.
rmula de Interpolação Linear (Base para Funções)
As funções trigonométricas rápidas (arm_sin_f32, arm_cos_f32) utilizam uma combinação de tabela de busca e interpolação linear para aproximação.

**Algoritmo de Aproximação Rápida (Exemplo: arm_sin_f32):**

1. **Normalização da Entrada:** $in = x \times \frac{1}{2\pi} \approx x \times 0.159154943092Ondex$ é o valor de entrada em radianos.
2. **Cálculo do Índice:** $findex = N \times inOndeN$ é o tamanho da tabela de busca (e.g., 256 ou 512).
3. **Separação de Componentes:** $index = \lfloor findex \rfloor fract = findex - index$
4. **Fórmula de Interpolação Linear:** $sinVal = (1.0 - fract) \times a + fract \times bOndea = \text{sinTable}[index]eb = \text{sinTable}[index+1]$.
2.2. Fórmulas de Funções Matemáticas Básicas
biblioteca fornece implementações otimizadas para operações vetoriais

*   **Produto Escalar (Dot Product):** $result = \sum_{i=0}^{N-1} A[i] \times B[i]$
*   **Adição Vetorial:** $C[i] = A[i] + B[i]$
*   **Multiplicação Vetorial:** $C[i] = A[i] \times B[i]$
*   **Escala (Scaling):** $C[i] = A[i] \times scale$
*   **Offset (Deslocamento):** $C[i] = A[i] + offset$
2.3. Algoritmos de Processamento de Sinais (Ca)
CMSIS-DSP abrange categorias de algoritmos de DSP, que são implementados com otimizações específicas para o Cortex-M:

*   **Transformadas:** Fast Fourier Transform (FFT), Inverse FFT (IFFT).
*   **Filtros:** Finite Impulse Response (FIR), Infinite Impulse Response (IIR), Biquad Cascade.
*   **Controle:** Proportional-Integral-Derivative (PID) Controller.
*   **Estatística:** Média, Desvio Padrão, Variância.
*   **Matrizes:** Multiplicação, Inversão, Transposição.
sador 20: Joseph YI
**Itens Técnicos Encontrados: 14**
**Contribuições:** Arquitetura ARM Cortex-M3, Conjunto de Instruções Thumb-2, Unidade de Proteção de Memória (MPU), Controlador de Interrupção Vetorizado Aninhado (NVIC), Registradores de Status de Programa (xPSR)
Técnico da Arquitetura ARM Cortex-M
O conteúdo técnico extraído foca nos conceitos de microarquitetura, princípios RISC, estruturas de hardware (regi-
conjunto de instruções do processador **ARM Cortex-M3**, conforme detalhado na obra de Joseph Yiu.
1. Princípios RISC e Microarquitetura
O Cortex-M3 é um processador baseado na arquitetura RISC (Reduced Instruction Set Computing), que se caracteriza por um conjunto de instruções simplificado, projetado para execução mais rápida.

*   **Arquitetura ARMv7-M:** O Cortex-M3 implementa a arquitetura ARMv7-M, que é otimizada para microcontroladores, combinando a arquitetura ARM de 32 bits com o conjunto de instruções Thumb-2.
*   **Microarquitetura:** O núcleo é projetado para ser altamente determinístico, com recursos como interrupções vetoriadas aninhadas, manipulação atômica de bits e uma Unidade de Proteção de Memória (MPU) opcional.
*   **Modos de Operação e Privilégio:**
    *   **Modos:** Thread Mode (para programas normais) e Handler Mode (para tratadores de exceção).
    *   **Níveis de Privilégio:** Privilegiado (acesso total à memória e registradores) e Usuário (acesso restrito, controlado pela MPU). O processador inicia em Thread Mode Privilegiado e as exceções sempre são tratadas em Handler Mode Privilegiado.
2. Estruturas de Hardware (Registradores)
gistradores de propósito geral (R0-R12) e registradores especi-
<table>
<tr>
<th>Registrador</th>
<th>Nome Completo</th>
<th>Função Técnica</th>
</tr>
<tr>
<td><strong>R0-R12</strong></td>
<td>General-purpose registers</td>
<td>Registradores de propósito geral de 32 bits.</td>
</tr>
<tr>
<td><strong>R13 (SP)</strong></td>
<td>Stack Pointer</td>
<td>Ponteiro de pilha, pode ser <strong>MSP</strong> (Main Stack Pointer, usado em Handler Mode e opcionalmente em Thread Mode) ou <strong>PSP</strong> (Process Stack Pointer, usado em Thread Mode).</td>
</tr>
<tr>
<td><strong>R14 (LR)</strong></td>
<td>Link Register</td>
<td>Armazena o endereço de retorno de uma sub-rotina.</td>
</tr>
<tr>
<td><strong>R15 (PC)</strong></td>
<td>Program Counter</td>
<td>Endereço da instrução atual.</td>
</tr>
<tr>
<td><strong>xPSR</strong></td>
<td>Program Status Registers</td>
<td>Conjunto de registradores de status (APSR, IPSR, EPSR) que contêm flags de processamento e status de execução.</td>
</tr>
<tr>
<td><strong>PRIMASK</strong></td>
<td>Interrupt Mask Register</td>
<td>Máscara todas as interrupções e exceções, exceto NMI e Hard Fault.</td>
</tr>
<tr>
<td><strong>FAULTMASK</strong></td>
<td>Fault Mask Register</td>
<td>Máscara todas as interrupções e exceções, exceto NMI.</td>
</tr>
<tr>
<td><strong>BASEPRI</strong></td>
<td>Base Priority Register</td>
<td>Define o nível de prioridade de mascaramento; desabilita interrupções de prioridade igual ou inferior.</td>
</tr>
<tr>
<td><strong>CONTROL</strong></td>
<td>Control Register</td>
<td>Define o nível de privilégio (Privilegiado/Usuário) e a seleção do Stack Pointer (MSP/PSP) em Thread Mode.</td>
</tr>
</table>
2.1. Registradores de Status de Programa (xPSR)

O xPSR é a combinação de três registradores de status
* **APSR (Application PSR):** Contém as flags de condição (N, Z, C, V) e a flag de saturação (Q).
* **IPSR (Interrupt PSR):** Contém o número da exceção/interrupção atualmente em execução.
* **EPSR (Execution PSR):** Contém os bits de status da instrução (ICI/IT) e o bit **T** (Thumb state, sempre 1 no Cortex-M).
<table>
<tr>
<th>Bit</th>
<th>Descrição</th>
</tr>
<tr>
<td><strong>N</strong> (31)</td>
<td>Negative (Resultado negativo)</td>
</tr>
<tr>
<td><strong>Z</strong> (30)</td>
<td>Zero (Resultado zero)</td>
</tr>
<tr>
<td><strong>C</strong> (29)</td>
<td>Carry/borrow (Carry ou empréstimo)</td>
</tr>
<tr>
<td><strong>V</strong> (28)</td>
<td>Overflow (Estouro)</td>
</tr>
<tr>
<td><strong>Q</strong> (27)</td>
<td>Sticky saturation flag (Saturação)</td>
</tr>
<tr>
<td><strong>T</strong> (24)</td>
<td>Thumb state (Sempre 1 no Cortex-M3)</td>
</tr>
<tr>
<td><strong>Exception number</strong> (8:0)</td>
<td>Indica qual exceção o processador está tratando</td>
</tr>
</table>
de Proteção de Memória
| Registros | Descrição |
|---|---|
| MPU_TYPE (0xE000ED90) | Indica se a MPU está presente e o número de regiões suportadas (0 ou 8). |
| MPU_CTRL (0xE000ED94) | Habilita/desabilita a MPU e o default memory map. |
| MPU_RNR (0xE000ED98) | Seleciona o número da região a ser configurada. |
| MPU_RBAR (0xE000ED9C) | Define o endereço base da região. |
| MPU_RASR (0xE000EDA0) | Define o tamanho e os atributos da região (TEX, S, C, B, XN, AP). |
4. Controlador de Interrupção Vetorizado Aninhado (NVIC)
O NVIC é um controlador de interrupção intimamente acoplado ao núcleo, responsável pela gestão eficiente de interrupções.

*   **Recursos:** Suporte a interrupções aninhadas (prioridades programáveis), vetorizadas (endereço do ISR lido diretamente da tabela de vetores), mudança dinâmica de prioridade e redução de latência.
*   **Redução de Latência:** Otimizações como salvamento e restauração automáticos de registradores (empilhamento/desempilhamento automático) e tratamento de interrupções de chegada tardia (*late arrival interrupts*).
5. Conjunto de Instruções Thumb-2
O Cortex-M3 suporta exclusivamente o conjunto de instruções **Thumb-2**, que é uma extensão do Thumb original, combinando instruções de 16 bits (para densidade de código) e 32 bits (para funcionalidade e desempenho).

*   **Sintaxe Unificada (UAL):** Permite que o código-fonte seja escrito de forma unificada, e o montador escolhe a instrução de 16 ou 32 bits mais apropriada.
*   **Instruções de 16 bits:** Usadas para alta densidade de código, geralmente acessando apenas registradores R0-R7.
*   **Instruções de 32 bits (Thumb-2):** Oferecem maior funcionalidade e acesso a todos os registradores (R0-R12, LR, PC).
*   **Instruções Especiais:** O conjunto inclui instruções para manipulação de bits (ex: BFC, BFI), que são cruciais para o controle de periféricos em sistemas embarcados.
*   **Instruções de Acesso a Registradores Especiais:**
    *   MRS `<reg>`, `<special_reg>`: Lê o conteúdo de um registrador especial.
    *   MSR `<special_reg>`, `<reg>`: Escreve em um registrador especial.
Algoritmos e Fórmulas (Conceitos de Endereçamento)
Embora o texto não apresente fórmulas matemáticas complexas, ele descreve o conceito de **Cálculo de Endereço e Alinhamento** inerente à arquitetura.

*   **Alinhamento de Dados:** A arquitetura Cortex-M3 exige que os acessos à memória sejam alinhados (ex: acesso de 32 bits deve ser em um endereço divisível por 4). O processador pode lidar com acessos não alinhados, mas isso pode gerar exceções de *Bus Fault* ou *Usage Fault* se não for configurado corretamente.
*   **Cálculo de Endereço em Instruções de Load/Store:** As instruções de acesso à memória (Load/Store) utilizam o endereço base (*Rn*) e um *offset* (*imm* ou *Rm*) para calcular o endereço efetivo:
    *   Endereço Efetivo = Rn + Offset
    *   O *offset* pode ser um valor imediato (#imm) ou o conteúdo de outro registrador (*Rm*), e pode ser aplicado com pré-indexação, pós-indexação ou *offset simples*.
*   **Cycles per Instruction (CPI):** Conceito de microarquitetura que mede a eficiência do processador, sendo o Cortex-M3 projetado para um CPI baixo, próximo de 1, devido ao pipeline ao conjunto de instruções otimizado.
**Nota:** O texto de Joseph Yiu é um guia de arquitetura e programação, e não um *paper* de pesquisa que introduz novas fórmulas matemáticas. O conteúdo técnico se concentra em estruturas de hardware, registradores, conjunto de instruções e conceitos de microarquitetura.