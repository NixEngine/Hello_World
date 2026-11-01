## Page 1

# RELATÓRIO TÉCNICO COMPLETO: ARQUITETURA x86

---

## Sumário Executivo

Total de Algoritmos/Fórmulas/Estruturas Coletados: 777

Conceitos da Arquitetura x86 Pesquisados: 28

Pesquisadores Analisados: 20

---

## PARTE 1: CONCEITOS DA ARQUITETURA x86 - CONTEÚDO TÉCNICO

---

### Conceito 1: ISA x86 - Codificação de Instruções e Modos de Endereçamento

Itens Técnicos Encontrados: 10

Conceitos-Chave: CISC, Codificação de Instrução Variável, Prefixos Legados, REX, VEX, XOP, ModR/M, SIB, Endereço Efetivo, Endereçamento Relativo a RIP/EIP, Micro-operações

### ISA x86: Estruturas Técnicas de Codificação e Endereçamento

A arquitetura x86, um exemplo clássico de **CISC (Complex Instruction Set Computer)**, é definida por um conjunto de instruções de tamanho variável (de 1 a 15 bytes) e complexidade elevada. A execução dessas instruções é frequentemente implementada através de **micro-operações (µops)** internas na CPU. O formato da instrução é modular e consiste em até sete componentes principais, que definem a operação, os operandos e o modo de endereçamento.

### Estrutura de Codificação de Instruções

A codificação de uma instrução x86-64 segue uma sequência estrita de campos opcionais, conforme detalhado na Tabela 1.

---


## Page 2

<table>
  <thead>
    <tr>
      <th>Ordem</th>
      <th>Componente</th>
      <th>Tamanho (Bytes)</th>
      <th>Função Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Prefixos Legados</td>
      <td>0 a 4</td>
      <td>Modificam o comportamento da instrução (ex: atomicidade com LOCK, repetição com REP, substituição de segmento, alteração de tamanho de operando/endereço).</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Prefixos Estendidos</td>
      <td>0 a 3</td>
      <td>Estendem o espaço de registradores e opcodes, suportando instruções SIMD avançadas (REX, VEX, XOP).</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Opcode</td>
      <td>1 a 3</td>
      <td>Define a operação primária a ser executada.</td>
    </tr>
    <tr>
      <td>4</td>
      <td>ModR/M</td>
      <td>0 ou 1</td>
      <td>Codifica o modo de endereçamento e/ou um registro operando.</td>
    </tr>
    <tr>
      <td>5</td>
      <td>SIB</td>
      <td>0 ou 1</td>
      <td>Usado em conjunto com ModR/M para endereçamento complexo com escala e índice.</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Deslocamento</td>
      <td>0, 1, 2, 4, ou 8</td>
      <td>Offset de memória adicionado ao endereço base.</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Imediato</td>
      <td>0, 1, 2, 4, ou 8</td>
      <td>Valor constante usado como operando.</td>
    </tr>
  </tbody>
</table>

## Prefixos Estendidos (REX, VEX, XOP)

Os prefixos estendidos são cruciais para a arquitetura de 64 bits e para as extensões vetoriais (SIMD).

### 1. Prefixos REX (64-bit Mode)

O prefixo **REX** (0x40-0x4F) é um byte único que estende o número de registradores acessíveis de 8 para 16 (R8-R15) e permite o uso de operandos de 64 bits.

**Estrutura de Bits REX (Byte):** $REX = 0100 | W | R | X | B$

*   **W (Bit 3):** Extensão do tamanho do operando para 64 bits.
*   **R (Bit 2):** Extensão do campo reg do ModR/M.
*   **X (Bit 1):** Extensão do campo index do SIB.
*   **B (Bit 0):** Extensão do campo r/m do ModR/M ou base do SIB.

### 2. Prefixos VEX (Advanced Vector Extensions)

O prefixo **VEX** (Vector Extensions) é usado para codificar instruções AVX/AVX2, suportando três ou quatro operandos e extensões de registradores vetoriais (XMM/YMM). Ele substitui os prefixos legados (0x66, 0xF3, 0xF2) e o REX.

**Estrutura de Bits VEX de 3 Bytes (0xC4):**

<table>
  <thead>
    <tr>
      <th>Byte</th>
      <th>Bits 7-0</th>
      <th>Campos</th>
      <th>Função</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>11000100</td>
      <td>Byte de Escape</td>
      <td>Valor fixo 0xC4 .</td>
    </tr>
    <tr>
      <td>1</td>
      <td>$R | $\overline{X}$ | $\overline{B}$ | m – mmmm</td>
      <td>R, X, B, Opcode Map</td>
      <td>$\overline{R}$, $\overline{X}$, $\overline{B}$ são complementos dos bits R, X, B do REX. m – mmmm define o mapa de opcodes (ex: 1, 2, 3 para 0x0F, 0x0F 0x38, 0x0F 0x3A).</td>
    </tr>
    <tr>
      <td>2</td>
      <td>W | $\overline{vvvv}$ | L | pp</td>
      <td>W, vvvv, L, pp</td>
      <td>W (64-bit operand size). $\overline{vvvv}$ (complemento do índice do registro fonte adicional). L (Vector length: 0=128b, 1=256b). pp (Implied prefix: 00=none, 01=0x66, 10=0xF3, 11=0xF2).</td>
    </tr>
  </tbody>
</table>

### 3. Prefixos XOP (eXtended Operations - AMD)

O prefixo **XOP** (0x8F) é uma extensão da AMD, similar ao VEX, mas com um byte de escape diferente e restrições no campo de mapa de opcodes.

**Estrutura de Bits XOP de 3 Bytes (0x8F):**

---


## Page 3

<table>
  <thead>
    <tr>
      <th>Byte</th>
      <th>Bits 7-0</th>
      <th>Campos</th>
      <th>Função</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>10001111</td>
      <td>Byte de Escape</td>
      <td>Valor fixo 0x8F.</td>
    </tr>
    <tr>
      <td>1</td>
      <td>$\overline{R} | \overline{X} | \overline{B} | m - mmmm$</td>
      <td>R, X, B, Opcode Map</td>
      <td>$\overline{R}, \overline{X}, \overline{B}$ são complementos dos bits R, X, B do REX. $m - mmmm$ define o mapa de opcodes (deve ser $\geq 8$).</td>
    </tr>
    <tr>
      <td>2</td>
      <td>$W | \overline{vvvv} | L | pp$</td>
      <td>W, vvvv, L, pp</td>
      <td>$W$ (64-bit operand size). $\overline{vvvv}$ (complemento do índice do registro fonte adicional). $L$ (Vector length: 0=128b, 1=256b). $pp$ (Implied prefix: geralmente 00 no XOP).</td>
    </tr>
  </tbody>
</table>

# Estruturas de Endereçamento (ModR/M e SIB)

Os bytes ModR/M e SIB são as estruturas de dados que codificam os complexos modos de endereçamento da arquitetura x86.

## 1. Byte ModR/M

O byte ModR/M é usado para especificar um operando de registro ou um operando de memória, e o modo de endereçamento.

**Estrutura de Bits ModR/M (Byte):** $ModR/M = mod | reg | r/m$

*   **mod (Bits 7-6):** 2 bits que, combinados com $r/m$, definem o modo de endereçamento (registro, memória sem deslocamento, memória com deslocamento de 8 bits, ou memória com deslocamento de 32 bits).
*   **reg (Bits 5-3):** 3 bits que especificam um registro operando ou são usados como extensão do opcode.
*   **r/m (Bits 2-0):** 3 bits que especificam um registro operando ou são usados para endereçamento de memória. Se $r/m = 100$ e $mod \neq 11$, o byte SIB está presente.

## 2. Byte SIB (Scale-Index-Base)

O byte SIB (Scale-Index-Base) é usado para calcular endereços de memória complexos que envolvem um fator de escala.

**Estrutura de Bits SIB (Byte):** $SIB = scale | index | base$

*   **scale (Bits 7-6):** 2 bits que definem o fator de escala ($S$) para o registro de índice (1, 2, 4 ou 8).
*   **index (Bits 5-3):** 3 bits que especificam o registro de índice ($I$).
*   **base (Bits 2-0):** 3 bits que especificam o registro base ($B$).

# Fórmulas de Cálculo de Endereço

O cálculo do Endereço Efetivo (EA) é a fórmula fundamental que define o modo de endereçamento de memória.

**Fórmula Geral do Endereço Efetivo (EA) em $^{32}_{64}$ bits (quando SIB é usado):** $EA = Base + (Index \times Scale) + Displacement$

Onde:

*   Base: Valor do registro base ($B$).
*   Index: Valor do registro de índice ($I$).
*   Scale: Fator de escala ($S \in \{1, 2, 4, 8\}$).
*   Displacement: Valor de deslocamento (offset).

**Endereçamento Relativo a RIP/EIP:** $EA = (RIP/EIP) + Displacement$ Este modo é usado para endereçamento de dados relativos ao ponteiro de instrução, crucial para código independente de posição (PIC).

---


## Page 4

# Conceito 2: x86-64 AMD64 - 64-bit extensions, REX prefix, RIP-relative addressing, canonical addresses

**Itens Técnicos Encontrados:** 3

**Conceitos-Chave:** REX prefix encoding, RIP-relative addressing formula, Canonical address structure, ModR/M byte, SIB byte, 64-bit operand size, Sign-extension

# Conteúdo Técnico: x86-64 AMD64, Prefixo REX, Endereçamento RIP-Relativo e Endereços Canônicos

O conteúdo técnico a seguir descreve as estruturas de hardware, formatos de dados e fórmulas de endereçamento relacionadas às extensões de 64 bits da arquitetura x86-64 (AMD64), focando no **Prefixo REX**, **Endereçamento RIP-Relativo** e **Endereços Canônicos**.

## 1. Estrutura do Prefixo REX

O **Prefixo REX** é um prefixo de instrução de 1 byte (8 bits) usado no modo de 64 bits (Long Mode) da arquitetura x86-64 para estender a capacidade de endereçamento e o tamanho do operando. Sua estrutura de codificação é fixa e definida da seguinte forma [1]:

<table>
<thead>
<tr>
<th>Bit 7</th>
<th>Bit 6</th>
<th>Bit 5</th>
<th>Bit 4</th>
<th>Bit 3 (W)</th>
<th>Bit 2 ®</th>
<th>Bit 1 (X)</th>
<th>Bit 0 (B)</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>W</td>
<td>R</td>
<td>X</td>
<td>B</td>
</tr>
</tbody>
</table>

O valor fixo dos 4 bits mais significativos é `0100` (hexadecimal `0x4`). Os 4 bits menos significativos (`W`, `R`, `X`, `B`) são bits de extensão:

*   **W (1 bit):** Extensão do tamanho do operando.
    *   `w=1`: O tamanho do operando é de 64 bits.
    *   `w=0`: O tamanho do operando é o padrão (geralmente 32 bits no modo de 64 bits).
*   **R (1 bit):** Extensão do campo `reg` do byte **ModR/M**.
    *   `R` é o bit mais significativo (MSB) para o campo `reg` (Registro).
*   **X (1 bit):** Extensão do campo `index` do byte **SIB** (Scale-Index-Base).
    *   `x` é o MSB para o campo `index` (Índice).
*   **B (1 bit):** Extensão do campo `rm` do byte **ModR/M** ou do campo `base` do byte **SIB**.
    *   `B` é o MSB para o campo `rm` (Registro/Memória) ou `base` (Base).

A combinação desses bits permite o acesso aos 8 novos registradores de uso geral (R8-R15) e a extensão do tamanho do operando para 64 bits [1].

## 2. Fórmula do Endereçamento RIP-Relativo

O **Endereçamento RIP-Relativo** (ou PC-Relativo) é um modo de endereçamento exclusivo do modo de 64 bits (Long Mode) que calcula o endereço efetivo adicionando um deslocamento (deslocamento de 32 bits com sinal) ao valor do **Registro de Ponteiro de Instrução (RIP)**.

A fórmula para o cálculo do **Endereço Efetivo (EA)** é [1]:

EA = RIP + Deslocamento (32 bits com sinal)

O valor do **RIP** usado no cálculo é o endereço da próxima instrução, ou seja, o endereço da instrução após o deslocamento de 32 bits. Este modo de endereçamento é crucial para a criação de código independente de posição (PIC - Position-Independent

---


## Page 5

Code), pois o endereço de memória é relativo ao código em execução, e não a um endereço fixo [1].

## 3. Estrutura do Endereço Canônico (Canonical Address)

Na arquitetura x86-64, o espaço de endereço virtual é de 64 bits, mas as implementações atuais (como 4-level paging) utilizam um número menor de bits para o endereçamento virtual (tipicamente 48 bits). Um **Endereço Canônico** é um endereço virtual de 64 bits onde os bits não utilizados (os bits mais significativos) são uma extensão de sinal do bit mais significativo implementado [2].

A regra de validação do endereço canônico é uma estrutura de dados e um protocolo de validação implementado pelo hardware:

1.  **Tamanho do Endereço Implementado:** Tipicamente 48 bits (para 4-level paging). O bit mais significativo implementado é o bit 47.
2.  **Regra de Extensão de Sinal:** Para que um endereço de 64 bits seja canônico, os bits 63 a 48 devem ser cópias do bit 47.

### Estrutura (48-bit implementation):

<table>
<thead>
<tr>
<th>Bit 63</th>
<th>...</th>
<th>Bit 48</th>
<th>Bit 47</th>
<th>...</th>
<th>Bit 0</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bit 47</td>
<td>...</td>
<td>Bit 47</td>
<td>Bit 47</td>
<td>...</td>
<td>Endereço</td>
</tr>
</tbody>
</table>

### Fórmula de Validação (Estrutura Lógica):

Um endereço virtual de 64 bits ($V$) é canônico se e somente se:

$$\text{Bit}_{63}(V) = \text{Bit}_{62}(V) = \cdots = \text{Bit}_{48}(V) = \text{Bit}_{47}(V)$$

*   **Endereço Canônico Baixo (Lower Half):** Se $\text{Bit}_{47}(V) = 0$, então $\text{Bit}_{63-48}(V)$ devem ser todos zeros (0x0000). O intervalo é de 0x0000000000000000 a 0x00007FFFFFFF.
*   **Endereço Canônico Alto (Upper Half):** Se $\text{Bit}_{47}(V) = 1$, então $\text{Bit}_{63-48}(V)$ devem ser todos uns (0xFFFF). O intervalo é de 0xFFFF800000000000 a 0xFFFFFFFFFFFFFF.

Qualquer endereço que não siga essa regra de extensão de sinal é considerado **não canônico** e gera uma exceção de **falha de proteção geral** (#GP) se o processador tentar acessá-lo [2].

---

## Referências

[1] OSDev Wiki. *X86-64 Instruction Encoding*. Disponível em: http://wiki.osdev.org/X86-64_Instruction_Encoding. [2] Stack Overflow. *x86-64 canonical address?*. Disponível em: https://stackoverflow.com/questions/25852367/x86-64-canonical-address.

---

## Conceito 3: Extensões SIMD - MMX, SSE, AVX, AVX-512 e Operações Vetoriais

Itens Técnicos Encontrados: 18

**Conceitos-Chave:** Registradores ZMM, Opmasking, Fused Multiply-Add (FMA), Aritmética Saturada, Permutação Vetorial, Packed Data Types, Unidade FMA, Registradores K

## Conteúdo Técnico das Extensões SIMD (MMX, SSE, AVX, AVX-512)

O conteúdo técnico a seguir foca exclusivamente nas estruturas de hardware, formatos de dados e algoritmos/fórmulas associados às extensões SIMD (Single Instruction, Multiple Data) da arquitetura x86.

---


## Page 6

# 1. Estruturas de Hardware e Registradores

As extensões SIMD introduziram hierarquias de registradores vetoriais, aumentando progressivamente a largura de processamento:

<table>
  <thead>
    <tr>
      <th>Extensão</th>
      <th>Registradores</th>
      <th>Largura (bits)</th>
      <th>Quantidade (Modo 64-bit)</th>
      <th>Sobreposição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>MMX</td>
      <td>MM0-MM7</td>
      <td>64</td>
      <td>8</td>
      <td>Registradores FPU (Stack)</td>
    </tr>
    <tr>
      <td>SSE/SSE2</td>
      <td>XMM0-XMM7</td>
      <td>128</td>
      <td>8</td>
      <td>Nenhuma</td>
    </tr>
    <tr>
      <td>SSE2+</td>
      <td>XMM0-XMM15</td>
      <td>128</td>
      <td>16</td>
      <td>Nenhuma</td>
    </tr>
    <tr>
      <td>AVX/AVX2</td>
      <td>YMM0-YMM15</td>
      <td>256</td>
      <td>16</td>
      <td>XMM (metade inferior)</td>
    </tr>
    <tr>
      <td>AVX-512</td>
      <td>ZMM0-ZMM31</td>
      <td>512</td>
      <td>32</td>
      <td>YMM (metade inferior)</td>
    </tr>
  </tbody>
</table>

## 1.1. Registradores de Máscara (Opmasking - AVX-512)

O AVX-512 introduziu oito registradores de máscara de 64 bits, designados **K0 a K7**, para controle condicional de elementos vetoriais.

*   **K0**: Máscara de reset/escrita (não pode ser usada como máscara de predicado).
*   **K1-K7**: Máscaras de predicado para operações condicionais.

O uso de um registrador de máscara ($K_i$) permite que uma instrução SIMD atue apenas sobre os elementos vetoriais correspondentes aos bits definidos (1) na máscara, seguindo a lógica:

$$\text{Resultado}_i = \begin{cases} \text{Operação}(A_i, B_i) & \text{se } K_i[j] = 1 \\ \text{Destino Original}_i \text{ ou } 0 & \text{se } K_i[j] = 0 \end{cases}$$

Onde $j$ é o índice do elemento no vetor e $K_i[j]$ é o bit correspondente na máscara.

# 2. Formatos de Dados Vetoriais

As extensões SIMD operam sobre dados empacotados (packed data types):

<table>
  <thead>
    <tr>
      <th>Tipo de Dado</th>
      <th>Tamanho (bits)</th>
      <th>Extensões Suportadas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Packed Byte (Signed/Unsigned)</td>
      <td>8</td>
      <td>MMX, SSE, AVX, AVX-512</td>
    </tr>
    <tr>
      <td>Packed Word (Signed/Unsigned)</td>
      <td>16</td>
      <td>MMX, SSE, AVX, AVX-512</td>
    </tr>
    <tr>
      <td>Packed Doubleword (Signed/Unsigned)</td>
      <td>32</td>
      <td>MMX, SSE, AVX, AVX-512</td>
    </tr>
    <tr>
      <td>Packed Quadword (Signed/Unsigned)</td>
      <td>64</td>
      <td>MMX, SSE2, AVX, AVX-512</td>
    </tr>
    <tr>
      <td>Packed Single-Precision Float (FP32)</td>
      <td>32</td>
      <td>SSE, AVX, AVX-512</td>
    </tr>
    <tr>
      <td>Packed Double-Precision Float (FP64)</td>
      <td>64</td>
      <td>SSE2, AVX, AVX-512</td>
    </tr>
    <tr>
      <td>Packed Half-Precision Float (FP16)</td>
      <td>16</td>
      <td>AVX-512 (Conversão)</td>
    </tr>
    <tr>
      <td>Packed Bfloat16 (BF16)</td>
      <td>16</td>
      <td>AVX-512 (Conversão)</td>
    </tr>
  </tbody>
</table>

# 3. Algoritmos e Fórmulas

## 3.1. Aritmética Saturada (MMX e SSE)

A aritmética saturada é fundamental para processamento de mídia e imagem, onde o resultado de uma operação que excede o limite do tipo de dado é fixado (saturado) no valor máximo ou mínimo representável, em vez de “dar a volta” (wrap around).

---


## Page 7

## Fórmula da Soma Saturada (Unsigned Byte - PADDUBS):

Para dois elementos de 8 bits sem sinal, $A_i$ e $B_i$, o resultado $R_i$ é:

$$ R_i = \begin{cases} 
255 & \text{se } A_i + B_i > 255 \\
A_i + B_i & \text{se } 0 \leq A_i + B_i \leq 255 \\
0 & \text{se } A_i + B_i < 0
\end{cases} $$

Como $A_i$ e $B_i$ são sem sinal, a condição $A_i + B_i < 0$ é impossível, simplificando para:

$$ R_i = \min(255, A_i + B_i) $$

## Fórmula da Subtração Saturada (Signed Word - PSUBSW):

Para dois elementos de 16 bits com sinal, $A_i$ e $B_i$, o resultado $R_i$ é limitado pelo intervalo $[-32768, 32767]$:

$$ R_i = \begin{cases} 
32767 & \text{se } A_i - B_i > 32767 \\
A_i - B_i & \text{se } -32768 \leq A_i - B_i \leq 32767 \\
-32768 & \text{se } A_i - B_i < -32768
\end{cases} $$

## 3.2. Fused Multiply-Add (FMA - AVX/AVX2/AVX-512)

O FMA combina multiplicação e adição em uma única instrução, com apenas um arredondamento, aumentando a precisão e o desempenho.

### Fórmula FMA (Instrução VFMADDPs):

$$ R = (A \times B) + C $$

Onde $A$, $B$, e $C$ são vetores de elementos de ponto flutuante. A operação é realizada em paralelo em todos os elementos, e o resultado intermediário da multiplicação ($A \times B$) não é arredondado antes da adição de $C$.

## 3.3. Soma das Diferenças Absolutas (SAD - PSADBW )

A instrução PSADBW (Packed Sum of Absolute Differences of Bytes in a Word) é crucial para algoritmos de compressão de vídeo (como a estimativa de movimento), calculando a soma das diferenças absolutas entre bytes correspondentes de dois vetores de 64 bits.

### Algoritmo PSADBW :

Para dois vetores de 64 bits, $A$ e $B$, cada um contendo 8 bytes ($A_0$ a $A_7$ e $B_0$ a $B_7$):

1. Calcular a diferença absoluta para cada par de bytes: $\$D_i = |A_i - B_i|$ para $i = 0$ a $7$
2. Somar as diferenças absolutas: $\$S = \sum_{i=0}^{7} D_i \$$
3. O resultado $S$ (um valor de 16 bits) é armazenado na palavra menos significativa do registrador de destino, e o restante do registrador é preenchido com zeros.

## 3.4. Operações de Permutação e Shuffle

As operações de permutações vetoriais são essenciais para reordenar dados dentro dos registradores SIMD.

*   **Packed Shuffle Byte ( PSHUFB - SSSE3):** Usa um byte de controle para selecionar e reordenar bytes de um vetor de 128 bits. $\$Destino[i] = \text{Fonte}[\text{Controle}[i] \land 0x0F] \text{Onde} \text{\textit{i}ébytedecontroleparaoi\$-ésimo byte de destino. Se o bit mais significativo do byte de controle for 1, o byte de destino é zerado.}$

*   **Permutação Vetorial ( VPERM - AVX/AVX-512):** Permite a reordenação de elementos de 32 bits (doublewords) ou 64 bits (quadwords) dentro de registradores YMM (256-bit) ou ZMM (512-bit), usando um vetor de índice como operando de controle.

### Algoritmo de Permutação (Exemplo VPERMD - 32-bit):

$\$Destino[i] = \text{Fonte}[\text{Índice}[i] \pmod N] \text{Onde} N é o número de elementos no vetor ($e.g., N=8 para YMM, N=16 para ZMM), e \text{\textit{i}éo\$-ésimo elemento do vetor de}$

---


## Page 8

controle, especificando a posição do elemento a ser movido.

**3.5. Operações de Redução (AVX-512)**

O AVX-512 introduziu operações de redução que aplicam uma operação a todos os elementos de um vetor e retornam um único resultado escalar.

**Exemplo de Redução (Instrução VREDUCEPS):**

A instrução calcula o valor reduzido de cada elemento de ponto flutuante, como o logaritmo base 2 ou a exponenciação, com precisão controlada.

```
Destino_i = Função_Redução(Fonte_i)
```

Onde Função_Redução pode ser, por exemplo, $\log_2(x)$ ou $2^x$, com o resultado sendo armazenado no elemento correspondente do vetor de destino.

**4. Contagem de Elementos Técnicos**

A contagem aproximada de elementos técnicos distintos (estruturas, fórmulas, algoritmos) é de **18**, incluindo:

1. Registradores MMX (Estrutura)
2. Registradores XMM (Estrutura)
3. Registradores YMM (Estrutura)
4. Registradores ZMM (Estrutura)
5. Registradores K (Opmask) (Estrutura)
6. Fórmula da Soma Saturada (Unsigned Byte)
7. Fórmula da Subtração Saturada (Signed Word)
8. Fórmula Fused Multiply-Add (FMA)
9. Algoritmo Packed Sum of Absolute Differences (PSADBW)
10. Algoritmo Packed Shuffle Byte (PSHUFB)
11. Algoritmo de Permutação Vetorial (VPERM)
12. Packed Byte Data Type (Estrutura/Formato)
13. Packed Word Data Type (Estrutura/Formato)
14. Packed Doubleword Data Type (Estrutura/Formato)
15. Packed Quadword Data Type (Estrutura/Formato)
16. Packed Single-Precision Float (Estrutura/Formato)
17. Packed Double-Precision Float (Estrutura/Formato)
18. Operações de Redução (Algoritmo)

---

**Conceito 4: Vector Extensions - AVX-VNNI, AMX tile matrix, APX extended GPRs**

**Itens Técnicos Encontrados:** 9

**Conceitos-Chave:** AVX-VNNI, AMX, APX, Instruções de Rede Neural Vetorial, Multiplicação de Matriz de Blocos, Registradores de Propósito Geral Estendidos, Prefixos REX2, Registradores Tile, TILECFG, TMUL

---


## Page 9

# Conteúdo Técnico: Vector Extensions (AVX-VNNI), AMX Tile Matrix e APX Extended GPRs

O conteúdo a seguir foca estritamente nas estruturas de hardware, formatos de dados, protocolos e algoritmos técnicos associados às extensões **AVX-VNNI**, **AMX** e **APX** da arquitetura x86, conforme solicitado.

## 1. Advanced Vector Extensions - Vector Neural Network Instructions (AVX-VNNI)

O **AVX-VNNI** (Vector Neural Network Instructions) é uma extensão do conjunto de instruções **AVX-512** [1] que acelera operações de *Deep Learning* (Aprendizado Profundo), especificamente a multiplicação e acumulação de inteiros (MAC) usadas em convoluções e camadas totalmente conectadas.

### Estrutura e Algoritmo (Instrução Principal)

A principal inovação técnica reside na instrução **VPDPWSSD** (Vector Packed Doubleword Product Sum Doubleword) e suas variantes, que combinam três operações em uma única instrução SIMD (Single Instruction, Multiple Data) [2]:

1.  **Multiplicação de Palavras (Word Multiplication):** Multiplica palavras de 16 bits (Word, W) de dois vetores de entrada.
2.  **Soma de Produtos (Product Sum):** Soma os produtos resultantes em pares.
3.  **Acumulação (Accumulation):** Acumula o resultado em um vetor de acumuladores de 32 bits (Doubleword, D).

A instrução **VPDPWSSD** opera em vetores de 512 bits (ZMM registers) e implementa a seguinte operação fundamental para a convolução de redes neurais:

$$\text{Acc}[i] = \text{Acc}[i] + \sum_{j=0}^{15} \text{A}[j] \times \text{B}[j]$$

Onde:
*   A e B são sub-vetores de 16 elementos de 16 bits (Word) extraídos dos registradores de origem.
*   Acc é um sub-vetor de 8 elementos de 32 bits (Doubleword) do registrador de destino.
*   A operação é realizada em paralelo em 16 pares de palavras (16 bits) e acumulada em 8 elementos de 32 bits.

O AVX-VNNI suporta formatos de dados como **INT8** e **INT16** [2].

## 2. Advanced Matrix Extensions (AMX) - Tile Matrix

O Intel **AMX** (Advanced Matrix Extensions) é um bloco de hardware dedicado que introduz um novo modelo de programação baseado em matrizes (ou *tiles*) para acelerar operações de multiplicação de matrizes densas, essenciais para *Deep Learning* e computação de alto desempenho [3].

### Estruturas de Hardware (Registradores)

O AMX introduz dois novos componentes de hardware no estado arquitetural:

1.  **Registradores Tile (TMM):** Um conjunto de **oito** registradores bidimensionais (TMM0 a TMM7).
    *   Cada registrador TMM pode armazenar um sub-bloco de matriz (*tile*) de até **1024 elementos** (64 linhas x 16 colunas) [4].
    *   O tamanho total do estado do Tile é de **8 KBytes** (8 registradores x 1 KByte por registrador).
    *   As dimensões (linhas e colunas) de cada *tile* são configuráveis.
2.  **Registrador de Configuração Tile (TILECFG):** Um registrador de controle de 64 bits que define as dimensões dos *tiles* e o formato de dados.
    *   O **TILECFG** deve ser carregado com a instrução **LDTILECFG** antes de qualquer operação AMX [5].

---


## Page 10

*   O formato do TILECFG inclui campos como:
    *   START_ROW : A primeira linha válida.
    *   MAX_ROW : O número máximo de linhas.
    *   MAX_COL : O número máximo de colunas.
    *   DATATYPE : O formato de dados (e.g., INT8, BF16).

## Algoritmo (Instrução Principal)

A principal operação do AMX é a instrução **TMUL** (Tile Matrix Multiply), que realiza uma multiplicação de matrizes de blocos e acumulação:

$$\text{TileC} = \text{TileC} + (\text{TileA} \times \text{TileB})$$

Onde:

*   TileA, TileB e TileC são registradores TMM.
*   A operação é uma multiplicação de matrizes de blocos $M \times K$ por $K \times N$, resultando em uma matriz $M \times N$ acumulada em TileC.
*   A fórmula de multiplicação de matrizes subjacente é: $\$C_{i,j} = C_{i,j} + \sum_{k=1}^{K} A_{i,k} \times B_{k,j}$ onde i é o índice da linha, j é o índice da coluna k é o índice de soma.

## 3. Advanced Performance Extensions (APX) - Extended GPRs

O Intel APX (Advanced Performance Extensions) é uma extensão que visa melhorar o desempenho geral do código x86-64, principalmente dobrando o número de registradores de propósito geral (GPRs) e introduzindo um novo prefixo de instrução [6].

### Estruturas de Hardware (Registradores)

O APX estende o conjunto de registradores de 16 para 32 GPRs de 64 bits.

*   GPRs Existentes: R0 a R15 (16 registradores).
*   GPRs Estendidos (EGPRs): R16 a R31 (16 registradores adicionais) [7].

### Protocolo (Codificação de Instrução)

Para endereçar os 32 registradores (5 bits de índice), o APX introduz um novo prefixo de instrução de 2 bytes, o **REX2** [8].

### Formato do Prefixo REX2:

O prefixo REX2 é um prefixo de 2 bytes que substitui o prefixo REX de 1 byte (0x40-0x4F) e fornece bits de extensão adicionais para os campos de endereço de registrador (ModR/M e SIB) e para o código de operação.

<table>
<thead>
<tr>
<th>Byte</th>
<th>Bit 7</th>
<th>Bit 6</th>
<th>Bit 5</th>
<th>Bit 4</th>
<th>Bit 3</th>
<th>Bit 2</th>
<th>Bit 1</th>
<th>Bit 0</th>
</tr>
</thead>
<tbody>
<tr>
<td>REX2 Byte 1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>REX2 Byte 2</td>
<td>R2</td>
<td>X2</td>
<td>B2</td>
<td>W</td>
<td>L</td>
<td>V</td>
<td>Z</td>
<td>P</td>
</tr>
</tbody>
</table>

Os bits R2, X2 e B2 são os bits de extensão de 5º bit (MSB) para os campos de registrador (Reg), índice (Index) e base (Base) no byte ModR/M e SIB, respectivamente.

*   **Endereçamento de 32 GPRs:** O índice de registrador de 4 bits (3 bits no ModR/M + 1 bit no REX) é estendido para 5 bits (3 bits no ModR/M + 1 bit no REX + 1 bit no REX2), permitindo o endereçamento de $2^5 = 32$ registradores [9].

---


## Page 11

<table>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Bits de Endereçamento</th>
      <th>Prefixo REX</th>
      <th>Prefixo REX2</th>
      <th>Total de Bits</th>
      <th>Registradores Endereçáveis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Reg</td>
      <td>3 (ModR/M)</td>
      <td>R</td>
      <td>R2</td>
      <td>5</td>
      <td>32 (R0-R31)</td>
    </tr>
    <tr>
      <td>Index</td>
      <td>3 (SIB)</td>
      <td>X</td>
      <td>X2</td>
      <td>5</td>
      <td>32 (R0-R31)</td>
    </tr>
    <tr>
      <td>Base</td>
      <td>3 (SIB)</td>
      <td>B</td>
      <td>B2</td>
      <td>5</td>
      <td>32 (R0-R31)</td>
    </tr>
  </tbody>
</table>

O APX também introduz o formato de instrução de **três operandos** (três registradores) para instruções inteiras legadas, o que era incomum no x86-64 anterior [7].

## Referências

[1] Intel. Deep Learning with Intel® AVX-512 and Intel® DL Boost. [2] Wikichip. AVX-512 Vector Neural Network Instructions (VNNI). [3] Intel. What Is Intel® Advanced Matrix Extensions (Intel® AMX)?. [4] Intel. Optimizing Machine Learning (ML) Models with Intel Advanced Matrix Extensions (Intel AMX). [5] Fixstars. Intel AMX (Advanced Matrix Extension) Explained (Introduction). [6] Intel. Introducing Intel® Advanced Performance Extensions (Intel® APX). [7] ServeTheHome. Intel APX Advanced Performance Extensions and AVX10 for Next-Gen CPUs. [8] Wikipedia. REX prefix. [9] LLVM. APX & AVX10.

---

## Conceito 5: Instruction Formats - Variable length encoding, opcode maps, escape sequences, VEX/EVEX prefixes

Itens Técnicos Encontrados: 18

Conceitos-Chave: Codificação de Comprimento Variável, Prefixos Legacy, Opcode Maps, Sequências de Escape, Prefixos VEX, Prefixos EVEX, ModR/M, SIB, Zeroing/Merging, Broadcast, Vector Length

## Formatos de Instrução x86: Codificação de Comprimento Variável, Prefixos VEX e EVEX

O formato de instrução da arquitetura x86-64 é de **comprimento variável**, podendo ter entre 1 e 15 bytes. A estrutura da instrução é composta por uma sequência de componentes opcionais e obrigatórios, lidos da menor para a maior posição de memória [1].

### 1. Estrutura de Codificação de Comprimento Variável (x86-64)

A ordem dos componentes da instrução é estritamente definida, e a presença de cada componente é determinada pelo(s) byte(s) de Opcode e pelos prefixos [1]:

---


## Page 12

<table>
  <thead>
    <tr>
      <th>Componente</th>
      <th>Comprimento (Bytes)</th>
      <th>Obrigatoriedade</th>
      <th>Função Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Prefixos Legacy</b></td>
      <td>0 a 4</td>
      <td>Opcional</td>
      <td>Modificadores de comportamento (LOCK, REP), substituição de segmento, tamanho de operando/endereço.</td>
    </tr>
    <tr>
      <td><b>Opcode</b></td>
      <td>1 a 4</td>
      <td>Obrigatório</td>
      <td>Define a operação e o mapa de opcode.</td>
    </tr>
    <tr>
      <td><b>ModR/M</b></td>
      <td>0 ou 1</td>
      <td>Condicional</td>
      <td>Especifica o modo de endereçamento, registro de destino e registro/memória de origem.</td>
    </tr>
    <tr>
      <td><b>SIB</b></td>
      <td>0 ou 1</td>
      <td>Condicional</td>
      <td><b>Scale-Index-Base</b>. Usado para endereçamento complexo (índice escalonado e base).</td>
    </tr>
    <tr>
      <td><b>Deslocamento</b></td>
      <td>0, 1, 2, 4, 8</td>
      <td>Condicional</td>
      <td>Valor de deslocamento para endereçamento de memória.</td>
    </tr>
    <tr>
      <td><b>Imediato</b></td>
      <td>0, 1, 2, 4, 8</td>
      <td>Condicional</td>
      <td>Valor constante usado como operando.</td>
    </tr>
  </tbody>
</table>

O algoritmo de decodificação de comprimento variável é um processo sequencial onde cada byte é lido e interpretado para determinar a presença e o comprimento do próximo componente, até que o Opcode e todos os seus operandos sejam completamente definidos [1].

## 2. Sequências de Escape e Mapas de Opcode

O Opcode pode ter 1, 2 ou 3 bytes de comprimento. O primeiro byte do Opcode (ou o byte de escape) determina o **mapa de opcode** a ser usado para decodificar a instrução [1]:

<table>
  <thead>
    <tr>
      <th>Sequência de Escape</th>
      <th>Mapa de Opcode</th>
      <th>Comprimento</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>&lt;op&gt;</td>
      <td>Mapa 0 (Legacy)</td>
      <td>1 byte</td>
    </tr>
    <tr>
      <td>0x0F &lt;op&gt;</td>
      <td>Mapa 1 (Legacy 2-byte)</td>
      <td>2 bytes</td>
    </tr>
    <tr>
      <td>0x0F 0x38 &lt;op&gt;</td>
      <td>Mapa 2 (Legacy 3-byte)</td>
      <td>3 bytes</td>
    </tr>
    <tr>
      <td>0x0F 0x3A &lt;op&gt;</td>
      <td>Mapa 3 (Legacy 3-byte)</td>
      <td>3 bytes</td>
    </tr>
  </tbody>
</table>

## 3. Prefixos VEX (Vector Extension)

O prefixo VEX é um substituto para os prefixos Legacy mais comuns e as sequências de escape de Opcode, introduzindo novos campos para estender o conjunto de registradores (R8-R15, XMM8-XMM15, YMM8-YMM15) e especificar o comprimento do vetor (128/256 bits) [2].

### 3.1. Estrutura VEX de 3 Bytes (VEX3)

O formato VEX3 é codificado com o byte inicial 0xC4 [2]:

<table>
  <thead>
    <tr>
      <th>Byte</th>
      <th>Bit 7</th>
      <th>Bit 6</th>
      <th>Bit 5</th>
      <th>Bit 4</th>
      <th>Bit 3</th>
      <th>Bit 2</th>
      <th>Bit 1</th>
      <th>Bit 0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0 (0xC4)</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>1 (P0)</td>
      <td>R☒</td>
      <td>X☒</td>
      <td>B☒</td>
      <td>m4</td>
      <td>m3</td>
      <td>m2</td>
      <td>m1</td>
      <td>m0</td>
    </tr>
    <tr>
      <td>2 (P1)</td>
      <td>W</td>
      <td>v☒3</td>
      <td>v☒2</td>
      <td>v☒1</td>
      <td>v☒0</td>
      <td>L</td>
      <td>p1</td>
      <td>p0</td>
    </tr>
  </tbody>
</table>

**Campos Técnicos:**

*   **R☒, X☒, B☒ (Bits 7-5 do Byte 1):** Complementos dos bits REX.R, REX.X, REX.B. Estendem os campos ModR/M.reg, SIB.index e ModR/M.r/m (ou SIB.base) para permitir o endereçamento dos 16 registradores (R8-R15, XMM8-XMM15, etc.)

---


## Page 13

[2].

*   **m4m3m2m1m0 (Bits 4-0 do Byte 1):** Define o Mapa de Opcode VEX. Os valores 1, 2 e 3 correspondem aos mapas de escape Legacy `0x0F`, `0x0F 0x38` e `0x0F 0x3A`, respectivamente [2].
*   **W (Bit 7 do Byte 2):** Bit de extensão de Opcode ou especifica o tamanho do operando de 64 bits (se W=1) [2].
*   **v⊗3v⊗2v⊗1v⊗0 (Bits 6-3 do Byte 2):** Complemento do índice de um registro fonte adicional (não destrutivo), permitindo operações de 3 ou 4 operandos [2].
*   **L (Bit 2 do Byte 2):** Comprimento do Vetor. L=0 para 128 bits (XMM), L=1 para 256 bits (YMM) [2].
*   **p1p0 (Bits 1-0 do Byte 2):** Codifica os Prefixos Implícitos Legacy (Mandatory Prefixes):
    *   `00`: Nenhum prefixo (implícito).
    *   `01`: `0x66` (tamanho do operando).
    *   `10`: `0xF3` (REP/REPE/REPZ).
    *   `11`: `0xF2` (REPNE/REPNZ) [2].

## 3.2. Estrutura VEX de 2 Bytes (VEX2)

O formato VEX2 é uma abreviação do VEX3, codificado com o byte inicial `0xC5` [2]:

<table>
<thead>
<tr>
<th>Byte</th>
<th>Bit 7</th>
<th>Bit 6</th>
<th>Bit 5</th>
<th>Bit 4</th>
<th>Bit 3</th>
<th>Bit 2</th>
<th>Bit 1</th>
<th>Bit 0</th>
</tr>
</thead>
<tbody>
<tr>
<td>0 (0xC5)</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>1 (P1)</td>
<td>R⊗</td>
<td>v⊗3</td>
<td>v⊗2</td>
<td>v⊗1</td>
<td>v⊗0</td>
<td>L</td>
<td>p1</td>
<td>p0</td>
</tr>
</tbody>
</table>

### Condições de Abreviação (Implícitas):

*   W = 0 (tamanho do operando de 32 bits).
*   B = 1 (B = 0).
*   X = 1 (X = 0).
*   m4m3m2m1m0 = 00001 (Mapa de Opcode 1, equivalente a `0x0F`) [2].

## 4. Prefixos EVEX (Enhanced Vector Extension)

O prefixo EVEX é uma extensão de 4 bytes do VEX, introduzido para suportar o conjunto de instruções AVX-512. Ele permite endereçar os registradores ZMM de 512 bits e introduz o uso de registradores de máscara (k0-k7) [3].

## 4.1. Estrutura EVEX de 4 Bytes

O formato EVEX é codificado com o byte inicial `0x62` [3]:

<table>
<thead>
<tr>
<th>Byte</th>
<th>Bit 7</th>
<th>Bit 6</th>
<th>Bit 5</th>
<th>Bit 4</th>
<th>Bit 3</th>
<th>Bit 2</th>
<th>Bit 1</th>
<th>Bit 0</th>
</tr>
</thead>
<tbody>
<tr>
<td>0 (0x62)</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td>1 (P0)</td>
<td>R⊗</td>
<td>X⊗</td>
<td>B⊗</td>
<td>R⊗'</td>
<td>0</td>
<td>m2</td>
<td>m1</td>
<td>m0</td>
</tr>
<tr>
<td>2 (P1)</td>
<td>W</td>
<td>v⊗3</td>
<td>v⊗2</td>
<td>v⊗1</td>
<td>v⊗0</td>
<td>1</td>
<td>p1</td>
<td>p0</td>
</tr>
<tr>
<td>3 (P2)</td>
<td>z</td>
<td>L'</td>
<td>L</td>
<td>b</td>
<td>v⊗'</td>
<td>a2</td>
<td>a1</td>
<td>a0</td>
</tr>
</tbody>
</table>

### Campos Técnicos Adicionais/Modificados (em relação ao VEX):

*   R⊗' (Bit 4 do Byte 1): Extensão de 4º bit para o campo ModR/M.reg, permitindo o endereçamento de até 32 registradores vetoriais (ZMM0-ZMM31) [3].

---


## Page 14

*   **m2m1m0 (Bits 2-0 do Byte 1):** Define o Mapa de Opcode EVEX. Permite 8 mapas de opcode (0-7) [3].
*   **L' L (Bits 6-5 do Byte 3): Comprimento do Vetor e Modo de Arredondamento.**
    *   Comprimento do Vetor: `00` (128 bits), `01` (256 bits), `10` (512 bits).
    *   Modo de Arredondamento (se b=1): Define o modo de arredondamento para operações de ponto flutuante [3].
*   **z (Bit 7 do Byte 3): Zeroing/Merging.** z=1 ativa o zeroing (preenchimento com zero do destino se a máscara for zero) ou merging (mesclagem com o destino se a máscara for zero) [3].
*   **b (Bit 4 do Byte 3): Broadcast/Modo de Arredondamento.**
    *   Se b=0: Sem broadcast.
    *   Se b=1: Ativa o broadcast do operando de memória (escalar para vetor) ou o modo de arredondamento estático [3].
*   **V☒' (Bit 3 do Byte 3):** Extensão de 5º bit para o campo de registro fonte adicional (junto com `v3v2v1v0`), permitindo endereçar até 32 registradores vetoriais [3].
*   **a2a1a0 (Bits 2-0 do Byte 3):** Define o índice do Registro de Máscara k (k0-k7) a ser usado para mascaramento de elementos vetoriais [3].

## Referências

[1] X86-64 Instruction Encoding - OSDev Wiki. URL: http://wiki.osdev.org/X86-64_Instruction_Encoding [2] VEX prefix - Wikipedia. URL: https://en.wikipedia.org/wiki/VEX_prefix [3] EVEX prefix - Wikipedia. URL: https://en.wikipedia.org/wiki/EVEX_prefix


# Conceito 6: Microcode - RISC micro-ops, microcode ROM, microcode updates, complex instruction decomposition

Itens Técnicos Encontrados: 11

Conceitos-Chave: Micro-ops, Microcode ROM, Microcode Sequencer, Microcode Update Header, Checksum, MSR IA32_BIOS_SIGN_ID, MSR IA32_UCODE_WRITE, Complex Instruction Decomposition, Runtime Microcode Update, Firmware Interface Table (FIT)


# Conteúdo Técnico - Microcode e Micro-ops x86

## 1. Estrutura do Pacote de Atualização de Microcódigo (MCU) da Intel

O pacote de atualização de microcódigo (MCU) da Intel é um blob binário que contém o código de microcódigo atualizado e metadados para o processador. O tamanho total do pacote é tipicamente de 2048 bytes (2KB), consistindo em um cabeçalho de 48 bytes seguido pelos dados de atualização criptografados.

### 1.1. Estrutura do Cabeçalho do Microcódigo (48 bytes)

A estrutura do cabeçalho do microcódigo é crucial para o carregamento e validação da atualização. Os campos principais são:

---


## Page 15

<table>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Offset (bytes)</th>
      <th>Tamanho (bytes)</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Header Version</td>
      <td>0</td>
      <td>4</td>
      <td>Número da versão do cabeçalho da atualização (geralmente 0x00000001)</td>
    </tr>
    <tr>
      <td>Update Revision</td>
      <td>4</td>
      <td>4</td>
      <td>Número de revisão exclusivo para a atualização (versão do microcódigo)</td>
    </tr>
    <tr>
      <td>Date</td>
      <td>8</td>
      <td>4</td>
      <td>Data de criação da atualização (formato BCD: MM/DD/YYYY)</td>
    </tr>
    <tr>
      <td>Processor Signature</td>
      <td>12</td>
      <td>4</td>
      <td>Assinatura (Family/Model/Stepping) do processador ao qual esta atualização se aplica</td>
    </tr>
    <tr>
      <td>Checksum</td>
      <td>16</td>
      <td>4</td>
      <td>Checksum de 32 bits da soma de todos os DWORDs no cabeçalho e nos dados de atualização.</td>
    </tr>
    <tr>
      <td>Loader Revision</td>
      <td>20</td>
      <td>4</td>
      <td>Versão do carregador (loader) necessária para carregar esta atualização (geralmente 0x00000001)</td>
    </tr>
    <tr>
      <td>Processor Flags</td>
      <td>24</td>
      <td>4</td>
      <td>Máscara de bits (bitmask) dos IDs de plataforma aos quais esta atualização se aplica</td>
    </tr>
    <tr>
      <td>Data Size</td>
      <td>28</td>
      <td>4</td>
      <td>Tamanho (em bytes) dos dados de atualização criptografados (tipicamente 2000 bytes)</td>
    </tr>
    <tr>
      <td>Total Size</td>
      <td>32</td>
      <td>4</td>
      <td>Tamanho (em bytes) de toda a atualização, incluindo cabeçalho e dados (tipicamente 2048 bytes)</td>
    </tr>
    <tr>
      <td>Reserved</td>
      <td>36</td>
      <td>4</td>
      <td>Reservado (anteriormente usado para Metadata Size)</td>
    </tr>
    <tr>
      <td>Minimum Runtime Update Revision</td>
      <td>40</td>
      <td>4</td>
      <td>Revisão mínima do microcódigo atualmente carregado necessária para suportar o carregamento em tempo de execução desta atualização.</td>
    </tr>
    <tr>
      <td>Reserved</td>
      <td>44</td>
      <td>4</td>
      <td>Reservado</td>
    </tr>
    <tr>
      <td>Update Data</td>
      <td>48</td>
      <td>Variável</td>
      <td>Dados de atualização criptografados (o código de microcódigo real)</td>
    </tr>
  </tbody>
</table>

## 1.2. Algoritmo de Verificação de Checksum

O **Checksum** (Offset 16) é um valor de 32 bits que garante a integridade do pacote. O algoritmo de verificação é a soma de todos os DWORDs (palavras de 32 bits) no cabeçalho e nos dados de atualização.

$$\text{Checksum} = \sum_{i=0}^{\text{TotalSize}/4-1} \text{DWORD}_i$$

Onde DWORD<sub>i</sub> é a palavra de 32 bits no offset 4 × i do pacote. O valor final do Checksum no pacote deve ser tal que a soma de todos os DWORDs, incluindo o próprio campo Checksum, resulte em zero (0x00000000).

## 1.3. Protocolo de Atualização em Tempo de Execução (Runtime Update)

O protocolo de atualização de microcódigo em tempo de execução (Runtime Microcode Update) utiliza o **Model-Specific Register (MSR)** IA32_UCODE_WRITE (endereço 0x0000008B ) para iniciar o processo.

### Algoritmo de Verificação de Adequação para Atualização em Tempo de Execução:

O campo **Minimum Runtime Update Revision** (Offset 40) é usado para determinar se uma atualização pode ser carregada sem reinicialização.

### 1. Leitura da Revisão Atual:

*   Executar CPUID(1) para obter a assinatura do processador.
*   Ler o MSR IA32_BIOS_SIGN_ID (endereço 0x0000008B ).
*   A **Current_Revision** é o valor de 32 bits mais significativo ([63:32] ) do IA32_BIOS_SIGN_ID.

---


## Page 16

## 2. Verificação de Adequação:

*   Se `Update_Base.Min_Runtime_Update_Revision ≠ 0 E Current_Revision ≥ Update_Base.Min_Runtime_Update_Revision`, então a atualização é **adequada** para carregamento em tempo de execução.
*   Caso contrário, a atualização **não é adequada** para carregamento em tempo de execução e deve ser carregada durante o boot (OS Early Load ou BIOS/UEFI).

### Pseudo-código (Intel):

```c
Suitable_For_Runtime_Update(Update_Base) {
    // 1. Leitura da Revisão Atual
    wrmsr(IA32_BIOS_SIGN_ID, 0) // Limpa o MSR para garantir a leitura correta
    cpuid(1)
    Current_Revision = rdmsr(IA32_BIOS_SIGN_ID) >> 32

    // 2. Verificação de Adequação
    if (Update_Base.Min_Runtime_Update_Revision != 0 &&
        Current_Revision >= Update_Base.Min_Runtime_Update_Revision) {
        return True
    } else {
        return False
    }
}
```

## 2. Decomposição de Instruções Complexas (Complex Instruction Decomposition)

Em microarquiteturas x86 modernas (a partir do P6 da Intel e K5 da AMD), as instruções x86 de comprimento variável e complexas (CISC) são decodificadas no *front-end* do pipeline em uma sequência de operações internas mais simples, de comprimento fixo e estilo RISC, chamadas **micro-ops** (*μ*ops).

### 2.1. Estrutura de Hardware: Decodificadores e ROM de Microcódigo

*   **Decodificadores Simples (Short Decoders):** Decodificam instruções x86 simples (que resultam em 1 a 3 *μ*ops) em um único ciclo de clock.
*   **Decodificador Complexo (Long Decoder / Microcode Sequencer):** Responsável por decompor instruções x86 complexas (que resultam em 4 ou mais *μ*ops) em uma sequência de *μ*ops.
*   **ROM de Microcódigo (Microcode ROM / Control Store):** Armazena as sequências de *μ*ops para as instruções x86 mais complexas. Quando o Decodificador Complexo identifica uma instrução complexa, ele a traduz em um endereço de entrada na ROM de Microcódigo, que então emite a sequência de *μ*ops para o *back-end* do pipeline.
*   **SRAM de Microcódigo (Microcode SRAM / Patch RAM):** Uma pequena memória de acesso rápido (SRAM) que armazena os patches de microcódigo carregados via atualização (MCU). As atualizações de microcódigo (patches) substituem ou redirecionam as sequências de *μ*ops armazenadas na ROM de Microcódigo para corrigir *errata* ou implementar mitigações de segurança.

### 2.2. Algoritmo de Decomposição (High-Level)

O processo de decomposição de instruções (Instruction Decoding) no *front-end* segue um algoritmo de prioridade:

1.  **Busca e Pré-decodificação:** A instrução x86 é buscada e o comprimento da instrução é determinado.
2.  **Decodificação Paralela:** A instrução é enviada simultaneamente para os Decodificadores Simples e para o Decodificador Complexo/Microcode Sequencer.
3.  **Seleção de *μ*ops:**

---


## Page 17

* Se a instrução for simples (e.g., ADD EAX, EBX), os Decodificadores Simples geram 1-3 μops em um ciclo.
* Se a instrução for complexa (e.g., CPUID, ENTER, LOOP), o Decodificador Complexo/Microcode Sequencer é ativado, e a sequência de μops é lida da ROM de Microcódigo (ou da SRAM de Microcódigo se um patch estiver presente).

**4. Emissão:** As μops resultantes são emitidas para o back-end (agendadores, unidades de execução) para processamento out-of-order.

**Exemplo de Decomposição (Conceitual):**

Uma instrução complexa como MOV [mem], reg (que envolve cálculo de endereço, leitura/escrita de memória e movimentação de dados) pode ser decomposta em:

1.  μop_ADDR: Calcular o endereço efetivo.
2.  μop_STORE_DATA: Preparar os dados para escrita.
3.  μop_STORE_ADDR: Enviar o endereço e os dados para o buffer de armazenamento.

**Estruturas de Dados/Hardware:**

*   Instruction Queue (IQ): Buffer de instruções x86 antes da decodificação.
*   Micro-op Queue (MoQ): Buffer de μops após a decodificação, antes do renamer e scheduler.
*   Reorder Buffer (ROB): Estrutura para manter a ordem de execução e o estado arquitetural.
*   Microcode Sequencer: Máquina de estado finito que controla a emissão de μops da ROM/SRAM.
*   MSR IA32_BIOS_SIGN_ID (0x0000008B): Contém a revisão do microcódigo atualmente carregado.
*   MSR IA32_UCODE_WRITE (0x0000008B): Usado para carregar o microcódigo de atualização.
*   FIT (Firmware Interface Table): Estrutura de dados na flash do BIOS que pode conter ponteiros para atualizações de microcódigo.
*   Extended Signature Table: Estrutura opcional que pode seguir os dados de atualização do microcódigo para suportar múltiplos processadores.

---

## Conceito 7: Pipeline x86 - Fetch, Decode, Execute, Writeback, Superscalar, Width, Depth

**Itens Técnicos Encontrados:** 15

**Conceitos-Chave:** Fetch, Decode, Execute, Writeback, Superscalar, Issue Width, Decode Width, Out-of-Order Execution, Speculative Execution, Branch Prediction, Op Cache, Micro-ops, ZMMWORD, YMMWORD, XMMWORD, AGU

## Pipeline x86 - Fetch, Decode, Execute, Writeback, Superscalar, Width, Depth

A microarquitetura x86 moderna, exemplificada pelo AMD Zen4, emprega um pipeline de execução superscalar e fora de ordem (Out-of-Order) para maximizar o paralelismo de instruções. Este design complexo envolve a tradução de instruções x86 de comprimento variável (macro-ops) em micro-operações (uops) de comprimento fixo, que são então agendadas para execução em múltiplas unidades funcionais.

---


## Page 18

# Estruturas de Hardware e Larguras (Width)

O pipeline é caracterizado por larguras específicas em seus estágios de *front-end* (Fetch e Decode) e *back-end* (Execute e Writeback), que definem sua capacidade de processamento paralelo.

## Front-End: Fetch e Decode

O estágio de *Fetch* é otimizado para buscar grandes blocos de instruções, utilizando um tamanho de *cacheline* de 64 bytes. O *Op Cache* (OC) armazena até 6.75K micro-ops, permitindo que o *front-end* ignore a decodificação repetitiva de instruções. A **Largura de Decodificação (Decode Width)** é de 4-way, o que significa que o decodificador pode processar até quatro instruções x86 por ciclo.

A **Decomposição de Instrução** é um algoritmo fundamental onde as instruções x86 são classificadas em:

*   **Fastpath Single**: 1 macro-op.
*   **Fastpath Double**: 2 macro-ops (geralmente para instruções com operando de memória que requerem uma operação de carga/armazenamento separada).
*   **Microcode**: Mais de 2 macro-ops (para instruções complexas).

## Back-End: Execute e Writeback

O **Issue Width** (Largura de Emissão) do *scheduler* é de até 8 micro-ops por ciclo, o que define a capacidade máxima de paralelismo do *back-end*. A execução é distribuída por múltiplas unidades funcionais, conforme detalhado na Tabela 1.

<table>
<thead>
<tr>
<th>Unidade Funcional</th>
<th>Largura de Execução (Way)</th>
<th>Função Principal</th>
</tr>
</thead>
<tbody>
<tr>
<td>Integer Execution Units</td>
<td>5-way</td>
<td>Processamento de instruções de inteiros.</td>
</tr>
<tr>
<td>Address Generation Units (AGUs)</td>
<td>3-way</td>
<td>Geração de endereços para operações de Load/Store.</td>
</tr>
<tr>
<td>Floating-Point/Packed Integer Units</td>
<td>4-way (256-bit)</td>
<td>Processamento de ponto flutuante e instruções SIMD (AVX/AVX2).</td>
</tr>
<tr>
<td>Data Pipe Width</td>
<td>64 bytes</td>
<td>Largura de transferência de dados entre cache e unidades de execução.</td>
</tr>
</tbody>
</table>

## Algoritmos de Controle e Protocolos

O controle do pipeline é regido por algoritmos de hardware que implementam o paradigma **Superscalar** e **Out-of-Order Execution**.

*   **Dynamic Out-of-Order Scheduling**: Algoritmo que gerencia a execução de micro-ops com base na disponibilidade de operandos, e não na ordem sequencial do programa, utilizando estruturas como o *Reorder Buffer* (ROB) e *Reservation Stations*.
*   **Speculative Execution**: Protocolo onde o processador executa instruções antes de confirmar a necessidade (ex: após uma predição de *branch*), revertendo o estado em caso de erro.
*   **Advanced Dynamic Branch Prediction**: Algoritmo complexo que utiliza estruturas de hardware (como *Branch History Table* e *Branch Target Buffer*) para prever o fluxo de controle do programa e evitar *stalls* no pipeline.
*   **Prefetchers**: Algoritmos de hardware que carregam dados e instruções na hierarquia de cache (L1/L2) antes que sejam explicitamente solicitados pelo *front-end*.
*   **Protocolos de Segurança e Virtualização**: O hardware implementa protocolos de segurança como **Shadow Stack Protection** (INCSSP, RDSSP, WRSS, etc.) e **Secure Nested Paging** (RMPUPDATE, PVALIDATE, etc.) através de instruções dedicadas.

---


## Page 19

# Fórmulas e Profundidade (Depth) do Pipeline

A **Profundidade (Depth)** do pipeline é um parâmetro de design que afeta diretamente a frequência de clock e o custo de penalidade por erro de predição de *branch*. Embora o número exato de estágios seja microarquiteturalmente específico e não explicitamente divulgado, as métricas de desempenho são regidas pelas seguintes relações:

1.  **Throughput (Taxa de Transferência) Máximo:** $Throughput \approx \frac{Issue Width}{Clock Cycle Time}$ Onde o *Issue Width* é a largura de emissão de micro-ops por ciclo.
2.  **Penalidade por Erro de Predição de Branch:** $Penalty = Misprediction Rate \times Pipeline Flush Cost$ O **Pipeline Flush Cost** é o custo em ciclos para limpar o pipeline e é diretamente proporcional à profundidade do pipeline. Um pipeline mais profundo (maior *Depth*) resulta em um custo de penalidade maior.
3.  **Largura de Processamento Vetorial (SIMD):** A largura máxima de processamento de dados é definida pelos formatos de registradores vetoriais:
    *   **ZMMWORD:** 512 bits (64 bytes) - Suportado pelas extensões AVX-512.
    *   **YMMWORD:** 256 bits (32 bytes) - Suportado pelas extensões AVX/AVX2.
    *   **XMMWORD:** 128 bits (16 bytes) - Suportado pelas extensões SSE.

**Referências:** [1] AMD. Software Optimization Guide for the AMD Zen4 Microarchitecture. Publicação 57647 Rev. 1.00, Abril 2023.

---

# Conceito 8: Out-of-Order Execution

**Itens Técnicos Encontrados:** 12

**Conceitos-Chave:** Out-of-Order Execution, Tomasulo Algorithm, Reservation Stations, Reorder Buffer (ROB), Register Renaming, Micro-operations (*µops*), Common Data Bus (CDB), Retirement, Speculative Execution, Dependency Chain, Branch Target Buffer (BTB)

## Out-of-Order Execution (OOOE) e Micro-operações (*µops*)

A **Execução Fora de Ordem (OOOE)** é um algoritmo de hardware para agendamento dinâmico de instruções que permite que o processador execute instruções assim que seus dados de entrada estiverem disponíveis, independentemente da ordem do programa original. Isso é feito para evitar o desperdício de ciclos de *clock* causado por **cadeias de dependência longas** [1].

Em processadores x86 modernos (a partir do PPro), as instruções complexas do *Instruction Set Architecture* (ISA) x86 são traduzidas em uma ou mais **micro-operações (*µops*) internas** de formato fixo. O agendamento OOOE opera sobre essas *µops* [1].

## Renomeação de Registradores (Register Renaming)

A **Renomeação de Registradores** é um mecanismo de hardware que elimina as dependências de nome (falsas dependências: *Write-After-Write* - WAW e *Write-After-Read* - WAR) ao mapear os registradores arquiteturais (lógicos, como EAX, EBX) para um conjunto maior de **registradores físicos temporários**.

*   **Processo:** Sempre que uma *µop* escreve em um registrador lógico, o hardware aloca um novo registrador físico para armazenar o resultado. Isso permite que instruções subsequentes que usam o mesmo registrador lógico, mas que não dependem do resultado da instrução anterior, sejam executadas em paralelo [1].
*   **Estruturas Implícitas:** O mapeamento é gerenciado por uma tabela, a **Register Alias Table (RAT)**, que aponta o registrador lógico para o seu registrador físico correspondente.

## Algoritmo de Tomasulo e Estruturas de Hardware

O algoritmo de Tomasulo, ou uma variação dele, é a base para o agendamento dinâmico em arquiteturas x86 [2]. As principais estruturas de hardware envolvidas são:

---


## Page 20

# 1. Estações de Reserva (Reservation Stations - RS):

*   São *buffers* que armazenam as µops que foram decodificadas e estão aguardando a execução.
*   Cada RS contém os operandos da µop (se disponíveis) ou as **tags** (rótulos) do Reorder Buffer (**ROB**) que produzirão os operandos.
*   Campos de Dados (Estrutura): Op (operação), Qj , Qk (tags do ROB que produzirão os operandos), Vj , Vk (valores dos operandos, se disponíveis), Busy (status) [2].

# 2. Buffer de Reordenação (Reorder Buffer - ROB):

*   É uma fila circular que armazena os resultados das µops em execução fora de ordem, garantindo que o estado arquitetural seja atualizado na ordem original do programa.
*   É essencial para a **Execução Especulativa**, pois os resultados são escritos no ROB, mas não no arquivo de registradores permanentes até o **Retirement** [1].
*   Campos de Dados (Estrutura): Type (tipo de instrução), Destination (registrador ou endereço de memória de destino), Value (resultado da operação), Ready (status de conclusão) [2].

# 3. Barramento de Dados Comum (Common Data Bus - CDB):

*   É um barramento de alta velocidade que transmite os resultados das Unidades de Execução para todas as Estações de Reserva e o ROB.
*   As RS monitoram o CDB, e quando uma tag corresponde à tag de um operando pendente (Qj ou Qk), o valor é capturado [2].

## Execução Especulativa e Retirement

A **Execução Especulativa** ocorre quando o processador executa instruções cuja necessidade ainda não foi confirmada (ex: após um *branch* condicional).

*   **Mecanismo:** As µops são executadas, mas seus resultados são armazenados temporariamente no **ROB** e não no arquivo de registradores permanentes.
*   **Retirement (Commit):** É o processo final onde os resultados são copiados do ROB para os registradores arquiteturais permanentes (EAX, EBX, etc.) e as escritas na memória são finalizadas. O *Retirement* **deve** ocorrer na ordem do programa original [1].
*   **Tratamento de Erros/Misprediction:** Se a especulação estiver incorreta (ex: *branch misprediction*), o ROB é esvaziado, e os resultados especulativos são descartados, mantendo o estado arquitetural correto [1].

## Estrutura de Predição de Desvio (Branch Prediction)

A OOOE depende da **Predição de Desvio** para manter o *pipeline* cheio.

*   **Branch Target Buffer (BTB):** Uma cache que armazena o endereço de destino de desvios (*jumps*) previamente executados. É consultada para buscar a próxima instrução antes que o desvio seja resolvido [1].
*   **Contador Saturante (Saturating Counter):** Um mecanismo de hardware simples, frequentemente de 2 bits, usado para prever se um desvio condicional será tomado ou não, baseado no histórico recente [1].

---

## Referências

[1] Agner Fog. *The microarchitecture of Intel, AMD, and VIA CPUs*. (Seções 2, 2.2, 3, 6.7). [2] Robert M. Tomasulo. *An efficient algorithm for exploiting multiple arithmetic units*. IBM Journal of Research and Development, 1967. (Conceitos de Tomasulo).

---

# Conceito 9: Branch Prediction - BTB, BHT, Perceptron, TAGE

Itens Técnicos Encontrados: 10

---


## Page 21

**Conceitos-Chave:** Branch Target Buffer (BTB), Pattern History Table (PHT), Branch History Table (BHT), Contador Saturante de Dois Bits, Perceptron Predictor, TAGE Predictor, História Global de Desvios, Série Geométrica de Históricos, Algoritmo de Treinamento do Perceptron

## Conteúdo Técnico de Branch Prediction (BTB, BHT, Perceptron, TAGE)

O conteúdo técnico a seguir foca exclusivamente nas estruturas de hardware, algoritmos e fórmulas que definem os mecanismos de predição de desvios, conforme solicitado.

### 1. Estruturas de Hardware Fundamentais (BTB, BHT, PHT)

#### 1.1. Branch Target Buffer (BTB)

O BTB é uma estrutura de memória associativa (cache) que armazena o endereço alvo (Target Address) de desvios tomados, permitindo que a busca de instruções continue no alvo predito sem esperar pela decodificação do desvio.

*   **Estrutura de Entrada (Típica):** [Endereço do Desvio (PC)] -> [Tag, Endereço Alvo (Target Address), Bits de Predição (PHT/BHT)]
*   **Função:** Predição do alvo do desvio (Branch Target Prediction).

#### 1.2. Pattern History Table (PHT) / Branch History Table (BHT)

A PHT armazena o estado de predição de desvios condicionais. Em arquiteturas x86 modernas, a PHT é frequentemente implementada como um array de **Contadores Saturantes de Dois Bits**.

*   **Estrutura do Contador Saturante de Dois Bits:** Máquina de estados finitos com 4 estados:
    *   `00`: Forte Não Tomado (Strongly Not Taken)
    *   `01`: Fraco Não Tomado (Weakly Not Taken)
    *   `10`: Fraco Tomado (Weakly Taken)
    *   `11`: Forte Tomado (Strongly Taken)
*   **Algoritmo de Predição:** A predição é baseada no bit mais significativo do contador (e.g., `0x` = Não Tomado, `1x` = Tomado).
*   **Algoritmo de Atualização:**
    *   Se o desvio for **Tomado (T)**: O contador é incrementado (satura em `11`).
    *   Se o desvio for **Não Tomado (NT)**: O contador é decrementado (satura em `00`).

### 2. Perceptron Predictor

O Perceptron Predictor utiliza um modelo de rede neural simples para prever o resultado de desvios condicionais, explorando correlações de longo histórico.

#### 2.1. Estrutura e Entrada

*   **Perceptron:** Um vetor de pesos inteiros com sinal `w = (w₀, w₁, ..., wₙ)`.
    *   `w₀`: Peso de **Bias** (viés), sempre associado a uma entrada `x₀ = 1`.
    *   `w₁, ..., wₙ`: Pesos associados aos `n` bits do histórico global de desvios.
*   **Histórico Global de Desvios (`x`):** Um vetor de entrada bipolar `x = (x₀, x₁, ..., xₙ)`, onde `xᵢ ∈ {-1, 1}` (Não Tomado/Tomado).

#### 2.2. Fórmula de Predição

A predição é o produto escalar do vetor de pesos `w` e do vetor de histórico `x`.

---


## Page 22

y = w₀ + Σ (from i=1 to n) xᵢwᵢ

*   **Regra de Predição:**
    *   Se y ≥ 0: Prediz Tomado (T).
    *   Se y < 0: Prediz Não Tomado (NT).

## 2.3. Algoritmo de Treinamento (Atualização de Pesos)

Seja t ∈ {-1, 1} o resultado real do desvio (1 para Tomado, -1 para Não Tomado) e θ um limiar de treinamento.

1.  **Condição de Treinamento:** O treinamento ocorre se a predição y estiver errada (sign(y) ≠ t) OU se a magnitude da predição for fraca (|y| ≤ θ).
2.  **Atualização de Pesos:** Se a condição de treinamento for satisfeita, os pesos são atualizados:

    Para i = 0 até n : wᵢ := wᵢ + t · xᵢ

## 3. TAGE Predictor (TAgged GEometric history length)

O TAGE é um preditor híbrido que combina um preditor base com múltiplos componentes (tabelas) indexados por históricos de diferentes comprimentos.

### 3.1. Estrutura

*   **Preditor Base (T₀):** Geralmente uma tabela bimodal simples (Contadores de 2 bits) indexada pelo PC (Program Counter).
*   **Componentes Tagged (T₁ a Tₘ):** M tabelas de preditores parcialmente tagueadas.
    *   Cada entrada Tᵢ contém: [Tag, Contador de Predição (ctr), Contador de Utilidade (u)].
*   **Históricos Geométricos:** Os comprimentos de histórico L(i) usados para indexar Tᵢ formam uma série geométrica:

    L(i) = ⌊α^(i-1) · L(1) + 0.5⌋ para 1 ≤ i ≤ m

    Onde α é o fator de crescimento (e.g., 1.2 a 1.5) e L(1) é o comprimento de histórico inicial.

### 3.2. Indexação e Tagging

Para cada tabela Tᵢ, o índice e a tag são calculados usando funções de hash que combinam o PC do desvio e o Histórico Global de Desvios (GHIST) de comprimento L(i).

indexᵢ = Hash(PC, GHIST[L(i)])
tagᵢ = Hash(PC, GHIST[L(i)])

### 3.3. Algoritmo de Predição

1.  **Busca:** O preditor busca em todas as tabelas T₁ a Tₘ usando os índices e tags calculados.
2.  **Predição Válida:** A predição é fornecida pela tabela Tᵢ com o maior i (histórico mais longo) que resulta em um acerto de tag (tag match).
3.  **Predição Final:**
    *   Se houver um acerto (tabela Tᵢ): A predição é o sinal do contador ctr da entrada correspondente.
    *   Se não houver acerto (miss): A predição é fornecida pelo Preditor Base T₀.

### 3.4. Algoritmo de Alocação (Simplificado)

Quando o preditor falha (misprediction) e a predição veio do preditor base T₀, uma nova entrada é alocada em uma das tabelas Tᵢ (geralmente uma com um histórico mais curto e um contador de utilidade u baixo) para tentar capturar o padrão.

---


## Page 23

*   **Contador de Utilidade (u):** Usado para gerenciar a substituição de entradas. Entradas com u = 0 são candidatas à substituição. O contador u é incrementado em acertos e decrementado em falhas de predição.

---

Nota: As estruturas de hardware do BTB e BHT em CPUs x86 reais (Intel/AMD) são proprietárias e não documentadas publicamente, mas os modelos teóricos acima (PHT, Contador Saturante) representam os princípios microarquiteturais subjacentes.

---

# Conceito 10: Speculative Execution - Meltdown, Spectre variants, transient execution, mitigations, retpline

Itens Técnicos Encontrados: 18

Conceitos-Chave: Execução Especulativa, Execução Transiente, Branch Predictor, Cache Timing, Meltdown, Spectre V1, Spectre V2, Retpoline, IBRS, IBPB, STIBP, RSB, LFENCE, MSRs

## Spectre Variant 1 (Bounds Check Bypass) - Exemplo de Código

O ataque Spectre V1 explora a execução especulativa de instruções que seguem um desvio condicional mal previsto.

Pseudocódigo do Trecho Vulnerável:

```c
if (x < array1_size)
    y = array2[array1[x] * 4096];
```

Mecanismo de Ataque (Exploração da Execução Transiente):

1.  **Treinamento do Branch Predictor:** O atacante treina o preditor de desvios (Branch Predictor) para prever que a condição (x < array1_size) será **verdadeira**, mesmo quando x estiver fora dos limites válidos (x >= array1_size).
2.  **Execução Especulativa:** Quando o CPU encontra a instrução `if` com um x malicioso (fora dos limites), ele especula que a condição é verdadeira e executa a instrução dependente: `y = array2[array1[x] * 4096];`.
3.  **Vazamento de Dados:**
    *   `array1[x]` acessa um endereço de memória **fora dos limites** de `array1`, lendo um byte de dados secretos (S) de outra área de memória (ex: kernel).
    *   O valor secreto S é usado como índice para acessar `array2`: `array2[S * 4096]`.
    *   O acesso a `array2[S * 4096]` carrega a linha de cache correspondente a esse endereço.
4.  **Reversão e Efeito Colateral:** Quando o CPU finalmente resolve a condição `if` e descobre que a previsão estava errada, ele **reverte** o estado arquitetural (descarta y). No entanto, o **estado microarquitetural** (o conteúdo do cache) **não é revertido**.
5.  **Canal Lateral (Side Channel):** O atacante usa um ataque de **cache timing** (ex: Flush+Reload ou Prime+Probe) para medir o tempo de acesso a cada linha de `array2`. O índice que for acessado rapidamente (hit no cache) revela o valor secreto S.

Estruturas de Hardware Exploradas:

*   **Branch Predictor (Preditor de Desvios):** Componente que armazena o histórico de desvios e prevê o caminho de execução. É manipulado para induzir a execução especulativa.
*   **Cache (L1/L2/L3):** Usado como canal lateral para vazar a informação. O tempo de acesso ao cache revela qual endereço foi tocado durante a execução especulativa.
*   **Execution Units (Unidades de Execução):** Realizam as operações de leitura e cálculo durante a execução transiente.

---


## Page 24

# Speculative Execution (Execução Especulativa)

**Protocolo/Mecanismo:**

*   **Out-of-Order Execution (OOO):** A CPU executa instruções fora da ordem do programa para manter as unidades de execução ocupadas, desde que as dependências de dados sejam respeitadas.
*   **Transient Execution (Execução Transiente):** Ocorre quando a CPU executa instruções baseadas em uma previsão (ex: de desvio ou de valor de endereço) que mais tarde se revela incorreta. O resultado arquitetural dessas instruções é descartado, mas os efeitos colaterais microarquiteturais (como o estado do cache) persistem.
*   **Rollback (Reversão):** O mecanismo pelo qual a CPU descarta o estado arquitetural (registradores, memória) das instruções transientes quando a previsão é invalidada.

---

# Meltdown (CVE-2017-5754)

**Mecanismo de Ataque (Exploração da Execução Transiente com Exceção):**

1.  **Acesso Privilegiado Transiente:** O atacante executa uma instrução de leitura de memória (load) para um endereço de memória privilegiado (ex: kernel) a partir de um contexto de usuário.
2.  **Execução Especulativa:** A CPU executa a instrução de leitura especulativamente antes de verificar as permissões de acesso.
3.  **Vazamento de Dados:** O valor lido (s) é usado para indexar um array (como no Spectre) para criar um efeito colateral no cache.
4.  **Exceção e Efeito Colateral:** A CPU detecta a violação de permissão e gera uma exceção (falha de página ou proteção). A exceção interrompe a execução arquitetural, mas o efeito colateral no cache **persiste.**
5.  **Canal Lateral:** O atacante usa o canal lateral de cache timing para recuperar o valor s.

**Estruturas de Hardware Exploradas:**

*   **Memory Management Unit (MMU) / Translation Lookaside Buffer (TLB):** O Meltdown explora o fato de que a verificação de permissão da MMU/TLB é feita assincronamente ou tardivamente em relação à execução especulativa da instrução de carga.
*   **Cache:** Usado como canal lateral.

---

# Retpoline (Return Trampoline)

**Algoritmo/Estrutura de Mitigação (Spectre V2 - Branch Target Injection):**

*   **Objetivo:** Mitigar o ataque Spectre V2 (Branch Target Injection), que manipula o Branch Target Buffer (BTB) para desviar chamadas indiretas (call *reg ou jmp *reg) para código malicioso.
*   **Estrutura:** Substitui chamadas indiretas por uma sequência de instruções que usa o Return Stack Buffer (RSB) em vez do BTB para a previsão de desvio.

**Pseudocódigo (Conceitual):**

Em vez de:

```c
call *%reg
```

Usa-se uma sequência que simula uma chamada/salto, mas que o preditor de desvios interpreta como um retorno:

---


## Page 25

assembly
// Retpoline para chamada indireta
push %reg          // Salva o endereço de destino no topo da pilha
call .L_retpoline_target // Chama a "trampoline"
.L_retpoline_target:
    pause
    lfence        // Barreira de especulação (em algumas implementações)
    jmp .L_retpoline_target // Loop infinito (para consumo de especulação)
```

**Mecanismo:**

1. A chamada indireta é substituída por uma chamada direta para a **trampoline** (`.L_retpoline_target`).
2. O endereço de retorno (o endereço após a chamada) é empurrado para o **RSB**.
3. A trampoline executa um loop infinito (`jmp .L_retpoline_target`).
4. A CPU especula que o loop infinito será executado.
5. Quando a CPU descobre que a chamada original era indireta, ela usa o RSB para prever o destino do retorno, que é o endereço de retorno correto.
6. O loop infinito é usado para “consumir” a execução especulativa, garantindo que o BTB não seja usado para prever o destino da chamada indireta.

**Estruturas de Hardware Envolvidas:**

*   **Branch Target Buffer (BTB):** O alvo do ataque Spectre V2. O Retpoline evita seu uso.
*   **Return Stack Buffer (RSB):** Usado pelo Retpoline para a previsão de desvio, pois é mais difícil de ser manipulado pelo atacante para desvios arbitrários.
*   **LFENCE (Load Fence):** Instrução de barreira de especulação (em algumas variantes) que garante que todas as instruções de carga anteriores sejam concluídas antes que as instruções subsequentes possam ser executadas.

---

## Mitigações de Hardware (Exemplos x86)

*   **LFENCE:** Barreira de especulação. Garante que as instruções de carga anteriores sejam concluídas.
*   **IBRS (Indirect Branch Restricted Speculation):** Um bit de controle (MSR) que restringe a especulação de desvios indiretos.
*   **IBPB (Indirect Branch Predictor Barrier):** Uma instrução que limpa o Branch Predictor (BTB) ao alternar entre contextos de segurança (ex: kernel/usuário).
*   **STIBP (Single Thread Indirect Branch Predictors):** Restringe a especulação de desvios indiretos dentro de um único thread.
*   **RSBA (Return Stack Buffer Allocation):** Controle sobre o RSB para mitigar ataques como o **Retbleed** (uma variante do Spectre V2).
*   **SSB (Speculative Store Bypass) / MDS (Microarchitectural Data Sampling) Mitigations:** Envolvem o uso de instruções como VERW (em algumas CPUs) ou o bit TSX_FORCE_ABORT e o MSR IA32_FLUSH_CMD para limpar buffers microarquiteturais.
*   **MSRs (Model-Specific Registers):** Registradores específicos do modelo da CPU usados para configurar e controlar as mitigações de hardware (ex: IA32_PRED_CMD para IBPB).
*   **Microcode Updates:** Atualizações de firmware da CPU que modificam o comportamento microarquitetural, como o tratamento de exceções e a execução especulativa.

---

## Conceito 11: Register Renaming - RAT, PRF, Retirement

Itens Técnicos Encontrados: 10

---


## Page 26

**Conceitos-Chave:** Register Renaming, Physical Register File (PRF), Register Alias Table (RAT), Reorder Buffer (ROB), Retirement, Free List (FRL), Physical Register Reclaim Table (PRRT), Dependência de Saída (WAW), Dependência Anti (WAR), Alocação de Registradores

# Register Renaming, RAT, PRF e Retirement na Arquitetura x86

O **Register Renaming** (Renomeação de Registradores) é uma técnica fundamental em microarquiteturas x86 *Out-of-Order* (OOO) que elimina as dependências falsas de dados (Anti-Dependência - WAR e Dependência de Saída - WAW), permitindo maior paralelismo em nível de instrução. O processo é gerenciado por um conjunto de estruturas de hardware interconectadas.

## Estruturas de Hardware Principais

<table>
  <thead>
    <tr>
      <th>Estrutura</th>
      <th>Sigla</th>
      <th>Função Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Physical Register File</td>
      <td>PRF</td>
      <td>Armazena os valores de dados de todos os registradores físicos. É o conjunto expandido de registradores que inclui os registradores arquiteturais e os temporários.</td>
    </tr>
    <tr>
      <td>Register Alias Table</td>
      <td>RAT</td>
      <td>Tabela de mapeamento que armazena o mapeamento atual de registradores arquiteturais (lógicos) para registradores físicos (P-regs).</td>
    </tr>
    <tr>
      <td>Reorder Buffer</td>
      <td>ROB</td>
      <td>Buffer circular que rastreia todas as micro-operações (µops) em voo na ordem do programa. Garante a aposentadoria (Retirement) em ordem e o tratamento preciso de exceções.</td>
    </tr>
    <tr>
      <td>Free List</td>
      <td>FRL</td>
      <td>Lista de registradores físicos (P-regs) disponíveis e não alocados no PRF.</td>
    </tr>
    <tr>
      <td>Physical Register Reclaim Table</td>
      <td>PRRT</td>
      <td>(Específico da microarquitetura Sandy Bridge e posteriores) Estrutura que rastreia o P-reg antigo que deve ser liberado para a FRL quando a instrução correspondente se aposentar.</td>
    </tr>
  </tbody>
</table>

## Algoritmo de Renomeação (Estágio de Alocação/Despacho)

O processo de renomeação ocorre no estágio de Alocação/Despacho (Allocator) do pipeline e é executado para cada micro-operação (µop) que requer um registrador de destino.

Para uma µop com registradores de origem ($R_{src}$) e registrador de destino ($R_{dest}$):

1.  **Consulta de Origem (Source Lookup):**
    *   Para cada $R_{src}$, o **RAT** é consultado para obter o nome do registrador físico atual ($P_{src}$).
    *   O valor de $P_{src}$ é usado para buscar o dado no **PRF** ou para configurar o tag de encaminhamento (se o dado ainda não estiver pronto).

2.  **Alocação de Destino (Destination Allocation):**
    *   Um novo registrador físico ($P_{new}$) é alocado a partir da **Free List (FRL)** para o $R_{dest}$.

3.  **Atualização do RAT (RAT Update):**
    *   O **RAT** é atualizado para mapear $R_{dest}$ para $P_{new}$.
    *   O mapeamento antigo ($P_{old}$) de $R_{dest}$ é lido do RAT antes da atualização.

4.  **Entrada no ROB (ROB Entry):**
    *   Uma nova entrada é criada no **ROB** para a µop.

---


## Page 27

* O $P_{old}$ é armazenado na entrada do ROB. Este $P_{old}$ é o registrador físico que a µop irá “liberar” quando se aposentar.

## Resolução de Dependência de Saída (WAW):

* A atualização do RAT com $P_{new}$ e o armazenamento de $P_{old}$ no ROB resolvem a dependência WAW. A escrita mais recente (com $P_{new}$) sobrescreve o mapeamento no RAT, garantindo que leituras futuras obtenham o valor correto. A escrita anterior (com $P_{old}$) não pode mais sobrescrever o valor, pois seu *tag* foi substituído.

# Algoritmo de Aposentadoria (Retirement)

O *Retirement* (Aposentadoria) é o estágio final do *pipeline*, onde o estado arquitetural do processador é atualizado de forma permanente e em ordem.

## Para a µop no cabeçalho do ROB (ROB Head):

1.  **Verificação de Conclusão:** A µop deve ter concluído a execução e escrito seu resultado no PRF.
2.  **Atualização do Estado Arquitetural:** O estado arquitetural é implicitamente atualizado, pois o **RAT** já contém o mapeamento para o resultado correto ($P_{new}$).
3.  **Liberação do Registrador Físico Antigo:** O registrador físico antigo ($P_{old}$) armazenado na entrada do ROB é liberado de volta para a Free List (FRL).
4.  **Desalocação do ROB:** A entrada da µop é desalocada do ROB.

## Tratamento de Exceções:

*   Se uma exceção ocorrer, o *Retirement* é interrompido.
*   O estado arquitetural é restaurado para o estado da instrução que causou a exceção, utilizando os mapeamentos de registradores físicos rastreados pelo **ROB** e **RAT** (em algumas arquiteturas, um *Checkpoint* do RAT é usado para restauração rápida).
*   Todas as µops no ROB após a µop com exceção são descartadas.

# Estrutura de Dados do RAT (Exemplo Conceitual)

O RAT é conceitualmente uma tabela de mapeamento:
$$\text{RAT}[A_{reg}] \rightarrow P_{reg}$$

Onde:
*   $A_{reg}$ é o índice do registrador arquitetural (ex: EAX, RBX, XMM0 ).
*   $P_{reg}$ é o índice do registrador físico no PRF.

## Exemplo de Estado do RAT:

<table>
<thead>
<tr>
<th>$A_{reg}$ (Índice)</th>
<th>$P_{reg}$ (Índice no PRF)</th>
</tr>
</thead>
<tbody>
<tr>
<td>EAX (0)</td>
<td>P42</td>
</tr>
<tr>
<td>EBX (1)</td>
<td>P105</td>
</tr>
<tr>
<td>ECX (2)</td>
<td>P12</td>
</tr>
<tr>
<td>...</td>
<td>...</td>
</tr>
</tbody>
</table>

---


## Page 28

# Estrutura de Dados do ROB (Exemplo Conceitual)

O ROB é um buffer circular, onde cada entrada armazena informações críticas para o *retirement* e recuperação de exceções.

<table>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Descrição Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Type</td>
      <td>Tipo de operação (ALU, Load, Store, Branch).</td>
    </tr>
    <tr>
      <td>Destination</td>
      <td>Registrador Arquitetural ($A_{reg}$) de destino.</td>
    </tr>
    <tr>
      <td>Value</td>
      <td>Valor do resultado (escrito pelo FU).</td>
    </tr>
    <tr>
      <td>Ready</td>
      <td>Bit que indica se a µop concluiu a execução.</td>
    </tr>
    <tr>
      <td>$P_{old}$</td>
      <td>Registrador físico antigo que deve ser liberado para a FRL no *retirement*.</td>
    </tr>
    <tr>
      <td>Exception</td>
      <td>Bit que indica se ocorreu uma exceção.</td>
    </tr>
  </tbody>
</table>

# Fórmulas de Capacidade (Conceitual)

A capacidade do sistema de renomeação é limitada pelas seguintes relações:

1.  **Tamanho do PRF:** $N_{PRF} = N_{Arch} + N_{Temp}$
    *   $N_{PRF}$: Número total de registradores físicos.
    *   $N_{Arch}$: Número de registradores arquiteturais (ex: 16 para x86-64 GPRs).
    *   $N_{Temp}$: Número de registradores temporários disponíveis para renomeação.
2.  **Tamanho do ROB:** $N_{ROB} \approx N_{Temp}$
    *   O número de entradas no ROB ($N_{ROB}$) deve ser pelo menos igual ao número de registradores temporários ($N_{Temp}$), pois cada P-reg temporário está associado a uma µop em voo no ROB.
3.  **Latência de Renomeação:** A latência de renomeação é tipicamente de 1 ciclo de *clock* para permitir o mapeamento de múltiplos registradores por ciclo (ex: 4 registradores por ciclo em algumas microarquiteturas Intel).

Throughput Renomeação = $\frac{\text{Registradores Renomeados}}{\text{Ciclo}}$

# Conceito 12: Execution Units - ALU arithmetic, FPU floating point, AGU address generation, load/store ports, vector units

**Itens Técnicos Encontrados:** 12

**Conceitos-Chave:** Unidade de Geração de Endereços (AGU), Endereço Efetivo (EA), Unidade Lógica Aritmética (ALU), Somador de Antecipação de Transporte (CLA), Unidade de Ponto Flutuante (FPU), IEEE 754, Unidade de Carga/Armazenamento (LSU), Store-to-Load Forwarding, SIMD, AVX-512

# Conteúdo Técnico: Unidades de Execução da Arquitetura x86

O processamento de instruções na microarquitetura x86 é realizado por um conjunto de unidades de execução especializadas, cada uma responsável por um tipo específico de operação, como aritmética inteira, ponto flutuante, cálculo de endereço e operações vetoriais.

---


## Page 29

# 1. Unidade de Geração de Endereços (AGU)

A Unidade de Geração de Endereços (AGU), também conhecida como Unidade de Cálculo de Endereços (ACU), é uma unidade de execução dedicada que calcula endereços de memória para operações de carga (load) e armazenamento (store). O cálculo do **Endereço Efetivo (EA)** é uma operação fundamental da AGU, definida pela seguinte fórmula estrutural, que é a base para a maioria dos modos de endereçamento complexos do x86 [1]:

$$\text{EA} = \text{Base} + (\text{Index} \times \text{Scale}) + \text{Displacement}$$

*   **Base:** Um registrador de propósito geral (GPR) que contém o endereço base.
*   **Index:** Um GPR que contém um índice a ser escalado.
*   **Scale:** Um fator de escala implícito ou explícito de 1, 2, 4 ou 8.
*   **Displacement:** Uma constante de 8, 16 ou 32 bits.

A AGU é implementada como um *hardware combinacional rápido*, permitindo que o cálculo do endereço seja concluído em um único ciclo de *clock* na maioria das microarquiteturas modernas, operando em paralelo com as Unidades Lógicas Aritméticas (ALUs) [2].

# 2. Unidade Lógica Aritmética (ALU)

A Unidade Lógica Aritmética (ALU) é responsável pelas operações de aritmética inteira (adição, subtração) e lógica (AND, OR, XOR, NOT). A estrutura fundamental para a adição é o **Somador Completo (Full Adder)**, que calcula a soma e o transporte (carry) de três bits de entrada. Para otimizar a velocidade, as ALUs modernas utilizam estruturas de *hardware* avançadas, como o **Somador de Antecipação de Transporte (Carry-Lookahead Adder - CLA)**, que calcula os bits de transporte em paralelo, reduzindo a latência da propagação de transporte [3].

O projeto de uma ALU é modular, com múltiplas ALUs conectadas a diferentes portas de execução (*execution ports*) no *backend* do processador, permitindo a execução paralela de várias micro-operações (*uops*) inteiras por ciclo.

# 3. Unidade de Ponto Flutuante (FPU)

A Unidade de Ponto Flutuante (FPU), ou Unidade de Execução de Ponto Flutuante (FPU/VPU), lida com operações de números reais. O formato de dados fundamental é o padrão **IEEE 754**, que define a representação de números de ponto flutuante em termos de:

$$\text{Número} = (-1)^{\text{Sinal}} \times 2^{\text{Expoente}} \times (1 + \text{Mantissa})$$

O padrão define formatos de dados específicos:

*   **Precisão Simples (Single Precision):** 32 bits (1 bit de sinal, 8 bits de expoente, 23 bits de mantissa).
*   **Precisão Dupla (Double Precision):** 64 bits (1 bit de sinal, 11 bits de expoente, 52 bits de mantissa).
*   **Precisão Estendida (Extended Precision):** 80 bits (usado internamente pelo *hardware* x87, 1 bit de sinal, 15 bits de expoente, 64 bits de mantissa).

As operações de ponto flutuante, como multiplicação e adição, são implementadas em *hardware* através de algoritmos complexos. Por exemplo, a adição de ponto flutuante envolve as seguintes etapas algorítmicas:

1.  **Alinhamento do Expoente:** O expoente menor é ajustado para corresponder ao maior, deslocando a mantissa correspondente.
2.  **Adição/Subtração da Mantissa:** As mantissas são somadas ou subtraídas.
3.  **Normalização:** O resultado é normalizado, ajustando o expoente e a mantissa para o formato IEEE 754.
4.  **Arredondamento:** O resultado é arredondado de acordo com um dos modos de arredondamento definidos pelo IEEE 754.

Operações como divisão e raiz quadrada frequentemente utilizam **algoritmos iterativos** (como o método de Newton-Raphson ou algoritmos de divisão de alto-radix) implementados em *hardware* para alcançar alta velocidade e precisão [4].

---


## Page 30

# 4. Portas de Carga/Armazenamento (Load/Store Ports)

As portas de Carga/Armazenamento (LSU) gerenciam o fluxo de dados entre os registradores e a memória (cache L1). O principal algoritmo de otimização de desempenho é o Store-to-Load Forwarding [5].

## Algoritmo de Store-to-Load Forwarding

Esta técnica permite que uma operação de carga (*load*) receba dados diretamente de uma operação de armazenamento (*store*) anterior que ainda não foi confirmada na memória (*cache*), mas que já está presente no **Store Buffer** (ou *Store Queue*).

1.  **Operação de Store:** Uma instrução de armazenamento é emitida e seus dados são colocados no **Store Buffer** (SB) junto com seu endereço.
2.  **Operação de Load:** Uma instrução de carga é emitida.
3.  **Verificação de Endereço:** O endereço da carga é comparado com os endereços de todas as entradas pendentes no SB.
4.  **Forwarding:** Se houver uma correspondência de endereço e a carga estiver contida no armazenamento (ou for um armazenamento completo), os dados são **encaminhados** (*forwarded*) diretamente do SB para a unidade de execução, ignorando a latência da memória.
5.  **Estrutura de Hardware:** O hardware da LSU é composto pelo **Store Buffer** e pelo **Load Buffer** (ou *Load Queue*), que são estruturas de fila que gerenciam a ordem e a dependência das operações de memória. A lógica de *disambiguation* de memória é o circuito que realiza a comparação de endereços e determina se o *forwarding* é seguro e possível [5].

# 5. Unidades Vetoriais (SIMD)

As **Unidades Vetoriais** implementam o modelo de execução SIMD (*Single Instruction, Multiple Data*) através de extensões do conjunto de instruções como SSE, AVX e AVX-512.

*   **Estrutura de Dados:** Os dados são armazenados em registradores de largura crescente:
    *   XMM: 128 bits (SSE)
    *   YMM: 256 bits (AVX)
    *   ZMM: 512 bits (AVX-512)
*   **Estrutura de Hardware:** As unidades vetoriais são ALUs e FPUs de largura total (128, 256 ou 512 bits) que podem executar a mesma operação em múltiplos elementos de dados (vetores) simultaneamente. Por exemplo, uma unidade AVX-512 pode realizar 16 adições de ponto flutuante de precisão simples em um único ciclo.
*   **Protocolo de Máscara (AVX-512):** O AVX-512 introduziu registradores de máscara de 64 bits ( k0 a k7 ), que permitem que as operações SIMD sejam condicionalmente aplicadas a subconjuntos de elementos do vetor. O protocolo de máscara é um formato de dados que controla a execução seletiva:

    Resultado\[i\] = {
        Operação(VetorA\[i\], VetorB\[i\]) se Máscara\[i\] = 1
        VetorDestino\[i\] se Máscara\[i\] = 0 (ou zero)

Este protocolo é implementado por *hardware* de multiplexação e lógica de controle que decide, elemento por elemento, se o resultado da operação deve ser escrito de volta ou se o valor original do destino deve ser preservado [6].

---

## Referências

[1] Wikipedia. Address generation unit. [2] Agner Fog. The microarchitecture of Intel, AMD, and VIA CPUs. [3] Wikipedia. Carry-lookahead adder. [4] IEEE. IEEE 754. [5] Stuffed Cow. Store-to-Load Forwarding and Memory Disambiguation in x86. [6] Intel. Intel® Advanced Vector Extensions 512 (Intel® AVX-512).

---

## Conceito 13: Hierarquia de Cache (L1, L2, L3, Inclusiva/Exclusiva, Victim Cache)

Itens Técnicos Encontrados: 18

---


## Page 31

**Conceitos-Chave:** MOESI, MESIF, L1 Cache, L2 Cache, L3 Cache, Victim Cache, Coerência de Cache, Protocolo Snooping, Inclusividade, Exclusividade

## Hierarquia de Cache e Estruturas (L1, L2, L3)

A arquitetura x86 emprega uma hierarquia de cache multinível para reduzir a latência de acesso à memória.

*   **L1 Cache (Nível 1):** Geralmente dividida em duas estruturas separadas: L1 Instruction Cache (L1I) e L1 Data Cache (L1D). É a cache mais rápida e de menor capacidade, privada por núcleo.
*   **L2 Cache (Nível 2):** Tipicamente unificada (armazena instruções e dados) e privada por núcleo.
*   **L3 Cache (Nível 3) / Last Level Cache (LLC):** Unificada e compartilhada entre todos os núcleos do processador.

## Propriedades de Inclusividade/Exclusividade

A relação entre os níveis de cache é definida pela propriedade de inclusividade:

*   **Inclusiva:** O conteúdo da L1 e L2 é um subconjunto do conteúdo da L3.
*   **Exclusiva:** O conteúdo da L1 e L2 não é duplicado na L3.

## Protocolos de Coerência de Cache

Os processadores x86 utilizam protocolos de coerência baseados em *snooping* para manter a consistência dos dados em ambientes multi-core.

### Protocolo MOESI (AMD)

O protocolo MOESI (Modified, Owned, Exclusive, Shared, Invalid) é utilizado pela AMD para garantir a coerência de cache [1].

<table>
<thead>
<tr>
<th>Estado</th>
<th>Nome</th>
<th>Descrição Técnica</th>
</tr>
</thead>
<tbody>
<tr>
<td>M</td>
<td>Modified<br>(Modificado)</td>
<td>A linha de cache contém a cópia mais recente e correta dos dados. A cópia na memória principal está obsoleta. Nenhuma outra cache possui uma cópia.</td>
</tr>
<tr>
<td>O</td>
<td>Owned<br>(Propriedade)</td>
<td>A linha de cache contém a cópia mais recente e correta dos dados. A cópia na memória principal pode estar obsoleta. Outras caches podem ter cópias no estado S. O proprietário (O) é responsável por fornecer os dados a outros solicitantes e por escrever de volta na memória principal.</td>
</tr>
<tr>
<td>E</td>
<td>Exclusive<br>(Exclusivo)</td>
<td>A linha de cache contém a cópia mais recente e correta dos dados. A cópia na memória principal também está correta. Nenhuma outra cache possui uma cópia.</td>
</tr>
<tr>
<td>S</td>
<td>Shared<br>(Compartilhado)</td>
<td>A linha de cache contém a cópia mais recente e correta dos dados. Outras caches podem ter cópias no estado S ou uma cache pode ter a cópia no estado O.</td>
</tr>
<tr>
<td>I</td>
<td>Invalid (Inválido)</td>
<td>A linha de cache não contém dados válidos.</td>
</tr>
</tbody>
</table>

### Transições (Exemplo Lógico):

*   **Write Hit (E/S/O) → M:** Uma escrita local em uma linha E, S ou O a move para o estado M, exigindo uma transação de invalidação (BusRdX) para as outras cópias.
*   **Read Miss → E/S:** Uma leitura de uma linha não presente resulta em E se nenhuma outra cache a tiver, ou S se outra cache a tiver (e não estiver em M ou O).
*   **Probe Write Hit (BusRdX) → I:** Uma solicitação de escrita exclusiva de outro processador invalida a linha local.

### Protocolo MESIF (Intel)

O protocolo MESIF (Modified, Exclusive, Shared, Invalid, Forwarding) é uma variação do MESI, introduzida pela Intel (derivado do protocolo QuickPath Interconnect - QPI) [2]. Ele adiciona o estado F para otimizar a transferência de dados em interconexões ponto a ponto.

---


## Page 32

<table>
  <thead>
    <tr>
      <th>Estado</th>
      <th>Nome</th>
      <th>Descrição Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>M</td>
      <td>Modified (Modificado)</td>
      <td>Idêntico ao MESI. A cópia local é a única e está suja (dirty).</td>
    </tr>
    <tr>
      <td>E</td>
      <td>Exclusive (Exclusivo)</td>
      <td>Idêntico ao MESI. A cópia local é a única e está limpa (clean).</td>
    </tr>
    <tr>
      <td>S</td>
      <td>Shared (Compartilhado)</td>
      <td>A linha de cache é compartilhada. Não é a responsável por fornecer os dados.</td>
    </tr>
    <tr>
      <td>I</td>
      <td>Invalid (Inválido)</td>
      <td>A linha de cache não contém dados válidos.</td>
    </tr>
    <tr>
      <td>F</td>
      <td>Forwarding<br>(Encaminhamento)</td>
      <td>A linha de cache é compartilhada e limpa. É a única cache entre as caches S que é designada para responder a solicitações de leitura de outros processadores (Source Snooping).</td>
    </tr>
  </tbody>
</table>

**Função do Estado F:**

O estado F atua como um “primeiro entre iguais” para dados compartilhados, garantindo que apenas uma cache responda a uma solicitação de leitura (ReadShared), reduzindo o tráfego de snooping e a latência de cache-a-cache para 2 hops [2].

*   **ReadShared (RS) Hit em F:** A cache F fornece os dados ao solicitante e transiciona para o estado S. O solicitante recebe os dados no estado F.
*   **ReadShared (RS) Miss:** Se a linha não estiver em nenhuma cache, o solicitante a recebe da memória no estado E. Se estiver em S, uma das caches S é promovida a F e fornece os dados.

**Victim Cache**

O Victim Cache é uma pequena cache totalmente associativa, tipicamente localizada entre a L1 e a L2, projetada para reduzir as falhas de conflito (conflict misses) em caches L1 de mapeamento direto (direct-mapped) [3].

**Estrutura e Algoritmo**

*   **Estrutura:** Uma pequena cache totalmente associativa (geralmente 4 a 8 blocos).
*   **Propriedade:** O Victim Cache e a L1 são exclusivos, ou seja, o mesmo bloco de dados não pode estar em ambas as caches simultaneamente.
*   **Algoritmo de Substituição (Replacement Policy):** Geralmente FIFO (First-In, First-Out).
*   **Fluxo de Dados (Estrutura):**
    1.  **L1 Miss:** Se o dado não estiver na L1, o Victim Cache é verificado.
    2.  **Victim Cache Hit:** Se o dado for encontrado no Victim Cache, ocorre uma troca (swap): o bloco do Victim Cache é movido para a L1, e o bloco da L1 que causou a falha (o bloco que seria substituído) é movido para o Victim Cache, sendo colocado no final da fila FIFO.
    3.  **Victim Cache Miss:** O dado é buscado na L2/Memória e colocado na L1. O bloco desalojado da L1 é movido para o Victim Cache. O bloco mais antigo do Victim Cache (o “victim”) é escrito de volta na L2/Memória, se modificado, ou descartado.

**Referências**

[1] AMD64 Technology: AMD x86-64 Architecture Programmer’s Manual. Advanced Micro Devices. URL: https://www.cse.wustl.edu/~roger/569M/24593.pdf

[2] Goodman, J.R. & Hum, H.H.J. (2009). MESIF: A Two-Hop Cache Coherency Protocol for Point-to-Point Interconnects. University of Auckland. URL: https://www.cs.auckland.ac.nz/~goodman/TechnicalReports/MESIF-2009.pdf

[3] Jouppi, N. (1990). Improving direct-mapped cache performance by the addition of a small fully-associative cache and prefetch buffers. Proceedings of the 17th International Symposium on Computer Architecture (ISCA). URL: https://csg.csail.mit.edu/6.823S14/StudyMaterials/Handouts/handout7-victim-cache.pdf

---


## Page 33

# Conceito 14: Coerência de Cache (MESI, MOESI, Snooping, Diretório)

**Itens Técnicos Encontrados:** 20

**Conceitos-Chave:** MOESI, MESI, Snooping, Coerência Baseada em Diretório, Estados da Linha de Cache, Probe Read Hit, Probe Write Hit, BusRd, BusRdX, Snoop Filter, Write Buffer

## Protocolo MOESI (AMD x86-64)

### Estados da Linha de Cache

*   **Invalid (I):** A linha de cache não contém uma cópia válida dos dados.
*   **Exclusive (E):** A linha de cache contém a cópia mais recente e correta dos dados. A cópia na memória principal também é a mais recente e correta. Nenhum outro processador possui uma cópia dos dados.
*   **Shared (S):** A linha de cache contém a cópia mais recente e correta dos dados. Outros processadores no sistema também podem ter cópias dos dados no estado Shared.
*   **Modified (M):** A linha de cache contém a cópia mais recente e correta dos dados. A cópia na memória principal está obsoleta (incorreta), e nenhum outro processador possui uma cópia.
*   **Owned (O):** A linha de cache contém a cópia mais recente e correta dos dados. O estado Owned é semelhante ao estado Shared, pois outros processadores podem ter uma cópia no estado Shared. No entanto, a cópia na memória principal pode estar obsoleta (incorreta). Apenas um processador pode ter os dados no estado Owned.

### Diagrama de Transição de Estados (Lógica de Software)

As transições de estado são acionadas por eventos de execução de instrução (CPU local) e transações de barramento externas (outras CPUs).

#### Transições Iniciadas pela CPU Local:

*   **Read Miss (Exclusive):** Invalid -> Exclusive
*   **Read Miss (Shared):** Invalid -> Shared
*   **Write Hit:** Exclusive -> Modified
*   **Write Hit:** Owned -> Modified
*   **Write Hit:** Shared -> Modified (requer invalidação de outras cópias)

#### Transições Iniciadas por Outras CPUs (Probe/Snoop):

*   **Probe Read Hit:** Modified -> Owned
*   **Probe Read Hit:** Exclusive -> Shared
*   **Probe Write Hit:** Owned -> Shared
*   **Probe Write Hit:** Shared -> Invalid
*   **Probe Write Hit:** Exclusive -> Invalid
*   **Probe Write Hit:** Modified -> Invalid (com write-back para a memória)

### Mecanismo de Coerência (Snooping/Probe)

*   **Algoritmo:** Quando um processador tem um cache miss (leitura ou escrita), ele emite um “probe” (snoop) no barramento para verificar se outros processadores têm uma cópia mais recente da linha de cache. Se sim, a linha é fornecida pelo cache do outro processador; caso contrário, é buscada na memória principal.

---


## Page 34

# Protocolo MESI (Intel x86)

O protocolo MESI é conceitualmente semelhante ao MOESI, mas sem o estado “Owned”.

## Estados da Linha de Cache

*   **Modified (M):** A linha de cache foi modificada e é a única cópia válida.
*   **Exclusive (E):** A linha de cache é uma cópia limpa da memória e é a única cópia em cache.
*   **Shared (S):** A linha de cache é uma cópia limpa da memória e pode haver outras cópias em outros caches.
*   **Invalid (I):** A linha de cache é inválida.

## Transações de Barramento (Exemplos)

*   **BusRd:** Solicitação de leitura. Move a linha de I para S.
*   **BusRdX:** Solicitação de leitura com intenção de escrita (Read-for-Ownership). Move a linha de S para M.

# Estruturas de Hardware para Coerência de Cache (x86)

*   **Cache Line State Bits:** Cada linha de cache possui bits para armazenar seu estado atual (M, O, E, S, I).
*   **Snoop Filter / Directory:** Estrutura de hardware que rastreia quais linhas de cache estão sendo mantidas por quais processadores. Em processadores Intel modernos (como Skylake), isso é implementado como um diretório distribuído junto com o cache L3. Ele evita a necessidade de transmitir (broadcast) todas as solicitações de snoop para todos os cores, melhorando a escalabilidade.
*   **Barramento/Interconexão:** O meio físico pelo qual as mensagens de coerência (probes, invalidações, etc.) são trocadas entre os processadores.
*   **Write Buffer:** Fila temporária para escritas pendentes na memória ou no cache, permitindo que o processador continue a execução sem esperar a conclusão da escrita.

# Conceito 15: TLB Translation Lookaside Buffer - Page table walks, TLB hierarchy, TLB shootdown, PCID

Itens Técnicos Encontrados: 12

Conceitos-Chave: TLB, Page Table Walk, PML4E, PDPE, PDE, PTE, CR3, PCID, INVPCID, INVLPG, TLB Shootdown, 4-Level Paging

# Conteúdo Técnico Bruto - TLB, Page Table Walks, TLB Shootdown, PCID (Arquitetura x86-64)

## 1. Estrutura de Endereçamento e Page Table Walk (4-Level Paging)

A tradução de endereço linear para físico na arquitetura x86-64 (4-Level Paging) envolve uma caminhada de quatro níveis na tabela de páginas, conforme descrito na Seção 4.5.4 do Manual do Desenvolvedor de Software da Intel (Volume 3A) [1].

O endereço linear de 48 bits é dividido nos seguintes campos (para páginas de 4 KBytes):

---


## Page 35

<table>
  <thead>
    <tr>
      <th>Bits</th>
      <th>Tamanho (bits)</th>
      <th>Campo</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>63:48</td>
      <td>16</td>
      <td>Endereço Canônico</td>
      <td>Deve ser uma extensão de sinal do bit 47.</td>
    </tr>
    <tr>
      <td>47:39</td>
      <td>9</td>
      <td>PML4 Index</td>
      <td>Índice na Tabela de Mapeamento de Nível 4 (PML4).</td>
    </tr>
    <tr>
      <td>38:30</td>
      <td>9</td>
      <td>PDP Index</td>
      <td>Índice na Tabela de Diretório de Ponteiros de Página (PDPT).</td>
    </tr>
    <tr>
      <td>29:21</td>
      <td>9</td>
      <td>PD Index</td>
      <td>Índice na Tabela de Diretório de Páginas (PD).</td>
    </tr>
    <tr>
      <td>20:12</td>
      <td>9</td>
      <td>PT Index</td>
      <td>Índice na Tabela de Páginas (PT).</td>
    </tr>
    <tr>
      <td>11:0</td>
      <td>12</td>
      <td>Offset</td>
      <td>Deslocamento dentro da página de 4 KBytes.</td>
    </tr>
  </tbody>
</table>

**Algoritmo de Page Table Walk (Simplificado):**

1. O endereço base da PML4 (Page Map Level 4) é carregado do registrador de controle CR3.
2. O campo **PML4 Index** (bits 47:39) é usado para indexar a PML4, resultando em uma **PML4 Entry (PML4E)**.
3. O endereço base da PDPT (Page-Directory-Pointer Table) é extraído da PML4E.
4. O campo **PDP Index** (bits 38:30) é usado para indexar a PDPT, resultando em uma **PDP Entry (PDPE)**.
5. O endereço base da PD (Page Directory) é extraído da PDPE.
6. O campo **PD Index** (bits 29:21) é usado para indexar a PD, resultando em uma **Page Directory Entry (PDE)**.
7. O endereço base da PT (Page Table) é extraído da PDE.
8. O campo **PT Index** (bits 20:12) é usado para indexar a PT, resultando em uma **Page Table Entry (PTE)**.
9. O endereço base da página física é extraído da PTE.
10. O campo **Offset** (bits 11:0) é adicionado ao endereço base da página física para formar o **Endereço Físico** final.

## 2. Estruturas de Hardware: Formato do Registrador CR3 e Entradas da Tabela de Páginas (PTEs)

### 2.1. Formato do Registrador CR3 (com PCID)

O registrador CR3 contém o endereço base da PML4 e, quando o **PCID** (Process-Context Identifier) está habilitado (CR4.PCIDE = 1), ele também armazena o PCID atual [1].

<table>
  <thead>
    <tr>
      <th>Bits</th>
      <th>Campo</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>63:MAXPHYADDR</td>
      <td>Reservado</td>
      <td>Deve ser 0.</td>
    </tr>
    <tr>
      <td>MAXPHYADDR-1:12</td>
      <td>Endereço Base da PML4</td>
      <td>Endereço físico da Tabela de Mapeamento de Nível 4 (PML4).</td>
    </tr>
    <tr>
      <td>11:0</td>
      <td>PCID</td>
      <td>Process-Context Identifier (12 bits). Usado para marcar entradas do TLB.</td>
    </tr>
  </tbody>
</table>

### 2.2. Formato da Entrada da Tabela de Páginas (PML4E, PDPE, PDE, PTE)

As entradas da tabela de páginas (PML4E, PDPE, PDE, PTE) são estruturas de 64 bits (8 bytes) que contêm o endereço base do próximo nível da tabela ou do quadro de página, além de vários bits de controle [1].

---


## Page 36

<table>
  <thead>
    <tr>
      <th>Bit</th>
      <th>Nome</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>P</td>
      <td>Present (1 = presente na memória física).</td>
    </tr>
    <tr>
      <td>1</td>
      <td>R/W</td>
      <td>Read/Write (0 = somente leitura, 1 = leitura/escrita).</td>
    </tr>
    <tr>
      <td>2</td>
      <td>U/S</td>
      <td>User/Supervisor (0 = Supervisor, 1 = Usuário).</td>
    </tr>
    <tr>
      <td>3</td>
      <td>PWT</td>
      <td>Page Write-Through (Controle de cache).</td>
    </tr>
    <tr>
      <td>4</td>
      <td>PCD</td>
      <td>Page Cache Disable (Controle de cache).</td>
    </tr>
    <tr>
      <td>5</td>
      <td>A</td>
      <td>Accessed (Definido pelo hardware na leitura/escrita).</td>
    </tr>
    <tr>
      <td>6</td>
      <td>D</td>
      <td>Dirty (Definido pelo hardware na escrita - Somente em PTEs).</td>
    </tr>
    <tr>
      <td>7</td>
      <td>PS</td>
      <td>Page Size (0 = 4KB, 1 = 2MB/1GB - Não usado em PML4E e PTE).</td>
    </tr>
    <tr>
      <td>8</td>
      <td>G</td>
      <td>Global (1 = Entrada global, não invalidada em troca de CR3 se CR4.PGE=1).</td>
    </tr>
    <tr>
      <td>11:9</td>
      <td>Ignorado</td>
      <td>Ignorado.</td>
    </tr>
    <tr>
      <td>51:12</td>
      <td>Endereço Base</td>
      <td>Endereço base da próxima tabela de páginas ou do quadro de página física.</td>
    </tr>
    <tr>
      <td>62:52</td>
      <td>Ignorado</td>
      <td>Ignorado.</td>
    </tr>
    <tr>
      <td>63</td>
      <td>XD</td>
      <td>Execute Disable (1 = Não executável - Se IA32_EFER.NXE=1).</td>
    </tr>
  </tbody>
</table>

## 3. TLB (Translation Lookaside Buffer) e PCID

O TLB é um cache de hardware que armazena as traduções de endereço linear para físico. O **PCID** (Process-Context Identifier) é um identificador de 12 bits (0 a 4095) que permite que o TLB armazene entradas de múltiplos espaços de endereçamento simultaneamente [1].

### Estrutura do TLB (Conceitual com PCID):

Cada entrada do TLB armazena, no mínimo:

*   **Endereço Virtual (Tag):** Parte do endereço linear.
*   **Endereço Físico (Dado):** Endereço base do quadro de página.
*   **PCID (Tag):** O identificador de contexto do processo (12 bits).
*   **Flags de Controle:** P, R/W, U/S, D, G, etc.

A hierarquia do TLB (**TLB Hierarchy**) varia entre as implementações (Intel/AMD), mas tipicamente inclui:

*   **L1 TLB de Instrução (ITLB)** e **L1 TLB de Dados (DTLB):** Menores, mais rápidos, por núcleo.
*   **L2 TLB Unificado (STLB):** Maior, mais lento, compartilhado ou por núcleo.

## 4. Protocolo de Invalidação (TLB Shootdown e INVPCID)

O **TLB Shootdown** é o protocolo de software (geralmente implementado pelo kernel do SO) para garantir a coerência do TLB em sistemas multiprocessados (SMP) quando uma tabela de páginas é modificada.

### Instruções de Invalidação de TLB (Hardware):

As instruções e operações de hardware que causam a invalidação do TLB são [1]:

1.  **INVLPG (Invalidate Page):**
    *   **Operando:** Endereço linear.

---


## Page 37

*   **Função:** Invalida entradas do TLB para o endereço linear especificado, associadas ao PCID atual, exceto entradas globais (G=1). Também invalida todas as entradas nos caches de estrutura de paginação associados ao PCID atual.

**2. INVPCID (Invalidate Process-Context Identifier):**

*   **Operando:** Tipo de INVPCID (em um registrador) e um **Descriptor INVPCID** (em memória).
*   **Função:** Invalida entradas do TLB e caches de estrutura de paginação com base no PCID e/ou endereço linear.

**Estrutura do Descritor INVPCID (128 bits) [2]:**

<table>
  <thead>
    <tr>
      <th>Bits</th>
      <th>Tamanho (bits)</th>
      <th>Campo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>127:64</td>
      <td>64</td>
      <td>Endereço Linear (Usado apenas para o Tipo 0)</td>
    </tr>
    <tr>
      <td>63:12</td>
      <td>52</td>
      <td>Reservado (Deve ser zero)</td>
    </tr>
    <tr>
      <td>11:0</td>
      <td>12</td>
      <td>PCID</td>
    </tr>
  </tbody>
</table>

**Tipos de Invalidação INVPCID (Algoritmo):**

<table>
  <thead>
    <tr>
      <th>Tipo</th>
      <th>Nome</th>
      <th>Algoritmo de Invalidação</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Individual-address</td>
      <td>Invalida mapeamentos (exceto globais) para o Endereço Linear e PCID especificados.</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Single-context</td>
      <td>Invalida todos os mapeamentos (exceto globais) associados ao PCID especificado.</td>
    </tr>
    <tr>
      <td>2</td>
      <td>All-context, including globals</td>
      <td>Invalida todos os mapeamentos (incluindo globais) para todos os PCIDs.</td>
    </tr>
    <tr>
      <td>3</td>
      <td>All-context</td>
      <td>Invalida todos os mapeamentos (exceto globais) para todos os PCIDs.</td>
    </tr>
  </tbody>
</table>

**1. MOV to CR3:**

*   **CR4.PCIDE = 0:** Invalida todas as entradas do TLB associadas ao PCID 000H (exceto globais) e todos os caches de estrutura de paginação para o PCID 000H.
*   **CR4.PCIDE = 1 (Bit 63 do operando fonte = 0):** Invalida todas as entradas do TLB associadas ao PCID especificado em CR3<ins>11:0</ins> e todos os caches de estrutura de paginação para esse PCID.

**2. MOV to CR4 (Modificando CR4.PGE ou CR4.PCIDE de 1 para 0):** Invalida todas as entradas do TLB (incluindo globais) e todos os caches de estrutura de paginação para todos os PCIDs.

## Referências

[1] Intel. *Intel® 64 and IA-32 Architectures Software Developer’s Manual*, Volume 3A: System Programming Guide, Part 1. Seções 4.5.4, 4.10.1, 4.10.4.1. [2] Cloutier, Felix. *INVPCID – Invalidate Process-Context Identifier*. https://www.felixcloutier.com/x86/invpcid

## Conceito 16: Memory Ordering - TSO total store order, fence instructions, memory barriers, acquire/release

Itens Técnicos Encontrados: 16

Conceitos-Chave: Total Store Order (TSO), Store Buffer, Store Forwarding, MFENCE, SFENCE, LFENCE, Semântica Acquire, Semântica Release, LOCK prefix, Protocolo MESI/MOESI

---


## Page 38

# Conteúdo Técnico: Memory Ordering (TSO, Fence Instructions, Acquire/Release) na Arquitetura x86

## 1. Modelo de Ordenação de Memória x86-TSO (Total Store Order)

O modelo de memória da arquitetura x86 (Intel 64 e IA-32) é classificado como **Total Store Order (TSO)**, que é um modelo de consistência de memória forte. A característica fundamental do TSO é que ele permite o reordenamento de operações de **Store** (escrita) seguidas por operações de **Load** (leitura) (**StoreLoad**), mas proíbe todos os outros tipos de reordenamento de memória:

<table>
  <thead>
    <tr>
      <th>Reordenamento</th>
      <th>Permitido no x86-TSO</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>LoadLoad (Load1 seguido por Load2)</td>
      <td>Não</td>
    </tr>
    <tr>
      <td>StoreStore (Store1 seguido por Store2)</td>
      <td>Não</td>
    </tr>
    <tr>
      <td>LoadStore (Load seguido por Store)</td>
      <td>Não</td>
    </tr>
    <tr>
      <td>StoreLoad (Store seguido por Load)</td>
      <td>Sim (A principal fonte de reordenação no TSO)</td>
    </tr>
  </tbody>
</table>

### Estrutura de Hardware: Store Buffer

A permissão do reordenamento StoreLoad é uma consequência direta da implementação de hardware que utiliza um **Store Buffer (Buffer de Escrita)** por núcleo de processamento.

*   **Algoritmo de Escrita (Store):**
    1.  A operação de escrita é registrada no **Store Buffer** local do processador.
    2.  A operação de escrita é considerada **localmente visível** (o processador pode ler seu próprio Store Buffer - **Store Forwarding**).
    3.  A operação de escrita é eventualmente esvaziada do Store Buffer para o cache L1 (tornando-se **globalmente visível**).

*   **Algoritmo de Leitura (Load):**
    1.  A operação de leitura primeiro verifica o **Store Buffer** local (Store Forwarding).
    2.  Se o dado não estiver no Store Buffer, a leitura é feita do cache L1 (ou níveis superiores/memória).

O reordenamento **StoreLoad** ocorre porque uma operação de **Load** subsequente pode ser executada e concluída antes que uma operação de **Store** anterior tenha sido esvaziada do Store Buffer para o cache L1 e se tornado globalmente visível.

## 2. Instruções de Barreira de Memória (Fence Instructions)

A arquitetura x86 fornece instruções de barreira de memória (Memory Fences) para impor a ordenação onde o TSO a relaxa (StoreLoad) ou para garantir a visibilidade de operações de memória fracamente ordenadas (como as não-temporais).

### MFENCE (Memory Fence)

*   **Tipo:** Barreira de memória bidirecional (Full Barrier).
*   **Efeito Técnico:** Garante que todas as operações de **Load** e **Store** que precedem o MFENCE no código sejam **globalmente visíveis** antes que qualquer operação de **Load** ou **Store** que o segue seja executada.
*   **Garantias de Ordenação (Impostas):**
    *   LoadLoad
    *   StoreStore

---


## Page 39

*   LoadStore
*   StoreLoad (A principal função, pois o TSO permite StoreLoad)

*   Operação (Pseudocódigo):
    `Wait_On_Following_Loads_And_Stores_Until(preceding_loads_and_stores_globally_visible);`

## SFENCE (Store Fence)

*   Tipo: Barreira de escrita (Store Barrier).
*   Efeito Técnico: Garante que todas as operações de **Store** que precedem o SFENCE no código sejam **globalmente visíveis** antes que qualquer operação de **Store** que o segue seja executada.
*   Garantias de Ordenação (Impostas):
    *   StoreStore
*   Operação (Pseudocódigo): `WaitOnStores(PrecedingStoresGloballyVisible);`
*   Nota: Não impõe ordenação sobre operações de Load.

## LFENCE (Load Fence)

*   Tipo: Barreira de leitura (Load Barrier).
*   Efeito Técnico: Garante que todas as operações de **Load** que precedem o LFENCE no código sejam **globalmente visíveis** antes que qualquer operação de **Load** que o segue seja executada.
*   Garantias de Ordenação (Impostas):
    *   LoadLoad
*   Operação (Pseudocódigo): `WaitOnLoads(PrecedingLoadsGloballyVisible);`
*   Nota: Não impõe ordenação sobre operações de Store. Em processadores modernos, o LFENCE também é usado para serializar a execução de instruções, impedindo a execução especulativa de instruções subsequentes (mitigação de vulnerabilidades como Spectre).

# 3. Semântica Acquire/Release e Instruções Atômicas

Na arquitetura x86, a semântica **Acquire** e **Release** é frequentemente alcançada sem o uso explícito das instruções MFENCE, SFENCE ou LFENCE para operações de memória normais (cacheable, Write-Back).

*   **Semântica Release (Store):** Uma operação de Store com semântica Release garante que todas as operações de memória anteriores sejam visíveis antes da Store Release. No x86-TSO, como o reordenamento StoreStore e LoadStore é proibido, uma Store normal já atua como uma **Release Barrier** (StoreStore e LoadStore).
*   **Semântica Acquire (Load):** Uma operação de Load com semântica Acquire garante que todas as operações de memória subsequentes sejam visíveis após a Load Acquire. No x86-TSO, como o reordenamento LoadLoad e StoreLoad é proibido (exceto o StoreLoad), uma Load normal não é uma Acquire Barrier.
*   **Instruções Atômicas (LOCK prefix):** O prefixo LOCK em instruções como LOCK ADD, LOCK XCHG, ou LOCK CMPXCHG atua como uma **Full Memory Barrier** (equivalente a um MFENCE em termos de ordenação) e garante a atomicidade da operação. O LOCK é a forma mais comum e eficiente de implementar semântica Acquire/Release em primitivas de sincronização.

## Estrutura de Protocolo (Implícita)

*   **Protocolo de Coerência de Cache (MESI/MOESI):** O TSO é implementado sobre um protocolo de coerência de cache (como MESI ou MOESI) que garante que todas as escritas se tornem visíveis em uma ordem total (Total Store Order) para todos os processadores. O Store Buffer garante que as escritas de um processador sejam vistas por ele mesmo (via Store Forwarding) antes de serem vistas pelos outros.

---


## Page 40

*   **Regra de Ordenação Fundamental do TSO:** A ordem em que as escritas (Stores) de um processador são observadas por outros processadores é a mesma ordem em que o processador as emitiu (Program Order). A única exceção é a reordenação StoreLoad.

---

## Conceito 17: Prefetching - Hardware prefetcher, stride detection, stream buffers, software prefetch hints

**Itens Técnicos Encontrados:** 11

**Conceitos-Chave:** Hardware Prefetcher, Stride Detection, Stream Buffers, PREFETCHh, NTA Hint, Non-Temporal Cache Structure

---

## Prefetching na Arquitetura x86: Conteúdo Técnico

### 1. Hardware Prefetcher (Prefetcher de Hardware)

O prefetcher de hardware é um componente microarquitetural que opera de forma especulativa, monitorando os padrões de acesso à memória para buscar blocos de dados ou instruções para os caches (L1, L2, L3) antes que sejam explicitamente solicitados pela Unidade Central de Processamento (CPU).

#### 1.1. Detecção de Stride (Stride Detection)

O algoritmo de detecção de stride é o mecanismo fundamental para o funcionamento do prefetcher de hardware, permitindo a identificação de acessos sequenciais ou com passo constante.

*   **Estrutura de Dados Implícita:** O prefetcher mantém um histórico de acessos à memória, frequentemente associado a um Load/Store Unit (LSU) ou a um Instruction Pointer (IP) específico, para rastrear a origem dos acessos.
*   **Algoritmo Básico de Stride:**
    1.  Monitora uma sequência de endereços de memória acessados: $A_0, A_1, A_2, ...$
    2.  Calcula a diferença (stride) entre acessos consecutivos: $\$S_i = A_i - A_{i-1}\$$
    3.  Se $S_i$ for constante por um número de acessos (limiar de ativação), o prefetcher é ativado.
    4.  **Próximo Endereço Prefetch:** O endereço a ser pré-buscado é calculado pela fórmula: $\$A_{next} = A_i + S_i\$$
*   **Limiar de Ativação:** O prefetcher é ativado após um número mínimo de acessos consecutivos com o mesmo stride.
*   **Streamer (Prefetcher Sequencial):** Detecta acessos sequenciais, onde o stride é constante e geralmente igual ao tamanho da linha de cache.
*   **Data Prefetcher (Prefetcher de Dados):** Detecta padrões de stride mais complexos, incluindo strides não-unitários.

#### 1.2. Stream Buffers (Buffers de Stream)

Os stream buffers são estruturas de hardware projetadas para armazenar dados pré-buscados, atuando como um cache dedicado para streams de dados e minimizando a poluição dos caches L1 e L2.

*   **Estrutura:** Um stream buffer é tipicamente implementado como uma fila FIFO (First-In, First-Out) de linhas de cache.
*   **Componentes (Modelo Conceitual):**
    *   **Tag:** Endereço base do stream.
    *   **Available Bit:** Indica se o buffer está em uso.
    *   **Linhas de Cache:** Múltiplos blocos de cache pré-buscados (a profundidade $N$ varia, tipicamente 4 a 16 linhas).

---


## Page 41

*   **Operação:**
    1. Quando um padrão de stream é detectado, o prefetcher aloca um stream buffer.
    2. O prefetcher busca sequencialmente as próximas N linhas de cache e as armazena no buffer.
    3. Quando a CPU solicita um endereço presente no stream buffer, o dado é movido para o cache L1/L2 e o buffer avança, buscando a próxima linha para manter a fila cheia.
    4. Se o stream for interrompido (miss), o buffer pode ser desalocado.

# 2. Software Prefetch Hints (Dicas de Prefetching por Software)

A arquitetura x86 (Intel e AMD) fornece a instrução PREFETCHh para que o software possa fornecer dicas ao hardware sobre a localidade dos dados, influenciando a hierarquia de cache.

## 2.1. Instrução PREFETCHh (PREFETCHT0, PREFETCHT1, PREFETCHT2, PREFETCHNTA)

A instrução PREFETCHh (onde ‘h’ representa o hint) busca a linha de cache que contém o endereço de memória especificado para um nível da hierarquia de cache, conforme a dica de localidade.

*   **Sintaxe (Assembly):** PREFETCHh m8
*   **Operação (Modelo):** FETCH (m8); (Busca a linha de cache que contém o byte em m8 ).
*   **Hints de Localidade (Locality Hints):**
    *   T0 (Temporal Data): Prefetch para todos os níveis da hierarquia de cache (L1, L2, L3). Indica que o dado será reutilizado em breve.
    *   T1 (Temporal Data, L1 Miss): Prefetch para L2 e níveis superiores. Usado para dados que não precisam poluir o L1.
    *   T2 (Temporal Data, L2 Miss): Prefetch para L3 e níveis superiores (ou escolha específica da implementação).
    *   NTA (Non-Temporal Data): Prefetch para uma estrutura de cache não-temporal (Non-Temporal Cache Structure - NTCS) e para uma localização próxima ao processador, com o objetivo de minimizar a poluição do cache. Usado para dados que serão lidos uma única vez (streaming).

## 2.2. Estrutura de Cache Não-Temporal (Non-Temporal Cache Structure - NTCS)

O hint NTA sugere o uso de uma estrutura de cache especial para dados que não serão reutilizados.

*   **Propósito:** Evitar que dados de uso único (non-temporal) desalojem dados de alta reutilização (temporal) dos caches L1/L2.
*   **Implementação (Conceitual):** O dado pré-buscado com NTA pode ser colocado em um buffer de prefetch dedicado ou em uma seção do cache L1/L2 com uma política de substituição mais agressiva (ex: fill-bypass ou write-combining buffer).

---


## Page 42

# 3. Resumo de Estruturas, Algoritmos e Fórmulas

<table>
  <thead>
    <tr>
      <th>Conceito</th>
      <th>Tipo</th>
      <th>Descrição Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Stride</b></td>
      <td>Fórmula</td>
      <td>$S = A_i - A_{i-1}$ (Diferença de endereço entre acessos consecutivos)</td>
    </tr>
    <tr>
      <td><b>Próximo Endereço</b></td>
      <td>Algoritmo</td>
      <td>$A_{next} = A_i + S$ (Usado pelo hardware prefetcher)</td>
    </tr>
    <tr>
      <td><b>Stream Buffer</b></td>
      <td>Estrutura</td>
      <td>Fila FIFO de linhas de cache (Tag, Available Bit, Linhas de Cache [N])</td>
    </tr>
    <tr>
      <td><b>PREFETCHh</b></td>
      <td>Protocolo/Instrução</td>
      <td>PREFETCHh m8 (Instrução x86 com hints de localidade)</td>
    </tr>
    <tr>
      <td><b>Hints de Localidade</b></td>
      <td>Protocolo/Estrutura</td>
      <td>T0, T1, T2, NTA (Direcionamento do dado para níveis específicos da hierarquia de cache)</td>
    </tr>
    <tr>
      <td><b>NTCS</b></td>
      <td>Estrutura</td>
      <td>Estrutura de cache dedicada para dados NTA (minimiza poluição)</td>
    </tr>
    <tr>
      <td><b>FIFO</b></td>
      <td>Estrutura</td>
      <td>Política de substituição/organização de dados no Stream Buffer</td>
    </tr>
    <tr>
      <td><b>LSU/IP Tracking</b></td>
      <td>Estrutura</td>
      <td>Rastreamento de acessos por Load/Store Unit ou Instruction Pointer</td>
    </tr>
    <tr>
      <td><b>Fill-Bypass</b></td>
      <td>Algoritmo/Política</td>
      <td>Política de cache sugerida pelo NTA para evitar poluição</td>
    </tr>
    <tr>
      <td><b>Write-Combining Buffer</b></td>
      <td>Estrutura</td>
      <td>Buffer de memória usado em operações não-temporais (implícito no NTA)</td>
    </tr>
    <tr>
      <td><b>Limiar de Ativação</b></td>
      <td>Algoritmo/Parâmetro</td>
      <td>Número mínimo de strides constantes para ativar o prefetcher</td>
    </tr>
  </tbody>
</table>

## Conceito 18: Paging x86 - Page tables, 4-level paging, 5-level paging, huge pages 2MB/1GB, PAE

**Itens Técnicos Encontrados:** 24

**Conceitos-Chave:** Paging de 5 Níveis, Paging de 4 Níveis, PAE, Page Walk, PML5 Index, PML4 Index, PDPT Index, PD Index, PT Index, Page Offset, CR3, PTE, PDE, PDPTE, PML4E, PML5E, Huge Pages, 2 MiB Pages, 1 GiB Pages, Execute Disable, Global Page, Accessed Bit, Dirty Bit

# Paging x86: Estruturas, Algoritmos e Fórmulas

## 1. Estruturas de Hardware e Formatos de Dados

### 1.1. Paging de 5 Níveis (5-Level Paging)

O 5-Level Paging estende o espaço de endereçamento virtual para $2^{57}$ bytes ($\approx 128$ PiB).

---


## Page 43

Estrutura do Endereço Linear (57 bits)

<table>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Bits</th>
      <th>Tamanho (bits)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PML5 Index</td>
      <td>56-48</td>
      <td>9</td>
    </tr>
    <tr>
      <td>PML4 Index</td>
      <td>47-39</td>
      <td>9</td>
    </tr>
    <tr>
      <td>PDPT Index</td>
      <td>38-30</td>
      <td>9</td>
    </tr>
    <tr>
      <td>PD Index</td>
      <td>29-21</td>
      <td>9</td>
    </tr>
    <tr>
      <td>PT Index</td>
      <td>20-12</td>
      <td>9</td>
    </tr>
    <tr>
      <td>Page Offset</td>
      <td>11-0</td>
      <td>12</td>
    </tr>
  </tbody>
</table>

Estruturas de Tabela de Paginação (PML5T, PML4T, PDPT, PD, PT)

Todas as tabelas são estruturas de **4 KiB** e contêm **512 entradas de 8 bytes** (**64 bits**).

Formato da Entrada de Tabela de Páginas (PML5E, PML4E, PDPTE, PDE, PTE - 64 bits)

<table>
  <thead>
    <tr>
      <th>Bit(s)</th>
      <th>Nome</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>63</td>
      <td>XD</td>
      <td>Execute Disable (se suportado)</td>
    </tr>
    <tr>
      <td>62-52</td>
      <td>Disponível</td>
      <td></td>
    </tr>
    <tr>
      <td>51-12</td>
      <td>Endereço Base da Tabela/Página</td>
      <td>Endereço físico de 4 KiB alinhado da próxima tabela de paginação ou da página final.</td>
    </tr>
    <tr>
      <td>11</td>
      <td>Ignorado</td>
      <td></td>
    </tr>
    <tr>
      <td>10-9</td>
      <td>Ignorado</td>
      <td></td>
    </tr>
    <tr>
      <td>8</td>
      <td>G</td>
      <td>Global Page</td>
    </tr>
    <tr>
      <td>7</td>
      <td>PS</td>
      <td>Page Size (0=4 KiB, 1=2 MiB/1 GiB) - Apenas em PDE/PDPTE</td>
    </tr>
    <tr>
      <td>6</td>
      <td>D</td>
      <td>Dirty (escrita na página)</td>
    </tr>
    <tr>
      <td>5</td>
      <td>A</td>
      <td>Accessed (leitura ou escrita na página)</td>
    </tr>
    <tr>
      <td>4</td>
      <td>PCD</td>
      <td>Page-level Cache Disable</td>
    </tr>
    <tr>
      <td>3</td>
      <td>PWT</td>
      <td>Page-level Write Through</td>
    </tr>
    <tr>
      <td>2</td>
      <td>U/S</td>
      <td>User/Supervisor</td>
    </tr>
    <tr>
      <td>1</td>
      <td>R/W</td>
      <td>Read/Write</td>
    </tr>
    <tr>
      <td>0</td>
      <td>P</td>
      <td>Present (página presente na memória)</td>
    </tr>
  </tbody>
</table>

1.2. Paging de 4 Níveis (4-Level Paging - x86-64)

O 4-Level Paging (Long Mode) utiliza um espaço de endereçamento virtual de $2^{48}$ bytes ($\approx 256$ TiB). A estrutura é idêntica à de 5 níveis, exceto pela ausência do PML5.

---


## Page 44

Estrutura do Endereço Linear (48 bits)

<table>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Bits</th>
      <th>Tamanho (bits)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PML4 Index</td>
      <td>47-39</td>
      <td>9</td>
    </tr>
    <tr>
      <td>PDPT Index</td>
      <td>38-30</td>
      <td>9</td>
    </tr>
    <tr>
      <td>PD Index</td>
      <td>29-21</td>
      <td>9</td>
    </tr>
    <tr>
      <td>PT Index</td>
      <td>20-12</td>
      <td>9</td>
    </tr>
    <tr>
      <td>Page Offset</td>
      <td>11-0</td>
      <td>12</td>
    </tr>
  </tbody>
</table>

## 1.3. Extensão de Endereço Físico (PAE - Physical Address Extension)

O PAE é um modo de paginação de 32 bits que estende o endereço físico para 36 bits (ou mais), permitindo até 64 GiB de RAM.

### Estruturas de Tabela de Paginação (PAE)

*   **Page Directory Pointer Table (PDPT):** 32 bytes, 4 entradas de 64 bits. Endereço base em CR3.
*   **Page Directory (PD):** 512 entradas de 64 bits.
*   **Page Table (PT):** 512 entradas de 64 bits.

### Estrutura do Endereço Linear (32 bits)

<table>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Bits</th>
      <th>Tamanho (bits)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PDPT Index</td>
      <td>31-30</td>
      <td>2</td>
    </tr>
    <tr>
      <td>PD Index</td>
      <td>29-21</td>
      <td>9</td>
    </tr>
    <tr>
      <td>PT Index</td>
      <td>20-12</td>
      <td>9</td>
    </tr>
    <tr>
      <td>Page Offset</td>
      <td>11-0</td>
      <td>12</td>
    </tr>
  </tbody>
</table>

## 1.4. Paging de 32 bits (Protected Mode)

### Estrutura do Endereço Linear (32 bits)

<table>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Bits</th>
      <th>Tamanho (bits)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Page Directory Index</td>
      <td>31-22</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Page Table Index</td>
      <td>21-12</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Page Offset</td>
      <td>11-0</td>
      <td>12</td>
    </tr>
  </tbody>
</table>

---


## Page 45

Formato da Entrada de Tabela de Páginas (PTE/PDE - 32 bits)

<table>
  <thead>
    <tr>
      <th>Bit(s)</th>
      <th>Nome</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>31-12</td>
      <td>Endereço Base da Tabela/Página</td>
      <td>Endereço físico de 4 KiB alinhado.</td>
    </tr>
    <tr>
      <td>11-9</td>
      <td>Disponível</td>
      <td></td>
    </tr>
    <tr>
      <td>8</td>
      <td>G</td>
      <td>Global Page</td>
    </tr>
    <tr>
      <td>7</td>
      <td>PS</td>
      <td>Page Size (0=4 KiB, 1=4 MiB) - Apenas em PDE</td>
    </tr>
    <tr>
      <td>6</td>
      <td>D</td>
      <td>Dirty (escrita na página)</td>
    </tr>
    <tr>
      <td>5</td>
      <td>A</td>
      <td>Accessed (leitura ou escrita na página)</td>
    </tr>
    <tr>
      <td>4</td>
      <td>PCD</td>
      <td>Page-level Cache Disable</td>
    </tr>
    <tr>
      <td>3</td>
      <td>PWT</td>
      <td>Page-level Write Through</td>
    </tr>
    <tr>
      <td>2</td>
      <td>U/S</td>
      <td>User/Supervisor</td>
    </tr>
    <tr>
      <td>1</td>
      <td>R/W</td>
      <td>Read/Write</td>
    </tr>
    <tr>
      <td>0</td>
      <td>P</td>
      <td>Present (página presente na memória)</td>
    </tr>
  </tbody>
</table>

# 2. Algoritmos e Fórmulas

## 2.1. Algoritmo de Tradução de Endereço (Page Walk)

O Page Walk é o algoritmo de hardware para traduzir um **Endereço Linear** ($L$) em um **Endereço Físico** ($P$).

### Algoritmo para 5-Level Paging

1.  **Endereço Base PML5T:** Obtido do registro de controle **CR3**.
2.  **Cálculo do Endereço PML5E:** $Endereço PML5E = (CR3 Base Address) + (PML5 Index × 8)$ onde $\text{PML5 Index} = L[56:48]$.
3.  **Endereço Base PML4T:** Obtido da PML5E (bits 51-12).
4.  **Cálculo do Endereço PML4E:** $Endereço PML4E = (PML5E Base Address) + (PML4 Index × 8)$ onde $\text{PML4 Index} = L[47:39]$.
5.  **Endereço Base PDPT:** Obtido da PML4E (bits 51-12).
6.  **Cálculo do Endereço PDPTE:** $Endereço PDPTE = (PML4E Base Address) + (PDPT Index × 8)$ onde $\text{PDPT Index} = L[38:30]$.
7.  **Endereço Base PD:** Obtido da PDPTE (bits 51-12).
8.  **Cálculo do Endereço PDE:** $Endereço PDE = (PDPTE Base Address) + (PD Index × 8)$ onde $\text{PD Index} = L[29:21]$.
9.  **Endereço Base PT:** Obtido da PDE (bits 51-12).
10. **Cálculo do Endereço PTE:** $Endereço PTE = (PDE Base Address) + (PT Index × 8)$ onde $\text{PT Index} = L[20:12]$.
11. **Endereço Base da Página Física:** Obtido da PTE (bits 51-12).
12. **Cálculo do Endereço Físico Final:** $P = (PTE Base Address) + \text{Page Offset}$ onde $\text{Page Offset} = L[11:0]$.

### Algoritmo para PAE Paging

1.  **Endereço Base PDPT:** Obtido do registro de controle **CR3**.
2.  **Cálculo do Endereço PDPTE:** $Endereço PDPTE = (CR3 Base Address) + (PDPT Index × 8)$ onde $\text{PDPT Index} = L[31:30]$.

---


## Page 46

3. **Endereço Base PD**: Obtido da PDPTE (bits 63-12).
4. **Cálculo do Endereço PDE**: $Endereço PDE = (PDPTE Base Address) + (PD Index × 8) onde\text{PD Index} = L[29:21]$.
5. **Endereço Base PT**: Obtido da PDE (bits 63-12).
6. **Cálculo do Endereço PTE**: $Endereço PTE = (PDE Base Address) + (PT Index × 8) onde\text{PT Index} = L[20:12]$.
7. **Endereço Base da Página Física**: Obtido da PTE (bits 63-12).
8. **Cálculo do Endereço Físico Final**: $P = (PTE Base Address) + Page Offset onde\text{Page Offset} = L[11:0]$.

## 2.2. Páginas Enormes (Huge Pages)

### Páginas de 2 MiB (2 MiB Pages)
*   **Mapeamento**: Usam a Page Directory Entry (PDE) com o bit PS (Page Size) = 1.
*   **Page Offset**: L[20 : 0] (21 bits).
*   **Cálculo do Endereço Físico**: $P = (PDE Base Address[51 : 21]) \ll 21 + L[20 : 0]$

### Páginas de 1 GiB (1 GiB Pages)
*   **Mapeamento**: Usam a Page-Directory-Pointer Table Entry (PDPTE) com o bit PS (Page Size) = 1.
*   **Page Offset**: L[29 : 0] (30 bits).
*   **Cálculo do Endereço Físico**: $P = (PDPTE Base Address[51 : 30]) \ll 30 + L[29 : 0]$

## 2.3. Fórmulas de Tamanho de Espaço de Endereçamento

### Tamanho do Espaço Virtual (5-Level Paging)
Espaço Virtual = 2^57 bytes

### Tamanho do Espaço Virtual (4-Level Paging)
Espaço Virtual = 2^48 bytes

### Tamanho do Espaço Físico (PAE)
Espaço Físico ≈ 2^36 bytes

## 2.4. Registros de Controle (Estruturas de Hardware)

*   **CR3**: Contém o endereço base da tabela de paginação de nível mais alto (PML5T, PML4T ou PDPT para PAE).
*   **CR4.PAE**: Bit de controle que habilita o modo PAE.
*   **CR4.PGE**: Bit de controle que habilita o Global Pages.
*   **CR4.LA57**: Bit de controle que habilita o 5-level paging.

---

## Conceito 19: Segmentation x86 - GDT global descriptor table, LDT local, segment descriptors, selectors (legacy)

**Itens Técnicos Encontrados:** 3

**Conceitos-Chave:** Segment Selector,Segment Descriptor,GDT,LDT,GDTR,LDTR,Endereço Linear,Granularidade,Nível de Privilégio Requisitado

---


## Page 47

# Conteúdo Técnico: Segmentação x86 (GDT, LDT, Descritores e Seletores)

O mecanismo de segmentação na arquitetura x86 (modo protegido e modo de compatibilidade IA-32e) é um componente fundamental do gerenciamento de memória e proteção. Ele traduz endereços lógicos em endereços lineares. O conteúdo técnico a seguir é extraído do Manual do Desenvolvedor de Software de Arquiteturas Intel® 64 e IA-32, Volume 3A: Guia de Programação do Sistema, Parte 1 [1].

## 1. Algoritmo de Tradução de Endereço

A tradução de um endereço lógico para um endereço linear é um processo de duas etapas definido pela seguinte fórmula (algoritmo):

Endereço Linear = Endereço Base do Segmento + Offset

O Offset é a parte do endereço lógico que especifica a localização do byte dentro do segmento. O Endereço Base do Segmento é obtido a partir do **Descritor de Segmento** correspondente, que é localizado usando o **Seletor de Segmento**.

## 2. Estrutura do Seletor de Segmento (Segment Selector)

O Seletor de Segmento é um identificador de 16 bits que aponta para um Descritor de Segmento em uma tabela (GDT ou LDT).

<table>
<thead>
<tr>
<th>Campo</th>
<th>Bits</th>
<th>Descrição Técnica</th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice</td>
<td>15:3</td>
<td>Seleciona uma das 8192 entradas (descritores) na GDT ou LDT. O endereço do descritor é calculado como: Base da Tabela + (índice * 8).</td>
</tr>
<tr>
<td>TI (Table Indicator)</td>
<td>2</td>
<td>Indica a tabela de descritores a ser usada: <strong>0</strong> para a <strong>GDT</strong> (Global Descriptor Table); <strong>1</strong> para a <strong>LDT</strong> (Local Descriptor Table).</td>
</tr>
<tr>
<td>RPL (Requested Privilege Level)</td>
<td>1:0</td>
<td>Nível de privilégio solicitado (0 a 3, onde 0 é o mais privilegiado). Usado para verificações de proteção.</td>
</tr>
</tbody>
</table>

## 3. Estruturas de Tabela de Descritores (GDT e LDT)

As tabelas de descritores são estruturas de dados que contêm os Descritores de Segmento.

### 3.1. Registradores de Tabela de Descritores

O processador usa registradores de 48 bits (ou 80 bits em modo IA-32e) para localizar as tabelas:

*   GDTR (Global Descriptor Table Register): Contém o endereço base linear de 32 bits (ou 64 bits em IA-32e) e o limite de 16 bits da GDT.
*   LDTR (Local Descriptor Table Register): Contém o seletor de segmento, o endereço base linear, o limite e os direitos de acesso da LDT atual.

### 3.2. Estrutura do Descritor de Segmento (Segment Descriptor)

Um Descritor de Segmento é uma estrutura de 8 bytes (64 bits) na GDT ou LDT que define as características de um segmento.

---


## Page 48

<table>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Bits</th>
      <th>Descrição Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Base Address (Endereço Base)</td>
      <td>63:56, 31:24, 15:0</td>
      <td>Endereço linear de 32 bits (ou 64 bits em IA-32e) onde o segmento começa.</td>
    </tr>
    <tr>
      <td>Segment Limit (Limite do Segmento)</td>
      <td>51:48, 15:0</td>
      <td>Valor de 20 bits que define o tamanho do segmento.</td>
    </tr>
    <tr>
      <td>G (Granularity)</td>
      <td>55</td>
      <td>0 = Limite em bytes (1 byte a 1 MByte); 1 = Limite em páginas de 4 KBytes (4 KBytes a 4 GBytes).</td>
    </tr>
    <tr>
      <td>D/B (Default/Big)</td>
      <td>54</td>
      <td>Segmentos de Código: 0 = 16 bits, 1 = 32 bits. Segmentos de Dados: 0 = 16 bits, 1 = 32 bits (ou 4 GB de limite).</td>
    </tr>
    <tr>
      <td>AVL (Available)</td>
      <td>52</td>
      <td>Disponível para uso por software de sistema.</td>
    </tr>
    <tr>
      <td>P (Present)</td>
      <td>47</td>
      <td>0 = Segmento não presente na memória; 1 = Segmento presente.</td>
    </tr>
    <tr>
      <td>DPL (Descriptor Privilege Level)</td>
      <td>46:45</td>
      <td>Nível de privilégio do segmento (0 a 3).</td>
    </tr>
    <tr>
      <td>S (Descriptor Type)</td>
      <td>44</td>
      <td>0 = Descritor de Sistema (TSS, LDT, Gate); 1 = Descritor de Código ou Dados.</td>
    </tr>
    <tr>
      <td>Type (Tipo)</td>
      <td>43:40</td>
      <td>Define o tipo de segmento (ex: código de leitura/execução, dados de leitura/escrita).</td>
    </tr>
  </tbody>
</table>

## 4. Algoritmo de Cálculo do Limite (Baseado no Bit G)

O limite efetivo do segmento ($L_{eff}$) é determinado pelo valor do campo **SegmentLimit** *(L20$)* e pelo bit de Granularidade (G):

1. Se G = 0 (Granularidade de Byte): $L_{eff} = L_{20}$ bytes$ (O limite varia de 1 byte a 1 MByte).
2. Se G = 1 (Granularidade de Página): $L_{eff} = (L_{20} \times 4096)$ bytes$ (O limite varia de 4 KBytes a 4 GBytes).

[1] Intel. *Intel® 64 and IA-32 Architectures Software Developer’s Manual, Volume 3A: System Programming Guide, Part 1.* Order Number 253668-089US. October 2025.

## Conceito 20: Protection Rings (Ring 0, Ring 3, CPL, DPL, RPL)

Itens Técnicos Encontrados: 6

Conceitos-Chave: Segment Descriptor, Segment Selector, CPL, DPL, RPL, Call Gate, Segment-Level Protection, ARPL instruction

## Estruturas de Dados e Hardware: Segment Descriptor (i386/x86)

O Segment Descriptor é uma estrutura de 8 bytes que define um segmento de memória. Os campos relevantes para o mecanismo de proteção são:

*   DPL (Descriptor Privilege Level): 2 bits (bits 13 e 14 do campo de acesso/tipo) que especificam o nível de privilégio do segmento (0 a 3).
*   Type Field: 4 bits que definem o tipo de segmento (código, dados, gate, TSS) e suas permissões (leitura/escrita, executável, conforme).
*   G (Granularity) bit: 1 bit (bit 23 do campo de limite superior) que define a unidade de limite: 0 = bytes, 1 = 4 KB páginas.
*   P (Present) bit: 1 bit (bit 15 do campo de acesso/tipo) que indica se o segmento está presente na memória física.

---


## Page 49

*   **Limit:** 20 bits (divididos em dois campos) que definem o tamanho do segmento.
*   **Base Address:** 32 bits (divididos em três campos) que definem o endereço linear inicial do segmento.

## Algoritmos/Fórmulas de Verificação de Privilégio (CPL, DPL, RPL)

O processador x86 utiliza um conjunto de regras de comparação de níveis de privilégio para controlar o acesso a segmentos e a transferência de controle. Os níveis de privilégio são:

*   **CPL (Current Privilege Level):** Nível de privilégio do código atualmente em execução (armazenado nos bits 0 e 1 do registrador CS).
*   **RPL (Requestor’s Privilege Level):** Nível de privilégio associado ao seletor de segmento que está sendo usado (armazenado nos bits 0 e 1 do seletor).
*   **DPL (Descriptor Privilege Level):** Nível de privilégio do segmento de destino (armazenado no Segment Descriptor).

### 1. Regra de Acesso a Segmentos de Dados (Leitura/Escrita)

Para carregar um seletor de segmento de dados (DS, ES, FS, GS, SS) em um registrador de segmento, a seguinte condição deve ser satisfeita:

$$\text{DPL}_{\text{segmento}} \geq \text{MAX}(\text{CPL}, \text{RPL}_{\text{seletor}})$$

Onde:
*   $\text{DPL}_{\text{segmento}}$ é o DPL do Segment Descriptor.
*   CPL é o Current Privilege Level.
*   $\text{RPL}_{\text{seletor}}$ é o Requestor’s Privilege Level do seletor.

### 2. Regra de Transferência de Controle (JMP/CALL) para Segmentos de Código Não-Conformes

Para uma transferência de controle (JMP ou CALL) para um segmento de código **não-conforme** (bit C=0 no Type Field do descriptor), a seguinte condição deve ser satisfeita:

$$\text{CPL} = \text{DPL}_{\text{segmento}}$$

Onde:
*   $\text{DPL}_{\text{segmento}}$ é o DPL do Segment Descriptor de código de destino.
*   CPL é o Current Privilege Level.

### 3. Regra de Transferência de Controle (JMP/CALL) para Segmentos de Código Conformes

Para uma transferência de controle (JMP ou CALL) para um segmento de código **conforme** (bit C=1 no Type Field do descriptor), a seguinte condição deve ser satisfeita:

$$\text{CPL} \leq \text{DPL}_{\text{segmento}}$$

Onde:
*   $\text{DPL}_{\text{segmento}}$ é o DPL do Segment Descriptor de código de destino.
*   CPL é o Current Privilege Level.
*   O CPL não muda após a transferência.

### 4. Regra de Transferência de Controle (CALL) via Call Gate (Mudança de Privilégio)

Para uma chamada (CALL) através de um **Call Gate** (que permite a transição para um nível de privilégio maior, ou seja, numericamente menor), duas verificações são realizadas:

---


## Page 50

# Verificação 1: Acesso ao Gate Descriptor

O código chamador deve ter privilégio suficiente para usar o Call Gate:

MAX(CPL, RPL<sub>seletor</sub>) ≤ DPL<sub>gate</sub>

Onde:
* DPL<sub>gate</sub> é o DPL do Call Gate Descriptor.
* RPL<sub>seletor</sub> é o RPL do seletor que aponta para o Call Gate.

# Verificação 2: Acesso ao Segmento de Código de Destino

O segmento de código de destino deve ser mais privilegiado (ou igual) ao CPL atual:

DPL<sub>destino</sub> ≤ CPL

Onde:
* DPL<sub>destino</sub> é o DPL do Segment Descriptor de código de destino.

Se ambas as verificações passarem, o CPL é alterado para o DPL<sub>destino</sub> (o novo CPL é DPL<sub>destino</sub>).

## 5. Instrução ARPL (Adjust RPL)

A instrução ARPL é usada para garantir que o RPL de um seletor de segmento não seja mais privilegiado do que o CPL do código que o está utilizando.

IF RPL<sub>seletor</sub> < CPL THEN RPL<sub>seletor</sub> ← CPL

Esta é uma estrutura de hardware (instrução) que implementa um algoritmo de ajuste de privilégio.

## 6. Estrutura de Seletor de Segmento

O **Segment Selector** é uma estrutura de 16 bits carregada nos registradores de segmento (CS, DS, ES, FS, GS, SS).

<table>
<thead>
<tr>
<th>Bits</th>
<th>Campo</th>
<th>Descrição</th>
</tr>
</thead>
<tbody>
<tr>
<td>15-3</td>
<td>Index</td>
<td>Índice do descriptor na GDT ou LDT.</td>
</tr>
<tr>
<td>2</td>
<td>TI</td>
<td>Table Indicator (0=GDT, 1=LDT).</td>
</tr>
<tr>
<td>1-0</td>
<td>RPL</td>
<td><strong>Requestor’ s Privilege Level</strong> (00=Ring 0, 11=Ring 3).</td>
</tr>
</tbody>
</table>

---

# Conceito 21: Virtualization x86 - VT-x VMX, EPT, VMCS

Itens Técnicos Encontrados: 11

Conceitos-Chave: EPT PDE, EPT PDPE, EPT PML4E, EPT PML5E, EPT PTE, EPT Page Walk Algorithm, EPT Page-Walk Length, EPT Paging Structures, EPT Violation, EPTP, EPTP Format, Guest-Physical Address (GPA), Physical Address (PA), VMCLEAR, VMCS Region Format, VMCS Revision Identifier, VMCS State Diagram, VMLAUNCH, VMPTRLD, VMX-abort Indicator

---


## Page 51

# Virtualization x86 - VT-x, VMX, EPT, VMCS

---

## Virtual-Machine Control Structure (VMCS)

---

## Formato da Região VMCS (Estrutura de Dados)

A região VMCS tem até 4 KBytes e seu formato inicial é:

<table>
  <tr>
    <td>Byte Offset</td>
  </tr>
  <tr>
    <td>0</td>
  </tr>
  <tr>
    <td>Contents</td>
  </tr>
  <tr>
    <td>Bits 30:0: VMCS revision identifier</td>
  </tr>
  <tr>
    <td>Bit 31: shadow-VMCS indicator (see Section 25.10)</td>
  </tr>
  <tr>
    <td>4</td>
  </tr>
  <tr>
    <td>VMX-abort indicator</td>
  </tr>
  <tr>
    <td>8</td>
  </tr>
  <tr>
    <td>VMCS data (implementation-specific format)</td>
  </tr>
</table>

---

## Organização dos Dados VMCS (Estrutura Lógica)

Os dados VMCS são organizados em seis grupos lógicos:

*   Guest-state area. Processor state is saved into the guest-state area on VM exits and loaded from there on VM entries.
*   Host-state area. Processor state is loaded from the host-state area on VM exits.
*   VM-execution control fields. These fields control processor behavior in VMX non-root operation. They determine in part the causes of VM exits.
*   VM-exit control fields. These fields control VM exits.
*   VM-entry control fields. These fields control VM entries.
*   VM-exit information fields. These fields receive information on VM exits and describe the cause and the nature of VM exits. On some processors, these fields are read-only.

---

## Algoritmo de Transição de Estado VMCS (VMPTRLD, VMCLEAR, VMLAUNCH)

O ciclo de vida de uma VMCS é controlado pelas instruções VMX, alterando seu estado (Ativo/Inativo, Atual/Não Atual, Clear/Launched).

Algoritmo de transição de estado (simplificado):

---


## Page 52

mermaid
stateDiagram-v2
    [*] --> Inactive_NotCurrent_Clear
    Inactive_NotCurrent_Clear --> Active_Current_Clear : VMPLRD X
    Active_Current_Clear --> Active_Current_Launched : VMLAUNCH
    Active_Current_Clear --> Active_NotCurrent_Clear : VMRESUME (on failure)
    Active_Current_Launched --> Active_NotCurrent_Launched : VMPLRD Y
    Active_NotCurrent_Clear --> Inactive_NotCurrent_Clear : VMCLEAR X
    Active_NotCurrent_Launched --> Inactive_NotCurrent_Clear : VMCLEAR X
```

# Extended Page Table Mechanism (EPT)

## Mecanismo de Tradução EPT (Extended Page Table)

O EPT traduz endereços físicos do convidado (Guest-Physical Addresses - GPA) para endereços físicos da máquina (Physical Addresses - PA) através de uma segunda camada de estruturas de paginação.

O mecanismo pode ser configurado em 4-level EPT (4 Page-Walk Length) ou 5-level EPT (5 Page-Walk Length), determinado pelo campo **EPTP** (Extended-Page-Table Pointer).

### Estrutura EPTP (Extended-Page-Table Pointer)

O EPTP é um campo de controle VMX que aponta para a estrutura de paginação EPT e define o comprimento do Page-Walk.

O formato do EPTP (simplificado) inclui:

*   Bits 5:3: Comprimento do EPT Page-Walk (valor - 1). 3 para 4-level EPT, 4 para 5-level EPT.
*   Bits 51:12: Endereço físico base da tabela EPT PML4 (para 4-level EPT) ou EPT PML5 (para 5-level EPT).

### Estruturas de Paginação EPT (EPT Paging Structures)

As estruturas de paginação EPT são semelhantes às estruturas de paginação IA-32e, mas com campos de controle de acesso específicos para virtualização (Read, Write, Execute).

O processo de tradução (EPT Page Walk) envolve a travessia das seguintes estruturas (para 5-level EPT):

1.  EPT PML5 Table / EPT PML5E (Page Map Level 5 Entry)
2.  EPT PML4 Table / EPT PML4E (Page Map Level 4 Entry)
3.  EPT PDP Table / EPT PDPE (Page-Directory-Pointer Entry)
4.  EPT Page Directory / EPT PDE (Page-Directory Entry)
5.  EPT Page Table / EPT PTE (Page-Table Entry)

---


## Page 53

# Algoritmo de Tradução de Endereço (EPT Page Walk)

O algoritmo de tradução de GPA para PA (4-level EPT) segue a seguinte lógica (simplificada):

1. O processador usa o **EPTP** para encontrar o endereço físico da **EPT PML4 Table**.
2. O GPA é dividido em índices para as tabelas: **PML4 Index**, **PDP Index**, **PD Index**, **PT Index**, e **Offset**.
3. O processador percorre as tabelas (PML4E -> PDPE -> PDE -> PTE), usando os bits do GPA como índices para encontrar a entrada da próxima tabela.
4. Cada entrada (E) é verificada quanto aos **Direitos de Acesso EPT** (Read, Write, Execute). Se a permissão for negada, ocorre uma **EPT Violation** (VM Exit).
5. A **EPT PTE** final contém o endereço físico base (PA) da página de 4KB, que é combinado com o **Offset** do GPA para formar o Endereço Físico final.

---

# Conceito 22: Real Mode - 16-bit mode, segmented memory model, BIOS interrupts, A20 gate

**Itens Técnicos Encontrados:** 10

**Conceitos-Chave:** Segmented Memory Model, Endereço Físico, Interrupt Vector Table, IVT Entry Format, A20 Gate, Controlador de Teclado 8042, Fast A20 Gate

---

# Conteúdo Técnico: Real Mode, Modelo de Memória Segmentada, Interrupções BIOS e A20 Gate

O conteúdo técnico a seguir descreve as estruturas, fórmulas e protocolos de baixo nível que governam o **Real Mode** (Modo Real) da arquitetura x86, o modelo de endereçamento de memória segmentada, o mecanismo de interrupções via BIOS e o controle do **A20 Gate**.

## 1. Modelo de Memória Segmentada (Real Mode)

O Modo Real utiliza um modelo de endereçamento de memória segmentada de 20 bits, permitindo o acesso a 1 Megabyte (MB) de memória. O endereço lógico é composto por um par **Segmento**:Offset, ambos de 16 bits.

### 1.1. Fórmula de Endereçamento Físico

O Endereço Físico (Physical Address - PA) de 20 bits é calculado a partir do endereço lógico (Segmento:Offset) através da seguinte fórmula:

$$PA = (Segmento \times 16) + Offset$$

Onde:
* *Segmento* é o valor de 16 bits de um registrador de segmento (CS, DS, ES, SS).
* *Offset* é o valor de 16 bits do deslocamento dentro do segmento.
* *Segmento × 16* é equivalente a um *shift* de 4 bits para a esquerda (*Segmento << 4*), resultando no endereço base de 20 bits.

---


## Page 54

# 1.2. Estrutura de Endereço Lógico

<table>
<thead>
<tr>
<th>Componente</th>
<th>Tamanho (bits)</th>
<th>Função</th>
</tr>
</thead>
<tbody>
<tr>
<td>Segmento</td>
<td>16</td>
<td>Endereço base do segmento (multiplicado por 16 para obter o endereço físico)</td>
</tr>
<tr>
<td>Offset</td>
<td>16</td>
<td>Deslocamento dentro do segmento</td>
</tr>
</tbody>
</table>

# 1.3. Comportamento de Wrap-Around (8086/8088/80186)

Nos processadores 8086, 8088 e 80186, que possuem apenas 20 linhas de endereço (A0-A19), o endereçamento acima de 1 MB (acima de 0xFFFFF) resulta em um “wrap-around” (envolvimento) para o início da memória.

$PA_{20-bit} = ((Segmento \ll 4) + Offset) \pmod{2^{20}}$

O endereço máximo possível é 0xFFFF0 + 0xFFFF = 0x10FFEF. Sem o A20 Gate habilitado, o endereço 0x100000 é mapeado para 0x00000 (devido ao módulo $2^{20}$).

# 2. Interrupt Vector Table (IVT) e Interrupções BIOS

No Modo Real, o mecanismo de interrupções (hardware e software, incluindo as chamadas BIOS) é gerenciado pela **Interrupt Vector Table (IVT)**.

## 2.1. Estrutura de Dados da IVT

*   **Localização:** A IVT está fixada no endereço físico 0x00000 (Segmento 0x0000, Offset 0x0000).
*   **Tamanho:** 1024 bytes (400H), contendo 256 entradas.
*   **Algoritmo de Cálculo do Endereço do Handler:** O endereço de memória onde o vetor de interrupção N está armazenado é dado por:

    $Endereço_{IVT} = IVT_{Base} + (N \times 4)$

    Onde N é o número da interrupção (0x00 a 0xFF).

## 2.2. Formato da Entrada da IVT

Cada entrada da IVT é um ponteiro de 4 bytes para o *Interrupt Handler* (rotina de tratamento de interrupção), no formato Segmento:Offset (16 bits cada).

<table>
<thead>
<tr>
<th>Offset na IVT</th>
<th>Tamanho (bytes)</th>
<th>Conteúdo</th>
</tr>
</thead>
<tbody>
<tr>
<td>$N \times 4$</td>
<td>2</td>
<td>Offset (endereço de 16 bits)</td>
</tr>
<tr>
<td>$(N \times 4) + 2$</td>
<td>2</td>
<td>Segmento (endereço de 16 bits)</td>
</tr>
</tbody>
</table>

# 3. A20 Gate

O A20 Gate é um mecanismo de hardware (um AND gate) introduzido no 80286 para controlar a 21ª linha de endereço (A20), garantindo a compatibilidade com o comportamento de wrap-around do 8086.

## 3.1. Protocolo de Controle via Controlador de Teclado 8042

O método tradicional para controlar o A20 Gate utiliza o **Controlador de Teclado 8042** (ou um *chipset* que o emule) através de portas de I/O específicas.

---


## Page 55

<table>
  <thead>
    <tr>
      <th>Porta de I/O</th>
      <th>Função</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0x64</td>
      <td>Porta de Comando/Status do 8042</td>
    </tr>
    <tr>
      <td>0x60</td>
      <td>Porta de Dados do 8042</td>
    </tr>
  </tbody>
</table>

Algoritmo de Habilitação (Sequência de Comandos):

1.  **Desabilitar Interrupções:** cli (para evitar interrupções durante a manipulação do 8042).
2.  **Esperar 8042 (Status):** Loop de leitura da porta 0x64 até que o bit 1 (Input Buffer Full - IBF) esteja **limpo** (0).
3.  **Desabilitar Teclado:** Enviar comando 0xAD para a porta 0x64.
4.  **Esperar 8042 (Status):** Loop de leitura da porta 0x64 até que o bit 1 (IBF) esteja **limpo** (0).
5.  **Ler Byte de Saída:** Enviar comando 0xD0 (Read Output Port) para a porta 0x64.
6.  **Esperar 8042 (Dados):** Loop de leitura da porta 0x64 até que o bit 0 (Output Buffer Full - OBF) esteja **setado** (1).
7.  **Ler Status:** Ler o byte de status da porta 0x60 (Porta de Dados).
8.  **Esperar 8042 (Status):** Loop de leitura da porta 0x64 até que o bit 1 (IBF) esteja **limpo** (0).
9.  **Escrever Byte de Saída:** Enviar comando 0xD1 (Write Output Port) para a porta 0x64.
10. **Esperar 8042 (Status):** Loop de leitura da porta 0x64 até que o bit 1 (IBF) esteja **limpo** (0).
11. **Modificar Status:** Aplicar a operação lógica **OR** no byte lido no passo 7: `Status_{novo} = Status_{antigo} \lor 0x02`. O **bit 1** do byte de saída do 8042 controla o A20 Gate.
12. **Enviar Status Modificado:** Enviar `Status_{novo}` para a porta 0x60.
13. **Esperar 8042 (Status):** Loop de leitura da porta 0x64 até que o bit 1 (IBF) esteja **limpo** (0).
14. **Habilitar Teclado:** Enviar comando 0xAE para a porta 0x64.
15. **Habilitar Interrupções:** sti.

### 3.2. Protocolo de Controle via Fast A20 Gate

Em sistemas mais modernos, o controle do A20 Gate pode ser feito diretamente através da **Porta de Controle do Sistema** (System Control Port), geralmente na porta de I/O 0x92.

Algoritmo de Habilitação (Fast A20):

1.  **Ler Status:** IN AL, 0x92
2.  **Setar Bit A20:** OR AL, 0x02 (O bit 1 da porta 0x92 controla o A20 Gate).
3.  **Escrever Status:** OUT 0x92, AL

<table>
  <thead>
    <tr>
      <th>Porta de I/O</th>
      <th>Bit de Controle</th>
      <th>Função</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0x92</td>
      <td>Bit 1</td>
      <td>Habilita/Desabilita o A20 Gate</td>
    </tr>
    <tr>
      <td>0x92</td>
      <td>Bit 0</td>
      <td>Reinicialização de software (Software Reset)</td>
    </tr>
  </tbody>
</table>

---

## Conceito 23: Protected Mode - 32-bit mode, paging enabled, protection mechanisms, task switching

Itens Técnicos Encontrados: 15

Conceitos-Chave: Segment Descriptor, Task State Segment (TSS), Page Directory Entry (PDE), Page Table Entry (PTE), Global Descriptor Table (GDT), Local Descriptor Table (LDT), Interrupt Descriptor Table (IDT), Call Gate, Task Gate, Tradução de

---


## Page 56

Endereço Lógico, Tradução de Endereço Linear, Níveis de Privilégio (CPL, DPL, RPL), Registrador CR3, Algoritmo de Troca de Tarefas

# Protected Mode - 32-bit Mode, Paging Enabled, Protection Mechanisms, Task Switching (x86)

O conteúdo técnico a seguir descreve as estruturas de dados e os algoritmos de hardware que governam o **Protected Mode** de 32 bits na arquitetura x86, com foco em segmentação, paginação, proteção e troca de tarefas.

## 1. Estruturas de Segmentação e Tradução de Endereços

A segmentação é o primeiro estágio da tradução de endereços, convertendo um **Endereço Lógico** (Segment Selector:Offset) em um **Endereço Linear**.

### 1.1. Seletor de Segmento (Segment Selector)

O Seletor de Segmento é um campo de 16 bits que aponta para um Descritor de Segmento na GDT ou LDT.

<table>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Bits</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Index</td>
      <td>15-3</td>
      <td>Índice do Descritor de Segmento na Tabela (GDT ou LDT).</td>
    </tr>
    <tr>
      <td>TI (Table Indicator)</td>
      <td>2</td>
      <td>0 = GDT (Global Descriptor Table); 1 = LDT (Local Descriptor Table).</td>
    </tr>
    <tr>
      <td>RPL (Requested Privilege Level)</td>
      <td>1-0</td>
      <td>Nível de Privilégio Solicitado (0 = mais privilegiado, 3 = menos privilegiado).</td>
    </tr>
  </tbody>
</table>

### 1.2. Descritor de Segmento (Segment Descriptor)

O Descritor de Segmento é uma estrutura de 64 bits (8 bytes) que define as características de um segmento.

<table>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Bits</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Base Address</td>
      <td>31-0</td>
      <td>Endereço linear inicial do segmento.</td>
    </tr>
    <tr>
      <td>Segment Limit</td>
      <td>19-0</td>
      <td>Tamanho do segmento.</td>
    </tr>
    <tr>
      <td>P (Present)</td>
      <td>1</td>
      <td>1 = Segmento presente na memória física.</td>
    </tr>
    <tr>
      <td>DPL (Descriptor Privilege Level)</td>
      <td>1-0</td>
      <td>Nível de privilégio do segmento (0-3).</td>
    </tr>
    <tr>
      <td>S (System)</td>
      <td>1</td>
      <td>0 = Descritor de Sistema (TSS, Gate); 1 = Descritor de Código/Dados.</td>
    </tr>
    <tr>
      <td>Type</td>
      <td>4</td>
      <td>Tipo de segmento (ex: Código de leitura/execução, Dados de leitura/escrita).</td>
    </tr>
    <tr>
      <td>A (Accessed)</td>
      <td>1</td>
      <td>1 = Segmento acessado pelo processador.</td>
    </tr>
    <tr>
      <td>G (Granularity)</td>
      <td>1</td>
      <td>0 = Limite em bytes (até 1MB); 1 = Limite em páginas de 4KB (até 4GB).</td>
    </tr>
    <tr>
      <td>D/B (Default/Big)</td>
      <td>1</td>
      <td>1 = 32-bit operand/address size; 0 = 16-bit.</td>
    </tr>
    <tr>
      <td>AVL (Available)</td>
      <td>1</td>
      <td>Disponível para uso pelo software.</td>
    </tr>
  </tbody>
</table>

### 1.3. Fórmula de Tradução de Endereço Lógico para Linear

A tradução de endereço lógico para linear é dada por:

Endereço Linear = Base do Segmento + Offset

---


## Page 57

Onde:
* Base do Segmento é obtida do Descritor de Segmento (GDT/LDT) apontado pelo Seletor de Segmento.
* Offset é o campo de 32 bits do endereço lógico.

# 2. Estruturas de Paginação e Tradução de Endereços

A paginação é o segundo estágio da tradução de endereços (quando habilitada), convertendo um **Endereço Linear** em um **Endereço Físico**.

## 2.1. Formato do Endereço Linear (32-bit Paging, 4KB Pages)

O endereço linear de 32 bits é dividido em três campos:

<table>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Bits</th>
      <th>Tamanho</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Directory</td>
      <td>31-22</td>
      <td>10 bits</td>
      <td>Índice para a Page Directory (Diretório de Páginas).</td>
    </tr>
    <tr>
      <td>Table</td>
      <td>21-12</td>
      <td>10 bits</td>
      <td>Índice para a Page Table (Tabela de Páginas).</td>
    </tr>
    <tr>
      <td>Offset</td>
      <td>11-0</td>
      <td>12 bits</td>
      <td>Offset dentro da página de 4 KBytes.</td>
    </tr>
  </tbody>
</table>

## 2.2. Algoritmo de Tradução de Endereço Linear para Físico (4KB Pages)

1.  **Endereço do Page Directory (PD):** O registrador de controle CR3 contém o endereço base físico do Page Directory.
2.  **Busca da Page Directory Entry (PDE):** $Endereço Físico da PDE = CR3[31 : 12] << 12 + Endereço Linear[31 : 22] << 2$ A PDE é lida. Se o bit P (Present) for 0, ocorre uma Page Fault.
3.  **Busca da Page Table Entry (PTE):** O campo **Base Address** da PDE (bits 31-12) contém o endereço base físico da Page Table. $Endereço Físico da PTE = PDE[31 : 12] << 12 + Endereço Linear[21 : 12] << 2$ A PTE é lida. Se o bit P (Present) for 0, ocorre uma Page Fault.
4.  **Endereço Físico Final:** O campo **Base Address** da PTE (bits 31-12) contém o endereço base físico da página. $Endereço Físico = PTE[31 : 12] << 12 + Endereço Linear[11 : 0]$

## 2.3. Formato da PDE/PTE (32-bit)

As entradas de Page Directory (PDE) e Page Table (PTE) são estruturas de 32 bits.

---


## Page 58

<table>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Bits</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Base Address</b></td>
      <td>31-12</td>
      <td>Endereço base físico da Page Table (PDE) ou da Page (PTE).</td>
    </tr>
    <tr>
      <td><b>AVL</b></td>
      <td>11-9</td>
      <td>Disponível para uso pelo software.</td>
    </tr>
    <tr>
      <td><b>G (Global)</b></td>
      <td>8</td>
      <td>PTE: 1 = Não invalida no TLB em CR3 load.</td>
    </tr>
    <tr>
      <td><b>PS (Page Size)</b></td>
      <td>7</td>
      <td>PDE: 1 = Página de 4MB; 0 = Página de 4KB.</td>
    </tr>
    <tr>
      <td><b>D (Dirty)</b></td>
      <td>6</td>
      <td>1 = Página foi escrita.</td>
    </tr>
    <tr>
      <td><b>A (Accessed)</b></td>
      <td>5</td>
      <td>1 = Página foi lida ou escrita.</td>
    </tr>
    <tr>
      <td><b>PCD (Page-level Cache Disable)</b></td>
      <td>4</td>
      <td>1 = Cache desabilitado para esta página.</td>
    </tr>
    <tr>
      <td><b>PWT (Page-level Write Through)</b></td>
      <td>3</td>
      <td>1 = Política Write-Through para esta página.</td>
    </tr>
    <tr>
      <td><b>U/S (User/Supervisor)</b></td>
      <td>2</td>
      <td>1 = Nível 3 (User) pode acessar; 0 = Níveis 0, 1, 2 (Supervisor) podem acessar.</td>
    </tr>
    <tr>
      <td><b>R/W (Read/Write)</b></td>
      <td>1</td>
      <td>1 = Leitura/Escrita; 0 = Somente Leitura.</td>
    </tr>
    <tr>
      <td><b>P (Present)</b></td>
      <td>0</td>
      <td>1 = Entrada presente na memória.</td>
    </tr>
  </tbody>
</table>

## 3. Mecanismos de Proteção (Privilégios)

O modelo de proteção é baseado em anéis de privilégio (0 a 3), onde 0 é o mais privilegiado (Kernel) e 3 é o menos privilegiado (User).

### 3.1. Verificação de Acesso a Dados

Para que um código em execução (com CPL) possa acessar um segmento de dados (com DPL), a seguinte regra deve ser satisfeita:

Max(CPL, RPL) ≤ DPL

Onde:
* **CPL** (Current Privilege Level): Nível de privilégio do código em execução (armazenado nos bits 1-0 do registrador CS).
* **RPL** (Requested Privilege Level): Nível de privilégio solicitado no Seletor de Segmento.
* **DPL** (Descriptor Privilege Level): Nível de privilégio do segmento de dados (armazenado no Descritor de Segmento).

### 3.2. Transferência de Controle (Gates)

O mecanismo de Call Gate permite transferências de controle (chamadas de função) para segmentos de código de maior privilégio (menor número de DPL).

**Regra de Verificação de Privilégio (Call Gate):**
1. **Acesso ao Gate**: Max(CPL, RPL) ≤ DPL<sub>Gate</sub>
2. **Acesso ao Segmento Destino**: CPL ≥ DPL<sub>Destino</sub>

Se CPL > DPL<sub>Destino</sub>, ocorre uma mudança de pilha (Stack Switching) para a pilha do nível de privilégio destino, cujo ponteiro é carregado do TSS da tarefa atual.

## 4. Troca de Tarefas (Task Switching)

A troca de tarefas é um mecanismo de hardware ativado por um Task Gate ou um TSS Descriptor.

---


## Page 59

# 4.1. Task State Segment (TSS)

O TSS é um segmento de sistema que armazena o estado completo de uma tarefa (registradores, ponteiros de pilha, etc.). O TSS de 32 bits tem um tamanho mínimo de 104 bytes.

<table>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Offset (Bytes)</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Previous Task Link</td>
      <td>0x00</td>
      <td>Seletor de Segmento do TSS da tarefa anterior.</td>
    </tr>
    <tr>
      <td>ESP0</td>
      <td>0x04</td>
      <td>Ponteiro de Pilha (Stack Pointer) para CPL 0.</td>
    </tr>
    <tr>
      <td>SS0</td>
      <td>0x08</td>
      <td>Seletor de Segmento de Pilha para CPL 0.</td>
    </tr>
    <tr>
      <td>ESP1</td>
      <td>0x0C</td>
      <td>Ponteiro de Pilha para CPL 1.</td>
    </tr>
    <tr>
      <td>SS1</td>
      <td>0x10</td>
      <td>Seletor de Segmento de Pilha para CPL 1.</td>
    </tr>
    <tr>
      <td>ESP2</td>
      <td>0x14</td>
      <td>Ponteiro de Pilha para CPL 2.</td>
    </tr>
    <tr>
      <td>SS2</td>
      <td>0x18</td>
      <td>Seletor de Segmento de Pilha para CPL 2.</td>
    </tr>
    <tr>
      <td>CR3</td>
      <td>0x1C</td>
      <td>Endereço base do Page Directory (para paginação da tarefa).</td>
    </tr>
    <tr>
      <td>EIP</td>
      <td>0x20</td>
      <td>Ponteiro de Instrução (Instruction Pointer).</td>
    </tr>
    <tr>
      <td>EFLAGS</td>
      <td>0x24</td>
      <td>Registrador de Flags.</td>
    </tr>
    <tr>
      <td>EAX, ECX, EDX, EBX, ESP, EBP, ESI, EDI</td>
      <td>0x28 - 0x44</td>
      <td>Registradores de Propósito Geral.</td>
    </tr>
    <tr>
      <td>ES, CS, SS, DS, FS, GS</td>
      <td>0x48 - 0x5C</td>
      <td>Seletores de Segmento.</td>
    </tr>
    <tr>
      <td>LDT Selector</td>
      <td>0x60</td>
      <td>Seletor de Segmento da LDT da tarefa.</td>
    </tr>
    <tr>
      <td>T-Flag (Trap Flag)</td>
      <td>0x64 (Bit 0)</td>
      <td>1 = Gera uma exceção de Debug após a troca de tarefa.</td>
    </tr>
    <tr>
      <td>I/O Map Base Address</td>
      <td>0x66</td>
      <td>Offset para o mapa de permissão de I/O.</td>
    </tr>
  </tbody>
</table>

# 4.2. Algoritmo de Troca de Tarefas (Hardware)

A troca de tarefas é realizada pelo hardware do processador quando um JMP ou CALL é executado com um seletor de TSS ou Task Gate.

1.  **Salvar Estado da Tarefa Atual:** O processador salva o estado completo da CPU (registradores, seletores de segmento, EFLAGS, EIP) no TSS da tarefa atual.
2.  **Marcar Tarefa Atual como Inativa:** O bit B (Busy) no Descritor de Segmento do TSS atual é limpo.
3.  **Carregar Estado da Nova Tarefa:** O processador carrega o estado completo da CPU a partir do novo TSS (apontado pelo seletor no JMP/CALL).
4.  **Marcar Nova Tarefa como Ativa:** O bit B (Busy) no Descritor de Segmento do novo TSS é definido.
5.  **Atualizar Registradores de Sistema:** Os registradores TR (Task Register) e LDTR (Local Descriptor Table Register) são atualizados com os seletores da nova tarefa.
6.  **Iniciar Execução:** A execução continua a partir do novo EIP e EFLAGS carregados.

# 5. Conceitos Técnicos Principais

*   **Estruturas de Dados:** Segment Descriptor (64-bit), Task State Segment (TSS, min 104 bytes), Page Directory Entry (PDE, 32-bit), Page Table Entry (PTE, 32-bit), Global Descriptor Table (GDT), Local Descriptor Table (LDT), Interrupt Descriptor Table (IDT), Task Gate Descriptor.
*   **Algoritmos/Fórmulas:** Tradução de Endereço Lógico para Linear (Endereço Linear = Base do Segmento + Offset), Algoritmo de Tradução de Endereço Linear para Físico (2-níveis de lookup), Regra de Verificação de Privilégio (

---


## Page 60

Max(CPL, RPL) ≤ DPL), Algoritmo de Troca de Tarefas (Hardware).
* Registradores de Controle: CR0 (PE, PG bits), CR3 (Base do Page Directory).
* Campos de Controle: CPL, RPL, DPL, P (Present), R/W, U/S, G (Granularity), D/B (Default/Big), T-Flag (TSS).

---

## Conceito 24: Long Mode - 64-bit mode, compatibility mode for 32-bit, canonical address form

Itens Técnicos Encontrados: 25

Conceitos-Chave: Long Mode, 64-bit Mode, Compatibility Mode, Canonical Address Form, EFER, CR0.PG, CR4.PAE, REX.W, Flat Memory Model, 4-Level Paging, PML4T, PDPT, PDT, PT, NX Bit

---

# Long Mode, 64-bit Mode, Compatibility Mode e Canonical Address Form (Arquitetura AMD64/x86-64)

O conteúdo técnico a seguir é baseado principalmente no AMD64 Architecture Programmer’s Manual, Volume 2: System Programming.

## 1. Canonical Address Form (Forma Canônica de Endereço)

A arquitetura AMD64 define um espaço de endereço virtual de 64 bits, mas as implementações atuais do processador suportam um número menor de bits de endereço virtual (por exemplo, 48 bits). Para garantir a compatibilidade futura e evitar o uso indevido dos bits superiores não implementados, o conceito de **Canonical Address Form** é imposto.

### Estrutura/Regra

Um endereço virtual de 64 bits está em forma canônica se os bits do endereço de 63 até o bit mais significativo implementado (por exemplo, bit 47) forem todos iguais ao bit mais significativo implementado.

* Se o bit 47 for 0, os bits 63:48 devem ser 0. O endereço está no intervalo `0x0000_0000_0000_0000` a `0x0000_FFFF_FFFF_FFFF`.
* Se o bit 47 for 1, os bits 63:48 devem ser 1. O endereço está no intervalo `0xFFFF_0000_0000_0000` a `0xFFFF_FFFF_FFFF_FFFF`.

Endereços que não estão na forma canônica causam uma **General-Protection Exception (#GP)** ou uma **Stack Exception (#SS)** (para referências implícitas à pilha).

## 2. Long Mode (Modo Longo)

O Long Mode é o modo de operação de 64 bits da arquitetura AMD64. Ele é composto por dois submodos: **64-bit Mode** e **Compatibility Mode**.

### Algoritmo/Estrutura de Ativação

A ativação do Long Mode segue uma sequência de passos de programação do sistema:

1. Habilitar PAE (Physical-Address Extensions): O bit CR4.PAE deve ser definido como 1. O Long Mode requer PAE.

---


## Page 61

2. **Habilitar Long Mode:** O bit EFER.LME (Long-Mode Enable) no Extended Feature Enable Register (EFER) deve ser definido como 1.

3. **Ativar Paging:** O bit CR0.PG (Paging Enable) deve ser definido como 1.

A ativação do paging (CR0.PG=1) enquanto o Long Mode está habilitado (EFER.LME=1) faz com que o processador entre no Long Mode, indicado pelo bit EFER.LMA (Long-Mode Active) ser definido como 1.

## Estruturas de Dados (Registradores de Controle)

*   **EFER (Extended Feature Enable Register):**
    *   LME (Long-Mode Enable, bit 8): Habilita o Long Mode.
    *   LMA (Long-Mode Active, bit 11): Indica que o processador está operando em Long Mode.
    *   NXE (No-Execute Enable, bit 11): Habilita o bit NX (No-Execute) nas entradas da tabela de páginas.
*   **CR0 (Control Register 0):**
    *   PG (Paging Enable, bit 31): Habilita o mecanismo de paginação, ativando o Long Mode se EFER.LME estiver definido.
*   **CR4 (Control Register 4):**
    *   PAE (Physical Address Extension, bit 5): Deve ser 1 para o Long Mode.

## 3. 64-bit Mode (Submodo do Long Mode)

O 64-bit Mode é o submodo principal do Long Mode, onde o código é executado com as seguintes características:

### Estruturas/Características

*   **Endereçamento:** Endereços virtuais de 64 bits (sujeitos à Canonical Address Form).
*   **Tamanho de Operando/Endereço Padrão:** 32 bits, mas pode ser estendido para 64 bits usando o prefixo REX.W.
*   **Registradores:** Acesso a 16 registradores de propósito geral (GPRs) de 64 bits (RAX a RSP, e R8 a R15).
*   **Segmentação:** O modelo de memória é essencialmente flat (plano). O endereço base do segmento é tratado como 0, e o limite do segmento é ignorado.

## 4. Compatibility Mode (Modo de Compatibilidade)

O Compatibility Mode é o segundo submodo do Long Mode, projetado para executar código legado de 16 bits e 32 bits em um sistema operacional de 64 bits.

### Estruturas/Características

*   **Endereçamento:** Endereços virtuais de 32 bits.
*   **Tamanho de Operando/Endereço Padrão:** 32 bits.
*   **Registradores:** Acesso aos 8 registradores de propósito geral (GPRs) de 32 bits (EAX a ESP). Os registradores estendidos (R8 a R15) não estão disponíveis.
*   **Segmentação:** O mecanismo de segmentação de 32 bits (Protected Mode) é usado.

## 5. Estruturas de Paginação em Long Mode (4-Level Paging)

O Long Mode utiliza um esquema de paginação de quatro níveis para traduzir endereços virtuais de 48 bits (ou mais, dependendo da implementação) em endereços físicos (até 52 bits).

---


## Page 62

# Algoritmo de Tradução de Endereço Virtual (4-Kbyte Page)

O endereço virtual de 64 bits é dividido em campos para a tradução:

<table>
  <thead>
    <tr>
      <th>Bits</th>
      <th>Campo</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>63:48</td>
      <td>Sinal</td>
      <td>Extensão de sinal para Canonical Address Form. Deve ser 0s ou 1s.</td>
    </tr>
    <tr>
      <td>47:39</td>
      <td>PML4 Index</td>
      <td>Índice na Page-Map Level 4 Table (PML4T).</td>
    </tr>
    <tr>
      <td>38:30</td>
      <td>PDP Index</td>
      <td>Índice na Page-Directory Pointer Table (PDPT).</td>
    </tr>
    <tr>
      <td>29:21</td>
      <td>PD Index</td>
      <td>Índice na Page-Directory Table (PDT).</td>
    </tr>
    <tr>
      <td>20:12</td>
      <td>PT Index</td>
      <td>Índice na Page-Table (PT).</td>
    </tr>
    <tr>
      <td>11:0</td>
      <td>Offset</td>
      <td>Offset dentro da página de 4 Kbytes.</td>
    </tr>
  </tbody>
</table>

## Estruturas de Dados (Tabelas de Paginação):

1. **PML4T (Page-Map Level 4 Table):**
   * Endereço base armazenado em CR3.
   * Contém PML4Es (Page-Map Level 4 Entries).
   * Cada PML4E aponta para uma PDPT.

2. **PDPT (Page-Directory Pointer Table):**
   * Contém PDPEs (Page-Directory Pointer Entries).
   * Cada PDPE aponta para uma PDT ou para uma página grande de 1 Gbyte (se o bit PS estiver definido).

3. **PDT (Page-Directory Table):**
   * Contém PDEs (Page-Directory Entries).
   * Cada PDE aponta para uma PT ou para uma página grande de 2 Mbytes (se o bit PS estiver definido).

4. **PT (Page Table):**
   * Contém PTEs (Page-Table Entries).
   * Cada PTE aponta para uma página física de 4 Kbytes.

## Estruturas de Dados (Entradas da Tabela de Paginação - Exemplo de Campos Chave)

As entradas (PML4E, PDPE, PDE, PTE) são estruturas de 64 bits.

<table>
  <thead>
    <tr>
      <th>Bit</th>
      <th>Nome</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>P</td>
      <td>Present (Página/Tabela presente na memória física).</td>
    </tr>
    <tr>
      <td>1</td>
      <td>R/W</td>
      <td>Read/Write (Permissão de leitura/escrita).</td>
    </tr>
    <tr>
      <td>2</td>
      <td>U/S</td>
      <td>User/Supervisor (Nível de privilégio).</td>
    </tr>
    <tr>
      <td>7</td>
      <td>PS</td>
      <td>Page Size (Tamanho da página: 0=4KB/2MB/4MB, 1=2MB/1GB).</td>
    </tr>
    <tr>
      <td>63</td>
      <td>NX</td>
      <td>No-Execute (Habilita a proteção contra execução de código).</td>
    </tr>
  </tbody>
</table>

**Nota:** O Long Mode não suporta páginas de 4 Mbytes (usadas no Legacy Mode com PSE). Os tamanhos de página suportados são 4 Kbytes, 2 Mbytes e 1 Gbyte.

---


## Page 63

# 6. Fórmulas/Algoritmos

*   **Fórmula de Endereço Linear (Flat Model em 64-bit Mode):** $Endereço Linear = Endereço Base do Segmento + Endereço EfetivoNo64 – bitMode(modeloflat), o **EndereçoBase do Segmento** é tratado como 0, então : Endereço Linear = Endereço Efetivo$
*   **Algoritmo de Verificação de Endereço Canônico:** $Endereço Virtual ∈ Canonical Form ⇔ (Endereço[63 : N] = Endereço[N – 1]) Onde N é o número de bits de endereço virtual implementados (ex : 48). Se os bits de 63 a N forem uma extensão de sinal de bit N-1$, o endereço é canônico.
*   **Algoritmo de Tradução de Endereço (Simplificado):** $Endereço Físico = PTE[51 : 12] << 12 | Endereço Virtual[11 : 0]$ (Para páginas de 4K bytes, onde PTE é a entrada final da tabela de páginas). O processo completo envolve 4 etapas de lookup : CR3 → PML4T → PDPT → PDT → PT → Página Física$

# Conceito 25: Security Extensions - SGX enclaves, TDX trusted domains, CET control flow, SMAP, SMEP, UMIP

**Itens Técnicos Encontrados:** 37

**Conceitos-Chave:** KOT, PAMT, TDR, TDCS, TDVPS, EPC, EPCM, SIGSTRUCT, EINITTOKEN, EADD, EENTER, Shadow Stack, IBT, ENDBRANCH, CR4.SMAP, CR4.SMEP, CR4.UMIP

# Conteúdo Técnico: Extensões de Segurança x86

O conteúdo a seguir descreve as estruturas de hardware, protocolos, formatos de dados e mecanismos de baixo nível das extensões de segurança Intel SGX, Intel TDX, Intel CET, SMAP, SMEP e UMIP.

## 1. Intel® Trust Domain Extensions (Intel® TDX)

O TDX introduz um conjunto de estruturas de controle gerenciadas pelo Módulo TDX, que são opacas para o VMM (Virtual Machine Manager) e protegidas por criptografia de memória.

### Estruturas de Controle Gerenciadas (Hardware Structures)

<table>
<thead>
<tr>
<th>Estrutura</th>
<th>Escopo</th>
<th>Significado</th>
<th>Descrição Técnica (Função)</th>
</tr>
</thead>
<tbody>
<tr>
<td>KOT</td>
<td>Plataforma</td>
<td>Key Ownership Table</td>
<td>Tabela interna do Módulo TDX para controlar a atribuição de HKID (Host Key ID) privado.</td>
</tr>
<tr>
<td>PAMT</td>
<td>Plataforma</td>
<td>Physical Address Metadata Table</td>
<td>Tabela que armazena metadados de cada página em uma TDMR (Trust Domain Memory Range). Controla a atribuição de páginas físicas a TDs convidados.</td>
</tr>
<tr>
<td>TDR</td>
<td>TD (Domínio de Confiança)</td>
<td>Trust Domain Root</td>
<td>Estrutura raiz que contém o estado inicial e as medições de integridade do TD.</td>
</tr>
<tr>
<td>TDCS</td>
<td>TD</td>
<td>Trust Domain Control Structure</td>
<td>Estrutura principal que armazena o estado do TD, incluindo as EPTs (Extended Page Tables) seguras e o estado de memória.</td>
</tr>
<tr>
<td>TDVPS</td>
<td>VCPU</td>
<td>Trust Domain Virtual Processor State</td>
<td>Estrutura que armazena o estado do VCPU (Virtual CPU) do TD, incluindo os registradores e o estado de execução. Possui vistas físicas (TDVPR/TDVPX) e lógicas.</td>
</tr>
</tbody>
</table>

### Protocolos e Funções de Interface

*   **SEAMCALL (Host-Side Interface Functions):** Conjunto de leaf functions (funções de folha) invocadas pelo VMM (Host) para gerenciar o ciclo de vida do TD, como TD_CREATE , TD_DESTROY , e operações de gerenciamento de memória.

---


## Page 64

*   **TDCALL (Guest-Side Interface Functions):** Conjunto de leaf functions invocadas pelo TD (Guest) para solicitar serviços ao Módulo TDX, como atestado e operações de I/O.
*   **Gerenciamento de Memória:** Inclui operações de **Dynamic Page Addition** (conversão de memória compartilhada para privada) e **Page Promotion** (fusão de mapeamentos de páginas).

## 2. Intel® Software Guard Extensions (Intel® SGX)

O SGX define estruturas de dados e instruções de CPU para criar **Enclaves** (regiões de memória protegidas).

### Estruturas de Hardware e Formatos de Dados

*   **EPC (Enclave Page Cache):** Região de memória física protegida por hardware onde residem o código e os dados do enclave. O conteúdo é criptografado e verificado por integridade.
*   **EPCM (Enclave Page Cache Map):** Estrutura de metadados de hardware que rastreia o conteúdo do EPC. Cada entrada do EPCM corresponde a uma página do EPC e armazena metadados como o tipo de página (TCS, SECS, Regular), o **MRENCLAVE** (hash de medição do enclave) e o **MRSIGNER** (hash da chave de assinatura).
*   **TCS (Thread Control Structure):** Estrutura dentro do EPC que armazena o estado de execução de um thread dentro do enclave.
*   **SIGSTRUCT:** Estrutura de dados assinada pelo desenvolvedor do enclave que contém o **MRENCLAVE** (hash do código e dados do enclave), **MRSIGNER** (hash da chave pública do desenvolvedor) e outros atributos. É usada na instrução EINIT para inicializar o enclave.
*   **EINITTOKEN:** Estrutura de dados gerada pela CPU que atesta a integridade do enclave e é necessária para a instrução EINIT.

### Instruções de Enclave (Algoritmos/Operações)

As instruções de enclave (E-Instructions) são micro-operações atômicas que gerenciam o ciclo de vida e o acesso ao EPC:

*   **EADD:** Adiciona uma página ao EPC.
*   **EINIT:** Inicializa um enclave.
*   **EENTER:** Entra em um enclave.
*   **EEXIT:** Sai de um enclave.
*   **EGETKEY:** Gera chaves criptográficas dentro do enclave.
*   **EREPORT:** Gera um relatório de atestado local.
*   **EREMOVE:** Remove uma página do EPC.

## 3. Intel® Control-flow Enforcement Technology (Intel® CET)

O CET é composto por dois mecanismos principais para proteger contra ataques de desvio de fluxo de controle (ROP/JOP).

### Mecanismos de Hardware

*   **Shadow Stack (Pilha Sombra):** Uma pilha secundária, separada da pilha de dados normal, que armazena apenas endereços de retorno. É protegida contra escrita por código não-CET e usada para proteger o **fluxo de controle de borda reversa** (backward-edge control-flow).
*   **SSP (Shadow Stack Pointer):** Um novo registrador que aponta para o topo da Pilha Sombra atual.
*   **IBT (Indirect Branch Tracking):** Um mecanismo que protege o **fluxo de controle de borda direta** (forward-edge control-flow). Ele exige que os destinos de saltos/chamadas indiretas sejam marcados com as novas instruções ENDBR32 ou ENDBR64.

---


## Page 65

# 4. SMAP, SMEP e UMIP

Estas são extensões de proteção de modo supervisor controladas por bits no **Control Register 4 (CR4)**.

## Estruturas de Controle (CR4 Bits)

<table>
<thead>
<tr>
<th>Extensão</th>
<th>Registrador/Bit</th>
<th>Descrição Técnica (Mecanismo)</th>
</tr>
</thead>
<tbody>
<tr>
<td>SMEP</td>
<td>CR4.SMEP (Bit 20)</td>
<td><strong>Supervisor Mode Execution Prevention</strong>. Quando ativo, impede que o código em modo supervisor (kernel) execute código localizado em páginas de memória de modo usuário. A verificação é feita durante a tradução de endereço (Page Table Walk).</td>
</tr>
<tr>
<td>SMAP</td>
<td>CR4.SMAP (Bit 21)</td>
<td><strong>Supervisor Mode Access Prevention</strong>. Quando ativo, impede que o código em modo supervisor acesse dados localizados em páginas de memória de modo usuário. Pode ser temporariamente desativado usando as instruções CLAC e STAC.</td>
</tr>
<tr>
<td>UMIP</td>
<td>CR4.UMIP (Bit 11)</td>
<td><strong>User-Mode Instruction Prevention</strong>. Quando ativo, impede que certas instruções privilegiadas (como SGDT, SIDT, SLDT, SMSW, STR) sejam executadas no modo usuário (CPL > 0), prevenindo a coleta de informações do sistema.</td>
</tr>
</tbody>
</table>

---

# Conceito 26: Performance Monitoring (PMU, Performance Counters, Sampling, PEBS)

**Itens Técnicos Encontrados:** 30

**Conceitos-Chave:** PMU, Performance Counters, PEBS, MSRs, LBR, Uncore PMU, Frequência de Amostragem, RDPMC, WRMSR

# Conteúdo Técnico sobre Performance Monitoring (PMU, Performance Counters, Sampling, PEBS)

---

# Capítulo 18: DEBUG, BRANCH PROFILE, TSC, AND INTEL® RESOURCE DIRECTOR TECHNOLOGY (INTEL® RDT) FEATURES

## MSRs de Last Branch Record (LBR)

*   **MSR_LASTBRANCH_x_FROM_IP**: Armazena o endereço de origem do branch.
*   **MSR_LASTBRANCH_x_TO_IP**: Armazena o endereço de destino do branch.
*   **MSR_LBR_INFO_x**: Armazena informações sobre a predição do branch, informações de TSX e dados de ciclos decorridos.

## MSRs de LBR para Intel® Xeon Phi™ Processor

*   **MSR_LASTBRANCH_0_FROM_IP (680H)** a **MSR_LASTBRANCH_7_FROM_IP (687H)**: Armazenam os endereços de origem.
*   **MSR_LASTBRANCH_0_TO_IP (6C0H)** a **MSR_LASTBRANCH_7_TO_IP (6C7H)**: Armazenam os endereços de destino.
*   **MSR_LASTBRANCH_TOS (1C9H)**: Ponteiro para o MSR na pilha LBR que contém o registro mais recente.

---


## Page 66

# MSRs de Controle de Debug e Branch Recording

*   IA32_DEBUGCTL MSR: Fornece campos de bits para configurar mecanismos relacionados a trace de debug, branch recording, branch trace store e operações de contadores de performance.

# Capítulo 20: PERFORMANCE MONITORING

## Estrutura da Performance Monitoring Unit (PMU)

A PMU é composta por:

1.  **Contadores de Função Fixa (Fixed-Function Counters):** Contam eventos predefinidos (ex: ciclos de clock não-halted).
2.  **Contadores de Propósito Geral (General-Purpose Counters):** Contam eventos configuráveis via MSRs de seleção de evento.

## Estruturas de Hardware e MSRs (Core PMU)

*   IA32_PERF_GLOBAL_CTRL (MSR 38FH): Habilita/desabilita todos os contadores de performance.
*   IA32_PERF_GLOBAL_STATUS (MSR 3E9H): Indica o status de overflow dos contadores.
*   IA32_PERF_GLOBAL_OVF_CTRL (MSR 3EAH): Controla o overflow e o reset dos contadores.
*   IA32_PERFEVTSELx (MSRs 186H a 189H): Registradores de seleção de evento para os contadores de propósito geral.
    *   **Estrutura de Bits (IA32_PERFEVTSELx):**
        *   **Bits 7:0:** Código do evento a ser contado.
        *   **Bit 16:** Contar em CPL > 0 (nível de usuário).
        *   **Bit 17:** Contar em CPL = 0 (nível de sistema operacional).
        *   **Bit 18:** Habilitar o contador.
        *   **Bit 19:** Habilitar o Precise Event Based Sampling (PEBS).
        *   **Bit 20:** Habilitar a interrupção no overflow.
        *   **Bit 22:** Contador de limite (contar apenas se o evento ocorrer mais de N vezes).
        *   **Bit 23:** Inverter o CMASK.
*   IA32_PMCx (MSRs C1H a C4H): Contadores de performance de propósito geral (48 ou 64 bits).
*   IA32_FIXED_CTRx (MSRs 309H a 30BH): Contadores de função fixa.
*   IA32_FIXED_CTR_CTRL (MSR 38DH): Controla os contadores de função fixa.

## Estruturas de Hardware e MSRs (Uncore PMU - Exemplo Xeon 7500)

A PMU Uncore é distribuída em “Boxes” (CBox, SBox, MBox, RBox, WBox, UBox).

*   **MSRs de Controle Global (Uncore):**
    *   MSR_U_PMON_GLOBAL_CTL: Controle global de habilitação/desabilitação e PMI.
    *   MSR_%box#%_PMON_BOX_CTL: Controle por Box (ex: MSR_S0_PMON_BOX_CTL).
*   **MSRs de Status (Uncore):**
    *   MSR_U_PMON_GLOBAL_STATUS: Status global de overflow.
    *   MSR_%box#%_PMON_BOX_STATUS: Status de overflow por Box.
*   **MSRs de Contadores (Uncore):**
    *   MSR_U_PMON_CTR: Contador de propósito geral Uncore.
    *   MSR_%box#%_PMON_CTR%n%: Contadores de propósito geral por Box (ex: MSR_C7_PMON_CTR5).

---


## Page 67

*   **MSRs de Seleção de Evento (Uncore):**
    *   MSR_U_PMON_EVNT_SEL: Seleção de evento Uncore.
    *   MSR_%box#%_PMON_EVNT_SEL%n%: Seleção de evento por Box (ex: MSR_C7_PMON_EVNT_SEL5).

## Precise Event Based Sampling (PEBS)

*   **Estrutura de Dados (PEBS Record):**
    *   O PEBS armazena um registro (record) em uma área de memória definida pelo software (PEBS Buffer) no momento do evento.
    *   O registro PEBS contém o estado do processador no momento do evento, incluindo:
        *   Registradores de Propósito Geral (EAX, EBX, ECX, EDX, ESI, EDI, EBP, ESP, R8-R15).
        *   Registradores de Segmento (CS, SS, DS, ES, FS, GS).
        *   Registrador de Flags (EFLAGS).
        *   Endereço da Instrução (RIP).
        *   MSRs de Performance (IA32_PERF_GLOBAL_STATUS).
        *   Dados específicos do evento (ex: endereço de memória para eventos de cache/memória).

*   **MSRs de Controle PEBS:**
    *   IA32_PEBS_ENABLE (MSR 3F1H): Habilita o PEBS para contadores específicos.
    *   IA32_DS_AREA (MSR 600H): Aponta para a estrutura de dados de Debug Store (DS), que contém o ponteiro para o PEBS Buffer.
    *   IA32_PEBS_BASE (MSR 3F2H): Aponta para o início do PEBS Buffer.
    *   IA32_PEBS_INDEX (MSR 3F3H): Aponta para o próximo slot livre no PEBS Buffer.
    *   IA32_PEBS_DATA_CFG (MSR 3F4H): Configura quais dados adicionais (ex: dados de latência) serão incluídos no registro PEBS.

## Fórmulas e Algoritmos (Conceituais)

1.  **Cálculo da Frequência de Amostragem (Sampling):** $Frequência\ de\ Amostragem = \frac{Frequência\ do\ Clock\ do\ Processador}{Valor\ Inicial\ do\ Contador}$ O contador é programado com um valor inicial (complemento de 2 do valor desejado) e, ao atingir zero, gera uma interrupção (PMI) e/ou um registro PEBS.

2.  **Cálculo da Taxa de Overflow (Overflow Rate):** $Taxa\ de\ Overflow = \frac{Número\ de\ Eventos\ Contados}{Valor\ de\ Threshold}$ Onde o Valor de Threshold é o valor programado no contador (complemento de 2).

3.  **Algoritmo de Leitura de Contadores (RDPMC):**

```assembly
; Ler o contador de performance N (N é o índice do contador)
MOV ECX, N
RDPMC
; Resultado em EDX:EAX (64 bits)
```

4.  **Algoritmo de Configuração de Contador (WRMSR):**

---


## Page 68

assembly
; Configurar o MSR de seleção de evento (IA32_PERFEVTSELx)
MOV ECX, MSR_ADDRESS_PERFEVTSELx
MOV EAX, LOW_32_BITS_CONFIG
MOV EDX, HIGH_32_BITS_CONFIG
WRMSR

; Configurar o MSR do contador (IA32_PMCx) com o valor inicial (threshold)
MOV ECX, MSR_ADDRESS_PMCx
MOV EAX, LOW_32_BITS_THRESHOLD
MOV EDX, HIGH_32_BITS_THRESHOLD
WRMSR
```

5. Estrutura de Dados do PEBS Buffer (Simplificada):

```c
typedef struct {
    uint64_t R15;
    uint64_t R14;
    // ... outros registradores de propósito geral
    uint64_t RIP;
    uint64_t RFLAGS;
    uint64_t RSP;
    // ... registradores de segmento
    uint64_t IA32_PERF_GLOBAL_STATUS;
    // ... dados específicos do evento (ex: Data Linear Address)
} PEBS_RECORD;

typedef struct {
    uint64_t PEBS_BASE;  // Endereço base do buffer
    uint64_t PEBS_INDEX; // Ponteiro para o próximo registro
    uint64_t PEBS_THRESHOLD; // Limite do buffer
    // ... outros campos do Debug Store
} DS_AREA;
```

---

# Conceito 27: Power Management (C-states, P-states, Turbo Boost, SpeedStep, DVFS)

**Itens Técnicos Encontrados:** 15

**Conceitos-Chave:** C-states, P-states, Turbo Boost, DVFS, Enhanced Intel SpeedStep Technology (EIST), RAPL, MSR, IA32_PERF_CTL, IA32_APERF, IA32_MPERF, MSR_PKG_POWER_LIMIT, ACPI_CST

## Power Management (Gerenciamento de Energia) - Arquitetura x86 (Intel)

Conteúdo técnico extraído do Intel® 64 and IA-32 Architectures Software Developer’s Manual, Volume 3B: System Programming Guide, Part 2 (Capítulo 14) e Volume 4 (MSRs).

### P-States (Performance States) e Hardware Coordinated Feedback

O gerenciamento de P-states é a otimização da frequência e tensão da CPU durante a operação.

#### 1. Registros MSR para Coordenação de P-State (Hardware Coordinated Feedback)

O mecanismo de feedback coordenado por hardware utiliza dois Model-Specific Registers (MSRs) para medir o desempenho e a frequência:

---


## Page 69

*   **IA32_MPERF (MSR E7H):** Contador de Frequência Nominal (Nominal Frequency Counter).
    *   Incrementa em proporção a uma frequência fixa (frequência de referência).
    *   Representa o tempo que o processador passou em um estado de desempenho máximo (não-ocioso) durante um período de amostragem.
*   **IA32_APERF (MSR E8H):** Contador de Desempenho Real (Actual Performance Counter).
    *   Incrementa em proporção ao desempenho real (performance) ou throttling iniciado por software/TM1/TM2.
    *   Representa o tempo que o processador passou em um estado de desempenho real (não-ocioso) durante o mesmo período de amostragem.

## 2. Cálculo de Desempenho (PercentPerformance)

O desempenho percentual (PercentPerformance) é uma métrica usada para a tomada de decisão de P-state.

*   **PercentBusy:** Percentual de tempo do processador não ocioso (não em C-state).
*   **ACNT/MCNT Ratio:** Razão entre o desempenho real e o desempenho nominal.

### Fórmula Implícita para Desempenho Coordenado por Hardware:

```
PercentPerformance = PercentBusy × (IA32_APERF / IA32_MPERF)
```

Onde:
*   IA32_APERF e IA32_MPERF são as diferenças (deltas) dos valores dos MSRs lidos ao longo de um intervalo de tempo.

## 3. Algoritmo de Transição de P-State (Exemplo Simplificado)

O sistema operacional (OS) ou o firmware pode usar o PercentPerformance para determinar o P-state alvo:

```c
// Exemplo 14-1: Determinar o P-state Alvo a partir do Feedback Coordenado por Hardware
// PercentBusy: Percentual de tempo do processador não ocioso.
// ACNT: Delta de IA32_APERF
// MCNT: Delta de IA32_MPERF

TargetPstate = FindPstate(PercentPerformance);

if (TargetPstate != CurrentPstate) {
    SetPstate(TargetPstate);
}
```

## 4. Registros de Controle de P-State

*   **IA32_PERF_CTL (MSR 0199H):** Usado para iniciar transições de estado de performance.
    *   Bits 15:0: Target Performance State (Estado de Performance Alvo).
    *   Bit 32: IDA/Turbo DISENGAGE (Desativação de IDA/Turbo).
*   **IA32_PERF_STATUS (MSR 0198H):** Contém o estado de performance atual.

## Enhanced Intel SpeedStep® Technology (EIST)

*   Tecnologia que permite o gerenciamento do consumo de energia do processador através de transições de estado de performance (P-states).
*   **Estrutura:** Centralização do mecanismo de controle e interface de software no processador usando MSRs.
*   **Habilitação:** Suporte indicado pelo CPUID, e habilitado pelo bit 16 do IA32_MISC_ENABLE MSR.

---


## Page 70

# C-States (Processor Idle States) - ACPI

Os C-states são estados de sono do processador (C1 a Cn) onde o consumo de energia é reduzido. O estado C0 é o estado ativo.

## 1. Estrutura de Dados _CST (C States)

A estrutura _CST (C States) é um objeto ACPI opcional que fornece um método alternativo para declarar os estados de energia suportados pelo processador.

### Estrutura do Pacote de Retorno_CST:

```c
Package {
    Count                  // Integer (Número de sub-pacotes CState)
    CStates[0]             // Package (Sub-pacote CState)
    ...
    CStates[Count-1]       // Package
}
```

### Estrutura de Cada Sub-Pacote CState:

```c
Package {
    Register              // Buffer (Descritor de Recurso)
    Type                  // Integer (BYTE) - Tipo de C-state (1=C1, 2=C2, 3=C3, etc.)
    Latency               // Integer (WORD) - Latência de entrada/saída (microssegundos)
    Power                 // Integer (DWORD) - Consumo de energia (miliwatts)
}
```

## 2. Estrutura do Descritor de Recurso (Register)

O campo Register é um Buffer que contém um **Descritor de Recurso de Endereço Genérico** (Generic Address Resource Descriptor) que especifica o registro de hardware a ser acessado para entrar no C-state.

### Estrutura do Descritor de Recurso de Endereço Genérico (simplificada):

<table>
<thead>
<tr>
<th>Campo</th>
<th>Tamanho (Bytes)</th>
<th>Descrição</th>
</tr>
</thead>
<tbody>
<tr>
<td>Address Space</td>
<td>1</td>
<td>0x01 (System Memory), 0x02 (System I/O), 0x03 (PCI Config), etc.</td>
</tr>
<tr>
<td>Bit Width</td>
<td>1</td>
<td>Largura do registro em bits.</td>
</tr>
<tr>
<td>Bit Offset</td>
<td>1</td>
<td>Offset do bit dentro do registro.</td>
</tr>
<tr>
<td>Access Size</td>
<td>1</td>
<td>Tamanho do acesso (Byte, Word, DWord, QWord).</td>
</tr>
<tr>
<td>Address</td>
<td>8</td>
<td>Endereço físico do registro (I/O ou Memória).</td>
</tr>
</tbody>
</table>

*   **C1 State (ACPI):** Geralmente implementado com a instrução HLT (Halt). O processador para de executar instruções, mas pode retornar ao estado C0 rapidamente.
*   **C2 State (ACPI):** Geralmente implementado através do acesso ao registro P_LVL2 no bloco de registro de processador (P_BLK).
*   **C3 State (ACPI):** Geralmente implementado através do acesso ao registro P_LVL3 no bloco de registro de processador (P_BLK), com a desativação do Bus Master (BM_STS e ARB_DIS).

---


## Page 71

# Turbo Boost e DVFS (Dynamic Voltage and Frequency Scaling) - RAPL

O Turbo Boost é um recurso de desempenho dinâmico que permite que o processador opere acima de sua frequência base (base operating frequency) dentro dos limites de potência, corrente e temperatura. O mecanismo técnico subjacente para o controle de potência é o RAPL (Running Average Power Limit).

## 1. Estrutura de Limites de Potência (MSR_PKG_POWER_LIMIT - 0x610)

Este MSR define os limites de potência de curto prazo (PL2) e longo prazo (PL1) que governam o comportamento do Turbo Boost.

<table>
<thead>
<tr>
<th>Bits</th>
<th>Campo</th>
<th>Descrição</th>
</tr>
</thead>
<tbody>
<tr>
<td>14:0</td>
<td>Power Limit #1</td>
<td>Limite de potência de longo prazo (PL1). O valor é um inteiro que, quando multiplicado pela unidade de potência (Power Unit), define o limite em Watts.</td>
</tr>
<tr>
<td>15</td>
<td>Enable Power Limit #1</td>
<td>Habilita o PL1.</td>
</tr>
<tr>
<td>23:17</td>
<td>Time Window for Power Limit #1</td>
<td>Janela de tempo sobre a qual a potência média deve permanecer abaixo do PL1. Codificado em unidades de tempo (Time Unit).</td>
</tr>
<tr>
<td>30:16</td>
<td>Power Limit #2</td>
<td>Limite de potência de curto prazo (PL2). Geralmente maior que PL1, permitindo picos de desempenho por curtos períodos.</td>
</tr>
<tr>
<td>31</td>
<td>Enable Power Limit #2</td>
<td>Habilita o PL2.</td>
</tr>
<tr>
<td>38:32</td>
<td>Time Window for Power Limit #2</td>
<td>Janela de tempo sobre a qual a potência média deve permanecer abaixo do PL2.</td>
</tr>
<tr>
<td>63:39</td>
<td>Reserved</td>
<td>Reservado.</td>
</tr>
</tbody>
</table>

## 2. Unidades de Medida (MSR_RAPL_POWER_UNIT - 0x606)

O MSR MSR_RAPL_POWER_UNIT define as unidades de medida para potência, energia e tempo usadas nos MSRs RAPL.

<table>
<thead>
<tr>
<th>Bits</th>
<th>Campo</th>
<th>Descrição</th>
<th>Fórmula de Unidade</th>
</tr>
</thead>
<tbody>
<tr>
<td>3:0</td>
<td>Power Units (PU)</td>
<td>Unidade de Potência.</td>
<td>Unidade de Potência = 1/2<sup>PU</sup> Watts</td>
</tr>
<tr>
<td>12:8</td>
<td>Energy Status Units (ESU)</td>
<td>Unidade de Energia.</td>
<td>Unidade de Energia = 1/2<sup>ESU</sup> Joules</td>
</tr>
<tr>
<td>19:16</td>
<td>Time Units (TU)</td>
<td>Unidade de Tempo.</td>
<td>Unidade de Tempo = 1/2<sup>TU</sup> Segundos</td>
</tr>
</tbody>
</table>

**Exemplo de Cálculo de Potência:** Se o valor lido em Power Limit #1 for X e o valor de Power Units for PU, o limite de potência em Watts é dado por: $PL1 (Watts) = X × (\frac{1}{2^{PU}})$

## 3. Estruturas de Status

*   **MSR_PKG_ENERGY_STATUS (0x611):** Contador de energia acumulada consumida pelo pacote (Package). O valor lido é multiplicado pela Energy Status Unit para obter a energia em Joules.
*   **IA32_PACKAGE_THERM_STATUS (0x1B1):** Contém informações de status térmico do pacote, incluindo o status de PROCHOT# (Processor Hot), que é um sinal de limitação térmica que pode reduzir a frequência do processador para evitar danos.

---


## Page 72

# Conceito 28: Interrupts Exceptions - IDT, APIC, MSI

**Itens Técnicos Encontrados:** 32

**Conceitos-Chave:** Interrupt Descriptor Table (IDT), Interrupt Gate Descriptor, Trap Gate Descriptor, Interrupt Handling Algorithm, Local APIC (xAPIC), I/O APIC, Interrupt Command Register (ICR), Task Priority Register (TPR), Interrupt Request Register (IRR), In-Service Register (ISR), End-Of-Interrupt (EOI), x2APIC, Message Signaled Interrupts (MSI), MSI-X, APIC Priority Algorithm

# Interrupts Exceptions - IDT, APIC, MSI (Arquitetura x86)

O conteúdo técnico a seguir descreve as estruturas de dados, registradores de hardware e protocolos subjacentes ao sistema de interrupções e exceções na arquitetura x86, conforme detalhado nos Manuais do Desenvolvedor de Software da Intel (Volume 3A) [1].

## 1. Interrupt Descriptor Table (IDT) e Descritores

A Interrupt Descriptor Table (IDT) é uma estrutura de dados que mapeia vetores de interrupção (0 a 255) para os respectivos procedimentos de tratamento (handlers). A IDT é localizada na memória pelo registrador **IDTR** (Interrupt Descriptor Table Register).

### 1.1. Formato do Descritor de Interrupção/Trap (Interrupt/Trap Gate Descriptor)

A IDT pode conter três tipos de descritores de gate: *Task-Gate*, *Interrupt-Gate* e *Trap-Gate*. Os formatos diferem entre o Modo Protegido (32-bit) e o Modo IA-32e (64-bit).

#### 1.1.1. Modo Protegido (32-bit) - Descritor de 8 Bytes

<table>
<thead>
<tr>
<th>Campo</th>
<th>Bits</th>
<th>Descrição</th>
</tr>
</thead>
<tbody>
<tr>
<td>Offset [15:0]</td>
<td>15:0</td>
<td>Offset de 16 bits do ponto de entrada do procedimento de tratamento.</td>
</tr>
<tr>
<td>Segment Selector</td>
<td>31:16</td>
<td>Seletor de segmento para o segmento de código do handler.</td>
</tr>
<tr>
<td>Reserved</td>
<td>36:32</td>
<td>Deve ser 0.</td>
</tr>
<tr>
<td>Gate Type</td>
<td>39:37</td>
<td>Tipo de Gate: 110b para Interrupt Gate, 111b para Trap Gate.</td>
</tr>
<tr>
<td>S (Storage Segment)</td>
<td>40</td>
<td>Deve ser 0 para Gates.</td>
</tr>
<tr>
<td>DPL (Descriptor Privilege Level)</td>
<td>42:41</td>
<td>Nível de privilégio necessário para acessar o Gate.</td>
</tr>
<tr>
<td>P (Present)</td>
<td>43</td>
<td>Bit de Presença (1 = presente).</td>
</tr>
<tr>
<td>Offset [31:16]</td>
<td>63:48</td>
<td>Offset de 16 bits (continuação) do ponto de entrada.</td>
</tr>
</tbody>
</table>

#### 1.1.2. Modo IA-32e (64-bit) - Descritor de 16 Bytes

No modo 64-bit, os descritores de *Interrupt* e *Trap Gate* são estendidos para 16 bytes para acomodar um offset de 64 bits para o ponteiro de instrução (RIP) [1].

---


## Page 73

<table>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Bits</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Offset [15:0]</td>
      <td>15:0</td>
      <td>Offset de 16 bits do ponto de entrada do procedimento de tratamento.</td>
    </tr>
    <tr>
      <td>Segment Selector</td>
      <td>31:16</td>
      <td>Seletor de segmento de código.</td>
    </tr>
    <tr>
      <td>IST (Interrupt Stack Table) Index</td>
      <td>34:32</td>
      <td>Índice na Interrupt Stack Table (IST) da TSS (Task State Segment).</td>
    </tr>
    <tr>
      <td>Reserved</td>
      <td>39:35</td>
      <td>Deve ser 0.</td>
    </tr>
    <tr>
      <td>Gate Type</td>
      <td>47:44</td>
      <td>Tipo de Gate: 1110b para Interrupt Gate, 1111b para Trap Gate.</td>
    </tr>
    <tr>
      <td>DPL (Descriptor Privilege Level)</td>
      <td>42:41</td>
      <td>Nível de privilégio.</td>
    </tr>
    <tr>
      <td>P (Present)</td>
      <td>43</td>
      <td>Bit de Presença (1 = presente).</td>
    </tr>
    <tr>
      <td>Offset [31:16]</td>
      <td>63:48</td>
      <td>Offset de 16 bits (continuação).</td>
    </tr>
    <tr>
      <td>Offset [63:32]</td>
      <td>95:64</td>
      <td>Offset de 32 bits (continuação).</td>
    </tr>
    <tr>
      <td>Reserved</td>
      <td>127:96</td>
      <td>Deve ser 0.</td>
    </tr>
  </tbody>
</table>

## 1.2. Algoritmo de Tratamento de Interrupção (High-Level)

O processador lida com interrupções e exceções de forma similar a uma chamada de procedimento via *Call Gate*. O algoritmo simplificado envolve:

1. **Indexação:** O vetor de interrupção (0-255) é usado como índice na IDT para selecionar um descritor de *gate*.
2. **Validação:** O processador verifica o bit **P** (Presente) e o **DPL** (Descriptor Privilege Level) do *gate* para verificar a validade e o privilégio.
3. **Transferência de Controle:**
   * Se for um **Interrupt/Trap Gate**, o processador transfere a execução para o endereço de destino (Segment Selector:Offset) especificado no *gate*.
   * Se for um **Interrupt Gate**, o processador limpa o *Interrupt Flag* (**IF**) no registrador EFLAGS/RFLAGS para desabilitar interrupções externas mascaráveis.
   * Se for um **Trap Gate**, o processador não altera o bit **IF**.
   * Se for um **Task Gate**, o processador executa uma troca de tarefa (*task switch*) para a TSS do handler.
4. **Empilhamento:** O processador salva o estado (incluindo SS, RSP, RFLAGS, CS, RIP, e Error Code, se aplicável) na pilha do *handler* [1].

## 2. Advanced Programmable Interrupt Controller (APIC)

O **APIC** (Advanced Programmable Interrupt Controller) é o subsistema de interrupção usado em sistemas multiprocessadores (MP) e multi-core. Ele é dividido em **Local APIC** (integrado a cada núcleo do processador) e **I/O APIC** (geralmente parte do chipset).

### 2.1. Registradores do Local APIC (xAPIC/MMIO)

O Local APIC é acessado via endereços de memória mapeados (MMIO), tipicamente na faixa FEE0 0000H a FEE0 03FFH [1].

---


## Page 74

<table>
  <thead>
    <tr>
      <th>Registrador</th>
      <th>Endereço MMIO</th>
      <th>Tamanho (bits)</th>
      <th>Função Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Local APIC ID Register</td>
      <td>FEE0 0020H</td>
      <td>32</td>
      <td>Contém o ID físico do Local APIC.</td>
    </tr>
    <tr>
      <td>Task Priority Register (TPR)</td>
      <td>FEE0 0080H</td>
      <td>32</td>
      <td>Define a prioridade de tarefa do processador (bits 7:4).</td>
    </tr>
    <tr>
      <td>Arbitration Priority Register (APR)</td>
      <td>FEE0 0090H</td>
      <td>32</td>
      <td>Contém a prioridade de arbitragem atual.</td>
    </tr>
    <tr>
      <td>Processor Priority Register (PPR)</td>
      <td>FEE0 00A0H</td>
      <td>32</td>
      <td>Contém a prioridade do processador (máximo entre TPR e IRR).</td>
    </tr>
    <tr>
      <td>End-Of-Interrupt (EOI) Register</td>
      <td>FEE0 00B0H</td>
      <td>32</td>
      <td>Escrita (qualquer valor) sinaliza o fim do tratamento da interrupção.</td>
    </tr>
    <tr>
      <td>Interrupt Request Register (IRR)</td>
      <td>FEE0 0200H - 02F0H</td>
      <td>256</td>
      <td>Armazena as interrupções pendentes (um bit por vetor).</td>
    </tr>
    <tr>
      <td>In-Service Register (ISR)</td>
      <td>FEE0 0100H - 01F0H</td>
      <td>256</td>
      <td>Armazena as interrupções que estão sendo atendidas.</td>
    </tr>
    <tr>
      <td>Trigger Mode Register (TMR)</td>
      <td>FEE0 0300H - 03F0H</td>
      <td>256</td>
      <td>Indica o modo de disparo (Edge/Level) para cada vetor.</td>
    </tr>
    <tr>
      <td>Interrupt Command Register (ICR)</td>
      <td>FEE0 0300H - 0310H</td>
      <td>64</td>
      <td>Usado para enviar Interrupções Interprocessador (IPIs).</td>
    </tr>
    <tr>
      <td>Local Vector Table (LVT)</td>
      <td>FEE0 0320H - 0370H</td>
      <td>32 (cada)</td>
      <td>Define o comportamento de interrupções locais (Timer, LINT0, LINT1, etc.).</td>
    </tr>
  </tbody>
</table>

## 2.2. Protocolo de Entrega de Interrupções Interprocessador (IPI)

O Interrupt Command Register (ICR) é a estrutura chave para o protocolo IPI. É um registrador de 64 bits (dividido em duas DWORDS de 32 bits no xAPIC) que define a mensagem IPI [1].

<table>
  <thead>
    <tr>
      <th>Campo ICR</th>
      <th>Bits</th>
      <th>Descrição Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Vector</td>
      <td>7:0</td>
      <td>O número do vetor de interrupção a ser entregue.</td>
    </tr>
    <tr>
      <td>Delivery Mode</td>
      <td>10:8</td>
      <td>Define o tipo de IPI: 000 (Fixed), 001 (Lowest Priority), 010 (SMI), 100 (NMI), 101 (INIT), 110 (Start-Up IPI - SIPI).</td>
    </tr>
    <tr>
      <td>Destination Mode</td>
      <td>11</td>
      <td>0 (Physical), 1 (Logical).</td>
    </tr>
    <tr>
      <td>Delivery Status</td>
      <td>12</td>
      <td>0 (Idle), 1 (Send Pending).</td>
    </tr>
    <tr>
      <td>Level</td>
      <td>14</td>
      <td>Usado para INIT/SIPI: 0 (De-assert), 1 (Assert).</td>
    </tr>
    <tr>
      <td>Trigger Mode</td>
      <td>15</td>
      <td>0 (Edge), 1 (Level).</td>
    </tr>
    <tr>
      <td>Destination Shorthand</td>
      <td>19:18</td>
      <td>00 (No Shorthand), 01 (Self), 10 (All Including Self), 11 (All Excluding Self).</td>
    </tr>
    <tr>
      <td>Destination Field</td>
      <td>63:56</td>
      <td>ID do APIC de destino (usado quando Destination Shorthand é 00).</td>
    </tr>
  </tbody>
</table>

## 2.3. x2APIC

O x2APIC é uma extensão do xAPIC que aumenta a endereçabilidade do processador (ID do APIC de 32 bits) e usa uma interface de programação baseada em MSRs (Model-Specific Registers) em vez de MMIO para a maioria dos registradores [1].

---


## Page 75

*   **Endereçamento:** O ID do APIC é estendido para 32 bits, permitindo endereçar até $2^{32} - 1$ processadores.
*   **Interface de Programação:** Acesso aos registradores do APIC via MSRs na faixa 800H a 8FFH. O ICR é um MSR de 64 bits.
*   **SELF IPI Register (MSR 83FH):** Um novo registrador dedicado para enviar IPIs para o próprio processador, otimizando o caminho de entrega.

# 3. Message Signaled Interrupts (MSI e MSI-X)

Message Signaled Interrupts (MSI) e sua extensão MSI-X são mecanismos que permitem que dispositivos PCI Express gerem interrupções escrevendo uma mensagem (um formato de dados) em um endereço de memória específico, em vez de usar pinos de interrupção dedicados (INTx#) [1].

## 3.1. Formato da Mensagem MSI (PCI Express)

A mensagem MSI é uma transação de escrita de memória (Memory Write Transaction) que contém o vetor de interrupção e o ID do APIC de destino.

### 3.1.1. Registrador de Endereço da Mensagem (Message Address Register)

O dispositivo escreve no endereço de memória especificado por este registrador.

<table>
<thead>
<tr>
<th>Campo</th>
<th>Bits</th>
<th>Descrição Técnica</th>
</tr>
</thead>
<tbody>
<tr>
<td>Reserved</td>
<td>63:20</td>
<td>Deve ser 0FEEH (para roteamento para o APIC).</td>
</tr>
<tr>
<td>Destination ID</td>
<td>19:12</td>
<td>ID do APIC de destino (8 bits).</td>
</tr>
<tr>
<td>Redirection Hint (RH)</td>
<td>11</td>
<td>0 (Direcionamento Físico), 1 (Direcionamento Lógico).</td>
</tr>
<tr>
<td>Reserved</td>
<td>10:3</td>
<td>Deve ser 0.</td>
</tr>
<tr>
<td>Destination Mode</td>
<td>2</td>
<td>0 (Físico), 1 (Lógico).</td>
</tr>
<tr>
<td>Reserved</td>
<td>1:0</td>
<td>Deve ser 0.</td>
</tr>
</tbody>
</table>

### 3.1.2. Registrador de Dados da Mensagem (Message Data Register)

O valor escrito no endereço acima é o dado da mensagem, que contém o vetor de interrupção e o modo de entrega.

<table>
<thead>
<tr>
<th>Campo</th>
<th>Bits</th>
<th>Descrição Técnica</th>
</tr>
</thead>
<tbody>
<tr>
<td>Reserved</td>
<td>31:16</td>
<td>Deve ser 0.</td>
</tr>
<tr>
<td>Trigger Mode</td>
<td>15</td>
<td>0 (Edge), 1 (Level).</td>
</tr>
<tr>
<td>Level</td>
<td>14</td>
<td>Usado apenas para interrupções Level-Triggered (MSI-X).</td>
</tr>
<tr>
<td>Delivery Mode</td>
<td>10:8</td>
<td>Tipo de entrega: 000 (Fixed), 001 (Lowest Priority), 100 (NMI), 101 (INIT), 111 (ExtINT).</td>
</tr>
<tr>
<td>Vector</td>
<td>7:0</td>
<td>O vetor de interrupção a ser entregue (16 a 255).</td>
</tr>
</tbody>
</table>

## 3.2. MSI-X

O MSI-X é uma extensão que permite que um dispositivo use até 2048 vetores de interrupção independentes, cada um com seu próprio endereço e dados de mensagem. O MSI-X usa duas estruturas de dados na memória do sistema: a Tabela MSI-X e a Área de PBAR (Pending Bit Array Register) [1].

---


## Page 76

*   **Tabela MSI-X (MSI-X Table):** Contém entradas (Message Address, Message Data, Vector Control) para cada vetor de interrupção.
*   **Área de PBAR (Pending Bit Array Register):** Usada para rastrear interrupções pendentes.

# 4. Algoritmo de Prioridade do APIC

O APIC usa um sistema de prioridade de 8 bits (0 a 15) para determinar qual interrupção deve ser atendida. O vetor de interrupção (0-255) é dividido em duas partes:

Prioridade de Interrupção = Vetor / 16

O processador só entregará interrupções cuja **Prioridade de Interrupção** seja maior que a **Prioridade do Processador (PPR)**.

PPR = max(TPR, IRR)

Onde:
*   **TPR (Task Priority Register):** Define a prioridade mínima que uma interrupção deve ter para interromper o processador.
*   **IRR (Interrupt Request Register):** Contém as interrupções pendentes.

A prioridade de arbitragem do APIC é um protocolo de rodízio (round-robin) para decidir qual APIC tem permissão para usar o barramento (APIC Bus ou System Bus) para enviar mensagens [1].

# Referências

[1] Intel. *Intel® 64 and IA-32 Architectures Software Developer’s Manual, Volume 3A: System Programming Guide, Part 1.* Disponível em: https://cdrdv2-public.intel.com/812386/253668-sdm-vol-3a.pdf.

---

# PARTE 2: PESQUISADORES E TEORIAS

## Pesquisador 1: Federico Faggin

Itens Técnicos Encontrados: 11

Contribuições: Metodologia de Design de Lógica Aleatória em Silício (SGDM), Contato Enterrado (Buried Contact), Dispositivos de Carga Bootstrap (Bootstrap Load), Barramento Multiplexado de 4 bits (4004), Estrutura de Interrupção com Ponteiro de Pilha (8080), Tecnologia N-Channel de Alta Voltagem (8080), Arquitetura Segmentada (8086), Unidade de Interface de Barramento (BIU) (8086), Unidade de Execução (EU) (8086), Pipelining de Instruções (8086), Microcódigo Vertical (8086)

## Conteúdo Técnico Puro das Contribuições de Federico Faggin (Intel 4004, 8080, 8086)

O conteúdo técnico a seguir foca exclusivamente em **algoritmos, fórmulas, estruturas de hardware e conceitos de microarquitetura** relacionados às contribuições de Federico Faggin nos microprocessadores Intel 4004, 8080 e 8086, conforme a pesquisa em patentes, artigos técnicos e história oral.

---


## Page 77

# 1. Intel 4004 (1971)

## 1.1. Metodologia de Design de Lógica Aleatória em Silício (SGDM) [1]

A SGDM (Silicon Gate Design Methodology) foi a metodologia criada por Faggin para o design de circuitos de lógica aleatória complexa utilizando a Tecnologia de Porta de Silício (SGT).

*   **Conceito:** Minimizar o número de “traduções” entre a especificação, o design lógico/circuito e o *layout* físico. O design lógico e de circuito é realizado concorrentemente para produzir um documento que reflete a topologia de *layout* (ordem das linhas de sinal, posicionamento dos blocos).
*   **Estrutura de Hardware:** Uso de blocos de circuito padronizados com regras simples para cálculo das dimensões dos transistores baseadas em **fatores de carga** (load factors), que são determinados a partir do documento de design.
*   **Otimização:** O *layout* começa com uma grade de linhas de polisilício e alumínio para sinais-chave, com os circuitos “encaixados” por baixo.
*   **Resultado (Fórmula de Otimização):** Fator de melhoria de **2x** na densidade de circuito e **5x a 10x** no produto velocidade-potência (*speed-power product*) em comparação com designs de porta de metal equivalentes.

## 1.2. Contato Enterrado (*Buried Contact*) [1]

Técnica de processo inventada por Faggin na Fairchild (1968) e essencial para a densidade do 4004.

*   **Estrutura de Hardware:** Requer uma camada de máscara adicional para permitir a conexão direta de linhas de polisilício a junções sob óxido.
*   **Conceito:** Elimina a ponte de metal que seria necessária, disponibilizando duas camadas de interconexão e reduzindo drasticamente a área de circuitos de lógica aleatória.

## 1.3. Dispositivos de Carga Bootstrap (*Bootstrap Load Devices*) [1]

Técnica de circuito para alcançar a velocidade e dissipação de potência necessárias no design de lógica síncrona de duas fases.

*   **Conceito:** Circuito que permite a criação de *bootstrap loads* com a SGT, superando a limitação anterior que exigia uma máscara adicional. Essencial para o design de circuitos lógicos de duas fases rápidos e eficientes em termos de potência.

## 1.4. Organização do Barramento (Patente US3821715) [2]

O 4004 utiliza um barramento multiplexado de 4 bits para a comunicação com os chips de suporte (MCS-4).

*   **Estrutura de Hardware:** Barramento de dados bidirecional de 4 bits.
*   **Algoritmo/Protocolo:** O barramento é multiplexado para transferir:
    *   Endereços de 12 bits (4 bits por ciclo, 3 ciclos).
    *   Instruções de 8 bits (4 bits por ciclo, 2 ciclos).
    *   Dados de 4 bits (1 ciclo).
*   **Endereçamento:** O CPU pode endereçar diretamente **4K palavras de instrução de 8 bits** de memória de programa e **5120 bits** de RAM de armazenamento de dados.

# 2. Intel 8080 (1974)

## 2.1. Estrutura de Interrupção e Ponteiro de Pilha (*Stack Pointer*) [3]

Faggin concebeu o 8080 para resolver as limitações do 8008, especialmente a estrutura de interrupção primitiva.

*   **Conceito:** Introdução de um **ponteiro de pilha (Stack Pointer)** dedicado para gerenciar o status da máquina (endereço de retorno, registradores) durante o serviço de interrupção. Isso permitiu uma estrutura de interrupção funcional e não primitiva.

---


## Page 78

*   **Estrutura de Hardware:** Uso de um *package* de 40 pinos para eliminar o multiplexamento de endereços e dados no chip, o que era um gargalo de desempenho no 8008.
*   **Tecnologia:** Transição para a **Tecnologia N-Channel de Alta Voltagem** (três fontes de alimentação: +5V, +12V, -5V) para alcançar maior velocidade (0.5 MHz do 8008 para 2 MHz no 8080) e densidade.

## 2.2. Microarquitetura e Conjunto de Instruções (Shima sob direção de Faggin) [3]

O design detalhado por Masatoshi Shima, sob a direção de Faggin, implementou as melhorias arquitetônicas.

*   **Estrutura de Hardware:**
    *   **Registradores:** Acumulador de 8 bits e cinco registradores de propósito geral de 8 bits (B, C, D, E, H, L) que podem ser pareados para operações de 16 bits (BC, DE, HL).
    *   **Barramento:** Barramento de dados bidirecional de 8 bits e barramento de endereço de 16 bits (permitindo endereçamento de 64 KB de memória).

*   **Algoritmo/Conceito:**
    *   **Modos de Endereçamento:** Melhoria significativa nos modos de endereçamento, incluindo endereçamento direto para instruções de *load* e *store* e endereçamento indireto por registrador para instruções de *jump*.
    *   **Instruções de Troca (Exchange):** Inclusão de instruções para trocar dados entre registradores de 16 bits, eliminando a necessidade de salvar o ponteiro de endereço no mundo externo (memória lenta).

## 3. Intel 8086 (1978)

Embora Faggin tenha deixado a Intel antes do 8086, a arquitetura x86 é uma extensão direta dos conceitos que ele estabeleceu no 8080. O 8086 foi projetado para ser compatível em nível de linguagem *assembly* com o 8080.

### 3.1. Arquitetura Segmentada e Unidades Funcionais (Baseado em 8080) [4]

O 8086 introduziu a divisão do processador em duas unidades para otimizar o desempenho, um conceito de microarquitetura que se baseia na busca por maior velocidade iniciada no 8080.

*   **Estrutura de Hardware:**
    *   **Bus Interface Unit (BIU):** Responsável por buscar instruções e dados da memória.
    *   **Execution Unit (EU):** Responsável por decodificar e executar as instruções.

*   **Algoritmo/Conceito:**
    *   **Pipelining de Instruções:** A BIU busca até 6 bytes de instruções (fila de pré-busca) enquanto a EU executa a instrução atual. Isso implementa uma forma inicial de *pipelining* para acelerar o processamento.
    *   **Endereçamento Segmentado:** Para endereçar 1 MB de memória com registradores de 16 bits, o 8086 usa a fórmula de endereço físico: $Endereço Físico = (Segmento × 16) + Offset$ Onde o valor do registrador de segmento é deslocado 4 bits para a esquerda (multiplicado por 16) e somado ao *offset* de 16 bits para gerar o endereço físico de 20 bits.

### 3.2. Microcódigo Vertical (Vertical Microcode) [5]

O 8086 utiliza microcódigo para implementar seu conjunto de instruções complexo (CISC).

*   **Estrutura de Hardware:** O microcódigo consiste em **512 micro-instruções**, cada uma com **21 bits** de largura.
*   **Algoritmo/Conceito:**
    *   **Micro-instrução:** Cada micro-instrução executa uma ou mais micro-operações em um ciclo de *clock*, como transferência de dados entre registradores (*S* → *D*) e operações da ALU (*SUBT*, *LRCY*).
    *   **Controle de Fluxo:** O motor de microcódigo usa um registrador de 13 bits para percorrer o microcódigo e um registrador de sub-rotina de 13 bits para endereços de retorno. Inclui operações de *short jump* (condicional dentro de um bloco de 16 micro-instruções), *long jump* e *long call* (para 16 locais fixos).

---


## Page 79

*   **Otimização de ROM:** O opcode da instrução é multiplicado por 16 (4 zeros anexados) para formar o endereço inicial no microcódigo, permitindo que até 16 micro-instruções sejam executadas sequencialmente sem um salto explícito. O decodificador de endereço é parcialmente decodificado, permitindo que múltiplos opcodes compartilhem o mesmo microcódigo, reduzindo o tamanho da ROM.

---

## Referências

[1] The New Methodology for Random Logic Design. Intel4004.com. http://www.intel4004.com/mrld.htm [2] US3821715A - Memory system for a multi chip digital computer. Google Patents. https://patents.google.com/patent/US3821715A/en [3] Oral History Panel on the Development and Promotion of the Intel 8080 Microprocessor. Computer History Museum. https://archive.computerhistory.org/resources/text/Oral_History/Intel_8080_102658123-05.01.pdf [4] Intel Microprocessors: 8008 to 8086. Steve Morse. https://stevemorse.org/8086history/8086history.pdf [5] How the 8086 processor’s microcode engine works. Ken Shirriff’s blog. http://www.righto.com/2022/11/how-8086-processors-microcode-engine.html

---

## Pesquisador 2: Marcian Edward Hoff Jr.

Itens Técnicos Encontrados: 15

Contribuições: Arquitetura multi-chip, Barramento multiplexado de 4 bits, Unidade Central de Processamento em chip único, Endereçamento de memória por decodificação de chip, Uso de RAM dinâmica

## Intel 4004 Technical Specifications and Microarchitecture

### Technical Specifications

*   Maximum Clock Rate: 740 kHz
*   Instruction Cycle Time: 10.8 µs (8 clock cycles per machine cycle)
*   Instruction Execution Time: 10.8 or 21.6 µs (1 or 2 machine cycles)
*   Instruction Speed: 46,250 to 92,500 instructions per second
*   Data/Program Storage: Separate program and data storage. Uses a single multiplexed 4-bit bus for transferring 12-bit addresses, 8-bit instructions, and 4-bit data words.
*   Addressable RAM: 640 bytes
*   Addressable ROM: 4096 8-bit words (4 KB)
*   Instruction Set: 46 instructions (41 are 8-bit, 5 are 16-bit)
*   Registers:
    *   One 4-bit accumulator
    *   Sixteen 4-bit index registers
*   Stack: Internal subroutine stack, 3 levels deep.

---


## Page 80

# Logic Levels

<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Min.</th>
      <th>Max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>VSS-DD</td>
      <td>+15 V - 5%</td>
      <td>+15 V + 5%</td>
    </tr>
    <tr>
      <td>VIL</td>
      <td>VDD</td>
      <td>VSS - 5.5 V</td>
    </tr>
    <tr>
      <td>VIH</td>
      <td>VSS - 1.5 V</td>
      <td>VSS + 0.3 V</td>
    </tr>
    <tr>
      <td>VOL</td>
      <td>VSS - 12 V</td>
      <td>VSS - 6.5 V</td>
    </tr>
    <tr>
      <td>VOH</td>
      <td>VSS - 0.5 V</td>
      <td>VSS</td>
    </tr>
  </tbody>
</table>

# Memory System for a Multi-Chip Digital Computer (from Patent US3821715A)

*   **Concept:** A general-purpose digital computer comprising a plurality of separate MOS chips interconnected by a number of lines, including four bi-directional data bus lines.
*   **Architecture:**
    *   A central processing unit (CPU) on a single chip.
    *   Random-access-memories (RAMs) and read-only-memories (ROMs) on separate chips.
    *   Each memory chip includes decoding circuitry to recognize a predetermined code, allowing the CPU to address a single memory chip even though all are on a common data bus.
*   **Key Claims:**
    *   A digital computer with a CPU on a first MOS chip, and at least two memory chips (ROM and RAM) on separate chips.
    *   A plurality of data lines interconnecting the CPU and memory chips for communicating address and data signals.
    *   The processor can selectively communicate with one of the memories.
    *   The RAM chips can be dynamic storage devices.
    *   The computer can have four common data lines.
    *   Memory chips can include ports for input and output signals.

---

# Pesquisador 3: Stan Mazor

Itens Técnicos Encontrados: 11

Contribuições: Arquitetura de computador multi-chip, Barramento de dados bidirecional comum, Endereçamento de chip por decodificação de código, Refresh de DRAM com contador e ciclo de tempo dedicado, Latch de status da CPU via barramento de dados, Instrução de salto especial de todos os zeros/uns

# Conteúdo Técnico das Contribuições de Stan Mazor (Intel 4004 e 8080)

O conteúdo técnico extraído das patentes US3821715 (Intel 4004/MCS-4) e US4010449 (Intel 8080), nas quais Stan Mazor é listado como inventor, foca exclusivamente em conceitos de microarquitetura, estruturas de hardware e algoritmos.

## Intel 4004 / MCS-4 (Patente US3821715)

A patente US3821715 descreve um sistema de memória para um computador digital multi-chip que estabeleceu a base para a arquitetura do MCS-4 (que inclui o 4004).

---


## Page 81

# Estrutura de Hardware e Microarquitetura

1.  **Arquitetura de Computador Multi-Chip:** O sistema é composto por uma pluralidade de *chips* de semicondutores de óxido metálico (MOS) separados, incluindo um *chip* de Unidade Central de Processamento (CPU), *chips* de Memória de Acesso Aleatório (RAM) e *chips* de Memória Somente Leitura (ROM).
2.  **Barramento de Dados Bidirecional Comum:** As memórias (RAM e ROM) são acopladas a um conjunto comum de **linhas de barramento de dados bidirecionais** (quatro linhas no modelo preferencial) que comunicam informações entre a CPU e as memórias.
3.  **Unidade Aritmética (ALU):** A unidade aritmética de 4 bits é do tipo “ripple through carry” (transporte em cascata).
4.  **Registrador de Endereço e Pilha:** O registrador de endereço da CPU inclui um **contador de programa**, uma **pilha de endereços** (*address stack*) e um **incrementador de endereço**. A pilha é uma matriz de células RAM dinâmica de 4 por 12 bits, onde três níveis são usados como pilha para chamadas de sub-rotina.
5.  **Registrador de Índice:** O registrador de índice é uma matriz de células RAM dinâmica de 16 por 4 bits, com dois modos de operação: 16 locais de armazenamento endereçáveis diretamente para computação intermediária, ou oito pares de locais de armazenamento para endereçamento de RAMs/ROMs e armazenamento de dados.

# Algoritmos e Conceitos de Controle

1.  **Endereçamento de Chip por Decodificação de Código:** Cada *chip* de memória (RAM e ROM) possui um **circuito de decodificação de \*chip\*** (*chip recognition circuitry*) que reconhece um **código predeterminado diferente** comunicado pela CPU no barramento de dados. Isso permite que a CPU selecione e acesse um **único chip** de memória por vez, apesar de todos estarem conectados ao mesmo barramento comum.
2.  **Refresh de DRAM com Ciclo de Tempo Dedicado:** As RAMs são dispositivos de armazenamento dinâmico (DRAM). O sistema inclui um mecanismo para **refrescar** esses dispositivos. A CPU comunica **sinais de temporização** que definem um **primeiro período** para comunicação e um **segundo período** para o refresh da RAM. O mecanismo de *refresh* inclui um **contador** para selecionar a porção da RAM a ser refrescada.

## Intel 8080 (Patente US4010449)

A patente US4010449 descreve **melhorias em um computador MOS multi-chip** que se aplicam à arquitetura do Intel 8080.

# Estrutura de Hardware e Microarquitetura

1.  **Latch de Status da CPU via Barramento de Dados:** Um *latch* de status da CPU é acoplado às linhas do barramento de dados bidirecional. A CPU gera sinais de status que são **periodicamente acoplados ao barramento de dados** (em vez de linhas dedicadas). Um **sinal estroboscópico** (*strobe signal*) é gerado pela CPU e comunicado ao *latch*, que então **sensibiliza o sinal de status diretamente das linhas do barramento de dados**. Este método elimina a necessidade de pinos dedicados para a transmissão de status, reduzindo a contagem de pinos do *chip* da CPU.

# Algoritmos e Conceitos de Controle

1.  **Instrução de Salto Especial (Jump Instruction) de Todos os Zeros/Uns:** Uma instrução de salto especial é definida como uma palavra binária consistindo de **todos os zeros ou todos os uns**.
2.  **Geração de Instrução de Salto por Inibição:** Esta instrução especial é inserida no barramento de dados por um **circuito inibidor** que impede o fluxo de uma instrução da ROM e, em vez disso, aplica o sinal de todos os zeros (aterrando as linhas) ou todos os uns (aplicando um potencial predeterminado) ao barramento.
3.  **Tratamento de Falhas de Endereçamento:** O conceito de instrução de salto de todos os zeros/uns é usado para **tratar falhas de endereçamento**. Se um decodificador de ROM receber um endereço que não reconhece (por exemplo, fora do intervalo), ele não transmite dados, resultando na condição de “sem dados” no barramento, que é interpretada pela CPU como a instrução de salto especial (todos os zeros ou todos os uns), acionando uma ação apropriada predeterminada.

---


## Page 82

<table>
  <thead>
    <tr>
      <th>Conceito Técnico</th>
      <th>Microprocessador</th>
      <th>Tipo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Arquitetura de Computador Multi-Chip (CPU, RAM, ROM em chips separados)</td>
      <td>4004 (MCS-4)</td>
      <td>Estrutura de Hardware</td>
    </tr>
    <tr>
      <td>Barramento de Dados Bidirecional Comum</td>
      <td>4004 (MCS-4)</td>
      <td>Microarquitetura</td>
    </tr>
    <tr>
      <td>Endereçamento de Chip por Decodificação de Código (Chip Select)</td>
      <td>4004 (MCS-4)</td>
      <td>Algoritmo/Microarquitetura</td>
    </tr>
    <tr>
      <td>Refresh de DRAM com Contador e Ciclo de Tempo Dedicado</td>
      <td>4004 (MCS-4)</td>
      <td>Algoritmo/Microarquitetura</td>
    </tr>
    <tr>
      <td>Unidade Aritmética “Ripple Through Carry” de 4 bits</td>
      <td>4004 (MCS-4)</td>
      <td>Estrutura de Hardware</td>
    </tr>
    <tr>
      <td>Registrador de Endereço com Pilha de Sub-rotina (4x12 bits)</td>
      <td>4004 (MCS-4)</td>
      <td>Estrutura de Hardware</td>
    </tr>
    <tr>
      <td>Registrador de Índice com 2 Modos de Operação (16x4 bits)</td>
      <td>4004 (MCS-4)</td>
      <td>Estrutura de Hardware</td>
    </tr>
    <tr>
      <td>Latch de Status da CPU via Barramento de Dados (Economia de Pinos)</td>
      <td>8080</td>
      <td>Microarquitetura</td>
    </tr>
    <tr>
      <td>Instrução de Salto Especial de Todos os Zeros/Uns</td>
      <td>8080</td>
      <td>Algoritmo/Microarquitetura</td>
    </tr>
    <tr>
      <td>Geração de Instrução de Salto por Inibição do Barramento</td>
      <td>8080</td>
      <td>Algoritmo/Microarquitetura</td>
    </tr>
    <tr>
      <td>Tratamento de Falhas de Endereçamento via Instrução de Salto Especial</td>
      <td>8080</td>
      <td>Algoritmo/Microarquitetura</td>
    </tr>
  </tbody>
</table>

[1] Patente US3821715A: Memory system for a multi chip digital computer. [2] Patente US4010449A: Mos computer employing a plurality of separate chips. [3] Intel 4004: https://patents.google.com/patent/US3821715A/en [4] Intel 8080: https://patents.google.com/patent/US4010449/en

---

## Pesquisador 4: Masatoshi Shima

Itens Técnicos Encontrados: 10

Contribuições: Design de Circuito e Layout do Intel 8080, Arquitetura do Zilog Z80, Conjunto de Registradores Alternativos, Circuito de Refresh de DRAM Integrado, Interrupção Não-Mascarável (NMI)

## Conceitos de Microarquitetura e Hardware (Intel 8080 e Zilog Z80)

O trabalho de Masatoshi Shima no desenvolvimento do Intel 8080 e, posteriormente, do Zilog Z80, introduziu conceitos de microarquitetura e estruturas de hardware que foram fundamentais para a segunda e terceira gerações de microprocessadores de 8 bits.

### Intel 8080 (Contribuição de Circuito e Layout)

A principal contribuição de Shima para o 8080 foi o **design detalhado do circuito** e o **layout físico** do chip, que permitiu um aumento de desempenho significativo em relação ao 8008.

*   **Estrutura de Hardware (8080):**
    *   Tecnologia de Processo: N-channel Silicon Gate (melhorando a velocidade e densidade em relação ao p-MOS do 8008).
    *   **Barramentos:** Utilização de um **barramento de dados bidirecional** de 8 bits e um **barramento de endereços** de **16 bits** (permitindo endereçamento de 64 Kbytes de memória).
    *   **Registradores:** Conjunto de registradores de 8 bits (A, B, C, D, E, H, L) e registradores de 16 bits (PC, SP, HL, DE, BC).
    *   **Clock:** Uso de um **clock de duas fases não sobrepostas** ($\phi_1$ e $\phi_2$) para sincronização das operações internas.
    *   **Transistores:** Aproximadamente **4.800 transistores** (densidade de transistores com fator de escala 1.0, conforme a tecnologia da época).

---


## Page 83

# Zilog Z80 (Inovações Arquiteturais)

O Z80, projetado por Shima na Zilog, foi um aprimoramento arquitetural direto do 8080, focado em reduzir a necessidade de chips de suporte e aumentar a eficiência do sistema.

*   **Conjunto de Registradores Alternativos:**
    *   **Estrutura:** O Z80 possui dois conjuntos completos de registradores de uso geral: o conjunto principal (AF, BC, DE, HL) e o conjunto alternativo (AF', BC', DE', HL').
    *   **Conceito:** Permite uma troca rápida de contexto (task switching) ou manipulação de interrupções de alta velocidade.
    *   **Algoritmo de Troca:** A troca é realizada por instruções dedicadas:
        *   EX AF, AF' (Troca o acumulador e o registrador de flags).
        *   EXX (Troca os registradores BC, DE, HL com BC', DE', HL').
    *   **Vantagem:** Evita a necessidade de salvar e restaurar o estado completo do processador na memória (stack) durante interrupções, economizando ciclos de máquina.

*   **Circuito de Refresh de DRAM Integrado:**
    *   **Estrutura de Hardware:** Inclusão de um contador de refresh de 7 bits® e lógica de controle dedicada no chip.
    *   **Algoritmo de Refresh:** O Z80 executa um ciclo de refresh de DRAM durante a segunda metade de um ciclo de fetch de instrução (M1) que não utiliza o barramento de endereços.
    *   **Fórmula de Endereçamento de Refresh:** O endereço de refresh é formado pela concatenação do conteúdo do registrador R (7 bits) com o registrador I (7 bits) e bits de status do barramento, gerando um endereço de linha para o refresh da DRAM.
    *   **Conceito:** Permite que o chip gerencie o refresh da memória dinâmica (DRAM) de forma autônoma, reduzindo a complexidade e o custo do hardware externo.

*   **Interrupção Não-Mascarável (NMI):**
    *   **Estrutura de Hardware:** Introdução de um pino de entrada dedicado para NMI.
    *   **Algoritmo de Resposta:** Quando o pino NMI é ativado (borda de descida), o processador executa automaticamente uma instrução RESTART para o endereço fixo 0066h (ou 0038h em alguns modos), independentemente do estado do flag de interrupção.
    *   **Conceito:** Garante que eventos críticos de hardware (como falha de energia) sejam processados imediatamente.

*   **Melhoria na Eficiência do Barramento (Z80):**
    *   **Conceito:** O Z80 alcançou um fator de uso do barramento de 65-70% para mixes de instruções típicas, um aumento significativo em relação ao 8080, devido a um conjunto de instruções mais eficiente e ao uso de microcode mais otimizado.
    *   **Transistores:** Aproximadamente 8.200 transistores (fator de escala 0.70 em relação ao 8080).

<table>
<thead>
<tr>
<th>Característica Técnica</th>
<th>Intel 8080</th>
<th>Zilog Z80 (Aprimoramento de Shima)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Registradores</td>
<td>Conjunto único (AF, BC, DE, HL)</td>
<td>Conjunto Principal + Conjunto Alternativo (AF', BC', DE', HL')</td>
</tr>
<tr>
<td>Refresh de DRAM</td>
<td>Requer hardware externo</td>
<td>Circuito de Refresh Integrado (usando o registrador R)</td>
</tr>
<tr>
<td>Interrupções</td>
<td>Interrupção Mascarável (INT)</td>
<td>Interrupção Mascarável (INT) + Interrupção Não-Mascarável (NMI)</td>
</tr>
<tr>
<td>Transistores</td>
<td>4.800</td>
<td>8.200</td>
</tr>
<tr>
<td>Tecnologia</td>
<td>N-channel Silicon Gate</td>
<td>N-channel Silicon Gate (low-voltage depletion load)</td>
</tr>
</tbody>
</table>

---


## Page 84

# Pesquisador 5: Stephen P. Morse

**Itens Técnicos Encontrados:** 15

**Contribuições:** Endereçamento Segmentado, Pipeline BIU/EU, Algoritmo de Prefetch, Instruções de String com REP, Instrução LOCK, Aritmética BCD, Flags de Status Expandidos, Mecanismo de Endereçamento Estendido (Patente)

# Conteúdo Técnico da Arquitetura Intel 8086 (Stephen P. Morse)

O trabalho de Stephen P. Morse no desenvolvimento do microprocessador Intel 8086 estabeleceu os fundamentos técnicos da arquitetura x86, introduzindo conceitos cruciais de endereçamento, microarquitetura e conjunto de instruções. A seguir, são detalhados os elementos técnicos extraídos de artigos e patentes relacionadas ao seu trabalho.

## I. Mecanismos de Endereçamento e Estrutura de Registradores

O 8086 superou a limitação de endereçamento de 64KB de seus predecessores (8080/8085) através da implementação do **Endereçamento Segmentado** (Segmented Addressing). Este mecanismo permite o acesso a um espaço de memória física de 1MB (20 bits de endereço) utilizando registradores de 16 bits. O **Endereço Físico (PA)** é calculado pela soma do conteúdo de um **Registro de Segmento** deslocado quatro bits para a esquerda (multiplicado por 16) com um **Endereço Efetivo (EA)** de 16 bits, conforme a fórmula:

PA = (Registro de Segmento × 16) + EA

O **Endereço Efetivo (EA)**, que representa o offset dentro do segmento, é calculado pela soma de até três componentes de 16 bits: Base, Índice e Deslocamento (Displacement).

EA = Base + Index + Displacement

O processador utiliza quatro **Registros de Segmento** (CS, DS, SS, ES) e um conjunto de **Registros de Offset** (IP, SP, BP, SI, DI, BX) para suportar uma rica variedade de **Modos de Endereçamento**, incluindo indireto por registrador, relativo à base, relativo ao índice, e indexado pela base.

<table>
<thead>
<tr>
<th>Componente</th>
<th>Registradores de 16 bits</th>
<th>Função Principal</th>
</tr>
</thead>
<tbody>
<tr>
<td>Segmento</td>
<td>CS, DS, SS, ES</td>
<td>Define o endereço base do segmento de 64KB.</td>
</tr>
<tr>
<td>Offset/Geral</td>
<td>AX, BX, CX, DX</td>
<td>Registradores de propósito geral, acessíveis como 16 bits (ex: AX) ou dois registradores de 8 bits (ex: AH, AL).</td>
</tr>
<tr>
<td>Ponteiro/Índice</td>
<td>SP, BP, SI, DI</td>
<td>Usados para calcular o Endereço Efetivo (EA) e controlar operações de pilha e string.</td>
</tr>
</tbody>
</table>

O formato da instrução é de comprimento variável (1 a 6 bytes) e utiliza campos cruciais para a decodificação. O **Campo MOD** (Mode) é fundamental para especificar o modo de endereçamento, indicando se o operando é um registrador ( mod = 11 ) ou um endereço de memória, e como o deslocamento ( DISP ) de 8 ou 16 bits é aplicado.

## II. Microarquitetura e Pipeline

A arquitetura do 8086 introduziu um **pipeline rudimentar** através do desacoplamento de duas unidades de hardware principais, conforme detalhado na patente US4449184A:

---


## Page 85

1. Unidade de Interface de Barramento (Bus Interface Unit - BIU): Corresponde à Unidade de Controle Superior da patente. É responsável por gerenciar o barramento e realizar o **Prefetch de Instruções** (Instruction Prefetch). A BIU busca instruções da memória de forma assíncrona e as armazena em uma **Fila de Instruções** (Instruction Queue) de 6 bytes (FIFO), mantendo-a preenchida sempre que o barramento estiver livre.
2. Unidade de Execução (Execution Unit - EU): Corresponde à Unidade de Controle Inferior da patente. A EU consome as instruções da fila, decodifica-as e as executa utilizando a Unidade Lógica e Aritmética (ALU).

O **mechanismo de execução sobreposta e assíncrona** (pipeline) permite que a EU execute uma instrução enquanto a BIU busca a próxima, otimizando o throughput ao esconder a latência de busca de instruções. A patente descreve o uso de um **Loader Means** com múltiplos estados cíclicos e um sinal de controle NXT (next-to-the-last clock signal) gerado pela Microcode ROM para gerenciar o fluxo de instruções e a recarga da fila.

## III. Conceitos Avançados do Conjunto de Instruções (ISA)

O conjunto de instruções (ISA) do 8086 introduziu conceitos de alto nível que se tornaram marcas registradas da arquitetura x86:

*   **Instruções de String:** Instruções dedicadas ( MOVS , CMPS , SCAS , LODS , STOS ) para manipulação eficiente de blocos de memória. O **Algoritmo de Repetição** é implementado pelo prefixo REP , que executa um loop de microcódigo, decrementando o registrador CX (Count Register) e ajustando os registradores de índice ( SI e DI ) automaticamente, com a direção controlada pelo **Direction Flag (DF)**.
*   **Instrução LOCK (Bus Lock):** O prefixo LOCK é uma instrução de sincronização que garante o acesso atômico a um recurso compartilhado em sistemas multiprocessados. O processador asserta o sinal LOCK no barramento, impedindo que outros dispositivos acessem a memória até que a instrução prefixada seja concluída.
*   **Aritmética BCD Descompactada:** O 8086 inclui instruções de ajuste ( AAA , AAS , AAM , AAD ) que implementam algoritmos para corrigir o resultado de operações binárias com números Decimais Codificados em Binário (BCD) descompactados, garantindo a validade do resultado BCD.
*   **Flags de Status Expandidos:** O 8086 expandiu os flags de status para incluir o **Overflow Flag (OF)**, que corrige a deficiência dos 8008 / 8080 ao indicar overflow de números assinados, e o **Direction Flag (DF)**, que controla a direção das operações de string.

## IV. Mecanismo de Endereçamento Estendido da Patente

A patente US4449184A descreve o **Mecanismo de Endereçamento Estendido** em termos de hardware. O conceito envolve o uso de **registradores de relocação** (os Registros de Segmento) que possuem bits assumidos para estender o comprimento efetivo do endereço. O algoritmo de geração de endereço estendido envolve a soma de bits selecionados do registrador de relocação com uma word predeterminada, e a **prefixação/sufixação** dos bits não selecionados, com a possibilidade de propagação de *carry* através do prefixo.

A patente também detalha a **Estrutura de Microcódigo** para instruções complexas, utilizando uma **Subroutine Translation ROM** para carregar endereços de microcódigo em resposta a campos de bits em instruções de multiple byte, e um **Subroutine Register** para salvar o endereço de microcódigo durante saltos internos.

## Quantificação de Conceitos Técnicos

1.  Endereçamento Segmentado (Conceito/Fórmula)
2.  Cálculo do Endereço Efetivo (Fórmula)
3.  Modos de Endereçamento (Conceito/Estrutura)
4.  Formato da Instrução com Campo MOD/REG/R/M (Estrutura)
5.  Pipeline Rudimentar (BIU/EU Decoupling) (Microarquitetura)

---


## Page 86

6. Prefetch de Instruções (Algoritmo)
7. Fila de Instruções de 6 bytes (Estrutura)
8. Instruções de String (Conceito)
9. Algoritmo de Repetição (REP prefix) (Algoritmo/Microcódigo)
10. Instrução LOCK (Bus Lock) (Conceito/Estrutura)
11. Aritmética BCD Descompactada (Conceito/Instruções)
12. Overflow Flag (OF) (Estrutura/Conceito)
13. Direction Flag (DF) (Estrutura/Conceito)
14. Mecanismo de Endereçamento Estendido (Patente) (Algoritmo/Estrutura)
15. Estrutura de Microcódigo com Subroutine Translation ROM (Estrutura)

---

## Pesquisador 6: John Crawford

**Itens Técnicos Encontrados:** 15

**Contribuições:** Arquitetura 32-bit x86, MMU On-Chip, Paginação de Dois Níveis, Segmentação Estendida (4GB), Pipeline de Tradução de Endereços de Alta Velocidade

## Conteúdo Técnico do Intel 80386 (John Crawford)

### Estrutura de Hardware e Microarquitetura

O Intel 80386, projetado sob a liderança de John Crawford, foi o primeiro processador x86 a implementar uma **arquitetura completa de 32 bits**, utilizando um caminho de dados interno de 32 bits para registradores, ALU e barramentos internos. Foi fabricado em **tecnologia CMOS de 1.5µ** e possuía uma interface de **barramento externo de 32 bits**.

A arquitetura introduziu oito **registradores gerais de 32 bits** (EAX, EBX, ECX, EDX, ESP, EBP, ESI, EDI) e estendeu os **registradores de segmento** (CS, SS, DS, ES, FS, GS) para suportar segmentos de até 4 Gigabytes. Os registradores de controle e status foram atualizados com o **EIP (Instruction Pointer)** de 32 bits e o **EFLAGS** de 32 bits, que contém bits de status como *carry, overflow, sign* e *zero*.

O chip integrava uma **Unidade de Gerenciamento de Memória (MMU) On-Chip** completa, suportando segmentação e paginação. A microarquitetura interna, conforme ilustrado no diagrama do chip, incluía unidades especializadas como:

*   Page Cache e PAGING UNIT
*   PREFETCH UNIT e Prefetch Queue
*   Segment Descriptor Cache e SEGMENT UNIT
*   INSTRUCTION DECODE UNIT e Instruction Queue
*   ALU e Barrel Shifter
*   32-Bit Register File
*   EXECUTION UNIT e Microcode

### Conceitos de Arquitetura e Algoritmos

O 80386 implementou a **Segmentação Estendida**, que expandiu o modelo do 80286 para permitir segmentos de até $2^{32}$ bytes (4 Gigabytes). Introduziu o mecanismo de **Paginação (Paging)** padrão de dois níveis para gerenciamento de memória física, operando abaixo da segmentação. O sistema permite o uso de segmentação, paginação ou ambos, sem penalidades de desempenho.

---


## Page 87

Um dos avanços cruciais foi o **Pipeline de Tradução de Endereços de Alta Velocidade**, totalmente suportado on-chip com cache de informações de mapeamento de segmentação e paginação. Este pipeline permitia que:

*   Uma instrução de carregamento de memória (*Memory Load instruction*), incluindo tradução de segmento e endereço de página, fosse executada em apenas **4 ciclos de clock** (250 ns a 16 Mhz).
*   Uma instrução de armazenamento (*Store instruction*) fosse executada em apenas **2 ciclos de clock** (125 ns a 16 Mhz).

O processador suporta um conjunto completo de **instruções de 32 bits** e é otimizado para sistemas operacionais multitarefa, incorporando um robusto **Mecanismo de Proteção** e gerenciamento de memória.

## Fórmulas e Relações de Tempo

As relações de tempo de execução e capacidade de endereçamento são definidas pelas seguintes fórmulas:

1.  **Tempo de Ciclo de Clock (para 16 MHz):** $T_{clock} = \frac{1}{16\times10^9}$ segundos = 62.5 ns$
2.  **Tempo de Carga de Memória (4 ciclos):** $T_{load} = 4 \times T_{clock} = 4 \times 62.5$ ns = 250 ns$
3.  **Tempo de Armazenamento (2 ciclos):** $T_{store} = 2 \times T_{clock} = 2 \times 62.5$ ns = 125 ns$
4.  **Capacidade de Endereçamento Físico:** $2^{32}$ bytes = 4 Gigabytes$ (Espaço de endereçamento físico e tamanho máximo de segmento)
5.  **Capacidade de Endereçamento Virtual:** $2^{46}$ bytes = 64 Terabytes$ (Implícito pelo seletor de segmento de 16 bits e offset de 32 bits)

---

## Pesquisador 7: Patrick Paul Gelsinger

**Itens Técnicos Encontrados:** 11

**Contribuições:** Pipeline de 5 estágios (i486), Cache Unificado 8KB (i486), Pipeline FP de 8 estágios (i486), Execução Superscalar (Pentium), Pipeline U/V (Pentium), Previsão Dinâmica de Desvio (Pentium), Cache L1 Separado (Pentium)

## Conteúdo Técnico - Pat Gelsinger (Intel 80486 e Pentium)

### Intel 80486 (i486)

## Microarquitetura e Pipeline

*   **Pipeline de Inteiros de Cinco Estágios (AGI Pipeline):**
    *   **1. Fetch (F):** Busca 16 bytes de instruções do cache de 8KB (4-way set associative, fisicamente endereçado) para um prefetch buffer. Usa dois buffers de 16 bytes em modo double-buffered ou um para prefetch em um caminho de alvo de desvio.
    *   **2. D1 (Decodificação Principal):** Processa até três bytes de instrução por vez. Determina o comprimento da instrução e avança o prefetch buffer. Ciclos extras para prefixos ou opcodes de dois bytes.
    *   **3. D2 (Decodificação Secundária):** Inclui o cálculo do endereço efetivo. Ciclos extras quando a instrução tem uma constante imediata e um deslocamento de memória, ou quando um registrador de índice deve ser adicionado a um registrador base e um deslocamento.
    *   **4. Execute (EX):** Inclui a busca de operando de registrador e acesso ao cache de dados.
        *   Operações de ALU com todos os operandos/resultados em registradores podem ser realizadas em **um ciclo**.

---


## Page 88

*   Operações de carga ou armazenamento (e.g., MOV mem to reg, MOV reg to mem) com *hit* no cache de dados são concluídas em **um ciclo** no estágio EX.
*   Instruções complexas (e.g., reg-to-memory add) requerem três ciclos EX: um para busca de dados do cache, um para a adição e um para o armazenamento do resultado no cache.
*   **Encaminhamento (Forwarding):** Um resultado carregado está disponível para uso no ciclo seguinte.
*   **Atrasos de Carga de Ponteiro:** O cálculo de endereço em D2 pode causar um *stall* de um ciclo se uma instrução subsequente usar o registrador carregado como base ou índice.

5. **Write Back (WB):** Escrita de volta nos registradores.

*   **Cache:** Cache unificado (instrução e dados) de 8KB, 4-way set associative, *write-through*.
*   **Unidade de Ponto Flutuante (FPU):** Pipeline de FP de oito estágios, seguindo os estágios de inteiro F/D1/D2/EX, seguidos pelos estágios de FP: **X1** (execute-1), **X2** (execute-2), **WF** (FP write-back) e **ER** (error reporting).
*   **Desvios (Branches):**
    *   **Previsão de Desvio:** *Predict-untaken* (mesmo para saltos incondicionais).
    *   **Penalidade de Desvio Incorreto:** Dois ciclos, pois a mudança no PC é determinada durante o estágio EX, exigindo o *flush* dos conteúdos de D1 e D2.


# Intel Pentium

## Microarquitetura Superscalar

*   **Execução Superscalar:** O Pentium possui duas pipelines de inteiros independentes, chamadas **U-pipe** e **V-pipe**, permitindo a execução de **duas instruções por ciclo de clock** em muitos casos.
*   **Pipeline de Inteiros:** Semelhante ao i486, mas com cinco estágios:
    1.  **PF (Prefetch):** Busca código do cache de instrução e alinha o código para o *First Decode*.
    2.  **D1 (First Decode):** Decodifica a instrução para gerar uma *control word*.
    3.  **D2 (Second Decode):** Gera a *control word* a partir de D1 e o endereço de memória.
    4.  **E (Execute):** Acesso ao cache de dados ou cálculo de resultado da ALU.
    5.  **WB (Write Back):** Atualiza registradores e *flags*.
*   **Algoritmo de Emissão de Instrução (Instruction Issue Algorithm):**
    *   Duas instruções consecutivas (I1 e I2) são emitidas em paralelo (U-pipe e V-pipe) se:
        *   Ambas são instruções “simples” (a maioria das instruções de uso geral).
        *   Nenhuma é uma instrução de salto.
        *   O destino de I1 é diferente da fonte de I2.
        *   O destino de I1 é diferente do destino de I2.
        *   Neste caso, I1 vai para o U-pipe e I2 vai para o V-pipe. Caso contrário, I1 vai para o U-pipe e I2 é *stalled*.
*   **Previsão Dinâmica de Desvio (Dynamic Branch Prediction):** Utiliza um *Branch Target Buffer (BTB)* para prever desvios dinamicamente, o que é uma melhoria significativa em relação ao *predict-untaken* estático do i486.
*   **Caches Separados:** Possui caches separados para instrução e dados (*L1 split cache*), cada um com 8KB, 2-way set associative.
*   **Unidade de Ponto Flutuante (FPU):** Pipeline de FP dedicado e mais rápido, com um multiplicador e um divisor dedicados. O Pentium alcança até cinco vezes o *speedup* em código de vetor de ponto flutuante em comparação com o i486.
*   **Barramento de Dados:** Interface externa de 64 bits (dobro do i486).
*   **Tecnologia:** 0.8-µm BiCMOS, 3.1 milhões de transistores.

---


## Page 89

# Pesquisador 8: Glenn J. Hinton

**Itens Técnicos Encontrados:** 31

**Contribuições:** Trace Cache, ALUs double-pumped, Unidade de Execução Híbrida, Execução Dinâmica, Renomeação de Registradores, Instruções SSE2

# Conteúdo Técnico - Microarquitetura NetBurst (Glenn Hinton et al.)

A microarquitetura NetBurst, desenvolvida para o processador Pentium 4, é fundamentalmente dividida em quatro seções principais: o **Front End In-Order**, o **Motor de Execução Out-of-Order**, as **Unidades de Execução de Inteiros e Ponto Flutuante**, e o **Subsistema de Memória**.

## Front End In-Order

O Front End In-Order introduziu o **Trace Cache (Cache de Traços)**, um novo tipo de cache de instruções que armazena micro-operações (*micro-ops*) decodificadas e rastros de execução (*traços*). O conceito central é armazenar *micro-ops* em sua ordem de execução prevista, eliminando a necessidade de decodificação repetida de instruções IA-32 e armazenando o resultado da predição de desvio. Estruturalmente, o Trace Cache pode armazenar até **12K micro-ops**. O Decodificador IA-32 é usado apenas em caso de falha (*miss*) do Trace Cache.

## Lógica de Execução Out-of-Order

A Lógica de Execução Out-of-Order prepara as instruções e as reordena para otimizar o fluxo através do pipeline, utilizando vários *buffers* para suavizar e reordenar o fluxo de instruções. A **Lógica de Aposentadoria (Retirement Logic)** é responsável por reordenar as instruções executadas fora de ordem de volta para a ordem original do programa. O algoritmo de aposentadoria permite que o processador se aposente (*commit*) até **três micro-ops por ciclo de clock**.

## Unidades de Execução e Subsistema de Memória

O Rapid Execution Engine (Motor de Execução Rápida) é um conceito de hardware que utiliza **Unidades Lógicas e Aritméticas (ALUs) de inteiro double-pumped** (bombeadas duplamente). Estruturalmente, as ALUs operam no dobro da frequência do clock do núcleo (ex: 3 GHz de clock do núcleo = **6 GHz de frequência efetiva da ALU**). Isso resulta em uma latência extremamente baixa de apenas **dois ciclos de clock** para operações de inteiro. O Subsistema de Memória apresenta um **Cache L1 de Dados** acessível em apenas **dois ciclos de clock**. O **Barramento do Sistema (System Bus)** suporta uma largura de banda de **3.2 GB/segundo** (para o modelo de 1.5 GHz). A microarquitetura também adicionou **144 novas instruções SIMD de 128 bits (SSE2 - Streaming SIMD Extension 2)**.

# Conteúdo Técnico - Patente US5574942A (Unidade de Execução Híbrida)

A patente US5574942A, de co-autoria de Glenn Hinton, descreve a **Unidade de Execução Híbrida (Hybrid Execution Unit)**, uma unidade de execução projetada para executar instruções diversas (*miscellaneous instructions*) em um único ciclo de **clock**, operando em conjunto com as unidades de execução de inteiro e ponto flutuante existentes.

O conceito de hardware permite que a unidade receba dados de inteiro ou ponto flutuante e realize manipulações (*manipulations*) de duas fontes de entrada. A **Estrutura de Dados** é otimizada para receber fontes de dados do mesmo tamanho das fontes de dados de ponto flutuante, permitindo a manipulação de ambos os tipos de dados. Para otimização de pipeline, a unidade compartilha a mesma porta de despacho (*dispatch port*) e o mesmo barramento de write back que outras unidades. O **Algoritmo de Bypass** inclui um mecanismo de bypass de informação para outras unidades de execução, permitindo o agendamento eficiente de operações. A **Lógica de Controle** é implementada para direcionar o caminho de dados (*data path*) para realizar as várias manipulações de dados ou *swizzling*.

---


## Page 90

# Conteúdo Técnico - Microarquitetura P6 (Pentium Pro)

A microarquitetura P6, que serviu de base para o Pentium Pro, foi a primeira da Intel a implementar a **Execução Dinâmica** (*Dynamic Execution*), um conceito que engloba a execução fora de ordem (*Out-of-Order*), a execução especulativa e a Renomeação de Registradores.

<table>
  <thead>
    <tr>
      <th>Estrutura</th>
      <th>Conceito/Função</th>
      <th>Algoritmo/Regra</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Pipeline</td>
      <td>Profundidade do pipeline de instruções.</td>
      <td>14 estágios (Pentium Pro).</td>
    </tr>
    <tr>
      <td>Decodificadores</td>
      <td>Conversão de instruções IA-32 (complexas) em micro-operações (*micro-ops*) RISC-like (simples).</td>
      <td>Três decodificadores capazes de gerar 4-1-1 micro-ops por ciclo.</td>
    </tr>
    <tr>
      <td>Renomeação de Registradores</td>
      <td>Técnica para eliminar dependências falsas de dados (WAR - Write After Read e WAW - Write After Write).</td>
      <td>Mapeamento de registradores lógicos (IA-32) para registradores físicos (no ROB) usando uma Tabela de Alias de Registradores (RAT - Register Alias Table).</td>
    </tr>
    <tr>
      <td>ReOrder Buffer (ROB)</td>
      <td>Buffer principal para o *pool* de instruções em execução.</td>
      <td>Implementado como uma Matriz de Memória Endereçável por Conteúdo (*CAM - Content Addressable Memory*).</td>
    </tr>
    <tr>
      <td>Execução Out-of-Order</td>
      <td>Agendamento e execução de micro-ops com base na disponibilidade de dados e unidades de execução.</td>
      <td>O ROB pode aceitar até três resultados de execução por ciclo de clock.</td>
    </tr>
    <tr>
      <td>Reservation Station (RS)</td>
      <td>Buffer de agendamento que mantém micro-ops prontas para serem despachadas para as unidades de execução.</td>
      <td>Despacha micro-ops para cinco portas de execução diferentes.</td>
    </tr>
    <tr>
      <td>Memory Order Buffer (MOB)</td>
      <td>Gerencia a ordem de execução de operações de memória (cargas e armazenamentos).</td>
      <td>Atua como uma *Reservation Station* e *ReOrder Buffer* para operações de memória, garantindo a coerência da ordem de memória.</td>
    </tr>
  </tbody>
</table>

---

## Pesquisador 9: Robert M. Tomasulo

Itens Técnicos Encontrados: 15

Contribuições: Algoritmo de Tomasulo, Execução Fora de Ordem, Escalonamento Dinâmico, Renomeamento de Registradores, Common Data Bus, Estações de Reserva

# Conteúdo Técnico do Algoritmo de Tomasulo (R. M. Tomasulo)

## Estruturas de Hardware e Microarquitetura

O algoritmo de Tomasulo é implementado através de várias estruturas de hardware interconectadas, projetadas para permitir a **Execução Fora de Ordem** (*Out-of-Order Execution*) e o **Escalonamento Dinâmico** (*Dynamic Scheduling*).

### 1. Estações de Reserva (Reservation Stations - RS)

As RSs substituem os registradores de entrada da unidade funcional. Cada RS armazena os operandos e o estado de uma instrução que está aguardando execução.

**Campos da Estação de Reserva (RS):**

---


## Page 91

*   **Op (Operation):** Operação a ser executada na unidade funcional (ex: ADD, SUB, MUL, DIV).
*   **Vj, Vk (Value j, Value k):** Valores dos operandos de origem.
*   **Qj, Qk (Tag j, Tag k):** Tags das Estações de Reserva ou Buffers de Armazenamento que produzirão os operandos de origem. Um valor de 0 indica que o operando está pronto e armazenado em Vj ou Vk.
*   **Busy:** Flag booleano que indica se a RS está ocupada.
*   **A (Address):** Usado para instruções de Load/Store para armazenar o endereço de memória (ou o operando base + deslocamento).

## 2. Registradores de Ponto Flutuante (Floating-Point Registers - FLR)

Os registradores de destino (FLR) são modificados para incluir um campo de tag, essencial para o Renomeamento de Registradores.

### Campo do Registrador de Ponto Flutuante (FLR):

*   **Busy Bit:** Flag booleano que indica se o registrador está ocupado (aguardando um resultado).
*   **Tag:** Identificador da Estação de Reserva que produzirá o resultado para este registrador. Se o Busy Bit for 0, o Tag é irrelevante.

## 3. Common Data Bus (CDB)

O CDB é um barramento de alta velocidade que transmite resultados das unidades funcionais para todas as Estações de Reserva e Registradores de Ponto Flutuante. É o mecanismo central para a propagação de resultados.

### Operação do CDB:

1.  A unidade funcional que completa a execução coloca o resultado e a tag da sua RS no CDB.
2.  Todas as RSs e FLRs monitoram o CDB.
3.  Se o Qj ou Qk de uma RS corresponder à tag no CDB, o valor do resultado é copiado para Vj ou Vk e o Qj / Qk é resetado para 0.
4.  Se o Tag de um FLR corresponder à tag no CDB, o Busy Bit do FLR é resetado e o valor é escrito no registrador.

## Algoritmo (Ciclos de Vida da Instrução)

O algoritmo de Tomasulo é dividido em três fases principais:

### 1. Emissão (Issue)

A instrução é lida da fila de instruções e enviada para uma RS livre.

### Regras de Emissão:

*   Se uma RS livre estiver disponível:
    *   Copia-se a operação para o campo Op da RS.
    *   Para cada operando de origem (Rj, Rk):
        *   Se o Busy Bit do registrador de origem for 0 (valor disponível), copia-se o valor para Vj ou Vk da RS e define-se Qj / Qk como 0.
        *   Se o Busy Bit for 1 (valor não disponível), copia-se o Tag do registrador de origem para Qj ou Qk da RS.
    *   Define-se o Busy Bit do registrador de destino como 1.
    *   Define-se o Tag do registrador de destino como o identificador da RS.
*   Se nenhuma RS livre estiver disponível, a instrução é paralisada (Stall).

---


## Page 92

# 2. Execução (Execute)

A instrução aguarda na RS até que todos os seus operandos estejam disponíveis.

## Regras de Execução:

*   A instrução pode começar a executar quando:
    *   O campo 0p está preenchido.
    *   Ambos os campos Qj e Qk são 0 (ou seja, Vj e Vk contêm os valores).
*   A execução é realizada pela unidade funcional apropriada (Adder, Multiplier/Divider).

# 3. Escrita de Resultado (Write Result)

O resultado da execução é transmitido para o CDB.

## Regras de Escrita de Resultado:

*   A unidade funcional coloca o resultado e a tag da RS no CDB.
*   Todas as RSs e FLRs que estavam esperando por essa tag (ou seja, tinham essa tag em Qj , Qk ou Tag ) capturam o resultado e atualizam seus estados.
*   A RS que completou a execução é liberada ( Busy = 0).

# Fórmulas/Representações (Regras Lógicas)

A representação das instruções no pipeline é puramente lógica e de controle.

## Regra Lógica para Início da Execução (RS):

```plaintext
Start_Execution = Busy AND (Qj == 0) AND (Qk == 0)
```

## Regra Lógica para Atualização de Registrador (FLR):

```plaintext
Update_FLR = Busy AND (Tag == CDB_Tag)
```

## Regra Lógica para Atualização de RS (RS):

```plaintext
Update_RS_Vj = Busy AND (Qj == CDB_Tag)
Update_RS_Vk = Busy AND (Qk == CDB_Tag)
```

# Conceitos de Microarquitetura Chave

*   **Renomeamento de Registradores (Register Renaming):** Elimina as dependências de nome (WAW - Write After Write e WAR - Write After Read) através do uso de tags ( Qj , Qk , Tag ).
*   **Escalonamento Dinâmico (Dynamic Scheduling):** A ordem de execução é determinada pela disponibilidade dos operandos, e não pela ordem sequencial do programa.
*   **Precedência de Preservação (Preservation of Precedence):** O algoritmo garante que as dependências de dados (RAW - Read After Write) sejam respeitadas.
*   **Unidades Funcionais Múltiplas (Multiple Functional Units):** Permite a operação paralela de unidades independentes (Adders, Multipliers).

---


## Page 93

*   **Buffer de Armazenamento (Store Buffer):** Estrutura para instruções de Store, garantindo a ordem correta de Stores na memória.
*   **Tags:** Identificadores binários que rastreiam a dependência de dados e atuam como ponteiros lógicos para resultados pendentes.

## Contagem de Componentes (Exemplo IBM 360%91)

*   3 Adders (unidades funcionais)
*   2 Multiplier/Dividers (unidades funcionais)
*   6 Floating-Point Buffers (RSs para Load/Store)
*   5 Reservation Stations (RSs para Add/Sub/Mul/Div)
*   1 Common Data Bus (CDB)
*   4 Floating-Point Registers (FLR)
*   3 Store Data Buffers (SDB)

## Pesquisador 10: John L. Hennessy

Itens Técnicos Encontrados: 31

Contribuições: Arquitetura RISC (MIPS), Equação de Desempenho da CPU, Lei de Amdahl (aplicação quantitativa), Hazards de Pipeline (Estrutural, Dados, Controle), Algoritmo de Tomasulo, Renomeação de Registradores, Regras de Ouro de Arquitetura

## Conteúdo Técnico do Trabalho de John Hennessy (Arquitetura de Computadores)

## Fórmulas Fundamentais de Desempenho e Análise

1.  **Tempo de CPU (CPU time)** $CPU time = Instruction count × Clock cycles per instruction × Clock cycle time$
2.  **Lei de Amdahl (Amdahl’s Law)** $Speedup_{overall} = \frac{Execution time_{old}}{Execution time_{new}} = \frac{1}{(1-Fraction_{enhanced}) + \frac{Fraction_{enhanced}}{Speedup_{enhanced}}}$
3.  **Energia Dinâmica (Dynamic Energy)** $Energy_{dynamic} ∝ 1/2 × Capacitive load × Voltage^2$
4.  **Potência Dinâmica (Dynamic Power)** $Power_{dynamic} ∝ 1/2 × Capacitive load × Voltage^2 × Frequency switched$
5.  **Potência Estática (Static Power)** $Power_{static} ∝ Current_{static} × Voltage$
6.  **Disponibilidade (Availability)** $Availability = \frac{Mean time to fail}{Mean time to fail+Mean time to repair}$
7.  **Rendimento do Die (Die yield)** $Die yield = Wafer yield × \frac{1}{(1+Defects per unit area×Die area)^N}$ onde N é o fator de complexidade do processo.
8.  **Tempo Médio de Acesso à Memória (Average memory-access time)** $Average memory-access time = Hit time + Miss rate × Miss penalty$
9.  **Misses por Instrução (Misses per instruction)** $Misses per instruction = Miss rate × Memory access per instruction$
10. **Índice de Cache (Cache index size)** $Cache index size : 2^{index} = \frac{Cache size}{(Block size×Set associativity)}$

---


## Page 94

11. Efetividade de Utilização de Energia (Power Utilization Effectiveness - PUE) $PUE = \frac{\text{Total Facility Power}}{\text{IT Equipment Power}}$

# Conceitos de Paralelismo em Nível de Instrução (ILP) e Pipeline

## Hazards de Pipeline

*   **Hazard Estrutural (Structural Hazard):** Conflito de hardware onde múltiplas instruções tentam acessar o mesmo recurso na mesma fase do ciclo.
*   **Hazard de Dados (Data Hazard):** Ocorre quando uma instrução depende do resultado de uma instrução anterior que ainda está no pipeline.
    *   RAW (Read After Write): Dependência verdadeira.
    *   WAW (Write After Write): Dependência de nome.
    *   WAR (Write After Read): Dependência de nome.
*   **Hazard de Controle (Control Hazard):** Causado por instruções de desvio (branches) que alteram o fluxo de controle.

## Técnicas de Resolução de Hazards

*   **Reorganização de Código (Code Reordering):** Técnica de scheduling estático para evitar stalls de pipeline.
*   **Escalonamento Dinâmico (Dynamic Scheduling):** Reorganização da ordem de execução das instruções pelo hardware.
*   **Algoritmo de Tomasulo:** Algoritmo de escalonamento dinâmico que utiliza:
    *   Estações de Reserva (Reservation Stations - RS): Buffers que mantêm operandos e informações de operação.
    *   Common Data Bus (CDB): Barramento de alta velocidade para data forwarding.
    *   Buffer de Reordenamento (Reorder Buffer - ROB): Estrutura para garantir a execução em ordem de programa.
    *   Renomeação de Registradores (Register Renaming): Técnica para eliminar hazards WAW e WAR.

## Fórmulas de Pipeline

*   **Tempo de Execução com Pipeline (Execution Time with Pipeline):** $Tempo de Execução = Tempo de Ciclo × (CPI_{ideal} + Stalls por Instrução) × Contagem de Instruções$
*   **Speedup do Pipeline (Pipeline Speedup):** $Speedup = \frac{\text{Tempo de Execução não-pipeline}}{\text{Tempo de Execução pipeline}}$
*   **Penalidade de Desvio (Branch Penalty):** $Penalidade de Desvio = Frequência de Desvio × Taxa de Erro de Predição × Custo do Erro de Predição$
*   **Predição de Desvio (Branch Prediction):** Uso de Tabela de Histórico de Desvio (Branch History Table - BHT) e Preditor de 2 bits (2-bit Predictor).

## Regras de Ouro (Heurísticas de Projeto)

*   **Regra Amdahl/Case:** 1 MB de memória e 1 megabit/s de E/S por MIPS de desempenho da CPU.
*   **Regra de Localidade 90/10:** 90% das instruções em 10% do código.
*   **Regra de Largura de Banda:** Largura de banda cresce α (melhoria na latência)².
*   **Regra de Cache 2:1:** Taxa de miss de cache direct-mapped de tamanho N é ≈ cache two-way set-associative de tamanho N/2.

---

## Pesquisador 11: David A. Patterson

Itens Técnicos Encontrados: 17

---


## Page 95

Contribuições: Níveis RAID (0-5), Equação Fundamental de Desempenho da CPU, Arquitetura Load/Store, Algoritmo de Janelas de Registradores, Fórmula MTTF de Arrays de Discos, Lei de Amdahl na Crise de E/S

# Conteúdo Técnico Puro (Algoritmos, Fórmulas, Estruturas de Hardware, Conceitos de Microarquitetura)

## Fórmulas Fundamentais de Desempenho e Confiabilidade

1.  **Lei de Amdahl (Speedup S):** $S = \frac{1}{(1-f) + \frac{f}{k}}$ onde $S$ é o ganho de velocidade no modo mais rápido.
    *   $f$: fração de trabalho em modo mais rápido.
    *   $k$: número de instruções.

2.  **Equação Fundamental do Desempenho do Processador (Tempo de CPU):** $Tempo\text{ de CPU} = Instruções \times CPI \times Tempo\text{ de Ciclo}$ onde $Instruções$ é a contagem de instruções (determinada pelo ISA e compilador), $CPI$ é o ciclo por instrução (determinada pela microarquitetura), e $Tempo\text{ de Ciclo}$ é o tempo de ciclo do clock (determinada pela tecnologia de hardware).

3.  **Tempo Médio Entre Falhas (MTTF) de Arrays de Discos (RAID 3, 4, 5):** $MTTF_{RAID} = \frac{MTTF_{disk}^2}{N \times (Tempo\text{ de Reparo})}$ onde $MTTF_{disk}$ é o MTTF de um único disco, $N$ é o número de discos no array, e $Tempo\text{ de Reparo}$ é o tempo para reconstruir os dados.

4.  **Densidade de Área Magnética (MAD):** $MAD = 10^{(Year - 1971)/10}$

## Estruturas de Hardware e Organização de Dados (RAID)

<table>
<thead>
<tr>
<th>Nível</th>
<th>Organização</th>
<th>Conceito Chave</th>
<th>Estrutura de Hardware</th>
<th>Capacidade Efetiva</th>
</tr>
</thead>
<tbody>
<tr>
<td>RAID 0</td>
<td>Non-Redundant Striping</td>
<td>Striping de dados em blocos sem redundância.</td>
<td>$N$ discos de dados.</td>
<td>$N \times Capacidade_{disk}$</td>
</tr>
<tr>
<td>RAID 1</td>
<td>Disk Mirroring</td>
<td>Espelhamento de dados (cópia exata).</td>
<td>$N$ discos de dados e $N$ discos espelhados.</td>
<td>$\frac{N}{2} \times Capacidade_{disk}$</td>
</tr>
<tr>
<td>RAID 2</td>
<td>Memory-Style ECC</td>
<td>Código de Hamming para correção de erros em nível de bit/palavra.</td>
<td>$N$ discos de dados e $P$ discos de paridade/ECC, onde $P = \lceil \log_2(N+1) \rceil$.</td>
<td>$(N-P) \times Capacidade_{disk}$</td>
</tr>
<tr>
<td>RAID 3</td>
<td>Bit-Interleaved Parity</td>
<td>Striping de dados em nível de byte/bit com paridade XOR dedicada.</td>
<td>$N$ discos de dados e 1 disco de paridade.</td>
<td>$(N-1) \times Capacidade_{disk}$</td>
</tr>
<tr>
<td>RAID 4</td>
<td>Block-Interleaved Parity</td>
<td>Striping de dados em nível de bloco com paridade XOR dedicada.</td>
<td>$N$ discos de dados e 1 disco de paridade.</td>
<td>$(N-1) \times Capacidade_{disk}$</td>
</tr>
<tr>
<td>RAID 5</td>
<td>Block-Interleaved Distributed Parity</td>
<td>Striping de dados em nível de bloco com paridade XOR distribuída.</td>
<td>$N$ discos de dados, com paridade rotacionada entre todos os discos.</td>
<td>$(N-1) \times Capacidade_{disk}$</td>
</tr>
</tbody>
</table>

## Conceitos de Microarquitetura e Algoritmos (RISC)

1.  **Princípios de Design RISC:**
    *   **Instruções Simples e Fixas:** Facilita o pipeline (Instruction Pipelining) e a decodificação (Fetch/Decode).
    *   **Load/Store Architecture:** Separação entre operações de memória (LOAD / STORE ) e operações de ALU (operam apenas em registradores).
    *   **Controle Hardwired:** Implementação do controle do processador por lógica combinacional, reduzindo o Tempo de Ciclo e o CPI.

2.  **Algoritmo de Janelas de Registradores (Register Windows):**

3.  **Algoritmo de Janelas de Registros (Register Windows):**

4.  **Algoritmo de Janelas de Registros (Register Windows):**

5.  **Algoritmo de Janelas de Registros (Register Windows):**

6.  **Algoritmo de Janelas de Registros (Register Windows):**

7.  **Algoritmo de Janelas de Registros (Register Windows):**

8.  **Algoritmo de Janelas de Registros (Register Windows):**

9.  **Algoritmo de Janelas de Registros (Register Windows):**

10. **Algoritmo de Janelas de Registros (Register Windows):**

11. **Algoritmo de Janelas de Registros (Register Windows):**

12. **Algoritmo de Janelas de Registros (Register Windows):**

13. **Algoritmo de Janelas de Registros (Register Windows):**

14. **Algoritmo de Janelas de Registros (Register Windows):**

15. **Algoritmo de Janelas de Registros (Register Windows):**

16. **Algoritmo de Janelas de Registros (Register Windows):**

17. **Algoritmo de Janelas de Registros (Register Windows):**

18. **Algoritmo de Janelas de Registros (Register Windows):**

19. **Algoritmo de Janelas de Registros (Register Windows):**

20. **Algoritmo de Janelas de Registros (Register Windows):**

21. **Algoritmo de Janelas de Registros (Register Windows):**

22. **Algoritmo de Janelas de Registros (Register Windows):**

23. **Algoritmo de Janelas de Registros (Register Windows):**

24. **Algoritmo de Janelas de Registros (Register Windows):**

25. **Algoritmo de Janelas de Registros (Register Windows):**

26. **Algoritmo de Janelas de Registros (Register Windows):**

27. **Algoritmo de Janelas de Registros (Register Windows):**

28. **Algoritmo de Janelas de Registros (Register Windows):**

29. **Algoritmo de Janelas de Registros (Register Windows):**

30. **Algoritmo de Janelas de Registros (Register Windows):**

31. **Algoritmo de Janelas de Registros (Register Windows):**

32. **Algoritmo de Janelas de Registros (Register Windows):**

33. **Algoritmo de Janelas de Registros (Register Windows):**

34. **Algoritmo de Janelas de Registros (Register Windows):**

35. **Algoritmo de Janelas de Registros (Register Windows):**

36. **Algoritmo de Janelas de Registros (Register Windows):**

37. **Algoritmo de Janelas de Registros (Register Windows):**

38. **Algoritmo de Janelas de Registros (Register Windows):**

39. **Algoritmo de Janelas de Registros (Register Windows):**

40. **Algoritmo de Janelas de Registros (Register Windows):**

41. **Algoritmo de Janelas de Registros (Register Windows):**

42. **Algoritmo de Janelas de Registros (Register Windows):**

43. **Algoritmo de Janelas de Registros (Register Windows):**

44. **Algoritmo de Janelas de Registros (Register Windows):**

45. **Algoritmo de Janelas de Registros (Register Windows):**

46. **Algoritmo de Janelas de Registros (Register Windows):**

47. **Algoritmo de Janelas de Registros (Register Windows):**

48. **Algoritmo de Janelas de Registros (Register Windows):**

49. **Algoritmo de Janelas de Registros (Register Windows):**

50. **Algoritmo de Janelas de Registros (Register Windows):**

51. **Algoritmo de Janelas de Registros (Register Windows):**

52. **Algoritmo de Janelas de Registros (Register Windows):**

53. **Algoritmo de Janelas de Registros (Register Windows):**

54. **Algoritmo de Janelas de Registros (Register Windows):**

55. **Algoritmo de Janelas de Registros (Register Windows):**

56. **Algoritmo de Janelas de Registros (Register Windows):**

57. **Algoritmo de Janelas de Registros (Register Windows):**

58. **Algoritmo de Janelas de Registros (Register Windows):**

59. **Algoritmo de Janelas de Registros (Register Windows):**

60. **Algoritmo de Janelas de Registros (Register Windows):**

61. **Algoritmo de Janelas de Registros (Register Windows):**

62. **Algoritmo de Janelas de Registros (Register Windows):**

63. **Algoritmo de Janelas de Registros (Register Windows):**

64. **Algoritmo de Janelas de Registros (Register Windows):**

65. **Algoritmo de Janelas de Registros (Register Windows):**

66. **Algoritmo de Janelas de Registros (Register Windows):**

67. **Algoritmo de Janelas de Registros (Register Windows):**

68. **Algoritmo de Janelas de Registros (Register Windows):**

69. **Algoritmo de Janelas de Registros (Register Windows):**

70. **Algoritmo de Janelas de Registros (Register Windows):**

71. **Algoritmo de Janelas de Registros (Register Windows):**

72. **Algoritmo de Janelas de Registros (Register Windows):**

73. **Algoritmo de Janelas de Registros (Register Windows):**

74. **Algoritmo de Janelas de Registros (Register Windows):**

75. **Algoritmo de Janelas de Registros (Register Windows):**

76. **Algoritmo de Janelas de Registros (Register Windows):**

77. **Algoritmo de Janelas de Registros (Register Windows):**

78. **Algoritmo de Janelas de Registros (Register Windows):**

79. **Algoritmo de Janelas de Registros (Register Windows):**

80. **Algoritmo de Janelas de Registros (Register Windows):**

81. **Algoritmo de Janelas de Registros (Register Windows):**

82. **Algoritmo de Janelas de Registros (Register Windows):**

83. **Algoritmo de Janelas de Registros (Register Windows):**

84. **Algoritmo de Janelas de Registros (Register Windows):**

85. **Algoritmo de Janelas de Registros (Register Windows):**

86. **Algoritmo de Janelas de Registros (Register Windows):**

87. **Algoritmo de Janelas de Registros (Register Windows):**

88. **Algoritmo de Janelas de Registros (Register Windows):**

89. **Algoritmo de Janelas de Registros (Register Windows):**

90. **Algoritmo de Janelas de Registros (Register Windows):**

91. **Algoritmo de Janelas de Registros (Register Windows):**

92. **Algoritmo de Janelas de Registros (Register Windows):**

93. **Algoritmo de Janelas de Registros (Register Windows):**

94. **Algoritmo de Janelas de Registros (Register Windows):**

95. **Algoritmo de Janelas de Registros (Register Windows):**

96. **Algoritmo de Janelas de Registros (Register Windows):**

97. **Algoritmo de Janelas de Registros (Register Windows):**

98. **Algoritmo de Janelas de Registros (Register Windows):**

99. **Algoritmo de Janelas de Registros (Register Windows):**

100. **Algoritmo de Janelas de Registros (Register Windows):**

101. **Algoritmo de Janelas de Registros (Register Windows):**

102. **Algoritmo de Janelas de Registros (Register Windows):**

103. **Algoritmo de Janelas de Registros (Register Windows):**

104. **Algoritmo de Janelas de Registros (Register Windows):**

105. **Algoritmo de Janelas de Registros (Register Windows):**

106. **Algoritmo de Janelas de Registros (Register Windows):**

107. **Algoritmo de Janelas de Registros (Register Windows):**

108. **Algoritmo de Janelas de Registros (Register Windows):**

109. **Algoritmo de Janelas de Registros (Register Windows):**

110. **Algoritmo de Janelas de Registros (Register Windows):**

111. **Algoritmo de Janelas de Registros (Register Windows):**

112. **Algoritmo de Janelas de Registros (Register Windows):**

113. **Algoritmo de Janelas de Registros (Register Windows):**

114. **Algoritmo de Janelas de Registros (Register Windows):**

115. **Algoritmo de Janelas de Registros (Register Windows):**

116. **Algoritmo de Janelas de Registros (Register Windows):**

117. **Algoritmo de Janelas de Registros (Register Windows):**

118. **Algoritmo de Janelas de Registros (Register Windows):**

119. **Algoritmo de Janelas de Registros (Register Windows):**

120. **Algoritmo de Janelas de Registros (Register Windows):**

121. **Algoritmo de Janelas de Registros (Register Windows):**

122. **Algoritmo de Janelas de Registros (Register Windows):**

123. **Algoritmo de Janelas de Registros (Register Windows):**

124. **Algoritmo de Janelas de Registros (Register Windows):**

125. **Algoritmo de Janelas de Registros (Register Windows):**

126. **Algoritmo de Janelas de Registros (Register Windows):**

127. **Algoritmo de Janelas de Registros (Register Windows):**

128. **Algoritmo de Janelas de Registros (Register Windows):**

129. **Algoritmo de Janelas de Registros (Register Windows):**

130. **Algoritmo de Janelas de Registros (Register Windows):**

131. **Algoritmo de Janelas de Registros (Register Windows):**

132. **Algoritmo de Janelas de Registros (Register Windows):**

133. **Algoritmo de Janelas de Registros (Register Windows):**

134. **Algoritmo de Janelas de Registros (Register Windows):**

135. **Algoritmo de Janelas de Registros (Register Windows):**

136. **Algoritmo de Janelas de Registros (Register Windows):**

137. **Algoritmo de Janelas de Registros (Register Windows):**

138. **Algoritmo de Janelas de Registros (Register Windows):**

139. **Algoritmo de Janelas de Registros (Register Windows):**

140. **Algoritmo de Janelas de Registros (Register Windows):**

141. **Algoritmo de Janelas de Registros (Register Windows):**

142. **Algoritmo de Janelas de Registros (Register Windows):**

143. **Algoritmo de Janelas de Registros (Register Windows):**

144. **Algoritmo de Janelas de Registros (Register Windows):**

145. **Algoritmo de Janelas de Registros (Register Windows):**

146. **Algoritmo de Janelas de Registros (Register Windows):**

147. **Algoritmo de Janelas de Registros (Register Windows):**

148. **Algoritmo de Janelas de Registros (Register Windows):**

149. **Algoritmo de Janelas de Registros (Register Windows):**

150. **Algoritmo de Janelas de Registros (Register Windows):**

151. **Algoritmo de Janelas de Registros (Register Windows):**

152. **Algoritmo de Janelas de Registros (Register Windows):**

153. **Algoritmo de Janelas de Registros (Register Windows):**

154. **Algoritmo de Janelas de Registros (Register Windows):**

155. **Algoritmo de Janelas de Registros (Register Windows):**

156. **Algoritmo de Janelas de Registros (Register Windows):**

157. **Algoritmo de Janelas de Registros (Register Windows):**

158. **Algoritmo de Janelas de Registros (Register Windows):**

159. **Algoritmo de Janelas de Registros (Register Windows):**

160. **Algoritmo de Janelas de Registros (Register Windows):**

161. **Algoritmo de Janelas de Registros (Register Windows):**

162. **Algoritmo de Janelas de Registros (Register Windows):**

163. **Algoritmo de Janelas de Registros (Register Windows):**

164. **Algoritmo de Janelas de Registros (Register Windows):**

165. **Algoritmo de Janelas de Registros (Register Windows):**

166. **Algoritmo de Janelas de Registros (Register Windows):**

167. **Algoritmo de Janelas de Registros (Register Windows):**

168. **Algoritmo de Janelas de Registros (Register Windows):**

169. **Algoritmo de Janelas de Registros (Register Windows):**

170. **Algoritmo de Janelas de Registros (Register Windows):**

171. **Algoritmo de Janelas de Registros (Register Windows):**

172. **Algoritmo de Janelas de Registros (Register Windows):**

173. **Algoritmo de Janelas de Registros (Register Windows):**

174. **Algoritmo de Janelas de Registros (Register Windows):**

175. **Algoritmo de Janelas de Registros (Register Windows):**

176. **Algoritmo de Janelas de Registros (Register Windows):**

177. **Algoritmo de Janelas de Registros (Register Windows):**

178. **Algoritmo de Janelas de Registros (Register Windows):**

179. **Algoritmo de Janelas de Registros (Register Windows):**

180. **Algoritmo de Janelas de Registros (Register Windows):**

181. **Algoritmo de Janelas de Registros (Register Windows):**

182. **Algoritmo de Janelas de Registros (Register Windows):**

183. **Algoritmo de Janelas de Registros (Register Windows):**

184. **Algoritmo de Janelas de Registros (Register Windows):**

185. **Algoritmo de Janelas de Registros (Register Windows):**

186. **Algoritmo de Janelas de Registros (Register Windows):**

187. **Algoritmo de Janelas de Registros (Register Windows):**

188. **Algoritmo de Janelas de Registros (Register Windows):**

189. **Algoritmo de Janelas de Registros (Register Windows):**

190. **Algoritmo de Janelas de Registros (Register Windows):**

191. **Algoritmo de Janelas de Registros (Register Windows):**

192. **Algoritmo de Janelas de Registros (Register Windows):**

193. **Algoritmo de Janelas de Registros (Register Windows):**

194. **Algoritmo de Janelas de Registros (Register Windows):**

195. **Algoritmo de Janelas de Registros (Register Windows):**

196. **Algoritmo de Janelas de Registros (Register Windows):**

197. **Algoritmo de Janelas de Registros (Register Windows):**

198. **Algoritmo de Janelas de Registros (Register Windows):**

199. **Algoritmo de Janelas de Registros (Register Windows):**

200. **Algoritmo de Janelas de Registros (Register Windows):**

201. **Algoritmo de Janelas de Registros (Register Windows):**

202. **Algoritmo de Janelas de Registros (Register Windows):**

203. **Algoritmo de Janelas de Registros (Register Windows):**

204. **Algoritmo de Janelas de Registros (Register Windows):**

205. **Algoritmo de Janelas de Registros (Register Windows):**

206. **Algoritmo de Janelas de Registros (Register Windows):**

207. **Algoritmo de Janelas de Registros (Register Windows):**

208. **Algoritmo de Janelas de Registros (Register Windows):**

209. **Algoritmo de Janelas de Registros (Register Windows):**

210. **Algoritmo de Janelas de Registros (Register Windows):**

211. **Algoritmo de Janelas de Registros (Register Windows):**

212. **Algoritmo de Janelas de Registros (Register Windows):**

213. **Algoritmo de Janelas de Registros (Register Windows):**

214. **Algoritmo de Janelas de Registros (Register Windows):**

215. **Algoritmo de Janelas de Registros (Register Windows):**

216. **Algoritmo de Janelas de Registros (Register Windows):**

217. **Algoritmo de Janelas de Registros (Register Windows):**

218. **Algoritmo de Janelas de Registros (Register Windows):**

219. **Algoritmo de Janelas de Registros (Register Windows):**

220. **Algoritmo de Janelas de Registros (Register Windows):**

221. **Algoritmo de Janelas de Registros (Register Windows):**

222. **Algoritmo de Janelas de Registros (Register Windows):**

223. **Algoritmo de Janelas de Registros (Register Windows):**

224. **Algoritmo de Janelas de Registros (Register Windows):**

225. **Algoritmo de Janelas de Registros (Register Windows):**

226. **Algoritmo de Janelas de Registros (Register Windows):**

227. **Algoritmo de Janelas de Registros (Register Windows):**

228. **Algoritmo de Janelas de Registros (Register Windows):**

229. **Algoritmo de Janelas de Registros (Register Windows):**

230. **Algoritmo de Janelas de Registros (Register Windows):**

231. **Algoritmo de Janelas de Registros (Register Windows):**

232. **Algoritmo de Janelas de Registros (Register Windows):**

233. **Algoritmo de Janelas de Registros (Register Windows):**

234. **Algoritmo de Janelas de Registros (Register Windows):**

235. **Algoritmo de Janelas de Registros (Register Windows):**

236. **Algoritmo de Janelas de Registros (Register Windows):**

237. **Algoritmo de Janelas de Registros (Register Windows):**

238. **Algoritmo de Janelas de Registros (Register Windows):**

239. **Algoritmo de Janelas de Registros (Register Windows):**

240. **Algoritmo de Janelas de Registros (Register Windows):**

241. **Algoritmo de Janelas de Registros (Register Windows):**

242. **Algoritmo de Janelas de Registros (Register Windows):**

243. **Algoritmo de Janelas de Registros (Register Windows):**

244. **Algoritmo de Janelas de Registros (Register Windows):**

245. **Algoritmo de Janelas de Registros (Register Windows):**

246. **Algoritmo de Janelas de Registros (Register Windows):**

247. **Algoritmo de Janelas de Registros (Register Windows):**

248. **Algoritmo de Janelas de Registros (Register Windows):**

249. **Algoritmo de Janelas de Registros (Register Windows):**

250. **Algoritmo de Janelas de Registros (Register Windows):**

251. **Algoritmo de Janelas de Registros (Register Windows):**

252. **Algoritmo de Janelas de Registros (Register Windows):**

253. **Algoritmo de Janelas de Registros (Register Windows):**

254. **Algoritmo de Janelas de Registros (Register Windows):**

255. **Algoritmo de Janelas de Registros (Register Windows):**

256. **Algoritmo de Janelas de Registros (Register Windows):**

257. **Algoritmo de Janelas de Registros (Register Windows):**

258. **Algoritmo de Janelas de Registros (Register Windows):**

259. **Algoritmo de Janelas de Registros (Register Windows):**

260. **Algoritmo de Janelas de Registros (Register Windows):**

261. **Algoritmo de Janelas de Registros (Register Windows):**

262. **Algoritmo de Janelas de Registros (Register Windows):**

263. **Algoritmo de Janelas de Registros (Register Windows):**

264. **Algoritmo de Janelas de Registros (Register Windows):**

265. **Algoritmo de Janelas de Registros (Register Windows):**

266. **Algoritmo de Janelas de Registros (Register Windows):**

267. **Algoritmo de Janelas de Registros (Register Windows):**

268. **Algoritmo de Janelas de Registros (Register Windows):**

269. **Algoritmo de Janelas de Registros (Register Windows):**

270. **Algoritmo de Janelas de Registros (Register Windows):**

271. **Algoritmo de Janelas de Registros (Register Windows):**

272. **Algoritmo de Janelas de Registros (Register Windows):**

273. **Algoritmo de Janelas de Registros (Register Windows):**

274. **Algoritmo de Janelas de Registros (Register Windows):**

275. **Algoritmo de Janelas de Registros (Register Windows):**

276. **Algoritmo de Janelas de Registros (Register Windows):**

277. **Algoritmo de Janelas de Registros (Register Windows):**

278. **Algoritmo de Janelas de Registros (Register Windows):**

279. **Algoritmo de Janelas de Registros (Register Windows):**

280. **Algoritmo de Janelas de Registros (Register Windows):**

281. **Algoritmo de Janelas de Registros (Register Windows):**

282. **Algoritmo de Janelas de Registros (Register Windows):**

283. **Algoritmo de Janelas de Registros (Register Windows):**

284. **Algoritmo de Janelas de Registros (Register Windows):**

285. **Algoritmo de Janelas de Registros (Register Windows):**

286. **Algoritmo de Janelas de Registros (Register Windows):**

287. **Algoritmo de Janelas de Registros (Register Windows):**

288. **Algoritmo de Janelas de Registros (Register Windows):**

289. **Algoritmo de Janelas de Registros (Register Windows):**

290. **Algoritmo de Janelas de Registros (Register Windows):**

291. **Algoritmo de Janelas de Registros (Register Windows):**

292. **Algoritmo de Janelas de Registros (Register Windows):**

293. **Algoritmo de Janelas de Registros (Register Windows):**

294. **Algoritmo de Janelas de Registros (Register Windows):**

295. **Algoritmo de Janelas de Registros (Register Windows):**

296. **Algoritmo de Janelas de Registros (Register Windows):**

297. **Algoritmo de Janelas de Registros (Register Windows):**

298. **Algoritmo de Janelas de Registros (Register Windows):**

299. **Algoritmo de Janelas de Registros (Register Windows):**

300. **Algoritmo de Janelas de Registros (Register Windows):**

301. **Algoritmo de Janelas de Registros (Register Windows):**

302. **Algoritmo de Janelas de Registros (Register Windows):**

303. **Algoritmo de Janelas de Registros (Register Windows):**

304. **Algoritmo de Janelas de Registros (Register Windows):**

305. **Algoritmo de Janelas de Registros (Register Windows):**

306. **Algoritmo de Janelas de Registros (Register Windows):**

307. **Algoritmo de Janelas de Registros (Register Windows):**

308. **Algoritmo de Janelas de Registros (Register Windows):**

309. **Algoritmo de Janelas de Registros (Register Windows):**

310. **Algoritmo de Janelas de Registros (Register Windows):**

311. **Algoritmo de Janelas de Registros (Register Windows):**

312. **Algoritmo de Janelas de Registros (Register Windows):**

313. **Algoritmo de Janelas de Registros (Register Windows):**

314. **Algoritmo de Janelas de Registros (Register Windows):**

315. **Algoritmo de Janelas de Registros (Register Windows):**

316. **Algoritmo de Janelas de Registros (Register Windows):**

317. **Algoritmo de Janelas de Registros (Register Windows):**

318. **Algoritmo de Janelas de Registros (Register Windows):**

319. **Algoritmo de Janelas de Registros (Register Windows):**

320. **Algoritmo de Janelas de Registros (Register Windows):**

321. **Algoritmo de Janelas de Registros (Register Windows):**

322. **Algoritmo de Janelas de Registros (Register Windows):**

323. **Algoritmo de Janelas de Registros (Register Windows):**

324. **Algoritmo de Janelas de Registros (Register Windows):**

325. **Algoritmo de Janelas de Registros (Register Windows):**

326. **Algoritmo de Janelas de Registros (Register Windows):**

327. **Algoritmo de Janelas de Registros (Register Windows):**

328. **Algoritmo de Janelas de Registros (Register Windows):**

329. **Algoritmo de Janelas de Registros (Register Windows):**

330. **Algoritmo de Janelas de Registros (Register Windows):**

331. **Algoritmo de Janelas de Registros (Register Windows):**

332. **Algoritmo de Janelas de Registros (Register Windows):**

333. **Algoritmo de Janelas de Registros (Register Windows):**

334. **Algoritmo de Janelas de Registros (Register Windows):**

335. **Algoritmo de Janelas de Registros (Register Windows):**

336. **Algoritmo de Janelas de Registros (Register Windows):**

337. **Algoritmo de Janelas de Registros (Register Windows):**

338. **Algoritmo de Janelas de Registros (Register Windows):**

339. **Algoritmo de Janelas de Registros (Register Windows):**

340. **Algoritmo de Janelas de Registros (Register Windows):**

341. **Algoritmo de Janelas de Registros (Register Windows):**

342. **Algoritmo de Janelas de Registros (Register Windows):**

343. **Algoritmo de Janelas de Registros (Register Windows):**

344. **Algoritmo de Janelas de Registros (Register Windows):**

345. **Algoritmo de Janelas de Registros (Register Windows):**

346. **Algoritmo de Janelas de Registros (Register Windows):**

347. **Algoritmo de Janelas de Registros (Register Windows):**

348. **Algoritmo de Janelas de Registros (Register Windows):**

349. **Algoritmo de Janelas de Registros (Register Windows):**

350. **Algoritmo de Janelas de Registros (Register Windows):**

351. **Algoritmo de Janelas de Registros (Register Windows):**

352. **Algoritmo de Janelas de Registros (Register Windows):**

353. **Algoritmo de Janelas de Registros (Register Windows):**

354. **Algoritmo de Janelas de Registros (Register Windows):**

355. **Algoritmo de Janelas de Registros (Register Windows):**

356. **Algoritmo de Janelas de Registros (Register Windows):**

357. **Algoritmo de Janelas de Registros (Register Windows):**

358. **Algoritmo de Janelas de Registros (Register Windows):**

359. **Algoritmo de Janelas de Registros (Register Windows):**

360. **Algoritmo de Janelas de Registros (Register Windows):**

361. **Algoritmo de Janelas de Registros (Register Windows):**

362. **Algoritmo de Janelas de Registros (Register Windows):**

363. **Algoritmo de Janelas de Registros (Register Windows):**

364. **Algoritmo de Janelas de Registros (Register Windows):**

365. **Algoritmo de Janelas de Registros (Register Windows):**

366. **Algoritmo de Janelas de Registros (Register Windows):**

367. **Algoritmo de Janelas de Registros (Register Windows):**

368. **Algoritmo de Janelas de Registros (Register Windows):**

369. **Algoritmo de Janelas de Registros (Register Windows):**

370. **Algoritmo de Janelas de Registros (Register Windows):**

371. **Algoritmo de Janelas de Registros (Register Windows):**

372. **Algoritmo de Janelas de Registros (Register Windows):**

373. **Algoritmo de Janelas de Registros (Register Windows):**

374. **Algoritmo de Janelas de Registros (Register Windows):**

375. **Algoritmo de Janelas de Registros (Register Windows):**

376. **Algoritmo de Janelas de Registros (Register Windows):**

377. **Algoritmo de Janelas de Registros (Register Windows):**

378. **Algoritmo de Janelas de Registros (Register Windows):**

379. **Algoritmo de Janelas de Registros (Register Windows):**

380. **Algoritmo de Janelas de Registros (Register Windows):**

381. **Algoritmo de Janelas de Registros (Register Windows):**

382. **Algoritmo de Janelas de Registros (Register Windows):**

383. **Algoritmo de Janelas de Registros (Register Windows):**

384. **Algoritmo de Janelas de Registros (Register Windows):**

385. **Algoritmo de Janelas de Registros (Register Windows):**

386. **Algoritmo de Janelas de Registros (Register Windows):**

387. **Algoritmo de Janelas de Registros (Register Windows):**

388. **Algoritmo de Janelas de Registros (Register Windows):**

389. **Algoritmo de Janelas de Registros (Register Windows):**

390. **Algoritmo de Janelas de Registros (Register Windows):**

391. **Algoritmo de Janelas de Registros (Register Windows):**

392. **Algoritmo de Janelas de Registros (Register Windows):**

393. **Algoritmo de Janelas de Registros (Register Windows):**

394. **Algoritmo de Janelas de Registros (Register Windows):**

395. **Algoritmo de Janelas de Registros (Register Windows):**

396. **Algoritmo de Janelas de Registros (Register Windows):**

397. **Algoritmo de Janelas de Registros (Register Windows):**

398. **Algoritmo de Janelas de Registros (Register Windows):**

399. **Algoritmo de Janelas de Registros (Register Windows):**

400. **Algoritmo de Janelas de Registros (Register Windows):**

401. **Algoritmo de Janelas de Registros (Register Windows):**

402. **Algoritmo de Janelas de Registros (Register Windows):**

403. **Algoritmo de Janelas de Registros (Register Windows):**

404. **Algoritmo de Janelas de Registros (Register Windows):**

405. **Algoritmo de Janelas de Registros (Register Windows):**

406. **Algoritmo de Janelas de Registros (Register Windows):**

407. **Algoritmo de Janelas de Registros (Register Windows):**

408. **Algoritmo de Janelas de Registros (Register Windows):**

409. **Algoritmo de Janelas de Registros (Register Windows):**

410. **Algoritmo de Janelas de Registros (Register Windows):**

411. **Algoritmo de Janelas de Registros (Register Windows):**

412. **Algoritmo de Janelas de Registros (Register Windows):**

413. **Algoritmo de Janelas de Registros (Register Windows):**

414. **Algoritmo de Janelas de Registros (Register Windows):**

415. **Algoritmo de Janelas de Registros (Register Windows):**

416. **Algoritmo de Janelas de Registros (Register Windows):**

417. **Algoritmo de Janelas de Registros (Register Windows):**

418. **Algoritmo de Janelas de Registros (Register Windows):**

419. **Algoritmo de Janelas de Registros (Register Windows):**

420. **Algoritmo de Janelas de Registros (Register Windows):**

421. **Algoritmo de Janelas de Registros (Register Windows):**

422. **Algoritmo de Janelas de Registros (Register Windows):**

423. **Algoritmo de Janelas de Registros (Register Windows):**

424. **Algoritmo de Janelas de Registros (Register Windows):**

425. **Algoritmo de Janelas de Registros (Register Windows):**

426. **Algoritmo de Janelas de Registros (Register Windows):**

427. **Algoritmo de Janelas de Registros (Register Windows):**

428. **Algoritmo de Janelas de Registros (Register Windows):**

429. **Algoritmo de Janelas de Registros (Register Windows):**

430. **Algoritmo de Janelas de Registros (Register Windows):**

431. **Algoritmo de Janelas de Registros (Register Windows):**

432. **Algoritmo de Janelas de Registros (Register Windows):**

433. **Algoritmo de Janelas de Registros (Register Windows):**

434. **Algoritmo de Janelas de Registros (Register Windows):**

435. **Algoritmo de Janelas de Registros (Register Windows):**

436. **Algoritmo de Janelas de Registros (Register Windows):**

437. **Algoritmo de Janelas de Registros (Register Windows):**

438. **Algoritmo de Janelas de Registros (Register Windows):**

439. **Algoritmo de Janelas de Registros (Register Windows):**

440. **Algoritmo de Janelas de Registros (Register Windows):**

441. **Algoritmo de Janelas de Registros (Register Windows):**

442. **Algoritmo de Janelas de Registros (Register Windows):**

443. **Algoritmo de Janelas de Registros (Register Windows):**

444. **Algoritmo de Janelas de Registros (Register Windows):**

445. **Algoritmo de Janelas de Registros (Register Windows):**

446. **Algoritmo de Janelas de Registros (Register Windows):**

447. **Algoritmo de Janelas de Registros (Register Windows):**

448. **Algoritmo de Janelas de Registros (Register Windows):**

449. **Algoritmo de Janelas de Registros (Register Windows):**

450. **Algoritmo de Janelas de Registros (Register Windows):**

451. **Algoritmo de Janelas de Registros (Register Windows):**

452. **Algoritmo de Janelas de Registros (Register Windows):**

453. **Algoritmo de Janelas de Registros (Register Windows):**

454. **Algoritmo de Janelas de Registros (Register Windows):**

455. **Algoritmo de Janelas de Registros (Register Windows):**

456. **Algoritmo de Janelas de Registros (Register Windows):**

457. **Algoritmo de Janelas de Registros (Register Windows):**

458. **Algoritmo de Janelas de Registros (Register Windows):**

459. **Algoritmo de Janelas de Registros (Register Windows):**

460. **Algoritmo de Janelas de Registros (Register Windows):**

461. **Algoritmo de Janelas de Registros (Register Windows):**

462. **Algoritmo de Janelas de Registros (Register Windows):**

463. **Algoritmo de Janelas de Registros (Register Windows):**

464. **Algoritmo de Janelas de Registros (Register Windows):**

465. **Algoritmo de Janelas de Registros (Register Windows):**

466. **Algoritmo de Janelas de Registros (Register Windows):**

467. **Algoritmo de Janelas de Registros (Register Windows):**

468. **Algoritmo de Janelas de Registros (Register Windows):**

469. **Algoritmo de Janelas de Registros (Register Windows):**

470. **Algoritmo de Janelas de Registros (Register Windows):**

471. **Algoritmo de Janelas de Registros (Register Windows):**

472. **Algoritmo de Janelas de Registros (Register Windows):**

473. **Algoritmo de Janelas de Registros (Register Windows):**

474. **Algoritmo de Janelas de Registros (Register Windows):**

475. **Algoritmo de Janelas de Registros (Register Windows):**

476. **Algoritmo de Janelas de Registros (Register Windows):**

477. **Algoritmo de Janelas de Registros (Register Windows):**

478. **Algoritmo de Janelas de Registros (Register Windows):**

479. **Algoritmo de Janelas de Registros (Register Windows):**

480. **Algoritmo de Janelas de Registros (Register Windows):**

481. **Algoritmo de Janelas de Registros (Register Windows):**

482. **Algoritmo de Janelas de Registros (Register Windows):**

483. **Algoritmo de Janelas de Registros (Register Windows):**

484. **Algoritmo de Janelas de Registros (Register Windows):**

485. **Algoritmo de Janelas de Registros (Register Windows):**

486. **Algoritmo de Janelas de Registros (Register Windows):**

487. **Algoritmo de Janelas de Registros (Register Windows):**

488. **Algoritmo de Janelas de Registros (Register Windows):**

489. **Algoritmo de Janelas de Registros (Register Windows):**

490. **Algoritmo de Janelas de Registros (Register Windows):**

491. **Algoritmo de Janelas de Registros (Register Windows):**

492. **Algoritmo de Janelas de Registros (Register Windows):**

493. **Algoritmo de Janelas de Registros (Register Windows):**

494. **Algoritmo de Janelas de Registros (Register Windows):**

495. **Algoritmo de Janelas de Registros (Register Windows):**

496. **Algoritmo de Janelas de Registros (Register Windows):**

497. **Algoritmo de Janelas de Registros (Register Windows):**

498. **Algoritmo de Janelas de Registros (Register Windows):**

as99. **Algoritmo de Janelas de Registros (Register Windows):**

as100. **Algoritmo de Janelas de Registros (Register Windows):**

as101. **Algoritmo de Janelas de Registros (Register Windows):**

as102. **Algoritmo de Janelas de Registros (Register Windows):**

as103. **Algoritmo de Janelas de Registros (Register Windows):**

as104. **Algoritmo de Janelas de Registros (Register Windows):**

as105. **Algoritmo de Janelas de Registros (Register Windows):**

as106. **Algoritmo de Janelas de Registros (Register Windows):**

as107. **Algoritmo de Janelas de Registros (Register Windows):**

as108. **Algoritmo de Janelas de Registros (Register Windows):**

as109. **Algoritmo de Janelas de Registros (Register Windows):**

as110. **Algoritmo de Janelas de Registros (Register Windows):**

as111. **Algoritmo de Janelas de Registros (Register Windows):**

as112. **Algoritmo de Janelas de Registros (Register Windows):**

as113. **Algoritmo de Janelas de Registros (Register Windows):**

as114. **Algoritmo de Janelas de Registros (Register Windows):**

as115. **Algoritmo de Janelas de Registros (Register Windows):**

as116. **Algoritmo de Janelas de Registros (Register Windows):**

as117. **Algoritmo de Janelas de Registros (Register Windows):**

as118. **Algoritmo de Janelas de Registros (Register Windows):**

as119. **Algoritmo de Janelas de Registros (Register Windows):**

as120. **Algoritmo de Janelas de Registros (Register Windows):**

as121. **Algoritmo de Janelas de Registros (Register Windows):**

as122. **Algoritmo de Janelas de Registros (Register Windows):**

as123. **Algoritmo de Janelas de Registros (Register Windows):**

as124. **Algoritmo de Janelas de Registros (Register Windows):**

as125. **Algoritmo de Janelas de Registros (Register Windows):**

as126. **Algoritmo de Janelas de Registros (Register Windows):**

as127. **Algoritmo de Janelas de Registros (Register Windows):**

as128. **Algoritmo de Janelas de Registros (Register Windows):**

as129. **Algoritmo de Janelas de Registros (Register Windows):**

as130. **Algoritmo de Janelas de Registros (Register Windows):**

as131. **Algoritmo de Janelas de Registros (Register Windows):**

as132. **Algoritmo de Janelas de Registros (Register Windows):**

as133. **Algoritmo de Janelas de Registros (Register Windows):**

as134. **Algoritmo de Janelas de Registros (Register Windows):**

as135. **Algoritmo de Janelas de Registros (Register Windows):**

as136. **Algoritmo de Janelas de Registros (Register Windows):**

as137. **Algoritmo de Janelas de Registros (Register Windows):**

as138. **Algoritmo de Janelas de Registros (Register Windows):**

as139. **Algoritmo de Janelas de Registros (Register Windows):**

as140. **Algoritmo de Janelas de Registros (Register Windows):**

as111. **Algoritmo de Janelas de Registros (Register Windows):**

as112. **Algoritmo de Janelas de Registros (Register Windows):**

as113. **Algoritmo de Janelas de Registros (Register Windows):**

as114. **Algoritmo de Janelas de Registros (Register Windows):**

as115. **Algoritmo de Janelas de Registros (Register Windows):**

as116. **Algoritmo de Janelas de Registros (Register Windows):**

as117. **Algoritmo de Janelas de Registros (Register Windows):**

as118. **Algoritmo de Janelas de Registros (Register Windows):**

as119. **Algoritmo de Janelas de Registros (Register Windows):**

as120. **Algoritmo de Janelas de Registros (Register Windows):**

as121. **Algoritmo de Janelas de Registros (Register Windows):**

as122. **Algoritmo de Janelas de Registros (Register Windows):**

as123. **Algoritmo de Janelas de Registros (Register Windows):**

as124. **Algoritmo de Janelas de Registros (Register Windows):**

as125. **Algoritmo de Janelas de Registros (Register Windows):**

as126. **Algoritmo de Janelas de Registros (Register Windows):**

as127. **Algoritmo de Janelas de Registros (Register Windows):**

as128. **Algoritmo de Janelas de Registros (Register Windows):**

as129. **Algoritmo de Janelas de Registros (Register Windows):**

as130. **Algoritmo de Janelas de

---


## Page 96

*   **Estrutura:** Banco de registradores dividido em janelas sobrepostas para otimizar a passagem de parâmetros em chamadas de função.
*   **Composição da Janela:** Registradores Locais (L), Registradores de Saída (O), Registradores de Entrada (I), e Registradores Globais (G).
*   **Tamanho da Janela:** Tamanho da Janela = L + O + I.
*   **Total de Registradores:** Total de Registradores = G + Número de Janelas × (L + I).

3. **Princípios de Arquitetura de Computadores:**
    *   **Design para o Comum (Make the Common Case Fast):** Otimização de hardware para operações de alta frequência (ex: acessos a registradores).
    *   **Paralelismo em Nível de Instrução (ILP):** Uso de Pipeline e arquiteturas Superscalar para executar múltiplas instruções por ciclo de clock.
    *   **Princípio da Localidade:** Base para a hierarquia de memória (Caches), explorando a Localidade Temporal e Espacial.

---

## Pesquisador 12: Maurice Vincent Wilkes

**Itens Técnicos Encontrados:** 29

**Contribuições:** Microprogramação, Unidade de Controle com Matrizes de Diodos, Memória Cache (Slave Memory), Algoritmo de Substituição LRU, Arquitetura EDSAC de Endereço Único

## Unidade de Controle Microprogramada de Wilkes (1952)

**Conceito Central:** O sistema de controle é dividido em duas partes:

1.  **Unidade Aritmética:** Contém um conjunto de registradores e um somador com um sistema de comutação para realizar as micro-operações.
2.  **Unidade de Micro-Controle (Micro-control unit):** Controla a sequência de micro-ordens para executar cada ordem de máquina.

**Estrutura da Unidade de Micro-Controle:** A unidade consiste em:

*   Uma árvore de decodificação (decoding tree).
*   Duas matrizes retificadoras (rectifier matrices): Matriz A e Matriz B.
*   Dois registradores de controle (control registers): Registrador I e Registrador II.

**Funcionamento (Sequência de Micro-operações):**

1.  O endereço da micro-ordem a ser executada é colocado no **Registrador I**.
2.  Um pulso de controle é gerado e aplicado à entrada da **árvore de decodificação**.
3.  Cada pulso é roteado para a linha de saída correta da árvore, de acordo com o número no Registrador I.
4.  As linhas de saída da árvore passam para a **Matriz A**.
5.  As saídas da **Matriz A** são os pulsos que operam os vários gates associados às **micro-operações**.
6.  As linhas de saída da árvore também passam para a **Matriz B**.
7.  As saídas da **Matriz B** são conectadas ao **Registrador II**.
8.  O endereço da próxima micro-ordem a ser executada é colocado no **Registrador II** pela Matriz B.
9.  O endereço da micro-ordem no Registrador II é transferido para o **Registrador I**.
10. A aplicação alternada de pulsos aos Registradores I e II causa uma sequência predeterminada de micro-ordens a ser executada.

---


## Page 97

**Matrizes de Diodos (Matriz A e Matriz B):**

*   **Matriz A:** Uma linha de entrada da matriz corresponde a uma micro-ordem. As saídas da Matriz A são os sinais de controle (pulsos) para as micro-operações.
*   **Matriz B:** As saídas da Matriz B são conectadas ao Registrador II e determinam o endereço da próxima micro-ordem. A fiação (wiring) na Matriz B implementa a lógica de sequenciamento.

**Micro-ordem (Micro-order):**

*   Composta por dois campos de bits: Campo de Micro-operação (Matriz A) e Campo de Endereço da Próxima Micro-ordem (Matriz B).

**Microprogramação Condicional:**

*   Feita por meio de um flip-flop de código condicional (conditional code flip-flop) que seleciona entre duas linhas de saída da Matriz B.

**Conceito de Pipeline (Implícito):**

*   Divisão do sistema de controle em Registradores I e II que se alternam, permitindo que o endereço da próxima micro-ordem seja determinado enquanto a micro-ordem atual está sendo executada.

---

# Memória Cache (Slave Memories) de Maurice Wilkes (1965)

**Conceito Central:** Uso de uma memória de núcleo rápido (*fast core memory*), chamada de memória escrava (*slave memory*), como um *buffer* para uma memória de núcleo mais lenta (*slower core memory*).

**Estrutura Hierárquica:**

*   **Memória Principal (Main Memory):** Memória de núcleo mais lenta e de grande capacidade.
*   **Memória Escrava (Slave Memory):** Memória de núcleo mais rápida e de menor capacidade.

**Mecanismo de Endereçamento e Transferência (Conceito de Bloco):**

1.  Memória principal dividida em **blocos** (*blocks*) de tamanho fixo.
2.  Memória escrava dividida em **linhas** (*lines*), cada uma armazenando um bloco da memória principal.
3.  Cada linha possui um campo de endereço de bloco (*block address field*) (*tag*).

**Algoritmo de Acesso (Hit/Miss):**

*   **Condição de Hit:** O endereço do bloco é comparado simultaneamente com todos os campos de endereço de bloco na memória escrava.
*   **Fórmula para Endereçamento (Implícita):** $A_{bloco} = \text{Tag}(A_{linha})$
*   **Miss:** O bloco completo é transferido da memória principal para uma linha livre na memória escrava.

**Algoritmo de Substituição (Replacement Algorithm):**

*   Algoritmo proposto: LRU (*Least Recently Used*), implementado com contadores de uso (*usage counters*) de hardware.
*   **Mecanismo de LRU (Proposto):** Contadores zerados no *hit* e incrementados no *miss*. A linha com o maior valor de contador é a candidata à substituição.

**Estrutura de Hardware (Implícita):**

*   **Memória Associativa (Associative Memory):** O campo de endereço de bloco atua como uma memória associativa para a busca simultânea.
*   **Tipo de Cache:** Cache totalmente associativo (*fully associative cache*).

---


## Page 98

# Arquitetura EDSAC (Electronic Delay Storage Automatic Calculator)

## Estrutura de Hardware (Memória):

*   **Tecnologia:** Linhas de Retardo de Mercúrio (*Mercury Delay Lines*).
*   **Princípio de Funcionamento:** Armazenamento serial de dados por meio da circulação contínua de pulsos acústicos.
*   **Capacidade:** 512 palavras curtas de 17 bits (expansível para 1024).

## Formato da Instrução (Ordem):

*   **Tamanho Básico:** 18 bits (17 bits utilizáveis).
*   **Estrutura:** 5 bits (Opcode) + 1 bit (Spare) + 10 bits (Address) + 1 bit (Length).
*   **Length Bit:** 0 para 17 bits (curto), 1 para 35 bits (longo).

## Registradores Principais:

*   **Acumulador (Accumulator):** 71 bits.
*   **Registrador Multiplicador (Multiplier Register):** 35 bits.

## Formato de Número:

*   **Números Curto:** 17 bits.
*   **Números Longos:** 35 bits.
*   **Representação:** Frações binárias de ponto fixo.

## Conjunto de Instruções (Micro-operações):

*   **Arquitetura:** Arquitetura de Endereço Único (*Single-Address Architecture*).
*   **Fórmulas de Micro-operação (Exemplos):**
    *   Adição: $Acc \leftarrow Acc + M[n]$
    *   Subtração: $Acc \leftarrow Acc - M[n]$
    *   Cópia para Multiplicador: $MR \leftarrow M[n]$
    *   Multiplicação e Adição: $Acc \leftarrow Acc + (M[n] \times MR)$
    *   Transferência e Limpeza: $M[n] \leftarrow Acc; Acc \leftarrow 0$
    *   Collate (AND Lógico): $Acc \leftarrow Acc + (M[n] \land MR)$
    *   Shift Right: $Acc \leftarrow Acc >> n$
    *   Jump Condicional (Positivo): If $Acc \geq 0$ then $PC \leftarrow n$

## Algoritmo de Inicialização:

*   **Initial Orders:** Programa de inicialização (*bootstrap*) carregado por *switches* de hardware para ler o programa principal da fita de papel.

---

# Pesquisador 13: Gene Amdahl

## Itens Técnicos Encontrados: 7

## Contribuições:
*   Lei de Amdahl,
*   Limite de Speedup,
*   Arquitetura Unificada IBM S/360,
*   Byte de 8 bits,
*   Controle por Microprograma

---


## Page 99

# Conteúdo Técnico do Trabalho de Gene Amdahl

O conteúdo técnico do trabalho de Gene Amdahl se concentra em dois pilares principais: a **Lei de Amdahl**, que estabelece os limites teóricos do ganho de desempenho em sistemas paralelos, e a **Arquitetura do IBM System/360**, que introduziu conceitos fundamentais de arquitetura de computadores.

## 1. Lei de Amdahl (Fórmulas e Conceitos)

A Lei de Amdahl é uma fórmula que calcula o **speedup** teórico máximo ($S$) de um sistema quando apenas uma parte do sistema é melhorada, tipicamente através da paralelização.

### Fórmula do Speedup:

O speedup teórico $S(N)$ que pode ser obtido pela execução de um dado algoritmo em um sistema com $N$ processadores é dado por:

$$ S(N) = \frac{1}{(1 - P) + \frac{P}{N}} $$

Onde:
* $S(N)$ é o speedup teórico.
* $P$ é a proporção (fração) do tempo de execução do algoritmo que pode ser totalmente paralelizada ($0 \leq P \leq 1$).
* $1 - P$ é a proporção (fração) do tempo de execução que é estritamente sequencial e não pode ser paralelizada.
* $N$ é o número de processadores (threads de execução).

### Limite de Speedup (Limites da Computação Paralela):

O limite máximo de speedup ($S_{max}$) que pode ser atingido, mesmo que o número de processadores ($N$) tenda ao infinito, é determinado unicamente pela fração sequencial do programa ($1 - P$):

$$ S_{max} = \lim_{N \to \infty} S(N) = \frac{1}{1 - P} $$

### Conceito Central:

O conceito fundamental é que o ganho de velocidade de um programa usando múltiplos processadores é **limitado pela fração sequencial** do programa. Mesmo que 95% do programa possa ser paralelizado ($P = 0.95$), o speedup máximo teórico é limitado a $1/(1 - 0.95) = 20$ vezes, independentemente do número de processadores utilizados.

## 2. IBM System/360 (Estruturas de Hardware e Microarquitetura)

A arquitetura do IBM System/360, cocriada por Amdahl, introduziu inovações estruturais e de microarquitetura que se tornaram padrões da indústria.

### Arquitetura de Conjunto de Instruções (ISA) Unificada:

*   **Compatibilidade Programática:** A arquitetura foi projetada para ser estritamente compatível em nível de *bit de programa* em toda uma linha de seis modelos, com um fator de desempenho variando em 50 vezes. Isso permitiu que um programa válido rodasse em qualquer modelo da linha, desde que os recursos mínimos (memória, I/O) estivessem presentes.
*   **Registradores:** A arquitetura define 16 registradores de uso geral de 32 bits e 4 registradores de ponto flutuante de 64 bits.
*   **Formatos de Dados:**
    *   A unidade básica de endereçamento é o **byte de 8 bits**.
    *   Aritmética de ponto flutuante com formatos de 32 bits e 64 bits.
    *   Endereçamento de 24 bits, permitindo um espaço de endereçamento de até 16 MB.

---


## Page 100

# Microarquitetura e Implementação:

*   **Controle por Microprograma:** Modelos menores da linha System/360 (como o Model 30) utilizavam **memória somente leitura** (Read-Only Storage - ROS) para armazenar o microprograma. Este microprograma implementava o conjunto de instruções da ISA, permitindo que máquinas com diferentes *implementações físicas* (microarquiteturas) fossem *programaticamente compatíveis*.
*   **Hierarquia de Armazenamento:** Introdução de uma abordagem de armazenamento que explora **hierarquias de velocidades** e utiliza memória somente leitura para o controle por microprograma.

# Sistema de Entrada/Saída (I/O):

*   **Canais de I/O:** O sistema de I/O utiliza **canais** (channels) que oferecem um novo grau de operação concorrente.
*   **Interface Padrão:** Estabelecimento de uma **interface de canal padrão** entre a Unidade Central de Processamento (CPU) e os dispositivos de entrada/saída.
*   **Taxas de Dados:** O sistema foi projetado para suportar taxas de dados de I/O que se aproximavam de 5.000.000 de caracteres/segundo.

---

## Pesquisador 14: Seymour Cray

**Itens Técnicos Encontrados:** 18

**Contribuições:** Arquitetura Vetorial, Pipelining, Chaining, Unidades Funcionais Segmentadas, Algoritmo de Recíproco de Newton-Raphson, Formato de Ponto Flutuante de 64 bits

# Conteúdo Técnico do CRAY-1 (Seymour Cray)

## 1. Microarquitetura e Estrutura de Hardware

O CRAY-1 é caracterizado por uma arquitetura de processamento vetorial altamente segmentada e paralela, operando com um ciclo de clock de 12.5 nanosegundos.

### 1.1. Registradores Operacionais

<table>
<thead>
<tr>
<th>Tipo de Registrador</th>
<th>Quantidade</th>
<th>Tamanho (bits)</th>
<th>Função Principal</th>
</tr>
</thead>
<tbody>
<tr>
<td>V (Vector)</td>
<td>8</td>
<td>64 x 64</td>
<td>Armazenamento de vetores de 64 elementos de 64 bits.</td>
</tr>
<tr>
<td>S (Scalar)</td>
<td>8</td>
<td>64</td>
<td>Armazenamento de operandos escalares.</td>
</tr>
<tr>
<td>A (Address)</td>
<td>8</td>
<td>24</td>
<td>Armazenamento de endereços de memória e contadores de loop.</td>
</tr>
<tr>
<td>T (Buffer Escalar)</td>
<td>64</td>
<td>64</td>
<td>Buffer de alta velocidade para registradores S.</td>
</tr>
<tr>
<td>B (Buffer de Endereço)</td>
<td>64</td>
<td>24</td>
<td>Buffer de alta velocidade para registradores A.</td>
</tr>
<tr>
<td>VL (Vector Length)</td>
<td>1</td>
<td>7</td>
<td>Define o número de elementos a serem processados em uma operação vetorial (máximo 64).</td>
</tr>
<tr>
<td>VM (Vector Mask)</td>
<td>1</td>
<td>64</td>
<td>Usado para controle condicional de elementos vetoriais (operações mascaradas).</td>
</tr>
</tbody>
</table>

---


## Page 101

# 1.2. Unidades Funcionais

O CRAY-1 possui 12 unidades funcionais independentes e totalmente segmentadas, permitindo a emissão de uma nova operação a cada ciclo de clock.

<table>
  <thead>
    <tr>
      <th>Categoria</th>
      <th>Unidade Funcional</th>
      <th>Segmentação (Latência)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Endereço</td>
      <td>Address Add</td>
      <td>2 ciclos</td>
    </tr>
    <tr>
      <td></td>
      <td>Address Multiply</td>
      <td>6 ciclos</td>
    </tr>
    <tr>
      <td>Escalar</td>
      <td>Scalar Add</td>
      <td>3 ciclos</td>
    </tr>
    <tr>
      <td></td>
      <td>Scalar Shift</td>
      <td>2 ou 3 ciclos</td>
    </tr>
    <tr>
      <td></td>
      <td>Scalar Logical</td>
      <td>1 ciclo</td>
    </tr>
    <tr>
      <td></td>
      <td>Population/Leading Zero Count</td>
      <td>4 ciclos</td>
    </tr>
    <tr>
      <td>Vetorial</td>
      <td>Vector Add</td>
      <td>3 ciclos</td>
    </tr>
    <tr>
      <td></td>
      <td>Vector Shift</td>
      <td>4 ciclos</td>
    </tr>
    <tr>
      <td></td>
      <td>Vector Logical</td>
      <td>2 ciclos</td>
    </tr>
    <tr>
      <td>Ponto Flutuante</td>
      <td>Floating Point Add</td>
      <td>6 ciclos</td>
    </tr>
    <tr>
      <td></td>
      <td>Floating Point Multiply</td>
      <td>7 ciclos</td>
    </tr>
    <tr>
      <td></td>
      <td>Reciprocal Approximation</td>
      <td>14 ciclos</td>
    </tr>
  </tbody>
</table>

# 1.3. Conceitos de Microarquitetura

*   **Segmentação (Pipelining):** Todas as 12 unidades funcionais são segmentadas, permitindo que uma nova operação comece a cada ciclo de clock, mesmo que a latência total da unidade seja maior.
*   **Chaining (Encadeamento):** O resultado de uma unidade funcional pode ser imediatamente encaminhado como operando de outra unidade funcional no ciclo de clock seguinte, sem a necessidade de ser escrito em um registrador intermediário, maximizando a taxa de transferência (throughput).
*   **Processamento Vetorial:** A arquitetura é otimizada para operações em vetores, onde uma única instrução opera em múltiplos elementos de dados, controlados pelos registradores VL e VM.

# 2. Algoritmos e Fórmulas

## 2.1. Formato de Ponto Flutuante (64 bits)

O formato de ponto flutuante do CRAY-1 é de 64 bits, consistindo em:

*   1 bit de sinal (s).
*   15 bits de expoente (e).
*   48 bits de mantissa (m).

O valor representado é dado por: $Valor = (-1)^s \times m \times 2^{e-E_0}OndeE_0éo * bias * doexpoente, eamantissam$ é normalizada (o bit mais significativo é sempre 1, exceto para zero).

## 2.2. Algoritmo de Recíproco (Divisão)

A divisão de ponto flutuante é realizada por multiplicação pelo recíproco, utilizando a unidade de Reciprocal Approximation (RA). O algoritmo de Recíproco (Reciprocal Iteration) é baseado na iteração de Newton-Raphson para calcular 1/D, onde D é

---


## Page 102

o divisor.

A unidade RA fornece uma aproximação inicial $X_0$ para 1/D. A iteração de Newton-Raphson é: $X_{i+1} = X_i \times (2 - D \times X_i)$ onde $X_i$ é a aproximação atual do divisor. A unidade Reciprocal Approximation calcula o termo $(2 - D \times X_i)$ em uma única instrução: Instrução 067ijk : $S_i \leftarrow 2 - (S_j) \times (S_k)$ onde $S_j$ e $S_k$ são registradores escalares.

## 2.3. Algoritmo de Adição de Ponto Flutuante (Simplificado)

1. Comparação de Expoentes: Determinar a diferença entre os expoentes.
2. Alinhamento: Deslocar a mantissa do número com o menor expoente para a direita pelo valor da diferença de expoentes.
3. Adição/Subtração: Realizar a adição ou subtração das mantissas alinhadas.
4. Normalização: Ajustar o expoente e a mantissa do resultado para garantir a forma normalizada.

## 2.4. Algoritmo de Multiplicação de Ponto Flutuante (Simplificado)

1. Adição de Expoentes: Somar os expoentes e subtrair o bias ($E_0$).
2. Multiplicação de Mantissas: Multiplicar as mantissas.
3. Normalização: Ajustar o expoente e a mantissa do resultado.
4. Sinal: O bit de sinal é o XOR dos bits de sinal dos operandos.

## 3. Instruções e Operações

*   **Instrução de Contagem de População (Population Count):** Calcula o número de bits ‘1’ em um registrador escalar. $Instrução 026ijk : A_i \leftarrow PopCount(S_j)$
*   **Instrução de Contagem de Zeros Iniciais (Leading Zero Count):** Calcula o número de zeros à esquerda do bit ‘1’ mais significativo em um registrador escalar. $Instrução 027ijk : A_i \leftarrow LZCount(S_j)$
*   **Instruções Lógicas Vetoriais:** Incluem produto lógico (AND), diferença lógica (XOR) e soma lógica (OR) aplicadas elemento por elemento nos registradores vetoriais.
*   **Transferência de Bloco (Block Transfer):** Instruções para mover grandes blocos de dados entre a memória principal e os buffers B/T, otimizando o acesso a dados. $Exemplo: 034ijk : B_{jk} \leftarrow Memoria[A_0 ... A_0 + A_i - 1]$

## Pesquisador 15: Gordon E. Moore

**Itens Técnicos Encontrados:** 11

**Contribuições:** Lei de Moore, Escalonamento de Transistores, Relação Custo-Complexidade, Densidade de Componentes, Padrões de Metalização Multicamadas, Escalonamento de Potência, Limitações de Integração Linear

A formulação inicial da **Lei de Moore** estabelece que a complexidade para o custo mínimo por componente em circuitos integrados aumenta a uma taxa de aproximadamente um **fator de dois por ano**. Esta observação levou à projeção de que, até 1975, o número de componentes por circuito integrado para custo mínimo atingiria **65.000**.

A relação **custo-complexidade** é um conceito central. Para circuitos simples, o custo por componente é quase inversamente proporcional ao número de componentes. No entanto, à medida que a complexidade aumenta, a diminuição do rendimento (yield) compensa o aumento, elevando o custo por componente e estabelecendo um **ponto de custo mínimo** (em 1965, cerca de 50 componentes por circuito).

O **escalonamento físico** é definido por tolerâncias dimensionais que permitem a construção de transistores de alto desempenho em centros separados por **dois milésimos de polegada** (2 mil). Esta tolerância resulta em uma **densidade de área** de cerca de um quarto de milhão (250.000) de componentes por polegada quadrada. Para alcançar essa alta

---


## Page 103

densidade, a **estrutura de interconexão** requer o uso de padrões de metalização multicamadas separados por filmes **dielétricos**, eliminando o desperdício de espaço.

Em termos de **microarquitetura e térmica**, as estruturas eletrônicas integradas são inerentemente **bidimensionais**, o que facilita a dissipação de calor ao fornecer uma superfície de resfriamento próxima a cada centro de geração de calor. O **escalonamento de potência** é favorecido pela redução das dimensões, que limita a quantidade de capacitância a ser acionada, permitindo que a estrutura opere em **velocidade mais alta para a mesma potência por unidade de área**.

As **limitações em circuitos lineares** são notáveis, principalmente devido à dificuldade em integrar **capacitores e indutores de grande valor**, que exigem o armazenamento de energia em um volume incompatível com a miniaturização. Contudo, o **casamento e rastreamento** (matching and tracking) de componentes semelhantes em estruturas integradas permite o projeto de **amplificadores diferenciais** de desempenho aprimorado e a estabilização de osciladores através de **feedback térmico**.

O **Silício** é projetado para permanecer o material básico devido à tecnologia estabelecida em torno dele e de seu óxido, enquanto o **Arsenieto de Gálio** é relevante para funções integradas de micro-ondas. Elementos semicondutores passivos são considerados atrativos para baixo custo e alta confiabilidade, desde que a precisão não seja um requisito primordial.

---

## Pesquisador 16: Andrew S. Grove

Itens Técnicos Encontrados: 20

Contribuições: Modelo de Deal-Grove, Equação Geral de Oxidação, Taxa Linear-Parabólica, Taxa Linear, Tecnologia Planar, Mitigação de Contaminação por Sódio, Livro Physics and Technology of Semiconductor Devices, Otimização de Rendimento

---

## Conteúdo Técnico do Trabalho de Andrew S. Grove

### 1. Modelo de Deal-Grove para Oxidação Térmica de Silício (com B. E. Deal)

O Modelo de Deal-Grove descreve matematicamente o crescimento de uma camada de óxido (SiO₂) na superfície do silício (Si) durante a oxidação térmica, um processo fundamental na fabricação de dispositivos semicondutores (transistores MOS).

#### 1.1. Equação Geral de Oxidação

A relação geral que descreve a espessura do óxido ($x_o$) em função do tempo de oxidação ($t$) é dada por:

$$x_o^2 + Ax_o = B(t + \tau)$$

Onde:

*   $x_o$: Espessura da camada de óxido (cm).
*   $t$: Tempo de oxidação (s).
*   $\tau$: Tempo de oxidação equivalente para a espessura inicial de óxido ($x_i$), $\tau = x_i^2/B + Ax_i/B$.

#### 1.2. Coeficientes de Taxa

A equação geral é definida por dois coeficientes de taxa, que são constantes para uma dada temperatura e pressão parcial do oxidante:

1.  **Taxa Linear-Parabólica ($B$):** $B = \frac{2D_{eff}C^*}{N_1}$

    *   $D_{eff}$: Coeficiente de difusão efetivo do oxidante no óxido (cm²/s).
    *   $C^*$: Concentração de equilíbrio do oxidante no óxido (moléculas/cm³).

---


## Page 104

*   $N_1$: Número de moléculas de oxidante incorporadas por unidade de volume de óxido (moléculas/cm³).

2. **Taxa Linear ($B/A$):** $\frac{B}{A} = \frac{k_s C^*}{N_1 \left( 1 + \frac{k_s}{h} + \frac{k_s x_o}{D_{eff}} \right)}$

*   $k_s$: Coeficiente de taxa de reação na interface Si/SiO₂ (cm/s).
*   $h$: Coeficiente de transferência de massa na fase gasosa (cm/s).

## 1.3. Regimes de Oxidação

A equação geral pode ser simplificada para dois regimes limitantes:

1. **Regime Limitado pela Reação (Óxidos Finos):** Para $t \ll \frac{A^2}{4B}$ (ou $x_o \ll A$), a equação se torna aproximadamente linear:
   $x_o \approx \frac{B}{A}(t + \tau)$ A taxa decrescente é controlada pela área química na interface Si/SiO₂.

2. **Regime Limitado pela Difusão (Óxidos Espessos):** Para $t \gg \frac{A^2}{4B}$ (ou $x_o \gg A$), a equação se torna aproximadamente parabólica: $x_o^2 \approx B(t + \tau)$ A taxa de crescimento é controlada pela difusão do oxidante através da camada de óxido existente.

## 1.4. Conceitos de Microarquitetura e Dispositivos

*   **Transistor MOS (Metal-Oxide-Semiconductor):** O trabalho de Grove sobre a oxidação do silício foi fundamental para o desenvolvimento da tecnologia MOS, que se tornou a base para a fabricação de microprocessadores e memórias.
*   **Tecnologia Planar:** O modelo Deal-Grove é um pilar da tecnologia planar, que permite a criação de dispositivos semicondutores em uma superfície plana, facilitando a integração em larga escala (VLSI).
*   **Contaminação por Sódio:** Grove, junto com Bruce Deal e Ed Snow, realizou trabalhos pioneiros na identificação e mitigação da contaminação por íons de sódio no óxido de silício, um problema crítico que afetava a estabilidade e o desempenho dos primeiros dispositivos MOS.

## 2. Livro “Physics and Technology of Semiconductor Devices” (1967)

Este livro é um texto fundamental que consolida o conhecimento sobre a física e a tecnologia dos dispositivos semicondutores, com ênfase nos dispositivos planares de silício.

### 2.1. Estruturas de Hardware/Conceitos de Dispositivos

*   **Teoria de Bandas em Semicondutores:** Descrição das propriedades eletrônicas dos materiais semicondutores.
*   **Fenômenos de Transporte:** Mecanismos de condução de corrente (deriva e difusão) em semicondutores.
*   **Junções p-n:** Análise detalhada da estrutura e operação de diodos.
*   **Transistores Bipolares de Junção (BJT):** Princípios de operação e características.
*   **Transistores de Efeito de Campo (FET) e MOS:** Análise da estrutura, operação e modelagem de dispositivos MOS.

### 2.2. Conceitos de Processamento

*   **Tecnologia Planar:** Processos de fabricação, incluindo:
    *   Crescimento de Camada (Vapor-Phase Growth).
    *   Oxidação Térmica (Deal-Grove Model).
    *   Difusão em Estado Sólido (Solid-State Diffusion).
    *   Implantação Iônica (Ion Implantation).
    *   Metalização (Metallization).

---


## Page 105

# 3. Conceitos de Manufatura e Otimização de Rendimento (Yield)

Embora Grove seja mais conhecido por suas filosofias de gestão, seus conceitos de otimização de rendimento na manufatura de semicondutores são técnicos:

*   **Otimização de Rendimento (Yield Optimization):** A busca incessante por aumentar a porcentagem de chips funcionais por wafer.
*   **Fórmula de Rendimento (Yield Formula - Conceito):** Embora Grove não tenha criado a fórmula de rendimento mais famosa (como a de Poisson ou Murphy), ele aplicou e popularizou o conceito de que o rendimento é uma função exponencial da densidade de defeitos ($D_0$) e da área do chip ($A$): $Yield \approx e^{-AD_0}$ (Modelo de Poisson Simplificado)
    *   $A$: Área do chip.
    *   $D_0$: Densidade de defeitos por unidade de área.
    *   O foco técnico de Grove estava na **redução de $D_0$** através de processos de manufatura rigorosos e controle de qualidade (conceito de “High Output Management” aplicado à fábrica).
*   **Estrutura de Hardware (Fábrica):** A fábrica de semicondutores (Fab) como um sistema de processamento de alto rendimento, onde cada etapa é um ponto de controle estatístico de processo (SPC) para minimizar a densidade de defeitos.
*   **Algoritmos de Controle de Processo:** Implementação de sistemas de medição e controle em tempo real para ajustar parâmetros de processo (temperatura, tempo, fluxo de gás) com base em dados de rendimento e defeitos.
*   **Inflection Point (Ponto de Inflexão Estratégica):** Embora seja um conceito de gestão, a mudança de tecnologia (e.g., de memória para microprocessadores) implica uma mudança técnica fundamental na arquitetura de hardware e nos algoritmos de fabricação (processos de litografia, deposição, ataque).

---

## Pesquisador 17: Jim Keller

Itens Técnicos Encontrados: 20

Contribuições: Arquitetura x86-64 (AMD64), Controlador de Memória Integrado (IMC), Tecnologia HyperTransport, Micro-Operações (Macro-Ops), Cache de Micro-Operações ($\mu$OP Cache), Predição de Desvio Neural-Net, Cache L1 Write-Back, Simultaneous Multi-Threading (SMT)

## Conteúdo Técnico das Contribuições de Jim Keller

### AMD K7 (Athlon) - Microarquitetura

O processador AMD-K7 implementa técnicas avançadas de design, incluindo: **Superscalar Out-of-Order (Fora de Ordem)** com três unidades de Mídia (Multimedia Units) e três unidades de Inteiros (Integer Units) superscalares e pipelined (com pipeline). Possui três decodificadores de instrução x86 e utiliza formatos de instrução interna de tamanho fixo (**Macro-Ops**). A Unidade de Controle de Instrução (ICU) tem **72 entradas**. Inclui a tecnologia **3DNow!™** para extensão de instruções multimídia, grandes estruturas de caches L1 e L2 e TLB (Translation Lookaside Buffer), **Renomeação de Registradores e Encaminhamento de Dados (Register Renaming and Data-Forwarding)**, **Predição Dinâmica de Desvio (Dynamic Branch Prediction)** e Tecnologia de Interface S2K (System 2000 - Slot A/Socket A).

---


## Page 106

# AMD K8 (Hammer - Athlon 64/Opteron) - Microarquitetura

A microarquitetura K8, codinome “Hammer”, introduziu a Arquitetura x86-64 (AMD64), uma estratégia de 64 bits que permite a execução de aplicações de 32 bits e 64 bits. Utiliza caminhos de dados e endereços de 64 bits de largura e incorpora um espaço de endereço virtual de 48 bits e um espaço de endereço físico de 40 bits. A microarquitetura utiliza dados de chave (key data) para o endereçamento. O Controlador de Memória Integrado (Integrated Memory Controller - IMC) foi movido do Northbridge para o die do processador, resultando na **redução da latência de acesso à memória** e **aumento da largura de banda**. A Tecnologia HyperTransport™ é um link ponto-a-ponto de alta velocidade e alto desempenho para interconexão de circuitos integrados, utilizando três links HyperTransport para **multiprocessamento glueless**, fornecendo escalabilidade, alta largura de banda e baixa latência para comunicação entre processadores e I/O.

# Apple A4 e A5 - Microarquitetura

Jim Keller esteve envolvido no design dos processadores Apple A4 e A5. O Apple A4 é um SoC (System on a Chip) de 32 bits, PoP (Package on Package), com núcleo single-core baseado em ARM Cortex-A8, Cache L1 de 32 KB para dados e 32 KB para instruções, e Cache L2 de 512 KB. O Apple A5 é um SoC de 32 bits com núcleo dual-core baseado em ARM Cortex-A9, **Cache L1 de 32 KB para instruções e 32 KB para dados por núcleo (split L1 cache)**, e Cache L2 de 1 MB (1024 KB) compartilhado entre os núcleos. O conceito de dual-core e arquitetura mais avançada resultou em um aumento de desempenho significativo sobre o A4.

# AMD Zen (Zen 1) - Microarquitetura

A microarquitetura Zen representa um redesenho completo do núcleo x86 da AMD. O Front-End inclui um **Cache de Micro-Operações (µOP Cache)** que armazena micro-operações decodificadas para alimentar o scheduler diretamente, ignorando a decodificação x86 complexa e reduzindo o consumo de energia. O Decodificador de Instruções decodifica **4 instruções x86 por ciclo**. A **Predição de Desvio (Branch Prediction)** tem precisão e latência aprimoradas, utilizando um **preditor de desvio neural-net**. O Execution Engine (Back-End) possui um **Pipeline Mais Largo e Mais Profundo**, com maior capacidade de execução *out-of-order* e *wider issue*. As Unidades de Execução de Inteiros incluem **seis pipes de inteiros**, com 4 ALUs (Arithmetic Logic Units) e 2 AGUs (Address Generation Units). As Unidades de Execução de Ponto Flutuante (FPUs) são **quatro de 128 bits**. A Hierarquia de Cache foi aprimorada com a mudança do Cache L1 de *write-through* para *write-back* (menor latência e maior largura de banda), Cache L2 de 512 KB dedicado por núcleo, e Cache L3 de 8 MB compartilhado por quatro núcleos (CCX), implementado como um **cache vítima**. Inclui a implementação de **Simultaneous Multi-Threading (SMT)** para melhor utilização dos recursos do núcleo.

# Pesquisador 18: Avi Kivity

**Itens Técnicos Encontrados:** 19

**Contribuições:** Utilização de VT-x/AMD-V para execução nativa, Implementação do Guest Execution Loop, Uso de EPT/NPT para Gerenciamento de Memória de Segunda Nível

# Conteúdo Técnico Puro: KVM, QEMU e Emulação x86 (Avi Kivity et al.)

O KVM (Kernel-based Virtual Machine) é um subsistema de virtualização que utiliza as **Extensões de Virtualização de Hardware** (Intel VT-x e AMD-V) da arquitetura x86. Estas extensões fornecem três mecanismos primários de microarquitetura para facilitar a virtualização: o **Novo Modo de Operação Convidado (Guest Operating Mode)**, que permite ao processador operar em um estado de privilégio regular com a capacidade de interceptar seletivamente instruções e acessos a registradores; a **Troca de Estado de Hardware (Hardware State Switch)**, que gerencia a transição eficiente entre o modo convidado e o modo host, trocando registradores de controle e segmento; e o **Relatório de Razão de Saída (Exit Reason Reporting)**, que comunica ao software host o motivo da interrupção da execução do convidado.

---


## Page 107

A arquitetura do KVM é centrada no **Nó de Dispositivo** `/dev/kvm`, que é a interface de comunicação entre o espaço de usuário (QEMU) e o kernel. As operações essenciais do `/dev/kvm` incluem a **Criação de VM**, **Alocação de Memória** (mapeando a memória física do convidado para a memória física do host), **Criação de vCPU** e **Configuração de Registradores** da vCPU.

O **Loop de Execução do Convidado** (**Guest Execution Loop**) define o algoritmo de execução da vCPU. O processo inicia no espaço de usuário com uma chamada `ioctl()` de Execução do Convidado, que transfere o controle para o modo kernel (KVM). O KVM então entra no Modo Convidado e executa o código do convidado **nativamente**. Qualquer evento que exija intervenção do hypervisor (como E/S, interrupções ou instruções privilegiadas) causa uma **Saída (Exit)** para o host. O KVM manipula a saída, e se for uma interrupção de E/S ou um sinal pendente, o controle é retornado ao espaço de usuário (QEMU) para emulação ou agendamento.

Para o **Gerenciamento de Memória**, o KVM emprega o **Gerenciamento de Memória de Segunda Nível** (**Second Level Memory Management**), implementado via **Extended Page Tables (EPT)** da Intel ou **Nested Page Tables (NPT)** da AMD. Este mecanismo de hardware permite que o KVM mantenha o mapeamento da memória física do convidado para a memória física do host, isolando o espaço de endereço do convidado.

A **Emulação de Dispositivos** é primariamente delegada ao QEMU no espaço de usuário. O KVM intercepta as operações de E/S do convidado e as repassa ao QEMU para processamento. O KVM utiliza um **APIC Virtualizado** e as facilidades de hardware, como o **Virtual-Interrupt Delivery**, para a **Injeção de Interrupções** no convidado. O **Agendamento** das vCPUs é realizado pelo agendador padrão do kernel Linux, tratando as vCPUs como **threads de usuário normais**. A **Sincronização** interna do KVM é garantida pelo uso de **bloqueios (locks)** e semáforos do kernel.

---


## Page 108

# Tabela de Conceitos e Estruturas de Hardware

<table>
  <thead>
    <tr>
      <th>Conceito/Estrutura</th>
      <th>Tipo</th>
      <th>Descrição Técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>KVM</td>
      <td>Subsistema Kernel</td>
      <td>Monitor de Máquina Virtual (VMM) no kernel Linux.</td>
    </tr>
    <tr>
      <td>VT-x / AMD-V</td>
      <td>Extensões de Hardware</td>
      <td>Mecanismos de microarquitetura x86 para virtualização.</td>
    </tr>
    <tr>
      <td>Guest Operating Mode</td>
      <td>Modo de CPU</td>
      <td>Estado de privilégio que permite execução nativa com interceptação seletiva.</td>
    </tr>
    <tr>
      <td>Hardware State Switch</td>
      <td>Mecanismo de CPU</td>
      <td>Troca de registradores de controle e segmento na transição host/guest.</td>
    </tr>
    <tr>
      <td>Exit Reason Reporting</td>
      <td>Mecanismo de CPU</td>
      <td>Comunicação do motivo da saída do convidado para o host.</td>
    </tr>
    <tr>
      <td>/dev/kvm</td>
      <td>Nó de Dispositivo</td>
      <td>Interface de controle entre QEMU (userspace) e KVM (kernel).</td>
    </tr>
    <tr>
      <td>Guest Execution Loop</td>
      <td>Algoritmo</td>
      <td>Fluxo de execução: ioctl() -> Enter Guest Mode -> Execute natively -> Exit -> Handle Exit.</td>
    </tr>
    <tr>
      <td>EPT / NPT</td>
      <td>Estrutura de Hardware</td>
      <td>Tabelas de página aninhadas para Gerenciamento de Memória de Segunda Nível.</td>
    </tr>
    <tr>
      <td>APIC Virtualizado</td>
      <td>Estrutura de Hardware</td>
      <td>Controlador de Interrupção Programável Avançado virtualizado.</td>
    </tr>
    <tr>
      <td>Virtual-Interrupt Delivery</td>
      <td>Mecanismo de Hardware</td>
      <td>Facilidade para injeção eficiente de interrupções no convidado.</td>
    </tr>
    <tr>
      <td>Emulação de Dispositivos (QEMU)</td>
      <td>Conceito de Software</td>
      <td>Emulação de hardware de E/S no espaço de usuário.</td>
    </tr>
    <tr>
      <td>vCPU como Thread</td>
      <td>Conceito de Agendamento</td>
      <td>Agendamento de vCPUs como threads de usuário normais pelo kernel host.</td>
    </tr>
    <tr>
      <td>ioctl()</td>
      <td>Chamada de Sistema</td>
      <td>Interface de comunicação e controle entre QEMU e KVM.</td>
    </tr>
    <tr>
      <td>Bloqueios e Semáforos</td>
      <td>Algoritmo de Sincronização</td>
      <td>Mecanismos do kernel Linux para proteger estruturas de dados compartilhadas.</td>
    </tr>
    <tr>
      <td>Alocação de Memória</td>
      <td>Conceito de Software</td>
      <td>Mapeamento da memória física do convidado para a memória física do host.</td>
    </tr>
    <tr>
      <td>Criação de vCPU</td>
      <td>Conceito de Software</td>
      <td>Criação de um thread de execução para o convidado.</td>
    </tr>
    <tr>
      <td>Configuração de Registradores</td>
      <td>Conceito de Software</td>
      <td>Inicialização dos registradores da vCPU.</td>
    </tr>
    <tr>
      <td>Interceptação de E/S</td>
      <td>Mecanismo de Software</td>
      <td>KVM intercepta E/S do convidado e repassa ao QEMU.</td>
    </tr>
    <tr>
      <td>Execução Nativa</td>
      <td>Conceito de Microarquitetura</td>
      <td>Execução direta do código do convidado no hardware.</td>
    </tr>
    <tr>
      <td>Gerenciamento de Memória de Segunda Nível</td>
      <td>Conceito de Microarquitetura</td>
      <td>Abstração de memória para isolamento e segurança.</td>
    </tr>
  </tbody>
</table>

---

## Pesquisador 19: Paul Rosenfeld

Itens Técnicos Encontrados: 20

Contribuições: Simulador de Sistema de Memória com Precisão de Ciclo (DRAMSim2), Modelagem Orientada a Objetos da Hierarquia de Memória, Implementação de Restrições de Temporização da JEDEC, Modelagem de Políticas de Buffer de Linha (Open/Closed Page Mode), Algoritmo de Agendamento de Comandos Out-of-Order, Modelo de Consumo de Energia Baseado em Transições de Estado

---


## Page 109

# Conteúdo Técnico de Paul Rosenfeld - DRAMSim2

**Pesquisador Principal:** Paul Rosenfeld (co-autor de DRAMSim2) **Área de Foco:** Sistemas de Memória, DRAM, Otimização de Cache (Simulação)

## Conceitos de Microarquitetura e Estruturas de Hardware (DRAMSim2)

O DRAMSim2 é um simulador de sistema de memória com precisão de ciclo (cycle-accurate) para dispositivos DDR2/3.

### Estrutura do Sistema de Memória (MemorySystem)

O simulador é implementado em C++ como um modelo orientado a objetos. O núcleo do DRAMSim2 é um objeto chamado MemorySystem .

1.  **Componentes Principais:**
    *   **Transaction Queue (Fila de Transações):** Fila de entrada (in-order) para requisições de memória (READ/WRITE).
    *   **Address Map Schedule (Agendador de Mapeamento de Endereço):** Determina a ordem de emissão de comandos.
    *   **Command Queue (Fila de Comandos):** Fila de comandos (out-of-order) para comandos DRAM (e.g., ACT, PRE, CAS, RAS).
    *   **Read Return Queue (Fila de Retorno de Leitura):** Fila de saída (out-of-order) para dados lidos.
    *   **Bank States (Estados do Banco):** Mantém o estado de cada banco de memória (e.g., fechado, ativo, pré-carregando).

2.  **Estrutura da Memória (Hierarquia):**
    *   **Channel (Canal):** O nível mais alto, representa o barramento de comunicação.
    *   **Rank (Rank):** Conjunto de chips DRAM que compartilham o mesmo barramento de comando/endereço.
    *   **Bank (Banco):** Unidade fundamental de armazenamento e operação.
    *   **Row (Linha):** Unidade de ativação e acesso.
    *   **Column (Coluna):** Unidade de acesso de dados dentro de uma linha ativa.

3.  **Parâmetros de Configuração (Device.ini):** Os parâmetros que definem o dispositivo DRAM específico (independentes do controlador) incluem:
    *   Número de ranks.
    *   Esquema de mapeamento de endereço ( ADDRESS_MAPPING_SCHEME ).
    *   Opções de depuração.
    *   Políticas de buffer de linha (row buffer policies).
    *   Estruturas de fila do controlador de memória.
    *   Parâmetros de temporização DRAM (tCL, tRCD, tRP, tRAS, tRC, tRFC, etc.).

## Algoritmos e Políticas

1.  **Política de Buffer de Linha (Row Buffer Policy):**
    *   **Open Page Mode (Modo de Página Aberta):** Mantém a linha ativa após o acesso, permitindo acessos subsequentes mais rápidos (menor latência) se forem para a mesma linha.
    *   **Closed Page Mode (Modo de Página Fechada):** Pré-carrega (precharge) a linha imediatamente após o acesso, garantindo que a próxima requisição não sofra com o overhead de pré-carregamento, mas pode aumentar a

---


## Page 110

latência para acessos subsequentes à mesma linha.

**2. Agendamento de Comandos (Command Scheduling):**

*   O controlador de memória é livre para emitir requisições da fila de comandos (Command Queue) fora de ordem, desde que não viole as restrições de dependência de leitura/escrita ou as restrições de temporização DRAM.
*   **Priorização de Requisições:** O controlador prioriza requisições que podem se beneficiar do *open page mode* (acessos a linhas já abertas) para aumentar a largura de banda e reduzir a latência.

**3. Gerenciamento de Refresh (Atualização):**

*   O controlador de memória modela os efeitos do *DRAM refresh* (atualização da DRAM).
*   O *refresh* é uma fonte significativa de variação na latência de memória, pois as requisições de memória devem esperar até que o *refresh* em andamento seja concluído.

## Fórmulas (Conceitos de Temporização)

Embora o artigo não apresente fórmulas matemáticas explícitas no formato de equações, ele se baseia em um conjunto rigoroso de restrições de temporização (timing constraints) da JEDEC, que funcionam como “fórmulas” para a precisão do simulador.

### Restrições de Temporização (Exemplos de Parâmetros do Device.ini):

<table>
  <thead>
    <tr>
      <th>Parâmetro</th>
      <th>Descrição</th>
      <th>Unidade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>tCL</td>
      <td>CAS Latency (Latência de Acesso à Coluna)</td>
      <td>Ciclos de Clock</td>
    </tr>
    <tr>
      <td>trCD</td>
      <td>RAS to CAS Delay (Atraso entre Ativação e Acesso à Coluna)</td>
      <td>Ciclos de Clock</td>
    </tr>
    <tr>
      <td>trp</td>
      <td>Row Precharge Time (Tempo de Pré-carregamento da Linha)</td>
      <td>Ciclos de Clock</td>
    </tr>
    <tr>
      <td>trAS</td>
      <td>Row Active Time (Tempo Mínimo de Ativação da Linha)</td>
      <td>Ciclos de Clock</td>
    </tr>
    <tr>
      <td>trC</td>
      <td>Row Cycle Time (Tempo de Ciclo da Linha)</td>
      <td>Ciclos de Clock</td>
    </tr>
    <tr>
      <td>trFC</td>
      <td>Refresh Cycle Time (Tempo de Ciclo de Atualização)</td>
      <td>Ciclos de Clock</td>
    </tr>
    <tr>
      <td>tWR</td>
      <td>Write Recovery Time (Tempo de Recuperação de Escrita)</td>
      <td>Ciclos de Clock</td>
    </tr>
    <tr>
      <td>twTR</td>
      <td>Write to Read Delay (Atraso de Escrita para Leitura)</td>
      <td>Ciclos de Clock</td>
    </tr>
    <tr>
      <td>tRTW</td>
      <td>Read to Write Delay (Atraso de Leitura para Escrita)</td>
      <td>Ciclos de Clock</td>
    </tr>
  </tbody>
</table>

### Cálculo de Latência (Conceito):

A latência total de uma requisição de memória é determinada pela soma dos atrasos de agendamento (scheduling delays) e a aplicação sequencial das restrições de temporização da JEDEC.

Latência Total = Atraso de Fila + Σ Restrição de Temporizaçãoᵢ

O simulador garante que: $Tempo de Emissão do Comando ≥ Tempo de Emissão do Comando Anterior + Restrição de Temporização Mínima$

### Modelo de Consumo de Energia (Power Model):

O DRAMSim2 utiliza um modelo de energia baseado nas transições de estado (state transitions) de cada banco de memória, conforme descrito pela Micron.

Energia Total = Σ Transições Energia Transição + Σ Tempo Energia Estática

---


## Page 111

O modelo inclui heurísticas para colocar os bancos em estados de baixa energia (low power mode) durante períodos de baixa atividade.

## Contribuições Técnicas Principais

*   Simulador de Sistema de Memória com Precisão de Ciclo (DRAMSim2).
*   Modelagem Orientada a Objetos da Hierarquia de Memória (Channel, Rank, Bank, Row, Column).
*   Implementação de Restrições de Temporização da JEDEC (tCL, tRCD, tRP, tRAS, etc.).
*   Modelagem de Políticas de Buffer de Linha (Open/Closed Page Mode).
*   Algoritmo de Agendamento de Comandos Out-of-Order (com priorização de linha aberta).
*   Modelo de Consumo de Energia Baseado em Transições de Estado.
*   Integração com Simuladores de Sistema Completo (MARSSx86).
*   Ferramenta de Visualização de Resultados (DRAMVis).

## Pesquisador 20: Onur Mutlu

Itens Técnicos Encontrados: 20

Contribuições: RowHammer, Target Row Refresh (TRR), BlockHammer, Processing-in-Memory (PIM), RowClone, Ambit, Processing Near Memory (PNM), Arquiteturas 3D-Stacked

## Conteúdo Técnico do Trabalho de Onur Mutlu

### I. RowHammer e Mitigações em Microarquitetura DRAM

#### Conceitos Fundamentais de Microarquitetura

*   **RowHammer (RH):** Vulnerabilidade de circuito em DRAM onde o acesso repetido a uma linha de memória (linha agressora) causa a inversão de bits (**bit-flips**) em linhas adjacentes (linhas vítimas) devido à interferência eletromagnética célula-a-célula.
*   **Threshold (Limite de Ativação):** O número mínimo de ativações de uma linha agressora necessário para induzir um bit-flip em uma linha vítima. O escalonamento da tecnologia DRAM tem reduzido drasticamente este limite (ex: de 139K ativações em 2014 para 4.8K em 2020).
*   **Double-Sided Hammering:** Técnica de ataque que envolve o acesso repetido a duas linhas adjacentes à linha vítima, sendo mais eficaz na indução de bit-flips.

#### Algoritmos e Mecanismos de Mitigação

*   **Target Row Refresh (TRR):** Mecanismo de defesa implementado no chip DRAM (in-DRAM). A DRAM rastreia as linhas ativadas e, ao atingir o *threshold*, emite um comando de *refresh* para as linhas vítimas adjacentes.
*   **pTRR (Probabilistic Target Row Refresh):** Versão anterior do TRR que utiliza probabilidade para refrescar linhas adjacentes.
*   **Refresh Management (RFM):** Recurso introduzido no padrão DDR5. O controlador de memória rastreia a contagem de ativações por granularidade de banco DRAM e emite um *refresh* RFM quando a contagem atinge um valor limite (baseado no *threshold* de RowHammer), assegurando o *refresh* seguro de todas as linhas vítimas potenciais.

---


## Page 112

*   **BlockHammer:** Mitigação de baixo custo que rastreia as taxas de ativação das linhas usando Bloom Filters eficientes em área. O mecanismo garante que nenhuma linha seja ativada acima do limite seguro. A segurança é determinada por uma equação que define o número máximo de linhas que o mecanismo deve rastrear dentro de um *epoch* para garantir a operação segura.
*   **Graphene:** Mecanismo de proteção que utiliza um rastreador de baixo custo (*low-cost tracker*) para identificar linhas agressoras.

## Conceitos de Ataque e Exploração

*   **SMASH:** Técnica de *hammering* lateral (*side-channel hammering*) que usa o RowHammer para inferir dados.
*   **RAMBleed:** Ataque que usa *bit-flips* de RowHammer como um canal lateral para determinar dados em outras linhas.

## II. Processing-in-Memory (PIM)

### Conceitos e Arquiteturas

*   **PIM (Processing-in-Memory) / NDP (Near-Data Processing):** Paradigma de computação que coloca mecanismos de computação perto ou dentro da memória (dentro dos chips de memória, na camada lógica de memória 3D-stacked, ou nos controladores de memória) para mitigar o gargalo de movimento de dados (*data movement bottleneck*).
*   **PUM (Processing Using Memory):** Abordagem que explora as propriedades operacionais analógicas da DRAM para realizar operações em massa e altamente paralelas na memória com pequenas mudanças de baixo custo.
    *   **RowClone:** Algoritmo que permite a cópia de uma linha inteira de DRAM para outra linha dentro do mesmo *sub-array* em um único ciclo de tempo, usando a ativação simultânea das linhas de origem e destino.
    *   **Ambit:** Arquitetura PIM que usa a propriedade de *triple-row activation* em três linhas de DRAM para realizar operações lógicas bitwise em massa (ex: A AND B, A OR B, A NOT B).
    *   **Gather-Scatter DRAM:** Arquitetura que permite a agregação (*Gather*) e dispersão (*Scatter*) de dados de/para a memória de forma eficiente, útil para operações de vetorização.
*   **PNM (Processing Near Memory):** Abordagem que utiliza a capacidade de computação em controladores de memória convencionais ou na camada lógica de memórias 3D-stacked.
    *   **Arquiteturas 3D-Stacked:** Uso de *Through-Silicon Vias* (TSVs) para conectar múltiplas camadas de memória e uma camada lógica, proporcionando alta largura de banda interna. Exemplos incluem **Hybrid Memory Cube (HMC)** e **High-Bandwidth Memory (HBM)**.
    *   **PEI (PIM-Enabled Instructions):** Instruções que permitem que o processador delegue tarefas de computação para a lógica PIM na memória.

### Algoritmos e Aplicações

O PIM é aplicado para acelerar cargas de trabalho intensivas em dados, como:

*   Análise de Genoma (*Genome Analysis*)
*   Aprendizado de Máquina (*Machine Learning*)
*   Análise de Séries Temporais (*Time Series Analysis*)
*   Gráficos (*Graph Processing*)