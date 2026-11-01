# Suplemento: Otimizações Matemáticas de ASIC para Mineração Bitcoin

---

## §A1 ARQUITETURA DE PIPELINE SHA-256

### A1.1 Modelo de Pipeline de 3 Estágios

**Estágio 1:** Expansão de Mensagem ($W_t$)
$$W_t = \sigma_1(W_{t-2}) \boxplus W_{t-7} \boxplus \sigma_0(W_{t-15}) \boxplus W_{t-16}$$

**Estágio 2:** Cálculo de $T_1$
$$T_1 = h \boxplus \Sigma_1(e) \boxplus \text{Ch}(e,f,g) \boxplus K_t \boxplus W_t$$

**Estágio 3:** Cálculo de $T_2$ e Atualização de Estado
$$T_2 = \Sigma_0(a) \boxplus \text{Maj}(a,b,c)$$
$$\mathbf{S}_{t+1} = f(\mathbf{S}_t, T_1, T_2)$$

### A1.2 Throughput vs Latência

**Sem pipeline:**
$$\text{Throughput} = \frac{1}{64 \cdot \tau_{\text{round}}}$$

**Com pipeline de $n$ estágios:**
$$\text{Throughput} = \frac{1}{\tau_{\text{stage}}} = \frac{n}{64 \cdot \tau_{\text{round}}}$$

**Latência:**
$$L_{\text{pipeline}} = 64 + (n - 1) \text{ ciclos}$$

### A1.3 Ganho de Throughput (14nm)

$$\text{Ganho} = 300\%$$

$$\text{Redução de energia/op} = 50.7\%$$

$$\text{Aumento de área} = 2.9\times$$

### A1.4 Frequência Máxima de Operação

$$f_{\max} = \frac{1}{\tau_{\text{crítico}} + \tau_{\text{setup}} + \tau_{\text{hold}}}$$

**Caminho crítico em SHA-256:**
$$\tau_{\text{crítico}} = \tau_{\text{add32}} + \tau_{\text{xor}} + \tau_{\text{mux}}$$

---

## §A2 OTIMIZAÇÃO DE ADIÇÃO MODULAR

### A2.1 Carry-Save Adder (CSA)

**Representação redundante:**
$$(S, C) = \text{CSA}(A, B, C_{\text{in}})$$

$$S_i = A_i \oplus B_i \oplus C_{\text{in},i}$$
$$C_{i+1} = \text{Maj}(A_i, B_i, C_{\text{in},i})$$

**Atraso:** $O(1)$ vs $O(\log n)$ para CLA

### A2.2 Cadeia de Adições em $T_1$

$$T_1 = ((((h \boxplus \Sigma_1(e)) \boxplus \text{Ch}) \boxplus K_t) \boxplus W_t)$$

**Com CSA (5 operandos):**
$$(S_1, C_1) = \text{CSA}(h, \Sigma_1(e), \text{Ch})$$
$$(S_2, C_2) = \text{CSA}(S_1, C_1, K_t)$$
$$(S_3, C_3) = \text{CSA}(S_2, C_2, W_t)$$
$$T_1 = S_3 + C_3 \text{ (CLA final)}$$

**Redução de atraso:**
$$\tau_{\text{CSA chain}} = 3\tau_{\text{CSA}} + \tau_{\text{CLA}} < 5\tau_{\text{CLA}}$$

### A2.3 Carry-Lookahead em Blocos

**Geração e Propagação:**
$$G_i = A_i \land B_i$$
$$P_i = A_i \oplus B_i$$

**Carry de bloco (4 bits):**
$$C_4 = G_3 + P_3G_2 + P_3P_2G_1 + P_3P_2P_1G_0 + P_3P_2P_1P_0C_0$$

---

## §A3 CONFIGURAÇÃO DE PLL

### A3.1 Fórmula Geral de PLL

$$f_{\text{VCO}} = f_{\text{REF}} \times \frac{\text{FBDIV}}{\text{REFDIV}}$$

$$\boxed{f_{\text{OUT}} = \frac{f_{\text{REF}} \times \text{FBDIV}}{\text{REFDIV} \times \text{POSTDIV1} \times \text{POSTDIV2}}}$$

### A3.2 Restrições de Configuração

$$60 \leq \text{FBDIV} \leq 160$$
$$1 \leq \text{REFDIV} \leq 63$$
$$1 \leq \text{POSTDIV1} \leq 7$$
$$1 \leq \text{POSTDIV2} \leq 7$$
$$\text{POSTDIV1} \geq \text{POSTDIV2}$$

### A3.3 Tabela de Configurações (BM1385, $f_{\text{REF}} = 25$ MHz)

| PLLDiv1 | PLLDiv2 | FBDIV | POSTDIV1 | POSTDIV2 | $f_{\text{OUT}}$ (MHz) |
|:-------:|:-------:|:-----:|:--------:|:--------:|:----------------------:|
| 0x20040 | 0x420 | 32 | 4 | 1 | 100 |
| 0x40040 | 0x420 | 64 | 4 | 1 | 200 |
| 0x60040 | 0x420 | 96 | 4 | 1 | 300 |
| 0x80040 | 0x420 | 128 | 4 | 1 | 400 |
| 0x60040 | 0x220 | 96 | 2 | 1 | 600 |
| 0x80040 | 0x220 | 128 | 2 | 1 | 800 |
| 0x50040 | 0x120 | 80 | 1 | 1 | 1000 |

### A3.4 Exemplo de Cálculo

Para $f_{\text{OUT}} = 400$ MHz:
$$f_{\text{OUT}} = \frac{25 \times 128}{2 \times 4 \times 1} = \frac{3200}{8} = 400 \text{ MHz}$$

---

## §A4 RELAÇÃO HASH RATE VS FREQUÊNCIA

### A4.1 Modelo Linear

$$\boxed{H = f \times K}$$

onde $K$ é constante específica do design (hashes/ciclo)

### A4.2 BM1384

$$H(\text{GH/s}) = f(\text{MHz}) \times 0.055$$

| $f$ (MHz) | $H$ (GH/s) | Reg. Value |
|:---------:|:----------:|:----------:|
| 100 | 5.50 | 0x0783 |
| 200 | 11.00 | 0x0782 |
| 300 | 16.50 | 0x0b82 |
| 400 | 22.00 | 0x08f2 |

### A4.3 Verificação

$$H_{400} = 400 \times 0.055 = 22.00 \text{ GH/s} \quad \checkmark$$

---

## §A5 EFICIÊNCIA VS TENSÃO

### A5.1 Modelo Empírico (BM1384)

| $V$ (V) | $H$ (GH/s) | $I$ (A) | $P$ (W) | $\varepsilon$ (W/GH) |
|:-------:|:----------:|:-------:|:-------:|:--------------------:|
| 0.60 | 8.25 | 3.43 | 2.058 | 0.249 |
| 0.65 | 11.00 | 4.46 | 2.899 | 0.264 |
| 0.70 | 13.75 | 6.60 | 4.620 | 0.336 |
| 0.72 | 15.13 | 7.44 | 5.357 | 0.354 |
| 0.75 | 17.88 | 9.20 | 6.900 | 0.386 |
| 0.80 | 22.00 | 12.31 | 9.848 | 0.448 |

### A5.2 Análise de Escalamento

$$\Delta V = 0.80 - 0.60 = 0.20 \text{ V} \quad (+33\%)$$
$$\Delta H = 22.00 - 8.25 = 13.75 \text{ GH/s} \quad (+167\%)$$
$$\Delta P = 9.848 - 2.058 = 7.79 \text{ W} \quad (+379\%)$$

**Conclusão:** $P$ cresce mais rápido que $H$ → eficiência piora com $V$ alto

### A5.3 Modelo de Potência

$$\boxed{\varepsilon \propto V^\beta, \quad \beta \approx 2.5 - 3.0}$$

**Normalizado ($V_{\text{ref}} = 0.60$ V):**

$$\varepsilon_{\text{norm}} = \left(\frac{V}{V_{\text{ref}}}\right)^\beta$$

| $V_{\text{norm}}$ | $\varepsilon_{\text{norm}}$ |
|:-----------------:|:---------------------------:|
| 1.00 | 1.00 |
| 1.08 | 1.06 |
| 1.17 | 1.35 |
| 1.25 | 1.55 |
| 1.33 | 1.80 |

### A5.4 Potência CMOS

$$\boxed{P_{\text{dynamic}} = \alpha C V^2 f}$$

$$P_{\text{static}} = I_{\text{leak}} \cdot V$$

$$P_{\text{total}} = \alpha C V^2 f + I_{\text{leak}} V$$

---

## §A6 ASICBOOST (CN105245327A)

### A6.1 Princípio de Otimização

**Estrutura do segundo bloco (chunk 2):**
$$\text{Chunk2} = \text{MerkleRoot}[224:255] \parallel \text{Time} \parallel \text{nBits} \parallel \text{Nonce} \parallel \text{Padding}$$

### A6.2 Compartilhamento de Expansão

Quando $N$ midstates têm **mesmo** $\text{MerkleRoot}[224:255]$:

$$\boxed{\text{Redução de potência} = \frac{N-1}{N}}$$

$$\boxed{\text{Redução de circuito} = \frac{N-1}{N}}$$

| $N$ | Redução de Potência | Redução de Área |
|:---:|:-------------------:|:---------------:|
| 2 | 50% | 50% |
| 4 | 75% | 75% |
| 8 | 87.5% | 87.5% |

### A6.3 Probabilidade de Colisão (32 bits baixos)

Para $2^{34}$ computações de MerkleRoot:

$$E[\text{colisões por grupo}] \approx \frac{2^{34}}{2^{32}} = 4$$

### A6.4 Arquitetura do Circuito

```
Midstate₁ ──→ Compressor₁ ──┐
Midstate₂ ──→ Compressor₂ ──┼──→ Expansor ──→ Operação ──→ Hash
    ...           ...       │    Compartilhado
Midstateₙ ──→ Compressorₙ ──┘
```

### A6.5 Ganho Teórico

$$\text{Fração de trabalho no Expansor} = p \approx 25\%$$

$$\boxed{\text{Ganho máximo} = p \times \left(1 - \frac{1}{n}\right) \approx 20-25\%}$$

---

## §A7 EARLY ABORT

### A7.1 Condição de Aborto

Durante cálculo de $H_2$, se:

$$H_2[0:k-1] \neq 0^k$$

onde $k$ = número de leading zeros requeridos pelo target:

$$\text{ABORTAR (impossível satisfazer } H_2 < T\text{)}$$

### A7.2 Economia de Operações

**Rodadas economizadas (em média):**

$$E[\text{rodadas economizadas}] = 64 \times \left(1 - 2^{-k}\right) \approx 64$$

### A7.3 Implementação por Rodada

Após rodada $r$, verificar bits MSB do estado:

$$\text{Se } a[0:k-1] \neq 0^k \implies \text{abort}$$

---

## §A8 MIDSTATE OPTIMIZATION

### A8.1 Estrutura do Block Header (80 bytes)

**Chunk 1 (bytes 0-63):** Version + PrevHash + MerkleRoot[0:223]

**Chunk 2 (bytes 64-79):** MerkleRoot[224:255] + Time + nBits + Nonce

### A8.2 Computação Incremental

**Midstate (fixo para mesmo bloco):**
$$\mathbf{S}_{\text{mid}} = \text{SHA256}_{\text{compress}}(H^{(0)}, \text{Chunk1})$$

**Variação apenas em Chunk2:**
$$H_1 = \text{SHA256}_{\text{compress}}(\mathbf{S}_{\text{mid}}, \text{Chunk2(Nonce)})$$

### A8.3 Economia de Operações

$$\text{Operações por hash} = 64 \text{ (Chunk2)} + 64 \text{ (SHA2)} = 128$$

vs.

$$\text{Sem midstate} = 64 \text{ (Chunk1)} + 64 \text{ (Chunk2)} + 64 \text{ (SHA2)} = 192$$

$$\boxed{\text{Economia} = \frac{192 - 128}{192} = 33\%}$$

---

## §A9 CLOCK GATING

### A9.1 Princípio

Desativar clock para circuitos com dados constantes:

$$P_{\text{gated}} = P_{\text{dynamic}} \times (1 - \text{gating\_ratio})$$

### A9.2 Aplicação em SHA-256

**Constantes ($K_t$):** Após primeira iteração, valores fixos

**Padding:** Sempre constante para mesmo tamanho de mensagem

### A9.3 Economia Estimada

$$\text{gating\_ratio} \approx 10-15\%$$

$$\text{Redução de potência dinâmica} \approx 10-15\%$$

---

## §A10 ESCALAMENTO DE PROCESSO

### A10.1 Lei de Dennard (Scaling Clássico)

| Parâmetro | Fator de Escala ($\kappa$) |
|:----------|:--------------------------:|
| Dimensões | $1/\kappa$ |
| Tensão | $1/\kappa$ |
| Corrente | $1/\kappa$ |
| Delay | $1/\kappa$ |
| Potência | $1/\kappa^2$ |
| Densidade de potência | 1 (constante) |

### A10.2 Evolução Real de Eficiência

| Processo | $\varepsilon$ (W/GH) | Melhoria vs Anterior |
|:--------:|:--------------------:|:--------------------:|
| 110nm | 9.2 | — |
| 28nm | 0.354 | 96.2% |
| 16nm | 0.098 | 72.3% |
| 7nm | 0.037 | 62.2% |
| 5nm | 0.0215 | 41.9% |
| ~2nm | 0.0128 | 40.5% |

### A10.3 Modelo Empírico

$$\boxed{\varepsilon \propto (\text{processo}_{\text{nm}})^\gamma, \quad \gamma \approx 1.2 - 1.5}$$

### A10.4 Rendimentos Decrescentes

$$\text{Melhoria}_{n \to n/2} < \text{Melhoria}_{2n \to n}$$

---

## §A11 METODOLOGIA FULL CUSTOM (Yang Zuoxing)

### A11.1 Ganho de Performance

$$\boxed{G_{\text{design}} \approx 2.0 \times}$$

(dobro de performance no mesmo processo)

### A11.2 Técnicas

1. **Registradores Multi-bit:** Redução de clock tree
2. **Posicionamento Manual:** Minimização de comprimento de fios
3. **Células Customizadas:** Otimização para baixa tensão

### A11.3 Resultados Reais (Tan Shuai, MicroBT)

| Processo | Tensão (V) | Eficiência | Algoritmo |
|:--------:|:----------:|:----------:|:---------:|
| TSMC 28nm | 0.45 | 257 J/T | Blake2b |
| TSMC 16nm | 0.38 | 65 J/T | SHA-256d |
| TSMC 7nm | 0.30 | 37 J/T | SHA-256d |
| SMIC N+1 | 0.30 | 35 J/T | SHA-256d |

### A11.4 Fórmula de Ganho Combinado

$$\boxed{G_{\text{total}} = G_{\text{processo}} \times G_{\text{design}} \times G_{\text{arquitetura}}}$$

**Exemplo (28nm → 16nm + Full Custom):**
$$G_{\text{total}} = 1.75 \times 2.0 \times 1.15 = 4.025\times$$

---

## §A12 ESPECIFICAÇÕES ELÉTRICAS

### A12.1 Limites Absolutos (BM1384/BM1385)

$$V_{\text{DD(max)}} = 1.2 \text{ V}$$
$$V_{\text{CC(max)}} = 1.98 \text{ V}$$
$$T_{\text{storage}} = -65°\text{C} \text{ a } 150°\text{C}$$

### A12.2 Condições de Operação Recomendadas

$$V_{\text{DD}}: 0.60 \text{ V} \leq 0.66 \text{ V (typ)} \leq 0.80 \text{ V}$$
$$V_{\text{IO}}: 1.62 \text{ V} \leq 1.80 \text{ V (typ)} \leq 1.98 \text{ V}$$
$$T_{\text{op}}: 0°\text{C} \leq 25°\text{C (typ)} \leq 125°\text{C}$$

### A12.3 Características DC

| Parâmetro | Mín | Típico | Máx | Unidade |
|:----------|:---:|:------:|:---:|:-------:|
| $V_{\text{IL}}$ | -0.3 | — | 0.63 | V |
| $V_{\text{IH}}$ | 1.17 | — | 1.98 | V |
| $V_{\text{OL}}$ | — | — | 0.45 | V |
| $V_{\text{OH}}$ | 1.35 | — | — | V |
| $I_L$ | — | — | ±10 | µA |
| $R_{\text{PU}}$ | 47 | 69 | 106 | kΩ |
| $R_{\text{PD}}$ | 49 | 85 | 159 | kΩ |
| $C_{\text{IN}}$ | — | 10 | — | pF |

---

## §A13 PROTOCOLO DE COMUNICAÇÃO (UART)

### A13.1 Configuração

$$\text{Baud Rate} = 115200 \text{ @ } f_{\text{XIN}} = 25 \text{ MHz}$$

$$\text{Bit Order} = \text{LSB first}$$

### A13.2 Formato de Trabalho (64 bytes)

| Bytes | Campo | Descrição |
|:-----:|:------|:----------|
| 0-31 | Midstate | Estado intermediário |
| 32-35 | Ignore | — |
| 36-39 | Ticket Mask | Máscara de dificuldade |
| 40-43 | HCN | Hash Counting Number |
| 44-47 | SNO | Start Nonce Offset |
| 48-50 | Ignore | — |
| 51 | WC | Work Count |
| 52-63 | Data2 | Dados do segundo bloco |

### A13.3 Formato de Resposta (5 bytes)

| Bytes | Campo |
|:-----:|:------|
| 0-3 | Nonce encontrado |
| 4 | Bit[7]=1, Bit[6:0]=WorkCount |

---

## §A14 EVOLUÇÃO DE CHIPS BITMAIN

### A14.1 Especificações por Geração

| Chip | Processo | Ano | $\varepsilon$ (W/GH) | Melhoria |
|:-----|:--------:|:---:|:--------------------:|:--------:|
| BM1380 | 55nm | 2013 | 0.350 | — |
| BM1382 | 28nm | 2014 | 0.175 | 50% |
| BM1384 | 28nm | 2014 | 0.090 | 49% |
| BM1385 | 28nm | 2015 | 0.216 | — |
| BM1387 | 16nm | 2016 | 0.098 | 55% |
| BM1391 | 7nm | 2018 | 0.042 | 57% |
| BM1397 | 7nm | 2019 | 0.030 | 29% |
| BM1398 | 7nm | 2020 | 0.0295 | 2% |

### A14.2 Especificações Antminer S9 (BM1387)

$$\text{Chips} = 189 \quad (3 \text{ placas} \times 63 \text{ chips})$$
$$H_{\text{total}} = 13.5 \text{ TH/s}$$
$$P_{\text{total}} = 1300 \text{ W}$$
$$\varepsilon_{\text{S9}} = \frac{1300}{13500} = 0.096 \text{ W/GH}$$

**Por chip:**
$$H_{\text{chip}} = \frac{13500}{189} = 71.43 \text{ GH/s}$$
$$P_{\text{chip}} = \frac{1300}{189} = 6.88 \text{ W}$$

---

## §A15 EQUAÇÕES FUNDAMENTAIS DE OTIMIZAÇÃO ASIC

### A15.1 Eficiência Energética

$$\boxed{\varepsilon = \frac{P}{H} = \frac{V \times I}{H} \quad [\text{W/GH ou J/TH}]}$$

### A15.2 Hash Rate do Sistema

$$\boxed{H_{\text{total}} = N_{\text{chips}} \times H_{\text{chip}}}$$

### A15.3 Frequência de Saída PLL

$$\boxed{f_{\text{OUT}} = \frac{f_{\text{REF}} \times \text{FBDIV}}{\text{REFDIV} \times \text{POSTDIV1} \times \text{POSTDIV2}}}$$

### A15.4 Potência CMOS

$$\boxed{P = \alpha C V^2 f + I_{\text{leak}} V}$$

### A15.5 Ganho Total de Design

$$\boxed{G_{\text{total}} = G_{\text{processo}} \times G_{\text{design}} \times G_{\text{arquitetura}}}$$

### A15.6 Economia AsicBoost

$$\boxed{\text{Ganho} = p \times \left(1 - \frac{1}{N}\right) \approx 20\%}$$

### A15.7 Economia Midstate

$$\boxed{\text{Economia} = \frac{64}{192} = 33\%}$$

---

**FIM DO SUPLEMENTO DE OTIMIZAÇÕES ASIC**

*Fontes: Patentes CN105245327A, CN105045364A, Datasheets BM1384 v2.1, BM1385 v2.0, BM1387, Full Custom ASIC Design Secrets (Tan Shuai)*
