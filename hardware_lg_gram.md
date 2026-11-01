Compêndio Matemático Integrado: Conceitos e Equações
1. Arquitetura x86-64
1.1 Pipeline de Processamento
$T_{\mathrm{total}}=N\times CPI\times T_{\mathrm{clock}}$
Onde:
* $N=$ número de instruções
* $CPI=$ ciclos por instrução
* $T_{clock}=$ período do relógio
1.2 Hierarquia de Cache
- $h$ = taxa de acerto L1
- $m$ = taxa de acerto L2
- $T_{L1}, T_{\text{mem}}, T_{\text{miss}}$ = latências
3 Largura de Banda
$BW=\frac{\textrm{bits transferidos}}{\textrm{tempo}}=f\times w\times n$
Onde:
*   *f* = frequência do relógio
*   *w* = largura do barramento
*   *n* = número de transferências por ciclo

## 1.4 Consumo de Potência

P = C × V² × f + P<sub>leak</sub>

Onde:

*   *C* = capacitância
*   *V* = tensão
*   *f* = frequência
*   *P<sub>leak</sub>* = potência de fuga
Onde:
2. Arquitetura ARM
2.1 Eficiência Energética
$\eta=\frac{\textbf{FLOPS}}{W}=\frac{f\times n_{\textbf{cores}}\times IPC}{P_{\textbf{total}}}$
**Onde:**
2.2 Throughput de Processamento
$T=f\times IPC\times n_{\mathrm{core}}$
2.3 Latência de Operação
# de Operação

$L = \frac{\text{profundidade do pipeline}}{\text{frequência}} + \text{latência de memória}$
2.4 Razão de Performance ARM vs x86
$$\frac{P_{\mathrm{ARM}}}{P_{\mathrm{x86}}}=\frac{IPC_{\mathrm{ARM}}\times f_{\mathrm{ARM}}}{IPC_{\mathrm{x86}}\times f_{\mathrm{x86}}}\times\frac{1}{\mathrm{overhead}_{\mathrm{x86}}}$$
3. Google Axion (TPU Architecture)
3.1 Throughput de Tensor
$T_{\text{tensor}}=f\times\text{unidades de compute}\times\text{operações por unidade por ciclo}$
3.2 Largura de Banda da Memória HBM
BW<sub>HBM</sub>=f<sub>mem</sub>×bits por pin×pins10<sup>9</sup>
Unidades: GB/s
3 Eficiência de Utiliz
$\eta_{\mathrm{util}}=\frac{\mathrm{opera\c{c}\~oes\ realizadas}}{\mathrm{opera\c{c}\~oes\ m\'aximas\ poss\'iveis}}\times100\%$
3.4 Latência Agregada
$$=L_{\mathrm{compute}}+L_{\mathrm{comunica\~ao}}+L_{\mathrm{sincroniza\~ao}}$$
3.5 Escalabilidade Horizontal
$S=\frac{T_{\mathrm{N\,n\,o\,s}}}{T_{1\,\mathrm{n\,o}}} \leq N$
Eficiência: $E=\frac{S}{N}\times100\%$
4. Samsung Galaxy S25 Hardware
4.1 Densidade de Pixels
$PPI=\sqrt{w^{2}+h^{2}}/d$
Onde:
* $w,h=$ resolução horizontal e vertical
* $d=$ diagonal da tela em polegadas
4.2 Consumo de Energia em Display
$P_{\mathrm{display}}=\mathrm{pixels}\times I_{\mathrm{pixel}}\times V_{\mathrm{supply}}$
4.3 Capacidade de Bateria
$E_{\mathrm{bateria}}=Q\times V_{\mathrm{nominal}}$
Onde:
$t=\frac{E_{\text{bateria}}}{P_{\text{mé dia}}}$
mé dia = consumo médio em carga típica
quência de Atualização
$f_{\mathrm{refresh}}=\frac{1}{T_{\mathrm{frame}}}
Onde $T_{\text{frame}}$ = tempo entre frames
5. TPU Pod Architecture
**Matriz Sistólica de Multiply-Accumulate**
$Y=A\times W+B$
Onde operações são realizadas em paralelo em $n \times n$ PEs (Processing Elements),
2 Throughput Máxim
T_{\mathrm{max}}=n^{2}\times f\times2~(\mathrm{FMA~por~ciclo})
Onde:
*   $n=$ dimensão da matriz sistólica
*   $f=$ frequência de operação
$E_{\mathrm{op}}=\frac{P_{\mathrm{total}}}{T_{\mathrm{max}}}$
Unidades: pJ/operação
5.4 Eficiência de Memória
$\texttt{Roofline}_{\texttt{compute}}=\operatorname*{min}\left(\texttt{peak~FP32},\frac{\textit{BW}\times\texttt{operações~por~byte}}{1}\right)$
5.5 Modelo Roofline
Onde I = intensidade aritmética (operações/byt
6. Criptografia e Segurança
6.1 SHA-256
Função de compressão:
$$T_{1}=H+\Sigma_{1}(E)+Ch(E,F,G)+K_{t}+W_{t}$$

$$T_{2}=\Sigma_{0}(A)+Maj(A,B,C)$$

$$H^{\prime}=T_{1}\pm T_{2}$$
Onde:
- $\Sigma_{1}(\boldsymbol{x}) = (\boldsymbol{x}\ggg 6)\oplus(\boldsymbol{x}\ggg 11)\oplus(\boldsymbol{x}\ggg 25)$
- $\Sigma_{0}(\boldsymbol{x}) = (\boldsymbol{x}\ggg 2)\oplus(\boldsymbol{x}\ggg 13)\oplus(\boldsymbol{x}\ggg 22)$
- $Ch(\boldsymbol{x},\boldsymbol{y},z) = (\boldsymbol{x}\wedge\boldsymbol{y})\oplus(\neg\boldsymbol{x}\wedge z)$
- $Maj(\boldsymbol{x},\boldsymbol{y},z) = (\boldsymbol{x}\wedge\boldsymbol{y})\oplus(\boldsymbol{x}\wedge z)\oplus(\boldsymbol{y}\wedge z)$
6.2 Operações Booleanas

Rotação circular:
$x\gg n=(x>>n)||(x<<32-n))$
Deslocamento circular à direita por n posições em 32 bits.
6.3 Constantes SHA-256
$K_{0},K_{1},\ldots,K_{63}$
6.4 Expansão de Mensagem
$c=m^{e}{\bmod{N}}$

$m=c^{d}{\bmod{N}}$
Onde:
6.6 ECC (Curva Elíptica)
Operação de adição de pontos
$P + Q = R$

Onde $P$, $Q$, $R$ são pontos na curva $y^2 = x^3 + ax + b$

Multiplicação escalar:
$[k]P=P+P+\ldots+P\;({\mathrm{k~vezes}})$
# 6.7 Função de Hash Iterada

H<sub>i</sub> = f(H<sub>i-1</sub>, M<sub>i</sub>)

Hash = H<sub>N</sub>

# 7. Mineração de Criptomoedas
7.1 Função de Trabalho (Proof of Work)
$H(\text{block header})<\text{target}$
Onde $H$ é uma função de hash criptográfica (e.g., SHA-256).

**7.2 Dificuldade de Rede**
7.3 Taxa de Has
Unidades: H/s, MH/s, GH/s, TH/s, PH/s, EH/s
7.4 Probabilidade de Encontrar Bloco
$P\equiv1-e^{-\lambda t}$
Onde:

*   λ = hashrate / 2^256 (para Bitcoin)
*   t = tempo de tentativa

7.5 Recompensa Esperada

R = hashrate total network / hashrate minerador × recompensa por bloco
7.6 Eficiência Energética (J/TH)
$\eta=\frac{W}{TH/s}$
Onde $W=$ watts consumidos
7.7 ROI (Return on Investment)
ROI = $\frac{\text{receita} - \text{custos}}{\text{investimento inicial}} \times 100\%$
Halving de Recomp
$R_{\mathrm{novo}}=\frac{R_{\mathrm{anterior}}}{2}$
Ocorre a cada 210.000 blocos (aproximadamente
8. RAP1 (Tecnologia e Criptografia)
8.1 Estrutura de Dados

Conversão binária:
$N_{10}=\sum_{i=0}^{n-1}\boldsymbol{b}_{i}\times\boldsymbol{2}^{i}$
Onde $b_{i}\in\{0,1\}$
8.2 Análise de Padrões

Frequência relativa:
$f_{i}=\frac{n_{i}}{N}$
e $n_{i}=$ contagem e $N=$ total
8.3 Variância
$\sigma^{2}={\frac{1}{N}}\sum_{i=1}^{N}(x_{i}-\mu)^{2}$
Onde $\boldsymbol{\mu} = \frac{1}{N}\sum_{i=1}^{N}\boldsymbol{x}_{i}$

**8.4 Desvio Padrão**
$\sigma=\sqrt{\sigma^{2}}$
8.5 Coeficiente de Variação
8.6 Entropia de Shannon
$H=-\sum_{i=1}^{n}p_{i}\log_{2}(p_{i})$
Onde $p_{i}=$ probabilidade do símbolo $i$
$D_{KL}(P||Q)=\sum_{i}p_{i}\log$
$\left(\frac{p_{i}}{q_{i}}\right)$
Onde $P$ e $Q$ são distribuições de probabilidade

**8.8 Teste de Chi-quadrado**
$\chi^{2}=\sum_{i=1}^{k}\frac{\left(O_{i}-E_{i}\right)^{2}}{E_{i}}$
Onde:
* $O_{i}$ = frequência observada
* $E_{i}$ = frequência esperada
8.9 Correlação de Pearson
$r=\frac{\sum_{i=1}^{n}(x_{i}-\mu_{x})(y_{i}-\mu_{y})}{\sqrt{\sum_{i=1}^{n}(x_{i}-\mu_{x})^{2}}\sqrt{\sum_{i=1}^{n}(y_{i}-\mu_{y})^{2}}}$
8.10 Autocorrelação
$\rho(k)=\frac{\sum_{t=1}^{n-k}(x_{t}-\mu)(x_{t+k}-\mu)}{\sum_{t=1}^{n}(x_{t}-\mu)^{2}}$
Onde $k = \text{lag}$
8.11 Distribuição Normal
$f(x)=\frac{1}{\sigma{\sqrt{2\pi}}}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}}$
8.12 Teste de Kolmogorov-Smirnov
$D=\operatorname*{max}_{x}|F_{n}(x)-F(x)|$
Onde:
* $F_{n}(\boldsymbol{x})=$ função de distribuição empírica
* $F(\boldsymbol{x})=$ função de distribuição teórica
8.13 Transformada de Fourier Discreta (DFT)
$X_{k}=\sum_{n=0}^{N-1}\boldsymbol{x}_{n}e^{-i2\pi kn/N}$
$\mathrm{Onde}\;k=0,1,\ldots,N-1$
8.14 Transformada de Fourier Rápida (FFT)

$$T_{\text{FFT}} = O(N \log N)$$
Versus DFT: $T_{\mathrm{DFT}}=O(N^{2})$
# 8.15 Densidade Espectral de Potência

$$S(f) = |X(f)|^2$$
8.16 Análise Espectral

Periodograma:
3.17 Regressão Linear
8.18 Coeficiente de Determinação
$R^{2}=1-\frac{\sum_{i=1}^{n}(y_{i}-\hat{y}_{i})^{2}}{\sum_{i=1}^{n}(y_{i}-\overline{{y}})^{2}}$
8.19 Erro Quadrático Médio (MSE)
$MSE=\frac{1}{n}\sum_{i=1}^{n}(y_{i}-\hat{y}_{i})^{2}$
8.20 Raiz do Erro Quadrático Médio (RMSE)

$$RMSE = \sqrt{MSE}$$
8.21 Erro Absoluto Médio (MAE)
MAE = 1/n Σ^n_i |y_i - ŷ_i|

8.22 Intervalo de Confiança

CI = x ± zα/2 σ / √n
Onde $z_{\alpha/2}$ é o valor crítico da distribuição normal padrão
**8.23 Valor-p (p-value)**

$$p = P(\text{estatística teste} \geq \text{valor observado}|H_0\text{ verdadeiro})$$

**8.24 Teorema do Limite Central**
$\bar{X}\sim N\left(\mu,\frac{\sigma^{2}}{n}\right){\mathrm{~quando~}}n\rightarrow\infty$
8.25 Distribuição t de Student
$t=\frac{\bar{x}-\mu}{s/\sqrt{n}}$
Onde $\boldsymbol{s}=$ desvio padrão da amostra
9. Fórmulas Complementares de Processamento

9.1 Lei de Amdahl
$S=\frac{1}{(1-p)+\frac{p}{k}}$
Onde:
$S=n+(1-n)\times(1-p)$
Onde n = número de processadores
9.3 Intensidade Aritmética
I = operações em ponto flutuante / bytes de dados transferidos
Unidades: FLOP/byte
9.4 Modelo Roofline Affinitário
Performance (GFLOPS) = min (pico de compute, I × BW)
9.5 Latência de Comunicação
$L_{\mathrm{comm}}=\boldsymbol{\alpha}+\frac{\boldsymbol{\beta}\times\boldsymbol{M}}{\mathbf{B}\mathbf{W}}$
Onde:
- $\alpha$ = latência inicial
- $\beta$ = overhead
- $M$ = tamanho da mensagem
# 9.6 Taxa de Acerto de Cache (Hit Rate)

$H = \frac{\text{cache hits}}{\text{total accesses}} \times 100\%$
# 9.7 Taxa de Erro de Cache (Miss Rate)

Miss Rate = 1 - H
9.8 Tempo Médio de Acesso à Memória
$T_{\mathrm{avg}}=H\times T_{cache}+(1-H)\times T_{memory}$
9.9 Redução de Potência por Scaling
$\frac{P_{\mathrm{novo}}}{P_{\mathrm{antigo}}}=\left(\frac{V_{\mathrm{novo}}}{V_{\mathrm{antigo}}}\right)^{2}\times\frac{f_{\mathrm{novo}}}{f_{\mathrm{antigo}}}$
9.10 Frequency Scaling
$f_{max}=\frac{V_{dd}-V_{t}}{\eta\times L_{eff}}$
Onde $\eta$ é uma constante tecnológica
10. Equações de Análise Dimensional

10.1 Análise de Escalabilidade
Strong Scaling: $E_s = \frac{S}{N} = \frac{T_1}{N \times T_N}$

Weak Scaling: $E_w = \frac{T_1}{T_N}$
Onde:

*   S = speedup
*   N = número de processadores
*   T<sub>N</sub> = tempo com N processadores

10.2 Consum Específico de Potência (PUE)

PUE = P<sub>total</sub>/P<sub>IT</sub>
Onde $P_{IT}$ = potência de equipamento de TI
10.3 Fator de Utilização
$U=\frac{\text{recursos utilizados}}{\text{recursos disponí veis}}$
×100%
nda Passante Norma
BW$_{\text{norm}}=\frac{\text{BW}_{\text{efetivo}}}{\text{BW}_{\text{teórico}}}\times100\%$
11. Cálculos Binários e de Dados
11.1 Conversão Endianness
Big-endian: byte mais significativo primeiro
Little-endian: byte menos significativo primeiro
$\boldsymbol{x_{\mathrm{big}}}=\sum_{i=0}^{n-1}\boldsymbol{b}_{i}\times2^{8(n-1-i)}$
11.2 Paridade
$\mathsf{Parity}=b_{0}\oplus b_{1}\oplus\cdots\oplus b_{n-1}$
11.3 Hamming Distance
$\boldsymbol{d}_{H}(\boldsymbol{x},\boldsymbol{y})=\sum_{i=0}^{n-1}(\boldsymbol{x}_{i}\oplus\boldsymbol{y}_{i})$
Número de posições onde bits diferem
11.4 Checksum
$\text{checksum}=\sum_{i}\text{bytes}_{i}\bmod2^{16}$

$g_{i}=b_{i}\oplus b_{i+1}$
11.5 Código Gray
Onde $b$ é binário natural e $g$ é Gray
12. Modelos de Performance Computacional
# 12.1 Equação de Performance Fundamental

Time = Instructions / Clock Rate × CPI

Performance = 1 / Time
throughput vs Laten
Throughput = $\frac{\text{Work Done}}{\text{Time}}$
Latency = Time to Complete Single Task
12.3 Relação com Poder
Power = Energy × Frequency

Energy Per Task = Power / Throughput
Gargalos

$$T_{\text{total}} = T_{\text{memory}} + T_{\text{compute}} + T_{\text{communication}}$$

Bottleneck = max(T<sub>memory</sub>, T<sub>compute</sub>, T<sub>communication</sub>)
4 Análise de Gargalho
Apêndice: Notação e Constantes
Operadores Binários
*   ⊕ = XOR (exclusive or)
*   ∧ = AND
*   ∨ = OR
*   ¬ = NOT
*   ≫ = rotação circular à direita
*   >> = deslocamento à direita lógico
*   << = deslocamento à esquerda

**Unidades Comuns:**

*   FLOPS = operações em ponto flutuante por segundo
*   Hz, MHz, GHz = frequência
*   Watt (W) = potência
*   Joule (J) = energia
*   Byte (B), KB, MB, GB, TB = armazenamento
*   BPS, KBPS, MBPS, GBPS = taxa de transferência

**Constantes e Valores Típicos:**

*   Velocidade da luz: $c = 3 \times 10^8$ m/s
*   Constante de Boltzmann: $k_B = 1.38 \times 10^{-23}$ J/K
*   Temperatura ambiente: $T \approx 298$ K (25°C)