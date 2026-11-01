# COMPÊNDIO MATEMÁTICO: CRIPTOGRAFIA E CRIPTOMOEDAS
## Equações, Fórmulas, Algoritmos e Especificações Técnicas

---

# PARTE I: CRIPTOGRAFIA DE CHAVE PÚBLICA

---

## 1. RSA (Rivest-Shamir-Adleman)

### 1.1 Geração de Chaves

| Parâmetro | Fórmula |
|-----------|---------|
| Módulo | n = p × q |
| Função Totiente | φ(n) = (p-1)(q-1) |
| Função Carmichael | λ(n) = lcm(p-1, q-1) |
| Expoente Privado | d ≡ e⁻¹ (mod λ(n)) |
| Condição de e | gcd(e, λ(n)) = 1, 1 < e < λ(n) |

### 1.2 Operações

```
Criptografia:    C ≡ M^e (mod n)
Descriptografia: M ≡ C^d (mod n)
Assinatura:      S = D_B(M)
Verificação:     M = E_B(S)
```

### 1.3 Otimização CRT (Teorema Chinês do Resto)

```
d_p = d mod (p-1)
d_q = d mod (q-1)
q_inv = q⁻¹ mod p
m₁ = c^(d_p) mod p
m₂ = c^(d_q) mod q
h = (q_inv × (m₁ - m₂)) mod p
m = m₂ + h × q
```

### 1.4 Propriedades

```
D_K(E_K(M)) = M
E_K(D_K(M)) = M
(x^e)^d ≡ x (mod n)
```

---

## 2. Diffie-Hellman Key Exchange

### 2.1 Protocolo Básico

| Variável | Definição |
|----------|-----------|
| p | Primo grande (módulo) |
| g | Raiz primitiva módulo p (gerador) |
| a, b | Chaves privadas |
| A, B | Chaves públicas |
| s | Segredo compartilhado |

```
A = g^a mod p          (Alice → Bob)
B = g^b mod p          (Bob → Alice)
s = B^a mod p = A^b mod p = g^(ab) mod p
```

### 2.2 Multi-party DH

```
Segredo compartilhado (3 partes): g^(abc) mod p
```

### 2.3 X3DH (Extended Triple Diffie-Hellman)

```
K = KDF(Y^x, B^x, Y^a, X, Y, A, B)
```

| Variável | Definição |
|----------|-----------|
| IKA, IKB | Chaves de identidade |
| EKA | Chave efêmera de Alice |
| SPKB | Chave pré-assinada de Bob |
| OPKB | Chave pré-única de Bob |

### 2.4 Suposições de Segurança

**Problema do Logaritmo Discreto (DLP):**
```
Dado (G, g, q, Y = g^x mod p), encontrar x = log_g Y mod p
```

**Diffie-Hellman Computacional (CDH):**
```
Dado (g, g^a, g^b), computar g^(ab)
Pr[A(g, g^a, g^b) = g^(ab)] ≤ negl(n)
```

**Diffie-Hellman Decisional (DDH):**
```
Distinguir: D₀ = (g, g^a, g^b, g^(ab)) vs D₁ = (g, g^a, g^b, g^c)
|Pr[A(D₀) = 1] - Pr[A(D₁) = 1]| ≤ negl(n)
```

---

## 3. Criptografia de Curva Elíptica (ECC)

### 3.1 Equação da Curva

```
Forma de Weierstrass:  y² = x³ + ax + b
secp256k1 (Bitcoin):   y² = x³ + 7
Edwards:               x² + y² = 1 + dx²y²
Edwards25519:          x² + y² = 1 - (121665/121666)x²y²
```

### 3.2 Parâmetros secp256k1

| Parâmetro | Valor |
|-----------|-------|
| p | 2²⁵⁶ - 2³² - 977 |
| a | 0 |
| b | 7 |
| G | Ponto gerador |
| n | Ordem do grupo |

### 3.3 ECDSA (Elliptic Curve Digital Signature Algorithm)

**Geração de Chave:**
```
Q_A = d_A × G
```

**Assinatura:**
```
e = HASH(m)
z = L_n bits mais à esquerda de e
(x₁, y₁) = k × G
r = x₁ mod n
s = k⁻¹(z + r × d_A) mod n
Assinatura = (r, s)
```

**Verificação:**
```
u₁ = z × s⁻¹ mod n
u₂ = r × s⁻¹ mod n
(x₁, y₁) = u₁ × G + u₂ × Q_A
Válida se r ≡ x₁ (mod n)
```

### 3.4 Assinaturas Schnorr

**Geração de Chave:**
```
y = g^x
```

**Assinatura:**
```
r = g^k
e = H(r || M)
s = k + xe
Assinatura = (e, s)
```

**Verificação:**
```
r_v = g^s × y^(-e)
e_v = H(r_v || M)
Válida se e_v = e
```

```
Verificação alternativa: s⋅G = R + hash(R || P || m)⋅P
```

---

## 4. Assinaturas BLS

### 4.1 Operações

```
Chave Pública:    pk = sk × g₂
Hash:             h = H(m)
Assinatura:       σ = h^(sk)
Verificação:      e(σ, g₂) = e(H(m), pk)
```

### 4.2 Agregação

```
σ = Aggregate(σ₁, σ₂, ..., σₖ)
Verificação: e(σ, g₂) = ∏ᵢ₌₁ᵏ e(H(mᵢ), pkᵢ)
```

### 4.3 MuSig

```
P_agg = Σᵢ₌₁ⁿ Pᵢ
s_agg = Σᵢ₌₁ⁿ sᵢ
```

---

# PARTE II: FUNÇÕES DE HASH CRIPTOGRÁFICAS

---

## 5. SHA-256

### 5.1 Funções Lógicas

```
Ch(x, y, z) = (x ∧ y) ⊕ (¬x ∧ z)
Maj(x, y, z) = (x ∧ y) ⊕ (x ∧ z) ⊕ (y ∧ z)
Σ₀(x) = ROTR²(x) ⊕ ROTR¹³(x) ⊕ ROTR²²(x)
Σ₁(x) = ROTR⁶(x) ⊕ ROTR¹¹(x) ⊕ ROTR²⁵(x)
σ₀(x) = ROTR⁷(x) ⊕ ROTR¹⁸(x) ⊕ SHR³(x)
σ₁(x) = ROTR¹⁷(x) ⊕ ROTR¹⁹(x) ⊕ SHR¹⁰(x)
```

### 5.2 Iteração Principal

```
T₁ = h + Σ₁(e) + Ch(e, f, g) + K[t] + W[t]
T₂ = Σ₀(a) + Maj(a, b, c)
W[t] = σ₁(W[t-2]) + W[t-7] + σ₀(W[t-15]) + W[t-16]
```

### 5.3 Especificações

| Parâmetro | Valor |
|-----------|-------|
| Tamanho de bloco | 512 bits |
| Tamanho de saída | 256 bits |
| Rodadas | 64 |
| Constantes K | 64 valores de 32 bits |
| Estado inicial H | 8 valores de 32 bits |

---

## 6. SHA-3 / Keccak

### 6.1 Funções de Permutação

```
θ step: C[x] = A[x,0] ⊕ A[x,1] ⊕ A[x,2] ⊕ A[x,3] ⊕ A[x,4]
        D[x] = C[x-1] ⊕ rot(C[x+1], 1)

ρ step: a[i,j] = rot(a[i,j], (t+1)(t+2)/2)

π step: A'[x,y] = A[x',y'] onde x' = y, y' = (2x + 3y) mod 5

χ step: A[x,y] = A[x,y] ⊕ ((¬A[x+1,y]) ∧ A[x+2,y])

ι step: A[0,0] = A[0,0] ⊕ RC[i_r]
```

---

## 7. MD5 / SHA-1

### 7.1 Funções Auxiliares MD5

```
F(X,Y,Z) = (X ∧ Y) ∨ (¬X ∧ Z)
G(X,Y,Z) = (X ∧ Z) ∨ (Y ∧ ¬Z)
H(X,Y,Z) = X ⊕ Y ⊕ Z
I(X,Y,Z) = Y ⊕ (X ∨ ¬Z)
```

### 7.2 Iteração MD5

```
a = b + ((a + F(b,c,d) + X[k] + T[i]) <<< s)
```

### 7.3 SHA-1 Message Schedule

```
W(t) = S¹(W(t-3) ⊕ W(t-8) ⊕ W(t-14) ⊕ W(t-16))
TEMP = S⁵(A) + f(t,B,C,D) + E + W(t) + K(t)
```

---

# PARTE III: ÁRVORES DE MERKLE

---

## 8. Merkle Trees

### 8.1 Definições Fundamentais

```
Nó Folha:        H(i,i,Y) = F(Yᵢ)
Nó Interno:      H(i,j,Y) = F(H(i,(i+j-1)/2,Y) || H((i+j+1)/2,j,Y))
Merkle Root:     R = H(1,n,Y)
```

### 8.2 Construção Iterativa

```
Nível 0 (folhas): hᵢ = H(dataᵢ)
Nível k:          parent = H(filho_esq || filho_dir)
Fórmula:          Mᵢ = hash(M₂ᵢ || M₂ᵢ₊₁)
```

### 8.3 Propriedades da Estrutura

| Propriedade | Fórmula |
|-------------|---------|
| Altura da árvore | h = ⌈log₂(n)⌉ |
| Total de nós | 2n - 1 |
| Nós internos | n - 1 |
| Nós folha | n = 2^h |
| Comprimento do caminho de autenticação | log₂(n) hashes |
| Tamanho da prova | 100 × log₂(n) bits |

### 8.4 Complexidade

| Operação | Complexidade |
|----------|--------------|
| Construção da árvore | O(n) |
| Verificação | O(log n) |
| Ataque de colisão (birthday) | O(2^(n/2)) |
| Ataque de preimagem | O(2^n) |

### 8.5 Caminho de Autenticação

```
auth[j] = Node(j, ⌊i/2ʲ⌋ ⊕ 1)

Para j = 0 até h-1:
  Se bit j do índice i = 0: A_{j+1} = H(Aⱼ || authⱼ)
  Senão:                    A_{j+1} = H(authⱼ || Aⱼ)
```

---

## 9. Construção Merkle-Damgård

### 9.1 Função de Compressão

```
f: {0,1}^(m+n) → {0,1}^n
f: {0,1}^b × {0,1}^n → {0,1}^n
```

### 9.2 Iteração

```
H₀ = IV (vetor de inicialização)
Hᵢ = f(H_{i-1}, Mᵢ)     para i = 1,...,L
Saída = H_L
```

### 9.3 Padding

```
Pad(M) = M || 1 || 0^k || ⟨|M|⟩
```

---

# PARTE IV: CRIPTOGRAFIA SIMÉTRICA

---

## 10. AES

### 10.1 Transformações

```
SubBytes:     Substituição não-linear via S-box
ShiftRows:    Rotação cíclica de linhas
MixColumns:   Multiplicação matricial em GF(2⁸)
AddRoundKey:  XOR com subchave da rodada
```

### 10.2 Especificações

| Parâmetro | AES-128 | AES-192 | AES-256 |
|-----------|---------|---------|---------|
| Tamanho da chave | 128 bits | 192 bits | 256 bits |
| Tamanho do bloco | 128 bits | 128 bits | 128 bits |
| Rodadas | 10 | 12 | 14 |

---

## 11. DES / 3DES

### 11.1 Rede de Feistel

```
L_{i+1} = R_i
R_{i+1} = L_i ⊕ f(R_i, K_i)
```

### 11.2 3DES

```
C = E_{K1}(D_{K2}(E_{K3}(P)))
```

### 11.3 Especificações DES

| Parâmetro | Valor |
|-----------|-------|
| Tamanho da chave | 56 bits |
| Tamanho do bloco | 64 bits |
| Rodadas | 16 |

---

## 12. Modos de Operação

### 12.1 CBC

```
C_i = E_K(P_i ⊕ C_{i-1})
C_0 = IV
```

### 12.2 CTR

```
C_i = P_i ⊕ E_K(Nonce || Counter_i)
```

### 12.3 GCM

```
Y_0 = IV || 0³¹1
C_i = P_i ⊕ E_K(Y_i)
Tag = GHASH(H, A, C) ⊕ E_K(Y_0)
```

---

# PARTE V: PROTOCOLOS DE CONSENSO

---

## 13. Consenso de Nakamoto

### 13.1 Probabilidade de Ataque

```
q_z = (q/p)^z    se p > q
q_z = 1          se p ≤ q

λ = z × (q/p)
P(X=k) = (λ^k × e^(-λ)) / k!
P_z = 1 - Σ_{k=0}^{z} [(λ^k × e^(-λ))/k! × (1 - (q/p)^(z-k))]
```

### 13.2 Limites de Segurança

```
E(X[r,r+s-1]) ≥ γs
Pr(X[r,r+τm-1] ≤ (1-δ)γτm) ≤ e^(-Ω(δ²γm))
f∆ < 1/(2(1-β)) × ln((1-β)/(β(1+δ)))
```

### 13.3 Dificuldade Bitcoin

```
new_difficulty = old_difficulty × (2016 × 10 × 60) / actual_time
Block_Reward_i = 50 / 2^i
Hash_Rate ≈ D × 2³² / 600
```

### 13.4 Fornecimento Total

```
Σᵢ₌₀³² (50 × 210000) / 2^i ≈ 21,000,000 BTC
```

---

## 14. Tolerância a Falhas Bizantinas (BFT)

### 14.1 Requisito Fundamental

```
n ≥ 3f + 1
n > 3f
```

| Variável | Definição |
|----------|-----------|
| n | Total de réplicas |
| f | Máximo de réplicas bizantinas |

### 14.2 pBFT Quorums

```
Quorum de prepare: 2f mensagens
Quorum de commit: 2f + 1 mensagens
```

---

## 15. Proof of Stake

### 15.1 Seleção de Validador

```
Hash(ProposedNewBlock || ClockTime) < target × StakeValue
```

### 15.2 Recompensa Base (Ethereum)

```
base_reward = effective_balance × (base_reward_factor / (base_rewards_per_epoch × sqrt(sum(active_balance))))
```

---

## 16. Mineração Egoísta (Selfish Mining)

### 16.1 Receita do Pool

```
R_pool = (α(1-α)²(4α+1) + α³) / (1-α(1+(2-α)α))
R_pool = (α - α²) / (1 - α)
R_pool = (α(2-α) - α³) / (1 - α(1+α(2-α)))
```

### 16.2 Parâmetros

```
g = e^(-α∆)
g²α > (1 + δ)β
Pr(falha) ≤ e^(-Ω(δ²g²k))
```

---

# PARTE VI: HASHCASH E PROOF OF WORK

---

## 17. Hashcash

### 17.1 Operações

```
MINT: T ← encontrar x tal que H(s||x) tem w zeros iniciais
VALUE: V ← verificar H(s||x) tem v zeros iniciais
```

### 17.2 Formato

```
ver:bits:date:resource:[ext]:rand:counter
```

### 17.3 Probabilidade

```
P(N) = 2^(-N)
```

---

## 18. Bitcoin Mining

### 18.1 Target

```
target = coefficient × 2^(8 × (exponent - 3))
difficulty = difficulty_1_target / current_target
```

### 18.2 Double SHA-256

```
H(bloco) = SHA256(SHA256(cabeçalho_do_bloco))
MerkleRoot(T) = MerkleTree(Hash(t₁), Hash(t₂), ..., Hash(tₙ))
```

---

# PARTE VII: PROVAS DE CONHECIMENTO ZERO

---

## 19. ZK-SNARKs

### 19.1 Verificação Groth16

```
e(A, B) = e(α, β) × e(L_pub, γ) × e(C, δ)
```

### 19.2 QAP (Quadratic Arithmetic Program)

```
A(x) × B(x) - C(x) = H(x) × Z(x)
```

---

## 20. PLONK

### 20.1 Restrições de Porta

```
q_L × a + q_R × b + q_O × c + q_M × (a × b) + q_C = 0
```

---

## 21. Bulletproofs

### 21.1 Inner Product

```
c = ⟨a, b⟩ = Σᵢ aᵢ × bᵢ
```

### 21.2 Range Proof

```
v ∈ [0, 2^n)
```

---

# PARTE VIII: CRIPTOGRAFIA HOMOMÓRFICA

---

## 22. Paillier

### 22.1 Operações

```
Criptografia:   E(m) = g^m × r^n mod n²
Adição:         E(m₁) × E(m₂) = E(m₁ + m₂)
                g^(m₁+m₂) × (r₁r₂)^n mod n² = E(m₁+m₂)
```

---

## 23. FHE Baseado em Inteiros

### 23.1 Criptografia

```
c = b + 2x + kp
```

### 23.2 Operações

```
Adição:        c₁ + c₂ = b₁ ⊕ b₂ + 2x + kp
Multiplicação: c₁ × c₂ = b₁ × b₂ + 2x + kp
```

---

## 24. Criptografia Baseada em Reticulado

### 24.1 LWE (Learning With Errors)

```
b = ⟨a, s⟩ + e mod q
```

### 24.2 RLWE (Ring-LWE)

```
b(x) = a(x) × s(x) + e(x) mod (q, f(x))
```

### 24.3 NTRU

```
h(x) = p × f_q(x) × g(x) mod q
c(x) = r(x) × h(x) + m(x) mod q
```

---

# PARTE IX: RING SIGNATURES E PRIVACIDADE

---

## 25. Ring Signatures (CryptoNote/Monero)

### 25.1 Chave Pública de Uso Único

```
P = H_s(rA)G + B
x = H_s(rA) + b
```

### 25.2 Key Image

```
I = x × H_p(P)
```

### 25.3 Assinatura em Anel

```
c_{i+1} = H_s(m, L_i, R_i)
L_i = s_i × G + c_i × P_i
R_i = s_i × H_p(P_i) + c_i × I
s_π = α - c_π × x mod l
```

### 25.4 MLSAG

```
L_j_π = α_j × G
R_j_π = α_j × H_p(P_j_π)
c_{π+1} = H(m, L_1_π, R_1_π, ..., L_m_π, R_m_π)
L_j_i = s_j_i × G + c_i × P_j_i
R_j_i = s_j_i × H_p(P_j_i) + c_i × I_j
```

---

## 26. Compromissos de Pedersen

### 26.1 Fórmula

```
C(v, r) = r × G + v × H
```

### 26.2 Propriedade Homomórfica

```
C(v₁, r₁) + C(v₂, r₂) = C(v₁ + v₂, r₁ + r₂)
```

---

## 27. Transações Confidenciais

### 27.1 Verificação

```
Σ(outputs) - Σ(inputs) = 0
Σ(C_out) - Σ(C_in) = (Σv_out - Σv_in)H + (Σr_out - Σr_in)G
```

---

## 28. MimbleWimble

### 28.1 Compromisso

```
C := vH + rG
```

### 28.2 Verificação de Transação

```
sum(outputs) - sum(inputs) = sum(kernel_excess) + kernel_offset × G
```

---

# PARTE X: ETHEREUM

---

## 29. Ethereum Virtual Machine

### 29.1 Transição de Estado

```
σ_{t+1} ≡ Υ(σ_t, T)
Π(σ,B) ≡ Υ(Υ(σ,T₀),T₁)...
```

### 29.2 Estado da Conta

```
v(x) ≡ x_n ∈ N₂₅₆ ∧ x_b ∈ N₂₅₆ ∧ x_s ∈ B₃₂ ∧ x_c ∈ B₃₂
EMPTY(σ, a) ≡ σ[a]_c = KEC() ∧ σ[a]_n = 0 ∧ σ[a]_b = 0
DEAD(σ, a) ≡ σ[a] = ∅ ∨ EMPTY(σ, a)
```

### 29.3 Gas

```
g₀ ≡ G_txdatazero + G_txdatanonzero + G_txcreate + G_accesslistaddress + G_accessliststoragekey
Custo Total = Unidades de Gás × (Taxa Base + Taxa de Prioridade)
```

### 29.4 EVM Especificações

| Parâmetro | Valor |
|-----------|-------|
| Profundidade da Pilha | 1024 itens |
| Tamanho da Palavra | 256 bits |

---

## 30. ECDSA no Ethereum

### 30.1 Geração de Endereço

```
Endereço = últimos 20 bytes de Keccak256(chave_pública)
```

### 30.2 Assinatura

```
(r, s, v) = ECDSASIGN(mensagem, chave_privada)
```

---

# PARTE XI: DERIVAÇÃO DE CHAVES

---

## 31. BIP32 HD Wallets

### 31.1 Derivação de Chave Privada (CKDpriv)

```
Endurecida (i ≥ 2³¹):
I = HMAC-SHA512(Key = c_par, Data = 0x00 || ser256(k_par) || ser32(i))

Normal:
I = HMAC-SHA512(Key = c_par, Data = serP(point(k_par)) || ser32(i))

k_i = parse256(I_L) + k_par (mod n)
c_i = I_R
```

### 31.2 Derivação de Chave Pública (CKDpub)

```
I = HMAC-SHA512(Key = c_par, Data = serP(K_par) || ser32(i))
K_i = point(parse256(I_L)) + K_par
c_i = I_R
```

### 31.3 Chave Mestre

```
I = HMAC-SHA512(Key = "Bitcoin seed", Data = S)
k_master = parse256(I_L)
c_master = I_R
```

### 31.4 Relações

```
K = point(k)
i_H = i + 2³¹
```

---

## 32. BIP39 Mnemônicos

### 32.1 Geração

```
CS = ENT / 32
MS = (ENT + CS) / 11
```

| ENT | CS | MS |
|-----|----|----|
| 128 | 4 | 12 |
| 160 | 5 | 15 |
| 192 | 6 | 18 |
| 224 | 7 | 21 |
| 256 | 8 | 24 |

### 32.2 Derivação de Semente

```
Seed = PBKDF2(password=mnemonic, salt="mnemonic"+passphrase, iterations=2048, dkLen=512)
```

---

# PARTE XII: BITCOIN SCRIPT

---

## 33. P2PKH (Pay to Public Key Hash)

```
scriptPubKey: OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
scriptSig: <sig> <pubKey>
```

---

## 34. P2SH (Pay to Script Hash)

```
scriptPubKey: OP_HASH160 <20-byte-hash-of-redeemScript> OP_EQUAL
scriptSig: ...signatures... <serialized_redeemScript>
```

---

## 35. Multisig (BIP 11)

```
scriptPubKey: m <pubkey1> ... <pubkeyN> n OP_CHECKMULTISIG
scriptSig: OP_0 <signature1> ... <signatureM>
```

---

## 36. SegWit

### 36.1 Peso do Bloco

```
Block_weight = (Base_size × 3) + Total_size
```

### 36.2 Serialização

```
[nVersion][marker][flag][txins][txouts][witness][nLockTime]
```

---

## 37. Taproot

### 37.1 Output Key

```
Q = P + hash(P||m)G
```

---

# PARTE XIII: LIGHTNING NETWORK

---

## 38. HTLC (Hash Time-Locked Contracts)

### 38.1 Script

```
OP_IF
    OP_HASH160 <payment_hash> OP_EQUALVERIFY
    <remote_pubkey>
OP_ELSE
    <cltv_expiry> OP_CHECKLOCKTIMEVERIFY OP_DROP
    <local_pubkey>
OP_ENDIF
OP_CHECKSIG
```

---

# PARTE XIV: PROTOCOLOS DE REDE

---

## 39. Kademlia DHT

### 39.1 Métrica de Distância

```
distance(x, y) = x ⊕ y
```

### 39.2 K-buckets

```
2^j ≤ distance(node, contact) < 2^(j+1)
```

---

# PARTE XV: COMPUTAÇÃO MULTI-PARTE

---

## 40. Shamir Secret Sharing

### 40.1 Polinômio

```
f(x) = a₀ + a₁x + a₂x² + ... + a_{k-1}x^{k-1}
```
onde a₀ = S (segredo)

### 40.2 Interpolação de Lagrange

```
ℓ_j(x) = ∏_{m=0, m≠j}^{k-1} (x - x_m)/(x_j - x_m)
f(x) = Σ_{j=0}^{k-1} y_j × ℓ_j(x)
a₀ = f(0) = Σ_{j=0}^{k-1} y_j × ∏_{m=0, m≠j}^{k-1} x_m/(x_m - x_j)
```

---

## 41. Threshold Signatures (TSS)

### 41.1 Chave Pública Distribuída

```
pk = g^(sk)
sk = Σ sk_i
```

---

## 42. Verifiable Random Functions (VRF)

### 42.1 Função

```
F_SK(x) = g^(1/(z+SK))
```

### 42.2 Verificação

```
y = h^d mod n
y^e ≡ h (mod n)
```

---

# PARTE XVI: PROTOCOLOS DEFI

---

## 43. AMM (Automated Market Maker)

### 43.1 Produto Constante (Uniswap)

```
x × y = k
```

### 43.2 Soma Constante

```
x + y = k
```

### 43.3 Média Constante (Balancer)

```
∏(xᵢ)^(wᵢ) = k
```

---

## 44. Taxas de Juros (Aave/Compound)

### 44.1 Taxa de Utilização

```
U = TotalBorrows / (TotalLiquidity + TotalBorrows)
```

### 44.2 Taxa de Empréstimo

```
Se U ≤ U_optimal:
    BorrowRate = BaseRate + (U / U_optimal) × Slope1

Se U > U_optimal:
    BorrowRate = BaseRate + Slope1 + ((U - U_optimal) / (1 - U_optimal)) × Slope2
```

### 44.3 Taxa de Fornecimento

```
SupplyRate = BorrowRate × U × (1 - ReserveFactor)
```

### 44.4 APY

```
APY = (1 + r/n)^n - 1
APY = ((((Rate / 10¹⁸ × BlocksPerDay + 1)^365)) - 1) × 100
```

---

# PARTE XVII: ESCALABILIDADE

---

## 45. TPS (Transactions Per Second)

```
TPS = (block_size / tx_size) / block_time
```

---

## 46. Rollups

### 46.1 ZK-Rollups

```
π = Prove(L₁_state, L₂_txs, L₂_state')
Verify(π, commitment) = true/false
```

### 46.2 Optimistic Rollups

```
Challenge_period ≈ 7 dias
```

---

# PARTE XVIII: CRIPTOSSISTEMA MERKLE-HELLMAN

---

## 47. Knapsack

### 47.1 Sequência Superincrescente

```
wᵢ > Σⱼ₌₁^{i-1} wⱼ     para todo i ∈ {2,...,n}
```

### 47.2 Geração de Chaves

```
Chave Pública: bᵢ = r × wᵢ mod q
q > Σᵢ₌₁ⁿ wᵢ
gcd(r, q) = 1
```

### 47.3 Criptografia

```
C = Σᵢ₌₁ⁿ xᵢ × bᵢ
```

### 47.4 Descriptografia

```
C' = r⁻¹ × C mod q
C' = Σᵢ₌₁ⁿ xᵢ × wᵢ
```

### 47.5 Parâmetro de Densidade

```
d = n / log₂(max(bᵢ))
```

---

# PARTE XIX: ASSINATURAS CEGAS

---

## 48. Assinatura Cega RSA

### 48.1 Protocolo

```
Cegamento:     m' = m × r^e mod N
Assinatura:    s' = (m')^d mod N
Desvelamento:  s = s' × r⁻¹ mod N = m^d mod N
```

---

# PARTE XX: TIMESTAMPING

---

## 49. Esquema de Vinculação

### 49.1 Certificado

```
C_n = (n, t_n, id_n, y_n, L_n)
L_n = (t_{n-1}, id_{n-1}, y_{n-1}, H(L_{n-1}))
s = σ(C_n)
```

### 49.2 Cadeia

```
L_i = H(t_i, ID_i, y_i, L_{i-1})
```

---

# PARTE XXI: CONSTANTES FÍSICAS

---

## 50. Constantes de Referência

| Constante | Símbolo | Valor | Unidades |
|-----------|---------|-------|----------|
| Boltzmann | k | 1.38 × 10⁻²³ | J/K |
| Avogadro | N_A | 6.02 × 10²³ | mol⁻¹ |
| Constante dos gases | R | 8.314 | J/(mol·K) |
| Limite de Landauer (300K) | E_L | kT×ln(2) ≈ 2.87 × 10⁻²¹ | J/bit |

---

# PARTE XXII: TEORIA DOS NÚMEROS

---

## 51. Fundamentos

### 51.1 Grupo Multiplicativo

```
Z*_p = {1, 2, ..., p-1}
|Z*_p| = p - 1 = φ(p)
```

### 51.2 Função Totiente de Euler

```
φ(n) = n × ∏_{p|n} (1 - 1/p)
φ(p) = p - 1     (p primo)
φ(pq) = (p-1)(q-1)
```

### 51.3 Teorema de Euler

```
a^φ(n) ≡ 1 (mod n)     para gcd(a,n) = 1
```

### 51.4 Pequeno Teorema de Fermat

```
a^(p-1) ≡ 1 (mod p)     para p primo, p ∤ a
```

### 51.5 Ordem de Gerador

```
ord_p(g) = p - 1     (g é raiz primitiva)
```

---

# PARTE XXIII: COMPLEXIDADE COMPUTACIONAL

---

## 52. Limites Clássicos vs Quânticos

| Problema | Clássico | Quântico (Shor) |
|----------|----------|-----------------|
| Fatoração | O(e^(n^(1/3))) | O(n³) |
| DLP | O(e^(n^(1/2))) | O(n³) |

---

## 53. Merkle Puzzles

### 53.1 Fator de Trabalho

| Parte | Complexidade |
|-------|--------------|
| Remetente | O(N) |
| Receptor | O(N) |
| Atacante | O(N²) |
| Gap de Segurança | O(N) |

### 53.2 Quântico

| Cenário | Complexidade |
|---------|--------------|
| Adversário clássico | Ω(N²) |
| Adversário quântico | O(N) |
| Limite inferior quântico | Ω(N^(3/2)) |

---

# PARTE XXIV: ÍNDICE DE SÍMBOLOS

---

| Símbolo | Significado |
|---------|-------------|
| ⊕ | XOR (ou exclusivo) |
| ∧ | AND (e lógico) |
| ∨ | OR (ou lógico) |
| ¬ | NOT (negação) |
| ≡ | Congruência modular |
| mod | Operação de módulo |
| \|\| | Concatenação |
| × | Multiplicação / Multiplicação escalar |
| + | Adição / Adição de pontos |
| G | Ponto gerador da curva |
| H | Função de hash / Ponto gerador secundário |
| n | Ordem do grupo / módulo |
| p, q | Números primos |
| e | Expoente público |
| d | Expoente privado |
| sk | Chave secreta |
| pk | Chave pública |
| σ | Assinatura |
| π | Prova |
| λ | Função de Carmichael |
| φ | Função totiente de Euler |
| ⌈x⌉ | Teto de x |
| ⌊x⌋ | Piso de x |
| ROTR | Rotação à direita |
| SHR | Deslocamento à direita |
| gcd | Máximo divisor comum |
| lcm | Mínimo múltiplo comum |

---

**FIM DO COMPÊNDIO MATEMÁTICO**

---

*Documento consolidado a partir de 12 fontes originais de criptografia e criptomoedas.*
*Contém apenas equações, fórmulas, algoritmos e especificações técnicas.*
