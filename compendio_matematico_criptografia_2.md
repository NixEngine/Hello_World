# COMPÊNDIO MATEMÁTICO: CRIPTOGRAFIA E CRIPTOMOEDAS

## Conceitos Fundamentais e Equações

---

# PARTE I: CRIPTOGRAFIA DE CHAVE PÚBLICA

---

## 1. Troca de Chaves Diffie-Hellman

### Equações Fundamentais

```
A = g^a mod p
B = g^b mod p
s = B^a mod p = A^b mod p
(g^a mod p)^b mod p = (g^b mod p)^a mod p
K = g^{ab} mod p
```

### Extensões

**Triple Diffie-Hellman (3-DH):**
```
K = KDF(Y^x, B^x, Y^a, X, Y, A, B)
```

**Multi-party (n partes):**
```
K = g^{abc...n} mod p
```

### Variáveis

| Símbolo | Definição |
|---------|-----------|
| p | Módulo primo |
| g | Raiz primitiva módulo p (gerador) |
| a, b | Chaves privadas |
| A, B | Chaves públicas |
| s, K | Segredo compartilhado |

---

## 2. Algoritmo RSA

### Equações de Geração de Chaves

```
n = p × q
λ(n) = lcm(p-1, q-1)
e · d ≡ 1 (mod λ(n))
d ≡ e^{-1} (mod λ(n))
```

### Equações de Criptografia/Descriptografia

```
c ≡ m^e (mod n)
m ≡ c^d (mod n)
(m^e)^d ≡ m (mod n)
```

### Assinatura Digital

```
s ≡ h(m)^d (mod n)
h(m) ≡ s^e (mod n)
```

### Otimização com Teorema Chinês do Resto

```
d_p = d mod (p-1)
d_q = d mod (q-1)
q_{inv} = q^{-1} mod p
m_1 = c^{d_p} mod p
m_2 = c^{d_q} mod q
h = q_{inv} × (m_1 - m_2) mod p
m = m_2 + h × q
```

### Variáveis

| Símbolo | Definição |
|---------|-----------|
| p, q | Primos grandes (secretos) |
| n | Módulo público |
| e | Expoente público |
| d | Expoente privado (secreto) |
| λ(n) | Função totiente de Carmichael |
| m | Mensagem |
| c | Texto cifrado |

---

## 3. Criptografia de Curvas Elípticas (ECC)

### Equação da Curva

```
y² = x³ + ax + b
```

### Curva de Edwards

```
x² + y² = 1 + dx²y²
```

### Curva Edwards25519

```
x² + y² = 1 - (121665/121666)x²y²
```

### Operação de Multiplicação Escalar

```
Q = kP
```

### ECDSA - Geração de Assinatura

```
e = HASH(m)
(x₁, y₁) = k × G
r = x₁ mod n
s = k^{-1}(z + r·d_A) mod n
```

### ECDSA - Verificação

```
u₁ = z·s^{-1} mod n
u₂ = r·s^{-1} mod n
(x₁, y₁) = u₁ × G + u₂ × Q_A
```

### Troca de Chaves ECDH

```
Segredo = AlicePubKey × BobPrivKey = BobPubKey × AlicePrivKey
```

### Variáveis

| Símbolo | Definição |
|---------|-----------|
| G | Ponto gerador (base) |
| n | Ordem do grupo |
| d_A | Chave privada |
| Q_A | Chave pública |
| k | Nonce aleatório |
| (r, s) | Assinatura |

---

## 4. Assinaturas de Schnorr

### Geração de Chave

```
y = g^x
```

### Assinatura

```
r = g^k
e = H(r || M)
s = k + xe
```

### Verificação

```
r_v = g^s · y^{-e}
e_v = H(r_v || M)
```

### Agregação de Assinaturas

```
P_{agg} = Σᵢ₌₁ⁿ Pᵢ
s_{agg} = Σᵢ₌₁ⁿ sᵢ
```

### Taproot

```
Q = P + hash(P||m)G
s·G = R + hash(R || P || m)·P
```

---

## 5. Assinaturas BLS

### Geração de Chave

```
pk = sk · g₂
```

### Assinatura

```
h = H(m)
σ = h^{sk}
```

### Verificação

```
e(σ, g₂) = e(H(m), pk)
```

### Agregação

```
σ = Aggregate(σ₁, σ₂, ..., σₖ)
e(σ, g₂) = Πᵢ₌₁ᵏ e(H(mᵢ), pkᵢ)
```

---

## 6. Compartilhamento Secreto de Shamir

### Polinômio

```
f(x) = a₀ + a₁x + a₂x² + ... + a_{k-1}x^{k-1}
```

onde `a₀ = S` (segredo)

### Interpolação de Lagrange

```
ℓⱼ(x) = Πₘ₌₀,ₘ≠ⱼ^{k-1} (x - xₘ)/(xⱼ - xₘ)

f(x) = Σⱼ₌₀^{k-1} yⱼ·ℓⱼ(x)

S = f(0) = Σⱼ₌₀^{k-1} yⱼ · Πₘ₌₀,ₘ≠ⱼ^{k-1} xₘ/(xₘ - xⱼ)
```

### Parâmetros

| Símbolo | Definição |
|---------|-----------|
| S | Segredo |
| n | Número de compartilhamentos |
| k | Limiar mínimo |
| q | Primo > max(n, S) |

---

# PARTE II: FUNÇÕES HASH E ESTRUTURAS

---

## 7. SHA-256

### Funções Lógicas

```
Σ₀(x) = ROTR(2,x) ⊕ ROTR(13,x) ⊕ ROTR(22,x)
Σ₁(x) = ROTR(6,x) ⊕ ROTR(11,x) ⊕ ROTR(25,x)
σ₀(x) = ROTR(7,x) ⊕ ROTR(18,x) ⊕ (x>>>3)
σ₁(x) = ROTR(17,x) ⊕ ROTR(19,x) ⊕ (x>>>10)
Ch(x,y,z) = (x ∧ y) ⊕ (¬x ∧ z)
Maj(x,y,z) = (x ∧ y) ⊕ (x ∧ z) ⊕ (y ∧ z)
```

### Função de Compressão

```
T₁ = h + Σ₁(e) + Ch(e,f,g) + K[t] + W[t]
T₂ = Σ₀(a) + Maj(a,b,c)
```

### Expansão de Mensagem

```
W[t] = σ₁(W[t-2]) + W[t-7] + σ₀(W[t-15]) + W[t-16]
```

### Parâmetros

- 64 rodadas de compressão
- 8 registradores de 32 bits
- Saída: 256 bits

---

## 8. Árvores de Merkle

### Construção

**Nó Folha:**
```
H(i,i,Y) = F(Yᵢ)
```

**Nó Interno:**
```
H(i,j,Y) = F(H(i,(i+j-1)/2,Y) || H((i+j+1)/2,j,Y))
Mᵢ = hash(M₂ᵢ || M₂ᵢ₊₁)
```

**Merkle Root:**
```
R = H(1,n,Y)
```

### Propriedades

| Propriedade | Fórmula |
|-------------|---------|
| Altura | h = ⌈log₂(n)⌉ |
| Total de nós | 2n - 1 |
| Tamanho da prova | O(log n) |
| Complexidade de construção | O(n) |

### Caminho de Autenticação

```
auth[j] = Node(j, ⌊i/2ʲ⌋ ⊕ 1)
```

---

## 9. Construção Merkle-Damgård

### Função de Compressão

```
f: {0,1}^{m+n} → {0,1}^n
```

### Iteração

```
H₀ = IV
Hᵢ = f(H_{i-1}, Mᵢ)  para i = 1,...,L
Saída = H_L
```

### Padding

```
Pad(M) = M || 1 || 0^k || ⟨|M|⟩
```

---

# PARTE III: ASSINATURAS CEGAS E ANONIMATO

---

## 10. Assinaturas Cegas (David Chaum)

### Protocolo

```
m' ≡ m·r^e (mod N)
s' ≡ (m')^d (mod N)
s ≡ s'·r^{-1} (mod N)
s ≡ m^d (mod N)
```

### Variáveis

| Símbolo | Definição |
|---------|-----------|
| m | Mensagem original |
| r | Fator de cegueira |
| m' | Mensagem cega |
| s' | Assinatura cega |
| s | Assinatura final |

---

## 11. Ring Signatures (CryptoNote/Monero)

### Chave Pública de Uso Único

```
P = Hₛ(rA)G + B
x = Hₛ(rA) + b
```

### Key Image

```
I = x·Hₚ(P)
```

### Assinatura

```
cᵢ₊₁ = Hₛ(m, Lᵢ, Rᵢ)
Lᵢ = sᵢG + cᵢPᵢ
Rᵢ = sᵢHₚ(Pᵢ) + cᵢI
sⱼ = α - cⱼxⱼ (mod l)
```

### Parâmetros da Curva

```
q = 2²⁵⁵ - 19
l = 2²⁵² + 27742317777372353535851937790883648493
```

---

## 12. Compromissos de Pedersen

### Compromisso

```
C(v, r) = r·G + v·H
```

### Propriedade Homomórfica

```
C(v₁, r₁) + C(v₂, r₂) = C(v₁+v₂, r₁+r₂)
```

### Verificação de Soma Zero (MimbleWimble)

```
Σ{C_{out}} - Σ{C_{in}} = 0·H + x·G
sum(outputs) - sum(inputs) = sum(kernel_excess) + kernel_offset·G
```

---

# PARTE IV: PROOF OF WORK E CONSENSO

---

## 13. Hashcash

### Função MINT

```
T ← MINT(s, k)
H(s||x) tem k zeros à esquerda
```

### Função VALUE

```
V ← VALUE(T)
H(s||x) tem v zeros à esquerda
```

### Probabilidade

```
P(encontrar k zeros) = 1/2^k
```

---

## 14. Bitcoin Mining

### Ajuste de Dificuldade

```
target = max_target / difficulty
new_difficulty = old_difficulty × (2016 × 10 × 60) / actual_time
```

### Target Compacto

```
target = coefficient × 2^{8×(exponent-3)}
```

### Recompensa por Bloco

```
Block_Reward_i = 50 / 2^i BTC
```

### Hash do Bloco

```
H(bloco) = SHA256(SHA256(cabeçalho))
```

---

## 15. Consenso de Nakamoto

### Probabilidade de Ataque

```
q_z = (q/p)^z  se p > q
q_z = 1        se p ≤ q
```

### Distribuição de Poisson

```
λ = z × (q/p)
P(X=k) = (λ^k × e^{-λ}) / k!
```

### Probabilidade de Sucesso do Atacante

```
P = 1 - Σₖ₌₀ᶻ [(λ^k × e^{-λ})/k! × (1 - (q/p)^{z-k})]
```

### Tolerância a Falhas Bizantinas

```
n = 3f + 1
```

### Fator de Crescimento da Cadeia

```
g = e^{-α∆}
g²α > (1 + δ)β
```

---

## 16. Selfish Mining

### Revenue Pool

```
R_pool = (α(1-α)²(4α+1) + α³) / (1-α(1+(2-α)α))
R_pool = (α - α²) / (1 - α)
R_pool = (α(2-α) - α³) / (1 - α(1+α(2-α)))
```

---

# PARTE V: ETHEREUM E SMART CONTRACTS

---

## 17. Ethereum Virtual Machine

### Transição de Estado

```
σ_{t+1} ≡ Υ(σ_t, T)
Π(σ,B) ≡ Υ(Υ(σ,T₀),T₁)...
```

### Estado da Conta

```
v(x) ≡ x_n ∈ N₂₅₆ ∧ x_b ∈ N₂₅₆ ∧ x_s ∈ B₃₂ ∧ x_c ∈ B₃₂
EMPTY(σ, a) ≡ σ[a]_c = KEC() ∧ σ[a]_n = 0 ∧ σ[a]_b = 0
DEAD(σ, a) ≡ σ[a] = ∅ ∨ EMPTY(σ, a)
```

### Gas

```
g₀ = G_{txdatazero} + G_{txdatanonzero} + G_{txcreate} + G_{accesslistaddress} + G_{accessliststoragekey}
R(x) ≡ G_{initcodeword} × ⌈x/32⌉
```

### Preço Efetivo

```
p ≡ min(T_f, T_m - H_f) + H_f
v₀ ≡ T_g × T_m + T_v
```

---

# PARTE VI: PROVAS DE CONHECIMENTO ZERO

---

## 18. zk-SNARKs

### QAP (Quadratic Arithmetic Program)

```
p(x) = (Σᵢ₌₀ᵐ cᵢ·vᵢ(x)) × (Σᵢ₌₀ᵐ cᵢ·wᵢ(x)) - (Σᵢ₌₀ᵐ cᵢ·yᵢ(x))
```

### Groth16 Verificação

```
e(A, B) = e(α, β) × e(Σᵢ₌₁ˡ aᵢuᵢ(x), γ) × e(C, δ)
```

### SSP (Square Span Program)

```
p(x) = (Σᵢ₌₁ᵐ cᵢ·vᵢ(x))² - v₀(x)
```

---

## 19. PLONK

### Restrição de Porta

```
q_L(X)a(X) + q_R(X)b(X) + q_O(X)c(X) + q_M(X)a(X)b(X) + q_C(X) = 0
```

### Argumento de Permutação

```
Z(gX) × (f'(X) + βS_{ID}(X) + γ) = Z(X) × (g'(X) + βS_σ(X) + γ)
```

---

## 20. Bulletproofs

### Produto Interno Recursivo

```
a' = a_L·x + a_R·x^{-1}
b' = b_L·x^{-1} + b_R·x
g' = g_L·x^{-1} + g_R·x
h' = h_L·x + h_R·x^{-1}
P' = L·x² + R·x^{-2} + P
```

### Range Proof

```
⟨a_L - z·1ⁿ, yⁿ ∘ (a_R + z·1ⁿ) + z²·2ⁿ⟩ = δ(y, z)
```

### Circuito Aritmético

```
w_L ∘ w_R = w_O
W_L·a_L + W_R·a_R + W_O·a_O = W_V·v + c
```

---

# PARTE VII: CRIPTOGRAFIA HOMOMÓRFICA

---

## 21. Paillier

### Criptografia

```
E(m) = g^m · r^n mod n²
```

### Propriedade Homomórfica Aditiva

```
E(m₁) · E(m₂) = g^{m₁+m₂} · (r₁r₂)^n mod n² = E(m₁+m₂)
```

---

## 22. FHE Baseada em Inteiros

### Criptografia

```
c = b + 2x + kp
```

### Adição Homomórfica

```
c ← c₁ + c₂ = b₁⊕b₂ + 2x + kp
```

### Multiplicação Homomórfica

```
c ← c₁ × c₂ = b₁·b₂ + 2x + kp
```

---

## 23. FHE Baseada em Reticulados

### Descriptografia

```
Decrypt_E(sk, Evaluate_E(pk, C, ψ₁, ..., ψₜ)) = C(π₁, ..., πₜ)
```

### Operações

```
Add(pk, ψ₁, ψ₂) = ψ₁ + ψ₂ ∈ (π₁ + π₂) + I
Mult(pk, ψ₁, ψ₂) = ψ₁ × ψ₂ ∈ (π₁ × π₂) + I
```

### Redução Modular

```
v mod B_I = v - B_I · ⌊B_I^{-1}v⌉
π = ψ - ⌊B_{sk}^{-1}ψ⌉
```

---

# PARTE VIII: CRIPTOGRAFIA SIMÉTRICA

---

## 24. DES (Rede de Feistel)

### Rodada de Feistel

```
L_n = R_{n-1}
R_n = L_{n-1} ⊕ f(R_{n-1}, K_n)
```

### Função f

```
f(R, K) = P(S(E(R) ⊕ K))
```

### Descriptografia

```
R_{n-1} = L_n
L_{n-1} = R_n ⊕ f(L_n, K_n)
```

---

## 25. 3DES

### Criptografia (EDE)

```
C = E_{K3}(D_{K2}(E_{K1}(P)))
```

### Descriptografia

```
P = D_{K1}(E_{K2}(D_{K3}(C)))
```

---

## 26. AES

### SubBytes (S-Box Affine)

```
b'_i = b_i ⊕ b_{(i+4) mod 8} ⊕ b_{(i+5) mod 8} ⊕ b_{(i+6) mod 8} ⊕ b_{(i+7) mod 8} ⊕ c_i
```

### MixColumns

```
s'_c(x) = a(x) ⊗ s_c(x)
s'_c(x) = a^{-1}(x) ⊗ s_c(x)  (inverso)
```

### AddRoundKey

```
[s'_{0,c}, s'_{1,c}, s'_{2,c}, s'_{3,c}] = [s_{0,c}, s_{1,c}, s_{2,c}, s_{3,c}] ⊕ [w_{round×Nb+c}]
```

---

## 27. Modos de Operação

### ECB

```
C_j = E_K(P_j)
P_j = D_K(C_j)
```

### CBC

```
C_j = E_K(P_j ⊕ C_{j-1})
P_j = D_K(C_j) ⊕ C_{j-1}
```

### CTR

```
C_j = P_j ⊕ E_K(T_j)
P_j = C_j ⊕ E_K(T_j)
```

### GCM

```
g = GHASH_H(A || C)
T = MSB_t(g ⊕ E_K(J_0))
```

---

# PARTE IX: DERIVAÇÃO DE CHAVES

---

## 28. BIP32 (HD Wallets)

### Derivação de Chave Privada (Hardened)

```
I = HMAC-SHA512(Key = c_{par}, Data = 0x00 || ser256(k_{par}) || ser32(i))
k_i = parse256(I_L) + k_{par} (mod n)
c_i = I_R
```

### Derivação de Chave Privada (Normal)

```
I = HMAC-SHA512(Key = c_{par}, Data = serP(point(k_{par})) || ser32(i))
```

### Derivação de Chave Pública

```
I = HMAC-SHA512(Key = c_{par}, Data = serP(K_{par}) || ser32(i))
K_i = point(parse256(I_L)) + K_{par}
```

### Semente Mestre

```
I = HMAC-SHA512(Key = "Bitcoin seed", Data = S)
```

### Índice Hardened

```
i_H = i + 2³¹
```

---

## 29. BIP39 (Mnemônico)

### Checksum

```
CS = ENT / 32
MS = (ENT + CS) / 11
```

### Semente

```
Seed = PBKDF2(password=mnemonic, salt="mnemonic"+passphrase, iterations=2048, dkLen=512)
```

---

# PARTE X: REDES P2P

---

## 30. Kademlia DHT

### Distância XOR

```
distance(x, y) = x ⊕ y
```

### K-Bucket

```
2^j ≤ distance(node, contact) < 2^{j+1}
```

---

# PARTE XI: PROTOCOLOS DE PAGAMENTO

---

## 31. Lightning Network

### HTLC (Hash Time-Locked Contract)

```
H(preimage) = hash
```

### SegWit

```
Block_weight = (Base_size × 3) + Total_size
```

### Serialização de Transação

```
[nVersion][marker][flag][txins][txouts][witness][nLockTime]
```

---

# PARTE XII: TEORIA DOS JOGOS

---

## 32. Mineração

### Eficiência

```
Efficiency(s) = P - Σⱼ₌₁ⁿ s_j
```

### Custo

```
Cost(s_i) = C × s_i
```

### Função de Ganho

```
g_i(x, s_i, s_{-i}) = (P - Σⱼ₌₁ⁿ s_j) × s_i - C × s_i
```

### Dinâmica

```
Ẋ(t) = ψ(X(t), S(X(t)))
ψ(x, s) = ξ·x - Σⱼ₌₁ⁿ s_j
```

---

# PARTE XIII: TIMESTAMPING

---

## 33. Timestamping Criptográfico

### Hash

```
h(x) = y
```

### Certificado

```
C_n = (n, t_n, id_n, y_n, L_n)
L_n = (t_{n-1}, id_{n-1}, y_{n-1}, H(L_{n-1}))
```

### Assinatura

```
s = σ(C_n)
s' = σ(n+1, t_{n+1}, id_{n+1}, y_{n+1}, L_{n+1})
```

### Múltiplas Testemunhas

```
s_j = σ_j(t, id, y)
```

---

# PARTE XIV: CRIPTOSSISTEMA KNAPSACK

---

## 34. Merkle-Hellman

### Sequência Superincrescente

```
w_i > Σⱼ₌₁^{i-1} w_j  ∀i ∈ {2,...,n}
```

### Geração de Chave Pública

```
b_i = r × w_i mod q
```

### Criptografia

```
C = Σᵢ₌₁ⁿ x_i × b_i
```

### Descriptografia

```
C' = r^{-1} × C mod q
```

### Densidade

```
d = n / log₂(max(b_i))
```

### Matriz de Reticulado LLL

```
    ┌ 1  0  0  ... 0   b₁ ┐
    │ 0  1  0  ... 0   b₂ │
M = │ 0  0  1  ... 0   b₃ │
    │ ...              ...│
    │ 0  0  0  ... 1   bₙ │
    └ 0  0  0  ... 0   -C ┘
```

### Heurística Gaussiana

```
λ₁(L) ≈ √(n/(2πe)) × (det(L))^{1/n}
```

---

# PARTE XV: ASSINATURAS HASH-BASED

---

## 35. WOTS (Winternitz OTS)

### Comprimento

```
len₁ = ⌈8n/lg(w)⌉
```

### Checksum

```
checksum = Σ(w-1-mᵢ)
```

---

## 36. MSS (Merkle Signature Scheme)

### Segurança

```
ε ≤ 2 × max{ε_{cr}, 2^N × ε_{1s}}
```

---

# PARTE XVI: VRF E FUNÇÕES ALEATÓRIAS

---

## 37. Função Aleatória Verificável

### Saída

```
y = h^d mod n
```

### Verificação

```
y^e ≡ h (mod n)
```

---

# PARTE XVII: COMPLEXIDADE COMPUTACIONAL

---

## 38. Problemas Fundamentais

### Problema do Logaritmo Discreto (DLP)

```
Dado (G, g, q, Y = g^x mod p), encontrar x = log_g Y mod p
```

### CDH (Computational Diffie-Hellman)

```
Dado (g, g^a, g^b), computar g^{ab}
Pr[A(g, g^a, g^b) = g^{ab}] ≤ negl(n)
```

### DDH (Decisional Diffie-Hellman)

```
Distinguir: D₀ = (g, g^a, g^b, g^{ab}) vs D₁ = (g, g^a, g^b, g^c)
|Pr[A(D₀) = 1] - Pr[A(D₁) = 1]| ≤ negl(n)
```

### Complexidade de Ataques

| Operação | Complexidade |
|----------|--------------|
| Ataque de colisão (birthday) | O(2^{n/2}) |
| Ataque de preimagem | O(2^n) |
| Adversário quântico (Grover) | O(√N) |
| Fatoração (GNFS) | exp(c(log n)^{1/3}(log log n)^{2/3}) |

---

## 39. Teste de Primalidade APR-CL

```
Complexidade: O((log n)^{c·log log log n})
```

---

# PARTE XVIII: CONSTANTES

---

## 40. Constantes Físicas e Criptográficas

| Constante | Valor |
|-----------|-------|
| Constante de Boltzmann (k) | 1.38 × 10⁻²³ J/K |
| Limite de Landauer (300K) | 2.87 × 10⁻²¹ J/bit |
| secp256k1 ordem (n) | 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141 |
| Ed25519 primo (q) | 2²⁵⁵ - 19 |
| Ed25519 ordem (l) | 2²⁵² + 27742317777372353535851937790883648493 |

---

# ÍNDICE DE FÓRMULAS POR CATEGORIA

## Criptografia Assimétrica
- RSA: c ≡ m^e (mod n), m ≡ c^d (mod n)
- DH: K = g^{ab} mod p
- ECDSA: s = k^{-1}(z + r·d_A) mod n
- Schnorr: s = k + xe

## Funções Hash
- SHA-256: 64 rodadas, blocos de 512 bits, saída 256 bits
- Merkle Tree: M_i = hash(M_{2i} || M_{2i+1})

## Consenso
- PoW: target = max_target / difficulty
- BFT: n = 3f + 1

## Zero-Knowledge
- QAP: p(x) = L(x)·R(x) - O(x)
- Groth16: e(A,B) = e(α,β)·e(L,γ)·e(C,δ)

## Criptografia Simétrica
- Feistel: R_n = L_{n-1} ⊕ f(R_{n-1}, K_n)
- AES: 10/12/14 rodadas

---

**FIM DO COMPÊNDIO MATEMÁTICO**

*Compilado a partir de documentos técnicos sobre criptografia e criptomoedas.*
