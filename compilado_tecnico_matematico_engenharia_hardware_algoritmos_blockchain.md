# Compilado Técnico e Matemático: Engenharia de Hardware e Algoritmos de Blockchain

Este documento apresenta uma síntese técnica e matemática rigorosa fundamentada nos trabalhos, patentes e especificações desenvolvidos por Micree Zhan, N.G. Zhang, Xiang Zhu, Jihan Wu, Josh Zerlan, Nasser Ghoseiri, Jeff Ownby e Sonny Vleisides. O conteúdo foca exclusivamente em arquiteturas de circuitos integrados, formulações matemáticas de criptografia e métricas de desempenho de semicondutores, omitindo qualquer narrativa histórica ou biográfica.

---

## 1. Fundamentos Matemáticos do Algoritmo SHA-256

O algoritmo SHA-256 constitui a base lógica para a Prova de Trabalho (PoW) e opera através de uma série de transformações em blocos de 512 bits. A mensagem de entrada é expandida para uma sequência de 64 palavras de 32 bits, designadas como $W_t$. O processamento de cada bloco envolve 64 rodadas de funções de compressão que atualizam oito variáveis de estado, de $a$ a $h$.

As operações lógicas fundamentais e as equações de atualização de estado são definidas conforme as expressões abaixo. Todas as adições são realizadas em aritmética modular $2^{32}$.

| Função | Expressão Matemática |
| :--- | :--- |
| **Escolha (Ch)** | $Ch(e, f, g) = (e \land f) \oplus (\neg e \land g)$ |
| **Maioria (Maj)** | $Maj(a, b, c) = (a \land b) \oplus (a \land c) \oplus (b \land c)$ |
| **Rotação Sigma 0 ($\Sigma_0$)** | $\Sigma_0(a) = ROTR^{2}(a) \oplus ROTR^{13}(a) \oplus ROTR^{22}(a)$ |
| **Rotação Sigma 1 ($\Sigma_1$)** | $\Sigma_1(e) = ROTR^{6}(e) \oplus ROTR^{11}(e) \oplus ROTR^{25}(e)$ |
| **Expansão Sigma 0 ($\sigma_0$)** | $\sigma_0(W_t) = ROTR^{7}(W_t) \oplus ROTR^{18}(W_t) \oplus SHR^{3}(W_t)$ |
| **Expansão Sigma 1 ($\sigma_1$)** | $\sigma_1(W_t) = ROTR^{17}(W_t) \oplus ROTR^{19}(W_t) \oplus SHR^{10}(W_t)$ |

As variáveis de estado são atualizadas em cada rodada através das constantes $K_t$ e das variáveis temporárias $T_1$ e $T_2$:
- $T_1 = h + \Sigma_1(e) + Ch(e, f, g) + K_t + W_t$
- $T_2 = \Sigma_0(a) + Maj(a, b, c)$
- A nova configuração de estado segue a transição: $h=g, g=f, f=e, e=d+T_1, d=c, c=b, b=a, a=T_1+T_2$.

No contexto da mineração, o objetivo é identificar um valor pseudoaleatório de 32 bits (nonce) tal que o resultado da função hash dupla do cabeçalho do bloco seja inferior a um valor alvo predefinido: $SHA256(SHA256(Block\_Header)) < Target$. O número esperado de operações para atingir esta condição é dado por $2^B$, onde $B$ representa o parâmetro de dificuldade.

---

## 2. Arquitetura de Circuitos Integrados de Aplicação Específica (ASIC)

A evolução do hardware de mineração, liderada por figuras como Micree Zhan e N.G. Zhang, focou na transição de FPGAs para ASICs altamente otimizados. A arquitetura técnica destes chips prioriza o paralelismo massivo e a redução do caminho crítico em operações de adição.

### 2.1 Otimização de Pipeline e Caminho Crítico
As implementações de alto desempenho utilizam arquiteturas de pipeline de múltiplos estágios (frequentemente 3 estágios). A inserção estratégica de Flip-Flops (FFs) de 32 bits permite isolar as unidades de cálculo de rodada, permitindo que o chip opere em frequências mais elevadas. Em tecnologias de 14nm, esta abordagem demonstrou um aumento de throughput de 300% com uma redução de 50.7% no consumo energético por operação, apesar de um incremento de 2.9 vezes na área total do silício.

### 2.2 Gestão de Energia e Frequência Dinâmica
A eficiência energética é maximizada através de técnicas como a modulação dinâmica de frequência via Phase-Locked Loops (PLLs), com degraus de ajuste entre 1% e 10%. Adicionalmente, o emprego de *clock gating* permite desativar circuitos que processam dados constantes após a iteração inicial, otimizando o consumo estático e dinâmico do hardware.

---

## 3. Especificações Técnicas de Dispositivos e Semicondutores

A tabela abaixo compila as métricas de desempenho e especificações físicas dos principais dispositivos desenvolvidos pelos autores citados, abrangendo diferentes gerações tecnológicas e processos de fabricação.

| Dispositivo | Autor/Empresa | Processo | Hash Rate | Consumo | Eficiência |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Antminer S1** | Zhan/Wu | 130/65nm | 180 GH/s | 360 W | 2.00 W/GH/s |
| **Antminer S19 Pro** | Zhan/Zhu | 7nm | 110 TH/s | 3250 W | 0.029 J/GH |
| **Avalon Icarus** | N.G. Zhang | 45nm | 380 MH/s | 19.2 W | 50.52 J/GH |
| **BFL Jalapeno** | Zerlan/Vleisides | 65nm | 5 GH/s | 30 W | 6.00 W/GH/s |
| **BFL Monarch** | Ghoseiri/Ownby | 28nm | 600 GH/s | 350 W | 0.58 W/GH/s |

### 3.1 Geometria e Física do Die (Chip BFSC100F144)
O chip BFSC100F144, representativo da primeira geração de ASICs da Butterfly Labs, apresenta um die com dimensões aproximadas de 7610 μm x 7520 μm, totalizando uma área de 57.22 mm². A metalização utiliza um processo de múltiplas camadas, com uma camada superior espessa de alumínio para distribuição de energia e camadas inferiores de cobre para sinalização. O encapsulamento é do tipo Ball Grid Array (BGA) de 144 pinos com passo de 0.8mm, utilizando substrato de poliimida.

---

## 4. Estrutura de Dados e Constantes de Sistema

O processamento SHA-256 utiliza 64 constantes de 32 bits ($K_t$), derivadas dos primeiros 32 bits das partes fracionárias das raízes cúbicas dos primeiros 64 números primos. O cabeçalho do bloco de Bitcoin, que serve como entrada para o hardware, possui uma estrutura rígida de 80 bytes (640 bits) antes do preenchimento:

- **Versão:** 4 bytes
- **Hash do Bloco Anterior:** 32 bytes
- **Raiz Merkle:** 32 bytes
- **Timestamp:** 4 bytes
- **Bits (Dificuldade):** 4 bytes
- **Nonce:** 4 bytes

A mensagem é preenchida até atingir 1024 bits para satisfazer os requisitos de entrada do algoritmo de compressão em blocos.
