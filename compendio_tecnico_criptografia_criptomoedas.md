# COMPÊNDIO TÉCNICO: CRIPTOGRAFIA E CRIPTOMOEDAS

## Dados Técnicos Crus: Fórmulas, Equações, Algoritmos e Variáveis

**APENAS PARTE TÉCNICA - SEM NARRATIVAS**

---

# SUMÁRIO

1. Ralph Merkle - Árvores de Merkle
2. Whitfield Diffie - troca de chaves Diffie-Hellman, criptografia de chave pública, New Directions in Cryptography 1976, Sun Microsystems
3. Martin Hellman - protocolo Diffie-Hellman, criptografia assimétrica, logaritmo discreto, Stanford University
4. David Chaum - Dinheiro Digital, Blind Signatures, Mix Networks
5. Stuart Haber - Timestamping Criptográfico
6. W. Scott Stornetta - Timestamping Distribuído
7. Ronald Rivest - RSA algorithm, MIT, RC4, RC5, RC6, MD2, MD4, MD5, ring signatures, todos os trabalhos
8. Adi Shamir - RSA algorithm, Shamir Secret Sharing, visual cryptography, differential cryptanalysis, Weizmann Institute
9. Leonard Adleman - Algoritmo RSA, Computação de DNA, USC, números primos, fatorização
10. Hal Finney - Reusable Proof of Work (RPOW), PGP, primeira transação Bitcoin, cypherpunks
11. Adam Back - Hashcash, proof of work, Blockstream, cypherpunks, anti-spam PoW
12. Nick Szabo - Contratos Inteligentes e Bit Gold
13. Wei Dai - b-money, criptografia, Crypto++
14. Satoshi Nakamoto - Bitcoin whitepaper, blockchain, proof of work, consenso distribuído, UTXO model
15. K. Eric Drexler - nanotecnologia, Engines of Creation, molecular assemblers, MIT, Foresight Institute
16. RSA Algorithm - Fatorização de inteiros, exponenciação modular, chaves pública/privada
17. Diffie-Hellman Key Exchange - logaritmo discreto, grupos cíclicos, troca de chaves, todas as equações
18. Elliptic Curve Cryptography (ECC)
19. SHA-256 hash function - Secure Hash Algorithm
20. Ralph Merkle - Árvores de Merkle
21. Assinaturas Digitais - ECDSA, Schnorr, BLS, Assinaturas Agregadas e Multisig
22. Proof of Work - hashcash, dificuldade, nonce, target, mining algorithm
23. Proof of Stake - seleção de validadores, staking, slashing, Casper, Ouroboros
24. Blockchain consensus - Nakamoto consensus, BFT, PBFT, Tendermint, Raft
25. Bitcoin Script - linguagem de script, OP_CODES, P2PKH, P2SH, SegWit
26. Lightning Network - canais de pagamento, HTLCs, roteamento, onion routing, capacidade
27. Provas de Conhecimento Zero - zk-SNARKs, zk-STARKs, Groth16, Plonk, bulletproofs
28. Criptografia Homomórfica - FHE, Paillier, Baseada em Reticulado
29. Ring Signatures - Monero, CryptoNote, linkability, anonimato, key images
30. Confidential Transactions - Compromissos de Pedersen, provas de alcance, fatores de cegueira
31. MimbleWimble - cut-through, kernel, Grin, Beam, compactação de blockchain
32. Ethereum Smart Contracts - EVM, Solidity, gas, state machine, Vitalik Buterin
33. Funções de Hash Criptográficas - MD5, SHA-1, SHA-2, SHA-3, Keccak
34. Public Key Infrastructure (PKI) - Certificados X.509, CAs, Revogação, Cadeia de Confiança
35. Criptografia Simétrica - AES, DES, 3DES e modos de operação CBC, ECB, CTR, GCM
36. Criptografia de Teoria dos Números - Números Primos, Fatorização, Teorema de Euler, Matemática RSA
37. Discrete Logarithm Problem - grupos cíclicos, geradores, ordem, segurança
38. Criptografia baseada em reticulado - LWE, RLWE, NTRU, Pós-quântica, Kyber, Dilithium
39. Movimento Cypherpunk - Manifesto, Timothy May, Eric Hughes, Mailing List, Privacidade
40. Criptografia da NSA: Suite A, Suite B, Dual_EC_DRBG, Backdoors e Curvas NIST
41. Mineração de Bitcoin - ASIC, pools, ajuste de dificuldade, recompensa por bloco, halving
42. Ethereum 2.0 - beacon chain, sharding, merge, validators, attestations
43. Protocolos DeFi - AMM, pools de liquidez, Uniswap, Compound, Aave, yield farming
44. Stablecoins - USDT, USDC, DAI, algorithmic, collateralized, peg mechanisms
45. Layer 2 solutions - rollups, optimistic, zk-rollups, state channels, sidechains
46. Cryptocurrency exchanges - order books, matching engines, custody, hot/cold wallets
47. Criptografia de Carteira - HD wallets, BIP32, BIP39, frases de semente, caminhos de derivação
48. Computação Multi-Parte (MPC), Assinaturas de Limiar (TSS) e Geração de Chave Distribuída (DKG)
49. Verifiable Random Functions (VRF) - randomness beacon, lottery, leader selection
50. Escalabilidade de Blockchain - TPS, Tamanho do Bloco, Sharding, State Bloat, Pruning

---

# 1. Ralph Merkle - Árvores de Merkle

## Equações e Fórmulas

$$
S = D_A(M)
$$

- E_B(S)
$$
y = F(x)
$$

$$
x = S_ia (6.26)
$$

$$
S_K(P) = C
$$

$$
P = S_K^{-1}(C)
$$

$$
D_K(E_K(M)) = M
$$

$$
E_K(D_K(M)) = M
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| P | Plaintext |
| C | Ciphertext |
| K | Key |
| S_K | Enciphering function under key K |
| E, E_K | Enciphering key / Public key |
| D, D_K | Deciphering key / Secret key |
| M | Message |
| S | Signed message |
| F | One-way hash function |
| x, y | variables in the hash function |
| n | size of the message in bits |
| s | size of the message in bits |

## Algoritmos e Protocolos

```
One-way hash function: A function that is easy to compute but difficult to invert, mapping large data to smaller fixed-size outputs.
Public Key Cryptosystem using Puzzles: A method for establishing a secret key over an insecure channel by solving cryptographic puzzles.
Certified Digital Signature: A scheme to create digital signatures where the authenticity of the signature can be verified by anyone.
Trapdoor Knapsack: A public-key cryptosystem based on the subset sum problem (knapsack problem), where the public key is an 'easy' knapsack problem to solve and the private key is the 'trapdoor' information that makes it easy.
```

## Vulnerabilidades

- Small values of 'n' in the trapdoor knapsack system weaken its security, making it susceptible to attacks similar to the greatest common divisor algorithm. The security of the DES is controversial.

---

# 2. Whitfield Diffie - troca de chaves Diffie-Hellman, criptografia de chave pública, New Directions in Cryptography 1976, Sun Microsystems

## Equações e Fórmulas

$$
A = g^a \mod p
$$

$$
B = g^b \mod p
$$

$$
s = B^a \mod p
$$

$$
s = A^b \mod p
$$

$$
(g^a \mod p)^b \mod p = (g^b \mod p)^a \mod p
$$

$$
K = KDF(Y^x, B^x, Y^a, X, Y, A, B)
$$

$$
g^{abc} \mod p
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| p | módulo primo |
| g | base (raiz primitiva módulo p) |
| a | chave privada de Alice |
| b | chave privada de Bob |
| A | chave pública de Alice |
| B | chave pública de Bob |
| s | segredo compartilhado |
| x, y | chaves efêmeras |
| X, Y | chaves públicas efêmeras |
| IKA, EKA | chave de identidade e chave efêmera de Alice (X3DH) |
| IKB, SPKB, OPKB | chave de identidade, prekey assinada e prekey de uso único de Bob (X3DH) |
| K | chave derivada |

## Algoritmos e Protocolos

```
Troca de chaves Diffie-Hellman: 1. Alice e Bob concordam publicamente com um módulo primo `p` e uma base `g`. 2. Alice escolhe um inteiro secreto `a` e envia a Bob `A = g^a \mod p`. 3. Bob escolhe um inteiro secreto `b` e envia a Alice `B = g^b \mod p`. 4. Alice calcula `s = B^a \mod p`. 5. Bob calcula `s = A^b \mod p`. 6. Alice e Bob agora compartilham o segredo `s`.
 Triple Diffie-Hellman (3-DH): Utiliza chaves de longo prazo (a, b) e chaves efêmeras (x, y). O segredo compartilhado K é derivado usando uma Key Derivation Function (KDF) a partir de uma combinação das chaves públicas e privadas.
 Extended Triple Diffie–Hellman (X3DH): Usado no Signal Protocol. Utiliza uma chave de identidade (IK), uma chave efêmera (EK) e, para o respondente, uma chave pré-assinada (SPK) e uma chave pré-compartilhada de uso único (OPK).
 Operação com mais de duas partes: Um processo iterativo onde cada participante eleva o valor intermediário à sua chave privada e o passa para o próximo, até que todos tenham contribuído.
```

## Vulnerabilidades

- Ataque Man-in-the-Middle (MitM): Um invasor intercepta a comunicação e estabelece trocas de chaves separadas com cada parte, personificando-as. A autenticação é necessária para prevenir isso.
- Ataque de Negação de Serviço (DoS): Um invasor pode forçar o servidor a realizar cálculos dispendiosos, consumindo recursos.
- Logjam Attack: Pré-computação para grupos DH comumente usados (especialmente de 1024 bits ou menos), permitindo que um invasor quebre a criptografia.
- Computadores Quânticos: O algoritmo de Shor pode quebrar o DH resolvendo o problema do logaritmo discreto.
- Geradores de números aleatórios fracos: Se as chaves privadas puderem ser previstas, a segurança é comprometida.
- Campos de característica pequena: Podem ser menos seguros.
- Ordem do grupo G: Deve ter um fator primo grande para evitar o algoritmo de Pohlig-Hellman.

---

# 3. Martin Hellman - protocolo Diffie-Hellman, criptografia assimétrica, logaritmo discreto, Stanford University

## Equações e Fórmulas

$$
Y = \alpha^X \mod q
$$

$$
X = \log_{\alpha} Y \mod q
$$

$$
K_{ij} = Y_i^{X_j} \mod q
$$

$$
K_{ij} = (\alpha^{X_i})^{X_j} \mod q
$$

$$
K_{ij} = Y_j^{X_i} \mod q
$$

$$
K_{ij} = (\alpha^{X_j})^{X_i} \mod q
$$

$$
Y_i = \alpha^{X_i} \mod q
$$

$$
K_{ij} = \alpha^{X_i X_j} \mod q
$$

$$
f(X) = S_K(P_0)
$$

$$
f(X) = P_0
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| q | um número primo |
| alpha | uma raiz primitiva de q |
| X | a chave privada de um usuário, um inteiro entre 1 e q-1 |
| Y | a chave pública de um usuário |
| Kij | a chave secreta compartilhada entre os usuários i e j |
| f(X) | uma função de mão única |
| SK | uma função de cifragem |
| P0 | um texto plano padrão |
| C | um texto cifrado |

## Algoritmos e Protocolos

```
Protocolo de troca de chaves Diffie-Hellman: 1. Dois usuários, i e j, concordam publicamente com um número primo q e uma raiz primitiva alpha. 2. O usuário i gera uma chave privada aleatória Xi e calcula sua chave pública Yi = alpha^Xi mod q. 3. O usuário j gera uma chave privada aleatória Xj e calcula sua chave pública Yj = alpha^Xj mod q. 4. Os usuários trocam suas chaves públicas. 5. O usuário i calcula a chave secreta compartilhada Kij = Yj^Xi mod q. 6. O usuário j calcula a chave secreta compartilhada Kij = Yi^Xj mod q. Ambas as chaves são idênticas, pois Kij = (alpha^Xj)^Xi mod q = (alpha^Xi)^Xj mod q = alpha^(Xi*Xj) mod q. Criptosistema de chave pública usando uma função de mão única: 1. Um usuário A deseja enviar uma mensagem segura para um usuário B. 2. O usuário B possui uma chave de decifragem secreta D e uma chave de cifragem pública E. 3. O usuário A obtém a chave pública E de B e a utiliza para cifrar a mensagem M, resultando no texto cifrado C = E(M). 4. O usuário B utiliza sua chave secreta D para decifrar a mensagem: M = D(C) = D(E(M)).
```

## Vulnerabilidades

- Vulnerabilidade a ataques man-in-the-middle: um invasor pode interceptar as chaves públicas e substituí-las por suas próprias, enganando as duas partes para que estabeleçam chaves secretas com o invasor em vez de uma com a outra. A autenticação das chaves públicas é necessária para evitar este ataque.
- A segurança do protocolo depende da dificuldade computacional de calcular logaritmos discretos. Se um algoritmo eficiente para calcular logaritmos discretos for descoberto, o protocolo será quebrado.
- O protocolo não fornece autenticação por si só. As identidades das partes não são verificadas, tornando-o vulnerável a ataques de representação se não for usado em conjunto com um mecanismo de autenticação.
- Ataque Logjam: um invasor man-in-the-middle pode forçar uma conexão TLS a usar criptografia de nível de exportação de 512 bits, permitindo que o invasor leia e modifique os dados. Isso se deve a uma falha no protocolo TLS, e não a uma vulnerabilidade de implementação.
- Ameaças de adversários de nível estatal: Muitos servidores usam os mesmos números primos para a troca de chaves Diffie-Hellman. Um invasor com recursos suficientes (como um estado-nação) pode realizar um cálculo de pré-computação caro no número primo. Depois que essa pré-computação é concluída, o invasor pode quebrar rapidamente as chaves de sessão individuais que usam esse primo.

---

# 4. David Chaum - Dinheiro Digital, Blind Signatures, Mix Networks

## Equações e Fórmulas

$$
m' \equiv mr^e \pmod{N}
$$

$$
s' \equiv (m')^d \pmod{N}
$$

$$
s \equiv s' \cdot r^{-1} \pmod{N}
$$

$$
s \equiv m^d \pmod{N}
$$

$$
c \equiv m^e \pmod{N}
$$

$$
s' \equiv c^d \equiv m \pmod{N}
$$

- K_b(R0, mensagem)
- K_m(R1, K_b(R0, mensagem), B)
- K_m(S1, A), K_x
- K_m(S1, A), K_x(S0, resposta)

## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| m | mensagem original |
| N | módulo público RSA |
| e | expoente público RSA |
| d | expoente secreto RSA |
| r | fator de cegueira aleatório, relativamente primo a N |
| m' | mensagem cega |
| s' | assinatura cega |
| s | assinatura RSA válida de m |
| c | mensagem criptografada |
| K_m | Chave pública do Mix |
| K_b | Chave pública do destinatário B |
| A, B | Endereços do remetente e do destinatário |
| R0, R1, S0, S1 | Strings aleatórias (nonces/sais) para prevenção de ataques |
| K_x | Chave pública de uso único para respostas anônimas |
| Moeda (Coin) | Um número de série único que representa um valor monetário no DigiCash |
| Fator de Cegueira (Blinding Factor) | Um número aleatório usado para cegar a moeda no DigiCash |
| Chave Privada do Banco (Bank's Private Key) | A chave usada pelo banco para assinar as moedas no DigiCash |
| String de Identidade (Identity String) | Uma string secreta embutida na moeda para detectar gasto duplo em cenários offline no DigiCash |

## Algoritmos e Protocolos

```
Assinatura Cega (Blind Signature): O protocolo de assinatura cega RSA permite que uma entidade assine uma mensagem sem conhecer seu conteúdo. O processo envolve o "cegamento" da mensagem original `m` com um fator aleatório `r`, resultando em `m'`. A autoridade assina `m'`, produzindo `s'`. O autor da mensagem então remove o fator de cegueira para obter a assinatura final `s`, que é uma assinatura RSA válida para a mensagem original `m`.
Redes Mix (Mix Networks): O protocolo de redes mix visa o anonimato nas comunicações. As mensagens são criptografadas em camadas e enviadas através de uma série de servidores (mixes). Cada mix remove uma camada de criptografia, embaralha um lote de mensagens e as retransmite para o próximo destino. Isso quebra a ligação entre remetente e destinatário, dificultando a análise de tráfego. O protocolo também suporta endereços de retorno anônimos para permitir respostas sem revelar a identidade do remetente original.
DigiCash/eCash: O sistema DigiCash implementou um protocolo de dinheiro eletrônico anônimo baseado em assinaturas cegas. Os principais protocolos são: Retirada (Withdrawal), Pagamento (Payment), Depósito (Deposit) e mecanismos de Prevenção de Gasto Duplo (online com banco de dados e offline com "cut-and-choose" e "challenge-response").
```

## Vulnerabilidades

- Ataque de Cegueira RSA
- Análise de Tráfego em Redes Mix (Timing Attacks)
- Ataques Ativos e de Repetição em Redes Mix
- Comprometimento de Mixes
- Centralização do DigiCash como ponto único de falha
- Dependência da segurança do algoritmo RSA no DigiCash

---

# 5. Stuart Haber - Timestamping Criptográfico

## Equações e Fórmulas

$$
h(x) = y
$$

$$
C_n = (n, t_n, id_n, y_n, L_n)
$$

$$
L_n = (t_{n-1}, id_{n-1}, y_{n-1}, H(L_{n-1}))
$$

$$
s = \sigma(C_n)
$$

$$
s' = \sigma(n+1, t_{n+1}, id_{n+1}, y_{n+1}, L_{n+1})
$$

$$
L_n = [(t_{n-k}, id_{n-k}, y_{n-k}, H(L_{n-k})), \dots, (t_{n-1}, id_{n-1}, y_{n-1}, H(L_{n-1}))]
$$

$$
G(y) = (id_1, id_2, \dots, id_k)
$$

$$
s_j = \sigma_j(t, id, y)
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| h | uma família de funções de hash criptograficamente seguras e sem colisão |
| x | o documento a ser carimbado com data e hora |
| y | o valor de hash do documento x |
| l | o comprimento fixo da string de bits de saída da função de hash |
| TSS | Serviço de Carimbo de Data e Hora (Time-Stamping Service) |
| id | número de identificação do cliente |
| n | número de sequência do certificado de carimbo de data e hora |
| t_n | a hora da n-ésima solicitação |
| id_n | o número do cliente da n-ésima solicitação |
| y_n | o valor de hash da n-ésima solicitação |
| L_n | informações de vinculação do certificado emitido anteriormente |
| H | uma função de hash sem colisão usada pelo TSS |
| \sigma() | o procedimento de assinatura usado pelo TSS |
| s | o certificado assinado |
| k | o número de solicitações subsequentes a serem vinculadas |
| G | um gerador pseudoaleatório seguro |
| id_j | o j-ésimo número de identificação do cliente da saída de G(y) |
| s_j | a mensagem assinada do cliente id_j |
| \rho | a fração de clientes possivelmente desonestos |
| p | parâmetro de segurança |

## Algoritmos e Protocolos

```
1.  **Serviço de Carimbo de Data e Hora Confiável com Hash e Assinatura:** O cliente calcula o hash `y = h(x)` do documento `x`. O cliente envia o hash `y` para o TSS. O TSS anexa a data e a hora ao hash, assina este documento composto e o envia de volta ao cliente. O cliente verifica a assinatura.
2.  **Esquema de Vinculação (Variante 1):** O TSS recebe a n-ésima solicitação `(y_n, id_n)`. O TSS cria um certificado `C_n = (n, t_n, id_n, y_n, L_n)`, onde `L_n = (t_{n-1}, id_{n-1}, y_{n-1}, H(L_{n-1}))`. O TSS assina o certificado `s = \sigma(C_n)` e o envia ao cliente. O TSS envia o ID do próximo cliente, `id_{n+1}`, para o cliente atual. Para verificar, um desafiante pode seguir a cadeia de carimbos de data e hora para frente e para trás.
3.  **Esquema de Vinculação (Variante 2):** Semelhante à Variante 1, mas vincula às próximas `k` solicitações. A informação de vinculação é `L_n = [(t_{n-k}, id_{n-k}, y_{n-k}, H(L_{n-k})), ..., (t_{n-1}, id_{n-1}, y_{n-1}, H(L_{n-1}))]`. O TSS envia a lista dos próximos `k` IDs de clientes para o cliente atual.
4.  **Esquema de Confiança Distribuída:** O cliente usa o hash `y` como semente para um gerador pseudoaleatório `G` para obter uma k-tupla de IDs de clientes: `G(y) = (id_1, id_2, ..., id_k)`. O cliente envia a solicitação `(y, id)` para cada um desses `k` clientes. Cada um dos `k` clientes retorna uma mensagem assinada `s_j = \sigma_j(t, id, y)`. O carimbo de data e hora consiste em `[(y, id), (s_1, ..., s_k)]`.
```

## Vulnerabilidades

- Conluio com o TSS: No esquema ingênuo, o TSS pode conspirar com um cliente para forjar um carimbo de data e hora.
- Falsificação de Carimbos de Data e Hora: Um adversário pode tentar preparar uma cadeia falsa de carimbos de data e hora.
- Quebra da Função de Hash: Se a função de hash for quebrada, todos os carimbos de data e hora emitidos anteriormente serão questionados.
- Necessidade de Renovação: Os carimbos de data e hora podem precisar ser renovados com novas implementações antes que as antigas sejam quebradas.

---

# 6. W. Scott Stornetta - Timestamping Distribuído

## Equações e Fórmulas

$$
h: \{0, 1\}^* \rightarrow \{0, 1\}^l
$$

$$
y = h(x)
$$

$$
L_i = H(t_i, ID_i, y_i, L_{i-1})
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| h | função de hash criptográfica |
| x | documento a ser carimbado |
| y | valor de hash do documento |
| l | comprimento da saída do hash |
| TSS | Serviço de Carimbo de Tempo |
| ID_i | identificação do cliente i |
| t_i | tempo do carimbo de data/hora |
| y_i | hash do documento do cliente i |
| L_i | i-ésimo elo da cadeia de timestamp |
| L_{i-1} | elo anterior na cadeia |
| H | função de hash para vincular os carimbos de data/hora |

## Algoritmos e Protocolos

```
1. Solução Ingênua (Cofre Digital): O cliente transmite o documento para o TSS, que armazena uma cópia com data e hora. A verificação é feita por comparação direta.
2. Serviço de Carimbo de Tempo Confiável (com Hash e Assinatura): O cliente envia o hash do documento para o TSS, que o assina digitalmente com data e hora e o retorna ao cliente.
3. Esquema de Vinculação (Precursor do Blockchain): O TSS cria um vínculo (hash) que inclui o hash do documento atual, a hora, a ID do cliente e o hash do vínculo anterior, formando uma cadeia. Periodicamente, o hash do último vínculo é publicado.
```

## Vulnerabilidades

- Solução Ingênua: Violação de privacidade, alto custo de armazenamento e largura de banda, dependência da competência e confiança no TSS. TSS Confiável: Requer confiança total no TSS para não fraudar os carimbos de data/hora. Esquema de Vinculação: A segurança depende da resistência à colisão da função de hash e da ampla publicação dos hashes da cadeia.

---

# 7. Ronald Rivest - RSA algorithm, MIT, RC4, RC5, RC6, MD2, MD4, MD5, ring signatures, todos os trabalhos

## Equações e Fórmulas

$$
C \equiv M^e \pmod{n}
$$

$$
M \equiv C^d \pmod{n}
$$

$$
e \cdot d \equiv 1 \pmod{\phi(n)}
$$

$$
D(E(M)) = M
$$

$$
E(D(M)) = M
$$

$$
S = D_B(M)
$$

$$
M = E_B(S)
$$

$$
f_i(x) = x^{e_i} \pmod{n_i}
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| p, q | Dois números primos grandes e secretos |
| n | Módulo, o produto de p e q (n = p*q) |
| \phi(n) | Função totiente de Euler, \phi(n) = (p-1)(q-1) |
| e | Expoente público, um inteiro tal que 1 < e < \phi(n) e mdc(e, \phi(n)) = 1 |
| d | Expoente privado, o inverso multiplicativo de e módulo \phi(n) |
| M | Mensagem, um inteiro no intervalo [0, n-1] |
| C | Criptograma, um inteiro no intervalo [0, n-1] |
| E | Procedimento de encriptação |
| D | Procedimento de decriptação |
| S | Assinatura |
| D_B | Chave de decriptação de Bob |
| E_B | Chave de encriptação de Bob |
| w | Tamanho da palavra em bits (16, 32 ou 64) |
| r | Número de rodadas (0 a 255) |
| b | Tamanho da chave em bytes (0 a 2040) |
| K | A chave secreta |
| S | O array de subchaves da rodada |
| A, B | As duas palavras que compõem o bloco de texto a ser criptografado |
| P_w, Q_w | Constantes mágicas |
| A, B, C, D | Registradores de entrada de w bits |
| lg w | O logaritmo de base 2 de w |
| A, B, C, D | Registradores de 32 bits que mantêm o estado do hash |
| F | Uma função não linear |
| Mi | Um bloco de 32 bits da entrada da mensagem |
| Ki | Uma constante de 32 bits, diferente para cada rodada |
| F, G, H, I | Funções não lineares, uma para cada rodada |
| M[i] | O i-ésimo sub-bloco de 32 bits da mensagem |
| K[i] | Constantes de 32 bits, diferentes para cada operação |
| m | A mensagem a ser assinada |
| P_1, P_2, ..., P_r | As chaves públicas de todos os membros do anel |
| s | O índice do assinante real |
| S_s | A chave secreta do assinante real |
| σ | A assinatura em anel |
| v | Um valor de inicialização aleatório |
| x_i | Valores de entrada para as permutações trapdoor |
| y_i | Valores de saída das permutações trapdoor |
| g_i | A função de permutação trapdoor para o membro i |
| C_k,v | Uma função de combinação |
| f_i | A permutação trapdoor RSA para o membro i |
| e_i, n_i | A chave pública RSA para o membro i. |

## Algoritmos e Protocolos

```
RSA: Geração de Chaves - Escolha dois primos p e q, calcule n = p*q e phi(n) = (p-1)(q-1). Escolha e coprimo a phi(n) e calcule d como o inverso multiplicativo de e mod phi(n). Encriptação - C = M^e mod n. Decriptação - M = C^d mod n.
 RC5: Cifra de bloco com tamanho de bloco, número de rodadas e tamanho de chave variáveis. Consiste em expansão de chave, criptografia e descriptografia.
 RC6: Cifra de bloco baseada no RC5, com um tamanho de bloco de 128 bits e suporte para chaves de 128, 192 e 256 bits. Usa quatro registradores de trabalho e inclui uma multiplicação inteira como uma operação primitiva adicional.
 MD2: Processa mensagens em blocos de 128 bits, adicionando um checksum de 16 bytes. Usa um bloco auxiliar de 48 bytes e uma tabela S de 256 bytes, realizando 18 rodadas de permutação para cada bloco de mensagem.
 MD4: Processa mensagens em blocos de 512 bits, produzindo um digest de 128 bits. Consiste em 48 operações em três rodadas, usando funções não lineares.
 MD5: Processa mensagens em blocos de 512 bits e produz um hash de 128 bits. Opera em um estado de 128 bits e processa cada bloco em quatro rodadas de 16 operações.
 Assinaturas em Anel: Esquema de assinatura digital que pode ser executado por qualquer membro de um grupo de usuários, fornecendo anonimato.
```

## Vulnerabilidades

- RC5: Suscetível a ataques diferenciais com um número suficiente de textos simples escolhidos.
- MD2: Vulnerável a ataques de colisão, pré-imagem e pré-imagem aprimorados.
- MD4: Vulnerável a ataques de colisão e pré-imagem.
- MD5: Criptograficamente quebrado, com vulnerabilidades de colisão, pré-imagem e colisão de prefixo escolhido.
- Assinaturas em Anel: A segurança depende da segurança das permutações trapdoor subjacentes.

---

# 8. Adi Shamir - RSA algorithm, Shamir Secret Sharing, visual cryptography, differential cryptanalysis, Weizmann Institute

## Equações e Fórmulas

$$
(x^e)^d \equiv x \pmod{n}
$$

$$
c \equiv m^e \pmod{n}
$$

$$
c^d \equiv (m^e)^d \equiv m \pmod{n}
$$

$$
n = pq
$$

$$
\lambda(n) = \text{lcm}(p-1, q-1)
$$

$$
d \equiv e^{-1} \pmod{\lambda(n)}
$$

$$
d_p = d \pmod{p-1}
$$

$$
d_q = d \pmod{q-1}
$$

$$
q_{inv} = q^{-1} \pmod{p}
$$

$$
m_1 = c^{d_p} \pmod{p}
$$

$$
m_2 = c^{d_q} \pmod{q}
$$

$$
h = (q_{inv} \times (m_1 - m_2)) \pmod{p}
$$

$$
m = m_2 + h \times q
$$

$$
f(x) = a_0 + a_1x + a_2x^2 + \dots + a_{k-1}x^{k-1}
$$

$$
a_0 = f(0) = \sum_{j=0}^{k-1} y_j \prod_{m=0, m \neq j}^{k-1} \frac{x_m}{x_m - x_j}
$$

$$
\ell_j(x) = \prod_{m=0, m \neq j}^{k-1} \frac{x - x_m}{x_j - x_m}
$$

$$
f(x) = \sum_{j=0}^{k-1} y_j \ell_j(x)
$$

$$
H(V) \ge d
$$

$$
H(V) < d - \alpha m
$$

$$
m = 2^{k-1}
$$

$$
\alpha = 1/2^{k-1}
$$

$$
\Delta y = S(x \oplus \Delta x) \oplus S(x)
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| p | Um número primo grande |
| q | Um número primo grande |
| n | Módulo para as chaves pública e privada, n = pq |
| λ(n) | Função totiente de Carmichael, λ(n) = mcm(p-1, q-1) |
| e | Expoente da chave pública, 1 < e < λ(n) e mdc(e, λ(n)) = 1 |
| d | Expoente da chave privada, d ≡ e⁻¹ (mod λ(n)) |
| m | Mensagem de texto simples preenchida |
| c | Texto cifrado |
| d_p | d mod (p-1) |
| d_q | d mod (q-1) |
| q_inv | q⁻¹ mod p |
| m_1 | c^d_p mod p |
| m_2 | c^d_q mod q |
| h | (q_inv * (m_1 - m_2)) mod p |
| S | O segredo a ser compartilhado |
| n | O número de compartilhamentos a serem gerados |
| k | O número mínimo de compartilhamentos necessários para reconstruir o segredo |
| a_0, a_1, ..., a_{k-1} | Coeficientes do polinômio, onde a_0 = S |
| f(x) | O polinômio usado para gerar os compartilhamentos |
| D_i | O i-ésimo compartilhamento, consistindo em um par (x_i, f(x_i)) |
| q | Um número primo maior que n e o número de valores possíveis para o segredo |
| l_j(x) | O j-ésimo polinômio de base de Lagrange |
| x_j, y_j | As coordenadas de um ponto no polinômio |
| k | O número mínimo de compartilhamentos necessários para revelar o segredo |
| n | O número total de compartilhamentos |
| m | O número de subpixels em cada compartilhamento |
| d | O limiar de nível de cinza |
| α | A diferença relativa no peso de Hamming entre os compartilhamentos combinados de um pixel branco e um pixel preto |
| S | Uma matriz booleana n x m que descreve a estrutura resultante |
| V | O vetor m "OR"-ed booleano |
| H(V) | O peso de Hamming do vetor V |
| C0, C1 | Coleções de matrizes booleanas n x m |
| x | Texto simples |
| \Delta x | Diferença de texto simples |
| y | Texto cifrado |
| \Delta y | Diferença de texto cifrado |
| S | S-box |
| K | Chave |

## Algoritmos e Protocolos

```
RSA: O algoritmo RSA envolve quatro etapas: geração de chaves, distribuição de chaves, operação de chave pública (usada para criptografia ou verificação de uma assinatura) e operação de chave privada (usada para descriptografia ou assinatura de uma mensagem). A geração de chaves envolve a escolha de dois números primos grandes, p e q, e o cálculo de n = pq. A função totiente de Carmichael, λ(n) = mcm(p-1, q-1), é então calculada. Um inteiro e é escolhido tal que 1 < e < λ(n) e mdc(e, λ(n)) = 1. Finalmente, d é determinado como d ≡ e⁻¹ (mod λ(n)). A chave pública é (n, e) e a chave privada é d. A criptografia é realizada calculando c ≡ m^e (mod n), e a descriptografia é realizada calculando m ≡ c^d (mod n).
Compartilhamento Secreto de Shamir: O Compartilhamento Secreto de Shamir é um esquema de limiar (k, n) que divide um segredo S em n compartilhamentos, onde qualquer k compartilhamentos podem reconstruir o segredo, mas qualquer k-1 compartilhamentos não revelam nenhuma informação sobre S. O esquema é baseado na interpolação de polinômios sobre campos finitos. Um polinômio f(x) de grau k-1 é construído com o segredo como o termo constante, a_0 = S. Os outros coeficientes, a_1, ..., a_{k-1}, são escolhidos aleatoriamente. Os compartilhamentos são pontos no polinômio, (x_i, f(x_i)). A reconstrução do segredo é feita por interpolação de Lagrange para encontrar f(0) = S.
Criptografia Visual: A criptografia visual é um esquema criptográfico que permite que informações visuais (imagens, texto, etc.) sejam criptografadas de tal forma que a descriptografia possa ser realizada pelo sistema visual humano, sem o auxílio de computadores. O modelo básico consiste em duas coleções de matrizes booleanas n x m, C0 e C1. Para compartilhar um pixel branco, o revendedor escolhe aleatoriamente uma das matrizes em C0 e, para compartilhar um pixel preto, o revendedor escolhe aleatoriamente uma das matrizes em C1. A matriz escolhida define a cor dos m subpixels em cada uma das n transparências. A solução é considerada válida se as seguintes três condições forem atendidas: 1. Para qualquer S em C0, o "ou" V de quaisquer k das n linhas satisfaz H(V) <= d - αm. 2. Para qualquer S em C1, o "ou" V de quaisquer k das n linhas satisfaz H(V) >= d. 3. Para qualquer subconjunto de q < k compartilhamentos, as duas coleções de matrizes q x m são indistinguíveis.
Criptoanálise Diferencial: A criptoanálise diferencial é uma forma geral de criptoanálise aplicável principalmente a cifras de bloco, mas também a cifras de fluxo e funções de hash criptográficas. No sentido mais amplo, é o estudo de como as diferenças na entrada de informações podem afetar a diferença resultante na saída. No caso de uma cifra de bloco, refere-se a um conjunto de técnicas para rastrear diferenças através da rede de transformação, descobrindo onde a cifra exibe comportamento não aleatório e explorando tais propriedades para recuperar a chave secreta. O método básico usa pares de textos simples relacionados por uma diferença constante. A diferença pode ser definida de várias maneiras, mas a operação OU-exclusivo (XOR) é usual. O invasor então calcula as diferenças dos textos cifrados correspondentes, na esperança de detectar padrões estatísticos em sua distribuição. O par de diferenças resultante é chamado de diferencial. Suas propriedades estatísticas dependem da natureza das S-boxes usadas para criptografia, então o invasor analisa os diferenciais (Δx, Δy) onde Δy = S(x ⊕ Δx) ⊕ S(x) para cada S-box S-box.
```

## Vulnerabilidades

- Ataques contra RSA simples
- Ataque de texto cifrado escolhido
- Ataque de texto simples escolhido
- Propriedade multiplicativa
- Fatoração do módulo
- Geração de chave defeituosa
- Expoente privado pequeno
- Expoente público pequeno
- Vulnerabilidade ROCA
- Geração de número aleatório fraca
- Ataques de temporização
- Ataques de texto cifrado escolhido adaptativos
- Ataques de análise de canal lateral
- Ataque de injeção de falhas

---

# 9. Leonard Adleman - Algoritmo RSA, Computação de DNA, USC, números primos, fatorização

## Equações e Fórmulas

$$
(m^e)^d \equiv m \pmod{n}
$$

$$
n = p \cdot q
$$

$$
\lambda(n) = \text{lcm}(p-1, q-1)
$$

$$
e \cdot d \equiv 1 \pmod{\lambda(n)}
$$

$$
c \equiv m^e \pmod{n}
$$

$$
m \equiv c^d \pmod{n}
$$

$$
s \equiv h(m)^d \pmod{n}
$$

$$
h(m) \equiv s^e \pmod{n}
$$

$$
d_p = d \pmod{p-1}
$$

$$
d_q = d \pmod{q-1}
$$

$$
q_{inv} = q^{-1} \pmod{p}
$$

$$
m_1 = c^{d_p} \pmod{p}
$$

$$
m_2 = c^{d_q} \pmod{q}
$$

$$
h = q_{inv} \cdot (m_1 - m_2) \pmod{p}
$$

$$
m = m_2 + h \cdot q
$$

$$
O((\log n)^{c \log \log \log n})
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| p, q | Dois números primos grandes e distintos (secretos) |
| n | Módulo para as operações de criptografia e decriptografia (público) |
| e | Expoente público, usado para criptografar mensagens (público) |
| d | Expoente privado, usado para decriptografar mensagens (secreto) |
| \lambda(n) | Função totiente de Carmichael (secreta) |
| m | Mensagem original em formato numérico |
| c | Mensagem criptografada (ciphertext) |
| h(m) | Função de hash aplicada à mensagem m |
| s | Assinatura digital da mensagem |
| d_p, d_q, q_{inv} | Coeficientes para otimização com o Teorema Chinês do Resto (secretos) |
| O_i | Sequência de DNA para o vértice i |
| O_{i->j} | Sequência de DNA para a aresta i->j |
| O'_i | Sequência complementar de O_i |
| v_in, v_out | Vértices de início e fim |

## Algoritmos e Protocolos

```
Geração de Chaves RSA: 1. Escolher dois números primos grandes, p e q. 2. Calcular n = p * q. 3. Calcular λ(n) = lcm(p-1, q-1). 4. Escolher um inteiro e tal que 1 < e < λ(n) e gcd(e, λ(n)) = 1. 5. Calcular d como o inverso multiplicativo modular de e módulo λ(n).
 Criptografia RSA: 1. A mensagem m é convertida em um número. 2. O ciphertext c é calculado como c = m^e (mod n).
 Decriptografia RSA: 1. A mensagem original m é recuperada calculando m = c^d (mod n).
 Algoritmo Molecular para o Problema do Caminho Hamiltoniano: 1. Geração de Caminhos Aleatórios com moléculas de DNA. 2. Seleção de Caminhos Válidos (Início e Fim) via PCR. 3. Seleção por Comprimento via eletroforese em gel. 4. Verificação de Passagem por Todos os Vértices via purificação por afinidade. 5. Detecção do Resultado.
 Teste de Primalidade Adleman-Pomerance-Rumely (APR): 1. Seleção de um conjunto de pequenos primos q cujo produto s excede sqrt(n). 2. Verificação de uma série de congruências em corpos ciclotômicos Z[ζ_q]. 3. Uso de somas de Jacobi para relacionar o comportamento de n. 4. Se n passar em todos os testes, é primo.
```

## Vulnerabilidades

- Ataques de Fatoração (GNFS, Algoritmo de Shor)
- Expoentes de Criptografia Baixos sem padding
- Ataques de Texto Plano Escolhido (determinismo)
- Propriedade Multiplicativa permitindo ataques de texto cifrado escolhido
- Ataques de Timing
- Ataques de Canal Lateral (consumo de energia, predição de desvios)
- Geração de Chaves Fraca (primos próximos, vulnerabilidade ROCA)
- Ataques a Esquemas de Padding (Ataque de Bleichenbacher no PKCS#1 v1.5)
- Escalabilidade da computação de DNA
- Erros em operações bioquímicas (ligação, PCR)
- Ineficiência do algoritmo de força bruta da computação de DNA.

---

# 10. Hal Finney - Reusable Proof of Work (RPOW), PGP, primeira transação Bitcoin, cypherpunks

## Equações e Fórmulas

$$
SHA-1(text_string) = 0...0<hash_value>
$$

- 1 / (2^N)
$$
m = SK^e mod n
$$

$$
M = m + k*n
$$

$$
m = M mod n
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| N | O número de bits zero iniciais na colisão do hashcash. |
| collision size | O número de bits zero iniciais, determinando o valor do hashcash. |
| resource string | Uma string incorporada em um token hashcash para identificar seu uso pretendido e prevenir a reutilização em outros contextos. |
| L | Uma potência de 256 acima do módulo n. Para segurança, a próxima potência de 256 acima de n*(2^64). |
| n | O módulo RSA. |
| t | A parte inteira de L/n. |
| s | O resto da divisão de L por n (ou seja, L = n*t + s). |
| SK | A chave de sessão IDEA do PGP. |
| m | A versão criptografada em RSA da chave de sessão. |
| k | Um número aleatório no intervalo [0,t]. |
| M | A chave criptografada "oculta" (stegged). |

## Algoritmos e Protocolos

```
Criação de Hashcash: 1. Comece com uma string base. 2. Modifique iterativamente a string (por exemplo, incrementando um contador). 3. Para cada string modificada, calcule seu hash SHA-1. 4. Verifique se o hash possui o número desejado de bits zero iniciais (N). 5. Se possuir, a string é um token hashcash válido. Caso contrário, continue a iteração.
 Verificação de Hashcash: 1. Receba um token hashcash. 2. Calcule o hash SHA-1 do token. 3. Conte o número de bits zero iniciais. 4. Verifique se o número de bits zero atende à dificuldade exigida. 5. Verifique a `resource string` para garantir que o token está sendo usado para o propósito pretendido. 6. Consulte um banco de dados local para garantir que o token não foi usado anteriormente.
 Troca de Tokens RPOW: 1. Um usuário envia um token POW (hashcash) para um servidor RPOW. 2. O servidor verifica o token POW. 3. O servidor cria um novo token RPOW de valor igual. 4. O servidor registra a propriedade do novo token RPOW para o usuário. 5. O usuário pode então transferir o token RPOW para outro usuário, assinando uma ordem de transferência. 6. O destinatário pode então trocar o token RPOW no servidor por um novo, continuando a cadeia.
 Algoritmo PGP "Truly Stealthy": 1. Escolha um SK aleatório em [0,n). 2. Criptografe-o com RSA para formar `m = SK^e mod n`. 3. Escolha um k aleatório em [0,t]. 4. Calcule a chave criptografada "oculta" como `M = m + k*n`. 5. Se M não estiver em [0,L) (ou seja, se M >= L), falhe. A chance de isso acontecer é menor que 1 em 2^64. 6. Caso contrário, armazene M como um número binário bruto, ocupando `log base 256 de L` bytes.
 Recuperação da Chave: 1. Pegue os primeiros `log base 256 de L` bytes como M. 2. Calcule `m = M mod n`.
```

## Vulnerabilidades

- Gasto duplo de hashcash: Um token hashcash poderia ser usado várias vezes se não fossem as verificações da `resource string` e do banco de dados local.
- Falsificação de tokens RPOW: O sistema depende de um servidor confiável (executando em um coprocessador criptográfico seguro) para prevenir a falsificação. Um servidor comprometido poderia potencialmente criar tokens RPOW fraudulentos.
- Distribuição não uniforme do byte de ordem superior: No PGP "Stealth" original, o byte de ordem superior da chave de sessão criptografada tinha uma distribuição não uniforme, tornando-o distinguível de ruído aleatório.

---

# 11. Adam Back - Hashcash, proof of work, Blockstream, cypherpunks, anti-spam PoW

## Equações e Fórmulas

$$
x \stackrel{b}{=} y \iff \text{os primeiros } b \text{ bits de } x \text{ e } y \text{ são idênticos}
$$

$$
MINT(s, k) \rightarrow c \text{ tal que } H(s, c) \text{ tenha } k \text{ zeros à esquerda}
$$

$$
VALUE(s, c, k) \rightarrow \text{True se } H(s, c) \text{ tem } k \text{ zeros à esquerda}
$$

$$
CHAL(s, k) \rightarrow r
$$

$$
MINT(s, r, k) \rightarrow c \text{ tal que } H(s, r, c) \text{ tenha } k \text{ zeros à esquerda}
$$

$$
VALUE(s, r, c, k) \rightarrow \text{True se } H(s, r, c) \text{ tem } k \text{ zeros à esquerda}
$$

$$
mac = MAC_{sk}(t, s, conn, r)
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| s | string de serviço (identificador único do serviço) |
| k | parâmetro de dificuldade (número de zeros à esquerda no hash) |
| c | contador (nonce) |
| H | função de hash (ex: SHA-1) |
| r | desafio aleatório (na versão interativa) |
| t | timestamp |
| conn | parâmetros da conexão |
| sk | chave secreta do servidor |
| mac | código de autenticação de mensagem |

## Algoritmos e Protocolos

```
Hashcash Não-Interativo (Anti-Spam): 1. O cliente cria um cabeçalho de email. 2. O cliente adiciona um campo `X-Hashcash` ao cabeçalho, contendo: `ver` (versão), `bits` (dificuldade `k`), `date` (data/hora), `resource` (email do destinatário), `ext` (extensões), `rand` (string aleatória), `counter` (contador). 3. O cliente itera sobre o `counter`, calculando o hash (ex: SHA-1) do cabeçalho `X-Hashcash` até que o resultado tenha `k` zeros à esquerda. 4. O servidor verifica o hash
 se for válido e inédito, o email é aceito.
 Hashcash Interativo (Defesa de DoS): 1. O cliente inicia uma conexão (ex: TCP SYN). 2. O servidor, sob carga, responde com um desafio `r` (ex: no TCP SYN-ACK). 3. O cliente deve encontrar um contador `c` tal que `H(s, r, c)` tenha `k` zeros à esquerda. 4. O cliente envia `c` de volta ao servidor (ex: no TCP ACK). 5. O servidor verifica a solução e, se correta, estabelece a conexão.
```

## Vulnerabilidades

- Ataques de Pré-computação: Um atacante pode pré-computar tokens para usar em um ataque concentrado. Mitigado com timestamps ou desafios aleatórios.
- Ataques de Replay (Gasto Duplo): O mesmo token pode ser reutilizado. O servidor deve manter um banco de dados de tokens já utilizados para evitar isso.
- Vantagem do Hardware: Usuários com hardware mais rápido podem gerar tokens mais rapidamente.

---

# 12. Nick Szabo - Contratos Inteligentes e Bit Gold

## Equações e Fórmulas

- Nenhuma fórmula matemática específica ou equação foi encontrada no trabalho de Nick Szabo sobre contratos inteligentes ou bit gold. Seu trabalho é mais conceitual e descritivo.

## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| collateral | Ativos que garantem a execução do contrato |
| bonding | Mecanismos que garantem o cumprimento das obrigações |
| property rights | Direitos de propriedade definidos no contrato |
| challenge-response protocol | Protocolo para verificar a identidade e autorização do proprietário |
| smart lien protocol | Protocolo para transferir o controle de um ativo em caso de inadimplência |
| challenge string | Uma string de bits pública usada como desafio |
| proof of work string | O resultado do trabalho computacional, gerado a partir da challenge string |
| benchmark function | Uma função que mede o custo computacional para gerar a proof of work string |
| timestamp | Um registro de tempo seguro e distribuído |
| distributed property title registry | Um registro distribuído para rastrear a propriedade do bit gold |

## Algoritmos e Protocolos

```
Contratos Inteligentes (Exemplo de Automóvel): 1. Um bloqueio para permitir seletivamente a entrada do proprietário e excluir terceiros. 2. Uma "porta dos fundos" para permitir a entrada do credor. 3. A "porta dos fundos" do credor é ativada apenas em caso de não pagamento por um determinado período. 4. O pagamento eletrônico final desativa permanentemente a "porta dos fundos".
 Bit Gold: 1. Uma "challenge string" pública é criada. 2. Um participante gera a "proof of work string" a partir da "challenge string" usando uma "benchmark function". 3. A "proof of work" é carimbada com data/hora de forma segura e distribuída. 4. O participante adiciona a "challenge string" e a "proof of work" com carimbo de data/hora a um registro de títulos de propriedade distribuído. 5. A última "proof of work" criada fornece a "challenge string" para a próxima. 6. Para verificar a propriedade, um segundo participante verifica a cadeia de títulos no registro. 7. Para avaliar o valor, um segundo participante verifica a "challenge string", a "proof of work" e o carimbo de data/hora.
```

## Vulnerabilidades

- Contratos Inteligentes: A revogação da operação de um carro enquanto ele está em alta velocidade na estrada seria um problema.
- Bit Gold: A dependência da arquitetura do computador, não apenas da matemática abstrata, o que pode permitir que um produtor de baixo custo inunde o mercado. A não fungibilidade do bit gold, exigindo que os negociantes combinem peças de valores diferentes em unidades maiores de valor aproximadamente igual.

---

# 13. Wei Dai - b-money, criptografia, Crypto++

## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| K_A | Pseudônimo (chave pública) de um participante |
| K_B | Pseudônimo (chave pública) de outro participante |
| K_C | Pseudônimo (chave pública) do árbitro |
| X | Unidades de dinheiro a serem transferidas |
| P | Um problema computacional a ser resolvido |
| MU | Unidades Monetárias |

## Algoritmos e Protocolos

```
b-money: Criação de Dinheiro (resolução de problema computacional), Transferência de Dinheiro (transmissão de mensagem assinada), Execução de Contratos (débito/crédito com base em reparações máximas)
 Crypto++: GCM, CCM, EAX, ChaCha20Poly1305, XChaCha20Poly1305, AES, RSA, DSA, ECDSA, etc.
```

## Vulnerabilidades

- A avaliação do custo do esforço computacional para a criação de dinheiro no b-money é problemática
- O primeiro protocolo do b-money é impraticável por depender de um canal de transmissão anônimo, síncrono e à prova de bloqueio.

---

# 14. Satoshi Nakamoto - Bitcoin whitepaper, blockchain, proof of work, consenso distribuído, UTXO model

## Equações e Fórmulas

$$
P_z = (p/q)^z
$$

$$
q_z = ((1 - (p/q)^z) / (1 - p/q)) * (p/q)^z
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| p | probabilidade de um nó honesto encontrar o próximo bloco |
| q | probabilidade de o atacante encontrar o próximo bloco |
| z | número de blocos que o atacante precisa alcançar |

## Algoritmos e Protocolos

```
1. Novas transações são transmitidas para todos os nós. 2. Cada nó coleta novas transações em um bloco. 3. Cada nó trabalha para encontrar uma prova de trabalho para seu bloco. 4. Quando um nó encontra uma prova de trabalho, ele transmite o bloco para todos os nós. 5. Os nós aceitam o bloco somente se todas as transações nele forem válidas e ainda não tiverem sido gastas. 6. Os nós expressam sua aceitação do bloco trabalhando na criação do próximo bloco na cadeia, usando o hash do bloco aceito como o hash anterior.
```

## Vulnerabilidades

- Ataque de 51%: se mais da metade do poder da CPU da rede for controlada por um único atacante, ele pode gerar uma cadeia alternativa mais longa que a cadeia honesta e reverter transações.

---

# 15. K. Eric Drexler - nanotecnologia, Engines of Creation, molecular assemblers, MIT, Foresight Institute

## Equações e Fórmulas

- Nenhuma equação ou fórmula matemática foi encontrada nas fontes pesquisadas.

## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|

## Algoritmos e Protocolos

```
Nenhum algoritmo ou pseudocódigo detalhado foi encontrado nas fontes pesquisadas. O trabalho de Drexler é mais conceitual do que uma implementação algorítmica.
```

## Vulnerabilidades

- A principal vulnerabilidade discutida no trabalho de Drexler é o cenário de "grey goo", onde montadores moleculares autorreplicantes poderiam consumir descontroladamente a biosfera.

---

# 16. RSA Algorithm - Fatorização de inteiros, exponenciação modular, chaves pública/privada

## Equações e Fórmulas

$$
`n = p \times q`
$$

$$
`\lambda(n) = \text{lcm}(p-1, q-1)`
$$

$$
`1 < e < \lambda(n)` e `\text{gcd}(e, \lambda(n)) = 1`
$$

$$
`d \equiv e^{-1} \pmod{\lambda(n)}`
$$

$$
`c \equiv m^e \pmod{n}`
$$

$$
`m \equiv c^d \pmod{n}`
$$

$$
`(m^e)^d \equiv m \pmod{n}`
$$

$$
`h = \text{hash}(m)`
$$

$$
`s \equiv h^d \pmod{n}`
$$

$$
`s^e \equiv h \pmod{n}`
$$

$$
`d_P = d \pmod{p-1}`
$$

$$
`d_Q = d \pmod{q-1}`
$$

$$
`q_{\text{inv}} = q^{-1} \pmod{p}`
$$

$$
`m_1 = c^{d_P} \pmod{p}`
$$

$$
`m_2 = c^{d_Q} \pmod{q}`
$$

$$
`h = q_{\text{inv}} \times (m_1 - m_2) \pmod{p}`
$$

$$
`m = m_2 + h \times q`
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| `p`, `q` | Dois números primos grandes e distintos, mantidos em segredo |
| `n` | Módulo RSA, produto de `p` e `q`. É parte da chave pública |
| `λ(n)` | Função totiente de Carmichael de `n`, mantida em segredo |
| `e` | Expoente da chave pública, um inteiro tal que `1 < e < λ(n)` e `gcd(e, λ(n)) = 1` |
| `d` | Expoente da chave privada, o inverso multiplicativo modular de `e` módulo `λ(n)` |
| `m` | Mensagem original (texto claro) |
| `c` | Mensagem criptografada (texto cifrado) |
| `h` | Valor de hash da mensagem |
| `s` | Assinatura digital |
| `d_P`, `d_Q` | Expoentes para otimização com o Teorema Chinês do Resto |
| `q_inv` | Coeficiente para otimização com o Teorema Chinês do Resto |

## Algoritmos e Protocolos

```
### Geração de Chave
1.  Escolha dois números primos grandes e distintos, `p` e `q`.
2.  Calcule `n = p * q`.
3.  Calcule `λ(n) = lcm(p-1, q-1)`.
4.  Escolha um inteiro `e` tal que `1 < e < λ(n)` e `gcd(e, λ(n)) = 1`.
5.  Determine `d` como `d ≡ e⁻¹ (mod λ(n))`.
6.  A chave pública é `(n, e)` e a chave privada é `d`.

### Criptografia
1.  Receba a mensagem `m`.
2.  Calcule o texto cifrado `c ≡ m^e (mod n)`.

### Decriptografia
1.  Receba o texto cifrado `c`.
2.  Calcule a mensagem `m ≡ c^d (mod n)`.

### Assinatura Digital
1.  Calcule o hash da mensagem: `h = hash(m)`.
2.  Crie a assinatura: `s ≡ h^d (mod n)`.

### Verificação de Assinatura
1.  Receba a mensagem `m` e a assinatura `s`.
2.  Calcule o hash da mensagem: `h = hash(m)`.
3.  Verifique se `s^e ≡ h (mod n)`.
```

## Vulnerabilidades

- - **Ataques de Chave Pequena:** Se o expoente de criptografia `e` for pequeno (ex: 3) e a mensagem `m` for pequena, `m^e` pode ser menor que `n`, permitindo a recuperação de `m` calculando a raiz e-ésima inteira do texto cifrado.
- **Ataque de Håstad (Broadcast Attack):** Enviar a mesma mensagem para múltiplos destinatários com o mesmo expoente `e` mas diferentes módulos `n` pode permitir a recuperação da mensagem original usando o Teorema Chinês do Resto.
- **Não-Semântica:** O RSA sem preenchimento (padding) é um algoritmo determinístico, o que o torna vulnerável a ataques de texto plano escolhido. Um atacante pode criptografar textos prováveis e comparar com o texto cifrado.
- **Propriedade Multiplicativa:** A propriedade `(m1^e * m2^e) ≡ (m1*m2)^e (mod n)` permite ataques de texto cifrado escolhido. Um atacante pode obter a decriptografia de um texto cifrado `c` ao pedir a decriptografia de `c' = c * r^e`.
- **Fatoração do Módulo:** A segurança do RSA depende da dificuldade de fatorar o módulo `n`. Se `n` for fatorado, a chave privada `d` pode ser calculada. O Algoritmo de Shor é um algoritmo quântico que pode fatorar inteiros em tempo polinomial.
- **Ataques de Timing:** Variações no tempo de decriptografia podem vazar informações sobre a chave privada.
- **Ataques de Análise de Consumo de Energia:** O consumo de energia do dispositivo durante as operações criptográficas pode revelar informações sobre a chave.
- **Ataques de Falha:** Induzir falhas no hardware durante a computação pode levar à recuperação da chave.

---

# 17. Diffie-Hellman Key Exchange - logaritmo discreto, grupos cíclicos, troca de chaves, todas as equações

## Equações e Fórmulas

$$
`A = g^a \pmod{p}`
$$

$$
`B = g^b \pmod{p}`
$$

$$
`s = B^a \pmod{p}`
$$

$$
`s = A^b \pmod{p}`
$$

$$
`A^b \pmod{p} = (g^a)^b \pmod{p} = g^{ab} \pmod{p}`
$$

$$
`B^a \pmod{p} = (g^b)^a \pmod{p} = g^{ba} \pmod{p}`
$$

$$
`g^{ab} \pmod{p}`
$$

$$
`g^{abc} \pmod{p}`
$$

$$
`g^{bc} \pmod{p}`
$$

$$
`g^{ca} \pmod{p}`
$$

$$
`K = \text{KDF}(Y^x, B^x, Y^a, X, Y, A, B)`
$$

$$
`K = \text{KDF}(X^y, X^b, A^y, X, Y, A, B)`
$$

$$
`(g^a \pmod{p}, g, p)`
$$

$$
`(g^a)^b \pmod{p}`
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| p | um número primo (módulo) |
| g | uma raiz primitiva módulo p (base) |
| a | o inteiro secreto de Alice (chave privada) |
| b | o inteiro secreto de Bob (chave privada) |
| A | a chave pública de Alice |
| B | a chave pública de Bob |
| s | o segredo compartilhado |
| G | um grupo cíclico finito |
| n | ordem do grupo G |
| x, y | chaves efêmeras |
| X, Y | chaves públicas efêmeras |
| IKA, IKB | chaves de identidade de Alice e Bob |
| EKA | chave efêmera de Alice |
| SPKB | chave pré-assinada de Bob |
| OPKB | chave pré-única de Bob |
| KDF | função de derivação de chave |

## Algoritmos e Protocolos

```
**Troca de Chaves Diffie-Hellman:**
1. Alice e Bob concordam publicamente em usar um módulo `p` e uma base `g`.
2. Alice escolhe um inteiro secreto `a` e envia a Bob `A = g^a mod p`.
3. Bob escolhe um inteiro secreto `b` e envia a Alice `B = g^b mod p`.
4. Alice calcula `s = B^a mod p`.
5. Bob calcula `s = A^b mod p`.
6. Alice e Bob agora compartilham um segredo `s`.

**Generalização para Grupos Cíclicos Finitos:**
1. Alice e Bob concordam com um número natural `n` e um elemento gerador `g` no grupo cíclico finito `G` de ordem `n`.
2. Alice escolhe um número natural aleatório `a` com `1 < a < n` e envia o elemento `g^a` de `G` para Bob.
3. Bob escolhe um número natural aleatório `b` com `1 < b < n` e envia o elemento `g^b` de `G` para Alice.
4. Alice calcula o elemento `(g^b)^a = g^{ba}` de `G`.
5. Bob calcula o elemento `(g^a)^b = g^{ab}` de `G`.

**Operação com Mais de Duas Partes (Exemplo com Alice, Bob e Carol):**
1. As partes concordam com os parâmetros do algoritmo `p` e `g`.
2. As partes geram suas chaves privadas, `a`, `b` e `c`.
3. Alice calcula `g^a mod p` e envia para Bob.
4. Bob calcula `(g^a)^b mod p = g^{ab} mod p` e envia para Carol.
5. Carol calcula `(g^{ab})^c mod p = g^{abc} mod p` e o usa como seu segredo.
6. Bob calcula `g^b mod p` e envia para Carol.
7. Carol calcula `(g^b)^c mod p = g^{bc} mod p` e envia para Alice.
8. Alice calcula `(g^{bc})^a mod p = g^{bca} mod p = g^{abc} mod p` e o usa como seu segredo.
9. Carol calcula `g^c mod p` e envia para Alice.
10. Alice calcula `(g^c)^a mod p = g^{ca} mod p` e envia para Bob.
11. Bob calcula `(g^{ca})^b mod p = g^{cab} mod p = g^{abc} mod p` e o usa como seu segredo.
```

## Vulnerabilidades

- - **Ataque Man-in-the-Middle:** O protocolo original não autentica as partes, tornando-o vulnerável a um invasor (Mallory) que se interpõe na comunicação, estabelecendo chaves separadas com Alice e Bob e retransmitindo as mensagens.
- **Ataque de Negação de Serviço (DoS):** Um invasor pode forçar o servidor a realizar cálculos computacionalmente caros, consumindo seus recursos e impedindo o serviço a usuários legítimos.
- **Ataques Práticos ao Tráfego da Internet (Logjam):** A pré-computação de logaritmos discretos para grupos de 1024 bits ou menos, comumente usados, permite que invasores bem financiados (como agências de inteligência) quebrem a criptografia. A NSA é suspeita de ter essa capacidade.
- **Computadores Quânticos:** O algoritmo de Shor pode resolver o problema do logaritmo discreto de forma eficiente, quebrando a segurança do Diffie-Hellman. Variantes pós-quânticas estão em desenvolvimento.
- **Geradores de Números Aleatórios Fracos:** Se as chaves privadas não forem geradas com aleatoriedade suficiente, torna-se mais fácil para um invasor predizê-las.
- **Corpos de Característica Pequena:** Podem ser menos seguros.
- **Ordem do Grupo G:** A ordem do grupo deve ter um fator primo grande para evitar o uso do algoritmo de Pohlig-Hellman para obter as chaves privadas.

---

# 18. Elliptic Curve Cryptography (ECC)

## Equações e Fórmulas

$$
AlicePubKey * BobPrivKey = BobPubKey * AlicePrivKey = SharedSecret
$$

$$
Q = kP
$$

$$
y^2 = x^3 + ax + b
$$

$$
e = HASH(m)
$$

$$
r = x1 mod n
$$

$$
s = k^-1(z + r*dA) mod n
$$

$$
u1 = z*s^-1 mod n
$$

$$
u2 = r*s^-1 mod n
$$

$$
(x1, y1) = u1 * G + u2 * QA
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| priv | chave privada |
| pub | chave pública |
| a | coeficiente da equação da curva elíptica |
| b | coeficiente da equação da curva elíptica |
| x | coordenada x de um ponto na curva |
| y | coordenada y de um ponto na curva |
| n | número de vezes que um ponto é 'pontilhado' com ele mesmo |

## Algoritmos e Protocolos

```
### Algoritmo de Geração de Assinatura ECDSA

1. Calcule `e = HASH(m)`.
2. Seja `z` os `Ln` bits mais à esquerda de `e`, onde `Ln` é o comprimento em bits da ordem do grupo `n`.
3. Selecione um inteiro aleatório criptograficamente seguro `k` de `[1, n-1]`.
4. Calcule o ponto da curva `(x1, y1) = k * G`.
5. Calcule `r = x1 mod n`. Se `r = 0`, volte para a etapa 3.
6. Calcule `s = k^-1(z + r*dA) mod n`. Se `s = 0`, volte para a etapa 3.
7. A assinatura é o par `(r, s)`.

### Algoritmo de Verificação de Assinatura ECDSA

1. Verifique se `r` e `s` são inteiros em `[1, n-1]`.
2. Calcule `e = HASH(m)`.
3. Seja `z` os `Ln` bits mais à esquerda de `e`.
4. Calcule `u1 = z*s^-1 mod n` e `u2 = r*s^-1 mod n`.
5. Calcule o ponto da curva `(x1, y1) = u1 * G + u2 * QA`. Se `(x1, y1) = O`, a assinatura é inválida.
6. A assinatura é válida se `r ≡ x1 (mod n)`.
```

## Vulnerabilidades

- Reutilização do valor de k: O uso do mesmo valor de k para assinaturas diferentes permite que a chave privada seja calculada.
- Gerador de número aleatório defeituoso para k: Se o RNG for falho, pode levar a colisões em k, permitindo a recuperação da chave privada.
- Ataques de temporização: É possível recuperar uma chave privada TLS através de um ataque de temporização em algumas implementações do OpenSSL.
- Confiabilidade da curva NIST: Preocupações sobre possíveis backdoors em curvas produzidas pelo NIST.
- Dificuldade de implementação: O padrão é difícil de implementar corretamente e falhas podem reduzir a segurança.

---

# 19. SHA-256 hash function - Secure Hash Algorithm

## Equações e Fórmulas

$$
Σ0(x) = ROTR(2, x) ^ ROTR(13, x) ^ ROTR(22, x)
$$

$$
Σ1(x) = ROTR(6, x) ^ ROTR(11, x) ^ ROTR(25, x)
$$

$$
σ0(x) = ROTR(7, x) ^ ROTR(18, x) ^ (x>>>3)
$$

$$
σ1(x) = ROTR(17, x) ^ ROTR(19, x) ^ (x>>>10)
$$

$$
Ch(x, y, z) = (x & y) ^ (~x & z)
$$

$$
Maj(x, y, z) = (x & y) ^ (x & z) ^ (y & z)
$$

$$
T1 = h + Σ1(e) + Ch(e, f, g) + K[t] + W[t]
$$

$$
T2 = Σ0(a) + Maj(a, b, c)
$$

$$
W[t] = (σ1(W[t-2]) + W[t-7] + σ0(W[t-15]) + W[t-16]) >>> 0
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| K | um array de 64 constantes de 32 bits |
| H | um array de 8 valores de hash iniciais de 32 bits |
| W | um array de 64 palavras de 32 bits, representando o cronograma de mensagens |
| a, b, c, d, e, f, g, h | variáveis de trabalho de 32 bits |
| T1, T2 | variáveis temporárias de 32 bits |

## Algoritmos e Protocolos

```
1. Pre-processamento: A mensagem de entrada é preenchida para garantir que seu comprimento seja um múltiplo de 512 bits. Um único bit '1' é anexado à mensagem, seguido por bits '0' até que o comprimento da mensagem seja 64 bits menor que um múltiplo de 512. Os 64 bits restantes são preenchidos com o comprimento da mensagem original.
2. Processamento em Blocos: A mensagem preenchida é processada em blocos de 512 bits. Cada bloco é dividido em 16 palavras de 32 bits.
3. Cronograma de Mensagens: Um cronograma de mensagens de 64 palavras de 32 bits (W) é criado a partir das 16 palavras do bloco de mensagens.
4. Compressão: O coração do algoritmo é a função de compressão, que opera em um loop de 64 iterações (rounds). Em cada iteração, as variáveis de trabalho (a, b, c, d, e, f, g, h) são atualizadas usando as constantes K, o cronograma de mensagens W e as funções lógicas (Ch, Maj, Σ0, Σ1, σ0, σ1).
5. Atualização do Hash: Após 64 iterações, os valores das variáveis de trabalho são adicionados aos valores de hash intermediários (H). O resultado é o novo valor de hash intermediário.
6. Saída: Após o processamento de todos os blocos de mensagens, o valor final do hash é a concatenação dos 8 valores de hash intermediários de 32 bits, resultando em um hash de 256 bits.
```

## Vulnerabilidades

- Ataque de extensão de comprimento: Como o estado interno completo do algoritmo é a saída, um invasor pode anexar dados adicionais à mensagem original e calcular um novo hash válido sem conhecer a mensagem original.
- Ataques de colisão (teóricos): Embora nenhuma colisão prática tenha sido encontrada para o SHA-256, ataques de colisão teóricos existem para versões com número reduzido de rodadas. A segurança do SHA-256 depende do número total de rodadas (64), e a redução desse número o torna mais suscetível a ataques.
- Ataque de hash circular: Uma vulnerabilidade teórica onde é possível encontrar um input_hash e um message_block que resultam em input_hash = output_hash.

---

# 20. Ralph Merkle - Árvores de Merkle

## Equações e Fórmulas

$$
$$M_{i} = \text{hash}(M_{2i} \| M_{2i+1})$$
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| M_i | Nó na árvore de Merkle |
| hash() | Função de hash criptográfica (ex: SHA-2, Tiger) |
| || | Operação de concatenação |
| O(n) | Complexidade de espaço e travessia |
| O(log n) | Complexidade de busca, inserção, deleção e sincronização |

## Algoritmos e Protocolos

```
Construção da Árvore de Merkle: 1. Hashing das Folhas: Cada bloco de dados (transação) é hasheado individualmente, formando os nós folha da árvore. 2. Construção dos Nós Internos: Os nós internos são construídos recursivamente. Os nós folha são agrupados em pares, e o hash da concatenação de cada par é calculado, formando o nó pai. Se houver um número ímpar de nós em um nível, o último nó é duplicado e pareado consigo mesmo. 3. Cálculo da Raiz de Merkle: O processo continua até que reste apenas um único hash, a Raiz de Merkle (Merkle Root), que representa a 'impressão digital' de todo o conjunto de dados.
 Prova de Inclusão (Inclusion Proof) e Verificação de Pagamento Simplificada (SPV): Para provar que um dado específico (transação) pertence à árvore, um cliente precisa apenas do dado, da Raiz de Merkle e do 'ramo' de hashes irmãos ao longo do caminho do dado até a raiz. O cliente recalcula a Raiz de Merkle usando o hash do dado e o ramo fornecido. Se a raiz calculada corresponder à Raiz de Merkle conhecida, a inclusão do dado é verificada de forma eficiente, sem a necessidade de baixar e processar todo o conjunto de dados. Este é o princípio por trás da Verificação de Pagamento Simplificada (SPV) em criptomoedas.
```

## Vulnerabilidades

- Ataque de Segunda Pré-imagem (Second Preimage Attack): A Raiz de Merkle por si só não especifica a profundidade da árvore. Um invasor pode construir um documento diferente com o mesmo hash da raiz, mas com uma estrutura de árvore diferente. A mitigação envolve prefixar os dados com bytes distintos para folhas (`0x00`) e nós internos (`0x01`) antes do hashing, como especificado no Certificate Transparency.
- CVE-2012-2459 (Invalidity Caching): Um invasor pode criar uma versão inválida de um bloco (ex: com uma transação duplicada) que possui a mesma Raiz de Merkle do bloco válido. Se um nó do Bitcoin Core receber a versão inválida primeiro, ele a armazena em cache e rejeita a versão válida, possibilitando um ataque de eclipse. A vulnerabilidade foi corrigida no Bitcoin Core.
- CVE-2017-12842 (Transactions as txids and vice versa): Como o mesmo algoritmo de hash (SHA256d) é usado para folhas e nós internos no Bitcoin, uma transação de 64 bytes pode ser interpretada como a concatenação de dois hashes de 32 bytes de nós internos, e vice-versa. Isso pode ser explorado para enganar clientes SPV. As mitigações incluem a invalidação de transações de 64 bytes via soft fork e o uso de algoritmos de hash diferentes para diferentes partes da árvore em novas implementações como o Taproot.

---

# 21. Assinaturas Digitais - ECDSA, Schnorr, BLS, Assinaturas Agregadas e Multisig

## Equações e Fórmulas

$$
Q_A = d_A \times G
$$

$$
e = \text{HASH}(m)
$$

$$
r = x_1 \pmod{n}
$$

$$
s = k^{-1}(z + r \cdot d_A) \pmod{n}
$$

$$
C = u_1 \times G + u_2 \times Q_A
$$

$$
u_1 = z \cdot s^{-1} \pmod{n}
$$

$$
u_2 = r \cdot s^{-1} \pmod{n}
$$

$$
y = g^x
$$

$$
e = H(g^k || M)
$$

$$
s = k + xe
$$

$$
r_v = g^s y^{-e}
$$

$$
pk = sk \cdot g_2
$$

$$
h = H(m)
$$

$$
\sigma = h^{sk}
$$

$$
e(\sigma, g_2) = e(H(m), pk)
$$

$$
\sigma = \text{Aggregate}(\sigma_1, \sigma_2, ..., \sigma_k)
$$

$$
e(\sigma, g_2) = \prod_{i=1}^{k} e(H(m_i), pk_i)
$$

$$
P_{agg} = \sum_{i=1}^{n} P_i
$$

$$
s_{agg} = \sum_{i=1}^{n} s_i
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| CURVE | O corpo e a equação da curva elíptica utilizada |
| G | Ponto base da curva elíptica |
| n | Ordem inteira de G |
| d_A | A chave privada |
| Q_A | A chave pública |
| m | A mensagem |
| e | O hash da mensagem |
| z | Os L_n bits mais à esquerda de e |
| k | Inteiro aleatório |
| (r, s) | A assinatura digital |
| (x_1, y_1) | Coordenadas do ponto da curva |
| u_1, u_2 | Valores intermediários de verificação |
| C | Ponto da curva calculado na verificação |
| G | Grupo de ordem prima q com gerador g |
| H | Função de hash |
| x | Chave de assinatura privada |
| y | Chave de verificação pública |
| M | Mensagem |
| k | Nonce aleatório |
| r | Compromisso |
| e | Desafio |
| s | Resposta |
| (e, s) | Assinatura |
| e | Emparelhamento bilinear |
| G_1, G_2 | Grupos de curvas elípticas |
| g_2 | Gerador de G_2 |
| H | Função de hash |
| sk | A chave secreta |
| pk | A chave pública |
| m | A mensagem |
| h | O hash da mensagem |
| \sigma | A assinatura |
| \sigma_i | Assinatura do usuário i na mensagem m_i |
| \sigma | A assinatura agregada |
| m_i | Mensagem assinada pelo usuário i |
| pk_i | Chave pública do usuário i |
| k | Número de assinaturas a serem agregadas |
| n | O número de participantes |
| m | O limite de assinaturas necessárias |
| P_i | Chave pública do participante i |
| s_i | Assinatura (ou compartilhamento de assinatura) do participante i |

## Algoritmos e Protocolos

```
ECDSA Geração de Assinatura: 1. Calcule e = HASH(m). 2. Seja z os L_n bits mais à esquerda de e. 3. Selecione um inteiro aleatório k. 4. Calcule (x_1, y_1) = k * G. 5. Calcule r = x_1 mod n. 6. Calcule s = k^-1(z + r * d_A) mod n. 7. A assinatura é (r, s).
ECDSA Verificação de Assinatura: 1. Verifique se r e s são inteiros em [1, n-1]. 2. Calcule e = HASH(m). 3. Seja z os L_n bits mais à esquerda de e. 4. Calcule u_1 = z * s^-1 mod n. 5. Calcule u_2 = r * s^-1 mod n. 6. Calcule C = u_1 * G + u_2 * Q_A. 7. A assinatura é válida se r é congruente a x_C mod n.
Assinatura de Schnorr Geração de Chave: 1. Escolha uma chave privada x. 2. A chave pública é y = g^x.
Assinatura de Schnorr Assinatura: 1. Escolha um k aleatório. 2. Calcule r = g^k. 3. Calcule e = H(r || M). 4. Calcule s = k + xe. 5. A assinatura é (e, s).
Assinatura de Schnorr Verificação: 1. Calcule r_v = g^s * y^-e. 2. Calcule e_v = H(r_v || M). 3. Se e_v = e, a assinatura é verificada.
Assinatura BLS Geração de Chave: 1. Selecione um sk aleatório. 2. A chave pública é pk = sk * g_2.
Assinatura BLS Assinatura: 1. Calcule h = H(m). 2. A assinatura é sigma = h^sk.
Assinatura BLS Verificação: 1. Verifique se e(sigma, g_2) = e(H(m), pk).
Agregação Geral de Assinatura: 1. Cada usuário i cria a assinatura sigma_i em sua mensagem m_i. 2. Qualquer pessoa pode agregar as k assinaturas em uma única assinatura sigma.
Agregação Sequencial de Assinatura: 1. O usuário 1 assina m_1 para obter sigma_1. 2. O usuário 2 combina sigma_1 e m_2 para obter sigma_2, e assim por diante.
Multisig Ingênuo: 1. Cada um dos n usuários tem um par de chaves. 2. Uma assinatura válida é uma coleção de n assinaturas. 3. A verificação requer n chaves públicas.
MuSig: 1. Os participantes combinam suas chaves públicas para criar uma chave pública agregada. 2. Os participantes assinam a mensagem e combinam as saídas em uma única assinatura. 3. A verificação é feita usando a chave pública agregada.
```

## Vulnerabilidades

- Reutilização de k/nonce, Gerador de números aleatórios defeituoso, Ataques de tempo, Backdoors em parâmetros de curva, Nonces tendenciosos, Dependência da intratabilidade do problema Computacional Diffie-Hellman, Ataques de cálculo de índice no grupo alvo, Não é seguro contra ataques quânticos, Um adversário não deve ser capaz de criar uma assinatura agregada válida, A maioria das propostas de agregação requer uma ordem específica de assinatura, Ineficiência e complexidade em esquemas multisig ingênuos.

---

# 22. Proof of Work - hashcash, dificuldade, nonce, target, mining algorithm

## Equações e Fórmulas

$$
`target = \frac{max\_target}{difficulty}`
$$

$$
`H(s,x,c) / 2^{n-k} = 0`
$$

$$
`target = coefficient \times 2^{8 \times (exponent - 3)}`
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| `ver` | Versão do formato Hashcash |
| `bits` | Número de bits zero no início do hash |
| `date` | Data e hora do envio da mensagem no formato YYMMDD[hhmm[ss]] |
| `resource` | String de dados do recurso que está sendo transmitido (ex: endereço de e-mail) |
| `ext` | Extensão (opcional |
| `rand` | String de caracteres aleatórios, codificada em base-64 |
| `counter` | Contador binário, codificado em base-64 |
| `nonce` | Um número de 32 bits que os mineradores usam para tentar gerar um hash válido |
| `difficulty` | Uma medida de quão difícil é encontrar um hash abaixo do alvo |
| `target` | Um número de 256 bits que um hash de bloco deve ser menor ou igual |
| `max_target` | O valor máximo possível do alvo |
| `s` | String de serviço |
| `x` | Ponto de partida aleatório |
| `c` | Contador |
| `n` | Tamanho da saída do hash |
| `k` | Fator de trabalho |
| `coefficient` | Os 3 primeiros bytes do campo 'bits' |
| `exponent` | O último byte do campo 'bits' |

## Algoritmos e Protocolos

```
O formato do cabeçalho do Hashcash é `ver:bits:date:resource:[ext]:rand:counter`. O algoritmo consiste em:

1.  Preparar um cabeçalho com os campos especificados.
2.  Computar o hash (originalmente SHA-1) do cabeçalho.
3.  Verificar se os primeiros `bits` do hash são zero. Se forem, a prova de trabalho é válida.
4.  Caso contrário, o campo `counter` é incrementado e o processo é repetido.

### Mineração de Bitcoin

1.  Construir um cabeçalho de bloco incluindo a versão do software, o hash do bloco anterior, a raiz de Merkle, o timestamp, o alvo de dificuldade (bits) e um nonce.
2.  Alterar repetidamente o nonce (e o extra nonce/timestamp, se necessário) e computar o hash duplo SHA-256 do cabeçalho do bloco.
3.  Se o hash resultante for menor ou igual ao alvo, o bloco é minerado com sucesso.
4.  O primeiro minerador a encontrar um hash válido transmite o bloco para a rede.
```

## Vulnerabilidades

- Ataque de 51%, Riscos Criptoanalíticos, Mineração Egoísta (Selfish Mining)

---

# 23. Proof of Stake - seleção de validadores, staking, slashing, Casper, Ouroboros

## Equações e Fórmulas

$$
Hash(ProposedNewBlock \|\| ClockTime) < target \times StakeValue
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| Hash | A função de hash criptográfica |
| ProposedNewBlock | O novo bloco proposto |
| ClockTime | O tempo atual |
| target | Um valor alvo que determina a dificuldade |
| StakeValue | O valor do stake do validador. |

## Algoritmos e Protocolos

```
Chain-based PoS: Uma modificação do Proof of Work onde a dificuldade do quebra-cabeça varia com o stake
 Nominated PoS (NPoS): Eleição de um comitê de validadores por meio de uma função aleatória verificável, com probabilidades ponderadas pelo stake. Usado em Ouroboros Praos e BABE
 BFT-based PoS: Utiliza o consenso Byzantine Fault Tolerance para finalizar blocos. Requer que no máximo um terço dos validadores seja desonesto. Usado em Tendermint e Casper FFG
 Delegated Proof of Stake (DPoS): Um sistema de duas etapas onde os detentores de stake elegem 'testemunhas' para propor e votar em novos blocos. Usado em EOS, Lisk e Tron
 Liquid Proof of Stake (LPoS): Permite que qualquer pessoa com stake se torne um validador, com a opção de delegação de votos. Usado em Tezos
 Ouroboros: Uma família de protocolos de consenso PoS que inclui mini-protocolos para sincronização de cadeia, busca de blocos, submissão de transações, etc
 Casper: Um protocolo de consenso PoS (chamado Zug) que oferece finalidade rápida e flexibilidade, apoiado por WebAssembly.
```

## Vulnerabilidades

- Long-range attacks: Ataques que substituem uma parte significativa da blockchain, viáveis devido ao baixo custo computacional
- Nothing at stake: Validadores são incentivados a validar todos os forks da cadeia, o que pode levar a gastos duplos. A mitigação envolve penalidades
- Bribery attack: Atacantes podem subornar validadores para aprovar um fork malicioso da blockchain.

---

# 24. Blockchain consensus - Nakamoto consensus, BFT, PBFT, Tendermint, Raft

## Equações e Fórmulas

$$
P_z = 1 - \sum_{k=0}^{z} \frac{\lambda^k e^{-\lambda}}{k!} (1 - (q/p)^{z-k})
$$

$$
n >= 3f + 1
$$

- n > 3f

## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| p | probabilidade de um nó honesto encontrar o próximo bloco |
| q | probabilidade de o atacante encontrar o próximo bloco |
| z | número de blocos que o atacante precisa alcançar |
| λ | z * (q/p) |
| n | número total de réplicas no sistema |
| f | número máximo de réplicas bizantinas (defeituosas) |
| view | um número que identifica o líder atual. |
| request | uma solicitação de um cliente para o serviço. |
| pre-prepare | uma mensagem enviada pelo líder para os backups para iniciar o processo de consenso. |
| prepare | uma mensagem enviada pelos backups para confirmar que eles concordam com a ordem da solicitação. |
| commit | uma mensagem enviada pelos backups para confirmar que eles processaram a solicitação. |
| height | altura do bloco na cadeia. |
| round | rodada de consenso para uma determinada altura. |
| pre-vote | primeira fase de votação no algoritmo de consenso. |
| pre-commit | segunda fase de votação no algoritmo de consenso. |
| polka | quando mais de 2/3 dos validadores pré-votam no mesmo bloco. |
| termo | período de tempo no qual um líder é eleito. |
| líder | nó responsável por gerenciar o log replicado. |
| seguidor | nó que segue as instruções do líder. |
| candidato | nó que está concorrendo para se tornar o líder. |
| log | sequência de comandos que são replicados entre os nós. |

## Algoritmos e Protocolos

```
Consenso de Nakamoto: 1. Novas transações são transmitidas para todos os nós. 2. Cada nó coleta novas transações em um bloco. 3. Cada nó trabalha para encontrar uma prova de trabalho (proof-of-work) para seu bloco. 4. Quando um nó encontra uma prova de trabalho, ele transmite o bloco para todos os nós. 5. Os nós aceitam o bloco somente se todas as transações nele forem válidas e ainda não tiverem sido gastas. 6. Os nós expressam sua aceitação do bloco trabalhando na criação do próximo bloco da cadeia, usando o hash do bloco aceito como o hash anterior.
 BFT: Practical Byzantine Fault Tolerance (PBFT): Um algoritmo de replicação de máquina de estados que tolera falhas bizantinas em sistemas assíncronos. 1. Um cliente envia uma solicitação ao nó líder. 2. O líder transmite a solicitação para os nós de backup. 3. Os nós de backup executam a solicitação e enviam uma resposta ao cliente. 4. O cliente aguarda `f + 1` respostas idênticas de diferentes nós de backup.
 PBFT: O PBFT é um algoritmo de consenso que tolera falhas bizantinas em sistemas distribuídos. O algoritmo funciona em "views", onde cada view tem um líder. O processo de consenso para uma solicitação de cliente é o seguinte: 1. Um cliente envia uma solicitação ao nó líder. 2. O líder multicasta a solicitação para os nós de backup em uma mensagem `pre-prepare`. 3. Os backups recebem a mensagem `pre-prepare` e, se concordarem com ela, enviam uma mensagem `prepare` para todos os outros nós. 4. Um nó espera por `2f` mensagens `prepare` de outros nós que correspondam à mensagem `pre-prepare`. Se o fizer, envia uma mensagem `commit` para todos os outros nós. 5. Um nó espera por `2f + 1` mensagens `commit`. Se o fizer, ele executa a solicitação e envia uma resposta ao cliente.
 Tendermint: O consenso Tendermint é um protocolo de consenso BFT (Byzantine Fault Tolerant) baseado em proof-of-stake. O processo de consenso ocorre em rodadas e consiste em três etapas: 1. **Propose**: Um validador é escolhido para propor um novo bloco. A seleção do proponente é determinística e rotativa. 2. **Prevote**: Os validadores votam no bloco proposto. Se um validador recebe um bloco válido do proponente atual, ele transmite um `prevote` para o bloco. 3. **Precommit**: Se um validador recebe mais de 2/3 de `prevotes` para um bloco, ele transmite um `precommit` para esse bloco. Se um validador recebe mais de 2/3 de `precommits`, ele considera o bloco como confirmado.
 Raft: O Raft funciona através da eleição de um líder que é responsável por gerenciar o log replicado. O algoritmo é dividido em três subproblemas: 1. **Eleição de Líder**: Um líder é eleito para um determinado termo. Se o líder falhar, um novo líder é eleito para um novo termo. 2. **Replicação de Log**: O líder recebe comandos dos clientes e os adiciona ao seu log. Em seguida, ele envia os comandos para os seguidores para que eles também os adicionem aos seus logs. 3. **Segurança**: O Raft garante que, se qualquer servidor aplicou uma entrada de log em um determinado índice, nenhum outro servidor aplicará uma entrada diferente para o mesmo índice.
```

## Vulnerabilidades

- Ataque de 51%
- Ataque de egoísmo (Selfish Mining)
- Ataques de Desempenho
- Ataques de Temporização
- Desempenho
- Líder Malicioso
- Ataque de 1/3
- Ataque de Long Range
- Particionamento de Rede
- Nós Lentos

---

# 25. Bitcoin Script - linguagem de script, OP_CODES, P2PKH, P2SH, SegWit

## Equações e Fórmulas

$$
5 + 9 = 14
$$

$$
y^2 \equiv x^3 + ax + b \pmod{p}
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| scriptPubKey | O script que bloqueia a saída da transação. |
| scriptSig | O script que desbloqueia a saída da transação. |
| pubKey | Chave Pública. |
| pubKeyHash | O hash de uma chave pública. |
| sig | Assinatura. |
| redeemScript | Um script que é revelado e executado posteriormente. |
| nLockTime | Um campo na transação que especifica o tempo mais antigo em que a transação pode ser adicionada a um bloco válido. |
| nSequence | Um campo em cada entrada de uma transação que pode ser usado para tempo de bloqueio relativo. |
| witness | Uma nova seção nas transações SegWit que contém o código de desbloqueio. |
| wTXID | O ID da transação de testemunha, que inclui os dados da testemunha. |

## Algoritmos e Protocolos

```
**Pay-to-PubKey-Hash (P2PKH)**

*   **scriptPubKey:** `OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG`
*   **scriptSig:** `<sig> <pubKey>`

**Processo de Execução:**

1.  O `scriptSig` e o `scriptPubKey` são combinados.
2.  `<sig>` e `<pubKey>` são empurrados para a pilha.
3.  `OP_DUP` duplica o `<pubKey>` no topo da pilha.
4.  `OP_HASH160` calcula o hash do `<pubKey>` duplicado.
5.  O `<pubKeyHash>` do `scriptPubKey` é empurrado para a pilha.
6.  `OP_EQUALVERIFY` verifica se os dois hashes são iguais. Se não forem, a transação falha.
7.  `OP_CHECKSIG` verifica a assinatura da transação usando a `<pubKey>` e a `<sig>`.

---

**Pay-to-Script-Hash (P2SH)**

*   **scriptPubKey:** `OP_HASH160 <scriptHash> OP_EQUAL`
*   **scriptSig:** `<sig> <pubKey> <redeemScript>`

**Processo de Execução:**

1.  O `scriptSig` e o `scriptPubKey` são combinados.
2.  O `<redeemScript>` é verificado para garantir que corresponde ao `<scriptHash>`.
3.  O `<redeemScript>` é então executado.

---

**Pay-to-Witness-PubKey-Hash (P2WPKH)**

*   **Locking Script:** `0 <pubKeyHash>` (na saída da transação)
*   **Unlocking Script (Witness):** `<sig> <pubKey>`

**Pay-to-Witness-Script-Hash (P2WSH)**

*   **Locking Script:** `0 <scriptHash>` (na saída da transação)
*   **Unlocking Script (Witness):** `<sig> <pubKey> <redeemScript>`
```

## Vulnerabilidades

- Maleabilidade de Transação (Transaction Malleability)
- OP_LSHIFT Crash (CVE-2010-5137)
- Gastos não autorizados (CVE-2010-5141)

---

# 26. Lightning Network - canais de pagamento, HTLCs, roteamento, onion routing, capacidade

## Equações e Fórmulas

- OP_IF OP_HASH160 <Hash160(R)> OP_EQUALVERIFY 2 <Alice2> <Bob2> OP_CHECKMULTISIG OP_ELSE 2 <Alice1> <Bob1> OP_CHECKMULTISIG OP_ENDIF

## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| R | um dado de entrada aleatório de 20 bytes (pré-imagem) |
| H | o hash de R |
| P | chaves públicas |
| K | chaves privadas correspondentes |
| C | Transação de Compromisso |
| RD | Transação de Entrega Revogável |
| BR | Transação de Remédio de Violação |
| HED | Transação de Entrega de Execução de HTLC |
| HT | Transação de Tempo Limite de HTLC |
| HTRD | Transação de Entrega Revogável de Tempo Limite de HTLC |
| HERD | Transação de Entrega Revogável de Execução de HTLC |
| nLockTime | um parâmetro de transação que especifica o tempo mais antigo em que uma transação pode ser adicionada a um bloco |
| RSMC | Contrato de Vencimento de Sequência Revogável |

## Algoritmos e Protocolos

```
Hashed Timelock Contract (HTLC): Um contrato que permite que uma transação seja gasta se o destinatário puder fornecer a pré-imagem de um hash. Se a pré-imagem não for fornecida dentro de um determinado período de tempo, os fundos serão devolvidos ao remetente.
Revocable Sequence Maturity Contract (RSMC): Um contrato que invalida transações antigas. Se uma parte transmitir uma transação antiga, a outra parte pode reivindicar todos os fundos no canal. Isso é feito através de uma transação de penalidade (Breach Remedy transaction).
Roteamento de Pagamentos (Payment Routing): O roteamento é feito através de uma rede de canais de pagamento. O remetente encontra uma rota para o destinatário e cria HTLCs ao longo do caminho. Cada salto na rota tem um timelock decrescente. O destinatário resgata o pagamento revelando o segredo R, que então se propaga de volta ao remetente, permitindo que cada intermediário reivindique seus fundos.
```

## Vulnerabilidades

- Ataque de 51% através do sistema de revogação
- Ataque de negação de serviço (DDoS)
- Problemas de roteamento e liquidez
- Necessidade de watchtowers (serviços de terceiros) para monitorar fundos
- Bugs que podem causar perda de fundos (CVE-2019-12998, CVE-2019-12999, CVE-2019-13000)
- Ataques que podem retardar ou parar pagamentos
- Ataques de congestionamento
- Centralização crescente
- Ataque Flood & Loot
- Ataques de saída em massa (Mass Exit Attacks)
- Ataque de griefing
- Vulnerabilidade de jamming de retransmissão de transação (Transaction-Relay Jamming)
- Ataque de ciclo de substituição (Replacement Cycling Attack)
- Ataque Zumbi (Zombie Attack)
- Ataque de gasto duplo em massa (Mass Double-Spend Attack)
- Ataque de dilatação do tempo (Time-Dilation Attack)

---

# 27. Provas de Conhecimento Zero - zk-SNARKs, zk-STARKs, Groth16, Plonk, bulletproofs

## Equações e Fórmulas

$$
p(x) = (\Sigma_{i=0 to m} c_i * v_i(x)) * (\Sigma_{i=0 to m} c_i * w_i(x)) - (\Sigma_{i=0 to m} c_i * y_i(x))
$$

$$
p(x) = (\Sigma_{i=1 to m} c_i * v_i(x))^2 - v_0(x)
$$

$$
e(A, B) = e(\alpha, \beta) * e(\Sigma_{i=1 to l} a_i u_i(x), \gamma) * e(C, \delta)
$$

$$
q_L(X)a(X) + q_R(X)b(X) + q_O(X)c(X) + q_M(X)a(X)b(X) + q_C(X) = 0
$$

$$
Z(gX) * (f'(X) + \betaS_ID(X) + \gamma) = Z(X) * (g'(X) + \betaS_\sigma(X) + \gamma)
$$

$$
a' = a_L * x + a_R * x^{-1}
$$

$$
b' = b_L * x^{-1} + b_R * x
$$

$$
g' = g_L * x^{-1} + g_R * x
$$

$$
h' = h_L * x + h_R * x^{-1}
$$

$$
P' = L * x^2 + R * x^{-2} + P
$$

$$
<a_L - z*1^n, y^n \circ (a_R + z*1^n) + z^2*2^n> = \delta(y, z)
$$

$$
w_L \circ w_R = w_O
$$

$$
W_L * a_L + W_R * a_R + W_O * a_O = W_V * v + c
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| L | Uma linguagem na classe NP |
| R_L | Um algoritmo de tempo polinomial para a linguagem L |
| x | Uma string de entrada |
| w | Uma testemunha para x |
| crs | String de Referência Comum |
| vrs | String de Referência do Verificador |
| td | Trapdoor |
| \lambda | Parâmetro de segurança |
| R | Uma relação |
| u | Uma declaração |
| \pi | Um argumento ou prova |
| V, W, Y | Conjuntos de polinômios em um QAP |
| t(x) | Polinômio alvo em um QAP ou SSP |
| p(x) | Polinômio a ser verificado quanto à divisibilidade por t(x) |
| c_i | Coeficientes para o QAP |
| \alpha, \beta, \gamma, \delta, x, r, s | Elementos aleatórios de um corpo F |
| A, B, C | Elementos da prova em Groth16 |
| e | Uma função de emparelhamento |
| a(X), b(X), c(X) | Polinômios que representam os valores dos fios em Plonk |
| q_L(X), q_R(X), q_O(X), q_M(X), q_C(X) | Polinômios seletores em Plonk |
| Z(X) | Polinômio acumulador em Plonk |
| S_ID, S_\sigma | Polinômios que representam a permutação em Plonk |
| a, b | Vetores em uma prova de produto interno |
| L, R | Elementos de grupo em uma prova de produto interno |
| P | Compromisso em uma prova de produto interno |
| a_L, a_R | Vetores de bits em uma prova de intervalo |
| v | Valor a ser verificado em uma prova de intervalo |
| y, z | Desafios aleatórios em uma prova de intervalo |
| \delta(y, z) | Termo de correção em uma prova de intervalo |
| w_L, w_R, w_O | Vetores de fios em um circuito aritmético |
| W_L, W_R, W_O, W_V | Matrizes que definem um circuito aritmético |

## Algoritmos e Protocolos

```
zk-SNARKs: Baseado na conversão de um problema de satisfatibilidade de circuito em um Programa Aritmético Quadrático (QAP) ou Programa de Vão Quadrado (SSP). A prova é então gerada usando emparelhamentos em curvas elípticas.
zk-STARKs: Utiliza um sistema de Prova de Oráculo Interativa (IOP) e o protocolo FRI (Fast Reed-Solomon IOP of Proximity) para construir provas. A computação é representada como um traço de execução, que é então verificado.
Groth16: Um protocolo zk-SNARK específico que consiste em três algoritmos (Setup, Prove, Verify) e usa uma única equação de emparelhamento para verificação.
Plonk: Usa um esquema de compromisso de polinômio e um argumento de permutação para verificar a validade de uma computação. As restrições do circuito são expressas como uma única equação polinomial.
Bulletproofs: Baseado em um argumento de produto interno eficiente e recursivo. É particularmente adequado para provas de intervalo e não requer uma configuração confiável.
```

## Vulnerabilidades

- Circuitos Sub-restringidos e Não-Determinísticos, Overflows/Underflows Aritméticos, Comprimentos de Bits Incompatíveis, Maleabilidade da Prova (Groth16), Ataque do Último Desafio (Fiat-Shamir)

---

# 28. Criptografia Homomórfica - FHE, Paillier, Baseada em Reticulado

## Equações e Fórmulas

$$
E(m) = g^m r^n \mod n^2
$$

$$
E(m_1) \cdot E(m_2) = g^{m_1+m_2} (r_1 r_2)^n \mod n^2 = E(m_1+m_2)
$$

$$
\psi_i \leftarrow \pi_i^e \mod N
$$

$$
\Pi \psi_i = (\Pi \pi_i)^e \mod N
$$

$$
c = b + 2x + kp
$$

$$
c \leftarrow c_1 + c_2 = b_1 + b_2 + 2(x_1 + x_2) + (k_1 + k_2)p = b_1 \oplus b_2 + 2x + kp
$$

$$
c \leftarrow c_1 * c_2 = b_1 * b_2 + 2(b_1x_2 + b_2x_1 + 2x_1x_2) + kp = b_1 * b_2 + 2x + kp
$$

$$
Decrypt_E(sk, Evaluate_E(pk, C, \psi_1, ..., \psi_t)) = C(\pi_1, ..., \pi_t)
$$

$$
Add(pk, \psi_1, \psi_2) = \psi_1 + \psi_2 \in (\pi_1 + \pi_2) + I
$$

$$
Mult(pk, \psi_1, \psi_2) = \psi_1 \times \psi_2 \in (\pi_1 \times \pi_2) + I
$$

$$
v \mod B_I = v - B_I \cdot \lfloor B_I^{-1}v \rceil
$$

$$
\pi = \psi - \lfloor B_{sk}^{-1}\psi \rceil
$$

$$
\pi = \psi - \lfloor b_{vJsk} \times \psi e\rceil \mod B_I
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| n | módulo, chave pública |
| g | base, chave pública |
| m | mensagem |
| r | número aleatório em {0, ..., n-1} |
| N | Módulo RSA, produto de dois primos grandes |
| e | Expoente público RSA |
| π_i | Mensagem em texto claro |
| ψ_i | Mensagem cifrada |
| c | Texto cifrado |
| b | Bit de mensagem (0 ou 1) |
| x | Inteiro aleatório |
| k | Inteiro aleatório |
| p | Inteiro grande (módulo secreto) |
| pk | Chave pública |
| sk | Chave secreta |
| C | Circuito a ser avaliado |
| I, J | Ideais em um anel de polinômios R |
| B_I, B_sk | Bases de reticulado para os ideais I e sk |
| v | Vetor |

## Algoritmos e Protocolos

```
Esquema de Gentry (Baseado em Reticulados Ideais): Construído a partir de um esquema de criptografia de alguma forma homomórfico (somewhat homomorphic) que é "bootstrappable". Inclui os algoritmos KeyGen, Encrypt, Decrypt, Evaluate e Recrypt (bootstrapping).
```

## Vulnerabilidades

- Ataques de força bruta ao SVSSP (Sparse Vector Subset Sum Problem)
- Ataques de redução de reticulado contra knapsacks de baixa densidade
- Ataques de canal lateral (Side-channel attacks)
- Ataques de criptoanálise a Polly Cracker
- Ataques em reticulados de ideais circulantes com bases ortonormais
- Ataques de subcampo em variantes do NTRU

---

# 29. Ring Signatures - Monero, CryptoNote, linkability, anonimato, key images

## Equações e Fórmulas

$$
P = Hs(rA)G + B
$$

$$
P = xG
$$

$$
x = Hs(rA) + b
$$

$$
I = xHp(P)
$$

$$
ci+1 = Hs(m, Li, Ri)
$$

$$
Li = siG + ciPi
$$

$$
Ri = siHp(Pi) + ciI
$$

$$
si = α - cixi (mod l)
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| q | um número primo, q = 2^255 − 19 |
| d | um elemento de Fq, d = −121665/121666 |
| E | uma equação de curva elíptica, −x^2 + y^2 = 1 + dx^2y^2 |
| G | um ponto base, G = (x,−4/5) |
| l | uma ordem prima do ponto base, l = 2^252 + 27742317777372353535851937790883648493 |
| Hs | uma função de hash criptográfica {0,1}∗ → Fq |
| Hp | uma função de hash determinística E(Fq) → E(Fq) |
| a | chave privada ec, um número a ∈ [1,l − 1] |
| A | chave pública ec, um ponto A = aG |
| (a,b) | chave de usuário privada, um par de duas chaves privadas ec diferentes |
| (a,B) | chave de rastreamento, um par de chave privada e pública ec (onde B = bG e a != b) |
| (A,B) | chave de usuário pública, um par de duas chaves públicas ec derivadas de (a,b) |
| P | chave pública de uso único |
| x | a chave privada correspondente a P |
| r | um número aleatório escolhido pelo remetente |
| I | imagem da chave |
| m | a mensagem sendo assinada |
| Pi | chaves públicas dos membros do anel |
| s | a assinatura |
| c, s | parâmetros de assinatura |
| xi | a chave privada do signatário |

## Algoritmos e Protocolos

```
Geração de chave pública de uso único: O remetente calcula a chave pública de uso único P para o destinatário usando a fórmula P = Hs(rA)G + B, onde r é um número aleatório, A é a parte pública da chave do destinatário, G é o ponto base da curva elíptica e B é a outra parte pública da chave do destinatário.
Recuperação de chave privada: O destinatário pode calcular a chave privada x correspondente a P usando a fórmula x = Hs(rA) + b, onde b é a chave privada do destinatário.
Geração de imagem de chave: A imagem da chave I é calculada como I = xHp(P), onde Hp é uma função de hash que mapeia pontos da curva elíptica para outros pontos da curva elíptica.
Geração de assinatura em anel: O signatário real usa sua chave privada xi para assinar uma mensagem m em nome de um anel de n participantes. O processo envolve a geração de valores aleatórios e o cálculo de uma série de valores c e s para cada participante, de modo que a equação de verificação seja satisfeita.
Verificação de assinatura em anel: Um verificador pode confirmar que a assinatura foi gerada por um membro do anel sem saber qual deles. A verificação envolve o uso das chaves públicas de todos os membros do anel, da imagem da chave e da mensagem para recalcular uma série de valores e garantir que eles correspondam aos valores na assinatura.
```

## Vulnerabilidades

- Ataque de criação infinita de moedas: Uma vulnerabilidade crítica descoberta no protocolo CryptoNote permitia a criação de um número ilimitado de moedas. Esta falha foi corrigida no Monero.
- Rastreabilidade de transações: Análises empíricas mostraram que as blockchains no estilo CryptoNote são vulneráveis a ataques de desanonimização, comprometendo a irrastreabilidade das transações.
- Ataques de exposição de chave: Alguns esquemas de assinatura em anel são vulneráveis a ataques de exposição de chave, onde a chave privada de um usuário pode ser comprometida.
- Ataques de negação de serviço: Uma vulnerabilidade no CryptoNote versão 0.8.9 permitia que atacantes remotos causassem uma negação de serviço.

---

# 30. Confidential Transactions - Compromissos de Pedersen, provas de alcance, fatores de cegueira

## Equações e Fórmulas

$$
C(v, r) = r*G + v*H
$$

$$
I = x * H_p(P)
$$

$$
L_j = α * G
$$

$$
R_j = α * H_p(P_j)
$$

$$
c_{j+1} = h(m, L_j, R_j)
$$

$$
L_{j+1} = s_{j+1} * G + c_{j+1} * P_{j+1}
$$

$$
R_{j+1} = s_{j+1} * H_p(P_{j+1}) + c_{j+1} * I
$$

$$
s_j = α - c_j * x mod l
$$

$$
I_j = x_j * H_p(P_j)
$$

$$
L_j_π = α_j * G
$$

$$
R_j_π = α_j * H_p(P_j_π)
$$

$$
c_{π+1} = H(m, L_1_π, R_1_π, ..., L_m_π, R_m_π)
$$

$$
L_j_{i} = s_j_i * G + c_i * P_j_i
$$

$$
R_j_{i} = s_j_i * H_p(P_j_i) + c_i * I_j
$$

$$
s_j_π = α_j - c_π * x_j mod l
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| C | Compromisso de Pedersen |
| v | Valor/montante da transação |
| r | Fator de cegueira (blinding factor) |
| G, H | Pontos geradores em uma curva elíptica |
| I | Imagem da chave (key image) |
| x | Chave privada |
| P | Chave pública |
| H_p | Função de hash que retorna um ponto na curva |
| m | Mensagem |
| α, s | Escalares aleatórios |
| c | Saída da função de hash |
| l | Ordem do grupo da curva elíptica |
| L, R | Valores intermediários no esquema de assinatura |
| MLSAG | Assinatura de Grupo Anônima Espontânea Linkable Multilayered |
| π | Índice secreto do assinante |

## Algoritmos e Protocolos

```
Esquema de Compromisso de Pedersen: Um esquema de compromisso que permite que uma parte se comprometa com um valor, mantendo-o oculto, com a capacidade de revelá-lo posteriormente. É homomórfico aditivamente.
 Assinaturas de Anel (LSAG e MLSAG): Um tipo de assinatura digital que pode ser realizada por qualquer membro de um grupo de usuários que possuam chaves. Uma mensagem assinada com uma assinatura de anel é endossada por alguém em um grupo específico de pessoas, sem revelar qual membro a assinou. A variante MLSAG permite a assinatura de vetores de chaves.
 Provas de Alcance (Range Proofs): Um tipo de prova de conhecimento zero que demonstra que um valor comprometido está dentro de um intervalo específico (por exemplo, [0, 2^n]), sem revelar o valor em si. O artigo menciona "Aggregate Schnorr Range Proofs" como um método para isso.
```

## Vulnerabilidades

- Análise de blockchain baseada em valores
- Conjunto de anonimato menor para valores menos comuns
- Criação de transações "poeira" (dust)
- Gasto duplo (Double-spending)
- Aquisição da chave mestra em configuração confiável (trusted setup)

---

# 31. MimbleWimble - cut-through, kernel, Grin, Beam, compactação de blockchain

## Equações e Fórmulas

$$
xG := G + ... + G
$$

$$
H = xG
$$

$$
X = xG
$$

$$
C := vH + rG
$$

- Com(v1
- r1) + Com(v2
$$
r2) = Com(v1 + v2
$$

- r1 + r2)
$$
\Sigma{Out} - \Sigma{In} = 0
$$

$$
\Sigma{C_{out}} - \Sigma{C_{in}} = (\Sigma{v_{out}} - \Sigma{v_{in}})H + (\Sigma{r_{out}} - \Sigma{r_{in}})G
$$

$$
\Sigma{C_{out}} - \Sigma{C_{in}} = 0H + xG
$$

$$
sum(outputs) - sum(inputs) = sum(kernel_excess) + kernel_offset*G
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| G | Ponto gerador em uma curva elíptica. |
| H | Outro ponto gerador na mesma curva elíptica, cujo logaritmo discreto em relação a G é desconhecido. |
| x | Uma chave secreta (escalar). |
| X | Uma chave pública (ponto na curva), calculada como xG. |
| v | O valor de uma entrada ou saída de transação (um escalar). |
| r | O fator de cegueira, um valor aleatório secreto usado para ofuscar o valor v. |
| C | Um compromisso de Pedersen com um valor v, calculado como vH + rG. |
| \pi | Uma prova de intervalo (range proof), que demonstra que um valor comprometido está em um intervalo específico (e.g., não é negativo) sem revelar o valor. |
| \sigma | Uma assinatura criptográfica. |
| kernel_offset | Um fator de cegueira adicional aplicado ao kernel da transação para prevenir o "problema do subconjunto". |

## Algoritmos e Protocolos

```
Compromissos de Pedersen: Um esquema de compromisso criptográfico que permite a um provador se comprometer com um valor para um verificador, mantendo-o oculto. O esquema é aditivamente homomórfico, o que significa que a soma de dois compromissos é um compromisso para a soma dos valores. No MimbleWimble, isso é usado para verificar que a soma das saídas de uma transação é igual à soma das entradas, sem revelar os valores reais.
Transações Confidenciais (CT): Proposto por Gregory Maxwell, este protocolo utiliza compromissos de Pedersen e provas de intervalo para ocultar os valores das transações em uma blockchain. O MimbleWimble baseia-se fortemente neste conceito para alcançar a confidencialidade dos valores.
CoinJoin: Um mecanismo de anonimização que combina múltiplas transações de diferentes remetentes em uma única transação, tornando mais difícil para um observador externo determinar o fluxo exato dos fundos. O MimbleWimble implementa uma forma não interativa de CoinJoin no nível do bloco.
Cut-through: Este é um mecanismo de compactação de blockchain central para o MimbleWimble. Quando uma saída é criada e subsequentemente gasta dentro do mesmo bloco (ou em blocos diferentes), tanto a saída quanto a entrada que a gasta podem ser removidas da cadeia sem comprometer a segurança. Isso ocorre porque suas contribuições para a equação de soma zero se anulam. O resultado é que o estado da cadeia consiste apenas nos cabeçalhos dos blocos, nos kernels das transações e no conjunto de saídas não gastas (UTXOs), reduzindo drasticamente o tamanho da blockchain.
Kernel Offsets: Para mitigar o "problema do subconjunto", onde um adversário poderia reconstruir as transações individuais dentro de um bloco agregado, o MimbleWimble introduz um *kernel offset*. Este é um valor secreto adicional incluído em cada kernel de transação. Ao agregar transações em um bloco, os offsets individuais são somados em um único offset agregado para o bloco inteiro, tornando impossível desvendar as transações originais.
```

## Vulnerabilidades

- Replicabilidade de Transações (Proposta Original): A proposta inicial do MimbleWimble continha uma falha onde o destinatário de uma transação poderia descobrir a chave secreta do excesso do remetente, permitindo-lhe potencialmente reverter ou modificar a transação. Implementações como Grin e Beam abordaram isso com esquemas de construção de transação interativos ou não interativos aprimorados.
- Ataque de Vinculação (Linkability Attack): Uma vulnerabilidade fundamental demonstrada por Ivan Bogatyy. Um adversário pode executar um "supernó" que se conecta a uma grande fração dos nós da rede para interceptar transações antes da fase de agregação (cut-through). Ao observar a propagação das transações (mesmo com o protocolo Dandelion), o atacante pode vincular as entradas às saídas com alta probabilidade (96% na rede Grin durante o teste), quebrando o anonimato do gráfico de transações, embora os valores permaneçam confidenciais. Esta vulnerabilidade é considerada inerente ao design do MimbleWimble.

---

# 32. Ethereum Smart Contracts - EVM, Solidity, gas, state machine, Vitalik Buterin

## Equações e Fórmulas

$$
Y(S, T) = S'
$$

- Unidades de Gás (Limite) * (Taxa Base + Taxa de Prioridade)
$$
∑𝑖=4^7 (7𝑖) * 0.1^𝑖 * 0.9^(7−𝑖) = 0.002728
$$

$$
∑𝑖=3^8 (8𝑖) * 0.1^𝑖 * 0.9^(8−𝑖) = 0.03809179
$$

$$
∑𝑖=6^8 (8𝑖) * 0.1^𝑖 * 0.9^(8−𝑖) = 0.00002341
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| S | O estado antigo válido |
| T | Um novo conjunto de transações válidas |
| S' | O novo estado de saída válido |
| Profundidade da Pilha (Stack) | 1024 itens |
| Tamanho da Palavra (Word Size) | 256-bit |
| Limite de Gás | A quantidade máxima de gás que um usuário está disposto a consumir em uma transação |
| Preço do Gás | O preço por unidade de gás |
| Taxa Base | O preço mínimo por unidade de gás definido pelo protocolo para que uma transação seja incluída em um bloco |
| Taxa de Prioridade (Gorjeta) | Uma taxa adicional paga aos validadores para incentivá-los a incluir a transação em um bloco |
| Unidades de Gás | A quantidade total de gás usada em uma transação |
| Tamanho Alvo | Metade do limite de gás para um bloco. |

## Algoritmos e Protocolos

```
Estrutura de Dados de Estado: Trie Merkle Patricia Modificada
 Memória Transiente: Array de bytes endereçado por palavra, não persiste entre transações
 Armazenamento Transiente: Armazenamento de chave-valor por transação, acessado pelos opcodes TSTORE e TLOAD. Persiste em chamadas internas na mesma transação, mas é limpo no final da transação
 Armazenamento Persistente: Trie de armazenamento Merkle Patricia associada à conta, parte do estado global
 Opcodes: XOR, AND, ADD, SUB, ADDRESS, BALANCE, BLOCKHASH, TSTORE, TLOAD
```

## Vulnerabilidades

- SC01: Vulnerabilidades de Controle de Acesso
- SC02: Manipulação de Oráculo de Preços
- SC03: Erros de Lógica
- SC04: Falta de Validação de Entrada
- SC05: Ataques de Reentrância
- SC06: Chamadas Externas Não Verificadas
- SC07: Ataques de Empréstimo Flash
- SC08: Overflow e Underflow de Inteiros
- SC09: Aleatoriedade Insegura
- SC10: Ataques de Negação de Serviço (DoS)

---

# 33. Funções de Hash Criptográficas - MD5, SHA-1, SHA-2, SHA-3, Keccak

## Equações e Fórmulas

$$
F(X,Y,Z) = (X \land Y) \lor (\neg X \land Z)
$$

$$
G(X,Y,Z) = (X \land Z) \lor (Y \land \neg Z)
$$

$$
H(X,Y,Z) = X \oplus Y \oplus Z
$$

$$
I(X,Y,Z) = Y \oplus (X \lor \neg Z)
$$

$$
a = b + ((a + F(b,c,d) + X[k] + T[i]) <<< s)
$$

$$
B,C,D) = (B \land C) \lor ((\neg B) \land D)
$$

$$
B,C,D) = B \oplus C \oplus D
$$

$$
B,C,D) = (B \land C) \lor (B \land D) \lor (C \land D)
$$

$$
W(t) = S^1(W(t-3) \oplus W(t-8) \oplus W(t-14) \oplus W(t-16))
$$

$$
TEMP = S^5(A) + f(t
$$

- B,C,D) + E + W(t) + K(t)
$$
Ch(E,F,G) = (E \land F) \oplus (\neg E \land G)
$$

$$
Maj(A,B,C) = (A \land B) \oplus (A \land C) \oplus (B \land C)
$$

$$
\Sigma_0(A) = (A \ggg 2) \oplus (A \ggg 13) \oplus (A \ggg 22)
$$

$$
\Sigma_1(E) = (E \ggg 6) \oplus (E \ggg 11) \oplus (E \ggg 25)
$$

$$
\sigma_0(w[i-15]) = (w[i-15] \ggg 7) \oplus (w[i-15] \ggg 18) \oplus (w[i-15] \gg 3)
$$

$$
\sigma_1(w[i-2]) = (w[i-2] \ggg 17) \oplus (w[i-2] \ggg 19) \oplus (w[i-2] \gg 10)
$$

$$
\theta \text{ step}: C[x] = A[x,0] \oplus A[x,1] \oplus A[x,2] \oplus A[x,3] \oplus A[x,4]
$$

$$
D[x] = C[x-1] \oplus rot(C[x+1],1)
$$

$$
\rho \text{ step}: a[i,j] = rot(a[i,j], (t+1)(t+2)/2) \text{ for } t \text{ from } 0 \text{ to } 23
$$

$$
\pi \text{ step}: A'[x,y] = A[x',y'] \text{ where } x' = y \text{ and } y' = (2x + 3y) \pmod 5
$$

$$
\chi \text{ step}: A[x,y] = A[x,y] \oplus ((\neg A[x+1,y]) \land A[x+2,y])
$$

$$
\iota \text{ step}: A[0,0] = A[0,0] \oplus RC[i_r]
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| MD5 | A, B, C, D: Registradores de 32 bits |
| M | Mensagem |
| T | Tabela de constantes |
| b | Comprimento da mensagem |
| X[k] | Palavra de 32 bits da mensagem |
| s | Número de bits para rotação |
| SHA-1 | A, B, C, D, E: Palavras de 32 bits |
| H0-H4 | Palavras de 32 bits do digest |
| W | Sequência de 80 palavras de 32 bits |
| K(t) | Constantes de passo |
| l | Comprimento da mensagem |
| SHA-2 | a-h: Variáveis de trabalho de 32 bits |
| h0-h7 | Valores de hash de 32 bits |
| k | Constantes de rodada |
| w | Array de agendamento de mensagem |
| SHA-3/Keccak | A: Array de estado |
| C, D | Variáveis intermediárias |
| RC | Constantes de rodada |
| r | Taxa |
| c | Capacidade |
| b | Largura da permutação |

## Algoritmos e Protocolos

```
MD5: O algoritmo processa a mensagem em blocos de 512 bits, através de quatro rodadas de 16 operações cada, utilizando as funções auxiliares F, G, H e I. A saída é a concatenação de quatro registradores de 32 bits.
 SHA-1: O algoritmo processa a mensagem em blocos de 512 bits, através de 80 rodadas de computação, e atualiza cinco registradores de 32 bits. A saída é a concatenação desses cinco registradores.
 SHA-2 (SHA-256): O algoritmo processa a mensagem em blocos de 512 bits, através de 64 rodadas de computação, e atualiza oito registradores de 32 bits. A saída é a concatenação desses oito registradores.
 SHA-3 (Keccak): O algoritmo utiliza a construção de esponja (sponge construction), com uma fase de absorção (absorbing) e uma fase de extração (squeezing). A mensagem é processada pela permutação Keccak-f.
```

## Vulnerabilidades

- MD5: Ataques de colisão, certificados forjados, não é adequado para uso criptográfico.
- SHA-1: Considerado inseguro para a maioria dos usos criptográficos desde 2015.
- SHA-2: Nenhuma vulnerabilidade prática conhecida.
- SHA-3/Keccak: Ataques de colisão práticos contra versões de rodadas reduzidas (até 6 rodadas). Distinguidores de soma zero para a permutação completa, mas não para a função de hash.

---

# 34. Public Key Infrastructure (PKI) - Certificados X.509, CAs, Revogação, Cadeia de Confiança

## Equações e Fórmulas

$$
C = M^e \mod n
$$

$$
M = C^d \mod n
$$

$$
r = (g^k \mod p) \mod q
$$

$$
s = (k^{-1} * (H(M) + x * r)) \mod q
$$

$$
w = (s	resse)^{-1} \mod q
$$

$$
u1 = (H(M	resse) * w) \mod q
$$

$$
u2 = (r	resse * w) \mod q
$$

$$
v = ((g^{u1} * y^{u2}) \mod p) \mod q
$$

$$
r = x_1 \mod n
$$

$$
s = k^{-1} * (z + r * d_A) \mod n
$$

$$
u1 = z * (s	resse)^{-1} \mod n
$$

$$
u2 = r	resse * (s	resse)^{-1} \mod n
$$

$$
(x_1, y_1) = u_1 * G + u_2 * Q_A
$$

$$
r	resse \equiv x_1 \pmod{n}
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| p | número primo grande |
| q | número primo grande |
| n | módulo, n = p * q |
| Φ(n) | Função Totiente de Euler, Φ(n) = (p - 1) * (q - 1) |
| e | expoente de criptografia |
| d | expoente de descriptografia |
| M | mensagem |
| C | texto cifrado |
| g | gerador |
| x | chave privada |
| y | chave pública |
| k | inteiro aleatório |
| r | componente da assinatura |
| s | componente da assinatura |
| H(M) | hash da mensagem |
| w | variável de verificação |
| u1 | variável de verificação |
| u2 | variável de verificação |
| v | variável de verificação |
| CURVE | A curva elíptica e a equação do corpo utilizadas |
| G | O ponto base da curva elíptica |
| n | A ordem inteira de G |
| dA | Chave Privada (ECDSA) |
| QA | Chave Pública (ECDSA) |
| z | L_n bits mais à esquerda de e |
| (x1, y1) | ponto na curva |

## Algoritmos e Protocolos

```
RSA: Geração de chaves, criptografia e descriptografia
 DSA: Geração de chaves, assinatura e verificação
 ECDSA: Geração de chaves, assinatura e verificação
```

## Vulnerabilidades

- Protocolos desatualizados
- Chaves fracas e rotação infrequente
- Certificados mal gerenciados
- Proteção e gerenciamento inadequados de chaves privadas
- CA raiz comprometida
- Falha na aplicação de patches e na resposta a vulnerabilidades de segurança
- Falha de design fundamental
- Emissão incorreta de certificados
- Roubo de certificados de assinatura

---

# 35. Criptografia Simétrica - AES, DES, 3DES e modos de operação CBC, ECB, CTR, GCM

## Equações e Fórmulas

$$
L_n = R_{n-1}
$$

$$
R_n = L_{n-1} \oplus f(R_{n-1}, K_n)
$$

$$
R_{n-1} = L_n
$$

$$
L_{n-1} = R_n \oplus f(L_n, K_n)
$$

$$
f(R, K) = P(S(E(R) \oplus K))
$$

$$
K_n = KS(n, KEY)
$$

$$
C = E_{K3}(D_{K2}(E_{K1}(P)))
$$

$$
P = D_{K1}(E_{K2}(D_{K3}(C)))
$$

$$
b'_i = b_i \oplus b_{(i+4) \mod 8} \oplus b_{(i+5) \mod 8} \oplus b_{(i+6) \mod 8} \oplus b_{(i+7) \mod 8} \oplus c_i
$$

$$
s'_{c}(x) = a(x) \otimes s_c(x)
$$

$$
s'_{c}(x) = a^{-1}(x) \otimes s_c(x)
$$

$$
[s'_{0,c}, s'_{1,c}, s'_{2,c}, s'_{3,c}] = [s_{0,c}, s_{1,c}, s_{2,c}, s_{3,c}] \oplus [w_{round*Nb+c}]
$$

$$
C_j = E_K(P_j)
$$

$$
P_j = D_K(C_j)
$$

$$
C_j = E_K(P_j \oplus C_{j-1})
$$

$$
P_j = D_K(C_j) \oplus C_{j-1}
$$

$$
C_j = P_j \oplus E_K(T_j)
$$

$$
P_j = C_j \oplus E_K(T_j)
$$

$$
C_j = P_j \oplus E_K(T_j)
$$

$$
g = GHASH_H(A || C)
$$

$$
T = MSB_t(g \oplus E_K(J_0))
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| P | Bloco de texto claro de 64 bits |
| C | Bloco de texto cifrado de 64 bits |
| K1, K2, K3 | Chaves DES de 56 bits |
| E_K(P) | Cifragem DES do texto claro P com a chave K |
| D_K(C) | Decifragem DES do texto cifrado C com a chave K |
| state | Matriz de bytes 4x4 que representa o bloco de dados |
| Nb | Número de colunas no state (sempre 4 para AES) |
| Nk | Número de palavras de 32 bits na chave (4, 6 ou 8) |
| Nr | Número de rodadas (10, 12 ou 14), dependendo do Nk |
| w | Escalonamento de chave (key schedule) |
| IV | Vetor de Inicialização (Initialization Vector) - um bloco de bits aleatório e imprevisível |
| T_j | Um contador único para cada bloco |
| A | Dados autenticados adicionais (Additional Authenticated Data) |
| H | Chave de autenticação derivada de K |
| J_0 | Bloco de contador inicial |

## Algoritmos e Protocolos

```
DES: Cifra de bloco simétrica com chave de 56 bits e bloco de 64 bits, baseada em uma rede de Feistel com 16 rodadas.
3DES: Cifra de bloco que aplica o DES três vezes a cada bloco de dados, com opções de chaveamento de 112 ou 168 bits.
AES: Cifra de bloco com tamanho de bloco de 128 bits e tamanhos de chave de 128, 192 ou 256 bits, baseada em uma rede de substituição-permutação.
ECB: Modo de operação onde cada bloco de texto claro é cifrado independentemente.
CBC: Modo de operação onde cada bloco de texto claro é combinado com o bloco de texto cifrado anterior antes de ser cifrado.
CTR: Modo de operação que transforma uma cifra de bloco em uma cifra de fluxo, cifrando um contador e aplicando XOR ao texto claro.
GCM: Modo de operação que fornece confidencialidade e autenticação, combinando o modo CTR com um autenticador baseado em hash universal.
```

## Vulnerabilidades

- DES: Tamanho da chave de 56 bits, tamanho do bloco de 64 bits, chaves fracas e semi-fracas, criptoanálise diferencial e linear.
- 3DES: Ataque meet-in-the-middle, tamanho do bloco de 64 bits (ataque Sweet32), desempenho lento, chaves fracas e semi-fracas.
- AES: Ataques de canal lateral, ataques de falha, ataques relacionados à chave, ataques de computação quântica (teóricos).
- ECB: Repetição de padrões, não provê integridade.
- CBC: Propagação de erro, ataque de preenchimento (padding oracle attack).
- CTR: Reutilização de contador.
- GCM: Reutilização de IV, tags de autenticação curtas.

---

# 36. Criptografia de Teoria dos Números - Números Primos, Fatorização, Teorema de Euler, Matemática RSA

## Equações e Fórmulas

$$
`b = ac`
$$

$$
`a \equiv b \pmod{m}`
$$

$$
`a+b = c+d \pmod{n}`
$$

$$
`ab = cd \pmod{n}`
$$

$$
`(2+3) \pmod{26} = 5 \pmod{26} = 5`
$$

$$
`x \equiv a_1 \pmod{m_1}`
$$

$$
`x \equiv a_2 \pmod{m_2}`
$$

- `...`
$$
`x \equiv a_k \pmod{m_k}`
$$

$$
`\phi(p) = p - 1`
$$

$$
`\phi(N) = \phi(p) \cdot \phi(q) = (p-1)(q-1)`
$$

$$
`xy \equiv 1 \pmod{m}`
$$

$$
`b^e \equiv 1 \pmod{m}`
$$

$$
`a^{p-1} \equiv 1 \pmod{p}`
$$

$$
`c \equiv m^e \pmod{N}`
$$

$$
`m \equiv c^d \pmod{N}`
$$

$$
`ed \equiv 1 \pmod{\phi(N)}`
$$

$$
`ed - 1 = k\phi(N)`
$$

$$
`ed = 1 + k'(p-1)`
$$

$$
`m^{ed} = m^{1+k'(p-1)} = m \cdot (m^{p-1})^{k'}`
$$

$$
`c^d \equiv (m^e)^d \equiv m^{ed} \pmod{p}`
$$

$$
`c \equiv m^e \pmod{N} \equiv 25^3 \pmod{187} = 15625 \pmod{187} = 104`
$$

$$
`d(3) \equiv 1 \pmod{160}`
$$

$$
`3 \cdot (-53) \equiv 1 \pmod{160}`
$$

$$
`d = -53 \pmod{160} = 107`
$$

$$
`m = c^d \pmod{N} = 104^{107} \pmod{187} = 25`
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| `a|b` | a divide b |
| `n` | um inteiro |
| `p` | um número primo |
| `m` | módulo |
| `\phi(n)` | Função totiente de Euler, o número de inteiros entre 1 e n que são relativamente primos a n. |
| `N` | pq, onde p e q são números primos. |
| `e` | um inteiro relativamente primo a `\phi(N)`. |
| `d` | o inverso de `e` módulo `\phi(N)`. |
| `c` | texto cifrado, `c \equiv m^e \pmod{N}`. |
| `m` | mensagem em texto claro. |
| `k` | um inteiro. |

## Algoritmos e Protocolos

```
Cifra de César: Substitui cada letra por outra, deslocando o alfabeto um número específico de posições.
 Criptografia RSA: 1. Bob escolhe dois números primos, `p` e `q`, e calcula `N = pq`. 2. Bob escolhe um inteiro `e` que é relativamente primo a `\phi(N)`. 3. Bob divulga `N` e `e`. 4. Alice converte sua mensagem para um número `m` módulo `N`. 5. Alice calcula `c \equiv m^e \pmod{N}`. 6. Alice envia `c` para Bob. 7. Bob encontra o inverso `d` de `e` módulo `\phi(N)`. 8. Bob calcula `m \equiv c^d \pmod{N}`.
 SSL/TLS (Secure Socket Layer/Transport Layer Security): Protocolos de comunicação criptográfica para segurança em transações online.
 PGP (Pretty Good Privacy): Protocolo de criptografia de ponta a ponta para mensagens seguras.
 Signal Protocol: Protocolo de criptografia de ponta a ponta para mensagens seguras.
 bcrypt: Função de hash de senha criptograficamente segura.
 Argon2: Função de hash de senha criptograficamente segura.
```

## Vulnerabilidades

- Cifra de César: Facilmente quebrada por análise de frequência.
- RSA: Se `e` é pequeno e `m` também é pequeno, então `m^e` pode ser menor que `N`. Nesse caso, `c = m^e`, e `m` pode ser encontrado calculando a raiz `e`-ésima de `c`. Se a mesma mensagem é enviada para múltiplos destinatários com o mesmo `e` pequeno, o Teorema Chinês do Resto pode ser usado para quebrar a criptografia.
- Ataques de força bruta: Tentativa de adivinhar senhas tentando todas as combinações possíveis.
- Ataques de dicionário: Tentativa de adivinhar senhas tentando palavras de um dicionário.
- Injeção de malware: Inserção de software malicioso em um sistema.
- Ataques à cadeia de suprimentos: Comprometimento de software ou hardware durante o processo de fabricação ou distribuição.

---

# 37. Discrete Logarithm Problem - grupos cíclicos, geradores, ordem, segurança

## Equações e Fórmulas

$$
g^x = h
$$

$$
log_c(g) = log_c(b) \cdot log_b(g)
$$

$$
a^x \equiv b \pmod{p}
$$

$$
x = g^a \pmod{p}
$$

$$
y = g^b \pmod{p}
$$

$$
C = y^a \pmod{p} = x^b \pmod{p} = g^{ab} \pmod{p}
$$

$$
c = g^d \pmod{p}
$$

$$
(k, m \cdot c^i \pmod{p})
$$

$$
k = g^i \pmod{p}
$$

$$
m = y \cdot \text{inv}(k^d) \pmod{p}
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| G | Um grupo cíclico finito |
| g | Um gerador do grupo G |
| h | Um elemento do grupo G |
| x | O logaritmo discreto de h na base g |
| n | A ordem do grupo G |
| p | Um número primo, frequentemente usado como módulo em criptografia |
| a, b | Inteiros secretos na troca de chaves de Diffie-Hellman |
| d | A chave privada no sistema Elgamal |
| c | Um componente da chave pública no sistema Elgamal |
| i, k | Inteiros aleatórios usados na cifragem Elgamal |

## Algoritmos e Protocolos

```
Busca Linear (Linear Search): Testa todas as potências de g até encontrar h, com complexidade O(n)
 Passos de bebê, passos de gigante (Baby-step giant-step): Algoritmo de encontro no meio com complexidade de tempo e espaço de O(sqrt(n))
 Algoritmo de Pohlig-Hellman: Eficiente quando a ordem do grupo n é um número liso, reduzindo o problema a subgrupos de ordem de potência prima e combinando os resultados com o Teorema Chinês do Resto, com complexidade O(Σ e_i * (log n + sqrt(p_i)))
 Algoritmo de Cálculo de Índice (Index Calculus): Algoritmo sub-exponencial para grupos como (Z/pZ)*, que cria uma base de fatores de pequenos primos e resolve um sistema de equações lineares.
```

## Vulnerabilidades

- Computação Quântica: O algoritmo de Shor pode resolver o DLP em tempo polinomial
- Ordem do Grupo Lisa: O algoritmo de Pohlig-Hellman é eficiente se a ordem do grupo n for um número liso
- Tamanho do Primo: Primos p pequenos em (Z/pZ)* tornam o DLP vulnerável
- Ataque Logjam: Vulnerabilidade em implementações de Diffie-Hellman com parâmetros fracos.

---

# 38. Criptografia baseada em reticulado - LWE, RLWE, NTRU, Pós-quântica, Kyber, Dilithium

## Equações e Fórmulas

$$
L = \{ \sum_{i=1}^{n} a_i b_i : a_i \in \mathbb{Z} \}
$$

$$
b = \langle a, s \rangle + e \pmod{q}
$$

$$
b(x) = a(x) \cdot s(x) + e(x) \pmod{q}
$$

$$
h(x) = p \cdot f_q(x) \cdot g(x) \pmod{q}
$$

$$
e(x) = r(x) \cdot h(x) + m(x) \pmod{q}
$$

$$
a(x) = f(x) \cdot e(x) \pmod{q}
$$

$$
m(x) = f_p(x) \cdot a(x) \pmod{p}
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| L | O reticulado |
| b_i | Vetores da base do reticulado |
| a_i | Coeficientes inteiros |
| n | Dimensão do espaço |
| s | O vetor secreto em Z_q^n |
| a | Um vetor conhecido, amostrado uniformemente de Z_q^n |
| b | O resultado da equação LWE, que é conhecido |
| e | Um erro (ruído) pequeno, amostrado da distribuição χ |
| q | O módulo, um inteiro grande |
| n | A dimensão do vetor secreto s e dos vetores a |
| χ | A distribuição de erro, geralmente uma Gaussiana discreta |
| s(x) | O polinômio secreto em R_q |
| a(x) | Um polinômio conhecido, amostrado uniformemente de R_q |
| b(x) | O resultado da equação RLWE, que é conhecido |
| e(x) | Um polinômio de erro pequeno, cujos coeficientes são amostrados de uma distribuição χ |
| R_q | O anel de polinômios Z_q[x] / <f(x)> |
| f(x) | Um polinômio (geralmente ciclotômico) que define o anel |
| q | O módulo, um inteiro grande |
| n | O grau do polinômio f(x) |
| f(x), g(x) | Polinômios privados com coeficientes pequenos |
| f_p(x), f_q(x) | Inversos de f(x) módulo p e q |
| h(x) | Chave pública |
| m(x) | Mensagem (polinômio) |
| r(x) | Polinômio aleatório de ofuscação |
| e(x) | Cifra (polinômio) |
| N, p, q | Parâmetros do sistema |
| Â | Matriz pública (polinômios na forma NTT) |
| s, e | Vetores secretos com coeficientes pequenos |
| t | Vetor público t = As + e |
| r', e1, e2 | Vetores de erro com coeficientes pequenos |
| u, v | Partes da cifra |
| pk, sk | Chave pública e chave secreta |
| m | Mensagem |
| c | Cifra |
| ρ, σ | Sementes aleatórias |
| G, H, J | Funções de hash (XOF e hash) |
| NTT | Transformada Rápida de Número Teórico (Number-Theoretic Transform) |
| CBD | Amostragem da distribuição binomial centrada |
| Parse, Encode, Decode, Compress, Decompress | Funções de serialização e compressão |
| A | Matriz pública |
| s1, s2 | Chaves secretas com coeficientes pequenos |
| t | Parte da chave pública t = As1 + s2 |
| y, z | Vetores usados na assinatura |
| c | Desafio (challenge) |
| w, w0, w1 | Vetores intermediários |
| pk, sk | Chave pública e chave secreta |
| M | Mensagem |
| σ | Assinatura |
| ρ, K, μ | Sementes e hashes |
| G, H, CRH | Funções de hash |
| NTT | Transformada Rápida de Número Teórico |
| CBD, SampleInBall | Funções de amostragem |
| Power2Round, Decompose, MakeHint, UseHint | Funções de manipulação de bits. |

## Algoritmos e Protocolos

```
Kyber.CPAPKE.KeyGen(): Gera as chaves pública e privada para o Kyber PKE
Kyber.CPAPKE.Enc(pk, m, r): Cifra uma mensagem 'm' usando a chave pública 'pk'
Kyber.CPAPKE.Dec(sk, c): Decifra uma cifra 'c' usando a chave secreta 'sk'
Dilithium.KeyGen(): Gera as chaves pública e privada para o Dilithium
Dilithium.Sign(sk, M): Gera uma assinatura para a mensagem 'M' usando a chave secreta 'sk'
Dilithium.Verify(pk, M, σ): Verifica a assinatura 'σ' para a mensagem 'M' usando a chave pública 'pk'
```

## Vulnerabilidades

- Escolha de Parâmetros: A segurança é sensível à escolha de N, q e distribuição de erro. Erro Pequeno: Magnitude de erro muito pequena pode viabilizar ataques. Módulo q com Estrutura Especial: Fatores pequenos em q podem ser explorados. Ataques de Side-Channel: Vazamento de informações por canais laterais (energia, tempo). Ataques de Injeção de Falhas: Introdução de falhas no hardware pode recuperar a chave. Ataques de Reticulado: Algoritmos como LLL e BKZ podem resolver os problemas subjacentes. Ataque de Força Bruta no Erro: Adivinhar o erro se a distribuição for mal escolhida. Ataques em Anéis Específicos (RLWE): Anéis com estruturas particulares podem ser vulneráveis. Vulnerabilidades de Implementação: Geradores de números aleatórios fracos ou implementação incorreta da amostragem de erro.

---

# 39. Movimento Cypherpunk - Manifesto, Timothy May, Eric Hughes, Mailing List, Privacidade

## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| Chave Pública/Privada | Par de chaves em criptografia assimétrica para criptografar e descriptografar dados, com a chave pública distribuída e a privada mantida em segredo |
| Nível de Criptografia (Forte vs. Fraca) | Complexidade e tamanho da chave de um algoritmo criptográfico, determinando sua resistência a ataques |
| Encadeamento de Remailers (Chain length) | Número de remailers intermediários usados para encaminhar uma mensagem, aumentando o anonimato. |

## Algoritmos e Protocolos

```
Sistemas de Transação Anônima: Garante que cada parte de uma transação tenha conhecimento apenas do que é estritamente necessário, desassociando a identidade da transação, implementado com dinheiro eletrônico anônimo e assinaturas digitais
 Criptoanarquia: Utiliza uma combinação de criptografia de chave pública, sistemas de prova interativa de conhecimento zero e protocolos de software para interação, autenticação e verificação, com interações na rede tornadas não rastreáveis através do roteamento extensivo de pacotes criptografados e do uso de 'caixas à prova de violação' (tamper-proof boxes)
 Remailer Anônimo Cypherpunk (Tipo I): Oculta o remetente de um e-mail criptografando a mensagem com a chave pública do remailer, que então remove os cabeçalhos de identificação e a reenvia. O encadeamento (chaining) aumenta a segurança aninhando mensagens em camadas de criptografia para uma cadeia de remailers.
```

## Vulnerabilidades

- Análise de Tráfego
- Ataques de Repetição (Replay Attacks)
- Comprometimento do Servidor do Remailer
- Vulnerabilidades de Implementação
- Mercados Abomináveis

---

# 40. Criptografia da NSA: Suite A, Suite B, Dual_EC_DRBG, Backdoors e Curvas NIST

## Equações e Fórmulas

$$
s_k = g_P(s_{k-1})
$$

$$
r_k = g_Q(s_k)
$$

$$
y^2 = x^3 - 3x + b
$$

$$
X(x, y) = x
$$

$$
t(x) = x \pmod{2^{16}}
$$

$$
g_P(x) = X(P^x)
$$

$$
g_Q(x) = t(X(Q^x))
$$

$$
s_1 = g_P(\text{seed})
$$

$$
eQ = P
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| s | o estado interno do gerador |
| r | o número aleatório gerado |
| P, Q | pontos fixos na curva elíptica |
| p | o módulo primo do corpo finito |
| b | uma constante da curva elíptica |
| e | a chave secreta da NSA |

## Algoritmos e Protocolos

```
Suite B: 
- **AES (Advanced Encryption Standard)**: Criptografia simétrica de blocos com chaves de 128, 192 ou 256 bits. Usado com os modos de operação GCM ou CTR.
- **ECDSA (Elliptic Curve Digital Signature Algorithm)**: Algoritmo de assinatura digital que usa criptografia de curva elíptica. As curvas P-256 e P-384 são especificadas.
- **ECDH (Elliptic-curve Diffie–Hellman)**: Acordo de chaves baseado em curvas elípticas, usando as mesmas curvas que o ECDSA.
- **SHA-2 (Secure Hash Algorithm 2)**: Família de funções de hash criptográficas, especificamente SHA-256 e SHA-384.

Dual_EC_DRBG (Dual Elliptic Curve Deterministic Random Bit Generator):
1. O estado interno `s` é atualizado a cada iteração: `s_k = g_P(s_{k-1})`.
2. O número aleatório `r` é gerado a partir do novo estado: `r_k = g_Q(s_k)`.
3. As funções `g_P` e `g_Q` envolvem a multiplicação de pontos na curva elíptica e a extração da coordenada x.
```

## Vulnerabilidades

- Dual_EC_DRBG:
- **Backdoor Kleptográfico**: A principal vulnerabilidade é um backdoor deliberado. Se a relação entre os pontos P e Q da curva elíptica for conhecida (ou seja, se alguém souber o valor 'e' tal que eQ = P), é possível prever a saída do gerador a partir de uma pequena amostra de sua saída (32 bytes). A NSA é a principal suspeita de conhecer esse valor 'e' para as constantes padronizadas.
- **Viés e Previsibilidade**: Independentemente do backdoor, o algoritmo demonstrou ter um leve viés, não sendo perfeitamente aleatório. A pequena quantidade de truncamento na saída permite que um invasor, com conhecimento do backdoor, reverta o processo e determine o estado interno do gerador.
- **Constantes Suspeitas**: Os pontos P e Q usados no padrão não foram gerados de forma transparente (por exemplo, usando o princípio 'nothing up my sleeve'), levantando suspeitas de que foram escolhidos especificamente para permitir o backdoor.

Curvas NIST:
- **Geração de Sementes Opaca**: As sementes usadas para gerar as curvas padrão do NIST (como P-256, P-384) foram fornecidas pela NSA sem uma explicação transparente de como foram selecionadas. Isso levanta a preocupação de que as curvas possam conter fraquezas sutis que apenas a NSA pode explorar, embora nenhuma vulnerabilidade concreta tenha sido descoberta publicamente.

Suite A:
- **Segurança por Obscuridade**: Sendo um conjunto de algoritmos classificados e não públicos, sua segurança não pode ser verificada pela comunidade criptográfica em geral. A principal fraqueza é a falta de escrutínio público, o que contraria o princípio de Kerckhoffs.

---

# 41. Mineração de Bitcoin - ASIC, pools, ajuste de dificuldade, recompensa por bloco, halving

## Equações e Fórmulas

$$
difficulty = \frac{difficulty\_1\_target}{current\_target}
$$

$$
0x0404cb * 2^{(8 * (0x1b - 3))} = 0x00000000000404CB000000000000000000000000000000000000000000000000
$$

$$
Hash Rate = \frac{D * 2^{48}}{0xffff * 600}
$$

$$
Hash Rate \approx \frac{D * 2^{32}}{600}
$$

$$
\sum_{i=0}^{32} \frac{50 * 210000}{2^i}
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| difficulty | O valor da dificuldade da rede. |
| difficulty_1_target | Um valor de referência que representa a dificuldade 1. Tradicionalmente, é um hash com os 32 bits iniciais sendo zero e o restante um. |
| current_target | O alvo de hash atual que os mineradores devem atingir. |
| D | A dificuldade. |
| i | O índice da época de halving, começando em 0. |
| 210000 | O número de blocos em cada época de halving. |
| 50 | A recompensa inicial de bloco em Bitcoin. |
| 2 | O fator pelo qual a recompensa do bloco é dividida a cada halving. |

## Algoritmos e Protocolos

```
Ajuste de Dificuldade: A dificuldade da rede Bitcoin é ajustada a cada 2016 blocos (~2 semanas) para manter o tempo médio de geração de blocos em 10 minutos. Se o tempo para minerar os 2016 blocos for menor que duas semanas, a dificuldade aumenta
 se for maior, a dificuldade diminui. O ajuste é proporcional ao desvio em relação ao tempo esperado.
Halving: A cada 210.000 blocos (~4 anos), a recompensa por bloco é reduzida pela metade. Este mecanismo controla a emissão de novos bitcoins, assegurando um fornecimento máximo de 21 milhões de unidades.
Pools de Mineração: Pools de mineração são grupos de mineradores que combinam seu poder computacional (hashrate) para aumentar a probabilidade de encontrar um bloco. As recompensas são distribuídas proporcionalmente à contribuição de cada membro.
Protocolo Stratum V2: O Stratum V2 é um protocolo de comunicação para mineração em pool que aprimora o Stratum original. Suas principais características técnicas são a criptografia de ponta a ponta, redução de latência e largura de banda, e a seleção de transações pelo minerador.
```

## Vulnerabilidades

- Antbleed
- Backdoors de Hardware
- Vulnerabilidades de Firmware
- Fraquezas de Segurança de Rede
- Centralização
- Ataques de 51%
- Ataques de Negação de Serviço (DoS)

---

# 42. Ethereum 2.0 - beacon chain, sharding, merge, validators, attestations

## Equações e Fórmulas

$$
base_reward = effective_balance * (base_reward_factor / (base_rewards_per_epoch * sqrt(sum(active_balance))))
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| Slot | uint64 - um número de slot |
| Epoch | uint64 - um número de época |
| CommitteeIndex | uint64 - um índice de comitê em um slot |
| ValidatorIndex | uint64 - um índice de registro de validador |
| Gwei | uint64 - uma quantidade em Gwei |
| Root | Bytes32 - uma raiz Merkle |
| Hash32 | Bytes32 - um hash de 256 bits |
| Version | Bytes4 - um número de versão de fork |
| DomainType | Bytes4 - um tipo de domínio |
| ForkDigest | Bytes4 - um resumo dos dados do fork atual |
| Domain | Bytes32 - um domínio de assinatura |
| BLSPubkey | Bytes48 - uma chave pública BLS12-381 |
| BLSSignature | Bytes96 - uma assinatura BLS12-381 |
| UINT64_MAX | uint64(2**64 - 1) |
| UINT64_MAX_SQRT | uint64(4294967295) |
| GENESIS_SLOT | Slot(0) |
| GENESIS_EPOCH | Epoch(0) |
| FAR_FUTURE_EPOCH | Epoch(2**64 - 1) |
| BASE_REWARDS_PER_EPOCH | uint64(4) |
| DEPOSIT_CONTRACT_TREE_DEPTH | uint64(32) |
| JUSTIFICATION_BITS_LENGTH | uint64(4) |
| ENDIANNESS | 'little' |
| BLS_WITHDRAWAL_PREFIX | Bytes1('0x00') |
| ETH1_ADDRESS_WITHDRAWAL_PREFIX | Bytes1('0x01') |
| DOMAIN_BEACON_PROPOSER | DomainType('0x00000000') |
| DOMAIN_BEACON_ATTESTER | DomainType('0x01000000') |
| DOMAIN_RANDAO | DomainType('0x02000000') |
| DOMAIN_DEPOSIT | DomainType('0x03000000') |
| DOMAIN_VOLUNTARY_EXIT | DomainType('0x04000000') |
| DOMAIN_SELECTION_PROOF | DomainType('0x05000000') |
| DOMAIN_AGGREGATE_AND_PROOF | DomainType('0x06000000') |
| DOMAIN_APPLICATION_MASK | DomainType('0x00000001') |
| ParticipationFlags | uint8 - uma representação sucinta de 8 flags de participação booleanas |
| TIMELY_SOURCE_FLAG_INDEX | 0 |
| TIMELY_TARGET_FLAG_INDEX | 1 |
| TIMELY_HEAD_FLAG_INDEX | 2 |
| TIMELY_SOURCE_WEIGHT | uint64(14) |
| TIMELY_TARGET_WEIGHT | uint64(26) |
| TIMELY_HEAD_WEIGHT | uint64(14) |
| SYNC_REWARD_WEIGHT | uint64(2) |
| PROPOSER_WEIGHT | uint64(8) |
| WEIGHT_DENOMINATOR | uint64(64) |
| DOMAIN_SYNC_COMMITTEE | DomainType('0x07000000') |
| DOMAIN_SYNC_COMMITTEE_SELECTION_PROOF | DomainType('0x08000000') |
| DOMAIN_CONTRIBUTION_AND_PROOF | DomainType('0x09000000') |
| PARTICIPATION_FLAG_WEIGHTS | [TIMELY_SOURCE_WEIGHT, TIMELY_TARGET_WEIGHT, TIMELY_HEAD_WEIGHT] |
| INACTIVITY_PENALTY_QUOTIENT_ALTAIR | uint64(50331648) |
| MIN_SLASHING_PENALTY_QUOTIENT_ALTAIR | uint64(64) |
| PROPORTIONAL_SLASHING_MULTIPLIER_ALTAIR | uint64(2) |
| SYNC_COMMITTEE_SIZE | uint64(512) |
| EPOCHS_PER_SYNC_COMMITTEE_PERIOD | uint64(256) |
| INACTIVITY_SCORE_BIAS | uint64(4) |
| INACTIVITY_SCORE_RECOVERY_RATE | uint64(16) |
| Transaction | ByteList[MAX_BYTES_PER_TRANSACTION] - uma transação |
| ExecutionAddress | Bytes20 - Endereço de conta na camada de execução |
| INACTIVITY_PENALTY_QUOTIENT_BELLATRIX | uint64(16777216) |
| MIN_SLASHING_PENALTY_QUOTIENT_BELLATRIX | uint64(32) |
| PROPORTIONAL_SLASHING_MULTIPLIER_BELLATRIX | uint64(3) |
| MAX_BYTES_PER_TRANSACTION | uint64(1073741824) |
| MAX_TRANSACTIONS_PER_PAYLOAD | uint64(1048576) |
| BYTES_PER_LOGS_BLOOM | uint64(256) |
| MAX_EXTRA_DATA_BYTES | 32 |
| TERMINAL_TOTAL_DIFFICULTY | 58750000000000000000000 |
| TERMINAL_BLOCK_HASH | Hash32() |
| TERMINAL_BLOCK_HASH_ACTIVATION_EPOCH | FAR_FUTURE_EPOCH |

## Algoritmos e Protocolos

```
O Ethereum 2.0 emprega uma variedade de algoritmos para gerenciar o consenso e a operação da beacon chain. Funções como `get_block_root`, `get_randao_mix`, e `get_seed` são fundamentais para a segurança e a aleatoriedade da rede. A seleção de validadores e a formação de comitês são gerenciadas por `get_active_validator_indices`, `get_validator_churn_limit`, `get_committee_count_per_slot`, e `get_beacon_committee`. A proposição de blocos é determinada por `get_beacon_proposer_index`. A economia da rede é governada por algoritmos que calculam recompensas e penalidades. `get_base_reward` estabelece a recompensa fundamental, enquanto `get_proposer_reward` define a recompensa para os propositores de bloco. As penalidades por inatividade e outros comportamentos maliciosos são calculadas por `get_finality_delay`, `is_in_inactivity_leak`, e `get_inactivity_penalty_deltas`. A distribuição de recompensas e penalidades é realizada por `process_rewards_and_penalties`. O ciclo de vida de um validador é gerenciado por `initiate_validator_exit` e `slash_validator`. A adição de novos validadores é tratada por `get_validator_from_deposit`, `add_validator_to_registry`, e `apply_deposit`. O processamento de blocos e suas operações são realizados por `process_block_header`, `process_randao`, `process_eth1_data`, `process_proposer_slashing`, `process_attester_slashing`, e `process_attestation`. Com a introdução do Altair, novos algoritmos foram adicionados para suportar comitês de sincronização e reformas de incentivo, como `get_next_sync_committee`, `process_sync_aggregate`, e `process_participation_flag_updates`. O Bellatrix introduziu a execução de transações, com algoritmos como `is_merge_transition_complete`, `process_execution_payload`, e `verify_and_notify_new_payload`.
```

## Vulnerabilidades

- Vulnerabilidade de reorganização de bloco: A rede comunitária é mais vulnerável a ataques de reorganização, enquanto a rede hierárquica é mais resiliente. Sistema de proposição de blocos: Risco de vazamento de informações, pois o proponente do bloco é conhecido antes da proposição. Sistema de mensagens P2P: Problemas de spam e ataques de negação de serviço (DoS). Centralização de validadores: Quatro entidades controlam 64% dos nós validadores do Ethereum, criando vulnerabilidades críticas. Ataques de roteamento: StakeBleed e KnockBlock são dois ataques representativos contra o protocolo Proof-of-Stake do Ethereum.

---

# 43. Protocolos DeFi - AMM, pools de liquidez, Uniswap, Compound, Aave, yield farming

## Equações e Fórmulas

$$
x*y=k
$$

$$
x+y=k
$$

$$
\prod(x_i)^{w_i} = k
$$

$$
oneCTokenInUnderlying = exchangeRateCurrent / (1 * 10 ^ (18 + underlyingDecimals - cTokenDecimals))
$$

$$
APY = ((((Rate / ETH Mantissa * Blocks Per Day + 1) ^ Days Per Year)) - 1) * 100
$$

$$
APR = supplyRatePerBlock / ethMantissa * blocksPerYear * 100
$$

$$
UtilizationRate(U) = TotalBorrows / (TotalLiquidity + TotalBorrows)
$$

$$
BorrowRate = BaseRate + (Utilization / Uoptimal) * Slope1
$$

$$
BorrowRate = BaseRate + Slope1 + ((Utilization - Uoptimal) / (1 - Uoptimal)) * Slope2
$$

$$
SupplyRate = BorrowRate * Utilization * (1 - ReserveFactor)
$$

$$
APR = (interest_rate / 100) * investment_capital
$$

$$
APY = (1 + r/n)^n - 1
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| x | quantidade de um token no pool de liquidez |
| y | quantidade do outro token no pool de liquidez |
| k | um valor constante |
| x_i | a quantidade de cada token no pool |
| w_i | o peso de cada token |
| exchangeRateCurrent | a taxa de câmbio atual do cToken |
| underlyingDecimals | o número de casas decimais do ativo subjacente |
| cTokenDecimals | o número de casas decimais do cToken (sempre 8) |
| Rate | a taxa de oferta ou empréstimo por bloco (`supplyRatePerBlock` ou `borrowRatePerBlock`) |
| ETH Mantissa | `1 * 10 ^ 18` |
| Blocks Per Day | número de blocos por dia (aproximadamente 7200) |
| Days Per Year | número de dias por ano (365) |
| blocksPerYear | número de blocos por ano |
| TotalBorrows | o valor total emprestado |
| TotalLiquidity | a liquidez total disponível |
| Uoptimal | a taxa de utilização ótima |
| BaseRate | a taxa de juros base |
| Slope1 | o primeiro coeficiente de inclinação da curva de juros |
| Slope2 | o segundo coeficiente de inclinação da curva de juros |
| ReserveFactor | o fator de reserva do protocolo |
| r | a taxa de juros |
| n | o número de vezes que o juro é composto por ano |

## Algoritmos e Protocolos

```
AMM (Automated Market Maker): Utiliza fórmulas matemáticas para precificar ativos em pools de liquidez. Os principais tipos incluem a Fórmula de Produto Constante, a Fórmula de Soma Constante e a Fórmula de Média Constante. Outras variações incluem Modelos de Função Híbrida, Criadores de Mercado Automatizados Dinâmicos (DAMM) e Liquidez Concentrada.
Compound: Um protocolo de empréstimo que utiliza cTokens para representar os ativos fornecidos. As taxas de juros são calculadas com base na oferta e demanda de cada mercado.
Aave: Um protocolo de liquidez não custodial onde os usuários podem participar como fornecedores ou mutuários. As taxas de juros são determinadas algoritmicamente com base na taxa de utilização do pool.
Yield Farming: Uma estratégia que envolve o fornecimento de liquidez a protocolos DeFi em troca de recompensas, geralmente na forma de tokens de governança. Os retornos são calculados usando APR (Taxa de Porcentagem Anual) e APY (Rendimento Percentual Anual).
```

## Vulnerabilidades

- Ataques de Flash Loan
- Manipulação de Oráculo
- Reentrada
- Overflows e Underflows de Inteiros
- Problemas de Controle de Acesso
- Atualizações Maliciosas de Contratos (Hooks)

---

# 44. Stablecoins - USDT, USDC, DAI, algorithmic, collateralized, peg mechanisms

## Equações e Fórmulas

$$
fee = (value * basisPointsRate) / 10000
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| basisPointsRate | A taxa em pontos-base usada para calcular a taxa de transação |
| maximumFee | A taxa máxima que pode ser cobrada por uma transação |
| value | O valor da transação |
| Taxa de Estabilidade | Uma taxa de juros sobre o DAI cunhado para regular a oferta |
| Taxa de Poupança DAI (DSR) | Uma taxa de juros paga aos detentores de DAI para incentivar a poupança |
| Rácio de Colateralização | A proporção do valor do colateral para o valor do DAI emitido |
| Token de Vínculo (Bond Token) | Um segundo token em modelos de senhoriagem, usado para absorver a volatilidade e incentivar a estabilidade |
| Oferta Elástica | A capacidade de uma stablecoin de rebase de ajustar sua oferta circulante em resposta às mudanças de preço. |

## Algoritmos e Protocolos

```
USDT Minting: Cliente transfere fiat, Tether cunha USDT via função `issue(amount)`, e envia para o cliente. USDT Redemption: Cliente envia USDT, Tether queima via `redeem(amount)`, e retorna fiat. USDT Upgrade: Contrato antigo é depreciado via `deprecate(newAddress)` e encaminha chamadas para o novo. DAI Over-collateralization: Usuários depositam colateral em CDPs para cunhar DAI. DAI Stability Fee: Taxa de juros ajustada para regular a oferta/demanda. DAI DSR: Detentores de DAI ganham juros para reduzir a oferta. DAI Liquidation: Colateral é vendido se o valor cair abaixo do limite. DAI PSM: Permite a troca de stablecoins por DAI para estabilizar o peg. Seigniorage Stablecoins: Usa um segundo token (bond) para absorver volatilidade. Rebasing Stablecoins: Ajusta o fornecimento na carteira do detentor para manter o peg. Fractional-Algorithmic: Híbrido de colateralização e algoritmo.
```

## Vulnerabilidades

- Centralização (USDT)
- Risco Regulatório (USDT)
- Transparência de Reservas (USDT)
- Bugs de Contrato Inteligente
- Implementação não padrão de ERC-20 (USDT)
- Risco de Colateral (DAI)
- Complexidade de Contrato Inteligente (DAI)
- Governança (DAI)
- Dependência de Oráculo (DAI)
- Risco de De-pegging / Espiral da Morte (Algorítmicas)
- Dependência de Incentivos de Mercado (Algorítmicas)
- Complexidade (Algorítmicas)

---

# 45. Layer 2 solutions - rollups, optimistic, zk-rollups, state channels, sidechains

## Equações e Fórmulas

$$
C = [p(s)]_1
$$

$$
e(\pi, [Z(s)]_2) = e(C - [I(s)]_1, H)
$$

$$
Q(x) = (P(x) + P(\gamma x))/2
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| C | Compromisso com o polinômio p(X) |
| p(X) | Um polinômio |
| s | Um valor secreto |
| [x]_1 | xG onde G é um gerador do grupo G_1 |
| [x]_2 | xH onde H é um gerador do grupo G_2 |
| e | Uma função de emparelhamento |
| \pi | Uma prova |
| Z(X) | Um polinômio quociente |
| I(X) | Um polinômio de interpolação |
| Q(x) | Um polinômio reduzido no protocolo FRI |
| P(x) | O polinômio original no protocolo FRI |
| \gamma | Um valor aleatório no protocolo FRI |

## Algoritmos e Protocolos

```
ZK-Rollups: 1. Um usuário assina uma transação e a submete ao ZK-Rollup. 2. A transação é incluída em um lote e agregada off-chain. 3. Uma prova de conhecimento zero (zero-knowledge proof) que verifica todas as transações no rollup é postada na mainnet da Ethereum, juntamente com as transações agrupadas como `calldata`. 4. A prova é armazenada permanentemente no histórico da Ethereum. Optimistic Rollups: 1. Um usuário assina uma transação e a submete ao sistema operacional do Optimistic Rollup. 2. A transação é incluída em um lote e agregada off-chain. 3. As transações são postadas na mainnet da Ethereum como `calldata`. 4. Se um usuário provar que uma transação está incorreta (através de uma 'prova de fraude' ou 'fraud proof'), o rollup reverte a transação. 5. Se a transação for válida, os dados são armazenados permanentemente no histórico da Ethereum. State Channels: 1. Abertura do Canal: As partes bloqueiam fundos em um contrato inteligente na blockchain principal. 2. Transações Off-Chain: Os participantes realizam transações entre si, atualizando o estado do canal e assinando as atualizações. 3. Fechamento do Canal: O estado final é submetido à blockchain principal, que atualiza os saldos e libera os fundos. Sidechains: 1. Two-Way Peg: Ativos são bloqueados na cadeia principal, e uma quantidade equivalente é emitida na sidechain. 2. Operação Independente: A sidechain opera com seu próprio mecanismo de consenso e regras. 3. Sincronização: A sidechain se comunica periodicamente com a cadeia principal para sincronizar o estado.
```

## Vulnerabilidades

- ZK-Rollups: Complexidade Criptográfica: A criptografia subjacente é complexa, cara e difícil de implementar. Manutenção Especializada: Requer conhecimento técnico avançado para implantação e manutenção. Optimistic Rollups: Longos Períodos de Retirada: Os usuários enfrentam atrasos ao retirar fundos devido ao período de contestação de fraude. State Channels: Complexidade: A configuração e o gerenciamento de canais são complexos. Risco de Contraparte: A segurança depende da honestidade dos participantes ou de um mecanismo de resolução de disputas. Capacidade do Canal: A quantidade de fundos que pode ser transacionada é limitada aos fundos bloqueados. Sidechains: Riscos de Segurança: A segurança da sidechain é independente da cadeia principal e pode ser mais fraca. Complexidade: A interoperabilidade entre a cadeia principal e a sidechain adiciona complexidade. Problemas de Interoperabilidade: Garantir uma comunicação segura e confiável entre as cadeias é um desafio.

---

# 46. Cryptocurrency exchanges - order books, matching engines, custody, hot/cold wallets

## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| price | O preço de uma ordem |
| time | O momento em que uma ordem é colocada |
| size | O tamanho de uma ordem |
| bid | Uma ordem de compra |
| ask | Uma ordem de venda |
| spread | A diferença entre o melhor bid e o melhor ask |

## Algoritmos e Protocolos

```
First-In-First-Out (FIFO): As ordens são executadas na ordem em que são recebidas. As ordens mais antigas em um determinado nível de preço são preenchidas primeiro.
 Pro-Rata: A execução da ordem é baseada no tamanho da ordem. Ordens maiores recebem uma parcela maior das negociações disponíveis.
 Price-Time Priority (PTP): As ordens com o melhor preço são executadas primeiro. Para ordens com o mesmo preço, as mais antigas são executadas primeiro.
 Partially Signed Bitcoin Transaction (PSBT): Um protocolo de assinatura offline para transações de Bitcoin.
```

## Vulnerabilidades

- Matching Engines: Volatilidade de Preços, Alto Volume de Ordens, Congestionamento da Rede, Manipulação de Mercado (spoofing, wash trading)
- Hot Wallets: Superfície de Vulnerabilidade (sempre online), Irreversibilidade de transações maliciosas
- Cold Wallets: Fricção Operacional (acesso lento), Complexidade (risco de roubo, perda ou dano físico)

---

# 47. Criptografia de Carteira - HD wallets, BIP32, BIP39, frases de semente, caminhos de derivação

## Equações e Fórmulas

$$
CS = ENT / 32
$$

$$
MS = (ENT + CS) / 11
$$

- PBKDF2(password, salt, iterations, keylength, prf)
$$
I = HMAC-SHA512(Key = c_{par}, Data = 0x00 \|\| ser_{256}(k_{par}) \|\| ser_{32}(i))
$$

$$
I = HMAC-SHA512(Key = c_{par}, Data = ser_{P}(point(k_{par})) \|\| ser_{32}(i))
$$

$$
k_{i} = parse_{256}(I_{L}) + k_{par} \pmod{n}
$$

$$
I = HMAC-SHA512(Key = c_{par}, Data = ser_{P}(K_{par}) \|\| ser_{32}(i))
$$

$$
K_{i} = point(parse_{256}(I_{L})) + K_{par}
$$

$$
K = point(k)
$$

$$
I = HMAC-SHA512(Key = \text{"Bitcoin seed"}, Data = S)
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| ENT | Comprimento da entropia inicial em bits (128, 160, 192, 224 ou 256) |
| CS | Comprimento do checksum em bits |
| MS | Comprimento da sentença mnemônica em palavras |
| password | Sentença mnemônica em formato UTF-8 NFKD |
| salt | A string "mnemonic" + passphrase em formato UTF-8 NFKD |
| iterations | 2048 |
| keylength | 512 bits (64 bytes) |
| prf | HMAC-SHA512 |
| k | Chave privada |
| c | Código da cadeia (chain code) |
| K | Chave pública |
| i | Índice da chave filha (0 a 2^31 - 1 para normal, 2^31 a 2^32 - 1 para endurecida) |
| iH | Notação para índice de chave filha endurecida (i + 2^31) |
| I | Saída de 512 bits do HMAC-SHA512 |
| IL | 32 bytes à esquerda de I |
| IR | 32 bytes à direita de I |
| kpar | Chave privada pai |
| cpar | Código da cadeia pai |
| Kpar | Chave pública pai |
| ki | Chave privada filha |
| ci | Código da cadeia filho |
| Ki | Chave pública filha |
| n | Ordem da curva secp256k1 |
| S | Semente em bytes (comprimento entre 128 e 512 bits) |

## Algoritmos e Protocolos

```
BIP39 Geração de Mnemônico: 1. Gera-se uma entropia inicial (ENT). 2. Calcula-se um checksum (CS) aplicando SHA256 na entropia e pegando os primeiros ENT / 32 bits. 3. A entropia e o checksum são concatenados. 4. A sequência de bits resultante é dividida em grupos de 11 bits. 5. Cada grupo de 11 bits é mapeado para uma palavra em uma lista pré-definida de 2048 palavras. 6. As palavras resultantes formam a sentença mnemônica.
BIP39 Geração de Semente a partir do Mnemônico: 1. A função PBKDF2 é utilizada com a sentença mnemônica como senha e a string "mnemonic" + passphrase como salt. 2. A função de pseudo-aleatoriedade é HMAC-SHA512, com 2048 iterações. 3. A saída é uma semente de 512 bits, que serve de entrada para o BIP32.
BIP32 Geração de Chave Mestra: 1. A partir de uma semente S, calcula-se I = HMAC-SHA512(Key = "Bitcoin seed", Data = S). 2. I é dividido em duas metades de 32 bytes: IL e IR. 3. A chave privada mestra é parse256(IL) e o código da cadeia mestro é IR.
BIP32 Derivação de Chave Filha (CKD): Privada Pai -> Privada Filha: Para uma chave pai (kpar, cpar) e um índice i, calcula-se I usando HMAC-SHA512. Para chaves endurecidas (i >= 2^31), a entrada de dados inclui a chave privada pai. Para chaves normais, inclui a chave pública pai. A chave filha ki é a soma da parte esquerda de I com a chave pai (mod n), e o novo código de cadeia ci é a parte direita de I. Pública Pai -> Pública Filha: O processo é análogo, mas só funciona para chaves não endurecidas e deriva apenas a chave pública filha Ki e o código de cadeia ci.
```

## Vulnerabilidades

- Vazamento de Chave Privada Pai (BIP32): A posse de uma chave pública estendida e de qualquer chave privada filha não endurecida permite a derivação da chave privada pai, comprometendo toda a hierarquia de chaves abaixo dela.
- Falta de Versionamento (BIP39): O padrão BIP39 não inclui um número de versão, o que pode causar problemas de compatibilidade entre diferentes implementações de carteira.
- Negação Plausível Fraca (BIP39): A funcionalidade de "passphrase" para criar carteiras ocultas é considerada fraca contra ataques de coerção física.
- Armazenamento Inseguro: Implementações de carteiras podem armazenar a frase de semente ou chaves privadas em texto claro em locais inseguros.
- Fraquezas de Entropia (BIP39): Preocupações sobre a qualidade da entropia gerada e a possibilidade de fraquezas estatísticas na distribuição das palavras.
- Ataques de Força Bruta e Adivinhação: Frases de semente com baixa entropia ou passphrases fracas são vulneráveis a ataques de força bruta.

---

# 48. Computação Multi-Parte (MPC), Assinaturas de Limiar (TSS) e Geração de Chave Distribuída (DKG)

## Equações e Fórmulas

$$
pk := g^{sk}
$$

$$
pk_i := g^{sk_i}
$$

$$
f(x) = s + a_1*x + ... + a_t*x^t
$$

$$
sk := \sum_{j \in T} s_j
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| λ | parâmetro de segurança |
| X | um conjunto |
| x | um elemento amostrado uniformemente ao acaso de X |
| n | número de partes na rede |
| P | conjunto de n partes {P1, ..., Pn} |
| A | um adversário bizantino |
| t | número de partes corrompidas |
| ∆ | atraso de rede em uma rede síncrona |
| v | valor de entrada |
| V | conjunto de valores |
| val | função de validade externa |
| s | segredo |
| f(x) | um polinômio usado para compartilhamento de segredos |
| sk | chave secreta |
| pk | chave pública |
| ski | compartilhamento da chave secreta da parte i |
| Y | tupla de compartilhamentos de chave pública (pk1, ..., pkn) |

## Algoritmos e Protocolos

```
Protocolo DKG Síncrono de Pedersen
 Protocolo DKG Síncrono Seguro de Gennaro et al.
 Protocolo DKG Síncrono de Fouque-Stern
 Protocolo DKG Síncrono de Canny-Sorkin
 Protocolo ADKG de Kokoris-Kogias, Malkhi e Spiegelman
 Protocolo ADKG de Das et al.
 Protocolo ADKG de Abraham et al.
 Protocolo ADKG de Gao et al.
 Protocolo ADKG de Feng et al.
```

## Vulnerabilidades

- Insegurança do DKG de Pedersen original devido à manipulação por um adversário apressado
- Impossibilidade de um DKG de uma rodada totalmente seguro
- Protocolos ADKG com custo de comunicação quase quadrático dependem de rasuras seguras para segurança adaptativa, o que é indesejável na prática.

---

# 49. Verifiable Random Functions (VRF) - randomness beacon, lottery, leader selection

## Equações e Fórmulas

$$
F_{SK}(x) = g^{1/(z+SK)}
$$

$$
p_{SK}(x) = g^{1/(z+SK)}
$$

$$
e(g,g)^{1/(z+SK)} = e(g, p_{SK}(x))
$$

$$
e(g^z, g^{SK}) \cdot e(g,g)^{1/(z+SK)} = e(g,g)
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| F_SK(x) | Função VRF com chave secreta SK e entrada x |
| p_SK(x) | Prova para a avaliação da VRF |
| g | Gerador de um grupo cíclico |
| z | Valor derivado da entrada x |
| SK | Chave secreta |
| e(·,·) | Mapa bilinear |

## Algoritmos e Protocolos

```
RSA-FDH-VRF: Uma construção de VRF baseada no RSA Full Domain Hash. Esta construção utiliza a função hash de domínio completo para fornecer uma prova da correção do hash. A segurança deste esquema baseia-se na dificuldade do problema RSA.
 ECVRF: Uma construção de VRF baseada em Curvas Elípticas. Esta construção aproveita as propriedades das curvas elípticas para criar uma VRF eficiente e segura. A segurança do ECVRF depende da dificuldade do problema do logaritmo discreto em curvas elípticas.
```

## Vulnerabilidades

- Ataques de pré-imagem: As VRFs fornecem pré-compromissos determinísticos para entradas de baixa entropia, que devem ser resistentes a ataques de pré-imagem de força bruta.
- Ataques de enumeração offline (ataques de dicionário): As VRFs podem ser usadas para defesa contra ataques de enumeração offline em dados armazenados em estruturas de dados baseadas em hash.
- Enumeração de zona no DNSSEC: O sistema NSEC5 proposto, que usa VRFs, comprovadamente impede esse tipo de ataque.

---

# 50. Escalabilidade de Blockchain - TPS, Tamanho do Bloco, Sharding, State Bloat, Pruning

## Equações e Fórmulas

$$
TPS = (tamanho do bloco / tamanho da transação) / tempo do bloco
$$


## Variáveis e Parâmetros

| Variável | Definição |
|----------|----------|
| tamanho do bloco | A quantidade de dados de transação que um bloco pode armazenar |
| tamanho da transação | Varia entre 226 bytes e 500 bytes |
| tempo do bloco | O tempo médio necessário para confirmar uma transação em uma rede. |

## Algoritmos e Protocolos

```
O tamanho de bloco ideal pode ser determinado usando algoritmos meta-heurísticos, como otimização por enxame de partículas (PSO) e o algoritmo evolucionário de força de Pareto (SPEA). O sharding é uma técnica de particionamento de banco de dados que divide uma rede blockchain em segmentos menores e mais gerenciáveis chamados "shards". O Pruning (poda) é uma técnica para reduzir o tamanho da blockchain armazenada em um nó, removendo dados históricos desnecessários. Algoritmos de Pruning: Pruning baseado em idade, Pruning baseado em tamanho, Pruning seletivo.
```

## Vulnerabilidades

- Aumento do tempo de propagação
- Centralização da mineração
- State Bloat
- Ataque de controle de shard (1%)
- Complexidade de comunicação entre shards
- Perda de dados históricos
- Confiança em nós de arquivamento.

---

# ÍNDICE DE CONEXÕES (Pessoas, Organizações, Governos)

- 1kx
- A pesquisa não revelou conexões diretas do desenvolvimento fundamental do Problema do Logaritmo Discreto com agências governamentais como a NSA ou o GCHQ. As principais contribuições vieram do meio acadêmico
- A. Back
- ANSI (American National Standards Institute)
- Academia Nacional de Ciências
- Academia Nacional de Engenharia
- Adam Back
- Adhara Ltd.
- Adi Shamir
- Agência de Segurança Nacional (NSA)
- Alex Akselrod
- Alex Vieth (Well-Typed)
- Algorand
- Algorand)
- Ampleforth
- Andrew Poelstra
- Android Bitcoin Wallet
- Apache Cassandra
- Applied Blockchain
- Arche Capital
- Ari Juels
- Armando Santos (Well-Typed)
- Association for Computing Machinery (ACM)
- Aztec
- Bain Capital
- Bain Capital Crypto
- Barbara Liskov
- Basis Cash
- Beam
- Bellcore
- Ben Lynn
- Berkeley
- Berkeley; RSA Security Inc.; GCHQ (indireta)
- Bipartisan Policy Center
- BitMine Immersion
- BitTorrent
- Bitcoin
- Bitcoin Core
- Bitcoin Core Developer
- Bitmain
- BlackBerry Limited
- BlockApps
- Blockchain Digital Capital LTD
- Blockchain for Social Impact Coalition
- Blockstream
- Blockstream;Marek Palatinus
- Bob Fabry
- Breadwallet (BRD);Sean Bowe
- Brown University
- Bruce Englar
- Burt Kaliski
- CFRG (Crypto Forum Research Group)
- CISPA Helmholtz Center for Information Security
- CPPIB
- CRYPTREC
- CWI (Centrum Wiskunde & Informatica)
- Carol Shaw
- Center for Mathematics and Computer Science (CWI)
- Certicom
- Certificate Transparency
- Chainlink
- Chainsecurity
- Charlotte Coe
- Chia Network
- Christine Peterson
- Cisco
- Claus Schnorr
- Clifford Cocks
- Clifford Cocks - GCHQ
- Coinbase Ventures
- Comissão de Assistência Eleitoral
- Compound Labs
- ConsenSys AG
- Consul
- Consórcio de Padronização de Criptografia Homomórfica (IBM
- Coralogix
- Cosmos Network
- Coti Foundation
- CryptoLab
- CryptoNote
- Cynthia Dwork
- Cypherpunks
- Cypherpunks; Eric Hughes
- Cypherpunks; John Gilmore
- Cypherpunks; National Security Agency (NSA)
- D. Bayer
- DARPA
- DFINITY
- DSA
- Dan Boneh
- David Chaum
- Davoa Capital
- Decentriq
- Departamento de Segurança Interna dos EUA (DHS)
- Dfinity
- Diego Ongaro
- DigiCash Inc.
- Digital-Certificates.com
- Dimitrios Papadopoulos (Hong Kong University of Science and Technology)
- Direct Connect
- Don Coppersmith
- Donald Beaver
- Dov Andleman
- Dragonfly Capital
- Dragonfly Research
- Duality Technologies
- Duncan Coutts (Well-Typed
- Dynamo
- ENS
- ENS Labs Ltd.
- ENS de Lyon
- ERC3643
- ElGamal
- Electronic Frontier Foundation (EFF)
- Eli Biham
- Elixxir
- Elizabeth Stark
- Emertech Innovations Pvt Ltd
- Empty Set Dollar
- Enveil
- Eric Hughes
- Ernst & Young
- Etherealize
- Ethereum
- Ethereum Foundation
- European Data Protection Supervisor
- FIPS
- Federal Bureau of Investigation (FBI)
- Fireblocks
- Florida Atlantic University
- Foresight Institute
- Frank Olken
- Franklin
- Frax
- GCHQ
- GCHQ (Government Communications Headquarters)
- GCHQ (Sede de Comunicações do Governo do Reino Unido)
- Gaia
- Garrett Wollman
- Gateway.fm
- Georg Fuchsbauer
- George Furnas
- Georgetown University
- Gilles Van Assche
- Git
- Gnutella
- Gnutella2
- Google
- Government Communications Headquarters - GCHQ
- Governo dos EUA
- Gregory Maxwell
- Grin
- H. Massias
- Hacken
- Haiyan Li
- Hal Finney
- Hovav Shacham
- I2P
- IBM
- IBM Research - Zurich
- IEEE
- IETF
- IETF (Internet Engineering Task Force)
- IOHK)
- IRTF (Internet Research Task Force)
- ISO (International Organization for Standardization)
- ITU-T - X.1035
- Inc.
- Inpher
- Inria
- Intel
- InterPlanetary File System (IPFS)
- Interchain Foundation
- International Association for Cryptologic Research (IACR)
- Ivan Bogatyy
- Ivan Damgård
- J.-J. Quisquater
- JP Morgan Chase Bank
- Jae Kwon
- James H. Ellis
- James H. Ellis - GCHQ
- Jan Včelák (NS1)
- Jeff Shrager
- Jens Berlips
- Jim Reeds
- Joan Daemen
- John Brainard
- John Ousterhout
- Joseph Poon
- Juniper Networks
- Justin Reyneri
- Kaleido
- Karl Knutsson (Cardano Foundation)
- Kevin M. Esvelt
- Keyring
- Komodo Platform
- L2beat
- Ledger
- Leonard Adleman
- Leonid Reyzin (Boston University
- Leslie Lamport
- Lido
- Linux Foundation Decentralized Trust
- Lior Goldberg
- Litecoin
- Loren Kohnfelder
- Ltd.
- MD5: Ronald L. Rivest
- MI5
- MIT
- MIT Laboratory for Computer Science
- MIT; Adi Shamir
- MIT; Carl Pomerance; Robert Rumely; Henri Cohen; Hendrik Willem Lenstra; University of Southern California (USC); Massachusetts Institute of Technology (MIT); University of California
- MakerDAO
- Malcolm J. Williamson
- Malcolm J. Williamson - GCHQ
- Marc Fontaine (IOHK)
- Marcin Szamotulski (IOHK)
- Marshall Pease
- Martin Hellman
- Marvin Minsky
- Massachusetts Institute of Technology - MIT
- Max Planck Institute for Security and Privacy
- Mercurial
- Michael Rabin (Harvard University)
- Michaël Peeters
- Michele Orru`
- Microsoft
- Miguel Castro
- Mixmaster
- Monero Research Labs
- Moni Naor
- MoonPay
- Moti Yung
- NESSIE; SHA-3/Keccak: Guido Bertoni
- NIST
- NIST (National Institute of Standards and Technology)
- NIST - SP 800-56A
- NIST)
- NSA
- NSA (Agência de Segurança Nacional dos EUA)
- NSA (National Security Agency)
- NSF
- NTT
- NYU Graduate School of Business
- National Institute of Standards and Technology (NIST)
- National Science Foundation
- National Security Agency (NSA)
- National Space Society
- Neil Davies (PNSol
- Nenhuma conexão com governos
- Nenhuma conexão direta com governos
- NewView Capital
- Nexus
- Nick Szabo
- Niobium Microsystems
- Noam Nisan; SHA-1: Ronald L. Rivest
- NodeRise Capital
- Olympix
- OpenSSL
- OpenZFS
- PGP Corporation
- Paradigm
- Peter Blatman
- Peter Todd
- Peter Winkler
- Philip Zimmermann
- Pi Squared
- Pieter Wuille
- Plume Network
- Polychain Capital
- Polygon
- Programa Bullrun
- Programa Edgehill
- Programa de Inovação do Vale do Silício (SVIP)
- Public Works
- R.C. Merkle
- RSA Data Security
- RSA Security
- RSA Security LLC
- Ralph Merkle
- Raynold Kahn
- Revolut
- Riak
- Richard Smalley
- Robert Shostak
- Robinhood
- Ron Rivest
- Rootstock (RSK)
- Ruhr-Universität Bochum
- Rusty Russell
- S. Haber
- Saarland University
- Salil Vadhan (MIT)
- San Diego
- Sanyang Liu
- Satoshi Nakamoto
- SatoshiLabs;Aaron Voisine
- SatoshiLabs;Pavol Rusnak
- SemioticLabs
- Sharon Goldberg (Boston University)
- Shen Noether
- Shimon Even
- Silvio Micali (MIT)
- Skale
- Sony
- SpamAssassin
- Stanford University
- Stanford University;Martin E. Hellman
- Stanford University;Ralph Merkle;National Science Foundation;IEEE Information Theory Group
- StarkWare
- Steve Pohlig
- Steven Levy
- Stuart Haber
- Sun Microsystems
- Talos
- Taproot
- Tari
- Technion - Israel Institute of Technology
- Terra
- Thaddeus Dryja
- The Graph
- Timothy C. May
- Tom Elvis Jedusor
- Tony Hansen
- Transak
- Tron Foundation
- U.C. Berkeley
- U.S. Air Force Office of Scientific Research
- U.S. Army Research Office
- UC Berkeley
- US Federal Information Processing Standard (FIPS); SHA-2: National Security Agency (NSA)
- US Secret Service
- Uniswap
- Universidade da Califórnia
- University College London
- University College London (UCL)
- University of California
- Urban Larsson
- Validation Cloud
- Verisign
- Vincent Rijmen
- W Q Chen
- W. Dai
- W. Feller
- W. Scott Stornetta
- W.S. Stornetta
- Walter Tuchman
- Wanchain
- Wei Dai
- Weizmann Institute of Science
- Wen
- Whitfield Diffie
- X.S. Avila
- Yacov Yacobi
- Yael Tauman Kalai
- Yannick Seurin
- ZFS
- Zcash
- Zcash Foundation
- Zerocash
- Zyvex
- a16z
- com foco na privacidade e no anonimato.
- com pesquisadores de instituições como a Universidade de Stanford (Martin Hellman) e o MIT (Leonard Adleman).
- corporações ou agências de inteligência foi encontrada durante a pesquisa. O desenvolvimento do CryptoNote e do Monero parece ser impulsionado pela comunidade de código aberto
- corporações ou agências de inteligência foi identificada durante a pesquisa.
- corporações ou agências de inteligência foi identificada durante esta pesquisa.
- corporações ou agências foi encontrada nos documentos pesquisados.
- drand
- dsrv labs Co.
- etcd
- iFinex
- kpk
- xx.network

**Total de conexões identificadas: 375**

---

# RESUMO DE VULNERABILIDADES IDENTIFICADAS

1. Confiabilidade da curva NIST: Preocupações sobre possíveis backdoors em curvas produzidas pelo NIST.
2. Complexidade de comunicação entre shards
3. Long-range attacks: Ataques que substituem uma parte significativa da blockchain, viáveis devido ao baixo custo computacional
4. Ataque Man-in-the-Middle (MitM): Um invasor intercepta a comunicação e estabelece trocas de chaves separadas com cada parte, personificando-as. A autenticação é necessária para prevenir isso.
5. CVE-2012-2459 (Invalidity Caching): Um invasor pode criar uma versão inválida de um bloco (ex: com uma transação duplicada) que possui a mesma Raiz de Merkle do bloco válido. Se um nó do Bitcoin Core receber a versão inválida primeiro, ele a armazena em cache e rejeita a versão válida, possibilitando um ataque de eclipse. A vulnerabilidade foi corrigida no Bitcoin Core.
6. MD5: Ataques de colisão, certificados forjados, não é adequado para uso criptográfico.
7. Ataques de Flash Loan
8. Ataques de enumeração offline (ataques de dicionário): As VRFs podem ser usadas para defesa contra ataques de enumeração offline em dados armazenados em estruturas de dados baseadas em hash.
9. Perda de dados históricos
10. Ataques de temporização: É possível recuperar uma chave privada TLS através de um ataque de temporização em algumas implementações do OpenSSL.
11. Emissão incorreta de certificados
12. Falsificação de tokens RPOW: O sistema depende de um servidor confiável (executando em um coprocessador criptográfico seguro) para prevenir a falsificação. Um servidor comprometido poderia potencialmente criar tokens RPOW fraudulentos.
13. Ataque de injeção de falhas
14. Ataque de extensão de comprimento: Como o estado interno completo do algoritmo é a saída, um invasor pode anexar dados adicionais à mensagem original e calcular um novo hash válido sem conhecer a mensagem original.
15. Ataque de egoísmo (Selfish Mining)
16. Matching Engines: Volatilidade de Preços, Alto Volume de Ordens, Congestionamento da Rede, Manipulação de Mercado (spoofing, wash trading)
17. AES: Ataques de canal lateral, ataques de falha, ataques relacionados à chave, ataques de computação quântica (teóricos).
18. Ataque Flood & Loot
19. Bit Gold: A dependência da arquitetura do computador, não apenas da matemática abstrata, o que pode permitir que um produtor de baixo custo inunde o mercado. A não fungibilidade do bit gold, exigindo que os negociantes combinem peças de valores diferentes em unidades maiores de valor aproximadamente igual.
20. State Bloat
21. SC04: Falta de Validação de Entrada
22. Ataque de 51%
23. Negação Plausível Fraca (BIP39): A funcionalidade de "passphrase" para criar carteiras ocultas é considerada fraca contra ataques de coerção física.
24. Gasto duplo (Double-spending)
25. Ataques de força bruta: Tentativa de adivinhar senhas tentando todas as combinações possíveis.
26. Ataque de Negação de Serviço (DoS): Um invasor pode forçar o servidor a realizar cálculos dispendiosos, consumindo recursos.
27. SC09: Aleatoriedade Insegura
28. Ataques de Texto Plano Escolhido (determinismo)
29. Nós Lentos
30. Geração de chave defeituosa
31. Rastreabilidade de transações: Análises empíricas mostraram que as blockchains no estilo CryptoNote são vulneráveis a ataques de desanonimização, comprometendo a irrastreabilidade das transações.
32. O primeiro protocolo do b-money é impraticável por depender de um canal de transmissão anônimo, síncrono e à prova de bloqueio.
33. Campos de característica pequena: Podem ser menos seguros.
34. CTR: Reutilização de contador.
35. Ordem do Grupo Lisa: O algoritmo de Pohlig-Hellman é eficiente se a ordem do grupo n for um número liso
36. Particionamento de Rede
37. CA raiz comprometida
38. Falha de design fundamental
39. Propriedade multiplicativa
40. - **Ataque Man-in-the-Middle:** O protocolo original não autentica as partes, tornando-o vulnerável a um invasor (Mallory) que se interpõe na comunicação, estabelecendo chaves separadas com Alice e Bob e retransmitindo as mensagens.
- **Ataque de Negação de Serviço (DoS):** Um invasor pode forçar o servidor a realizar cálculos computacionalmente caros, consumindo seus recursos e impedindo o serviço a usuários legítimos.
- **Ataques Práticos ao Tráfego da Internet (Logjam):** A pré-computação de logaritmos discretos para grupos de 1024 bits ou menos, comumente usados, permite que invasores bem financiados (como agências de inteligência) quebrem a criptografia. A NSA é suspeita de ter essa capacidade.
- **Computadores Quânticos:** O algoritmo de Shor pode resolver o problema do logaritmo discreto de forma eficiente, quebrando a segurança do Diffie-Hellman. Variantes pós-quânticas estão em desenvolvimento.
- **Geradores de Números Aleatórios Fracos:** Se as chaves privadas não forem geradas com aleatoriedade suficiente, torna-se mais fácil para um invasor predizê-las.
- **Corpos de Característica Pequena:** Podem ser menos seguros.
- **Ordem do Grupo G:** A ordem do grupo deve ter um fator primo grande para evitar o uso do algoritmo de Pohlig-Hellman para obter as chaves privadas.
41. Overflows e Underflows de Inteiros
42. Risco Regulatório (USDT)
43. Ataques de congestionamento
44. Enumeração de zona no DNSSEC: O sistema NSEC5 proposto, que usa VRFs, comprovadamente impede esse tipo de ataque.
45. Logjam Attack: Pré-computação para grupos DH comumente usados (especialmente de 1024 bits ou menos), permitindo que um invasor quebre a criptografia.
46. ZK-Rollups: Complexidade Criptográfica: A criptografia subjacente é complexa, cara e difícil de implementar. Manutenção Especializada: Requer conhecimento técnico avançado para implantação e manutenção. Optimistic Rollups: Longos Períodos de Retirada: Os usuários enfrentam atrasos ao retirar fundos devido ao período de contestação de fraude. State Channels: Complexidade: A configuração e o gerenciamento de canais são complexos. Risco de Contraparte: A segurança depende da honestidade dos participantes ou de um mecanismo de resolução de disputas. Capacidade do Canal: A quantidade de fundos que pode ser transacionada é limitada aos fundos bloqueados. Sidechains: Riscos de Segurança: A segurança da sidechain é independente da cadeia principal e pode ser mais fraca. Complexidade: A interoperabilidade entre a cadeia principal e a sidechain adiciona complexidade. Problemas de Interoperabilidade: Garantir uma comunicação segura e confiável entre as cadeias é um desafio.
47. Small values of 'n' in the trapdoor knapsack system weaken its security, making it susceptible to attacks similar to the greatest common divisor algorithm. The security of the DES is controversial.
48. Aumento do tempo de propagação
49. Bribery attack: Atacantes podem subornar validadores para aprovar um fork malicioso da blockchain.
50. Ataques de canal lateral (Side-channel attacks)
51. Ataque de dilatação do tempo (Time-Dilation Attack)
52. Contratos Inteligentes: A revogação da operação de um carro enquanto ele está em alta velocidade na estrada seria um problema.
53. ECB: Repetição de padrões, não provê integridade.
54. Análise de blockchain baseada em valores
55. Ataques de 51%
56. Vulnerabilidade ROCA
57. CBC: Propagação de erro, ataque de preenchimento (padding oracle attack).
58. Atualizações Maliciosas de Contratos (Hooks)
59. Geração de Chaves Fraca (primos próximos, vulnerabilidade ROCA)
60. Antbleed
61. Ordem do grupo G: Deve ter um fator primo grande para evitar o algoritmo de Pohlig-Hellman.
62. Distribuição não uniforme do byte de ordem superior: No PGP "Stealth" original, o byte de ordem superior da chave de sessão criptografada tinha uma distribuição não uniforme, tornando-o distinguível de ruído aleatório.
63. Geradores de números aleatórios fracos: Se as chaves privadas puderem ser previstas, a segurança é comprometida.
64. Ataque de texto cifrado escolhido
65. SC02: Manipulação de Oráculo de Preços
66. Protocolos ADKG com custo de comunicação quase quadrático dependem de rasuras seguras para segurança adaptativa, o que é indesejável na prática.
67. Ataques de redução de reticulado contra knapsacks de baixa densidade
68. Complexidade de Contrato Inteligente (DAI)
69. Gerador de número aleatório defeituoso para k: Se o RNG for falho, pode levar a colisões em k, permitindo a recuperação da chave privada.
70. Implementação não padrão de ERC-20 (USDT)
71. Geração de número aleatório fraca
72. Nothing at stake: Validadores são incentivados a validar todos os forks da cadeia, o que pode levar a gastos duplos. A mitigação envolve penalidades
73. Falta de Versionamento (BIP39): O padrão BIP39 não inclui um número de versão, o que pode causar problemas de compatibilidade entre diferentes implementações de carteira.
74. SC10: Ataques de Negação de Serviço (DoS)
75. Protocolos desatualizados
76. Ataques que podem retardar ou parar pagamentos
77. Transparência de Reservas (USDT)
78. 3DES: Ataque meet-in-the-middle, tamanho do bloco de 64 bits (ataque Sweet32), desempenho lento, chaves fracas e semi-fracas.
79. Ataques de pré-imagem: As VRFs fornecem pré-compromissos determinísticos para entradas de baixa entropia, que devem ser resistentes a ataques de pré-imagem de força bruta.
80. Problemas de Controle de Acesso
81. Ataque de controle de shard (1%)
82. OP_LSHIFT Crash (CVE-2010-5137)
83. MD5: Criptograficamente quebrado, com vulnerabilidades de colisão, pré-imagem e colisão de prefixo escolhido.
84. Ataque de Long Range
85. SHA-3/Keccak: Ataques de colisão práticos contra versões de rodadas reduzidas (até 6 rodadas). Distinguidores de soma zero para a permutação completa, mas não para a função de hash.
86. Escolha de Parâmetros: A segurança é sensível à escolha de N, q e distribuição de erro. Erro Pequeno: Magnitude de erro muito pequena pode viabilizar ataques. Módulo q com Estrutura Especial: Fatores pequenos em q podem ser explorados. Ataques de Side-Channel: Vazamento de informações por canais laterais (energia, tempo). Ataques de Injeção de Falhas: Introdução de falhas no hardware pode recuperar a chave. Ataques de Reticulado: Algoritmos como LLL e BKZ podem resolver os problemas subjacentes. Ataque de Força Bruta no Erro: Adivinhar o erro se a distribuição for mal escolhida. Ataques em Anéis Específicos (RLWE): Anéis com estruturas particulares podem ser vulneráveis. Vulnerabilidades de Implementação: Geradores de números aleatórios fracos ou implementação incorreta da amostragem de erro.
87. Ataques de saída em massa (Mass Exit Attacks)
88. - **Ataques de Chave Pequena:** Se o expoente de criptografia `e` for pequeno (ex: 3) e a mensagem `m` for pequena, `m^e` pode ser menor que `n`, permitindo a recuperação de `m` calculando a raiz e-ésima inteira do texto cifrado.
- **Ataque de Håstad (Broadcast Attack):** Enviar a mesma mensagem para múltiplos destinatários com o mesmo expoente `e` mas diferentes módulos `n` pode permitir a recuperação da mensagem original usando o Teorema Chinês do Resto.
- **Não-Semântica:** O RSA sem preenchimento (padding) é um algoritmo determinístico, o que o torna vulnerável a ataques de texto plano escolhido. Um atacante pode criptografar textos prováveis e comparar com o texto cifrado.
- **Propriedade Multiplicativa:** A propriedade `(m1^e * m2^e) ≡ (m1*m2)^e (mod n)` permite ataques de texto cifrado escolhido. Um atacante pode obter a decriptografia de um texto cifrado `c` ao pedir a decriptografia de `c' = c * r^e`.
- **Fatoração do Módulo:** A segurança do RSA depende da dificuldade de fatorar o módulo `n`. Se `n` for fatorado, a chave privada `d` pode ser calculada. O Algoritmo de Shor é um algoritmo quântico que pode fatorar inteiros em tempo polinomial.
- **Ataques de Timing:** Variações no tempo de decriptografia podem vazar informações sobre a chave privada.
- **Ataques de Análise de Consumo de Energia:** O consumo de energia do dispositivo durante as operações criptográficas pode revelar informações sobre a chave.
- **Ataques de Falha:** Induzir falhas no hardware durante a computação pode levar à recuperação da chave.
89. Ataques de Repetição (Replay Attacks)
90. Aquisição da chave mestra em configuração confiável (trusted setup)
91. SHA-2: Nenhuma vulnerabilidade prática conhecida.
92. Ataque de texto simples escolhido
93. Centralização do DigiCash como ponto único de falha
94. Ataques à cadeia de suprimentos: Comprometimento de software ou hardware durante o processo de fabricação ou distribuição.
95. Injeção de malware: Inserção de software malicioso em um sistema.
96. Risco de Colateral (DAI)
97. SC05: Ataques de Reentrância
98. Ataques de Temporização
99. Ataque de ciclo de substituição (Replacement Cycling Attack)
100. Ataque de griefing
101. SHA-1: Considerado inseguro para a maioria dos usos criptográficos desde 2015.
102. Complexidade (Algorítmicas)
103. Ataques de análise de canal lateral
104. Ataque de Segunda Pré-imagem (Second Preimage Attack): A Raiz de Merkle por si só não especifica a profundidade da árvore. Um invasor pode construir um documento diferente com o mesmo hash da raiz, mas com uma estrutura de árvore diferente. A mitigação envolve prefixar os dados com bytes distintos para folhas (`0x00`) e nós internos (`0x01`) antes do hashing, como especificado no Certificate Transparency.
105. Ataques contra RSA simples
106. Bugs de Contrato Inteligente
107. Ataque Zumbi (Zombie Attack)
108. Cold Wallets: Fricção Operacional (acesso lento), Complexidade (risco de roubo, perda ou dano físico)
109. Ataque de gasto duplo em massa (Mass Double-Spend Attack)
110. Confiança em nós de arquivamento.
111. SC01: Vulnerabilidades de Controle de Acesso
112. Erros em operações bioquímicas (ligação, PCR)
113. Ataque de negação de serviço (DDoS)
114. Backdoors de Hardware
115. Ataques de Pré-computação: Um atacante pode pré-computar tokens para usar em um ataque concentrado. Mitigado com timestamps ou desafios aleatórios.
116. Desempenho
117. Centralização (USDT)
118. Tamanho do Primo: Primos p pequenos em (Z/pZ)* tornam o DLP vulnerável
119. Circuitos Sub-restringidos e Não-Determinísticos, Overflows/Underflows Aritméticos, Comprimentos de Bits Incompatíveis, Maleabilidade da Prova (Groth16), Ataque do Último Desafio (Fiat-Shamir)
120. Governança (DAI)
121. Ataques de Desempenho
122. DES: Tamanho da chave de 56 bits, tamanho do bloco de 64 bits, chaves fracas e semi-fracas, criptoanálise diferencial e linear.
123. Ataques de Negação de Serviço (DoS)
124. Ataques em reticulados de ideais circulantes com bases ortonormais
125. Ataque de 51% através do sistema de revogação
126. Criação de transações "poeira" (dust)
127. CVE-2017-12842 (Transactions as txids and vice versa): Como o mesmo algoritmo de hash (SHA256d) é usado para folhas e nós internos no Bitcoin, uma transação de 64 bytes pode ser interpretada como a concatenação de dois hashes de 32 bytes de nós internos, e vice-versa. Isso pode ser explorado para enganar clientes SPV. As mitigações incluem a invalidação de transações de 64 bytes via soft fork e o uso de algoritmos de hash diferentes para diferentes partes da árvore em novas implementações como o Taproot.
128. Ataque Logjam: um invasor man-in-the-middle pode forçar uma conexão TLS a usar criptografia de nível de exportação de 512 bits, permitindo que o invasor leia e modifique os dados. Isso se deve a uma falha no protocolo TLS, e não a uma vulnerabilidade de implementação.
129. O protocolo não fornece autenticação por si só. As identidades das partes não são verificadas, tornando-o vulnerável a ataques de representação se não for usado em conjunto com um mecanismo de autenticação.
130. Escalabilidade da computação de DNA
131. Ataques a Esquemas de Padding (Ataque de Bleichenbacher no PKCS#1 v1.5)
132. Reentrada
133. Gasto duplo de hashcash: Um token hashcash poderia ser usado várias vezes se não fossem as verificações da `resource string` e do banco de dados local.
134. Dependência de Incentivos de Mercado (Algorítmicas)
135. Propriedade Multiplicativa permitindo ataques de texto cifrado escolhido
136. Mercados Abomináveis
137. Ataques de Força Bruta e Adivinhação: Frases de semente com baixa entropia ou passphrases fracas são vulneráveis a ataques de força bruta.
138. Certificados mal gerenciados
139. Quebra da Função de Hash: Se a função de hash for quebrada, todos os carimbos de data e hora emitidos anteriormente serão questionados.
140. Fatoração do módulo
141. Reutilização de k/nonce, Gerador de números aleatórios defeituoso, Ataques de tempo, Backdoors em parâmetros de curva, Nonces tendenciosos, Dependência da intratabilidade do problema Computacional Diffie-Hellman, Ataques de cálculo de índice no grupo alvo, Não é seguro contra ataques quânticos, Um adversário não deve ser capaz de criar uma assinatura agregada válida, A maioria das propostas de agregação requer uma ordem específica de assinatura, Ineficiência e complexidade em esquemas multisig ingênuos.
142. Ataque de 51%, Riscos Criptoanalíticos, Mineração Egoísta (Selfish Mining)
143. Ataques de dicionário: Tentativa de adivinhar senhas tentando palavras de um dicionário.
144. Ataques de exposição de chave: Alguns esquemas de assinatura em anel são vulneráveis a ataques de exposição de chave, onde a chave privada de um usuário pode ser comprometida.
145. Chaves fracas e rotação infrequente
146. Manipulação de Oráculo
147. Ataques de texto cifrado escolhido adaptativos
148. Fraquezas de Entropia (BIP39): Preocupações sobre a qualidade da entropia gerada e a possibilidade de fraquezas estatísticas na distribuição das palavras.
149. Gastos não autorizados (CVE-2010-5141)
150. Solução Ingênua: Violação de privacidade, alto custo de armazenamento e largura de banda, dependência da competência e confiança no TSS. TSS Confiável: Requer confiança total no TSS para não fraudar os carimbos de data/hora. Esquema de Vinculação: A segurança depende da resistência à colisão da função de hash e da ampla publicação dos hashes da cadeia.
151. Ataque de 51%: se mais da metade do poder da CPU da rede for controlada por um único atacante, ele pode gerar uma cadeia alternativa mais longa que a cadeia honesta e reverter transações.
152. Ineficiência do algoritmo de força bruta da computação de DNA.
153. Ataque de Cegueira RSA
154. Necessidade de watchtowers (serviços de terceiros) para monitorar fundos
155. Ataques Ativos e de Repetição em Redes Mix
156. MD4: Vulnerável a ataques de colisão e pré-imagem.
157. Ataques de força bruta ao SVSSP (Sparse Vector Subset Sum Problem)
158. Comprometimento do Servidor do Remailer
159. Vulnerabilidades de Implementação
160. Reutilização do valor de k: O uso do mesmo valor de k para assinaturas diferentes permite que a chave privada seja calculada.
161. Falha na aplicação de patches e na resposta a vulnerabilidades de segurança
162. Computadores Quânticos: O algoritmo de Shor pode quebrar o DH resolvendo o problema do logaritmo discreto.
163. RC5: Suscetível a ataques diferenciais com um número suficiente de textos simples escolhidos.
164. Ataque de Vinculação (Linkability Attack): Uma vulnerabilidade fundamental demonstrada por Ivan Bogatyy. Um adversário pode executar um "supernó" que se conecta a uma grande fração dos nós da rede para interceptar transações antes da fase de agregação (cut-through). Ao observar a propagação das transações (mesmo com o protocolo Dandelion), o atacante pode vincular as entradas às saídas com alta probabilidade (96% na rede Grin durante o teste), quebrando o anonimato do gráfico de transações, embora os valores permaneçam confidenciais. Esta vulnerabilidade é considerada inerente ao design do MimbleWimble.
165. RSA: Se `e` é pequeno e `m` também é pequeno, então `m^e` pode ser menor que `N`. Nesse caso, `c = m^e`, e `m` pode ser encontrado calculando a raiz `e`-ésima de `c`. Se a mesma mensagem é enviada para múltiplos destinatários com o mesmo `e` pequeno, o Teorema Chinês do Resto pode ser usado para quebrar a criptografia.
166. Necessidade de Renovação: Os carimbos de data e hora podem precisar ser renovados com novas implementações antes que as antigas sejam quebradas.
167. Centralização
168. SC06: Chamadas Externas Não Verificadas
169. Problemas de roteamento e liquidez
170. Ataques de subcampo em variantes do NTRU
171. Fraquezas de Segurança de Rede
172. Ataques de Canal Lateral (consumo de energia, predição de desvios)
173. A avaliação do custo do esforço computacional para a criação de dinheiro no b-money é problemática
174. Dificuldade de implementação: O padrão é difícil de implementar corretamente e falhas podem reduzir a segurança.
175. Impossibilidade de um DKG de uma rodada totalmente seguro
176. Dependência da segurança do algoritmo RSA no DigiCash
177. Ataque de hash circular: Uma vulnerabilidade teórica onde é possível encontrar um input_hash e um message_block que resultam em input_hash = output_hash.
178. Roubo de certificados de assinatura
179. Ataques de Replay (Gasto Duplo): O mesmo token pode ser reutilizado. O servidor deve manter um banco de dados de tokens já utilizados para evitar isso.
180. SC08: Overflow e Underflow de Inteiros
181. Dual_EC_DRBG:
- **Backdoor Kleptográfico**: A principal vulnerabilidade é um backdoor deliberado. Se a relação entre os pontos P e Q da curva elíptica for conhecida (ou seja, se alguém souber o valor 'e' tal que eQ = P), é possível prever a saída do gerador a partir de uma pequena amostra de sua saída (32 bytes). A NSA é a principal suspeita de conhecer esse valor 'e' para as constantes padronizadas.
- **Viés e Previsibilidade**: Independentemente do backdoor, o algoritmo demonstrou ter um leve viés, não sendo perfeitamente aleatório. A pequena quantidade de truncamento na saída permite que um invasor, com conhecimento do backdoor, reverta o processo e determine o estado interno do gerador.
- **Constantes Suspeitas**: Os pontos P e Q usados no padrão não foram gerados de forma transparente (por exemplo, usando o princípio 'nothing up my sleeve'), levantando suspeitas de que foram escolhidos especificamente para permitir o backdoor.

Curvas NIST:
- **Geração de Sementes Opaca**: As sementes usadas para gerar as curvas padrão do NIST (como P-256, P-384) foram fornecidas pela NSA sem uma explicação transparente de como foram selecionadas. Isso levanta a preocupação de que as curvas possam conter fraquezas sutis que apenas a NSA pode explorar, embora nenhuma vulnerabilidade concreta tenha sido descoberta publicamente.

Suite A:
- **Segurança por Obscuridade**: Sendo um conjunto de algoritmos classificados e não públicos, sua segurança não pode ser verificada pela comunidade criptográfica em geral. A principal fraqueza é a falta de escrutínio público, o que contraria o princípio de Kerckhoffs.
182. Risco de De-pegging / Espiral da Morte (Algorítmicas)
183. Computação Quântica: O algoritmo de Shor pode resolver o DLP em tempo polinomial
184. Ataque de criação infinita de moedas: Uma vulnerabilidade crítica descoberta no protocolo CryptoNote permitia a criação de um número ilimitado de moedas. Esta falha foi corrigida no Monero.
185. Ataque Logjam: Vulnerabilidade em implementações de Diffie-Hellman com parâmetros fracos.
186. Vazamento de Chave Privada Pai (BIP32): A posse de uma chave pública estendida e de qualquer chave privada filha não endurecida permite a derivação da chave privada pai, comprometendo toda a hierarquia de chaves abaixo dela.
187. Bugs que podem causar perda de fundos (CVE-2019-12998, CVE-2019-12999, CVE-2019-13000)
188. Vantagem do Hardware: Usuários com hardware mais rápido podem gerar tokens mais rapidamente.
189. A segurança do protocolo depende da dificuldade computacional de calcular logaritmos discretos. Se um algoritmo eficiente para calcular logaritmos discretos for descoberto, o protocolo será quebrado.
190. Ataques de negação de serviço: Uma vulnerabilidade no CryptoNote versão 0.8.9 permitia que atacantes remotos causassem uma negação de serviço.
191. Ataques de Fatoração (GNFS, Algoritmo de Shor)
192. Maleabilidade de Transação (Transaction Malleability)
193. SC03: Erros de Lógica
194. Conjunto de anonimato menor para valores menos comuns
195. Armazenamento Inseguro: Implementações de carteiras podem armazenar a frase de semente ou chaves privadas em texto claro em locais inseguros.
196. Vulnerabilidade a ataques man-in-the-middle: um invasor pode interceptar as chaves públicas e substituí-las por suas próprias, enganando as duas partes para que estabeleçam chaves secretas com o invasor em vez de uma com a outra. A autenticação das chaves públicas é necessária para evitar este ataque.
197. Centralização da mineração
198. Expoentes de Criptografia Baixos sem padding
199. Vulnerabilidade de reorganização de bloco: A rede comunitária é mais vulnerável a ataques de reorganização, enquanto a rede hierárquica é mais resiliente. Sistema de proposição de blocos: Risco de vazamento de informações, pois o proponente do bloco é conhecido antes da proposição. Sistema de mensagens P2P: Problemas de spam e ataques de negação de serviço (DoS). Centralização de validadores: Quatro entidades controlam 64% dos nós validadores do Ethereum, criando vulnerabilidades críticas. Ataques de roteamento: StakeBleed e KnockBlock são dois ataques representativos contra o protocolo Proof-of-Stake do Ethereum.
200. Expoente privado pequeno
201. Ameaças de adversários de nível estatal: Muitos servidores usam os mesmos números primos para a troca de chaves Diffie-Hellman. Um invasor com recursos suficientes (como um estado-nação) pode realizar um cálculo de pré-computação caro no número primo. Depois que essa pré-computação é concluída, o invasor pode quebrar rapidamente as chaves de sessão individuais que usam esse primo.
202. Falsificação de Carimbos de Data e Hora: Um adversário pode tentar preparar uma cadeia falsa de carimbos de data e hora.
203. Vulnerabilidade de jamming de retransmissão de transação (Transaction-Relay Jamming)
204. Replicabilidade de Transações (Proposta Original): A proposta inicial do MimbleWimble continha uma falha onde o destinatário de uma transação poderia descobrir a chave secreta do excesso do remetente, permitindo-lhe potencialmente reverter ou modificar a transação. Implementações como Grin e Beam abordaram isso com esquemas de construção de transação interativos ou não interativos aprimorados.
205. Ataques de Timing
206. Ataques de colisão (teóricos): Embora nenhuma colisão prática tenha sido encontrada para o SHA-256, ataques de colisão teóricos existem para versões com número reduzido de rodadas. A segurança do SHA-256 depende do número total de rodadas (64), e a redução desse número o torna mais suscetível a ataques.
207. Ataques de criptoanálise a Polly Cracker
208. Líder Malicioso
209. Proteção e gerenciamento inadequados de chaves privadas
210. Cifra de César: Facilmente quebrada por análise de frequência.
211. Dependência de Oráculo (DAI)
212. Vulnerabilidades de Firmware
213. Conluio com o TSS: No esquema ingênuo, o TSS pode conspirar com um cliente para forjar um carimbo de data e hora.
214. Hot Wallets: Superfície de Vulnerabilidade (sempre online), Irreversibilidade de transações maliciosas
215. Expoente público pequeno
216. MD2: Vulnerável a ataques de colisão, pré-imagem e pré-imagem aprimorados.
217. Ataque de 1/3
218. Análise de Tráfego em Redes Mix (Timing Attacks)
219. GCM: Reutilização de IV, tags de autenticação curtas.
220. Comprometimento de Mixes
221. A principal vulnerabilidade discutida no trabalho de Drexler é o cenário de "grey goo", onde montadores moleculares autorreplicantes poderiam consumir descontroladamente a biosfera.
222. Ataques de temporização
223. Análise de Tráfego
224. Insegurança do DKG de Pedersen original devido à manipulação por um adversário apressado
225. Assinaturas em Anel: A segurança depende da segurança das permutações trapdoor subjacentes.
226. SC07: Ataques de Empréstimo Flash
227. Centralização crescente

**Total de vulnerabilidades: 227**

---

# RELATÓRIOS TÉCNICOS INDIVIDUAIS

## Relatório: 0_B8mZ1q5uL0pKMHVSUlXI2N_1766816215389_na1fn_L2hvbWUvdWJ1bnR1L21lcmtsZV9yZXNlYXJjaC9yZXBvcnQ.md

_conteúdo omitido_


## Variáveis e Parâmetros

P: Plaintext; C: Ciphertext; K: Key; S_K: Enciphering function under key K; E, E_K: Enciphering key / Public key; D, D_K: Deciphering key / Secret key; M: Message; S: Signed message; F: One-way hash function; x, y: variables in the hash function; n: size of the message in bits; s: size of the message in bits;


## Algoritmos

O trabalho de Ralph Merkle abrange vários algoritmos e protocolos criptográficos fundamentais. A **função de hash unidirecional** é um conceito central, sendo uma função fácil de calcular, mas computacionalmente difícil de inverter, usada para mapear dados de tamanho arbitrário para saídas de tamanho fixo. Outra contribuição significativa é o **criptossistema de chave pública usando quebra-cabeças**, um método para estabelecer uma chave secreta em um canal inseguro através da resolução de quebra-cabeças criptográficos. Além disso, Merkle desenvolveu um esquema de **assinatura digital certificada**, que permite a verificação da autenticidade de uma assinatura por qualquer pessoa. Finalmente, o **knapsack com alçapão** é um criptossistema de chave pública baseado no problema da soma de subconjuntos (problema da mochila), onde a chave pública corresponde a um problema de mochila 'fácil' de resolver, e a chave privada contém a informação 'alçapão' que o torna fácil.


## Vulnerabilidades

Uma vulnerabilidade notável reside no sistema de knapsack com alçapão, onde valores pequenos de 'n' enfraquecem a segurança do sistema, tornando-o suscetível a ataques análogos ao algoritmo do máximo divisor comum. Adicionalmente, a segurança do Data Encryption Standard (DES), embora não seja uma contribuição direta de Merkle, é mencionada como controversa, o que tem implicações para a segurança de sistemas que o utilizam.


## Conexões

O trabalho de Ralph Merkle foi desenvolvido em colaboração e com o apoio de diversas pessoas e instituições. Entre os colaboradores e figuras importantes mencionadas em sua tese, destacam-se: **Steve Pohlig, Raynold Kahn, Dov Andleman, Justin Reyneri, Bob Fabry, Jim Reeds, Whitfield Diffie, Charlotte Coe, Peter Blatman, Bruce Englar, Frank Olken, Loren Kohnfelder, Carol Shaw e Martin Hellman**. As instituições que apoiaram sua pesquisa incluem a **National Science Foundation, o U.S. Air Force Office of Scientific Research, o U.S. Army Research Office, a Stanford University e a U.C. Berkeley**.


---

## Relatório: 10_YBMqxSF8HvgoqiUv0xrLZw_1766816087278_na1fn_L2hvbWUvdWJ1bnR1L3JlcG9ydA.md

# Relatório Técnico: Adam Back - Hashcash

## Equações e Fórmulas

- **Comparação de Substring:**
$x \stackrel{b}{=} y \iff \text{os primeiros } b \text{ bits de } x \text{ e } y \text{ são idênticos}$

- **Função Hashcash (Não-Interativa):**
$MINT(s, k) \rightarrow c \text{ tal que } H(s, c) \text{ tenha } k \text{ zeros à esquerda}$
$VALUE(s, c, k) \rightarrow \text{True se } H(s, c) \text{ tem } k \text{ zeros à esquerda}$

- **Função Hashcash (Interativa):**
$CHAL(s, k) \rightarrow r$
$MINT(s, r, k) \rightarrow c \text{ tal que } H(s, r, c) \text{ tenha } k \text{ zeros à esquerda}$
$VALUE(s, r, c, k) \rightarrow \text{True se } H(s, r, c) \text{ tem } k \text{ zeros à esquerda}$

- **Hashcash-Cookie MAC:**
$mac = MAC_{sk}(t, s, conn, r)$

## Variáveis e Parâmetros

- **s:** string de serviço (identificador único do serviço)
- **k:** parâmetro de dificuldade (número de zeros à esquerda no hash)
- **c:** contador (nonce)
- **H:** função de hash (ex: SHA-1)
- **r:** desafio aleatório (na versão interativa)
- **t:** timestamp
- **conn:** parâmetros da conexão
- **sk:** chave secreta do servidor
- **mac:** código de autenticação de mensagem

## Algoritmos

### Hashcash Não-Interativo (Anti-Spam)

1. O cliente cria um cabeçalho de email.
2. O cliente adiciona um campo `X-Hashcash` ao cabeçalho, contendo:
    - `ver`: versão do hashcash (ex: 1)
    - `bits`: valor de `k` (dificuldade)
    - `date`: data e hora
    - `resource`: endereço de email do destinatário
    - `ext`: extensões (opcional)
    - `rand`: string aleatória
    - `counter`: valor inicial do contador (ex: 0)
3. O cliente itera sobre o valor do `counter`, calculando o hash SHA-1 do cabeçalho `X-Hashcash` até que o hash resultante tenha `k` zeros à esquerda.
4. O servidor receptor verifica o hash. Se for válido e não tiver sido usado antes (prevenção de replay), o email é aceito.

### Hashcash Interativo (Defesa de DoS)

1. O cliente tenta estabelecer uma conexão (ex: TCP SYN).
2. O servidor, sob carga, responde com um desafio `r` (ex: no TCP SYN-ACK).
3. O cliente deve encontrar um contador `c` tal que `H(s, r, c)` tenha `k` zeros à esquerda.
4. O cliente envia `c` de volta ao servidor (ex: no TCP ACK).
5. O servidor verifica a solução. Se correta, a conexão é estabelecida.

## Vulnerabilidades

- **Ataques de Pré-computação:** Um atacante pode pré-computar uma grande quantidade de tokens válidos para usar em um ataque concentrado. O uso de timestamps ou desafios aleatórios mitiga isso.
- **Ataques de Replay (Gasto Duplo):** O mesmo token pode ser reutilizado. O servidor deve manter um banco de dados de tokens já utilizados para evitar isso. A inclusão de um timestamp permite que o banco de dados seja podado.
- **Vantagem do Hardware:** Usuários com hardware mais rápido podem gerar tokens mais rapidamente, o que pode ser uma desvantagem em alguns cenários.

## Conexões

- **Adam Back:** Inventor do Hashcash, CEO da Blockstream.
- **Cypherpunks:** Adam Back era um membro ativo da lista de emails dos cypherpunks, onde o Hashcash foi originalmente proposto.
- **Blockstream:** Empresa co-fundada por Adam Back, focada em tecnologia Bitcoin e blockchain.
- **Trabalhos Relacionados:** O paper do Hashcash cita os trabalhos de Cynthia Dwork, Moni Naor, Ari Juels e John Brainard como precursores no campo de funções de custo de CPU e quebra-cabeças de cliente.


---

## Relatório: 11_ZqhsWmRpqb9WTpaaSVvukM_1766816088894_na1fn_L2hvbWUvdWJ1bnR1L3RlY2huaWNhbF9yZXBvcnQ.md

_Relatório Técnico sobre as Contribuições de Nick Szabo_

**Assunto:** Nick Szabo - Contratos Inteligentes e Bit Gold

**Equações e Fórmulas:**

- A pesquisa não produziu nenhuma fórmula matemática específica ou equações do trabalho de Nick Szabo sobre contratos inteligentes ou bit gold. Seu trabalho é mais conceitual e descritivo.

**Variáveis e Parâmetros:**

- **Contratos Inteligentes:**
    - `collateral`: Ativos que garantem a execução do contrato.
    - `bonding`: Mecanismos que garantem o cumprimento das obrigações.
    - `property rights`: Direitos de propriedade definidos no contrato.
    - `challenge-response protocol`: Protocolo para verificar a identidade e autorização do proprietário.
    - `smart lien protocol`: Protocolo para transferir o controle de um ativo em caso de inadimplência.
- **Bit Gold:**
    - `challenge string`: Uma string de bits pública usada como desafio.
    - `proof of work string`: O resultado do trabalho computacional, gerado a partir da `challenge string`.
    - `benchmark function`: Uma função que mede o custo computacional para gerar a `proof of work string`.
    - `timestamp`: Um registro de tempo seguro e distribuído.
    - `distributed property title registry`: Um registro distribuído para rastrear a propriedade do bit gold.

**Algoritmos:**

- **Contratos Inteligentes (Exemplo de Automóvel):**
    1.  Um bloqueio para permitir seletivamente a entrada do proprietário e excluir terceiros.
    2.  Uma "porta dos fundos" para permitir a entrada do credor.
    3.  A "porta dos fundos" do credor é ativada apenas em caso de não pagamento por um determinado período.
    4.  O pagamento eletrônico final desativa permanentemente a "porta dos fundos".
- **Bit Gold:**
    1.  Uma "challenge string" pública é criada.
    2.  Um participante gera a "proof of work string" a partir da "challenge string" usando uma "benchmark function".
    3.  A "proof of work" é carimbada com data/hora de forma segura e distribuída.
    4.  O participante adiciona a "challenge string" e a "proof of work" com carimbo de data/hora a um registro de títulos de propriedade distribuído.
    5.  A última "proof of work" criada fornece a "challenge string" para a próxima.
    6.  Para verificar a propriedade, um segundo participante verifica a cadeia de títulos no registro.
    7.  Para avaliar o valor, um segundo participante verifica a "challenge string", a "proof of work" e o carimbo de data/hora.

**Vulnerabilidades:**

- **Contratos Inteligentes:**
    - A revogação da operação de um carro enquanto ele está em alta velocidade na estrada seria um problema.
- **Bit Gold:**
    - A dependência da arquitetura do computador, não apenas da matemática abstrata, o que pode permitir que um produtor de baixo custo inunde o mercado.
    - A não fungibilidade do bit gold, exigindo que os negociantes combinem peças de valores diferentes em unidades maiores de valor aproximadamente igual.

**Conexões:**

- **Hal Finney:** Implementou uma variante do bit gold chamada RPOW (Reusable Proofs of Work).


---

## Relatório: 12_NAbFkvgCk2qRolZoC1Gi0b_1766816258966_na1fn_L2hvbWUvdWJ1bnR1L3RlY2huaWNhbF9yZXBvcnRfd2VpX2RhaQ.md

# Relatório Técnico: Wei Dai, b-money e Crypto++

## 1. b-money

_b-money_ é uma proposta de dinheiro eletrônico anônimo e distribuído. A seguir, os detalhes técnicos extraídos da proposta original.

### 1.1. Algoritmos e Protocolos

*   **Criação de Dinheiro:**
    1.  Um participante resolve um problema computacional não resolvido.
    2.  A solução é transmitida para todos os participantes.
    3.  Todos os participantes creditam a conta do transmissor com um número de unidades monetárias igual ao custo do esforço computacional em termos de uma cesta padrão de commodities.
*   **Transferência de Dinheiro:**
    1.  Alice (proprietária do pseudônimo K_A) transmite uma mensagem assinada: "Eu dou X unidades de dinheiro para K_B".
    2.  Todos os participantes debitam a conta de K_A em X unidades e creditam a conta de K_B em X unidades.
    3.  A transação é ignorada se resultar em um saldo negativo para K_A.
*   **Execução de Contratos:**
    1.  Um contrato válido deve incluir uma reparação máxima em caso de inadimplência para cada parte e um árbitro.
    2.  Todas as partes, incluindo o árbitro, devem transmitir suas assinaturas do contrato.
    3.  Após a transmissão do contrato e das assinaturas, cada participante debita a conta de cada parte pelo valor de sua reparação máxima e credita uma conta especial (identificada por um hash seguro do contrato) pela soma das reparações máximas.
    4.  O contrato se torna efetivo se os débitos forem bem-sucedidos para todas as partes sem produzir um saldo negativo; caso contrário, o contrato é ignorado e as contas são revertidas.

### 1.2. Variáveis e Parâmetros

*   `K_A`: Pseudônimo (chave pública) de um participante (por exemplo, Alice).
*   `K_B`: Pseudônimo (chave pública) de outro participante (por exemplo, Bob).
*   `K_C`: Pseudônimo (chave pública) do árbitro.
*   `X`: Unidades de dinheiro a serem transferidas.
*   `P`: Um problema computacional a ser resolvido.
*   `MU`: Unidades Monetárias.

### 1.3. Vulnerabilidades e Fraquezas

*   A avaliação do custo do esforço computacional para a criação de dinheiro é problemática, pois a tecnologia de computação avança rapidamente e nem sempre de forma pública, o que pode levar a avaliações imprecisas ou desatualizadas.
*   O primeiro protocolo proposto é considerado impraticável por depender de um canal de transmissão anônimo, síncrono e à prova de bloqueio.

## 2. Crypto++

A Crypto++ é uma biblioteca de classes C++ gratuita de esquemas criptográficos. A seguir, uma lista dos algoritmos e recursos que ela contém.

### 2.1. Algoritmos

*   **Esquemas de criptografia autenticada:** GCM, CCM, EAX, ChaCha20Poly1305, XChaCha20Poly1305
*   **Cifras de fluxo de alta velocidade:** ChaCha (8/12/20), ChaCha (IETF), HC (128/256), Panama, Rabbit (128/256), Sosemanuk, Salsa20 (8/12/20), XChaCha (8/12/20), XSalsa20
*   **AES e candidatos a AES:** AES (Rijndael), RC6, MARS, Twofish, Serpent, CAST-256
*   **Outras cifras de bloco:** ARIA, Blowfish, Camellia, CHAM, HIGHT, IDEA, Kalyna (128/256/512), LEA, SEED, RC5, SHACAL-2, SIMECK, SIMON (64/128), Skipjack, SPECK (64/128), Simeck, SM4, Threefish (256/512/1024), Triple-DES (DES-EDE2 e DES-EDE3), TEA, XTEA
*   **Modos de operação de cifra de bloco:** ECB, CBC, CBC ciphertext stealing (CTS), CFB, OFB, counter mode (CTR), XTS
*   **Códigos de autenticação de mensagem:** BLAKE2b, BLAKE2s, CMAC, CBC-MAC, DMAC, GMAC (GCM), HMAC, Poly1305, SipHash, Two-Track-MAC, VMAC
*   **Funções de hash:** BLAKE2b, BLAKE2s, Keccak (F1600), SHA-1, SHA-2, SHA-3, SHAKE (128/256), SipHash, LSH (128/256), Tiger, RIPEMD (128/160/256/320), SM3, WHIRLPOOL
*   **Criptografia de chave pública:** RSA, DSA, Determinsitic DSA (RFC 6979), ElGamal, Nyberg-Rueppel (NR), Rabin-Williams (RW), EC-based German Digital Signature (ECGDSA), LUC, LUCELG, DLIES (variantes de DHAES), ESIGN
*   **Esquemas de preenchimento para sistemas de chave pública:** PKCS#1 v2.0, OAEP, PSS, PSSR, IEEE P1363 EMSA2 e EMSA5
*   **Esquemas de acordo de chave:** Diffie-Hellman (DH), Unified Diffie-Hellman (DH2), Menezes-Qu-Vanstone (MQV), Hashed MQV (HMQV), Fully Hashed MQV (FHMQV), LUCDIF, XTR-DH
*   **Criptografia de curva elíptica:** ECDSA, Determinsitic ECDSA (RFC 6979), ed25519, ECGDSA, ECNR, ECIES, x25519, ECDH, ECMQV
*   **Algoritmos inseguros ou obsoletos:** MD2, MD4, MD5, Panama Hash, DES, ARC4, SEAL 3.0, WAKE-OFB, DESX (DES-XEX3), RC2, SAFER, 3-WAY, GOST, SHARK, CAST-128, Square

### 2.2. Outros Recursos

*   **Geradores de números pseudoaleatórios (PRNG):** ANSI X9.17 apêndice C, RandomPool, VIA Padlock, DARN, RDRAND, RDSEED, NIST Hash e HMAC DRBGs
*   **Funções de derivação de chave baseadas em senha:** PBKDF1 e PBKDF2 do PKCS #5, PBKDF do apêndice B do PKCS #12, HKDF do RFC 5869, Scrypt do RFC 7914
*   **Esquema de compartilhamento de segredo de Shamir e algoritmo de dispersão de informações de Rabin (IDA)**
*   **Operações com inteiros de precisão múltipla (bignum) e polinomiais**
*   **Aritmética de campo finito, incluindo GF(p) e GF(2^n)**
*   **Geração e verificação de números primos**

## 3. Conexões

*   **1kx:** Wei Dai é sócio de pesquisa na 1kx, uma empresa de investimentos focada em infraestrutura de blockchain e tecnologias emergentes.
*   **Bain Capital Crypto:** Foi sócio de pesquisa na Bain Capital Crypto em 2022.
*   **Universidade da Califórnia, San Diego (UCSD):** Obteve seu Ph.D. em Ciência da Computação na UC San Diego, onde sua pesquisa se concentrou em criptografia e segurança.

Não foram encontradas conexões diretas com governos, agências de inteligência (NSA, GCHQ) ou grandes corporações fora do setor de criptomoedas e investimentos em tecnologia.


---

## Relatório: 13_s0txKACqWQCNdDyBsihWUG_1766816200412_na1fn_L2hvbWUvdWJ1bnR1L3JlcG9ydA.md


P_z = (p/q)^z; q_z = ((1 - (p/q)^z) / (1 - p/q)) * (p/q)^z

p: probabilidade de um nó honesto encontrar o próximo bloco;q: probabilidade de o atacante encontrar o próximo bloco;z: número de blocos que o atacante precisa alcançar
1. Novas transações são transmitidas para todos os nós.
2. Cada nó coleta novas transações em um bloco.
3. Cada nó trabalha para encontrar uma prova de trabalho para seu bloco.
4. Quando um nó encontra uma prova de trabalho, ele transmite o bloco para todos os nós.
5. Os nós aceitam o bloco somente se todas as transações nele forem válidas e ainda não tiverem sido gastas.
6. Os nós expressam sua aceitação do bloco trabalhando na criação do próximo bloco na cadeia, usando o hash do bloco aceito como o hash anterior.
Ataque de 51%: se mais da metade do poder da CPU da rede for controlada por um único atacante, ele pode gerar uma cadeia alternativa mais longa que a cadeia honesta e reverter transações.
W. Dai; H. Massias; X.S. Avila; J.-J. Quisquater; S. Haber; W.S. Stornetta; D. Bayer; A. Back; R.C. Merkle; W. Feller


---

## Relatório: 14_vhHu8r2hFyU5z5ogAJBjB6_1766816667624_na1fn_L2hvbWUvdWJ1bnR1L2RyZXhsZXJfcmVwb3J0.md

# Relatório Técnico: K. Eric Drexler e Nanotecnologia

## Equações e Fórmulas

Nenhuma equação ou fórmula matemática foi encontrada nas fontes pesquisadas.

## Variáveis e Parâmetros

Nenhuma variável ou parâmetro específico foi encontrado nas fontes pesquisadas.

## Algoritmos

Nenhum algoritmo ou pseudocódigo detalhado foi encontrado nas fontes pesquisadas. O trabalho de Drexler é mais conceitual do que uma implementação algorítmica.

## Vulnerabilidades

A principal vulnerabilidade discutida no trabalho de Drexler é o cenário de "grey goo", onde montadores moleculares autorreplicantes poderiam consumir descontroladamente a biosfera.

## Conexões

- **MIT:** Onde obteve seu Ph.D. em Nanotecnologia Molecular.
- **Foresight Institute:** Co-fundador, uma organização de pesquisa para promover a nanotecnologia.
- **Christine Peterson:** Co-fundadora do Foresight Institute.
- **Marvin Minsky:** Escreveu o prefácio de "Engines of Creation".
- **Richard Smalley:** Notável crítico das visões de Drexler, com quem teve um debate público.
-chave.
- **National Space Society:** Drexler atua como governador.
- **Zyvex:** Empresa de nanotecnologia onde Drexler trabalhou.


---

## Relatório: 15_zX8s8KZD9tWDmcTZPY8VmQ_1766816118365_na1fn_L2hvbWUvdWJ1bnR1L3JzYV9yZXBvcnQ.md

# Relatório Técnico sobre o Algoritmo RSA

## Equações e Fórmulas

- Geração de Chaves:
  - `n = p \times q`
  - `\lambda(n) = \text{lcm}(p-1, q-1)`
  - `1 < e < \lambda(n)` e `\text{gcd}(e, \lambda(n)) = 1`
  - `d \equiv e^{-1} \pmod{\lambda(n)}`

- Criptografia:
  - `c \equiv m^e \pmod{n}`

- Decriptografia:
  - `m \equiv c^d \pmod{n}`

- Relação Fundamental:
  - `(m^e)^d \equiv m \pmod{n}`

- Assinatura Digital:
  - `h = \text{hash}(m)`
  - `s \equiv h^d \pmod{n}`

- Verificação de Assinatura:
  - `s^e \equiv h \pmod{n}`

- Teorema Chinês do Resto (Otimização):
  - `d_P = d \pmod{p-1}`
  - `d_Q = d \pmod{q-1}`
  - `q_{\text{inv}} = q^{-1} \pmod{p}`
  - `m_1 = c^{d_P} \pmod{p}`
  - `m_2 = c^{d_Q} \pmod{q}`
  - `h = q_{\text{inv}} \times (m_1 - m_2) \pmod{p}`
  - `m = m_2 + h \times q`


## Variáveis e Parâmetros

- `p`, `q`: Dois números primos grandes e distintos, mantidos em segredo.
- `n`: Módulo RSA, produto de `p` e `q`. É parte da chave pública.
- `λ(n)`: Função totiente de Carmichael de `n`, mantida em segredo.
- `e`: Expoente da chave pública, um inteiro tal que `1 < e < λ(n)` e `gcd(e, λ(n)) = 1`.
- `d`: Expoente da chave privada, o inverso multiplicativo modular de `e` módulo `λ(n)`.
- `m`: Mensagem original (texto claro).
- `c`: Mensagem criptografada (texto cifrado).
- `h`: Valor de hash da mensagem.
- `s`: Assinatura digital.
- `d_P`, `d_Q`: Expoentes para otimização com o Teorema Chinês do Resto.
- `q_inv`: Coeficiente para otimização com o Teorema Chinês do Resto.

## Algoritmos

### Geração de Chave
1.  Escolha dois números primos grandes e distintos, `p` e `q`.
2.  Calcule `n = p * q`.
3.  Calcule `λ(n) = lcm(p-1, q-1)`.
4.  Escolha um inteiro `e` tal que `1 < e < λ(n)` e `gcd(e, λ(n)) = 1`.
5.  Determine `d` como `d ≡ e⁻¹ (mod λ(n))`.
6.  A chave pública é `(n, e)` e a chave privada é `d`.

### Criptografia
1.  Receba a mensagem `m`.
2.  Calcule o texto cifrado `c ≡ m^e (mod n)`.

### Decriptografia
1.  Receba o texto cifrado `c`.
2.  Calcule a mensagem `m ≡ c^d (mod n)`.

### Assinatura Digital
1.  Calcule o hash da mensagem: `h = hash(m)`.
2.  Crie a assinatura: `s ≡ h^d (mod n)`.

### Verificação de Assinatura
1.  Receba a mensagem `m` e a assinatura `s`.
2.  Calcule o hash da mensagem: `h = hash(m)`.
3.  Verifique se `s^e ≡ h (mod n)`.

## Vulnerabilidades

- **Ataques de Chave Pequena:** Se o expoente de criptografia `e` for pequeno (ex: 3) e a mensagem `m` for pequena, `m^e` pode ser menor que `n`, permitindo a recuperação de `m` calculando a raiz e-ésima inteira do texto cifrado.
- **Ataque de Håstad (Broadcast Attack):** Enviar a mesma mensagem para múltiplos destinatários com o mesmo expoente `e` mas diferentes módulos `n` pode permitir a recuperação da mensagem original usando o Teorema Chinês do Resto.
- **Não-Semântica:** O RSA sem preenchimento (padding) é um algoritmo determinístico, o que o torna vulnerável a ataques de texto plano escolhido. Um atacante pode criptografar textos prováveis e comparar com o texto cifrado.
- **Propriedade Multiplicativa:** A propriedade `(m1^e * m2^e) ≡ (m1*m2)^e (mod n)` permite ataques de texto cifrado escolhido. Um atacante pode obter a decriptografia de um texto cifrado `c` ao pedir a decriptografia de `c' = c * r^e`.
- **Fatoração do Módulo:** A segurança do RSA depende da dificuldade de fatorar o módulo `n`. Se `n` for fatorado, a chave privada `d` pode ser calculada. O Algoritmo de Shor é um algoritmo quântico que pode fatorar inteiros em tempo polinomial.
- **Ataques de Timing:** Variações no tempo de decriptografia podem vazar informações sobre a chave privada.
- **Ataques de Análise de Consumo de Energia:** O consumo de energia do dispositivo durante as operações criptográficas pode revelar informações sobre a chave.
- **Ataques de Falha:** Induzir falhas no hardware durante a computação pode levar à recuperação da chave.

## Conexões

- **Inventores Públicos:** Ron Rivest, Adi Shamir, Leonard Adleman (Massachusetts Institute of Technology - MIT)
- **Inventor Secreto:** Clifford Cocks (Government Communications Headquarters - GCHQ, Reino Unido)
- **Empresa Associada:** RSA Security LLC
- **Agências Governamentais:** O GCHQ, uma agência de inteligência britânica, desenvolveu um sistema equivalente em segredo. A Agência de Segurança Nacional (NSA) dos EUA também está envolvida no campo da criptografia e segurança.


---

## Relatório: 16_Q3Qu1z1KHszguFJIAhZlL3_1766816297606_na1fn_L2hvbWUvdWJ1bnR1L2RpZmZpZV9oZWxsbWFuX3JlcG9ydA.md


## Equações e Fórmulas

`A = g^a \pmod{p}`;`B = g^b \pmod{p}`;`s = B^a \pmod{p}`;`s = A^b \pmod{p}`;`A^b \pmod{p} = (g^a)^b \pmod{p} = g^{ab} \pmod{p}`;`B^a \pmod{p} = (g^b)^a \pmod{p} = g^{ba} \pmod{p}`;`g^{ab} \pmod{p}`;`g^{abc} \pmod{p}`;`g^{bc} \pmod{p}`;`g^{ca} \pmod{p}`;`K = \text{KDF}(Y^x, B^x, Y^a, X, Y, A, B)`;`K = \text{KDF}(X^y, X^b, A^y, X, Y, A, B)`;`(g^a \pmod{p}, g, p)`;`(g^a)^b \pmod{p}`

## Variáveis e Parâmetros

p: um número primo (módulo);g: uma raiz primitiva módulo p (base);a: o inteiro secreto de Alice (chave privada);b: o inteiro secreto de Bob (chave privada);A: a chave pública de Alice;B: a chave pública de Bob;s: o segredo compartilhado;G: um grupo cíclico finito;n: ordem do grupo G;x, y: chaves efêmeras;X, Y: chaves públicas efêmeras;IKA, IKB: chaves de identidade de Alice e Bob;EKA: chave efêmera de Alice;SPKB: chave pré-assinada de Bob;OPKB: chave pré-única de Bob;KDF: função de derivação de chave

## Algoritmos

**Troca de Chaves Diffie-Hellman:**
1. Alice e Bob concordam publicamente em usar um módulo `p` e uma base `g`.
2. Alice escolhe um inteiro secreto `a` e envia a Bob `A = g^a mod p`.
3. Bob escolhe um inteiro secreto `b` e envia a Alice `B = g^b mod p`.
4. Alice calcula `s = B^a mod p`.
5. Bob calcula `s = A^b mod p`.
6. Alice e Bob agora compartilham um segredo `s`.

**Generalização para Grupos Cíclicos Finitos:**
1. Alice e Bob concordam com um número natural `n` e um elemento gerador `g` no grupo cíclico finito `G` de ordem `n`.
2. Alice escolhe um número natural aleatório `a` com `1 < a < n` e envia o elemento `g^a` de `G` para Bob.
3. Bob escolhe um número natural aleatório `b` com `1 < b < n` e envia o elemento `g^b` de `G` para Alice.
4. Alice calcula o elemento `(g^b)^a = g^{ba}` de `G`.
5. Bob calcula o elemento `(g^a)^b = g^{ab}` de `G`.

**Operação com Mais de Duas Partes (Exemplo com Alice, Bob e Carol):**
1. As partes concordam com os parâmetros do algoritmo `p` e `g`.
2. As partes geram suas chaves privadas, `a`, `b` e `c`.
3. Alice calcula `g^a mod p` e envia para Bob.
4. Bob calcula `(g^a)^b mod p = g^{ab} mod p` e envia para Carol.
5. Carol calcula `(g^{ab})^c mod p = g^{abc} mod p` e o usa como seu segredo.
6. Bob calcula `g^b mod p` e envia para Carol.
7. Carol calcula `(g^b)^c mod p = g^{bc} mod p` e envia para Alice.
8. Alice calcula `(g^{bc})^a mod p = g^{bca} mod p = g^{abc} mod p` e o usa como seu segredo.
9. Carol calcula `g^c mod p` e envia para Alice.
10. Alice calcula `(g^c)^a mod p = g^{ca} mod p` e envia para Bob.
11. Bob calcula `(g^{ca})^b mod p = g^{cab} mod p = g^{abc} mod p` e o usa como seu segredo.

## Vulnerabilidades

- **Ataque Man-in-the-Middle:** O protocolo original não autentica as partes, tornando-o vulnerável a um invasor (Mallory) que se interpõe na comunicação, estabelecendo chaves separadas com Alice e Bob e retransmitindo as mensagens.
- **Ataque de Negação de Serviço (DoS):** Um invasor pode forçar o servidor a realizar cálculos computacionalmente caros, consumindo seus recursos e impedindo o serviço a usuários legítimos.
- **Ataques Práticos ao Tráfego da Internet (Logjam):** A pré-computação de logaritmos discretos para grupos de 1024 bits ou menos, comumente usados, permite que invasores bem financiados (como agências de inteligência) quebrem a criptografia. A NSA é suspeita de ter essa capacidade.
- **Computadores Quânticos:** O algoritmo de Shor pode resolver o problema do logaritmo discreto de forma eficiente, quebrando a segurança do Diffie-Hellman. Variantes pós-quânticas estão em desenvolvimento.
- **Geradores de Números Aleatórios Fracos:** Se as chaves privadas não forem geradas com aleatoriedade suficiente, torna-se mais fácil para um invasor predizê-las.
- **Corpos de Característica Pequena:** Podem ser menos seguros.
- **Ordem do Grupo G:** A ordem do grupo deve ter um fator primo grande para evitar o uso do algoritmo de Pohlig-Hellman para obter as chaves privadas.

## Conexões Institucionais

Whitfield Diffie,Martin Hellman,Ralph Merkle,James H. Ellis - GCHQ,Clifford Cocks - GCHQ,Malcolm J. Williamson - GCHQ,National Security Agency (NSA),NIST - SP 800-56A,ITU-T - X.1035



---

## Relatório: 17_MDszfhKUhfdSlLj600yIAc_1766816320455_na1fn_L2hvbWUvdWJ1bnR1L3JlcG9ydA.md

# Relatório Técnico sobre Criptografia de Curva Elíptica (ECC)

## Equações e Fórmulas (LaTeX)

AlicePubKey * BobPrivKey = BobPubKey * AlicePrivKey = SharedSecret;
Q = kP;
y^2 = x^3 + ax + b;
e = HASH(m);
r = x1 mod n;
s = k^-1(z + r*dA) mod n;
u1 = z*s^-1 mod n;
u2 = r*s^-1 mod n;
(x1, y1) = u1 * G + u2 * QA;

## Variáveis e Parâmetros

priv: chave privada; pub: chave pública; a: coeficiente da equação da curva elíptica; b: coeficiente da equação da curva elíptica; x: coordenada x de um ponto na curva; y: coordenada y de um ponto na curva; n: número de vezes que um ponto é 'pontilhado' com ele mesmo;

## Algoritmos

### Algoritmo de Geração de Assinatura ECDSA

1. Calcule `e = HASH(m)`.
2. Seja `z` os `Ln` bits mais à esquerda de `e`, onde `Ln` é o comprimento em bits da ordem do grupo `n`.
3. Selecione um inteiro aleatório criptograficamente seguro `k` de `[1, n-1]`.
4. Calcule o ponto da curva `(x1, y1) = k * G`.
5. Calcule `r = x1 mod n`. Se `r = 0`, volte para a etapa 3.
6. Calcule `s = k^-1(z + r*dA) mod n`. Se `s = 0`, volte para a etapa 3.
7. A assinatura é o par `(r, s)`.

### Algoritmo de Verificação de Assinatura ECDSA

1. Verifique se `r` e `s` são inteiros em `[1, n-1]`.
2. Calcule `e = HASH(m)`.
3. Seja `z` os `Ln` bits mais à esquerda de `e`.
4. Calcule `u1 = z*s^-1 mod n` e `u2 = r*s^-1 mod n`.
5. Calcule o ponto da curva `(x1, y1) = u1 * G + u2 * QA`. Se `(x1, y1) = O`, a assinatura é inválida.
6. A assinatura é válida se `r ≡ x1 (mod n)`.

## Vulnerabilidades

Reutilização do valor de k: O uso do mesmo valor de k para assinaturas diferentes permite que a chave privada seja calculada.;Gerador de número aleatório defeituoso para k: Se o RNG for falho, pode levar a colisões em k, permitindo a recuperação da chave privada.;Ataques de temporização: É possível recuperar uma chave privada TLS através de um ataque de temporização em algumas implementações do OpenSSL.;Confiabilidade da curva NIST: Preocupações sobre possíveis backdoors em curvas produzidas pelo NIST.;Dificuldade de implementação: O padrão é difícil de implementar corretamente e falhas podem reduzir a segurança.

## Conexões

NIST, NSA


---

## Relatório: 18_CWgR076yryz4e2IAstJvJs_1766816104210_na1fn_L2hvbWUvdWJ1bnR1L3NoYTI1Nl9yZXBvcnQ.md

Σ0(x) = ROTR(2, x) ^ ROTR(13, x) ^ ROTR(22, x);Σ1(x) = ROTR(6, x) ^ ROTR(11, x) ^ ROTR(25, x);σ0(x) = ROTR(7, x) ^ ROTR(18, x) ^ (x>>>3);σ1(x) = ROTR(17, x) ^ ROTR(19, x) ^ (x>>>10);Ch(x, y, z) = (x & y) ^ (~x & z);Maj(x, y, z) = (x & y) ^ (x & z) ^ (y & z);T1 = h + Σ1(e) + Ch(e, f, g) + K[t] + W[t];T2 = Σ0(a) + Maj(a, b, c);W[t] = (σ1(W[t-2]) + W[t-7] + σ0(W[t-15]) + W[t-16]) >>> 0
K: um array de 64 constantes de 32 bits;H: um array de 8 valores de hash iniciais de 32 bits;W: um array de 64 palavras de 32 bits, representando o cronograma de mensagens;a, b, c, d, e, f, g, h: variáveis de trabalho de 32 bits;T1, T2: variáveis temporárias de 32 bits
1. Pre-processamento: A mensagem de entrada é preenchida para garantir que seu comprimento seja um múltiplo de 512 bits. Um único bit '1' é anexado à mensagem, seguido por bits '0' até que o comprimento da mensagem seja 64 bits menor que um múltiplo de 512. Os 64 bits restantes são preenchidos com o comprimento da mensagem original.
2. Processamento em Blocos: A mensagem preenchida é processada em blocos de 512 bits. Cada bloco é dividido em 16 palavras de 32 bits.
3. Cronograma de Mensagens: Um cronograma de mensagens de 64 palavras de 32 bits (W) é criado a partir das 16 palavras do bloco de mensagens.
4. Compressão: O coração do algoritmo é a função de compressão, que opera em um loop de 64 iterações (rounds). Em cada iteração, as variáveis de trabalho (a, b, c, d, e, f, g, h) são atualizadas usando as constantes K, o cronograma de mensagens W e as funções lógicas (Ch, Maj, Σ0, Σ1, σ0, σ1).
5. Atualização do Hash: Após 64 iterações, os valores das variáveis de trabalho são adicionados aos valores de hash intermediários (H). O resultado é o novo valor de hash intermediário.
6. Saída: Após o processamento de todos os blocos de mensagens, o valor final do hash é a concatenação dos 8 valores de hash intermediários de 32 bits, resultando em um hash de 256 bits.
Ataque de extensão de comprimento: Como o estado interno completo do algoritmo é a saída, um invasor pode anexar dados adicionais à mensagem original e calcular um novo hash válido sem conhecer a mensagem original.;Ataques de colisão (teóricos): Embora nenhuma colisão prática tenha sido encontrada para o SHA-256, ataques de colisão teóricos existem para versões com número reduzido de rodadas. A segurança do SHA-256 depende do número total de rodadas (64), e a redução desse número o torna mais suscetível a ataques.;Ataque de hash circular: Uma vulnerabilidade teórica onde é possível encontrar um input_hash e um message_block que resultam em input_hash = output_hash.
National Security Agency (NSA),National Institute of Standards and Technology (NIST),GCHQ


---

## Relatório: 19_SmPIHpCSm6ttW4Or8zaQVE_1766816184009_na1fn_L2hvbWUvdWJ1bnR1L21lcmtsZV90cmVlX3JlcG9ydA.md

# Relatório Técnico: Árvores de Merkle

## Equações e Fórmulas

- Construção do nó pai: $$M_{i} = \text{hash}(M_{2i} \| M_{2i+1})$$

## Variáveis e Parâmetros

- `M_i`: Nó na árvore de Merkle.
- `hash()`: Função de hash criptográfica (ex: SHA-2, Tiger).
- `||`: Operação de concatenação.
- `O(n)`: Complexidade de espaço e travessia.
- `O(log n)`: Complexidade de busca, inserção, deleção e sincronização.

## Algoritmos

### Construção da Árvore de Merkle

1.  **Hashing das Folhas:** Cada bloco de dados (transação) é hasheado individualmente, formando os nós folha da árvore.
2.  **Construção dos Nós Internos:** Os nós internos são construídos recursivamente. Os nós folha são agrupados em pares, e o hash da concatenação de cada par é calculado, formando o nó pai. Se houver um número ímpar de nós em um nível, o último nó é duplicado e pareado consigo mesmo.
3.  **Cálculo da Raiz de Merkle:** O processo continua até que reste apenas um único hash, a Raiz de Merkle (Merkle Root), que representa a "impressão digital" de todo o conjunto de dados.

### Prova de Inclusão (Inclusion Proof) e Verificação de Pagamento Simplificada (SPV)

- Para provar que um dado específico (transação) pertence à árvore, um cliente precisa apenas do dado, da Raiz de Merkle e do "ramo" de hashes irmãos ao longo do caminho do dado até a raiz.
- O cliente recalcula a Raiz de Merkle usando o hash do dado e o ramo fornecido. Se a raiz calculada corresponder à Raiz de Merkle conhecida, a inclusão do dado é verificada de forma eficiente, sem a necessidade de baixar e processar todo o conjunto de dados. Este é o princípio por trás da Verificação de Pagamento Simplificada (SPV) em criptomoedas.

## Vulnerabilidades

- **Ataque de Segunda Pré-imagem (Second Preimage Attack):** A Raiz de Merkle por si só não especifica a profundidade da árvore. Um invasor pode construir um documento diferente com o mesmo hash da raiz, mas com uma estrutura de árvore diferente. A mitigação envolve prefixar os dados com bytes distintos para folhas (`0x00`) e nós internos (`0x01`) antes do hashing, como especificado no Certificate Transparency.
- **CVE-2012-2459 (Invalidity Caching):** Um invasor pode criar uma versão inválida de um bloco (ex: com uma transação duplicada) que possui a mesma Raiz de Merkle do bloco válido. Se um nó do Bitcoin Core receber a versão inválida primeiro, ele a armazena em cache e rejeita a versão válida, possibilitando um ataque de eclipse. A vulnerabilidade foi corrigida no Bitcoin Core.
- **CVE-2017-12842 (Transactions as txids and vice versa):** Como o mesmo algoritmo de hash (SHA256d) é usado para folhas e nós internos no Bitcoin, uma transação de 64 bytes pode ser interpretada como a concatenação de dois hashes de 32 bytes de nós internos, e vice-versa. Isso pode ser explorado para enganar clientes SPV. As mitigações incluem a invalidação de transações de 64 bytes via soft fork e o uso de algoritmos de hash diferentes para diferentes partes da árvore em novas implementações como o Taproot.

## Conexões

- **Ralph Merkle:** Inventor do conceito de Árvore de Hash, patenteado em 1979.
- **Satoshi Nakamoto:** Incorporou as Árvores de Merkle no design do Bitcoin, conforme descrito em seu whitepaper de 2008.
- **Bitcoin Core:** A implementação de referência do Bitcoin, que utiliza Árvores de Merkle para agrupar transações em blocos e onde as vulnerabilidades CVE-2012-2459 e CVE-2017-12842 foram identificadas e corrigidas.
- **Taproot:** Uma atualização do Bitcoin que introduz novos usos para as Árvores de Merkle com regras de construção aprimoradas para maior segurança e flexibilidade.
- **Komodo Platform:** Utiliza Árvores de Merkle em sua solução de escalabilidade para alcançar interoperabilidade entre blockchains.
- **Governos e Corporações (Aplicações):** As Árvores de Merkle são usadas em uma vasta gama de sistemas que requerem verificação de integridade de dados, incluindo:
    - **Sistemas de Arquivos:** ZFS, OpenZFS.
    - **Sistemas de Controle de Versão:** Git, Mercurial.
    - **Redes Peer-to-Peer (P2P):** BitTorrent, Gnutella, Gnutella2, Direct Connect.
    - **Sistemas de Banco de Dados NoSQL:** Apache Cassandra, Riak, Dynamo.
    - **Sistemas de Arquivos Distribuídos:** InterPlanetary File System (IPFS).
    - **Segurança de Infraestrutura:** Certificate Transparency.


---

## Relatório: 1_wzsuVAV9bddj3BcWX8Ocpc_1766816072349_na1fn_L2hvbWUvdWJ1bnR1L3RlY2huaWNhbF9yZXBvcnQ.md

_Sujeito: Whitfield Diffie - troca de chaves Diffie-Hellman, criptografia de chave pública, New Directions in Cryptography 1976, Sun Microsystems_

**Equações e Fórmulas**
- `A = g^a \mod p`
- `B = g^b \mod p`
- `s = B^a \mod p`
- `s = A^b \mod p`
- `(g^a \mod p)^b \mod p = (g^b \mod p)^a \mod p`
- `K = KDF(Y^x, B^x, Y^a, X, Y, A, B)`
- `g^{abc} \mod p`

**Variáveis e Parâmetros**
- `p`: módulo primo
- `g`: base (raiz primitiva módulo p)
- `a`: chave privada de Alice
- `b`: chave privada de Bob
- `A`: chave pública de Alice
- `B`: chave pública de Bob
- `s`: segredo compartilhado
- `x, y`: chaves efêmeras
- `X, Y`: chaves públicas efêmeras
- `IKA, EKA`: chave de identidade e chave efêmera de Alice (X3DH)
- `IKB, SPKB, OPKB`: chave de identidade, prekey assinada e prekey de uso único de Bob (X3DH)
- `K`: chave derivada

**Algoritmos**
- **Troca de chaves Diffie-Hellman:**
    1. Alice e Bob concordam publicamente com um módulo primo `p` e uma base `g`.
    2. Alice escolhe um inteiro secreto `a` e envia a Bob `A = g^a \mod p`.
    3. Bob escolhe um inteiro secreto `b` e envia a Alice `B = g^b \mod p`.
    4. Alice calcula `s = B^a \mod p`.
    5. Bob calcula `s = A^b \mod p`.
    6. Alice e Bob agora compartilham o segredo `s`.
- **Triple Diffie-Hellman (3-DH):**
    - Utiliza chaves de longo prazo (a, b) e chaves efêmeras (x, y).
    - O segredo compartilhado K é derivado usando uma Key Derivation Function (KDF) a partir de uma combinação das chaves públicas e privadas.
- **Extended Triple Diffie–Hellman (X3DH):**
    - Usado no Signal Protocol.
    - Utiliza uma chave de identidade (IK), uma chave efêmera (EK) e, para o respondente, uma chave pré-assinada (SPK) e uma chave pré-compartilhada de uso único (OPK).
- **Operação com mais de duas partes:**
    - Um processo iterativo onde cada participante eleva o valor intermediário à sua chave privada e o passa para o próximo, até que todos tenham contribuído.

**Vulnerabilidades**
- **Ataque Man-in-the-Middle (MitM):** Um invasor intercepta a comunicação e estabelece trocas de chaves separadas com cada parte, personificando-as. A autenticação é necessária para prevenir isso.
- **Ataque de Negação de Serviço (DoS):** Um invasor pode forçar o servidor a realizar cálculos dispendiosos, consumindo recursos.
- **Logjam Attack:** Pré-computação para grupos DH comumente usados (especialmente de 1024 bits ou menos), permitindo que um invasor quebre a criptografia.
- **Computadores Quânticos:** O algoritmo de Shor pode quebrar o DH resolvendo o problema do logaritmo discreto.
- **Geradores de números aleatórios fracos:** Se as chaves privadas puderem ser previstas, a segurança é comprometida.
- **Campos de característica pequena:** Podem ser menos seguros.
- **Ordem do grupo G:** Deve ter um fator primo grande para evitar o algoritmo de Pohlig-Hellman.

**Conexões**
- Whitfield Diffie, Martin Hellman, Ralph Merkle, James H. Ellis, Clifford Cocks, Malcolm J. Williamson, GCHQ, Sun Microsystems, NSA


---

## Relatório: 20_M1SnxhsCNEZI858nL0DhuH_1766816339530_na1fn_L2hvbWUvdWJ1bnR1L3JlbGF0b3Jpb190ZWNuaWNvX2Fzc2luYXR1cmFzX2RpZ2l0YWlz.md

# Relatório Técnico sobre Assinaturas Digitais

## 1. ECDSA (Elliptic Curve Digital Signature Algorithm)

### 1.1. Equações e Fórmulas (LaTeX)

- Geração da chave pública: `Q_A = d_A \times G`
- Hash da mensagem: `e = \text{HASH}(m)`
- Assinatura (r, s): `r = x_1 \pmod{n}`; `s = k^{-1}(z + r \cdot d_A) \pmod{n}`
- Verificação: `C = u_1 \times G + u_2 \times Q_A`
- Parâmetros de verificação: `u_1 = z \cdot s^{-1} \pmod{n}`; `u_2 = r \cdot s^{-1} \pmod{n}`

### 1.2. Variáveis e Parâmetros

- `CURVE`: O corpo e a equação da curva elíptica utilizada.
- `G`: Ponto base da curva elíptica, um ponto na curva que gera um subgrupo de ordem prima `n`.
- `n`: Ordem inteira de `G`, o que significa que `n \times G = O`, onde `O` é o elemento identidade.
- `d_A`: A chave privada (selecionada aleatoriamente).
- `Q_A`: A chave pública (`d_A \times G`).
- `m`: A mensagem a ser enviada.
- `e`: O hash da mensagem `m`.
- `z`: Os `L_n` bits mais à esquerda de `e`, onde `L_n` é o comprimento em bits da ordem do grupo `n`.
- `k`: Um inteiro aleatório criptograficamente seguro de `[1, n-1]`.
- `(r, s)`: A assinatura digital.
- `(x_1, y_1)`: As coordenadas do ponto da curva `k \times G`.
- `u_1`, `u_2`: Valores intermediários usados no algoritmo de verificação.
- `C`: O ponto da curva calculado durante a verificação.

### 1.3. Algoritmos

#### Geração de Assinatura

1. Calcule `e = HASH(m)`.
2. Seja `z` os `L_n` bits mais à esquerda de `e`.
3. Selecione um inteiro aleatório criptograficamente seguro `k` de `[1, n-1]`.
4. Calcule o ponto da curva `(x_1, y_1) = k \times G`.
5. Calcule `r = x_1 \pmod{n}`. Se `r = 0`, volte para o passo 3.
6. Calcule `s = k^{-1}(z + r \cdot d_A) \pmod{n}`. Se `s = 0`, volte para o passo 3.
7. A assinatura é o par `(r, s)`.

#### Verificação de Assinatura

1. Verifique se `r` e `s` são inteiros em `[1, n-1]`.
2. Calcule `e = HASH(m)`.
3. Seja `z` os `L_n` bits mais à esquerda de `e`.
4. Calcule `u_1 = z \cdot s^{-1} \pmod{n}`.
5. Calcule `u_2 = r \cdot s^{-1} \pmod{n}`.
6. Calcule o ponto da curva `C = u_1 \times G + u_2 \times Q_A`.
7. A assinatura é válida se `r \equiv x_C \pmod{n}`, onde `x_C` é a coordenada x de `C`.

### 1.4. Vulnerabilidades

- **Reutilização de `k`**: A reutilização do valor `k` para diferentes assinaturas com a mesma chave privada permite que um invasor calcule a chave privada.
- **Gerador de números aleatórios defeituoso**: Se `k` for gerado por um gerador de números aleatórios defeituoso, isso pode vazar informações sobre a chave privada.
- **Ataques de tempo**: Implementações que não são de tempo constante podem ser vulneráveis a ataques de tempo.
- **Backdoors em parâmetros de curva**: Preocupações foram levantadas sobre a possibilidade de backdoors nos parâmetros de curva elíptica publicados pelo NIST, que foram potencialmente influenciados pela NSA.

### 1.5. Conexões

- **Sony**: A reutilização de `k` foi explorada para extrair a chave de assinatura do console PlayStation 3.
- **Android Bitcoin Wallet**: Um gerador de números aleatórios defeituoso no Android causou a perda de fundos de usuários de carteiras Bitcoin em 2013.
- **OpenSSL**: Vulnerável a ataques de tempo em versões mais antigas.
- **NIST (National Institute of Standards and Technology)**: Publicou os padrões para curvas elípticas usadas no ECDSA.
- **NSA (National Security Agency)**: Suspeita de ter influenciado os padrões do NIST para incluir backdoors.

## 2. Assinaturas de Schnorr

### 2.1. Equações e Fórmulas (LaTeX)

- Geração da chave pública: `y = g^x`
- Assinatura (e, s): `e = H(g^k || M)`; `s = k + xe`
- Verificação: `r_v = g^s y^{-e}`

### 2.2. Variáveis e Parâmetros

- `G`: Um grupo de ordem prima `q` com gerador `g`.
- `H`: Uma função de hash criptográfica.
- `x`: A chave de assinatura privada.
- `y`: A chave de verificação pública.
- `M`: A mensagem a ser assinada.
- `k`: Um nonce aleatório.
- `r`: O compromisso (`g^k`).
- `e`: O desafio (`H(r || M)`).
- `s`: A resposta (`k + xe`).
- `(e, s)`: A assinatura.

### 2.3. Algoritmos

#### Geração de Chave

1. Escolha uma chave de assinatura privada `x`.
2. A chave de verificação pública é `y = g^x`.

#### Assinatura

1. Escolha um `k` aleatório.
2. Calcule `r = g^k`.
3. Calcule `e = H(r || M)`.
4. Calcule `s = k + xe`.
5. A assinatura é o par `(e, s)`.

#### Verificação

1. Calcule `r_v = g^s y^{-e}`.
2. Calcule `e_v = H(r_v || M)`.
3. Se `e_v = e`, a assinatura é verificada.

### 2.4. Vulnerabilidades

- **Reutilização de Nonce**: A reutilização do valor de nonce secreto `k` em duas assinaturas de mensagens diferentes permitirá que observadores recuperem a chave privada.
- **Nonces Tendenciosos**: Mesmo pequenas tendências no valor `k` ou vazamento parcial de `k` podem revelar a chave privada.

### 2.5. Conexões

- **Claus Schnorr**: Inventor do algoritmo.
- **Bitcoin**: Usa assinaturas de Schnorr para assinaturas de transações após a atualização Taproot.
- **DSA, ECDSA, ElGamal**: Algoritmos de assinatura intimamente relacionados.

## 3. Assinaturas BLS

### 3.1. Equações e Fórmulas (LaTeX)

- Geração de chave pública: `pk = sk \cdot g_2`
- Assinatura: `h = H(m)`; `\sigma = h^{sk}`
- Verificação: `e(\sigma, g_2) = e(H(m), pk)`

### 3.2. Variáveis e Parâmetros

- `e`: Um emparelhamento bilinear `e: G_1 \times G_2 \to G_T`.
- `G_1`, `G_2`: Grupos de curvas elípticas de ordem prima `q`.
- `g_2`: Um gerador de `G_2`.
- `H`: Uma função de hash do espaço de mensagens para `G_1`.
- `sk`: A chave secreta, um inteiro aleatório de `[0, q-1]`.
- `pk`: A chave pública, `sk \cdot g_2`.
- `m`: A mensagem.
- `h`: O hash da mensagem, `H(m)`.
- `\sigma`: A assinatura, `h^{sk}`.

### 3.3. Algoritmos

#### Geração de Chave

1. Selecione um inteiro aleatório `sk` de `[0, q-1]`.
2. A chave pública é `pk = sk \cdot g_2`.

#### Assinatura

1. Dada a chave secreta `sk` e uma mensagem `m`, calcule `h = H(m)`.
2. A assinatura é `\sigma = h^{sk}`.

#### Verificação

1. Dada uma assinatura `\sigma` para uma mensagem `m` e uma chave pública `pk`, verifique se `e(\sigma, g_2) = e(H(m), pk)`.

### 3.4. Vulnerabilidades

- A segurança depende da intratabilidade do problema Computacional Diffie-Hellman em um grupo Gap Diffie-Hellman.
- Ataques de cálculo de índice são possíveis no grupo alvo `G_T`.
- Não é seguro contra ataques quânticos.

### 3.5. Conexões

- **Dan Boneh, Ben Lynn e Hovav Shacham**: Inventores do esquema de assinatura BLS.
- **Chia Network, Ethereum, Skale, drand**: Usam assinaturas BLS.
- **Zcash**: A curva BLS12-381 foi projetada para o Zcash.
- **IETF**: Trabalhando em um padrão para assinaturas BLS.

## 4. Assinaturas Agregadas e Multisig

### 4.1. Assinaturas Agregadas

#### Equações e Fórmulas (LaTeX)

- Agregação Geral: `\sigma = \text{Aggregate}(\sigma_1, \sigma_2, ..., \sigma_k)`
- Verificação (BLS): `e(\sigma, g_2) = \prod_{i=1}^{k} e(H(m_i), pk_i)`

#### Variáveis e Parâmetros

- `\sigma_i`: Assinatura do usuário `i` na mensagem `m_i`.
- `\sigma`: A assinatura agregada.
- `m_i`: Mensagem assinada pelo usuário `i`.
- `pk_i`: Chave pública do usuário `i`.
- `k`: Número de assinaturas a serem agregadas.

#### Algoritmos

##### Agregação Geral

1. Cada usuário `i` cria a assinatura `\sigma_i` em sua mensagem `m_i`.
2. Qualquer pessoa pode executar o algoritmo de agregação pública para juntar todas as `k` assinaturas em uma única assinatura `\sigma`.

##### Agregação Sequencial

1. O usuário 1 assina `m_1` para obter `\sigma_1`.
2. O usuário 2 combina `\sigma_1` e `m_2` para obter `\sigma_2`.
3. O processo continua até que o usuário `k` gere a assinatura final `\sigma`.

#### Vulnerabilidades

- Um adversário não deve ser capaz de criar uma assinatura agregada válida por conta própria.
- A maioria das propostas requer uma ordem específica ao assinar uma mensagem.

### 4.2. Assinaturas Múltiplas (Multisig)

#### Equações e Fórmulas (LaTeX)

- Verificação (naïve): Requer a verificação de `n` assinaturas individuais com `n` chaves públicas.
- Chave Pública Agregada (MuSig): `P_{agg} = \sum_{i=1}^{n} P_i`
- Assinatura Agregada (MuSig): `s_{agg} = \sum_{i=1}^{n} s_i`

#### Variáveis e Parâmetros

- `n`: O número de participantes.
- `m`: O limite de assinaturas necessárias.
- `P_i`: Chave pública do participante `i`.
- `s_i`: Assinatura (ou compartilhamento de assinatura) do participante `i`.

#### Algoritmos

##### Multisig Ingênuo

1. Cada um dos `n` usuários tem um par de chaves pública/privada.
2. Uma assinatura válida é uma coleção de `n` assinaturas de `n` usuários.
3. A verificação requer o uso da chave pública de cada assinante para verificar a assinatura final.

##### MuSig (exemplo de otimização)

1. Os participantes combinam suas chaves públicas para criar uma única chave pública agregada.
2. Os participantes assinam a mensagem com suas chaves secretas e combinam as saídas em uma única assinatura.
3. A verificação é feita usando a chave pública agregada.

#### Vulnerabilidades

- **Ineficiência**: As transações multisig ingênuas são mais caras em termos de espaço e custos de processamento, que aumentam linearmente com `n`.
- **Complexidade**: A coordenação entre vários assinantes pode ser complexa.

### 4.3. Conexões

- **Dfinity, Algorand**: Usam o esquema BLS para agregar assinaturas na mesma mensagem (considerado um caso de multisig).
- **Taproot (Bitcoin)**: Usa MuSig para otimizar assinaturas multisig.
- **Rootstock (RSK)**: Pesquisando e comparando esses esquemas de assinatura.


---

## Relatório: 21_3s2AQXJSHr6okTF4C1RW3j_1766816284885_na1fn_L2hvbWUvdWJ1bnR1L3Byb29mX29mX3dvcmtfcmVwb3J0.md

# Relatório Técnico: Proof of Work

## Equações e Fórmulas

- `target = \frac{max\_target}{difficulty}`
- `H(s,x,c) / 2^{n-k} = 0`
- `target = coefficient \times 2^{8 \times (exponent - 3)}`

## Variáveis e Parâmetros

`ver`: Versão do formato Hashcash; `bits`: Número de bits zero no início do hash; `date`: Data e hora do envio da mensagem no formato YYMMDD[hhmm[ss]]; `resource`: String de dados do recurso que está sendo transmitido (ex: endereço de e-mail); `ext`: Extensão (opcional; ignorado na versão 1); `rand`: String de caracteres aleatórios, codificada em base-64; `counter`: Contador binário, codificado em base-64; `nonce`: Um número de 32 bits que os mineradores usam para tentar gerar um hash válido; `difficulty`: Uma medida de quão difícil é encontrar um hash abaixo do alvo; `target`: Um número de 256 bits que um hash de bloco deve ser menor ou igual; `max_target`: O valor máximo possível do alvo; `s`: String de serviço; `x`: Ponto de partida aleatório; `c`: Contador; `n`: Tamanho da saída do hash; `k`: Fator de trabalho; `coefficient`: Os 3 primeiros bytes do campo 'bits'; `exponent`: O último byte do campo 'bits'.

## Algoritmos

### Hashcash

O formato do cabeçalho do Hashcash é `ver:bits:date:resource:[ext]:rand:counter`. O algoritmo consiste em:

1.  Preparar um cabeçalho com os campos especificados.
2.  Computar o hash (originalmente SHA-1) do cabeçalho.
3.  Verificar se os primeiros `bits` do hash são zero. Se forem, a prova de trabalho é válida.
4.  Caso contrário, o campo `counter` é incrementado e o processo é repetido.

### Mineração de Bitcoin

1.  Construir um cabeçalho de bloco incluindo a versão do software, o hash do bloco anterior, a raiz de Merkle, o timestamp, o alvo de dificuldade (bits) e um nonce.
2.  Alterar repetidamente o nonce (e o extra nonce/timestamp, se necessário) e computar o hash duplo SHA-256 do cabeçalho do bloco.
3.  Se o hash resultante for menor ou igual ao alvo, o bloco é minerado com sucesso.
4.  O primeiro minerador a encontrar um hash válido transmite o bloco para a rede.

## Vulnerabilidades

- **Ataque de 51%:** Um atacante que controla mais de 50% da taxa de hash de mineração da rede pode potencialmente comprometer a integridade da blockchain.
- **Riscos Criptoanalíticos:** Embora atualmente considerado seguro para resistência a pré-imagem, futuros ataques criptoanalíticos às funções de hash subjacentes (SHA-256) podem introduzir vulnerabilidades.
- **Mineração Egoísta (Selfish Mining):** Uma estratégia de mineração onde um minerador ou um grupo de mineradores tenta obter mais receita mantendo seus blocos descobertos privados e apenas revelando-os em momentos estratégicos.

## Conexões

Adam Back, Hal Finney, Wei Dai, Nick Szabo, Microsoft, SpamAssassin, I2P, Mixmaster


---

## Relatório: 22_ePWbtizwh5XsprI48FNPiw_1766816267746_na1fn_L2hvbWUvdWJ1bnR1L3JlcG9ydA.md

# Relatório Técnico sobre Proof of Stake

## Equações e Fórmulas

- **Fórmula de Hash do Chain-based PoS:**
  ```latex
  Hash(ProposedNewBlock \|\| ClockTime) < target \times StakeValue
  ```

## Variáveis e Parâmetros

- **Hash:** A função de hash criptográfica.
- **ProposedNewBlock:** O novo bloco proposto.
- **ClockTime:** O tempo atual.
- **target:** Um valor alvo que determina a dificuldade.
- **StakeValue:** O valor do stake do validador.

## Algoritmos

- **Chain-based PoS:** Uma modificação do Proof of Work onde a dificuldade do quebra-cabeça varia com o stake.
- **Nominated PoS (NPoS):** Eleição de um comitê de validadores por meio de uma função aleatória verificável, com probabilidades ponderadas pelo stake. Usado em Ouroboros Praos e BABE.
- **BFT-based PoS:** Utiliza o consenso Byzantine Fault Tolerance para finalizar blocos. Requer que no máximo um terço dos validadores seja desonesto. Usado em Tendermint e Casper FFG.
- **Delegated Proof of Stake (DPoS):** Um sistema de duas etapas onde os detentores de stake elegem "testemunhas" para propor e votar em novos blocos. Usado em EOS, Lisk e Tron.
- **Liquid Proof of Stake (LPoS):** Permite que qualquer pessoa com stake se torne um validador, com a opção de delegação de votos. Usado em Tezos.
- **Ouroboros:** Uma família de protocolos de consenso PoS que inclui mini-protocolos para sincronização de cadeia, busca de blocos, submissão de transações, etc.
- **Casper:** Um protocolo de consenso PoS (chamado Zug) que oferece finalidade rápida e flexibilidade, apoiado por WebAssembly.

## Vulnerabilidades

- **Long-range attacks:** Ataques que substituem uma parte significativa da blockchain, viáveis devido ao baixo custo computacional.
- **Nothing at stake:** Validadores são incentivados a validar todos os forks da cadeia, o que pode levar a gastos duplos. A mitigação envolve penalidades.
- **Bribery attack:** Atacantes podem subornar validadores para aprovar um fork malicioso da blockchain.

## Conexões

- **Ouroboros:** Duncan Coutts (Well-Typed, IOHK), Neil Davies (PNSol, IOHK), Marc Fontaine (IOHK), Karl Knutsson (Cardano Foundation), Armando Santos (Well-Typed), Marcin Szamotulski (IOHK), Alex Vieth (Well-Typed).


---

## Relatório: 23_wMhZzfWSbCTjJ52yGHCvoV_1766816639653_na1fn_L2hvbWUvdWJ1bnR1L3JlcG9ydA.md


# Relatório Técnico sobre Mecanismos de Consenso de Blockchain

## Consenso de Nakamoto

### Equações e Fórmulas

*   Probabilidade de um atacante alcançar a cadeia honesta:
    $$ P_z = 1 - \sum_{k=0}^{z} \frac{\lambda^k e^{-\lambda}}{k!} (1 - (q/p)^{z-k}) $$

### Variáveis e Parâmetros

*   **p**: probabilidade de um nó honesto encontrar o próximo bloco
*   **q**: probabilidade de o atacante encontrar o próximo bloco
*   **z**: número de blocos que o atacante precisa alcançar
*   **λ**: z * (q/p)

### Algoritmos

1.  Novas transações são transmitidas para todos os nós.
2.  Cada nó coleta novas transações em um bloco.
3.  Cada nó trabalha para encontrar uma prova de trabalho (proof-of-work) para seu bloco.
4.  Quando um nó encontra uma prova de trabalho, ele transmite o bloco para todos os nós.
5.  Os nós aceitam o bloco somente se todas as transações nele forem válidas e ainda não tiverem sido gastas.
6.  Os nós expressam sua aceitação do bloco trabalhando na criação do próximo bloco da cadeia, usando o hash do bloco aceito como o hash anterior.

### Vulnerabilidades

*   **Ataque de 51%**: Se um atacante controlar mais de 50% do poder de mineração da rede, ele poderá criar uma cadeia de blocos paralela que se tornará a mais longa, permitindo o gasto duplo de moedas.
*   **Ataque de egoísmo (Selfish Mining)**: Um minerador pode tentar manter seus blocos recém-minerados em segredo, liberando-os apenas quando a cadeia principal se aproxima de sua própria cadeia, com o objetivo de obter uma vantagem competitiva.

### Conexões

*   **Satoshi Nakamoto**: Pseudônimo do criador do Bitcoin e do conceito de Consenso de Nakamoto.

---

## Byzantine Fault Tolerance (BFT)

### Equações e Fórmulas

*   Número mínimo de réplicas para tolerar `f` falhas bizantinas: `n >= 3f + 1`

### Variáveis e Parâmetros

*   **n**: número total de réplicas no sistema
*   **f**: número máximo de réplicas bizantinas (defeituosas)

### Algoritmos

*   **Practical Byzantine Fault Tolerance (PBFT)**: Um algoritmo de replicação de máquina de estados que tolera falhas bizantinas em sistemas assíncronos.
    1.  Um cliente envia uma solicitação ao nó líder.
    2.  O líder transmite a solicitação para os nós de backup.
    3.  Os nós de backup executam a solicitação e enviam uma resposta ao cliente.
    4.  O cliente aguarda `f + 1` respostas idênticas de diferentes nós de backup.

### Vulnerabilidades

*   **Ataques de Desempenho**: Um líder malicioso pode degradar o desempenho do sistema, por exemplo, ignorando seletivamente as solicitações.
*   **Ataques de Temporização**: Um adversário pode explorar as temporizações da rede para comprometer a segurança do sistema.

### Conexões

*   **Leslie Lamport, Robert Shostak, and Marshall Pease**: Autores do artigo original que descreve o Problema dos Generais Bizantinos.
*   **Barbara Liskov and Miguel Castro**: Desenvolvedores do algoritmo Practical Byzantine Fault Tolerance (PBFT).

---

## Practical Byzantine Fault Tolerance (PBFT)

### Equações e Fórmulas

*   Número mínimo de réplicas para tolerar `f` falhas bizantinas: `n >= 3f + 1`

### Variáveis e Parâmetros

*   **n**: número total de réplicas no sistema
*   **f**: número máximo de réplicas bizantinas (defeituosas)
*   **view**: um número que identifica o líder atual.
*   **request**: uma solicitação de um cliente para o serviço.
*   **pre-prepare**: uma mensagem enviada pelo líder para os backups para iniciar o processo de consenso.
*   **prepare**: uma mensagem enviada pelos backups para confirmar que eles concordam com a ordem da solicitação.
*   **commit**: uma mensagem enviada pelos backups para confirmar que eles processaram a solicitação.

### Algoritmos

O PBFT é um algoritmo de consenso que tolera falhas bizantinas em sistemas distribuídos. O algoritmo funciona em "views", onde cada view tem um líder. O processo de consenso para uma solicitação de cliente é o seguinte:

1.  Um cliente envia uma solicitação ao nó líder.
2.  O líder multicasta a solicitação para os nós de backup em uma mensagem `pre-prepare`.
3.  Os backups recebem a mensagem `pre-prepare` e, se concordarem com ela, enviam uma mensagem `prepare` para todos os outros nós.
4.  Um nó espera por `2f` mensagens `prepare` de outros nós que correspondam à mensagem `pre-prepare`. Se o fizer, envia uma mensagem `commit` para todos os outros nós.
5.  Um nó espera por `2f + 1` mensagens `commit`. Se o fizer, ele executa a solicitação e envia uma resposta ao cliente.

### Vulnerabilidades

*   **Desempenho**: O PBFT tem uma complexidade de comunicação de O(n^2), o que pode ser um gargalo em redes grandes.
*   **Líder Malicioso**: Um líder malicioso pode retardar o sistema ao não enviar mensagens `pre-prepare` ou ao enviar mensagens diferentes para nós diferentes.

### Conexões

*   **Barbara Liskov e Miguel Castro**: Desenvolvedores do algoritmo Practical Byzantine Fault Tolerance (PBFT).

---

## Tendermint

### Equações e Fórmulas

*   A tolerância a falhas bizantinas do Tendermint é baseada na premissa de que o número de nós bizantinos é menor que 1/3 do total de nós. A fórmula para o número de nós necessários para tolerar `f` falhas é: `n > 3f`

### Variáveis e Parâmetros

*   **n**: número total de validadores no sistema.
*   **f**: número máximo de validadores bizantinos (defeituosos).
*   **height**: altura do bloco na cadeia.
*   **round**: rodada de consenso para uma determinada altura.
*   **pre-vote**: primeira fase de votação no algoritmo de consenso.
*   **pre-commit**: segunda fase de votação no algoritmo de consenso.
*   **polka**: quando mais de 2/3 dos validadores pré-votam no mesmo bloco.

### Algoritmos

O consenso Tendermint é um protocolo de consenso BFT (Byzantine Fault Tolerant) baseado em proof-of-stake. O processo de consenso ocorre em rodadas e consiste em três etapas:

1.  **Propose**: Um validador é escolhido para propor um novo bloco. A seleção do proponente é determinística e rotativa.
2.  **Prevote**: Os validadores votam no bloco proposto. Se um validador recebe um bloco válido do proponente atual, ele transmite um `prevote` para o bloco.
3.  **Precommit**: Se um validador recebe mais de 2/3 de `prevotes` para um bloco, ele transmite um `precommit` para esse bloco. Se um validador recebe mais de 2/3 de `precommits`, ele considera o bloco como confirmado.

### Vulnerabilidades

*   **Ataque de 1/3**: Se mais de 1/3 dos validadores forem maliciosos, eles podem interromper o consenso ou causar uma bifurcação na cadeia.
*   **Ataque de Long Range**: Um atacante com uma pequena quantidade de poder de voto pode tentar criar uma cadeia longa a partir de um bloco antigo. No entanto, o Tendermint tem mecanismos para mitigar esse tipo de ataque.

### Conexões

*   **Jae Kwon**: Criador do Tendermint.
*   **Cosmos Network**: Uma rede de blockchains que utiliza o Tendermint como seu mecanismo de consenso.
*   **Interchain Foundation**: Uma organização sem fins lucrativos que apoia o desenvolvimento do ecossistema Cosmos, incluindo o Tendermint.

---

## Raft

### Equações e Fórmulas

O Raft não possui equações complexas como o Consenso de Nakamoto. As principais regras são baseadas em lógica e contagem de votos.

### Variáveis e Parâmetros

*   **termo**: período de tempo no qual um líder é eleito.
*   **líder**: nó responsável por gerenciar o log replicado.
*   **seguidor**: nó que segue as instruções do líder.
*   **candidato**: nó que está concorrendo para se tornar o líder.
*   **log**: sequência de comandos que são replicados entre os nós.

### Algoritmos

O Raft funciona através da eleição de um líder que é responsável por gerenciar o log replicado. O algoritmo é dividido em três subproblemas:

1.  **Eleição de Líder**: Um líder é eleito para um determinado termo. Se o líder falhar, um novo líder é eleito para um novo termo.
2.  **Replicação de Log**: O líder recebe comandos dos clientes e os adiciona ao seu log. Em seguida, ele envia os comandos para os seguidores para que eles também os adicionem aos seus logs.
3.  **Segurança**: O Raft garante que, se qualquer servidor aplicou uma entrada de log em um determinado índice, nenhum outro servidor aplicará uma entrada diferente para o mesmo índice.

### Vulnerabilidades

*   **Particionamento de Rede**: Se um líder for particionado da maioria dos seguidores, ele não poderá confirmar novas entradas de log. No entanto, o sistema permanecerá disponível se a maioria dos servidores puder se comunicar.
*   **Nós Lentos**: Seguidores lentos podem atrasar a confirmação de entradas de log, pois o líder precisa esperar que a maioria dos seguidores replique a entrada.

### Conexões

*   **Diego Ongaro e John Ousterhout**: Criadores do algoritmo de consenso Raft.
*   **etcd**: Um armazenamento de chave-valor distribuído que usa o Raft para consenso.
*   **Consul**: Uma ferramenta para descoberta de serviços e configuração que usa o Raft.


---

## Relatório: 24_74XHrSPP0hCnF8gMcBlHud_1766816531713_na1fn_L2hvbWUvdWJ1bnR1L3JlcG9ydC90ZWNobmljYWxfcmVwb3J0.md

# Relatório Técnico sobre Bitcoin Script

**Assunto:** Bitcoin Script - linguagem de script, OP_CODES, P2PKH, P2SH, SegWit



## Algoritmos

**Pay-to-PubKey-Hash (P2PKH)**

*   **scriptPubKey:** `OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG`
*   **scriptSig:** `<sig> <pubKey>`

**Processo de Execução:**

1.  O `scriptSig` e o `scriptPubKey` são combinados.
2.  `<sig>` e `<pubKey>` são empurrados para a pilha.
3.  `OP_DUP` duplica o `<pubKey>` no topo da pilha.
4.  `OP_HASH160` calcula o hash do `<pubKey>` duplicado.
5.  O `<pubKeyHash>` do `scriptPubKey` é empurrado para a pilha.
6.  `OP_EQUALVERIFY` verifica se os dois hashes são iguais. Se não forem, a transação falha.
7.  `OP_CHECKSIG` verifica a assinatura da transação usando a `<pubKey>` e a `<sig>`.

---

**Pay-to-Script-Hash (P2SH)**

*   **scriptPubKey:** `OP_HASH160 <scriptHash> OP_EQUAL`
*   **scriptSig:** `<sig> <pubKey> <redeemScript>`

**Processo de Execução:**

1.  O `scriptSig` e o `scriptPubKey` são combinados.
2.  O `<redeemScript>` é verificado para garantir que corresponde ao `<scriptHash>`.
3.  O `<redeemScript>` é então executado.

---

**Pay-to-Witness-PubKey-Hash (P2WPKH)**

*   **Locking Script:** `0 <pubKeyHash>` (na saída da transação)
*   **Unlocking Script (Witness):** `<sig> <pubKey>`

**Pay-to-Witness-Script-Hash (P2WSH)**

*   **Locking Script:** `0 <scriptHash>` (na saída da transação)
*   **Unlocking Script (Witness):** `<sig> <pubKey> <redeemScript>`

---


## Equações e Fórmulas

```latex
5 + 9 = 14
```

```latex
y^2 \equiv x^3 + ax + b \pmod{p}
```


## Variáveis e Parâmetros

*   **scriptPubKey:** O script que bloqueia a saída da transação.
*   **scriptSig:** O script que desbloqueia a saída da transação.
*   **pubKey:** Chave Pública.
*   **pubKeyHash:** O hash de uma chave pública.
*   **sig:** Assinatura.
*   **redeemScript:** Um script que é revelado e executado posteriormente.
*   **nLockTime:** Um campo na transação que especifica o tempo mais antigo em que a transação pode ser adicionada a um bloco válido.
*   **nSequence:** Um campo em cada entrada de uma transação que pode ser usado para tempo de bloqueio relativo.
*   **witness:** Uma nova seção nas transações SegWit que contém o código de desbloqueio.
*   **wTXID:** O ID da transação de testemunha, que inclui os dados da testemunha.


## Vulnerabilidades

*   **Maleabilidade de Transação (Transaction Malleability):** Antes do SegWit, era possível para um terceiro alterar o ID de uma transação antes de ser confirmada, o que poderia levar a problemas de dupla despesa.
*   **OP_LSHIFT Crash (CVE-2010-5137):** Uma vulnerabilidade no opcode OP_LSHIFT que poderia causar o travamento de um nó Bitcoin.
*   **Gastos não autorizados (CVE-2010-5141):** Uma falha que permitia que um invasor gastasse moedas que não possuía.


## Conexões

*   **Governo dos EUA:** O governo dos EUA é o maior detentor estatal conhecido de bitcoin, com uma política para manter o bitcoin como um ativo de reserva nacional.
*   **NSA:** O algoritmo de hash SHA-256, usado no Bitcoin, foi projetado pela NSA.


---

## Relatório: 25_6Ie4lwMxtYUqPwa718pDpv_1766816365649_na1fn_L2hvbWUvdWJ1bnR1L2xpZ2h0bmluZ19yZXNlYXJjaC9yZXBvcnQ.md

# Relatório Técnico: Lightning Network

## Equações e Fórmulas

- **HTLC Script:** `OP_IF OP_HASH160 <Hash160(R)> OP_EQUALVERIFY 2 <Alice2> <Bob2> OP_CHECKMULTISIG OP_ELSE 2 <Alice1> <Bob1> OP_CHECKMULTISIG OP_ENDIF`

## Variáveis e Parâmetros

- **R:** um dado de entrada aleatório de 20 bytes (pré-imagem)
- **H:** o hash de R
- **P:** chaves públicas
- **K:** chaves privadas correspondentes
- **C:** Transação de Compromisso
- **RD:** Transação de Entrega Revogável
- **BR:** Transação de Remédio de Violação
- **HED:** Transação de Entrega de Execução de HTLC
- **HT:** Transação de Tempo Limite de HTLC
- **HTRD:** Transação de Entrega Revogável de Tempo Limite de HTLC
- **HERD:** Transação de Entrega Revogável de Execução de HTLC
- **nLockTime:** um parâmetro de transação que especifica o tempo mais antigo em que uma transação pode ser adicionada a um bloco
- **RSMC:** Contrato de Vencimento de Sequência Revogável

## Algoritmos

- **Hashed Timelock Contract (HTLC):** Um contrato que permite que uma transação seja gasta se o destinatário puder fornecer a pré-imagem de um hash. Se a pré-imagem não for fornecida dentro de um determinado período de tempo, os fundos serão devolvidos ao remetente.
- **Revocable Sequence Maturity Contract (RSMC):** Um contrato que invalida transações antigas. Se uma parte transmitir uma transação antiga, a outra parte pode reivindicar todos os fundos no canal. Isso é feito através de uma transação de penalidade (Breach Remedy transaction).
- **Roteamento de Pagamentos (Payment Routing):** O roteamento é feito através de uma rede de canais de pagamento. O remetente encontra uma rota para o destinatário e cria HTLCs ao longo do caminho. Cada salto na rota tem um timelock decrescente. O destinatário resgata o pagamento revelando o segredo R, que então se propaga de volta ao remetente, permitindo que cada intermediário reivindique seus fundos.

## Vulnerabilidades

- Ataque de 51% através do sistema de revogação
- Ataque de negação de serviço (DDoS)
- Problemas de roteamento e liquidez
- Necessidade de watchtowers (serviços de terceiros) para monitorar fundos
- Bugs que podem causar perda de fundos (CVE-2019-12998, CVE-2019-12999, CVE-2019-13000)
- Ataques que podem retardar ou parar pagamentos
- Ataques de congestionamento
- Centralização crescente
- Ataque Flood & Loot
- Ataques de saída em massa (Mass Exit Attacks)
- Ataque de griefing
- Vulnerabilidade de jamming de retransmissão de transação (Transaction-Relay Jamming)
- Ataque de ciclo de substituição (Replacement Cycling Attack)
- Ataque Zumbi (Zombie Attack)
- Ataque de gasto duplo em massa (Mass Double-Spend Attack)
- Ataque de dilatação do tempo (Time-Dilation Attack)

## Conexões

- Joseph Poon
- Thaddeus Dryja
- Alex Akselrod
- Peter Todd
- Elizabeth Stark
- Rusty Russell


---

## Relatório: 26_H1IlKyt8WxaonSKQzX1SDT_1766817289110_na1fn_L2hvbWUvdWJ1bnR1L3prcF9yZXNlYXJjaC90ZWNobmljYWxfcmVwb3J0.md

# Relatório Técnico sobre Provas de Conhecimento Zero

Este relatório detalha os aspectos técnicos de vários protocolos de prova de conhecimento zero, incluindo zk-SNARKs, zk-STARKs, Groth16, Plonk e Bulletproofs.



## zk-SNARKs

# zk-SNARKs - Technical Details



## Equations and Definitions

* **Definition 2.1 (The Class NP):** A language L is in the class NP if there exists a polynomial time algorithm R_L such that L = {x | ∃w, |w| = poly(|x|) ∧ R_L(x, w) = 1}.


## Definições e Equações Chave

### Protocolo Sigma (Definition 3.1)
Um protocolo Σ para uma linguagem L é uma prova de conhecimento de zero-conhecimento de verificador honesto de moeda pública, com uma estrutura particular de três movimentos:
1.  **Fase de Compromisso:** P envia a V alguns valores de compromisso para alguma aleatoriedade.
2.  **Fase de Desafio:** V envia a P um desafio aleatório uniforme `e`.
3.  **Fase de Resposta:** P envia a V uma resposta `f(w, r, e)` onde `f` é alguma função pública, e `w` é a testemunha mantida por P.

### Sistema de Argumento (Definition 5.1)
Um argumento não interativo para uma relação R é uma quádrupla de algoritmos polinomiais probabilísticos Π = (G, P, Ver, Sim) tal que:
*   `(crs, vrs, td) ← G(1^λ, R)`: O algoritmo de geração de CRS recebe como entrada um parâmetro de segurança λ, uma relação R e produz uma string de referência comum (CRS) e uma trapdoor (td).
*   `π ← P(crs, u, w)`: O algoritmo do provador recebe como entrada o crs, uma declaração u e uma testemunha w. Ele produz um argumento π.
*   `b ← Ver(crs, u, π)`: O algoritmo do verificador recebe como entrada uma declaração u juntamente com um argumento π e o crs.

### zk-SNARK (Definition 5.2)
Um argumento não interativo para R, Π = (G, P, Ver, Sim), é um zk-SNARK se satisfizer:
*   **Completude:** Para toda declaração verdadeira para a relação R, um provador honesto P com uma testemunha válida deve convencer o verificador Ver. Formalmente, para todo λ ∈ N e para todo (u, w) ∈ R:
    `Pr[Ver(crs, u, P(crs, u, w)) = 1 | (crs, td) ← G(1^λ, R)] = 1`
*   **Conhecimento-Solidez (Knowledge-Soundness):** Não é possível para o provador construir uma prova sem conhecer uma testemunha.
*   **Zero-Conhecimento:** A prova não revela nada além da veracidade da declaração.

### Programa Aritmético Quadrático (QAP - Definition 7.2)
Um Programa Aritmético Quadrático Q sobre o corpo F contém três conjuntos de m + 1 polinômios V = {vi(x)}, W = {wi(x)} e Y = {yi(x)}, i ∈ {0, 1 . . . m} e um polinômio alvo t(x). (c1, ..., cN) ∈ FN é uma atribuição válida das entradas e saídas de F, se e somente se existirem coeficientes (cN+1, ..., cm) tais que t(x) divide p(x), onde:
`p(x) = (Σ_{i=0 to m} c_i * v_i(x)) * (Σ_{i=0 to m} c_i * w_i(x)) - (Σ_{i=0 to m} c_i * y_i(x))`

### Programa de Vão Quadrado (SSP - Definition 7.3)
Um Programa de Vão Quadrado (SSP) S sobre o corpo F é uma tupla que consiste em m + 1 polinômios v0(x), ..., vm(x) ∈ F[x] e um polinômio alvo t(x). Diz-se que o SSP aceita uma entrada c1, ..., cN ∈ {0, 1} se e somente se existirem cN+1, ..., cm ∈ {0, 1} tais que t(x) divide p(x), onde:
`p(x) = (Σ_{i=1 to m} c_i * v_i(x))^2 - v_0(x)`


## zk-STARKs

# zk-STARKs - Technical Details



## Definições e Equações Chave

### Integridade Computacional (Definition 3.1)
A relação binária R_CI é o conjunto de pares (x, w) onde:
*   x = (M, x, y, T, S) com M uma Máquina de Turing não determinística, x e y denotam entrada e saída, e T ≥ S são inteiros em notação binária, indicando limites de tempo e espaço, respectivamente.
*   w é uma descrição das escolhas não determinísticas de M na entrada x que a fazem alcançar a saída y em ≤ T passos, usando uma fita de memória de tamanho no máximo S.

### Prova de Oráculo Interativa (IOP - Definition 3.2)
Um sistema de Prova de Oráculo Interativa (IOP) S para uma relação R com erro de solidez ε ∈ [0, 1] é um par de algoritmos aleatórios interativos S = (P, V) que satisfazem as seguintes propriedades:
*   **Operação:** A entrada do verificador é x, e a entrada do provador é (x, w) para alguma string w. O número de rodadas interativas, denotado r(x), é chamado de complexidade de rodada do sistema.
*   **Completude:** Se (x, w) ∈ R, então o verificador V sempre aceita após interagir com P na entrada comum x e na entrada privada w.
*   **Solidez:** Se x ∉ L_R, então para qualquer provador P*, a probabilidade de que V aceite após interagir com P* na entrada comum x é no máximo ε.

### IOP de Conhecimento Escalável e Transparente (STIK - Definition 3.3)
Seja R uma relação binária induzida por uma linguagem não determinística L ∈ NTIME(T(n)) para T(n) ≥ n e seja S = (P, V) um IOP para L com erro de solidez ε(n) < 1. Dizemos que S é:
*   **Transparente:** se todas as mensagens e consultas do verificador são moedas aleatórias públicas.
*   **(Totalmente, ou duplamente) escalável:** se para cada instância x de comprimento n, ambos os seguintes se mantêm:
    1.  **Verificador escalável:** t_v(n) = poly(n, log T(n), log 1/ε(n))
    2.  **Provador escalável:** t_p(n) = poly(n, T(n), log 1/ε(n))
*   **Prova de Conhecimento (POK):** se existe um extrator de oráculo esperado de tempo polinomial E tal que para qualquer provador P*, se P* convence V a aceitar com probabilidade δ > ε, então E, dado acesso de oráculo a P*, extrai uma testemunha w para x em tempo esperado poly(n, 1/(δ-ε)).

### Representação Intermediária Algébrica (AIR - Definition B.3)
A relação R_AIR é o conjunto de pares (x, w) = (x_AIR, w_AIR) que satisfazem:
1.  **Formato da Instância:** a instância x é uma tupla x = (F, T, w, P, C, B) onde F é um corpo finito, T é um limite de tempo, w é a largura do estado, P é um conjunto de polinômios de restrição de transição, C é um conjunto de polinômios de restrição de fronteira e B é um conjunto de pares (i, α) que especificam as restrições de fronteira.
2.  **Formato da Testemunha:** a testemunha w é uma função w: {0, ..., T-1} x {1, ..., w} → F, que representa o traço de execução.

### Representação Intermediária Algébrica Binária (BAIR - Definition B.5)
Uma instância de AIR binária (BAIR) é uma instância de AIR x = (F, T, w, P, C, B) que satisfaz para alguns n, t, d ∈ N+ (i) |F| = 2^n; (ii) T = 2^t - 1; e (iii) deg(C) ≤ 2^d.


## Groth16

# Groth16 - Technical Details



## Algoritmo Groth16

O protocolo Groth16 consiste em três algoritmos: Setup, Prove e Verify.

### Setup
O algoritmo de configuração gera os parâmetros públicos (CRS - Common Reference String) e a trapdoor de simulação.

`Setup(R)`: Escolha α, β, γ, δ, x ← F*. Defina τ = (α, β, γ, δ, x) e calcule σ.

### Prove
O provador usa o CRS e sua testemunha para gerar uma prova.

`Prove(R, σ, a1, ..., am)`: Escolha r, s ← F e calcule a prova π = (A, B, C) onde:

*   `A = α + Σ_{i=0 to m} a_i u_i(x) + rδ`
*   `B = β + Σ_{i=0 to m} a_i v_i(x) + sδ`
*   `C = (Σ_{i=l+1 to m} a_i(βu_i(x) + αv_i(x) + w_i(x)) + h(x)t(x)) / δ + As + rB - rsδ`

### Verify
O verificador usa os parâmetros públicos, a declaração e a prova para verificar a validade da prova.

`Vfy(R, σ, a1, ..., a_l)`: Verifica a seguinte equação de emparelhamento:

`e(A, B) = e(α, β) * e(Σ_{i=1 to l} a_i u_i(x), γ) * e(C, δ)`


## Plonk

# Plonk - Technical Details



## Algoritmo Plonk

O Plonk é um protocolo de prova de conhecimento zero que usa um esquema de compromisso de polinômio para verificar a validade de uma computação. A computação é primeiro convertida em um circuito aritmético, que é então representado como um conjunto de equações polinomiais.

### Aritmetização

A equação principal que descreve as restrições do circuito é:

`q_L(X)a(X) + q_R(X)b(X) + q_O(X)c(X) + q_M(X)a(X)b(X) + q_C(X) = 0`

Onde:
*   `a(X)`, `b(X)`, `c(X)` são polinômios que representam os valores dos fios de entrada e saída das portas do circuito.
*   `q_L(X)`, `q_R(X)`, `q_O(X)`, `q_M(X)`, `q_C(X)` são polinômios seletores que são pré-processados e definem a estrutura do circuito.

### Argumento de Permutação

Para garantir que os fios que conectam diferentes portas tenham o mesmo valor (restrições de cópia), o Plonk usa um argumento de permutação. Este argumento prova que um conjunto de valores é uma permutação de outro conjunto de valores. Isso é feito através de um "grande argumento de produto", que envolve a construção de um polinômio acumulador `Z(X)` que satisfaz certas relações em um subgrupo multiplicativo do corpo.

O argumento de permutação verifica a seguinte identidade:

`Z(gX) * (f'(X) + βS_ID(X) + γ) = Z(X) * (g'(X) + βS_σ(X) + γ)`

Onde:
*   `f'` e `g'` são os polinômios que contêm os valores a serem verificados.
*   `S_ID` e `S_σ` são polinômios que representam a permutação.
*   `β` e `γ` são desafios aleatórios do verificador.
*   `Z(X)` é o polinômio acumulador.


## Bulletproofs

# Bulletproofs - Technical Details



## Algoritmo Bulletproofs

Bulletproofs são provas de conhecimento zero curtas e não interativas que não requerem uma configuração confiável. Elas são particularmente eficientes para provas de intervalo (range proofs).

### Prova de Produto Interno (Inner Product Proof)

O núcleo do Bulletproofs é um argumento de produto interno eficiente. O objetivo é provar que o produto interno de dois vetores `a` e `b` é igual a `c`, ou seja, `<a, b> = c`, sem revelar os vetores.

A prova é construída recursivamente. Em cada passo, o tamanho do problema é reduzido pela metade. O provador envia `L` e `R` (elementos de grupo) ao verificador, que responde com um desafio `x`. Os novos vetores e geradores são calculados da seguinte forma:

*   `a\' = a_L * x + a_R * x^{-1}`
*   `b\' = b_L * x^{-1} + b_R * x`
*   `g\' = g_L * x^{-1} + g_R * x`
*   `h\' = h_L * x + h_R * x^{-1}`

O novo compromisso `P\'` é calculado como `P\' = L * x^2 + R * x^{-2} + P`.

### Prova de Intervalo (Range Proof)

Para provar que um valor `v` está no intervalo `[0, 2^n - 1]`, o provador representa `v` em binário como `a_L` e prova que cada bit é 0 ou 1. Isso é feito mostrando que `a_L ◦ (a_L - 1^n) = 0^n` e `a_R = a_L - 1^n`.

As restrições são combinadas em uma única equação de produto interno usando desafios aleatórios `y` e `z` do verificador:

`<a_L - z*1^n, y^n ◦ (a_R + z*1^n) + z^2*2^n> = δ(y, z)`

Onde `δ(y, z)` é um termo de correção. Esta equação de produto interno é então provada usando o argumento de produto interno.

### Provas para Circuitos Aritméticos

Bulletproofs também podem ser usados para provar a satisfatibilidade de circuitos aritméticos. As restrições do circuito são convertidas em um conjunto de equações polinomiais. O provador compromete-se com os polinômios que representam os valores dos fios e, em seguida, usa o argumento de produto interno para provar que as equações são satisfeitas em um ponto aleatório.

As restrições do circuito são da forma:

`w_L ◦ w_R = w_O`
`W_L * a_L + W_R * a_R + W_O * a_O = W_V * v + c`

Onde `W_L`, `W_R`, `W_O`, `W_V` são matrizes que definem o circuito. Essas restrições são combinadas em uma única equação polinomial usando desafios aleatórios.
## Vulnerabilidades

### Circuitos Sub-restringidos e Não-Determinísticos
- **Descrição:** A falta de restrições suficientes em um circuito ZK permite que um provador malicioso gere provas falsas. Por exemplo, se um circuito não impõe que os fatores de um número sejam positivos, um provador pode usar fatores negativos para gerar uma prova válida para um produto incorreto.
- **Exemplo:** Um circuito que verifica `val <== factorOne * factorTwo` sem verificar se `factorOne` e `factorTwo` são diferentes de 1, positivos e se o produto está dentro da ordem do corpo escalar.
- **Impacto:** Geração de provas falsas, quebra da solidez do sistema.

### Overflows/Underflows Aritméticos
- **Descrição:** As operações em corpos finitos podem resultar em overflows (resultados maiores que o módulo) ou underflows (resultados menores que zero), levando a resultados inesperados se não forem tratadas corretamente.
- **Exemplo:** Em um esquema de retirada, se `withdrawAmount > currentBalance`, o resultado `newBalance` pode sofrer um underflow e se tornar um número muito grande, permitindo que o usuário retire mais fundos do que possui.
- **Impacto:** Comportamento inesperado do circuito, possibilidade de double-spending ou retirada de fundos indevidos.

### Comprimentos de Bits Incompatíveis
- **Descrição:** Se um circuito não verificar o comprimento de bits das entradas, um atacante pode fornecer entradas com comprimentos de bits diferentes para causar um underflow e manipular o resultado de comparações.
- **Exemplo:** Em um circuito `LessThan(n)`, um atacante pode fornecer `in[0]` com `n` bits e `in[1]` com mais de `n` bits, fazendo com que a verificação `in[0] < in[1]` falhe mesmo que seja verdadeira.
- **Impacto:** Manipulação de comparações e lógica do circuito.

### Maleabilidade da Prova (Groth16)
- **Descrição:** A maleabilidade permite que um adversário modifique uma prova válida para criar outra prova válida para uma declaração relacionada, mas diferente. No Groth16, isso pode ser feito deslocando os elementos da prova por múltiplos de `δ`.
- **Exemplo:** Dado uma prova `(A, B, C)`, um atacante pode criar uma nova prova `(A', B', C')` onde `A' = A + r_A*δ`, `B' = B + r_B*δ`, `C' = C + r_C*δ`.
- **Impacto:** Possibilidade de ataques de repetição ou criação de provas para declarações não intencionais.

### Ataque do Último Desafio (Fiat-Shamir)
- **Descrição:** A transformação de Fiat-Shamir, usada para tornar os protocolos interativos não interativos, pode ser uma fonte de vulnerabilidades se não for implementada corretamente. Um atacante pode ser capaz de escolher o último desafio para quebrar a solidez da prova.
- **Impacto:** Quebra da solidez do sistema de prova.


## Conexões Institucionais

- **zk-SNARKs:** A pesquisa inicial sobre zk-SNARKs foi conduzida por pesquisadores do **MIT** e do **Technion - Israel Institute of Technology**. Alessandro Chiesa, um dos co-autores do artigo que cunhou o termo zk-SNARK, é professor na **UC Berkeley**.
- **zk-STARKs:** Eli Ben-Sasson, um dos criadores do zk-STARKs, é professor no **Technion - Israel Institute of Technology**. A StarkWare, empresa que desenvolve e promove a tecnologia STARK, foi co-fundada por ele.
- **Groth16:** Jens Groth é Cientista Chefe na **Nexus** e Professor Honorário de Criptologia na **University College London (UCL)**. Ele também tem afiliação com a **DFINITY**.
- **Plonk:** Ariel Gabizon, Zachary J. Williamson e Oana Ciobotaru são os autores do artigo do Plonk. Suas afiliações incluem **Aztec** e **Pi Squared**.
- **Bulletproofs:** Os autores do artigo Bulletproofs têm afiliações com a **Stanford University**, **University College London (UCL)** e **Blockstream**.

Não foram encontradas conexões diretas com agências governamentais como NSA ou GCHQ na pesquisa realizada.


---

## Relatório: 27_vtkGNjhQt9InmxdNPL9sjB_1766816788952_na1fn_L2hvbWUvdWJ1bnR1L3JlcG9ydA.md

# Relatório Técnico sobre Criptografia Homomórfica



## Criptossistema Paillier

### Equações

- Cifragem: $E(m) = g^m r^n \mod n^2$
- Propriedade Homomórfica: $E(m_1) \cdot E(m_2) = g^{m_1+m_2} (r_1 r_2)^n \mod n^2 = E(m_1+m_2)$

### Variáveis

- `n`: módulo, chave pública
- `g`: base, chave pública
- `m`: mensagem
- `r`: número aleatório em {0, ..., n-1}


## Vulnerabilidades e Ataques

- Ataques de força bruta ao SVSSP (Sparse Vector Subset Sum Problem).
- Ataques de redução de reticulado contra knapsacks de baixa densidade.
- Ataques de canal lateral (Side-channel attacks).
- Ataques de criptoanálise a Polly Cracker.
- Ataques em reticulados de ideais circulantes com bases ortonormais.
- Ataques de subcampo em variantes do NTRU.



## Algoritmos de Criptografia Totalmente Homomórfica (FHE)

### Esquema de Gentry (Baseado em Reticulados Ideais)

O esquema original de Gentry é construído a partir de um esquema de criptografia de alguma forma homomórfico (somewhat homomorphic) que é "bootstrappable".

- **KeyGen**: Gera um par de chaves (pk, sk) para o esquema de criptografia de alguma forma homomórfico.
- **Encrypt(pk, µ)**: Criptografa uma mensagem µ usando a chave pública pk.
- **Decrypt(sk, c)**: Descriptografa um texto cifrado c usando a chave secreta sk.
- **Evaluate(pk, C, c1, ..., ct)**: Avalia um circuito C em textos cifrados.
- **Recrypt(pk, c)**: "Refresca" um texto cifrado c, reduzindo o ruído acumulado. Este é o passo de bootstrapping.


## Conexões Institucionais

- **NSA (Agência de Segurança Nacional dos EUA)**: Demonstrou interesse em criptografia homomórfica para proteger dados de usuários em pesquisas na internet e no acesso a informações sensíveis. A NSA também publicou o "Commercial National Security Algorithm Suite 2.0", que inclui a criptografia homomórfica como uma tecnologia de interesse.
- **GCHQ (Sede de Comunicações do Governo do Reino Unido)**: Publicou um "conto de advertência" sobre a segurança de implementações de criptografia baseada em reticulado, que são a base para muitos esquemas FHE. O NCSC (Centro Nacional de Segurança Cibernética), parte do GCHQ, também lista a criptografia homomórfica como uma área de pesquisa em criptografia avançada.
- **MI5**: O serviço de segurança do Reino Unido mencionou o desenvolvimento de Criptografia Totalmente Homomórfica como uma tecnologia importante para a segurança nacional.
- **Consórcio de Padronização de Criptografia Homomórfica**: Um grupo da indústria formado por pesquisadores da IBM, Microsoft, Intel, NIST e outros, com o objetivo de padronizar a criptografia homomórfica.
- **Startups e Corporações**: Várias startups e grandes empresas de tecnologia estão desenvolvendo e aplicando a criptografia homomórfica, incluindo Enveil, Decentriq, SemioticLabs, Inpher, Duality Technologies, CryptoLab e Niobium Microsystems.




---

## Relatório: 28_kJdgOLHZs8szWSlnpLLK8f_1766816439790_na1fn_L2hvbWUvdWJ1bnR1L3JlcG9ydA.md

# Relatório Técnico: Ring Signatures, Monero e CryptoNote

## Equações e Fórmulas

```latex
P = H_s(rA)G + B; P = xG; x = H_s(rA) + b; I = xH_p(P); c_{i+1} = H_s(m, L_i, R_i); L_i = s_iG + c_iP_i; R_i = s_iH_p(P_i) + c_iI; s_i = \alpha - c_ix_i \pmod{l}
```

## Variáveis e Parâmetros

*   **q**: um número primo, q = 2^255 − 19
*   **d**: um elemento de Fq, d = −121665/121666
*   **E**: uma equação de curva elíptica, −x^2 + y^2 = 1 + dx^2y^2
*   **G**: um ponto base, G = (x,−4/5)
*   **l**: uma ordem prima do ponto base, l = 2^252 + 27742317777372353535851937790883648493
*   **Hs**: uma função de hash criptográfica {0,1}∗ → Fq
*   **Hp**: uma função de hash determinística E(Fq) → E(Fq)
*   **a**: chave privada ec, um número a ∈ [1,l − 1]
*   **A**: chave pública ec, um ponto A = aG
*   **(a,b)**: chave de usuário privada, um par de duas chaves privadas ec diferentes
*   **(a,B)**: chave de rastreamento, um par de chave privada e pública ec (onde B = bG e a != b)
*   **(A,B)**: chave de usuário pública, um par de duas chaves públicas ec derivadas de (a,b)
*   **P**: chave pública de uso único
*   **x**: a chave privada correspondente a P
*   **r**: um número aleatório escolhido pelo remetente
*   **I**: imagem da chave
*   **m**: a mensagem sendo assinada
*   **Pi**: chaves públicas dos membros do anel
*   **s**: a assinatura
*   **c, s**: parâmetros de assinatura
*   **xi**: a chave privada do signatário

## Algoritmos

**Geração de chave pública de uso único**: O remetente calcula a chave pública de uso único P para o destinatário usando a fórmula `P = Hs(rA)G + B`, onde `r` é um número aleatório, `A` é a parte pública da chave do destinatário, `G` é o ponto base da curva elíptica e `B` é a outra parte pública da chave do destinatário.

**Recuperação de chave privada**: O destinatário pode calcular a chave privada `x` correspondente a `P` usando a fórmula `x = Hs(rA) + b`, onde `b` é a chave privada do destinatário.

**Geração de imagem de chave**: A imagem da chave `I` é calculada como `I = xHp(P)`, onde `Hp` é uma função de hash que mapeia pontos da curva elíptica para outros pontos da curva elíptica.

**Geração de assinatura em anel**: O signatário real usa sua chave privada `xi` para assinar uma mensagem `m` em nome de um anel de `n` participantes. O processo envolve a geração de valores aleatórios e o cálculo de uma série de valores `c` e `s` para cada participante, de modo que a equação de verificação seja satisfeita.

**Verificação de assinatura em anel**: Um verificador pode confirmar que a assinatura foi gerada por um membro do anel sem saber qual deles. A verificação envolve o uso das chaves públicas de todos os membros do anel, da imagem da chave e da mensagem para recalcular uma série de valores e garantir que eles correspondam aos valores na assinatura.

## Vulnerabilidades

*   **Ataque de criação infinita de moedas**: Uma vulnerabilidade crítica descoberta no protocolo CryptoNote permitia a criação de um número ilimitado de moedas. Esta falha foi corrigida no Monero.
*   **Rastreabilidade de transações**: Análises empíricas mostraram que as blockchains no estilo CryptoNote são vulneráveis a ataques de desanonimização, comprometendo a irrastreabilidade das transações.
*   **Ataques de exposição de chave**: Alguns esquemas de assinatura em anel são vulneráveis a ataques de exposição de chave, onde a chave privada de um usuário pode ser comprometida.
*   **Ataques de negação de serviço**: Uma vulnerabilidade no CryptoNote versão 0.8.9 permitia que atacantes remotos causassem uma negação de serviço.

## Conexões

Nenhuma conexão direta com governos, corporações ou agências de inteligência foi encontrada durante a pesquisa. O desenvolvimento do CryptoNote e do Monero parece ser impulsionado pela comunidade de código aberto, com foco na privacidade e no anonimato.


---

## Relatório: 29_HR4Svmy8DrYLIngMYFQW4b_1766816372030_na1fn_L2hvbWUvdWJ1bnR1L3RlY2huaWNhbF9yZXBvcnQ.md

# Relatório Técnico: Confidential Transactions

## Equações e Fórmulas

- **Compromisso de Pedersen:** `C(v, r) = r*G + v*H`
- **Imagem da Chave (Key Image):** `I = x * H_p(P)`
- **Assinatura LSAG (Linkable Spontaneous Anonymous Group):**
  - `L_j = α * G`
  - `R_j = α * H_p(P_j)`
  - `c_{j+1} = h(m, L_j, R_j)`
  - `L_{j+1} = s_{j+1} * G + c_{j+1} * P_{j+1}`
  - `R_{j+1} = s_{j+1} * H_p(P_{j+1}) + c_{j+1} * I`
  - `s_j = α - c_j * x mod l`
- **Assinatura MLSAG (Multilayered Linkable Spontaneous Anonymous Group):**
  - `I_j = x_j * H_p(P_j)`
  - `L_j_π = α_j * G`
  - `R_j_π = α_j * H_p(P_j_π)`
  - `c_{π+1} = H(m, L_1_π, R_1_π, ..., L_m_π, R_m_π)`
  - `L_j_{i} = s_j_i * G + c_i * P_j_i`
  - `R_j_{i} = s_j_i * H_p(P_j_i) + c_i * I_j`
  - `s_j_π = α_j - c_π * x_j mod l`

## Variáveis e Parâmetros

- `C`: Compromisso de Pedersen
- `v`: Valor/montante da transação
- `r`: Fator de cegueira (blinding factor)
- `G`, `H`: Pontos geradores em uma curva elíptica
- `I`: Imagem da chave (key image)
- `x`: Chave privada
- `P`: Chave pública
- `H_p`: Função de hash que retorna um ponto na curva
- `m`: Mensagem
- `α`, `s`: Escalares aleatórios
- `c`: Saída da função de hash
- `l`: Ordem do grupo da curva elíptica
- `L`, `R`: Valores intermediários no esquema de assinatura
- `MLSAG`: Assinatura de Grupo Anônima Espontânea Linkable Multilayered
- `π`: Índice secreto do assinante

## Algoritmos

- **Esquema de Compromisso de Pedersen:** Um esquema de compromisso que permite que uma parte se comprometa com um valor, mantendo-o oculto, com a capacidade de revelá-lo posteriormente. É homomórfico aditivamente.
- **Assinaturas de Anel (LSAG e MLSAG):** Um tipo de assinatura digital que pode ser realizada por qualquer membro de um grupo de usuários que possuam chaves. Uma mensagem assinada com uma assinatura de anel é endossada por alguém em um grupo específico de pessoas, sem revelar qual membro a assinou. A variante MLSAG permite a assinatura de vetores de chaves.
- **Provas de Alcance (Range Proofs):** Um tipo de prova de conhecimento zero que demonstra que um valor comprometido está dentro de um intervalo específico (por exemplo, [0, 2^n]), sem revelar o valor em si. O artigo menciona "Aggregate Schnorr Range Proofs" como um método para isso.

## Vulnerabilidades

- **Análise de blockchain baseada em valores:** Um adversário pode restringir o possível remetente procurando por transações com valores específicos.
- **Conjunto de anonimato menor para valores menos comuns:** Para valores de transação menos comuns, o conjunto de anonimato é menor, tornando mais fácil a identificação do remetente.
- **Criação de transações "poeira" (dust):** A ofuscação do valor enviado pode criar um grande número de transações de pequeno valor, que podem ser rastreadas.
- **Gasto duplo (Double-spending):** O artigo descreve como as assinaturas de anel linkáveis (linkable ring signatures) previnem essa vulnerabilidade através do uso de imagens de chave (key images).
- **Aquisição da chave mestra em configuração confiável (trusted setup):** O artigo menciona que o Ring CT é imune a isso, ao contrário de protocolos como o Zerocash, pois a geração de moedas é feita por prova de trabalho (proof-of-work).

## Conexões

- **Shen Noether:** Monero Research Labs
- **Gregory Maxwell:** Bitcoin Core Developer
- **CryptoNote:** Protocolo original no qual o Monero foi baseado
- **Zerocash:** Outro protocolo de aprimoramento de privacidade mencionado para comparação
- **Adam Back:** Proponente da modificação das assinaturas LSAG para maior eficiência


---

## Relatório: 2_rYfsQDNg0QUYqG1fD6uTZ4_1766816441081_na1fn_L2hvbWUvdWJ1bnR1L3JlcG9ydA.md

# Relatório Técnico: Martin Hellman e o Protocolo Diffie-Hellman

## Equações e Fórmulas

```latex
Y = \alpha^X \mod q;X = \log_{\alpha} Y \mod q;K_{ij} = Y_i^{X_j} \mod q;K_{ij} = (\alpha^{X_i})^{X_j} \mod q;K_{ij} = Y_j^{X_i} \mod q;K_{ij} = (\alpha^{X_j})^{X_i} \mod q;Y_i = \alpha^{X_i} \mod q;K_{ij} = \alpha^{X_i X_j} \mod q;f(X) = S_K(P_0);f(X) = P_0;
```

## Variáveis e Parâmetros

*   **q:** um número primo
*   **alpha:** uma raiz primitiva de q
*   **X:** a chave privada de um usuário, um inteiro entre 1 e q-1
*   **Y:** a chave pública de um usuário
*   **Kij:** a chave secreta compartilhada entre os usuários i e j
*   **f(X):** uma função de mão única
*   **SK:** uma função de cifragem
*   **P0:** um texto plano padrão
*   **C:** um texto cifrado

## Algoritmos

### Protocolo de troca de chaves Diffie-Hellman

1.  Dois usuários, i e j, concordam publicamente com um número primo q e uma raiz primitiva alpha.
2.  O usuário i gera uma chave privada aleatória Xi e calcula sua chave pública Yi = alpha^Xi mod q.
3.  O usuário j gera uma chave privada aleatória Xj e calcula sua chave pública Yj = alpha^Xj mod q.
4.  Os usuários trocam suas chaves públicas.
5.  O usuário i calcula a chave secreta compartilhada Kij = Yj^Xi mod q.
6.  O usuário j calcula a chave secreta compartilhada Kij = Yi^Xj mod q.

Ambas as chaves são idênticas, pois Kij = (alpha^Xj)^Xi mod q = (alpha^Xi)^Xj mod q = alpha^(Xi*Xj) mod q.

### Criptosistema de chave pública usando uma função de mão única

1.  Um usuário A deseja enviar uma mensagem segura para um usuário B.
2.  O usuário B possui uma chave de decifragem secreta D e uma chave de cifragem pública E.
3.  O usuário A obtém a chave pública E de B e a utiliza para cifrar a mensagem M, resultando no texto cifrado C = E(M).
4.  O usuário B utiliza sua chave secreta D para decifrar a mensagem: M = D(C) = D(E(M)).

## Vulnerabilidades

*   **Vulnerabilidade a ataques man-in-the-middle:** um invasor pode interceptar as chaves públicas e substituí-las por suas próprias, enganando as duas partes para que estabeleçam chaves secretas com o invasor em vez de uma com a outra. A autenticação das chaves públicas é necessária para evitar este ataque.
*   **A segurança do protocolo depende da dificuldade computacional de calcular logaritmos discretos.** Se um algoritmo eficiente para calcular logaritmos discretos for descoberto, o protocolo será quebrado.
*   **O protocolo não fornece autenticação por si só.** As identidades das partes não são verificadas, tornando-o vulnerável a ataques de representação se não for usado em conjunto com um mecanismo de autenticação.
*   **Ataque Logjam:** um invasor man-in-the-middle pode forçar uma conexão TLS a usar criptografia de nível de exportação de 512 bits, permitindo que o invasor leia e modifique os dados. Isso se due a uma falha no protocolo TLS, e não a uma vulnerabilidade de implementação.
*   **Ameaças de adversários de nível estatal:** Muitos servidores usam os mesmos números primos para a troca de chaves Diffie-Hellman. Um invasor com recursos suficientes (como um estado-nação) pode realizar um cálculo de pré-computação caro no número primo. Depois que essa pré-computação é concluída, o invasor pode quebrar rapidamente as chaves de sessão individuais que usam esse primo.

## Conexões

*   Whitfield Diffie, Stanford University
*   Martin E. Hellman, Stanford University
*   Ralph Merkle
*   National Science Foundation
*   IEEE Information Theory Group


---

## Relatório: 30_9M1lG527GCbPsFpmKG4Q7W_1766816541360_na1fn_L2hvbWUvdWJ1bnR1L21pbWJsZXdpbWJsZV9yZXBvcnQ.md

# Relatório Técnico: MimbleWimble

## 1. Equações e Fórmulas (Notação LaTeX)

- **Adição de Ponto em Curva Elíptica:**
  ```latex
  xG := G + ... + G
  ```

- **Problema do Logaritmo Discreto:**
  ```latex
  H = xG
  ```

- **Geração de Chave Pública:**
  ```latex
  X = xG
  ```

- **Compromisso de Pedersen:**
  ```latex
  C := vH + rG
  ```

- **Propriedade Homomórfica dos Compromissos de Pedersen:**
  ```latex
  Com(v1; r1) + Com(v2; r2) = Com(v1 + v2; r1 + r2)
  ```

- **Balanceamento de Transação (Soma Zero):**
  ```latex
  \Sigma{Out} - \Sigma{In} = 0
  ```

- **Balanceamento de Compromisso:**
  ```latex
  \Sigma{C_{out}} - \Sigma{C_{in}} = (\Sigma{v_{out}} - \Sigma{v_{in}})H + (\Sigma{r_{out}} - \Sigma{r_{in}})G
  ```

- **Kernel de Transação Mimblewimble (Excesso de Kernel):**
  ```latex
  \Sigma{C_{out}} - \Sigma{C_{in}} = 0H + xG
  ```

- **Equação com Kernel Offset:**
  ```latex
  sum(outputs) - sum(inputs) = sum(kernel_excess) + kernel_offset*G
  ```

## 2. Variáveis e Parâmetros

| Variável | Definição |
|---|---|
| `G` | Ponto gerador em uma curva elíptica. |
| `H` | Outro ponto gerador na mesma curva elíptica, cujo logaritmo discreto em relação a `G` é desconhecido. |
| `x` | Uma chave secreta (escalar). |
| `X` | Uma chave pública (ponto na curva), calculada como `xG`. |
| `v` | O valor de uma entrada ou saída de transação (um escalar). |
| `r` | O fator de cegueira, um valor aleatório secreto usado para ofuscar o valor `v`. |
| `C` | Um compromisso de Pedersen com um valor `v`, calculado como `vH + rG`. |
| `\pi` | Uma prova de intervalo (range proof), que demonstra que um valor comprometido está em um intervalo específico (e.g., não é negativo) sem revelar o valor. |
| `\sigma` | Uma assinatura criptográfica. |
| `kernel_offset` | Um fator de cegueira adicional aplicado ao kernel da transação para prevenir o "problema do subconjunto". |

## 3. Algoritmos e Protocolos

### Compromissos de Pedersen
Um esquema de compromisso criptográfico que permite a um provador se comprometer com um valor para um verificador, mantendo-o oculto. O esquema é aditivamente homomórfico, o que significa que a soma de dois compromissos é um compromisso para a soma dos valores. No MimbleWimble, isso é usado para verificar que a soma das saídas de uma transação é igual à soma das entradas, sem revelar os valores reais.

### Transações Confidenciais (CT)
Proposto por Gregory Maxwell, este protocolo utiliza compromissos de Pedersen e provas de intervalo para ocultar os valores das transações em uma blockchain. O MimbleWimble baseia-se fortemente neste conceito para alcançar a confidencialidade dos valores.

### CoinJoin
Um mecanismo de anonimização que combina múltiplas transações de diferentes remetentes em uma única transação, tornando mais difícil para um observador externo determinar o fluxo exato dos fundos. O MimbleWimble implementa uma forma não interativa de CoinJoin no nível do bloco.

### Cut-through
Este é um mecanismo de compactação de blockchain central para o MimbleWimble. Quando uma saída é criada e subsequentemente gasta dentro do mesmo bloco (ou em blocos diferentes), tanto a saída quanto a entrada que a gasta podem ser removidas da cadeia sem comprometer a segurança. Isso ocorre porque suas contribuições para a equação de soma zero se anulam. O resultado é que o estado da cadeia consiste apenas nos cabeçalhos dos blocos, nos kernels das transações e no conjunto de saídas não gastas (UTXOs), reduzindo drasticamente o tamanho da blockchain.

### Kernel Offsets
Para mitigar o "problema do subconjunto", onde um adversário poderia reconstruir as transações individuais dentro de um bloco agregado, o MimbleWimble introduz um *kernel offset*. Este é um valor secreto adicional incluído em cada kernel de transação. Ao agregar transações em um bloco, os offsets individuais são somados em um único offset agregado para o bloco inteiro, tornando impossível desvendar as transações originais.

## 4. Vulnerabilidades e Fraquezas Conhecidas

- **Replicabilidade de Transações (Proposta Original):** A proposta inicial do MimbleWimble continha uma falha onde o destinatário de uma transação poderia descobrir a chave secreta do excesso do remetente, permitindo-lhe potencialmente reverter ou modificar a transação. Implementações como Grin e Beam abordaram isso com esquemas de construção de transação interativos ou não interativos aprimorados.

- **Ataque de Vinculação (Linkability Attack):** Uma vulnerabilidade fundamental demonstrada por Ivan Bogatyy. Um adversário pode executar um "supernó" que se conecta a uma grande fração dos nós da rede para interceptar transações antes da fase de agregação (cut-through). Ao observar a propagação das transações (mesmo com o protocolo Dandelion), o atacante pode vincular as entradas às saídas com alta probabilidade (96% na rede Grin durante o teste), quebrando o anonimato do gráfico de transações, embora os valores permaneçam confidenciais. Esta vulnerabilidade é considerada inerente ao design do MimbleWimble.

## 5. Conexões Institucionais e Colaboradores

| Nome/Entidade | Conexão/Contribuição |
|---|---|
| Tom Elvis Jedusor | Pseudônimo do criador anônimo do whitepaper original do MimbleWimble. |
| Gregory Maxwell | Criptógrafo cujas ideias, como Transações Confidenciais e CoinJoin, formam a base do MimbleWimble. |
| Andrew Poelstra | Criptógrafo e pesquisador da Blockstream que desenvolveu e formalizou muitos dos conceitos do MimbleWimble. |
| Georg Fuchsbauer | Pesquisador (Inria, ENS) que co-autorou uma investigação criptográfica formal do MimbleWimble. |
| Michele Orru` | Pesquisador (Inria, ENS) que co-autorou a investigação criptográfica formal. |
| Yannick Seurin | Pesquisador (Inria, ENS) que co-autorou a investigação criptográfica formal. |
| Ivan Bogatyy | Pesquisador (Dragonfly Research) que demonstrou o ataque de vinculação prático contra o MimbleWimble. |
| Grin | Implementação de código aberto e orientada pela comunidade do protocolo MimbleWimble, escrita em Rust. |
| Beam | Implementação do MimbleWimble com foco em usabilidade e governança, escrita em C++. |
| Tari | Uma plataforma de ativos digitais construída como uma camada de mesclagem-mineração no topo do Monero, que utiliza o MimbleWimble. |
| Litecoin | Criptomoeda que explorou e implementou o MimbleWimble como uma funcionalidade opcional através de Blocos de Extensão (Extension Blocks). |
| Dragonfly Research | Empresa de investimento e pesquisa em criptoativos, onde Ivan Bogatyy publicou sua pesquisa. |


---

## Relatório: 31_0QP4Rp4qkn1uYtjvTfOuO7_1766816900118_na1fn_L2hvbWUvdWJ1bnR1L3RlY2huaWNhbF9yZXBvcnQ.md


# Relatório Técnico: Ethereum Smart Contracts

## Ethereum Virtual Machine (EVM)

### Equações e Fórmulas

*   **Função de Transição de Estado:** `Y(S, T) = S'`

### Variáveis e Parâmetros

*   `S`: O estado antigo válido.
*   `T`: Um novo conjunto de transações válidas.
*   `S'`: O novo estado de saída válido.
*   **Profundidade da Pilha (Stack):** 1024 itens
*   **Tamanho da Palavra (Word Size):** 256-bit

### Algoritmos e Protocolos

*   **Estrutura de Dados de Estado:** Trie Merkle Patricia Modificada
*   **Memória Transiente:** Array de bytes endereçado por palavra, não persiste entre transações.
*   **Armazenamento Transiente:** Armazenamento de chave-valor por transação, acessado pelos opcodes `TSTORE` e `TLOAD`. Persiste em chamadas internas na mesma transação, mas é limpo no final da transação.
*   **Armazenamento Persistente:** Trie de armazenamento Merkle Patricia associada à conta, parte do estado global.

### Opcodes

*   **Operações de Pilha Padrão:** `XOR`, `AND`, `ADD`, `SUB`
*   **Operações Específicas da Blockchain:** `ADDRESS`, `BALANCE`, `BLOCKHASH`
*   **Opcodes de Armazenamento Transiente:** `TSTORE`, `TLOAD`

## Solidity

### Tipos de Valor

*   **Booleans (`bool`):** `true` ou `false`.
*   **Integers (`int`/`uint`):** Inteiros com e sem sinal de vários tamanhos de 8 a 256 bits. `uint` e `int` são aliases para `uint256` e `int256`.
*   **Números de Ponto Fixo (`fixed`/`ufixed`):** Números de ponto fixo com e sem sinal de vários tamanhos. Ainda não totalmente suportado.
*   **Address:** Contém um valor de 20 bytes (tamanho de um endereço Ethereum).
*   **Tipos de Contrato:** Um tipo de contrato pode ser explicitamente convertido de e para o tipo `address`.
*   **Arrays de bytes de tamanho fixo:** `bytes1`, `bytes2`, `bytes3`, ..., `bytes32`.
*   **Literais:** Literais de inteiros e strings.
*   **Enums:** Tipos enumerados definidos pelo usuário.

### Tipos de Referência

*   **Arrays:** Um array de tamanho fixo em tempo de compilação ou de tamanho dinâmico.
*   **Structs:** Tipos definidos pelo usuário que podem agrupar várias variáveis.
*   **Mappings:** Tabelas de hash que mapeiam chaves para valores.

### Operadores

*   **Comparações:** `<=`, `<`, `==`, `!=`, `>=`, `>`
*   **Operadores de bit:** `&`, `|`, `^`, `~`
*   **Operadores de deslocamento:** `<<`, `>>`
*   **Operadores aritméticos:** `+`, `-`, unário `-`, `*`, `/`, `%`, `**`

## Gas

### Fórmulas

*   **Taxa Total de Gás:** `Unidades de Gás (Limite) * (Taxa Base + Taxa de Prioridade)`
*   **Ajuste da Taxa Base:** A taxa base aumenta ou diminui em no máximo 12,5% por bloco se o tamanho do bloco anterior estiver acima ou abaixo do tamanho alvo, respectivamente.

### Variáveis e Parâmetros

*   **Limite de Gás:** A quantidade máxima de gás que um usuário está disposto a consumir em uma transação.
*   **Preço do Gás:** O preço por unidade de gás.
*   **Taxa Base:** O preço mínimo por unidade de gás definido pelo protocolo para que uma transação seja incluída em um bloco.
*   **Taxa de Prioridade (Gorjeta):** Uma taxa adicional paga aos validadores para incentivá-los a incluir a transação em um bloco.
*   **Unidades de Gás:** A quantidade total de gás usada em uma transação.
*   **Tamanho Alvo:** Metade do limite de gás para um bloco.

## Contribuições Técnicas de Vitalik Buterin

### Fórmulas de "A matemática de quando o estágio 1 e o estágio 2 fazem sentido"

*   **Probabilidade de Falha do Estágio 0:** `∑𝑖=4^7 (7𝑖) * 0.1^𝑖 * 0.9^(7−𝑖) = 0.002728`
*   **Probabilidade de Falha do Estágio 1 (Falha no Sistema de Prova):** `∑𝑖=3^8 (8𝑖) * 0.1^𝑖 * 0.9^(8−𝑖) = 0.03809179`
*   **Probabilidade de Falha do Estágio 1 (Falha no Conselho de Segurança):** `∑𝑖=6^8 (8𝑖) * 0.1^𝑖 * 0.9^(8−𝑖) = 0.00002341`

## Vulnerabilidades de Contratos Inteligentes (OWASP Top 10 2025)

*   **SC01: Vulnerabilidades de Controle de Acesso:** Falhas que permitem que usuários não autorizados acessem ou modifiquem os dados ou funções de um contrato.
*   **SC02: Manipulação de Oráculo de Preços:** Exploração de vulnerabilidades na forma como os contratos inteligentes buscam dados externos.
*   **SC03: Erros de Lógica:** O comportamento do contrato se desvia de sua funcionalidade pretendida.
*   **SC04: Falta de Validação de Entrada:** A validação de entrada insuficiente pode levar à manipulação do contrato.
*   **SC05: Ataques de Reentrância:** Exploração da capacidade de reentrar em uma função vulnerável antes que sua execução seja concluída.
*   **SC06: Chamadas Externas Não Verificadas:** Falha na verificação do sucesso de chamadas de funções externas.
*   **SC07: Ataques de Empréstimo Flash:** Exploração de empréstimos flash para manipular protocolos.
*   **SC08: Overflow e Underflow de Inteiros:** Erros aritméticos devido à superação dos limites de inteiros de tamanho fixo.
*   **SC09: Aleatoriedade Insegura:** Aleatoriedade previsível ou manipulável.
*   **SC10: Ataques de Negação de Serviço (DoS):** Esgotamento dos recursos do contrato, tornando-o não funcional.

## Conexões Institucionais

### Membros da Enterprise Ethereum Alliance (EEA)

Adhara Ltd., Arche Capital, Applied Blockchain, BlockApps, Inc., Blockchain Digital Capital LTD, Blockchain for Social Impact Coalition, Chainlink, ConsenSys AG, Coti Foundation, Chainsecurity, dsrv labs Co., Ltd., Emertech Innovations Pvt Ltd, ENS Labs Ltd., Ernst & Young, Ethereum Foundation, Etherealize, ERC3643, Franklin, Gaia, Gateway.fm, Hacken, JP Morgan Chase Bank, Kaleido, kpk, Keyring, Linux Foundation Decentralized Trust, L2beat, Lido, Microsoft, Olympix, Plume Network, Public Works, Polygon, The Graph, Validation Cloud, Wanchain


---

## Relatório: 32_ODpAEQj5ne1F3ph8WwSPo4_1766816788305_na1fn_L2hvbWUvdWJ1bnR1L2ZpbmFsX3JlcG9ydA.md



## MD5 Technical Report

### Equations

*   **F(X,Y,Z) = (X AND Y) OR (NOT(X) AND Z)**
*   **G(X,Y,Z) = (X AND Z) OR (Y AND NOT(Z))**
*   **H(X,Y,Z) = X XOR Y XOR Z**
*   **I(X,Y,Z) = Y XOR (X OR NOT(Z))**
*   **a = b + ((a + F(b,c,d) + X[k] + T[i]) <<< s)**

### Variables

*   **A, B, C, D:** Four 32-bit registers that form the MD buffer.
*   **M[0...N-1]:** The message to be hashed, divided into 16-word (512-bit) blocks.
*   **T[1...64]:** A 64-element table of constants constructed from the sine function. T[i] is the integer part of 4294967296 * abs(sin(i)).
*   **b:** The length of the original message in bits.
*   **X[k]:** The k-th 32-bit word of the current message block.
*   **s:** The number of bits to circularly shift left.

### Algorithm

1.  **Append Padding Bits:** A single '1' bit is appended to the message, followed by '0' bits until the message length is congruent to 448, modulo 512.
2.  **Append Length:** A 64-bit representation of the original message length 'b' is appended to the padded message.
3.  **Initialize MD Buffer:** The four registers (A, B, C, D) are initialized with specific hexadecimal values.
4.  **Process Message in 16-Word Blocks:** The core of the algorithm, which consists of four rounds of 16 operations each. Each operation involves one of the auxiliary functions (F, G, H, I), a message word, a constant from the T table, and a left circular shift.
5.  **Output:** The final message digest is the concatenation of the values in the four registers (A, B, C, D).

### Connections

*   **Author:** Ronald L. Rivest (MIT Laboratory for Computer Science and RSA Data Security, Inc.)
*   **Contributors:** Don Coppersmith, Burt Kaliski, Ralph Merkle, David Chaum, Noam Nisan.

### Vulnerabilities

*   **Collision Attacks:** It is computationally feasible for an attacker to generate two different inputs that produce the same MD5 hash. This weakness was first described in 1996 and practically demonstrated in 2004.
*   **Forged Certificates:** The collision vulnerability allows attackers to create fraudulent X.509 certificates. In 2008, researchers created a rogue Certificate Authority (CA) certificate by exploiting this flaw.
*   **Not Suitable for Cryptographic Use:** Due to these vulnerabilities, MD5 is considered cryptographically broken and should not be used for any security-related purposes, such as digital signatures or password storage.
## SHA-1 Technical Report

### Equations

*   **f(t;B,C,D) = (B AND C) OR ((NOT B) AND D)** (0 <= t <= 19)
*   **f(t;B,C,D) = B XOR C XOR D** (20 <= t <= 39 and 60 <= t <= 79)
*   **f(t;B,C,D) = (B AND C) OR (B AND D) OR (C AND D)** (40 <= t <= 59)
*   **W(t) = S^1(W(t-3) XOR W(t-8) XOR W(t-14) XOR W(t-16))**
*   **TEMP = S^5(A) + f(t;B,C,D) + E + W(t) + K(t)**

### Variables

*   **A, B, C, D, E:** Five 32-bit words that form the buffer.
*   **H0, H1, H2, H3, H4:** Five 32-bit words that form the message digest.
*   **W(0...79):** A sequence of eighty 32-bit words.
*   **K(t):** A sequence of constant words for each step 't'.
*   **l:** The length of the original message in bits.

### Algorithm

1.  **Padding:** Append a '1' bit, followed by '0' bits, and finally a 64-bit integer representing the original message length, to make the total length a multiple of 512.
2.  **Initialization:** Initialize the five H registers with specific hexadecimal values.
3.  **Processing:** For each 512-bit message block:
    a.  Divide the block into 16 words (W(0) to W(15)).
    b.  Extend the 16 words to 80 words using the specified formula.
    c.  Initialize the A, B, C, D, E buffer with the current H values.
    d.  Perform 80 rounds of computation, updating the buffer words in each round.
    e.  Update the H registers by adding the final buffer values.
4.  **Output:** The final message digest is the concatenation of the five H registers.

### Connections

*   **Source:** US Federal Information Processing Standard (FIPS) 180-1.
*   **Based on:** MD4 by Ronald L. Rivest (MIT).
*   **Acknowledgments:** Tony Hansen, Garrett Wollman.
## SHA-2 Technical Report

### Equations (SHA-256)

*   **Ch(E,F,G) = (E AND F) XOR (NOT E AND G)**
*   **Maj(A,B,C) = (A AND B) XOR (A AND C) XOR (B AND C)**
*   **Σ0(A) = (A >>> 2) XOR (A >>> 13) XOR (A >>> 22)**
*   **Σ1(E) = (E >>> 6) XOR (E >>> 11) XOR (E >>> 25)**
*   **σ0(w[i-15]) = (w[i-15] >>> 7) XOR (w[i-15] >>> 18) XOR (w[i-15] >> 3)**
*   **σ1(w[i-2]) = (w[i-2] >>> 17) XOR (w[i-2] >>> 19) XOR (w[i-2] >> 10)**

### Variables (SHA-256)

*   **a, b, c, d, e, f, g, h:** Eight 32-bit working variables.
*   **h0-h7:** Eight 32-bit hash values.
*   **k[0-63]:** 64 round constants.
*   **w[0-63]:** 64-word message schedule array.

### Algorithm (SHA-256)

1.  **Initialize hash values:** The eight hash values (h0-h7) are initialized with the first 32 bits of the fractional parts of the square roots of the first eight prime numbers.
2.  **Initialize round constants:** The 64 round constants (k[0-63]) are initialized with the first 32 bits of the fractional parts of the cube roots of the first 64 prime numbers.
3.  **Padding:** The message is padded to be a multiple of 512 bits.
4.  **Process message in 512-bit chunks:**
    a.  The message is broken into 512-bit chunks.
    b.  A 64-entry message schedule array (w[0-63]) is created.
    c.  The working variables are initialized with the current hash values.
    d.  A compression function main loop is executed for 64 rounds.
    e.  The compressed chunk is added to the current hash value.
5.  **Final hash value:** The final hash value is the concatenation of the eight hash values.

### Connections

*   **Designers:** National Security Agency (NSA)
*   **Certification:** FIPS PUB 180-4, CRYPTREC, NESSIE
## SHA-3 and Keccak Technical Report

### Equations (Keccak-f[1600])

*   **θ step:** C[x] = A[x,0] xor A[x,1] xor A[x,2] xor A[x,3] xor A[x,4]; D[x] = C[x-1] xor rot(C[x+1],1)
*   **ρ step:** a[i,j] = rot(a[i,j], (t+1)(t+2)/2) for t from 0 to 23
*   **π step:** A'[x,y] = A[x',y'] where x' = y and y' = (2x + 3y) mod 5
*   **χ step:** A[x,y] = A[x,y] xor ((not A[x+1,y]) and A[x+2,y])
*   **ι step:** A[0,0] = A[0,0] xor RC[i_r]

### Variables

*   **A:** State array (5x5x64 bits)
*   **C, D:** Intermediate variables for the θ step
*   **RC:** Round constants
*   **r:** Rate (size of the part of the state that is written and read)
*   **c:** Capacity (size of the part of the state that is untouched by input/output)
*   **b:** Width of the permutation (b = r + c = 1600 bits)

### Algorithm (Sponge Construction)

1.  **Padding:** The input message is padded using the `pad10*1` rule to a length divisible by the rate `r`.
2.  **Absorbing phase:** The padded message is divided into blocks of `r` bits. Each block is XORed with the state, and the Keccak-f permutation is applied.
3.  **Squeezing phase:** The output hash is generated by taking the first `r` bits of the state. If more output is needed, the Keccak-f permutation is applied again.

### Vulnerabilities

*   Practical collision attacks against round-reduced SHA-3 (up to 6 rounds).
*   Zero-sum distinguishers for the full 24-round Keccak-f[1600], but they cannot be used to attack the hash function itself.

### Connections

*   **Designers:** Guido Bertoni, Joan Daemen, Michaël Peeters, and Gilles Van Assche (Keccak team)
*   **Standardization:** National Institute of Standards and Technology (NIST) as FIPS 202.


---

## Relatório: 33_UIjjpWMYusga661lOaTVWg_1766816830336_na1fn_L2hvbWUvdWJ1bnR1L3RlY2huaWNhbF9yZXBvcnQ.md

# Relatório Técnico: Infraestrutura de Chave Pública (PKI)

## Algoritmos e Protocolos Técnicos

### Estrutura do Certificado X.509 v3

*   **Certificate**
    *   **Version Number**: A versão do formato do certificado (e.g., 3 para v3).
    *   **Serial Number**: Um número de série único para cada certificado emitido por uma CA específica.
    *   **Signature Algorithm ID**: O identificador do algoritmo usado pela CA para assinar o certificado.
    *   **Issuer Name**: O Nome Distinguido (DN) da entidade que emitiu o certificado (a CA).
    *   **Validity Period**: O período durante o qual o certificado é válido, com os campos:
        *   **Not Before**: A data e hora de início da validade.
        *   **Not After**: A data e hora de fim da validade.
    *   **Subject Name**: O Nome Distinguido (DN) da entidade a quem o certificado é emitido.
    *   **Subject Public Key Info**: A informação da chave pública do sujeito, incluindo:
        *   **Public Key Algorithm**: O algoritmo da chave pública (e.g., RSA, DSA, ECDSA).
        *   **Subject Public Key**: A chave pública em si.
    *   **Issuer Unique Identifier (Opcional)**: Um identificador único para o emissor (usado na v2).
    *   **Subject Unique Identifier (Opcional)**: Um identificador único para o sujeito (usado na v2).
    *   **Extensions (Opcional, v3)**: Uma sequência de uma ou mais extensões, cada uma com um OID (Object Identifier) único.
*   **Certificate Signature Algorithm**: O algoritmo de assinatura do certificado.
*   **Certificate Signature**: A assinatura digital da CA.

### Algoritmo RSA

#### Geração de Chaves

1.  **Escolha de primos:** Escolha dois números primos grandes, `p` e `q`.
2.  **Cálculo de n:** Calcule o módulo `n = p * q`.
3.  **Cálculo da Função Totiente de Euler:** Calcule `Φ(n) = (p - 1) * (q - 1)`.
4.  **Escolha do expoente de criptografia (e):** Escolha um inteiro `e` tal que `1 < e < Φ(n)` e `mdc(e, Φ(n)) = 1`.
5.  **Cálculo do expoente de descriptografia (d):** Calcule `d` tal que `(d * e) ≡ 1 (mod Φ(n))`. `d` é o inverso multiplicativo modular de `e` módulo `Φ(n)`.

*   **Chave Pública:** `(n, e)`
*   **Chave Privada:** `(n, d)`

#### Criptografia

Para uma mensagem `M`, o texto cifrado `C` é calculado como:

`C = M^e mod n`

#### Descriptografia

Para um texto cifrado `C`, a mensagem original `M` é recuperada como:

`M = C^d mod n`

### Digital Signature Algorithm (DSA)

#### Componentes Globais de Chave Pública

1.  **p**: Um número primo com comprimento entre 512 e 1024 bits.
2.  **q**: Um número primo de 160 bits, tal que `q` divide `(p - 1)`.
3.  **g**: Calculado como `h^((p-1)/q) mod p`, onde `h` é um inteiro `1 < h < (p - 1)` e `g > 1`.

#### Chave Privada do Usuário

*   **x**: Um inteiro aleatório ou pseudoaleatório tal que `0 < x < q`.

#### Chave Pública do Usuário

*   **y**: Calculado como `g^x mod p`.

#### Assinatura

Para uma mensagem com hash `H(M)` e um inteiro aleatório `k` (`0 < k < q`):

1.  **r** = `(g^k mod p) mod q`
2.  **s** = `(k^-1 * (H(M) + x * r)) mod q`

*   **Assinatura:** `(r, s)`

#### Verificação

Para uma mensagem `M\'`, e assinatura `(r\', s\')`:

1.  **w** = `(s\')^-1 mod q`
2.  **u1** = `(H(M\') * w) mod q`
3.  **u2** = `(r\' * w) mod q`
4.  **v** = `((g^u1 * y^u2) mod p) mod q`

A assinatura é válida se `v = r\'`.

### Elliptic Curve Digital Signature Algorithm (ECDSA)

#### Parâmetros da Curva

*   **CURVE**: A curva elíptica e a equação do corpo utilizadas.
*   **G**: O ponto base da curva elíptica, um ponto na curva que gera um subgrupo de ordem prima `n`.
*   **n**: A ordem inteira de `G`, o que significa que `n * G = O`, onde `O` é o elemento de identidade.

#### Geração de Chave

1.  **Chave Privada (dA):** Um inteiro selecionado aleatoriamente no intervalo `[1, n-1]`.
2.  **Chave Pública (QA):** Um ponto na curva calculado como `QA = dA * G`.

#### Assinatura

Para uma mensagem `m`:

1.  Calcule `e = HASH(m)`, onde HASH é uma função de hash criptográfica (por exemplo, SHA-2).
2.  Seja `z` os `L_n` bits mais à esquerda de `e`, onde `L_n` é o comprimento em bits da ordem do grupo `n`.
3.  Selecione um inteiro aleatório criptograficamente seguro `k` de `[1, n-1]`.
4.  Calcule o ponto da curva `(x1, y1) = k * G`.
5.  Calcule `r = x1 mod n`. Se `r = 0`, volte para a etapa 3.
6.  Calcule `s = k^-1 * (z + r * dA) mod n`. Se `s = 0`, volte para a etapa 3.
7.  A assinatura é o par `(r, s)`.

#### Verificação

Para uma mensagem `m\'` e assinatura `(r\', s\')`:

1.  Verifique se `r\'` e `s\'` são inteiros em `[1, n-1]`.
2.  Calcule `e = HASH(m\')`.
3.  Seja `z` os `L_n` bits mais à esquerda de `e`.
4.  Calcule `u1 = z * s\'^-1 mod n`.
5.  Calcule `u2 = r\' * s\'^-1 mod n`.
6.  Calcule o ponto da curva `(x1, y1) = u1 * G + u2 * QA`.

A assinatura é válida se `r\' ≡ x1 (mod n)`. Se `(x1, y1) = O`, a assinatura é inválida.
## Vulnerabilidades e Fraquezas Conhecidas

*   **Protocolos desatualizados:** O uso de protocolos criptográficos e algoritmos de hash obsoletos, como SHA-1 e TLS 1.1, aumenta o risco de ataques man-in-the-middle.
*   **Chaves fracas e rotação infrequente:** Comprimentos de chave inferiores a 2048 bits são considerados vulneráveis. A não rotação de chaves permite que invasores explorem chaves comprometidas.
*   **Certificados mal gerenciados:** A falha em gerenciar, emitir, renovar ou revogar certificados digitais corretamente pode levar a interrupções e violações de dados.
*   **Proteção e gerenciamento inadequados de chaves privadas:** O comprometimento de uma chave privada pode ser usado para descriptografar informações críticas e confidenciais.
*   **CA raiz comprometida:** Se a CA raiz for comprometida, toda a cadeia de confiança será quebrada, desmoronando a arquitetura PKI.
*   **Falha na aplicação de patches e na resposta a vulnerabilidades de segurança:** A falta de gerenciamento de patches pode deixar as organizações vulneráveis a ataques.
*   **Falha de design fundamental:** Qualquer uma das centenas de CAs confiáveis pode emitir um certificado para qualquer nome de domínio, o que pode levar a ataques man-in-the-middle se uma CA emitir um certificado não autorizado.
*   **Emissão incorreta de certificados:** Houve casos em que CAs emitiram certificados não autorizados, que foram usados para espionagem e outros ataques.
*   **Roubo de certificados de assinatura:** Os certificados de assinatura de uma CA podem ser roubados, permitindo que invasores emitam certificados fraudulentos.

### Contramedidas

*   **Autorização da Autoridade de Certificação (CAA):** Permite que os proprietários de nomes de domínio especifiquem quais CAs estão autorizadas a emitir certificados para seu domínio.
*   **Transparência de Certificados (CT):** Um protocolo para registrar publicamente a existência de certificados TLS, permitindo que qualquer pessoa audite a atividade da CA e observe a emissão de certificados suspeitos.
## Conexões Governamentais e Institucionais

*   **Parcerias secretas:** A Agência de Segurança Nacional (NSA) dos EUA e o Quartel-General de Comunicações do Governo (GCHQ) do Reino Unido inseriram vulnerabilidades secretas (backdoors) em softwares de criptografia comerciais.
*   **Programa Bullrun da NSA:** Um programa da NSA para "inserir vulnerabilidades em sistemas de criptografia comerciais" para torná-los exploráveis pela coleta de inteligência de sinais (Sigint).
*   **Programa Edgehill do GCHQ:** O equivalente britânico do programa Bullrun da NSA.
*   **Protocolos visados:** A NSA tem recursos contra protocolos online amplamente utilizados, como HTTPS, voz sobre IP (VoIP) e Secure Sockets Layer (SSL).


---

## Relatório: 34_yxg5Lq5YZNyfffv6GyQWjz_1766816935677_na1fn_L2hvbWUvdWJ1bnR1L2ZpbmFsX3JlcG9ydA.md




# Pesquisa sobre DES (Data Encryption Standard)



## Equações e Fórmulas (LaTeX)

- Cifragem: `L_n = R_{n-1}; R_n = L_{n-1} \oplus f(R_{n-1}, K_n)`
- Decifragem: `R_{n-1} = L_n; L_{n-1} = R_n \oplus f(L_n, K_n)`
- Função de cifragem: `f(R, K) = P(S(E(R) \oplus K))`
- Geração de sub-chave: `K_n = KS(n, KEY)`


## Algoritmos e Protocolos

### Permutação Inicial (IP)

```
58, 50, 42, 34, 26, 18, 10, 2
60, 52, 44, 36, 28, 20, 12, 4
62, 54, 46, 38, 30, 22, 14, 6
64, 56, 48, 40, 32, 24, 16, 8
57, 49, 41, 33, 25, 17, 9, 1
59, 51, 43, 35, 27, 19, 11, 3
61, 53, 45, 37, 29, 21, 13, 5
63, 55, 47, 39, 31, 23, 15, 7
```

### Permutação Final (IP-1)

```
40, 8, 48, 16, 56, 24, 64, 32
39, 7, 47, 15, 55, 23, 63, 31
38, 6, 46, 14, 54, 22, 62, 30
37, 5, 45, 13, 53, 21, 61, 29
36, 4, 44, 12, 52, 20, 60, 28
35, 3, 43, 11, 51, 19, 59, 27
34, 2, 42, 10, 50, 18, 58, 26
33, 1, 41, 9, 49, 17, 57, 25
```

### Função de Expansão (E)

```
32, 1,  2,  3,  4,  5
4,  5,  6,  7,  8,  9
8,  9,  10, 11, 12, 13
12, 13, 14, 15, 16, 17
16, 17, 18, 19, 20, 21
20, 21, 22, 23, 24, 25
24, 25, 26, 27, 28, 29
28, 29, 30, 31, 32, 1
```

### S-Boxes (Caixas de Substituição)

... (O conteúdo das S-boxes será adicionado aqui após a extração completa)

### Permutação (P)

```
16, 7, 20, 21, 29, 12, 28, 17
1, 15, 23, 26, 5, 18, 31, 10
2, 8, 24, 14, 32, 27, 3, 9
19, 13, 30, 6, 22, 11, 4, 25
```

### Escalonamento de Chave (Key Schedule)

#### Permuted Choice 1 (PC-1)

```
57, 49, 41, 33, 25, 17, 9,  1
58, 50, 42, 34, 26, 18, 10, 2
59, 51, 43, 35, 27, 19, 11, 3
60, 52, 44, 36, 63, 55, 47, 39
31, 23, 15, 7,  62, 54, 46, 38
30, 22, 14, 6,  61, 53, 45, 37
29, 21, 13, 5,  28, 20, 12, 4
```

#### Permuted Choice 2 (PC-2)

```
14, 17, 11, 24, 1,  5,  3,  28
15, 6,  21, 10, 23, 19, 12, 4
26, 8,  16, 7,  27, 20, 13, 2
41, 52, 31, 37, 47, 55, 30, 40
51, 45, 33, 48, 44, 49, 39, 56
34, 53, 46, 42, 50, 36, 29, 32
```
### S-Boxes (Caixas de Substituição)

**S1**
```
14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7
0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8
4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0
15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
```

**S2**
```
15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10
3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5
0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15
13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
```

**S3**
```
10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8
13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1
13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7
1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
```

**S4**
```
7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15
13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9
10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4
3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
```

**S5**
```
2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9
14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6
4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14
11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
```

**S6**
```
12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11
10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8
9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6
4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
```

**S7**
```
4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1
13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6
1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2
6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
```

**S8**
```
13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7
1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2
7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8
2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
```
## Vulnerabilidades

- **Tamanho da chave de 56 bits:** Suscetível a ataques de força bruta com hardware moderno.
- **Tamanho do bloco de 64 bits:** Pode levar a colisões de bloco e ataques de aniversário em grandes volumes de dados.
- **Chaves fracas:** Quatro chaves que produzem o mesmo resultado na cifragem e decifragem.
- **Chaves semi-fracas:** Seis pares de chaves que cifram texto plano para o mesmo texto cifrado.
- **Criptoanálise diferencial:** Requer 2^47 textos planos escolhidos.
- **Criptoanálise linear:** Requer 2^43 textos planos conhecidos.

## Conexões

- **IBM:** Desenvolveu o algoritmo Lucifer, que foi a base para o DES.
- **NSA (Agência de Segurança Nacional dos EUA):** Modificou o algoritmo Lucifer, alterando as S-boxes e reduzindo o tamanho da chave de 128 para 56 bits. Há suspeitas de que a NSA enfraqueceu o algoritmo intencionalmente para poder monitorar as comunicações.
# Pesquisa sobre 3DES (Triple DES)

## Equações e Fórmulas (LaTeX)

- Cifragem: `C = E_{K3}(D_{K2}(E_{K1}(P)))`
- Decifragem: `P = D_{K1}(E_{K2}(D_{K3}(C)))`

## Variáveis e Parâmetros

- `P`: Bloco de texto claro de 64 bits
- `C`: Bloco de texto cifrado de 64 bits
- `K1, K2, K3`: Chaves DES de 56 bits
- `E_K(P)`: Cifragem DES do texto claro `P` com a chave `K`
- `D_K(C)`: Decifragem DES do texto cifrado `C` com a chave `K`

## Algoritmos e Protocolos

O 3DES (Triple DES) aplica o algoritmo DES três vezes a cada bloco de dados. Existem três opções de chaveamento:

- **Opção de Chaveamento 1:** K1, K2 e K3 são chaves independentes. O comprimento da chave é de 168 bits (3 * 56 bits), mas a força efetiva da cifra é de 112 bits devido ao ataque meet-in-the-middle.
- **Opção de Chaveamento 2:** K1 e K2 são chaves independentes, e K3 é igual a K1. O comprimento da chave é de 112 bits (2 * 56 bits).
- **Opção de Chaveamento 3:** K1, K2 e K3 são todas iguais. Isso equivale ao DES de 56 bits e é usado para retrocompatibilidade.

O processo de cifragem para a Opção de Chaveamento 1 é o seguinte:

1. Cifrar o bloco de dados com a chave K1.
2. Decifrar o resultado do passo 1 com a chave K2.
3. Cifrar o resultado do passo 2 com a chave K3.

O processo de decifragem inverte essa ordem:

1. Decifrar o bloco de dados com a chave K3.
2. Cifrar o resultado do passo 1 com a chave K2.
3. Decifrar o resultado do passo 2 com a chave K1.

## Vulnerabilidades

- **Ataque meet-in-the-middle:** Reduz a segurança efetiva do 3DES com três chaves para 112 bits.
- **Tamanho do bloco de 64 bits:** O pequeno tamanho do bloco torna o 3DES vulnerável a ataques de colisão quando grandes quantidades de dados são criptografadas com a mesma chave. O ataque "Sweet32" (CVE-2016-2183) explora essa fraqueza.
- **Desempenho:** O 3DES é significativamente mais lento em software em comparação com algoritmos mais modernos como o AES.
- **Chaves fracas e semi-fracas:** O 3DES é suscetível às mesmas chaves fracas e semi-fracas do DES.

## Conexões

- **IBM:** O 3DES é uma extensão do DES, que foi projetado pela IBM.
- **NIST (National Institute of Standards and Technology):** O NIST padronizou o 3DES (conhecido como TDEA - Triple Data Encryption Algorithm) na FIPS PUB 46-3 e, mais tarde, na Special Publication 800-67. O NIST desaconselhou o uso do 3DES para novas aplicações e o descontinuou em 2023.
- **Walter Tuchman:** Em 1978, propôs um método de criptografia tripla com duas chaves.
- **Ralph Merkle e Martin Hellman:** Propuseram uma versão mais segura de criptografia tripla com três chaves.
# Pesquisa sobre AES (Advanced Encryption Standard)

## Equações e Fórmulas (LaTeX)

- **SubBytes (Transformação Afim):** `b'_i = b_i \oplus b_{(i+4) \mod 8} \oplus b_{(i+5) \mod 8} \oplus b_{(i+6) \mod 8} \oplus b_{(i+7) \mod 8} \oplus c_i`
- **MixColumns (Multiplicação de Matriz):** `s'_{c}(x) = a(x) \otimes s_c(x)` onde `a(x) = {03}x^3 + {01}x^2 + {01}x + {02}`
- **InvMixColumns (Multiplicação de Matriz):** `s'_{c}(x) = a^{-1}(x) \otimes s_c(x)` onde `a^{-1}(x) = {0b}x^3 + {0d}x^2 + {09}x + {0e}`
- **AddRoundKey:** `[s'_{0,c}, s'_{1,c}, s'_{2,c}, s'_{3,c}] = [s_{0,c}, s_{1,c}, s_{2,c}, s_{3,c}] \oplus [w_{round*Nb+c}]`

## Variáveis e Parâmetros

- `state`: Matriz de bytes 4x4 que representa o bloco de dados.
- `Nb`: Número de colunas no `state` (sempre 4 para AES).
- `Nk`: Número de palavras de 32 bits na chave (4, 6 ou 8).
- `Nr`: Número de rodadas (10, 12 ou 14), dependendo do `Nk`.
- `w`: Escalonamento de chave (key schedule).

## Algoritmos e Protocolos

O AES é uma cifra de bloco que opera em blocos de 128 bits. Ele usa chaves de 128, 192 ou 256 bits. O algoritmo consiste em várias rodadas, e o número de rodadas depende do tamanho da chave.

Cada rodada consiste em quatro transformações:

1.  **SubBytes:** Uma substituição não linear onde cada byte do `state` é substituído por outro de acordo com uma S-box.
2.  **ShiftRows:** Uma transposição onde as últimas três linhas do `state` são deslocadas ciclicamente.
3.  **MixColumns:** Uma operação de mistura que opera nas colunas do `state`, combinando os quatro bytes em cada coluna.
4.  **AddRoundKey:** Cada byte do `state` é combinado com um byte da sub-chave da rodada usando a operação XOR.

A rodada final é ligeiramente diferente, pois omite a transformação `MixColumns`.

### Escalonamento de Chave (Key Expansion)

O escalonamento de chave gera as sub-chaves para cada rodada a partir da chave de cifra original. Envolve as operações `RotWord`, `SubWord` e `Rcon`.

## Vulnerabilidades

- **Ataques de canal lateral (Side-channel attacks):** Implementações de AES podem ser vulneráveis a ataques que exploram informações vazadas durante a execução do algoritmo, como consumo de energia ou emanações eletromagnéticas.
- **Ataques de falha (Fault attacks):** A introdução de falhas no hardware que executa o AES pode levar à recuperação da chave.
- **Ataques relacionados à chave (Related-key attacks):** Embora o AES seja projetado para ser resistente a esses ataques, algumas variantes foram demonstradas em versões reduzidas do AES.
- **Ataques de computação quântica:** O algoritmo de Shor para computadores quânticos pode, teoricamente, quebrar o AES. No entanto, os computadores quânticos atuais não são poderosos o suficiente para isso.

## Conexões

- **NIST (National Institute of Standards and Technology):** O NIST iniciou o processo de seleção do AES em 1997 e publicou o padrão em 2001.
- **Joan Daemen e Vincent Rijmen:** Criptógrafos belgas que desenvolveram o algoritmo Rijndael, que foi selecionado como o AES.
# Pesquisa sobre Modos de Operação de Cifra de Bloco

## Electronic Codebook (ECB)

### Equações e Fórmulas (LaTeX)
- Cifragem: `C_j = E_K(P_j)`
- Decifragem: `P_j = D_K(C_j)`

### Vulnerabilidades
- **Repetição de padrões:** Blocos de texto claro idênticos produzem blocos de texto cifrado idênticos, o que revela padrões nos dados.
- **Não provê integridade:** É vulnerável a ataques de rearranjo de blocos.

## Cipher Block Chaining (CBC)

### Equações e Fórmulas (LaTeX)
- Cifragem: `C_j = E_K(P_j \oplus C_{j-1})` com `C_0 = IV`
- Decifragem: `P_j = D_K(C_j) \oplus C_{j-1}` com `C_0 = IV`

### Variáveis e Parâmetros
- `IV`: Vetor de Inicialização (Initialization Vector) - um bloco de bits aleatório e imprevisível.

### Vulnerabilidades
- **Propagação de erro:** Um erro em um bloco de texto cifrado afeta a decifragem de dois blocos.
- **Ataque de preenchimento (Padding oracle attack):** Pode permitir a um atacante decifrar o texto cifrado explorando o preenchimento dos blocos.

## Counter (CTR)

### Equações e Fórmulas (LaTeX)
- Cifragem: `C_j = P_j \oplus E_K(T_j)`
- Decifragem: `P_j = C_j \oplus E_K(T_j)`

### Variáveis e Parâmetros
- `T_j`: Um contador único para cada bloco.

### Vulnerabilidades
- **Reutilização de contador:** A reutilização do mesmo contador com a mesma chave quebra a segurança do modo CTR.

## Galois/Counter Mode (GCM)

### Equações e Fórmulas (LaTeX)
- Cifragem: `C_j = P_j \oplus E_K(T_j)`
- Autenticação (GHASH): `g = GHASH_H(A || C)`
- Tag de Autenticação: `T = MSB_t(g \oplus E_K(J_0))`

### Variáveis e Parâmetros
- `A`: Dados autenticados adicionais (Additional Authenticated Data).
- `H`: Chave de autenticação derivada de `K`.
- `J_0`: Bloco de contador inicial.

### Vulnerabilidades
- **Reutilização de IV:** A reutilização do mesmo IV com a mesma chave pode levar a falhas catastróficas de segurança, permitindo a recuperação da chave de autenticação.
- **Tags de autenticação curtas:** O uso de tags de autenticação curtas pode aumentar a probabilidade de sucesso de um ataque de falsificação.


---

## Relatório: 35_T0ZJIN2rP5NOyem0HCMVEt_1766816780571_na1fn_L2hvbWUvdWJ1bnR1L3RlY2huaWNhbF9yZXBvcnQ.md

# Relatório Técnico: Criptografia de Teoria dos Números

## Equações e Fórmulas (LaTeX)

`b = ac`; `a \equiv b \pmod{m}`; `a+b = c+d \pmod{n}`; `ab = cd \pmod{n}`; `(2+3) \pmod{26} = 5 \pmod{26} = 5`; `x \equiv a_1 \pmod{m_1}`; `x \equiv a_2 \pmod{m_2}`; `...`; `x \equiv a_k \pmod{m_k}`; `\phi(p) = p - 1`; `\phi(N) = \phi(p) \cdot \phi(q) = (p-1)(q-1)`; `xy \equiv 1 \pmod{m}`; `b^e \equiv 1 \pmod{m}`; `a^{p-1} \equiv 1 \pmod{p}`; `c \equiv m^e \pmod{N}`; `m \equiv c^d \pmod{N}`; `ed \equiv 1 \pmod{\phi(N)}`; `ed - 1 = k\phi(N)`; `ed = 1 + k'(p-1)`; `m^{ed} = m^{1+k'(p-1)} = m \cdot (m^{p-1})^{k'}`; `c^d \equiv (m^e)^d \equiv m^{ed} \pmod{p}`; `c \equiv m^e \pmod{N} \equiv 25^3 \pmod{187} = 15625 \pmod{187} = 104`; `d(3) \equiv 1 \pmod{160}`; `3 \cdot (-53) \equiv 1 \pmod{160}`; `d = -53 \pmod{160} = 107`; `m = c^d \pmod{N} = 104^{107} \pmod{187} = 25`

## Variáveis e Definições

- `a|b`: a divide b
- `n`: um inteiro
- `p`: um número primo
- `m`: módulo
- `\phi(n)`: Função totiente de Euler, o número de inteiros entre 1 e n que são relativamente primos a n.
- `N`: pq, onde p e q são números primos.
- `e`: um inteiro relativamente primo a `\phi(N)`.
- `d`: o inverso de `e` módulo `\phi(N)`.
- `c`: texto cifrado, `c \equiv m^e \pmod{N}`.
- `m`: mensagem em texto claro.
- `k`: um inteiro.

## Algoritmos

### Cifra de César
Substitui cada letra por outra, deslocando o alfabeto um número específico de posições.

### Criptografia RSA
1.  Bob escolhe dois números primos, `p` e `q`, e calcula `N = pq`.
2.  Bob escolhe um inteiro `e` que é relativamente primo a `\phi(N)`.
3.  Bob divulga `N` e `e`.
4.  Alice converte sua mensagem para um número `m` módulo `N`.
5.  Alice calcula `c \equiv m^e \pmod{N}`.
6.  Alice envia `c` para Bob.
7.  Bob encontra o inverso `d` de `e` módulo `\phi(N)`.
8.  Bob calcula `m \equiv c^d \pmod{N}`.

### Protocolos e Funções Criptográficas

- **SSL/TLS (Secure Socket Layer/Transport Layer Security):** Protocolos de comunicação criptográfica para segurança em transações online.
- **PGP (Pretty Good Privacy):** Protocolo de criptografia de ponta a ponta para mensagens seguras.
- **Signal Protocol:** Protocolo de criptografia de ponta a ponta para mensagens seguras.
- **bcrypt:** Função de hash de senha criptograficamente segura.
- **Argon2:** Função de hash de senha criptograficamente segura.

## Vulnerabilidades

- **Cifra de César:** Facilmente quebrada por análise de frequência.
- **RSA:**
    - Se `e` é pequeno e `m` também é pequeno, então `m^e` pode ser menor que `N`. Nesse caso, `c = m^e`, e `m` pode ser encontrado calculando a raiz `e`-ésima de `c`.
    - Se a mesma mensagem é enviada para múltiplos destinatários com o mesmo `e` pequeno, o Teorema Chinês do Resto pode ser usado para quebrar a criptografia.
- **Ataques de força bruta:** Tentativa de adivinhar senhas tentando todas as combinações possíveis.
- **Ataques de dicionário:** Tentativa de adivinhar senhas tentando palavras de um dicionário.
- **Injeção de malware:** Inserção de software malicioso em um sistema.
- **Ataques à cadeia de suprimentos:** Comprometimento de software ou hardware durante o processo de fabricação ou distribuição.

## Conexões

Nenhuma conexão com governos, corporações ou agências foi encontrada nos documentos pesquisados.


---

## Relatório: 36_8TxnX1y6YdKDnx0nOhX06p_1766816799501_na1fn_L2hvbWUvdWJ1bnR1L2RscF9yZXBvcnQ.md

# Relatório Técnico: O Problema do Logaritmo Discreto

## Equações e Fórmulas

- A equação fundamental do Problema do Logaritmo Discreto (DLP) é definida como: `g^x = h`, onde `g` é um gerador de um grupo cíclico `G`, `h` é um elemento de `G`, e `x` é o logaritmo discreto a ser encontrado.
- A fórmula de mudança de base para logaritmos discretos é: `log_c(g) = log_c(b) · log_b(g)`.
- No contexto de grupos multiplicativos de inteiros módulo `p`, o DLP é expresso como: `a^x ≡ b (mod p)`.
- No protocolo de troca de chaves de Diffie-Hellman, as chaves públicas são calculadas como `x = g^a mod p` e `y = g^b mod p`, e o segredo compartilhado é `C = y^a mod p = x^b mod p = g^(ab) mod p`.
- No sistema de criptografia Elgamal, a chave pública é `(p, g, c)` onde `c = g^d mod p`, a cifragem é `(k, m * c^i mod p)` com `k = g^i mod p`, e a decifragem é `m = y * inv(k^d) mod p`.

## Variáveis e Parâmetros

- `G`: Um grupo cíclico finito.
- `g`: Um gerador do grupo `G`.
- `h`: Um elemento do grupo `G`.
- `x`: O logaritmo discreto de `h` na base `g`.
- `n`: A ordem do grupo `G`.
- `p`: Um número primo, frequentemente usado como módulo em criptografia.
- `a`, `b`: Inteiros secretos na troca de chaves de Diffie-Hellman.
- `d`: A chave privada no sistema Elgamal.
- `c`: Um componente da chave pública no sistema Elgamal.
- `i`, `k`: Inteiros aleatórios usados na cifragem Elgamal.

## Algoritmos

### Algoritmos Genéricos

- **Busca Linear (Linear Search):** O algoritmo mais simples, que testa todas as potências de `g` até encontrar `h`. Sua complexidade é `O(n)`.
- **Passos de bebê, passos de gigante (Baby-step giant-step):** Um algoritmo de encontro no meio com complexidade de tempo e espaço de `O(sqrt(n))`.

### Algoritmos Específicos

- **Algoritmo de Pohlig-Hellman:** Eficiente quando a ordem do grupo `n` é um número liso (composto por pequenos fatores primos). Ele reduz o problema a subgrupos de ordem de potência prima e combina os resultados usando o Teorema Chinês do Resto. A complexidade é `O(Σ e_i * (log n + sqrt(p_i)))`.
- **Algoritmo de Cálculo de Índice (Index Calculus):** Um algoritmo sub-exponencial que se aplica a grupos como `(Z/pZ)*`. Ele envolve a criação de uma base de fatores de pequenos primos e a resolução de um sistema de equações lineares. É mais rápido que o Pohlig-Hellman para grupos de ordem prima grande.

## Vulnerabilidades

- **Computação Quântica:** O algoritmo de Shor pode resolver o DLP em tempo polinomial, tornando os sistemas baseados em DLP inseguros contra computadores quânticos.
- **Ordem do Grupo Lisa:** Se a ordem do grupo `n` for um número liso, o algoritmo de Pohlig-Hellman pode resolver o DLP eficientemente.
- **Tamanho do Primo:** Em criptossistemas baseados em `(Z/pZ)*`, um primo `p` pequeno torna o DLP vulnerável a ataques de força bruta e algoritmos como o cálculo de índice.
- **Ataque Logjam:** Uma vulnerabilidade em implementações de Diffie-Hellman que usam parâmetros fracos (primos pequenos), permitindo que um atacante pré-calcule logaritmos discretos para um primo comum.

## Conexões

- A pesquisa não revelou conexões diretas do desenvolvimento fundamental do Problema do Logaritmo Discreto com agências governamentais como a NSA ou o GCHQ. As principais contribuições vieram do meio acadêmico, com pesquisadores de instituições como a Universidade de Stanford (Martin Hellman) e o MIT (Leonard Adleman).


---

## Relatório: 37_FxaiUrlemU025jRbtZSQI5_1766816839461_na1fn_L2hvbWUvdWJ1bnR1L3JlcG9ydA.md

# Relatório Técnico sobre Criptografia Baseada em Reticulado


## Definições Matemáticas Fundamentais

### Reticulado (Lattice)

Um reticulado (lattice) L é um subconjunto de pontos no espaço euclidiano n-dimensional, que forma um grupo abeliano sob adição. Formalmente, dado um conjunto de vetores linearmente independentes **b**~1~, **b**~2~, ..., **b**~n~ em **R**^n^, que formam uma base, um reticulado gerado por esta base é o conjunto de todas as combinações lineares inteiras dos vetores da base:

```latex
L = \{ \sum_{i=1}^{n} a_i b_i : a_i \in \mathbb{Z} \}
```

**Variáveis:**
*   `L`: O reticulado.
*   `b_i`: Vetores da base do reticulado.
*   `a_i`: Coeficientes inteiros.
*   `n`: Dimensão do espaço.

### Problema do Vetor Mais Curto (Shortest Vector Problem - SVP)

O SVP é um problema computacionalmente difícil que consiste em encontrar o vetor não-nulo mais curto (em termos de norma euclidiana) em um dado reticulado L.

**Definição Formal:** Dado um reticulado L, encontrar um vetor `v` em L tal que `v` != 0 e ||`v`|| <= ||`u`|| para todos os `u` em L, `u` != 0.

### Problema do Vetor Mais Próximo (Closest Vector Problem - CVP)

O CVP é outro problema computacionalmente difícil que, dado um reticulado L e um vetor `t` que não pertence necessariamente a L, consiste em encontrar o vetor em L que está mais próximo de `t`.

**Definição Formal:** Dado um reticulado L e um vetor `t`, encontrar um vetor `v` em L tal que ||`v` - `t`|| <= ||`u` - `t`|| para todos os `u` em L.
_content

### Problema de Aprendizado com Erros (Learning With Errors - LWE)

O problema LWE é um problema computacional que forma a base de muitos criptossistemas pós-quânticos. A ideia é esconder um segredo `s` adicionando um pequeno ruído a um sistema de equações lineares.

**Definição Formal (Search LWE):**

Dado um módulo `q`, uma dimensão `n`, um vetor secreto `s` em Z_q^n e uma distribuição de erro `χ` sobre Z_q, o problema LWE consiste em encontrar `s` a partir de uma série de amostras da forma `(a, b)`, onde `a` é um vetor aleatório em Z_q^n e `b` é calculado como:

```latex
b = \langle a, s \rangle + e \pmod{q}
```

**Variáveis:**
*   `s`: O vetor secreto em Z_q^n.
*   `a`: Um vetor conhecido, amostrado uniformemente de Z_q^n.
*   `b`: O resultado da equação LWE, que é conhecido.
*   `e`: Um erro (ruído) pequeno, amostrado da distribuição `χ`.
*   `q`: O módulo, um inteiro grande.
*   `n`: A dimensão do vetor secreto `s` e dos vetores `a`.
*   `χ`: A distribuição de erro, geralmente uma Gaussiana discreta.

**Definição Formal (Decision LWE):**

A versão de decisão do LWE (DLWE) consiste em distinguir, com probabilidade não desprezível, entre um número polinomial de amostras LWE `(a, b)` e o mesmo número de amostras `(a, u)` onde `u` é amostrado uniformemente de Z_q.
### Problema de Aprendizado com Erros em Anéis (Ring Learning With Errors - RLWE)

O problema RLWE é uma variante do LWE que oferece maior eficiência, substituindo operações com vetores por operações com polinômios em um anel. Isso reduz o tamanho das chaves e acelera os cálculos.

**Definição Formal (Search RLWE):**

Seja `R_q = Z_q[x] / <f(x)>` um anel de polinômios, onde `f(x)` é um polinômio ciclotômico de grau `n`. O problema RLWE consiste em encontrar um polinômio secreto `s(x)` em `R_q` a partir de uma série de amostras da forma `(a(x), b(x))`, onde `a(x)` é um polinômio aleatório em `R_q` e `b(x)` é calculado como:

```latex
b(x) = a(x) \cdot s(x) + e(x) \pmod{q}
```

**Variáveis:**
*   `s(x)`: O polinômio secreto em `R_q`.
*   `a(x)`: Um polinômio conhecido, amostrado uniformemente de `R_q`.
*   `b(x)`: O resultado da equação RLWE, que é conhecido.
*   `e(x)`: Um polinômio de erro pequeno, cujos coeficientes são amostrados de uma distribuição `χ`.
*   `R_q`: O anel de polinômios `Z_q[x] / <f(x)>`.
*   `f(x)`: Um polinômio (geralmente ciclotômico) que define o anel.
*   `q`: O módulo, um inteiro grande.
*   `n`: O grau do polinômio `f(x)`.

**Definição Formal (Decision RLWE):**

A versão de decisão do RLWE (DRLWE) consiste em distinguir, com probabilidade não desprezível, entre um número polinomial de amostras RLWE `(a(x), b(x))` e o mesmo número de amostras `(a(x), u(x))` onde `u(x)` é um polinômio amostrado uniformemente de `R_q`.
### Criptossistema NTRU

O NTRU é um criptossistema de chave pública baseado em reticulado que não se baseia diretamente nos problemas LWE ou RLWE, mas em um problema de reticulado relacionado, conhecido como o problema do vetor mais curto em um reticulado NTRU.

**Geração de Chave:**

1.  **Parâmetros:** `N` (grau do polinômio), `p` (módulo pequeno), `q` (módulo grande).
2.  **Chave Privada:** Dois polinômios `f(x)` e `g(x)` de grau `N-1` com coeficientes pequenos (geralmente em `{-1, 0, 1}`). O polinômio `f(x)` deve ser invertível módulo `p` e `q`. A chave privada é `(f(x), f_p(x))`, onde `f_p(x)` é o inverso de `f(x)` mod `p`.
3.  **Chave Pública:** O polinômio `h(x)` é calculado como:

    ```latex
    h(x) = p \cdot f_q(x) \cdot g(x) \pmod{q}
    ```

    onde `f_q(x)` é o inverso de `f(x)` mod `q`.

**Cifragem:**

Para cifrar uma mensagem `m(x)` (um polinômio com coeficientes em `Z_p`), escolhe-se um polinômio aleatório `r(x)` com coeficientes pequenos. A cifra `e(x)` é:

```latex
e(x) = r(x) \cdot h(x) + m(x) \pmod{q}
```

**Decifragem:**

1.  O receptor calcula `a(x)`:

    ```latex
    a(x) = f(x) \cdot e(x) \pmod{q}
    ```

2.  Os coeficientes de `a(x)` são centrados no intervalo `[-q/2, q/2]`.
3.  A mensagem original é recuperada calculando:

    ```latex
    m(x) = f_p(x) \cdot a(x) \pmod{p}
    ```

**Variáveis:**
*   `f(x), g(x)`: Polinômios privados com coeficientes pequenos.
*   `f_p(x), f_q(x)`: Inversos de `f(x)` módulo `p` e `q`.
*   `h(x)`: Chave pública.
*   `m(x)`: Mensagem (polinômio).
*   `r(x)`: Polinômio aleatório de ofuscação.
*   `e(x)`: Cifra (polinômio).
*   `N, p, q`: Parâmetros do sistema.

### CRYSTALS-Kyber

O Kyber é um Mecanismo de Encapsulamento de Chave (KEM) seguro contra ataques de cifratexto escolhido (IND-CCA2), baseado na dureza do problema de aprendizado com erros em módulos (Module-LWE). Foi selecionado pelo NIST para padronização.

**Algoritmo 1: Kyber.CPAPKE.KeyGen()**

```
1: d ← B^32
2: (ρ, σ) ← G(d)
3: N ← 0
4: Â ← Parse(ρ)
5: s ← CBD_η1(σ, N)
6: N ← N + k
7: e ← CBD_η1(σ, N)
8: N ← N + k
9: ŝ ← NTT(s)
10: ê ← NTT(e)
11: t̂ ← Â ◦ ŝ + ê
12: pk ← Encode(t̂) || ρ
13: sk ← Encode(ŝ)
14: return (pk, sk)
```

**Algoritmo 2: Kyber.CPAPKE.Enc(pk, m, r)**

```
1: t̂ ← Decode(pk)
2: ρ ← pk + 32k
3: Â ← Parse(ρ)
4: r' ← CBD_η2(r, 0)
5: e1 ← CBD_η2(r, k)
6: e2 ← CBD_η2(r, 2k)
7: r̂ ← NTT(r')
8: u ← Â^T ◦ r̂ + NTT(e1)
9: v ← t̂^T ◦ r̂ + NTT(e2) + Decompress(m)
10: c1 ← Compress(u)
11: c2 ← Compress(v)
12: return (c1, c2)
```

**Algoritmo 3: Kyber.CPAPKE.Dec(sk, c)**

```
1: (c1, c2) ← c
2: u ← Decompress(c1)
3: v ← Decompress(c2)
4: ŝ ← Decode(sk)
5: m' ← v - ŝ^T ◦ u
6: return Compress(m')
```

**Variáveis:**
*   `Â`: Matriz pública (polinômios na forma NTT).
*   `s, e`: Vetores secretos com coeficientes pequenos.
*   `t`: Vetor público `t = As + e`.
*   `r', e1, e2`: Vetores de erro com coeficientes pequenos.
*   `u, v`: Partes da cifra.
*   `pk, sk`: Chave pública e chave secreta.
*   `m`: Mensagem.
*   `c`: Cifra.
*   `ρ, σ`: Sementes aleatórias.
*   `G, H, J`: Funções de hash (XOF e hash).
*   `NTT`: Transformada Rápida de Número Teórico (Number-Theoretic Transform).
*   `CBD`: Amostragem da distribuição binomial centrada.
*   `Parse, Encode, Decode, Compress, Decompress`: Funções de serialização e compressão.

### CRYSTALS-Dilithium

O Dilithium é um esquema de assinatura digital baseado em reticulado, cuja segurança se baseia na dureza dos problemas de reticulado sobre módulos. Assim como o Kyber, foi selecionado pelo NIST para padronização.

**Algoritmo 4: Dilithium.KeyGen()**

```
1: ζ ← B^32
2: (ρ, σ, K) ← G(ζ)
3: Â ← Parse(ρ)
4: s1 ← CBD_η(σ, 0)
5: s2 ← CBD_η(σ, l)
6: t ← Âs1 + s2
7: (t1, t0) ← Power2Round(t)
8: pk ← Encode(ρ) || Encode(t1)
9: sk ← Encode(ρ) || Encode(t1) || Encode(s1) || Encode(s2) || K
10: return (pk, sk)
```

**Algoritmo 5: Dilithium.Sign(sk, M)**

```
1: (ρ, t1, s1, s2, K) ← (Decode(sk), Decode(sk+32), Decode(sk+32+32k), Decode(sk+32+32k+32l), sk+32+32k+32l+32l)
2: Â ← Parse(ρ)
3: μ ← CRH(K, M)
4: κ ← 0
5: ρ' ← CRH(tr, μ)
6: y ← CBD_γ1(ρ', κ)
7: κ ← κ + l
8: w ← Ây
9: (w1, w0) ← Decompose(w)
10: c' ← SampleInBall(H(μ, w1))
11: c ← NTT^-1(c')
12: z ← y + cs1
13: r0 ← w0 - cs2
14: if ||z||_∞ ≥ γ1 - β or ||r0||_∞ ≥ γ2 - β then return Sign(sk, M)
15: h ← MakeHint(-cs2, w1)
16: σ ← (c', z, h)
17: return σ
```

**Algoritmo 6: Dilithium.Verify(pk, M, σ)**

```
1: (ρ, t1) ← (Decode(pk), Decode(pk+32))
2: (c', z, h) ← σ
3: Â ← Parse(ρ)
4: μ ← CRH(K, M)
5: c ← NTT^-1(c')
6: w' ← Âz - ct1
7: if ||z||_∞ ≥ γ1 - β or UseHint(h, w') ≠ w' then return false
8: return c' == SampleInBall(H(μ, w'))
```

**Variáveis:**
*   `A`: Matriz pública.
*   `s1, s2`: Chaves secretas com coeficientes pequenos.
*   `t`: Parte da chave pública `t = As1 + s2`.
*   `y, z`: Vetores usados na assinatura.
*   `c`: Desafio (challenge).
*   `w, w0, w1`: Vetores intermediários.
*   `pk, sk`: Chave pública e chave secreta.
*   `M`: Mensagem.
*   `σ`: Assinatura.
*   `ρ, K, μ`: Sementes e hashes.
*   `G, H, CRH`: Funções de hash.
*   `NTT`: Transformada Rápida de Número Teórico.
*   `CBD, SampleInBall`: Funções de amostragem.
*   `Power2Round, Decompose, MakeHint, UseHint`: Funções de manipulação de bits.

## Vulnerabilidades e Fraquezas Conhecidas

A segurança da criptografia baseada em reticulado depende da dificuldade presumida de certos problemas de reticulado. No entanto, como em qualquer área da criptografia, vulnerabilidades podem surgir de várias fontes:

*   **Escolha de Parâmetros:** A segurança dos esquemas baseados em reticulado é altamente sensível à escolha dos parâmetros (N, q, distribuição de erro). Parâmetros fracos podem tornar os problemas de reticulado subjacentes tratáveis.
    *   **Erro Pequeno (Small Error):** Em variantes do (R)LWE, se a magnitude do erro for muito pequena, ataques como o ataque de força bruta no erro ou ataques que exploram a estrutura do anel podem se tornar viáveis.
    *   **Módulo `q` com Estrutura Especial:** Se `q` tiver fatores pequenos ou uma estrutura particular, isso pode ser explorado em alguns ataques.

*   **Ataques de Side-Channel:** Implementações de hardware e software podem vazar informações sobre as chaves secretas através de canais laterais, como consumo de energia, tempo de execução ou emanações eletromagnéticas. Ataques de análise de potência e de tempo foram demonstrados contra implementações de (R)LWE e NTRU.

*   **Ataques de Injeção de Falhas (Fault Injection Attacks):** A introdução de falhas no hardware durante a computação criptográfica pode levar à recuperação da chave secreta. Vários ataques de injeção de falhas foram propostos contra implementações de (R)LWE e Dilithium.

*   **Ataques Algorítmicos:**
    *   **Ataques de Reticulado (Lattice Attacks):** Algoritmos como o LLL (Lenstra–Lenstra–Lovász) e suas variantes (BKZ) são usados para resolver problemas de reticulado. A melhoria contínua desses algoritmos impacta diretamente a segurança concreta dos criptossistemas baseados em reticulado.
    *   **Ataque de Força Bruta no Erro (Guessing the Error):** Se a distribuição de erro não for escolhida corretamente, um invasor pode tentar adivinhar o erro `e` e, em seguida, resolver um sistema de equações lineares para encontrar o segredo `s`.
    *   **Ataques em Anéis Específicos (para RLWE):** A escolha do anel no RLWE é crucial. Anéis com estruturas particulares (por exemplo, anéis ciclotômicos de potência de 2) podem ser mais vulneráveis a certos ataques, como o ataque de subcampo.

*   **Vulnerabilidades de Implementação:** Erros na implementação, como o uso de geradores de números aleatórios fracos ou a implementação incorreta da amostragem de erro, podem comprometer completamente a segurança do sistema.
## Conexões Institucionais e Governamentais

A criptografia baseada em reticulado, especialmente com o advento da computação quântica, tornou-se uma área de intenso interesse para governos, agências de inteligência e órgãos de padronização em todo o mundo.

*   **NIST (National Institute of Standards and Technology):** O NIST, uma agência do Departamento de Comércio dos EUA, tem liderado o esforço global para padronizar algoritmos criptográficos pós-quânticos (PQC). Em 2022, após um processo de vários anos, o NIST selecionou o **CRYSTALS-Kyber** para encapsulamento de chaves e o **CRYSTALS-Dilithium** para assinaturas digitais como os principais algoritmos a serem padronizados. Isso significa que eles se tornarão os padrões recomendados para proteger sistemas governamentais e comerciais dos EUA contra a ameaça quântica.

*   **NSA (National Security Agency):** A NSA, a principal agência de inteligência de sinais dos EUA, publicou orientações recomendando a transição para algoritmos PQC. A NSA declarou que espera que os algoritmos baseados em reticulado selecionados pelo NIST (Kyber e Dilithium) sejam aprovados para uso em Sistemas de Segurança Nacional (NSS).

*   **GCHQ (Government Communications Headquarters):** O GCHQ, a agência de inteligência e segurança do Reino Unido, também está ativamente envolvido na pesquisa e orientação sobre criptografia pós-quântica, alinhando-se em grande parte com as recomendações do NIST.

*   **Autores e Afiliações:** Os algoritmos Kyber e Dilithium foram desenvolvidos por uma equipe internacional de pesquisadores de várias instituições acadêmicas e do setor privado, incluindo:
    *   **CWI (Centrum Wiskunde & Informatica), Holanda**
    *   **Ruhr-Universität Bochum, Alemanha**
    *   **IBM Research - Zurich, Suíça**
    *   **ENS de Lyon, França**
    *   **Florida Atlantic University, EUA**
    *   **Google, EUA**
    *   **Max Planck Institute for Security and Privacy, Alemanha**

*   **NTRU:** O NTRU foi desenvolvido em 1996 por Jeffrey Hoffstein, Jill Pipher e Joseph H. Silverman, matemáticos da Brown University. Eles fundaram a NTRU Cryptosystems, Inc. para comercializar a tecnologia. A empresa e suas patentes foram posteriormente adquiridas por outras empresas de segurança.


---

## Relatório: 38_1aXtWIrJuLxDDzGLB1ijpQ_1766816531173_na1fn_L2hvbWUvdWJ1bnR1L2N5cGhlcnB1bmtfdGVjaG5pY2FsX3JlcG9ydA.md

## Relatório Técnico: Movimento Cypherpunk

### Sujeito

Movimento Cypherpunk - Manifesto, Timothy May, Eric Hughes, Mailing List, Privacidade

### Equações e Fórmulas

Nenhuma equação ou fórmula matemática explícita foi encontrada nos manifestos e documentos de alto nível pesquisados. Os conceitos são baseados em campos matemáticos complexos, mas não detalhados com notação específica nos textos fundadores.

### Variáveis e Parâmetros

*   **Chave Pública/Privada:** Em criptografia assimétrica, um par de chaves usado para criptografar e descriptografar dados. A chave pública é distribuída abertamente, enquanto a chave privada é mantida em segredo pelo proprietário.
*   **Nível de Criptografia (Forte vs. Fraca):** Refere-se à complexidade e ao tamanho da chave de um algoritmo criptográfico, determinando sua resistência a ataques de força bruta.
*   **Encadeamento de Remailers (Chain length):** O número de remailers intermediários usados para encaminhar uma mensagem, aumentando o anonimato.

### Algoritmos e Protocolos

1.  **Sistemas de Transação Anônima:**
    *   **Princípio:** Garantir que cada parte de uma transação tenha conhecimento apenas do que é estritamente necessário para aquela transação, desassociando a identidade da transação em si.
    *   **Implementação:** Uso de dinheiro eletrônico anônimo e assinaturas digitais para permitir a revelação seletiva da identidade.

2.  **Criptoanarquia (Baseado no Manifesto de Timothy C. May):**
    *   **Protocolo:** Utiliza uma combinação de criptografia de chave pública, sistemas de prova interativa de conhecimento zero e protocolos de software para interação, autenticação e verificação.
    *   **Roteamento Anônimo:** As interações na rede são tornadas não rastreáveis através do roteamento extensivo de pacotes criptografados e do uso de "caixas à prova de violação" (tamper-proof boxes) que implementam os protocolos criptográficos.

3.  **Remailer Anônimo Cypherpunk (Tipo I):**
    *   **Objetivo:** Ocultar o remetente de uma mensagem de e-mail.
    *   **Processo:**
        1.  O remetente formata uma mensagem para o remailer, incluindo o destinatário final (`Anon-To:`).
        2.  A mensagem é criptografada usando a chave pública PGP/GPG do remailer.
        3.  O remailer recebe a mensagem, a descriptografa com sua chave privada.
        4.  O remailer remove todos os cabeçalhos de identificação do remetente original (e.g., `From:`, `Reply-To:`).
        5.  A mensagem é então enviada ao destinatário final especificado no campo `Anon-To:`.
    *   **Encadeamento (Chaining):** Para maior segurança, as mensagens podem ser aninhadas e criptografadas em camadas para uma cadeia de remailers. Cada remailer na cadeia só pode descriptografar sua camada, ver o endereço do próximo remailer e encaminhar a mensagem. Apenas o último remailer vê o destinatário final.

### Vulnerabilidades e Fraquezas Conhecidas

*   **Análise de Tráfego:** A principal vulnerabilidade dos remailers Tipo I. Um adversário que monitora o tráfego de entrada e saída de um remailer pode correlacionar o tamanho e o tempo das mensagens para re-identificar o remetente. O encadeamento de remailers mitiga, mas não elimina completamente, esse risco.
*   **Ataques de Repetição (Replay Attacks):** Um adversário pode capturar uma mensagem criptografada e reenviá-la para o remailer para observar o comportamento e tentar extrair informações.
*   **Comprometimento do Servidor do Remailer:** Se um servidor de remailer for comprometido (seja por hackers ou por uma ordem judicial), os logs (se existirem) podem ser usados para quebrar o anonimato das mensagens que passam por ele.
*   **Vulnerabilidades de Implementação:** Falhas no software do remailer ou no PGP/GPG podem expor informações que deveriam ser anônimas.
*   **Mercados Abomináveis:** O próprio manifesto de Timothy May reconhece que a criptoanarquia poderia permitir mercados para atividades ilegais e imorais, como assassinatos e extorsão.

### Conexões Institucionais e Colaboradores

*   **Timothy C. May:** Intel (ex-cientista chefe), um dos fundadores da mailing list Cypherpunks.
*   **Eric Hughes:** Matemático da Universidade da Califórnia, Berkeley; autor do "A Cypherpunk's Manifesto"; criador de um dos primeiros remailers anônimos.
*   **John Gilmore:** Sun Microsystems (um dos primeiros funcionários); co-fundador da Electronic Frontier Foundation (EFF); figura central na mailing list Cypherpunks.
*   **Agências Governamentais (Adversários):** O movimento estava em conflito direto com agências como a National Security Agency (NSA) e o Federal Bureau of Investigation (FBI), principalmente durante as "Guerras Criptográficas" e a oposição à proposta do Clipper Chip.
*   **Corporações:** Vistas com desconfiança por coletarem dados dos usuários. A relação é de antagonismo, embora muitos Cypherpunks tivessem afiliações com empresas de tecnologia (como Intel e Sun Microsystems).


---

## Relatório: 39_1cdi4jYYSLRsHVcGX036rT_1766816678461_na1fn_L2hvbWUvdWJ1bnR1L25zYV9jcnlwdG8vcmVwb3J0.md

# Relatório Técnico: Criptografia da NSA

## Assunto

Criptografia da NSA: Suite A, Suite B, Dual_EC_DRBG, Backdoors e Curvas NIST

## Equações e Fórmulas (LaTeX)

s_k = g_P(s_{k-1});r_k = g_Q(s_k);y^2 = x^3 - 3x + b;X(x, y) = x;t(x) = x \pmod{2^{16}};g_P(x) = X(P^x);g_Q(x) = t(X(Q^x));s_1 = g_P(\text{seed});eQ = P

## Variáveis e Parâmetros

s: o estado interno do gerador;r: o número aleatório gerado;P, Q: pontos fixos na curva elíptica;p: o módulo primo do corpo finito;b: uma constante da curva elíptica;e: a chave secreta da NSA

## Algoritmos

### Suite B

- **AES (Advanced Encryption Standard)**: Criptografia simétrica de blocos com chaves de 128, 192 ou 256 bits. Usado com os modos de operação GCM ou CTR.
- **ECDSA (Elliptic Curve Digital Signature Algorithm)**: Algoritmo de assinatura digital que usa criptografia de curva elíptica. As curvas P-256 e P-384 são especificadas.
- **ECDH (Elliptic-curve Diffie–Hellman)**: Acordo de chaves baseado em curvas elípticas, usando as mesmas curvas que o ECDSA.
- **SHA-2 (Secure Hash Algorithm 2)**: Família de funções de hash criptográficas, especificamente SHA-256 e SHA-384.

### Dual_EC_DRBG (Dual Elliptic Curve Deterministic Random Bit Generator)

1. O estado interno `s` é atualizado a cada iteração: `s_k = g_P(s_{k-1})`.
2. O número aleatório `r` é gerado a partir do novo estado: `r_k = g_Q(s_k)`.
3. As funções `g_P` e `g_Q` envolvem a multiplicação de pontos na curva elíptica e a extração da coordenada x.

## Vulnerabilidades

### Dual_EC_DRBG

- **Backdoor Kleptográfico**: A principal vulnerabilidade é um backdoor deliberado. Se a relação entre os pontos P e Q da curva elíptica for conhecida (ou seja, se alguém souber o valor 'e' tal que eQ = P), é possível prever a saída do gerador a partir de uma pequena amostra de sua saída (32 bytes). A NSA é a principal suspeita de conhecer esse valor 'e' para as constantes padronizadas.
- **Viés e Previsibilidade**: Independentemente do backdoor, o algoritmo demonstrou ter um leve viés, não sendo perfeitamente aleatório. A pequena quantidade de truncamento na saída permite que um invasor, com conhecimento do backdoor, reverta o processo e determine o estado interno do gerador.
- **Constantes Suspeitas**: Os pontos P e Q usados no padrão não foram gerados de forma transparente (por exemplo, usando o princípio 'nothing up my sleeve'), levantando suspeitas de que foram escolhidos especificamente para permitir o backdoor.

### Curvas NIST

- **Geração de Sementes Opaca**: As sementes usadas para gerar as curvas padrão do NIST (como P-256, P-384) foram fornecidas pela NSA sem uma explicação transparente de como foram selecionadas. Isso levanta a preocupação de que as curvas possam conter fraquezas sutis que apenas a NSA pode explorar, embora nenhuma vulnerabilidade concreta tenha sido descoberta publicamente.

### Suite A

- **Segurança por Obscuridade**: Sendo um conjunto de algoritmos classificados e não públicos, sua segurança não pode ser verificada pela comunidade criptográfica em geral. A principal fraqueza é a falta de escrutínio público, o que contraria o princípio de Kerckhoffs.

## Conexões

NSA (National Security Agency), GCHQ (Government Communications Headquarters), NIST (National Institute of Standards and Technology), ANSI (American National Standards Institute), ISO (International Organization for Standardization), Certicom, RSA Security, BlackBerry Limited, Microsoft, Cisco, Juniper Networks


---

## Relatório: 3_uXn3rnrkhYN3CKDHg2upEu_1766816543294_na1fn_L2hvbWUvdWJ1bnR1L3JlbGF0b3Jpb19jaGF1bQ.md

# Relatório Técnico: David Chaum

## Equações e Fórmulas (LaTeX)

`m' \equiv mr^e \pmod{N}; s' \equiv (m')^d \pmod{N}; s \equiv s' \cdot r^{-1} \pmod{N}; s \equiv m^d \pmod{N}; c \equiv m^e \pmod{N}; s' \equiv c^d \equiv m \pmod{N}; K_b(R0, mensagem); K_m(R1, K_b(R0, mensagem), B); K_m(S1, A), K_x; K_m(S1, A), K_x(S0, resposta)`

## Variáveis e Parâmetros

*   **m**: mensagem original
*   **N**: módulo público RSA
*   **e**: expoente público RSA
*   **d**: expoente secreto RSA
*   **r**: fator de cegueira aleatório, relativamente primo a N
*   **m'**: mensagem cega
*   **s'**: assinatura cega
*   **s**: assinatura RSA válida de m
*   **c**: mensagem criptografada
*   **K_m**: Chave pública do Mix
*   **K_b**: Chave pública do destinatário B
*   **A, B**: Endereços do remetente e do destinatário
*   **R0, R1, S0, S1**: Strings aleatórias (nonces/sais) para prevenção de ataques
*   **K_x**: Chave pública de uso único para respostas anônimas
*   **Moeda (Coin)**: Um número de série único que representa um valor monetário no DigiCash
*   **Fator de Cegueira (Blinding Factor)**: Um número aleatório usado para cegar a moeda no DigiCash
*   **Chave Privada do Banco (Bank's Private Key)**: A chave usada pelo banco para assinar as moedas no DigiCash
*   **String de Identidade (Identity String)**: Uma string secreta embutida na moeda para detectar gasto duplo em cenários offline no DigiCash

## Algoritmos e Protocolos

### Assinatura Cega (Blind Signature)

O protocolo de assinatura cega RSA permite que uma entidade assine uma mensagem sem conhecer seu conteúdo. O processo envolve o "cegamento" da mensagem original `m` com um fator aleatório `r`, resultando em `m'`. A autoridade assina `m'`, produzindo `s'`. O autor da mensagem então remove o fator de cegueira para obter a assinatura final `s`, que é uma assinatura RSA válida para a mensagem original `m`.

### Redes Mix (Mix Networks)

O protocolo de redes mix visa o anonimato nas comunicações. As mensagens são criptografadas em camadas e enviadas através de uma série de servidores (mixes). Cada mix remove uma camada de criptografia, embaralha um lote de mensagens e as retransmite para o próximo destino. Isso quebra a ligação entre remetente e destinatário, dificultando a análise de tráfego. O protocolo também suporta endereços de retorno anônimos para permitir respostas sem revelar a identidade do remetente original.

### DigiCash/eCash

O sistema DigiCash implementou um protocolo de dinheiro eletrônico anônimo baseado em assinaturas cegas. Os principais protocolos são:

*   **Retirada (Withdrawal):** Um cliente gera uma "moeda" (número de série), a cega e a envia a um banco para assinatura. O banco debita a conta do cliente e retorna a moeda assinada.
*   **Pagamento (Payment):** O cliente entrega a moeda assinada a um comerciante, que a verifica junto ao banco.
*   **Depósito (Deposit):** O comerciante deposita a moeda no banco, que a credita e a registra como gasta para evitar o gasto duplo.
*   **Prevenção de Gasto Duplo:** Em sistemas online, o banco mantém um banco de dados de moedas gastas. Em sistemas offline, foram propostos mecanismos como "cut-and-choose" (para garantir a formação correta da moeda) e "challenge-response" (para identificar fraudadores que gastam a mesma moeda duas vezes).

## Vulnerabilidades e Fraquezas

*   **Ataque de Cegueira RSA:** A propriedade multiplicativa do RSA permite um ataque onde um adversário pode enganar um assinante para decifrar uma mensagem (ciphertext) ao pedi-lo para assinar uma versão cega dessa mensagem. Por isso, a mesma chave RSA não deve ser usada para criptografia e assinatura cega.
*   **Análise de Tráfego em Redes Mix:** Adversários que monitoram a entrada e saída de um mix podem realizar ataques de tempo (timing attacks) para correlacionar mensagens e comprometer o anonimato.
*   **Ataques Ativos e de Repetição em Redes Mix:** Invasores podem injetar suas próprias mensagens para perturbar a rede ou reenviar mensagens legítimas para obter informações.
*   **Comprometimento de Mixes:** Se todos os servidores em uma cadeia de mix forem comprometidos, o anonimato é completamente perdido.
*   **Centralização do DigiCash:** O sistema DigiCash dependia de um banco central, tornando-o um ponto único de falha e um alvo para ataques ou coerção legal.
*   **Dependência do RSA no DigiCash:** A segurança do sistema estava atrelada à segurança do algoritmo RSA, que poderia ser vulnerável a futuros ataques.

## Conexões e Colaboradores

*   **Institucionais:** David Chaum fundou a International Association for Cryptologic Research (IACR) e o grupo de criptografia no Center for Mathematics and Computer Science (CWI) em Amsterdã. Ele também lecionou na NYU Graduate School of Business e na University of California.
*   **Corporativas:** Fundou a DigiCash Inc. para comercializar suas ideias de dinheiro eletrônico. Mais recentemente, fundou a Elixxir e a xx.network.
*   **Governamentais:** O trabalho de Chaum sobre anonimato atraiu a atenção de agências governamentais. Um artigo de 1996 da National Security Agency (NSA), intitulado "How to Make a Mint: The Cryptography of Anonymous Electronic Cash", analisou sistemas de dinheiro eletrônico anônimo como o DigiCash, levantando preocupações sobre segurança e aplicação da lei.


---

## Relatório: 40_UUGyh0FHV5qiTJ5sDPbwTh_1766816636145_na1fn_L2hvbWUvdWJ1bnR1L3JlbGF0b3Jpb190ZWNuaWNv.md

# Relatório Técnico: Mineração de Bitcoin

## Equações e Fórmulas

### Ajuste de Dificuldade

**Fórmula da Dificuldade:**
```latex
difficulty = \frac{difficulty\_1\_target}{current\_target}
```

**Cálculo do Target (Exemplo):**
```latex
0x0404cb * 2^{(8 * (0x1b - 3))} = 0x00000000000404CB000000000000000000000000000000000000000000000000
```

**Taxa de Hash da Rede:**
```latex
Hash Rate = \frac{D * 2^{48}}{0xffff * 600}
```

**Taxa de Hash da Rede (Aproximada):**
```latex
Hash Rate \approx \frac{D * 2^{32}}{600}
```

### Recompensa por Bloco e Halving

**Fórmula de Fornecimento de Bitcoin (Halving):**
```latex
\sum_{i=0}^{32} \frac{50 * 210000}{2^i}
```

## Variáveis e Parâmetros

*   `difficulty`: O valor da dificuldade da rede.
*   `difficulty_1_target`: Um valor de referência que representa a dificuldade 1. Tradicionalmente, é um hash com os 32 bits iniciais sendo zero e o restante um.
*   `current_target`: O alvo de hash atual que os mineradores devem atingir.
*   `D`: A dificuldade.
*   `i`: O índice da época de halving, começando em 0.
*   `210000`: O número de blocos em cada época de halving.
*   `50`: A recompensa inicial de bloco em Bitcoin.
*   `2`: O fator pelo qual a recompensa do bloco é dividida a cada halving.

## Algoritmos e Protocolos

### Algoritmo de Ajuste de Dificuldade

A dificuldade da rede Bitcoin é ajustada a cada 2016 blocos (~2 semanas) para manter o tempo médio de geração de blocos em 10 minutos. Se o tempo para minerar os 2016 blocos for menor que duas semanas, a dificuldade aumenta; se for maior, a dificuldade diminui. O ajuste é proporcional ao desvio em relação ao tempo esperado.

### Algoritmo de Halving

A cada 210.000 blocos (~4 anos), a recompensa por bloco é reduzida pela metade. Este mecanismo controla a emissão de novos bitcoins, assegurando um fornecimento máximo de 21 milhões de unidades.

### Pools de Mineração

Pools de mineração são grupos de mineradores que combinam seu poder computacional (hashrate) para aumentar a probabilidade de encontrar um bloco. As recompensas são distribuídas proporcionalmente à contribuição de cada membro.

### Protocolo Stratum V2

O Stratum V2 é um protocolo de comunicação para mineração em pool que aprimora o Stratum original. Suas principais características técnicas são:

*   **Criptografia de ponta a ponta:** Protege a comunicação entre minerador e pool.
*   **Redução de latência e largura de banda:** Otimiza a transmissão de dados.
*   **Seleção de transações pelo minerador:** Permite que os mineradores escolham as transações a serem incluídas no bloco, aumentando a descentralização.

## Vulnerabilidades

### ASICs (Application-Specific Integrated Circuits)

*   **Antbleed:** Backdoor no firmware de mineradores Antminer da Bitmain que permitia o desligamento remoto dos dispositivos por um servidor centralizado.
*   **Backdoors de Hardware:** Possibilidade de inserção de backdoors nos chips durante a fabricação, permitindo controle ou acesso não autorizado.
*   **Vulnerabilidades de Firmware:** Firmware inseguro ou desatualizado pode ser explorado para injetar código malicioso ou controlar o hardware.
*   **Fraquezas de Segurança de Rede:** Configurações de rede inseguras (portas abertas, criptografia fraca) podem expor os mineradores a ataques.

### Pools de Mineração

*   **Centralização:** A concentração de hashrate em poucos pools aumenta o risco de conluio e ataques à rede.
*   **Ataques de 51%:** Uma entidade ou grupo que controle mais de 50% do hashrate da rede pode, teoricamente, executar ataques de gasto duplo e reorganizar a blockchain.
*   **Ataques de Negação de Serviço (DoS):** Pools de mineração são alvos potenciais de ataques DoS, que podem interromper suas operações.

## Conexões

*   **Bitmain:** Fabricante líder de ASICs (Antminer), esteve envolvida na controvérsia da vulnerabilidade "Antbleed", que demonstrou a capacidade de controle centralizado sobre uma grande porção do hashrate da rede Bitcoin.


---

## Relatório: 41_FgmoLdTw1ViSBlTirWHzoO_1766816943955_na1fn_L2hvbWUvdWJ1bnR1L3JlcG9ydA.md

# Relatório Técnico: Ethereum 2.0

## Equações e Fórmulas

$$base\_reward = effective\_balance \times \frac{base\_reward\_factor}{base\_rewards\_per\_epoch \times \sqrt{\sum active\_balance}}$$

## Variáveis e Parâmetros

| Variável | Definição |
|---|---|
| Slot | uint64 - um número de slot |
| Epoch | uint64 - um número de época |
| CommitteeIndex | uint64 - um índice de comitê em um slot |
| ValidatorIndex | uint64 - um índice de registro de validador |
| Gwei | uint64 - uma quantidade em Gwei |
| Root | Bytes32 - uma raiz Merkle |
| Hash32 | Bytes32 - um hash de 256 bits |
| Version | Bytes4 - um número de versão de fork |
| DomainType | Bytes4 - um tipo de domínio |
| ForkDigest | Bytes4 - um resumo dos dados do fork atual |
| Domain | Bytes32 - um domínio de assinatura |
| BLSPubkey | Bytes48 - uma chave pública BLS12-381 |
| BLSSignature | Bytes96 - uma assinatura BLS12-381 |
| UINT64_MAX | uint64(2**64 - 1) |
| UINT64_MAX_SQRT | uint64(4294967295) |
| GENESIS_SLOT | Slot(0) |
| GENESIS_EPOCH | Epoch(0) |
| FAR_FUTURE_EPOCH | Epoch(2**64 - 1) |
| BASE_REWARDS_PER_EPOCH | uint64(4) |
| DEPOSIT_CONTRACT_TREE_DEPTH | uint64(32) |
| JUSTIFICATION_BITS_LENGTH | uint64(4) |
| ENDIANNESS | 'little' |
| BLS_WITHDRAWAL_PREFIX | Bytes1('0x00') |
| ETH1_ADDRESS_WITHDRAWAL_PREFIX | Bytes1('0x01') |
| DOMAIN_BEACON_PROPOSER | DomainType('0x00000000') |
| DOMAIN_BEACON_ATTESTER | DomainType('0x01000000') |
| DOMAIN_RANDAO | DomainType('0x02000000') |
| DOMAIN_DEPOSIT | DomainType('0x03000000') |
| DOMAIN_VOLUNTARY_EXIT | DomainType('0x04000000') |
| DOMAIN_SELECTION_PROOF | DomainType('0x05000000') |
| DOMAIN_AGGREGATE_AND_PROOF | DomainType('0x06000000') |
| DOMAIN_APPLICATION_MASK | DomainType('0x00000001') |
| ParticipationFlags | uint8 - uma representação sucinta de 8 flags de participação booleanas |
| TIMELY_SOURCE_FLAG_INDEX | 0 |
| TIMELY_TARGET_FLAG_INDEX | 1 |
| TIMELY_HEAD_FLAG_INDEX | 2 |
| TIMELY_SOURCE_WEIGHT | uint64(14) |
| TIMELY_TARGET_WEIGHT | uint64(26) |
| TIMELY_HEAD_WEIGHT | uint64(14) |
| SYNC_REWARD_WEIGHT | uint64(2) |
| PROPOSER_WEIGHT | uint64(8) |
| WEIGHT_DENOMINATOR | uint64(64) |
| DOMAIN_SYNC_COMMITTEE | DomainType('0x07000000') |
| DOMAIN_SYNC_COMMITTEE_SELECTION_PROOF | DomainType('0x08000000') |
| DOMAIN_CONTRIBUTION_AND_PROOF | DomainType('0x09000000') |
| PARTICIPATION_FLAG_WEIGHTS | [TIMELY_SOURCE_WEIGHT, TIMELY_TARGET_WEIGHT, TIMELY_HEAD_WEIGHT] |
| INACTIVITY_PENALTY_QUOTIENT_ALTAIR | uint64(50331648) |
| MIN_SLASHING_PENALTY_QUOTIENT_ALTAIR | uint64(64) |
| PROPORTIONAL_SLASHING_MULTIPLIER_ALTAIR | uint64(2) |
| SYNC_COMMITTEE_SIZE | uint64(512) |
| EPOCHS_PER_SYNC_COMMITTEE_PERIOD | uint64(256) |
| INACTIVITY_SCORE_BIAS | uint64(4) |
| INACTIVITY_SCORE_RECOVERY_RATE | uint64(16) |
| Transaction | ByteList[MAX_BYTES_PER_TRANSACTION] - uma transação |
| ExecutionAddress | Bytes20 - Endereço de conta na camada de execução |
| INACTIVITY_PENALTY_QUOTIENT_BELLATRIX | uint64(16777216) |
| MIN_SLASHING_PENALTY_QUOTIENT_BELLATRIX | uint64(32) |
| PROPORTIONAL_SLASHING_MULTIPLIER_BELLATRIX | uint64(3) |
| MAX_BYTES_PER_TRANSACTION | uint64(1073741824) |
| MAX_TRANSACTIONS_PER_PAYLOAD | uint64(1048576) |
| BYTES_PER_LOGS_BLOOM | uint64(256) |
| MAX_EXTRA_DATA_BYTES | 32 |
| TERMINAL_TOTAL_DIFFICULTY | 58750000000000000000000 |
| TERMINAL_BLOCK_HASH | Hash32() |
| TERMINAL_BLOCK_HASH_ACTIVATION_EPOCH | FAR_FUTURE_EPOCH |

## Algoritmos

O Ethereum 2.0 emprega uma variedade de algoritmos para gerenciar o consenso e a operação da beacon chain. Funções como `get_block_root`, `get_randao_mix`, e `get_seed` são fundamentais para a segurança e a aleatoriedade da rede. A seleção de validadores e a formação de comitês são gerenciadas por `get_active_validator_indices`, `get_validator_churn_limit`, `get_committee_count_per_slot`, e `get_beacon_committee`. A proposição de blocos é determinada por `get_beacon_proposer_index`.

A economia da rede é governada por algoritmos que calculam recompensas e penalidades. `get_base_reward` estabelece a recompensa fundamental, enquanto `get_proposer_reward` define a recompensa para os propositores de bloco. As penalidades por inatividade e outros comportamentos maliciosos são calculadas por `get_finality_delay`, `is_in_inactivity_leak`, e `get_inactivity_penalty_deltas`. A distribuição de recompensas e penalidades é realizada por `process_rewards_and_penalties`.

O ciclo de vida de um validador é gerenciado por `initiate_validator_exit` e `slash_validator`. A adição de novos validadores é tratada por `get_validator_from_deposit`, `add_validator_to_registry`, e `apply_deposit`. O processamento de blocos e suas operações são realizados por `process_block_header`, `process_randao`, `process_eth1_data`, `process_proposer_slashing`, `process_attester_slashing`, e `process_attestation`.

Com a introdução do Altair, novos algoritmos foram adicionados para suportar comitês de sincronização e reformas de incentivo, como `get_next_sync_committee`, `process_sync_aggregate`, e `process_participation_flag_updates`. O Bellatrix introduziu a execução de transações, com algoritmos como `is_merge_transition_complete`, `process_execution_payload`, e `verify_and_notify_new_payload`.

## Vulnerabilidades

O Ethereum 2.0, apesar de seu design robusto, apresenta algumas vulnerabilidades conhecidas. A **reorganização de blocos** é uma preocupação, com a rede comunitária sendo mais suscetível a ataques de reorganização em comparação com uma rede hierárquica. O **sistema de proposição de blocos** introduz um risco de vazamento de informações, uma vez que o proponente do bloco pode ser identificado antes da proposição, abrindo vetores de ataque. O **sistema de mensagens P2P** é vulnerável a spam e ataques de negação de serviço (DoS), que podem degradar o desempenho da rede.

A **centralização de validadores** é outra vulnerabilidade crítica, com um pequeno número de entidades controlando uma porcentagem significativa dos nós validadores, o que pode levar a conluios e ataques à rede. Finalmente, **ataques de roteamento** como StakeBleed e KnockBlock representam ameaças ao protocolo Proof-of-Stake, explorando a topologia da rede para isolar validadores ou atrasar a propagação de blocos.

## Conexões Institucionais

O Ethereum 2.0 atraiu o interesse de várias entidades institucionais e governamentais. O **Governo dos EUA** demonstrou uma abordagem estratégica, acumulando Ethereum por meio da apreensão de ativos de crimes cibernéticos e utilizando o staking para gerar rendimento. No setor privado, a **BitMine Immersion** realizou uma aquisição significativa de $20 bilhões em Ethereum, sinalizando uma forte confiança institucional no futuro da plataforma. Além disso, empresas de tecnologia como a **Coralogix** estão integrando o Ethereum em suas operações, utilizando-o em seu agente de IA, Olly, e em ferramentas de nível empresarial. O ecossistema de capital de risco também está ativamente envolvido, com empresas como **NewView Capital** e **CPPIB** liderando rodadas de financiamento para empresas que constroem sobre o Ethereum.



---

## Relatório: 42_eT6tFzSYZocnC08QkcjjkJ_1766816683702_na1fn_L2hvbWUvdWJ1bnR1L3JlbGF0b3Jpb190ZWNuaWNvX2RlZmk.md

# Relatório Técnico sobre Protocolos DeFi

## Equações e Fórmulas

- **Fórmula de Produto Constante (AMM):** `x*y=k`
- **Fórmula de Soma Constante (AMM):** `x+y=k`
- **Fórmula de Média Constante (AMM):** `∏(x_i)^(w_i) = k`
- **Taxa de Câmbio (Compound):** `oneCTokenInUnderlying = exchangeRateCurrent / (1 * 10 ^ (18 + underlyingDecimals - cTokenDecimals))`
- **APY (Compound):** `APY = ((((Rate / ETH Mantissa * Blocks Per Day + 1) ^ Days Per Year)) - 1) * 100`
- **APR (Compound):** `APR = supplyRatePerBlock / ethMantissa * blocksPerYear * 100`
- **Taxa de Utilização (Aave):** `UtilizationRate(U) = TotalBorrows / (TotalLiquidity + TotalBorrows)`
- **Taxa de Empréstimo (Aave, U <= Uoptimal):** `BorrowRate = BaseRate + (Utilization / Uoptimal) * Slope1`
- **Taxa de Empréstimo (Aave, U > Uoptimal):** `BorrowRate = BaseRate + Slope1 + ((Utilization - Uoptimal) / (1 - Uoptimal)) * Slope2`
- **Taxa de Fornecimento (Aave):** `SupplyRate = BorrowRate * Utilization * (1 - ReserveFactor)`
- **APR (Yield Farming):** `APR = (interest_rate / 100) * investment_capital`
- **APY (Yield Farming):** `APY = (1 + r/n)^n - 1`

## Variáveis e Parâmetros

- `x`: quantidade de um token no pool de liquidez
- `y`: quantidade do outro token no pool de liquidez
- `k`: um valor constante
- `x_i`: a quantidade de cada token no pool
- `w_i`: o peso de cada token
- `exchangeRateCurrent`: a taxa de câmbio atual do cToken
- `underlyingDecimals`: o número de casas decimais do ativo subjacente
- `cTokenDecimals`: o número de casas decimais do cToken (sempre 8)
- `Rate`: a taxa de oferta ou empréstimo por bloco (`supplyRatePerBlock` ou `borrowRatePerBlock`)
- `ETH Mantissa`: `1 * 10 ^ 18`
- `Blocks Per Day`: número de blocos por dia (aproximadamente 7200)
- `Days Per Year`: número de dias por ano (365)
- `blocksPerYear`: número de blocos por ano
- `TotalBorrows`: o valor total emprestado
- `TotalLiquidity`: a liquidez total disponível
- `Uoptimal`: a taxa de utilização ótima
- `BaseRate`: a taxa de juros base
- `Slope1`: o primeiro coeficiente de inclinação da curva de juros
- `Slope2`: o segundo coeficiente de inclinação da curva de juros
- `ReserveFactor`: o fator de reserva do protocolo
- `r`: a taxa de juros
- `n`: o número de vezes que o juro é composto por ano

## Algoritmos

- **AMM (Automated Market Maker):** Utiliza fórmulas matemáticas para precificar ativos em pools de liquidez. Os principais tipos incluem a Fórmula de Produto Constante, a Fórmula de Soma Constante e a Fórmula de Média Constante. Outras variações incluem Modelos de Função Híbrida, Criadores de Mercado Automatizados Dinâmicos (DAMM) e Liquidez Concentrada.
- **Compound:** Um protocolo de empréstimo que utiliza cTokens para representar os ativos fornecidos. As taxas de juros são calculadas com base na oferta e demanda de cada mercado.
- **Aave:** Um protocolo de liquidez não custodial onde os usuários podem participar como fornecedores ou mutuários. As taxas de juros são determinadas algoritmicamente com base na taxa de utilização do pool.
- **Yield Farming:** Uma estratégia que envolve o fornecimento de liquidez a protocolos DeFi em troca de recompensas, geralmente na forma de tokens de governança. Os retornos são calculados usando APR (Taxa de Porcentagem Anual) e APY (Rendimento Percentual Anual).

## Vulnerabilidades

- **Ataques de Flash Loan:** Empréstimos de grandes quantias sem garantia dentro de uma única transação para manipular os preços dos ativos.
- **Manipulação de Oráculo:** Se um AMM depende de um único ou manipulável oráculo para feeds de preços, os atacantes podem distorcer os preços inundando o mercado com negociações.
- **Reentrada:** Uma vulnerabilidade que permite que um contrato malicioso chame repetidamente uma função em outro contrato antes que a primeira chamada seja concluída, potencialmente drenando fundos.
- **Overflows e Underflows de Inteiros:** Erros de arredondamento de precisão e problemas de invariantes na lógica do contrato inteligente.
- **Problemas de Controle de Acesso:** Falhas na verificação de permissões, permitindo que usuários não autorizados executem ações privilegiadas.
- **Atualizações Maliciosas de Contratos (Hooks):** A capacidade de modificar arbitrariamente a lógica de um contrato após a implantação, introduzindo novas vulnerabilidades de segurança.

## Conexões

- **Uniswap:** Fireblocks, Revolut, Talos, Ledger, Robinhood, MoonPay, Transak
- **Compound Labs:** a16z, Paradigm, Coinbase Ventures, Bain Capital, Polychain Capital, Dragonfly Capital, NodeRise Capital, Davoa Capital


---

## Relatório: 44_59ynUM6miTZXq0WBbuKslt_1766816830437_na1fn_L2hvbWUvdWJ1bnR1L3RlY2huaWNhbF9yZXBvcnQ.md

## Equações e Fórmulas Matemáticas

- **Compromisso KZG:** $C = [p(s)]_1$
- **Verificação de Prova KZG:** $e(\pi, [Z(s)]_2) = e(C - [I(s)]_1, H)$
- **Fórmula de Redução FRI:** $Q(x) = (P(x) + P(\gamma x))/2$

## Variáveis e Parâmetros

- `C`: Compromisso com o polinômio `p(X)`
- `p(X)`: Um polinômio
- `s`: Um valor secreto
- `[x]_1`: `xG` onde `G` é um gerador do grupo `G_1`
- `[x]_2`: `xH` onde `H` é um gerador do grupo `G_2`
- `e`: Uma função de emparelhamento
- `\pi`: Uma prova
- `Z(X)`: Um polinômio quociente
- `I(X)`: Um polinômio de interpolação
- `Q(x)`: Um polinômio reduzido no protocolo FRI
- `P(x)`: O polinômio original no protocolo FRI
- `\gamma`: Um valor aleatório no protocolo FRI

## Algoritmos e Protocolos Técnicos

### ZK-Rollups

1.  Um usuário assina uma transação e a submete ao ZK-Rollup.
2.  A transação é incluída em um lote e agregada off-chain.
3.  Uma prova de conhecimento zero (zero-knowledge proof) que verifica todas as transações no rollup é postada na mainnet da Ethereum, juntamente com as transações agrupadas como `calldata`.
4.  A prova é armazenada permanentemente no histórico da Ethereum.

### Optimistic Rollups

1.  Um usuário assina uma transação e a submete ao sistema operacional do Optimistic Rollup.
2.  A transação é incluída em um lote e agregada off-chain.
3.  As transações são postadas na mainnet da Ethereum como `calldata`.
4.  Se um usuário provar que uma transação está incorreta (através de uma "prova de fraude" ou "fraud proof"), o rollup reverte a transação.
5.  Se a transação for válida, os dados são armazenados permanentemente no histórico da Ethereum.

### State Channels

1.  **Abertura do Canal:** As partes bloqueiam fundos em um contrato inteligente na blockchain principal.
2.  **Transações Off-Chain:** Os participantes realizam transações entre si, atualizando o estado do canal e assinando as atualizações.
3.  **Fechamento do Canal:** O estado final é submetido à blockchain principal, que atualiza os saldos e libera os fundos.

### Sidechains

1.  **Two-Way Peg:** Ativos são bloqueados na cadeia principal, e uma quantidade equivalente é emitida na sidechain.
2.  **Operação Independente:** A sidechain opera com seu próprio mecanismo de consenso e regras.
3.  **Sincronização:** A sidechain se comunica periodicamente com a cadeia principal para sincronizar o estado.

## Vulnerabilidades e Fraquezas Conhecidas

### ZK-Rollups

*   **Complexidade Criptográfica:** A criptografia subjacente é complexa, cara e difícil de implementar.
*   **Manutenção Especializada:** Requer conhecimento técnico avançado para implantação e manutenção.

### Optimistic Rollups

*   **Longos Períodos de Retirada:** Os usuários enfrentam atrasos ao retirar fundos devido ao período de contestação de fraude.

### State Channels

*   **Complexidade:** A configuração e o gerenciamento de canais são complexos.
*   **Risco de Contraparte:** A segurança depende da honestidade dos participantes ou de um mecanismo de resolução de disputas.
*   **Capacidade do Canal:** A quantidade de fundos que pode ser transacionada é limitada aos fundos bloqueados.

### Sidechains

*   **Riscos de Segurança:** A segurança da sidechain é independente da cadeia principal e pode ser mais fraca.
*   **Complexidade:** A interoperabilidade entre a cadeia principal e a sidechain adiciona complexidade.
*   **Problemas de Interoperabilidade:** Garantir uma comunicação segura e confiável entre as cadeias é um desafio.

## Conexões Institucionais

Nenhuma conexão direta com governos, corporações ou agâncias de inteligância foi identificada durante a pesquisa.


---

## Relatório: 45_bnztyW42zn4aQRD7wHAclv_1766816677805_na1fn_L2hvbWUvdWJ1bnR1L3JlcG9ydA.md

_Subjeito: Cryptocurrency exchanges - order books, matching engines, custody, hot/cold wallets_

**Equações e Fórmulas**

N/A

**Variáveis e Parâmetros**

*   `price`: O preço de uma ordem.
*   `time`: O momento em que uma ordem é colocada.
*   `size`: O tamanho de uma ordem.
*   `bid`: Uma ordem de compra.
*   `ask`: Uma ordem de venda.
*   `spread`: A diferença entre o melhor `bid` e o melhor `ask`.

**Algoritmos**

*   **First-In-First-Out (FIFO):** As ordens são executadas na ordem em que são recebidas. As ordens mais antigas em um determinado nível de preço são preenchidas primeiro.
*   **Pro-Rata:** A execução da ordem é baseada no tamanho da ordem. Ordens maiores recebem uma parcela maior das negociações disponíveis.
*   **Price-Time Priority (PTP):** As ordens com o melhor preço são executadas primeiro. Para ordens com o mesmo preço, as mais antigas são executadas primeiro.
*   **Partially Signed Bitcoin Transaction (PSBT):** Um protocolo de assinatura offline para transações de Bitcoin.

**Vulnerabilidades**

*   **Matching Engines:**
    *   Volatilidade de Preços
    *   Alto Volume de Ordens
    *   Congestionamento da Rede
    *   Manipulação de Mercado (spoofing, wash trading)
*   **Hot Wallets:**
    *   Superfície de Vulnerabilidade (sempre online)
    *   Irreversibilidade de transações maliciosas
*   **Cold Wallets:**
    *   Fricção Operacional (acesso lento)
    *   Complexidade (risco de roubo, perda ou dano físico)

**Conexões**

Nenhuma conexão direta com governos, corporações ou agências de inteligência foi identificada durante esta pesquisa.


---

## Relatório: 46_52AiBiImnLKdpTRkA2oeoe_1766816836509_na1fn_L2hvbWUvdWJ1bnR1L2ZpbmFsX3JlcG9ydA.md

# Relatório Técnico: Criptografia de Carteira - HD Wallets, BIP32, BIP39

## 1. Equações e Fórmulas (LaTeX)

- `CS = ENT / 32`
- `MS = (ENT + CS) / 11`
- `PBKDF2(password, salt, iterations, keylength, prf)`
- `I = HMAC-SHA512(Key = c_{par}, Data = 0x00 \|\| ser_{256}(k_{par}) \|\| ser_{32}(i))`
- `I = HMAC-SHA512(Key = c_{par}, Data = ser_{P}(point(k_{par})) \|\| ser_{32}(i))`
- `k_{i} = parse_{256}(I_{L}) + k_{par} \pmod{n}`
- `I = HMAC-SHA512(Key = c_{par}, Data = ser_{P}(K_{par}) \|\| ser_{32}(i))`
- `K_{i} = point(parse_{256}(I_{L})) + K_{par}`
- `K = point(k)`
- `I = HMAC-SHA512(Key = \text{"Bitcoin seed"}, Data = S)`

## 2. Variáveis e Parâmetros

- **ENT**: Comprimento da entropia inicial em bits (128, 160, 192, 224 ou 256).
- **CS**: Comprimento do checksum em bits.
- **MS**: Comprimento da sentença mnemônica em palavras.
- **password**: Sentença mnemônica em formato UTF-8 NFKD.
- **salt**: A string "mnemonic" + passphrase em formato UTF-8 NFKD.
- **iterations**: 2048.
- **keylength**: 512 bits (64 bytes).
- **prf**: HMAC-SHA512.
- **k**: Chave privada.
- **c**: Código da cadeia (chain code).
- **K**: Chave pública.
- **i**: Índice da chave filha (0 a 2^31 - 1 para normal, 2^31 a 2^32 - 1 para endurecida).
- **iH**: Notação para índice de chave filha endurecida (i + 2^31).
- **I**: Saída de 512 bits do HMAC-SHA512.
- **IL**: 32 bytes à esquerda de I.
- **IR**: 32 bytes à direita de I.
- **kpar**: Chave privada pai.
- **cpar**: Código da cadeia pai.
- **Kpar**: Chave pública pai.
- **ki**: Chave privada filha.
- **ci**: Código da cadeia filho.
- **Ki**: Chave pública filha.
- **n**: Ordem da curva secp256k1.
- **S**: Semente em bytes (comprimento entre 128 e 512 bits).

## 3. Algoritmos e Protocolos

### BIP39: Geração de Mnemônico

1.  Gera-se uma entropia inicial (`ENT`).
2.  Calcula-se um checksum (`CS`) aplicando SHA256 na entropia e pegando os primeiros `ENT / 32` bits.
3.  A entropia e o checksum são concatenados.
4.  A sequência de bits resultante é dividida em grupos de 11 bits.
5.  Cada grupo de 11 bits é mapeado para uma palavra em uma lista pré-definida de 2048 palavras.
6.  As palavras resultantes formam a sentença mnemônica.

### BIP39: Geração de Semente a partir do Mnemônico

1.  A função PBKDF2 é utilizada com a sentença mnemônica como senha e a string "mnemonic" + passphrase como salt.
2.  A função de pseudo-aleatoriedade é HMAC-SHA512, com 2048 iterações.
3.  A saída é uma semente de 512 bits, que serve de entrada para o BIP32.

### BIP32: Geração de Chave Mestra

1.  A partir de uma semente `S`, calcula-se `I = HMAC-SHA512(Key = "Bitcoin seed", Data = S)`.
2.  `I` é dividido em duas metades de 32 bytes: `IL` e `IR`.
3.  A chave privada mestra é `parse256(IL)` e o código da cadeia mestro é `IR`.

### BIP32: Derivação de Chave Filha (CKD)

- **Privada Pai -> Privada Filha:** Para uma chave pai `(kpar, cpar)` e um índice `i`, calcula-se `I` usando HMAC-SHA512. Para chaves endurecidas (`i >= 2^31`), a entrada de dados inclui a chave privada pai. Para chaves normais, inclui a chave pública pai. A chave filha `ki` é a soma da parte esquerda de `I` com a chave pai (mod n), e o novo código de cadeia `ci` é a parte direita de `I`.
- **Pública Pai -> Pública Filha:** O processo é análogo, mas só funciona para chaves não endurecidas e deriva apenas a chave pública filha `Ki` e o código de cadeia `ci`.

## 4. Vulnerabilidades e Fraquezas

- **Vazamento de Chave Privada Pai (BIP32):** A posse de uma chave pública estendida e de qualquer chave privada filha não endurecida permite a derivação da chave privada pai, comprometendo toda a hierarquia de chaves abaixo dela. O uso de derivação endurecida (`hardened derivation`) nos níveis superiores da hierarquia (ex: nível de conta) mitiga este risco.
- **Falta de Versionamento (BIP39):** O padrão BIP39 não inclui um número de versão, o que pode causar problemas de compatibilidade entre diferentes implementações de carteira e dificultar a recuperação de fundos se a carteira original não estiver disponível.
- **Negação Plausível Fraca (BIP39):** A funcionalidade de "passphrase" para criar carteiras ocultas oferece uma forma de negação plausível, mas é considerada fraca contra ataques de coerção física ou de baixo custo (ataque de US$ 5), pois um atacante pode facilmente inferir a existência de múltiplas carteiras.
- **Armazenamento Inseguro:** Implementações de carteiras podem armazenar a frase de semente ou chaves privadas em texto claro em locais inseguros, como arquivos de log ou o armazenamento local do navegador, expondo-as a malwares e atacantes.
- **Fraquezas de Entropia (BIP39):** Existem preocupações sobre a qualidade da entropia gerada por algumas carteiras e a possibilidade de fraquezas estatísticas na distribuição das palavras, o que poderia, em teoria, tornar certas frases de semente mais suscetíveis a ataques de força bruta.
- **Ataques de Força Bruta e Adivinhação:** Frases de semente com baixa entropia (12 palavras) ou passphrases fracas são vulneráveis a ataques de força bruta, especialmente com o avanço do poder computacional.

## 5. Conexões e Colaboradores

- **Pieter Wuille (BIP32):** Desenvolvedor do Bitcoin Core, afiliado à Blockstream.
- **Marek Palatinus (BIP39):** Co-fundador da SatoshiLabs (Trezor).
- **Pavol Rusnak (BIP39):** Co-fundador da SatoshiLabs (Trezor).
- **Aaron Voisine (BIP39):** Fundador da Breadwallet (BRD).
- **Sean Bowe (BIP39):** Engenheiro de criptografia, afiliado à Zcash Foundation.


---

## Relatório: 47_mx8o34JbRy9RRoUVxbIinV_1766816878811_na1fn_L2hvbWUvdWJ1bnR1L3RlY2huaWNhbF9yZXBvcnQ.md


## Equações e Fórmulas

```latex
pk := g^{sk}; pk_i := g^{sk_i}; f(x) = s + a_1*x + ... + a_t*x^t; sk := \sum_{j \in T} s_j;
```

## Variáveis e Parâmetros

λ: parâmetro de segurança; X: um conjunto; x: um elemento amostrado uniformemente ao acaso de X; n: número de partes na rede; P: conjunto de n partes {P1, ..., Pn}; A: um adversário bizantino; t: número de partes corrompidas; ∆: atraso de rede em uma rede síncrona; v: valor de entrada; V: conjunto de valores; val: função de validade externa; s: segredo; f(x): um polinômio usado para compartilhamento de segredos; sk: chave secreta; pk: chave pública; ski: compartilhamento da chave secreta da parte i; Y: tupla de compartilhamentos de chave pública (pk1, ..., pkn);

## Algoritmos

Protocolo DKG Síncrono de Pedersen; Protocolo DKG Síncrono Seguro de Gennaro et al.; Protocolo DKG Síncrono de Fouque-Stern; Protocolo DKG Síncrono de Canny-Sorkin; Protocolo ADKG de Kokoris-Kogias, Malkhi e Spiegelman; Protocolo ADKG de Das et al.; Protocolo ADKG de Abraham et al.; Protocolo ADKG de Gao et al.; Protocolo ADKG de Feng et al.

## Vulnerabilidades

Insegurança do DKG de Pedersen original devido à manipulação por um adversário apressado; Impossibilidade de um DKG de uma rodada totalmente seguro; Protocolos ADKG com custo de comunicação quase quadrático dependem de rasuras seguras para segurança adaptativa, o que é indesejável na prática.

## Conexões

CISPA Helmholtz Center for Information Security, Saarland University, University College London, Georgetown University, Bipartisan Policy Center, European Data Protection Supervisor, IEEE, NTT, NSA


---

## Relatório: 48_wdFrxkW6Dd6iFt7c7tFWYp_1766816869126_na1fn_L2hvbWUvdWJ1bnR1L3RlY2huaWNhbF9yZXBvcnQ.md


## Equações e Fórmulas

```latex
F_{SK}(x) = g^{1/(z+SK)}; p_{SK}(x) = g^{1/(z+SK)}; e(g,g)^{1/(z+SK)} = e(g, p_{SK}(x)); e(g^z, g^{SK}) \cdot e(g,g)^{1/(z+SK)} = e(g,g)
```

## Variáveis e Parâmetros

*   `F_SK(x)`: Função VRF com chave secreta SK e entrada x
*   `p_SK(x)`: Prova para a avaliação da VRF
*   `g`: Gerador de um grupo cíclico
*   `z`: Valor derivado da entrada x
*   `SK`: Chave secreta
*   `e(·,·)`: Mapa bilinear
## Algoritmos

*   **RSA-FDH-VRF**: Uma construção de VRF baseada no RSA Full Domain Hash. Esta construção utiliza a função hash de domínio completo para fornecer uma prova da correção do hash. A segurança deste esquema baseia-se na dificuldade do problema RSA.

*   **ECVRF**: Uma construção de VRF baseada em Curvas Elípticas. Esta construção aproveita as propriedades das curvas elípticas para criar uma VRF eficiente e segura. A segurança do ECVRF depende da dificuldade do problema do logaritmo discreto em curvas elípticas.

## Vulnerabilidades

*   **Ataques de pré-imagem**: As VRFs fornecem pré-compromissos determinísticos para entradas de baixa entropia, que devem ser resistentes a ataques de pré-imagem de força bruta.

*   **Ataques de enumeração offline (ataques de dicionário)**: As VRFs podem ser usadas para defesa contra ataques de enumeração offline em dados armazenados em estruturas de dados baseadas em hash.

*   **Enumeração de zona no DNSSEC**: O sistema NSEC5 proposto, que usa VRFs, comprovadamente impede esse tipo de ataque.

## Conexões

*   Silvio Micali (MIT)
*   Michael Rabin (Harvard University)
*   Salil Vadhan (MIT)
*   Sharon Goldberg (Boston University)
*   Leonid Reyzin (Boston University, Algorand)
*   Dimitrios Papadopoulos (Hong Kong University of Science and Technology)
*   Jan Včelák (NS1)
*   IETF (Internet Engineering Task Force)
*   IRTF (Internet Research Task Force)
*   CFRG (Crypto Forum Research Group)
*   DARPA
*   NSF


---

## Relatório: 49_vXK57IRiTRQucsVUBRQJx3_1766816939310_na1fn_L2hvbWUvdWJ1bnR1L2Jsb2NrY2hhaW5fc2NhbGFiaWxpdHkvcmVwb3J0.md

# Relatório Técnico sobre Escalabilidade de Blockchain

## Transações por Segundo (TPS)

### Fórmulas

`TPS = (tamanho do bloco / tamanho da transação) / tempo do bloco`

### Variáveis

*   **tamanho do bloco**: A quantidade de dados de transação que um bloco pode armazenar.
*   **tamanho da transação**: Varia entre 226 bytes e 500 bytes.
*   **tempo do bloco**: O tempo médio necessário para confirmar uma transação em uma rede.

## Tamanho do Bloco

### Algoritmos

O tamanho de bloco ideal pode ser determinado usando algoritmos meta-heurísticos, como otimização por enxame de partículas (PSO) e o algoritmo evolucionário de força de Pareto (SPEA), para encontrar o número ideal de transações em cada bloco. A pesquisa "Computing Optimal Block Size for Blockchain based Applications with Contradictory Objectives" sugere que um tamanho de bloco de 255 Kbytes, contendo 213 transações (com um tamanho médio de transação de 1.2 Kb), é o ideal para larguras de banda de rede de mineradores entre 250 kbps e 1200 kbps, pois minimiza o tempo de transmissão e composição do bloco.

### Vulnerabilidades

*   **Aumento do tempo de propagação:** Blocos maiores levam mais tempo para se propagar pela rede, o que pode levar a uma maior taxa de blocos órfãos e forks na blockchain.
*   **Centralização da mineração:** Requisitos de hardware e largura de banda mais altos para processar blocos maiores podem levar à centralização da mineração, pois apenas os mineradores com recursos suficientes podem participar.
*   **State Bloat:** Blocos maiores contribuem para o crescimento mais rápido do estado da blockchain, tornando mais difícil para novos nós sincronizarem com a rede.

## Sharding

### Algoritmos

O sharding é uma técnica de particionamento de banco de dados que divide uma rede blockchain em segmentos menores e mais gerenciáveis chamados "shards". Cada shard possui seus próprios dados, tornando-o distinto e independente. Essa abordagem permite o processamento paralelo de transações, melhorando a escalabilidade. A divisão pode ser baseada em características, como o tipo de ativo digital ou o endereço da transação. Embora os shards sejam independentes, eles ainda podem compartilhar informações entre si para manter a integridade do livro-razão descentralizado.

### Vulnerabilidades

*   **Ataque de controle de shard (1%):** Um invasor pode se concentrar em controlar um único shard com uma fração do poder de hash total da rede, potencialmente introduzindo transações maliciosas nesse shard.
*   **Complexidade de comunicação entre shards:** A comunicação e a coordenação entre shards para transações que afetam vários shards podem ser complexas e introduzir novas vulnerabilidades se não forem projetadas corretamente.

## State Bloat e Pruning

### State Bloat

O State Bloat refere-se ao crescimento do conjunto de dados do estado da blockchain, que inclui todas as contas, saldos, contratos inteligentes e armazenamento. À medida que a rede é usada, o estado cresce, exigindo mais espaço de armazenamento, recursos computacionais para processar e largura de banda para transmitir. Isso pode tornar a execução de um nó completo mais cara e demorada, levando à centralização.

### Pruning

O Pruning (poda) é uma técnica para reduzir o tamanho da blockchain armazenada em um nó, removendo dados históricos desnecessários. Por exemplo, um nó pode descartar os detalhes de transações de blocos antigos, mantendo apenas os cabeçalhos dos blocos e o estado mais recente. Isso reduz significativamente os requisitos de armazenamento para executar um nó, tornando a rede mais acessível e descentralizada.

#### Algoritmos de Pruning

*   **Pruning baseado em idade:** Remove blocos e transações mais antigos que um determinado limite de idade.
*   **Pruning baseado em tamanho:** Mantém um tamanho máximo para a blockchain, descartando os dados mais antigos quando o limite é atingido.
*   **Pruning seletivo:** Permite que os nós escolham quais dados históricos descartar com base em predicados ou regras específicas.

### Vulnerabilidades

*   **Perda de dados históricos:** Se todos os nós da rede podarem seus dados, os dados históricos podem ser perdidos para sempre, a menos que sejam arquivados por alguns nós.
*   **Confiança em nós de arquivamento:** Os nós que precisam de dados históricos podados devem confiar em nós de arquivamento, o que pode introduzir um ponto de centralização e um vetor de ataque.


## Conexões Institucionais

O Departamento de Segurança Interna dos EUA (DHS), através do seu Programa de Inovação do Vale do Silício (SVIP), tem um portfólio de projetos de blockchain. O foco do DHS é permitir o suporte para uma linha de base interoperável de segurança e privacidade em implementações de blockchain, através do uso de padrões abertos e globais. As aplicações de interesse incluem a garantia da autenticidade e integridade de mídias, melhoria do comércio internacional e processos aduaneiros, e mitigação de falsificação de licenças e certificados. O DHS não se foca diretamente na pesquisa de escalabilidade, mas sim na aplicação e padronização da tecnologia blockchain para seus casos de uso governamentais.


---

## Relatório: 4_P7k00ckGB6HwW10OiVgeda_1766816112304_na1fn_L2hvbWUvdWJ1bnR1L3JlcG9ydA.md

## Equações e Fórmulas

- `h(x) = y`
- `C_n = (n, t_n, id_n, y_n, L_n)`
- `L_n = (t_{n-1}, id_{n-1}, y_{n-1}, H(L_{n-1}))`
- `s = \sigma(C_n)`
- `s' = \sigma(n+1, t_{n+1}, id_{n+1}, y_{n+1}, L_{n+1})`
- `L_n = [(t_{n-k}, id_{n-k}, y_{n-k}, H(L_{n-k})), ..., (t_{n-1}, id_{n-1}, y_{n-1}, H(L_{n-1}))]`
- `G(y) = (id_1, id_2, ..., id_k)`
- `s_j = \sigma_j(t, id, y)`

## Variáveis e Parâmetros

- `h`: uma família de funções de hash criptograficamente seguras e sem colisão.
- `x`: o documento a ser carimbado com data e hora.
- `y`: o valor de hash do documento `x`.
- `l`: o comprimento fixo da string de bits de saída da função de hash.
- `TSS`: Serviço de Carimbo de Data e Hora (Time-Stamping Service).
- `id`: número de identificação do cliente.
- `n`: número de sequência do certificado de carimbo de data e hora.
- `t_n`: a hora da n-ésima solicitação.
- `id_n`: o número do cliente da n-ésima solicitação.
- `y_n`: o valor de hash da n-ésima solicitação.
- `L_n`: informações de vinculação do certificado emitido anteriormente.
- `H`: uma função de hash sem colisão usada pelo TSS.
- `\sigma()`: o procedimento de assinatura usado pelo TSS.
- `s`: o certificado assinado.
- `k`: o número de solicitações subsequentes a serem vinculadas.
- `G`: um gerador pseudoaleatório seguro.
- `id_j`: o j-ésimo número de identificação do cliente da saída de G(y).
- `s_j`: a mensagem assinada do cliente `id_j`.
- `\rho`: a fração de clientes possivelmente desonestos.
- `p`: parâmetro de segurança.

## Algoritmos

1.  **Serviço de Carimbo de Data e Hora Confiável com Hash e Assinatura:**
    *   O cliente calcula o hash `y = h(x)` do documento `x`.
    *   O cliente envia o hash `y` para o TSS.
    *   O TSS anexa a data e a hora ao hash, assina este documento composto e o envia de volta ao cliente.
    *   O cliente verifica a assinatura.

2.  **Esquema de Vinculação (Variante 1):**
    *   O TSS recebe a n-ésima solicitação `(y_n, id_n)`.
    *   O TSS cria um certificado `C_n = (n, t_n, id_n, y_n, L_n)`, onde `L_n = (t_{n-1}, id_{n-1}, y_{n-1}, H(L_{n-1}))`.
    *   O TSS assina o certificado `s = \sigma(C_n)` e o envia ao cliente.
    *   O TSS envia o ID do próximo cliente, `id_{n+1}`, para o cliente atual.
    *   Para verificar, um desafiante pode seguir a cadeia de carimbos de data e hora para frente e para trás.

3.  **Esquema de Vinculação (Variante 2):**
    *   Semelhante à Variante 1, mas vincula às próximas `k` solicitações.
    *   A informação de vinculação é `L_n = [(t_{n-k}, id_{n-k}, y_{n-k}, H(L_{n-k})), ..., (t_{n-1}, id_{n-1}, y_{n-1}, H(L_{n-1}))]`.
    *   O TSS envia a lista dos próximos `k` IDs de clientes para o cliente atual.

4.  **Esquema de Confiança Distribuída:**
    *   O cliente usa o hash `y` como semente para um gerador pseudoaleatório `G` para obter uma k-tupla de IDs de clientes: `G(y) = (id_1, id_2, ..., id_k)`.
    *   O cliente envia a solicitação `(y, id)` para cada um desses `k` clientes.
    *   Cada um dos `k` clientes retorna uma mensagem assinada `s_j = \sigma_j(t, id, y)`.
    *   O carimbo de data e hora consiste em `[(y, id), (s_1, ..., s_k)]`.

## Vulnerabilidades

- **Conluio com o TSS:** No esquema ingênuo, o TSS pode conspirar com um cliente para forjar um carimbo de data e hora.
- **Falsificação de Carimbos de Data e Hora:** Um adversário pode tentar preparar uma cadeia falsa de carimbos de data e hora.
- **Quebra da Função de Hash:** Se a função de hash for quebrada, todos os carimbos de data e hora emitidos anteriormente serão questionados.
- **Necessidade de Renovação:** Os carimbos de data e hora podem precisar ser renovados com novas implementações antes que as antigas sejam quebradas.

## Conexões

- W. Scott Stornetta (co-autor)
- Bellcore (afiliação institucional)
- Donald Beaver
- Shimon Even
- George Furnas
- Burt Kaliski
- Ralph Merkle
- Jeff Shrager
- Peter Winkler
- Yacov Yacobi
- Moti Yung


---

## Relatório: 5_SPQ7c8k3d5Pco2xE4ZRsm5_1766816187241_na1fn_L2hvbWUvdWJ1bnR1L2V4dHJhY3RlZF9kYXRh.md

# Relatório Técnico: W. Scott Stornetta - Timestamping Distribuído

## Equações e Fórmulas

- Função de hash: $$h: \{0, 1\}^* \rightarrow \{0, 1\}^l$$
- Hash de um documento: $$y = h(x)$$
- Vínculo de timestamping: $$L_i = H(t_i, ID_i, y_i, L_{i-1})$$

## Variáveis e Parâmetros

- **h**: Uma função de hash criptográfica segura e livre de colisões.
- **x**: O documento a ser carimbado no tempo.
- **y**: O valor de hash do documento `x`.
- **l**: O comprimento fixo da saída da função de hash.
- **TSS**: Serviço de Carimbo de Tempo (Time-Stamping Service).
- **ID_i**: O número de identificação único do cliente `i`.
- **t_i**: O tempo do carimbo de data/hora para o cliente `i`.
- **y_i**: O hash do documento do cliente `i`.
- **L_i**: O `i`-ésimo elo da cadeia, contendo as informações do carimbo de data/hora.
- **L_{i-1}**: O elo anterior na cadeia.
- **H**: Uma função de hash usada para vincular os carimbos de data/hora.

## Algoritmos e Protocolos

### 1. Solução Ingênua (Cofre Digital)

1.  O cliente transmite o documento para o TSS.
2.  O TSS registra a data e a hora de recebimento e armazena uma cópia do documento.
3.  Para verificação, o documento do cliente é comparado com a cópia do TSS.

### 2. Serviço de Carimbo de Tempo Confiável (com Hash e Assinatura)

1.  O cliente calcula o hash do documento: $$y = h(x)$$.
2.  O cliente envia o valor de hash `y` para o TSS.
3.  O TSS anexa a data e a hora ao hash, assina o documento composto e o envia de volta ao cliente.
4.  O cliente verifica a assinatura para garantir a autenticidade.

### 3. Esquema de Vinculação (Precursor do Blockchain)

1.  No momento `i`, o cliente com `ID_i` envia um documento cujo hash é `y_i`.
2.  O TSS calcula o vínculo: $$L_i = H(t_i, ID_i, y_i, L_{i-1})$$, onde $$L_{i-1}$$ é o vínculo anterior.
3.  O TSS retorna a tupla assinada `(t_i, ID_i, y_i, L_{i-1})` ao cliente.
4.  Periodicamente, o TSS publica o hash de todos os vínculos criados durante um determinado período (por exemplo, em um jornal de grande circulação).

## Vulnerabilidades e Fraquezas

- **Solução Ingênua:**
    - **Privacidade:** O TSS tem acesso ao conteúdo do documento.
    - **Largura de banda e armazenamento:** Ineficiente para documentos grandes.
    - **Incompetência:** O TSS pode perder ou corromper o documento.
    - **Confiança:** O TSS pode conspirar com um cliente para criar um carimbo de data/hora falso.

- **TSS Confiável:**
    - A confiança no TSS ainda é um requisito fundamental. O TSS não deve conspirar com clientes para criar carimbos de data/hora falsos.

- **Esquema de Vinculação:**
    - A segurança depende da suposição de que a função de hash `H` é livre de colisões.
    - A segurança depende da ampla publicação dos hashes vinculados. Se a publicação não for generalizada, pode ser possível criar uma cadeia forjada.

## Conexões

- **Bellcore:** W. Scott Stornetta e Stuart Haber eram pesquisadores da Bellcore (Bell Communications Research) quando publicaram seu trabalho sobre timestamping.

## Colaboradores

- **Stuart Haber:** Coautor do artigo "How to Time-Stamp a Digital Document" e principal colaborador de W. Scott Stornetta nesta área.


---

## Relatório: 6_a3bEu4eCdFU4Lulx8gSCu5_1766816416637_na1fn_L2hvbWUvdWJ1bnR1L3Jlc2VhcmNoL3RlY2huaWNhbF9yZXBvcnQ.md

# Relatório Técnico: Ronald Rivest

## Equações e Fórmulas

`C \equiv M^e \pmod{n}`; `M \equiv C^d \pmod{n}`; `e \cdot d \equiv 1 \pmod{\phi(n)}`; `D(E(M)) = M`; `E(D(M)) = M`; `S = D_B(M)`; `M = E_B(S)`; `f_i(x) = x^{e_i} \pmod{n_i}`

## Variáveis e Parâmetros

*   `p, q`: Dois números primos grandes e secretos; `n`: Módulo, o produto de `p` e `q` (`n = p \cdot q`); `\phi(n)`: Função totiente de Euler, `\phi(n) = (p-1)(q-1)`; `e`: Expoente público, um inteiro tal que `1 < e < \phi(n)` e `mdc(e, \phi(n)) = 1`; `d`: Expoente privado, o inverso multiplicativo de `e` módulo `\phi(n)`; `M`: Mensagem, um inteiro no intervalo `[0, n-1]`; `C`: Criptograma, um inteiro no intervalo `[0, n-1]`; `E`: Procedimento de encriptação; `D`: Procedimento de decriptação; `S`: Assinatura; `D_B`: Chave de decriptação de Bob; `E_B`: Chave de encriptação de Bob; `w`: Tamanho da palavra em bits (16, 32 ou 64); `r`: Número de rodadas (0 a 255); `b`: Tamanho da chave em bytes (0 a 2040); `K`: A chave secreta; `S`: O array de subchaves da rodada; `A`, `B`: As duas palavras que compõem o bloco de texto a ser criptografado; `P_w`, `Q_w`: Constantes mágicas; `A`, `B`, `C`, `D`: Registradores de entrada de w bits; `lg w`: O logaritmo de base 2 de w; **Bloco auxiliar de 48 bytes**; **Tabela S de 256 bytes**; **Checksum de 16 bytes**; `A`, `B`, `C`, `D`: Registradores de 32 bits que mantêm o estado do hash; `F`: Uma função não linear; uma função é usada em cada rodada; `Mi`: Um bloco de 32 bits da entrada da mensagem; `Ki`: Uma constante de 32 bits, diferente para cada rodada; `A`, `B`, `C`, `D`: Quatro palavras de 32 bits que compõem o estado do hash; `F`, `G`, `H`, `I`: Funções não lineares, uma para cada rodada; `M[i]`: O i-ésimo sub-bloco de 32 bits da mensagem; `K[i]`: Constantes de 32 bits, diferentes para cada operação; `m`: A mensagem a ser assinada; `P_1, P_2, ..., P_r`: As chaves públicas de todos os membros do anel; `s`: O índice do assinante real; `S_s`: A chave secreta do assinante real; `σ`: A assinatura em anel; `v`: Um valor de inicialização aleatório; `x_i`: Valores de entrada para as permutações trapdoor; `y_i`: Valores de saída das permutações trapdoor; `g_i`: A função de permutação trapdoor para o membro `i`; `C_k,v`: Uma função de combinação; `f_i`: A permutação trapdoor RSA para o membro `i`; `e_i, n_i`: A chave pública RSA para o membro `i`.

## Algoritmos

### RSA
1.  **Geração de Chaves:** Escolha dois primos `p` e `q`, calcule `n = p*q` e `phi(n) = (p-1)(q-1)`. Escolha `e` coprimo a `phi(n)` e calcule `d` como o inverso multiplicativo de `e` mod `phi(n)`.
2.  **Encriptação:** `C = M^e mod n`.
3.  **Decriptação:** `M = C^d mod n`.

### RC5
O RC5 é uma cifra de bloco com tamanho de bloco, número de rodadas e tamanho de chave variáveis. Ele consiste em três componentes: expansão de chave, criptografia e descriptografia.

### RC6
O RC6 é uma cifra de bloco baseada no RC5, com um tamanho de bloco de 128 bits e suporte para chaves de 128, 192 e 256 bits. Ele usa quatro registradores de trabalho em vez de dois e inclui uma multiplicação inteira como uma operação primitiva adicional.

### MD2
O MD2 processa mensagens em blocos de 128 bits, adicionando um checksum de 16 bytes. Ele usa um bloco auxiliar de 48 bytes e uma tabela S de 256 bytes, realizando 18 rodadas de permutação para cada bloco de mensagem.

### MD4
O MD4 processa mensagens em blocos de 512 bits, produzindo um digest de 128 bits. Consiste em 48 operações em três rodadas, usando funções não lineares.

### MD5
O MD5 processa mensagens em blocos de 512 bits e produz um hash de 128 bits. Ele opera em um estado de 128 bits e processa cada bloco em quatro rodadas de 16 operações.

### Assinaturas em Anel
Um esquema de assinatura digital que pode ser executado por qualquer membro de um grupo de usuários. Ele fornece anonimato, pois a identidade do assinante real não é revelada.

## Vulnerabilidades

*   **RC5:** Suscetível a ataques diferenciais com um número suficiente de textos simples escolhidos.
*   **MD2:** Vulnerável a ataques de colisão, pré-imagem e pré-imagem aprimorados.
*   **MD4:** Vulnerável a ataques de colisão e pré-imagem.
*   **MD5:** Criptograficamente quebrado, com vulnerabilidades de colisão, pré-imagem e colisão de prefixo escolhido.
*   **Assinaturas em Anel:** A segurança depende da segurança das permutações trapdoor subjacentes.

## Conexões

*   **MIT:** Membro do Laboratório de Ciência da Computação e Inteligência Artificial (CSAIL).
*   **Adi Shamir e Leonard Adleman:** Co-inventores do algoritmo RSA.
*   **Yael Tauman Kalai:** Co-inventor das assinaturas em anel.
*   **Comissão de Assistência Eleitoral:** Membro do Comitê de Desenvolvimento de Diretrizes Técnicas.
*   **Academias Nacionais:** Membro da Academia Nacional de Engenharia e da Academia Nacional de Ciências.
*   **ACM:** Fellow.
*   **Empresas:** Co-fundador da RSA Data Security, Verisign e Digital-Certificates.com.


---

## Relatório: 7_6E5GwmDjZa9FdCP5xuWYau_1766816425434_na1fn_L2hvbWUvdWJ1bnR1L3JlcG9ydA.md


(x^e)^d \equiv x \pmod{n};c \equiv m^e \pmod{n};c^d \equiv (m^e)^d \equiv m \pmod{n};n = pq;\lambda(n) = \text{lcm}(p-1, q-1);d \equiv e^{-1} \pmod{\lambda(n)};d_p = d \pmod{p-1};d_q = d \pmod{q-1};q_{inv} = q^{-1} \pmod{p};m_1 = c^{d_p} \pmod{p};m_2 = c^{d_q} \pmod{q};h = (q_{inv} \times (m_1 - m_2)) \pmod{p};m = m_2 + h \times q;
f(x) = a_0 + a_1x + a_2x^2 + \dots + a_{k-1}x^{k-1};a_0 = f(0) = \sum_{j=0}^{k-1} y_j \prod_{m=0, m \neq j}^{k-1} \frac{x_m}{x_m - x_j};\ell_j(x) = \prod_{m=0, m \neq j}^{k-1} \frac{x - x_m}{x_j - x_m};f(x) = \sum_{j=0}^{k-1} y_j \ell_j(x);
H(V) \ge d;H(V) < d - \alpha m;m = 2^{k-1};\alpha = 1/2^{k-1};
\Delta y = S(x \oplus \Delta x) \oplus S(x);
p: Um número primo grande;q: Um número primo grande;n: Módulo para as chaves pública e privada, n = pq;λ(n): Função totiente de Carmichael, λ(n) = mcm(p-1, q-1);e: Expoente da chave pública, 1 < e < λ(n) e mdc(e, λ(n)) = 1;d: Expoente da chave privada, d ≡ e⁻¹ (mod λ(n));m: Mensagem de texto simples preenchida;c: Texto cifrado;d_p: d mod (p-1);d_q: d mod (q-1);q_inv: q⁻¹ mod p;m_1: c^d_p mod p;m_2: c^d_q mod q;h: (q_inv * (m_1 - m_2)) mod p;
S: O segredo a ser compartilhado;n: O número de compartilhamentos a serem gerados;k: O número mínimo de compartilhamentos necessários para reconstruir o segredo;a_0, a_1, ..., a_{k-1}: Coeficientes do polinômio, onde a_0 = S;f(x): O polinômio usado para gerar os compartilhamentos;D_i: O i-ésimo compartilhamento, consistindo em um par (x_i, f(x_i));q: Um número primo maior que n e o número de valores possíveis para o segredo;l_j(x): O j-ésimo polinômio de base de Lagrange;x_j, y_j: As coordenadas de um ponto no polinômio;
k: O número mínimo de compartilhamentos necessários para revelar o segredo;n: O número total de compartilhamentos;m: O número de subpixels em cada compartilhamento;d: O limiar de nível de cinza;α: A diferença relativa no peso de Hamming entre os compartilhamentos combinados de um pixel branco e um pixel preto;S: Uma matriz booleana n x m que descreve a estrutura resultante;V: O vetor m "OR"-ed booleano;H(V): O peso de Hamming do vetor V;C0, C1: Coleções de matrizes booleanas n x m;
x: Texto simples;\Delta x: Diferença de texto simples;y: Texto cifrado;\Delta y: Diferença de texto cifrado;S: S-box;K: Chave;

RSA: O algoritmo RSA envolve quatro etapas: geração de chaves, distribuição de chaves, operação de chave pública (usada para criptografia ou verificação de uma assinatura) e operação de chave privada (usada para descriptografia ou assinatura de uma mensagem). A geração de chaves envolve a escolha de dois números primos grandes, p e q, e o cálculo de n = pq. A função totiente de Carmichael, λ(n) = mcm(p-1, q-1), é então calculada. Um inteiro e é escolhido tal que 1 < e < λ(n) e mdc(e, λ(n)) = 1. Finalmente, d é determinado como d ≡ e⁻¹ (mod λ(n)). A chave pública é (n, e) e a chave privada é d. A criptografia é realizada calculando c ≡ m^e (mod n), e a descriptografia é realizada calculando m ≡ c^d (mod n).;
Compartilhamento Secreto de Shamir: O Compartilhamento Secreto de Shamir é um esquema de limiar (k, n) que divide um segredo S em n compartilhamentos, onde qualquer k compartilhamentos podem reconstruir o segredo, mas qualquer k-1 compartilhamentos não revelam nenhuma informação sobre S. O esquema é baseado na interpolação de polinômios sobre campos finitos. Um polinômio f(x) de grau k-1 é construído com o segredo como o termo constante, a_0 = S. Os outros coeficientes, a_1, ..., a_{k-1}, são escolhidos aleatoriamente. Os compartilhamentos são pontos no polinômio, (x_i, f(x_i)). A reconstrução do segredo é feita por interpolação de Lagrange para encontrar f(0) = S.;
Criptografia Visual: A criptografia visual é um esquema criptográfico que permite que informações visuais (imagens, texto, etc.) sejam criptografadas de tal forma que a descriptografia possa ser realizada pelo sistema visual humano, sem o auxílio de computadores. O modelo básico consiste em duas coleções de matrizes booleanas n x m, C0 e C1. Para compartilhar um pixel branco, o revendedor escolhe aleatoriamente uma das matrizes em C0 e, para compartilhar um pixel preto, o revendedor escolhe aleatoriamente uma das matrizes em C1. A matriz escolhida define a cor dos m subpixels em cada uma das n transparências. A solução é considerada válida se as seguintes três condições forem atendidas: 1. Para qualquer S em C0, o "ou" V de quaisquer k das n linhas satisfaz H(V) <= d - αm. 2. Para qualquer S em C1, o "ou" V de quaisquer k das n linhas satisfaz H(V) >= d. 3. Para qualquer subconjunto de q < k compartilhamentos, as duas coleções de matrizes q x m são indistinguíveis.;
Criptoanálise Diferencial: A criptoanálise diferencial é uma forma geral de criptoanálise aplicável principalmente a cifras de bloco, mas também a cifras de fluxo e funções de hash criptográficas. No sentido mais amplo, é o estudo de como as diferenças na entrada de informações podem afetar a diferença resultante na saída. No caso de uma cifra de bloco, refere-se a um conjunto de técnicas para rastrear diferenças através da rede de transformação, descobrindo onde a cifra exibe comportamento não aleatório e explorando tais propriedades para recuperar a chave secreta. O método básico usa pares de textos simples relacionados por uma diferença constante. A diferença pode ser definida de várias maneiras, mas a operação OU-exclusivo (XOR) é usual. O invasor então calcula as diferenças dos textos cifrados correspondentes, na esperança de detectar padrões estatísticos em sua distribuição. O par de diferenças resultante é chamado de diferencial. Suas propriedades estatísticas dependem da natureza das S-boxes usadas para criptografia, então o invasor analisa os diferenciais (Δx, Δy) onde Δy = S(x ⊕ Δx) ⊕ S(x) para cada S-box S-box.
Ataques contra RSA simples: Criptografar com expoentes de criptografia baixos (por exemplo, e = 3) e valores pequenos de m (ou seja, m < n1/e) torna o sistema vulnerável, pois o resultado de me é estritamente menor que o módulo n. Nesses casos, os textos cifrados podem ser descriptografados facilmente calculando a raiz e-ésima do texto cifrado sobre os inteiros.;Ataque de texto cifrado escolhido: Se a mesma mensagem de texto não criptografado for enviada para e ou mais destinatários de forma criptografada, e os destinatários compartilharem o mesmo expoente e, mas p, q e, portanto, n diferentes, então é fácil descriptografar a mensagem de texto não criptografado original por meio do teorema do resto chinês.;Ataque de texto simples escolhido: Como a criptografia RSA é um algoritmo de criptografia determinístico, um invasor pode iniciar com sucesso um ataque de texto simples escolhido contra o sistema de criptografia, criptografando textos simples prováveis sob a chave pública e testando se eles são iguais ao texto cifrado.;Propriedade multiplicativa: O RSA tem a propriedade de que o produto de dois textos cifrados é igual à criptografia do produto dos respectivos textos simples. Por causa dessa propriedade multiplicativa, um ataque de texto cifrado escolhido é possível.;Fatoração do módulo: Dada a chave privada d, pode-se fatorar eficientemente o módulo n = pq. E dada a fatoração do módulo n = pq, pode-se obter qualquer chave privada (d', n) gerada em relação a uma chave pública (e', n).;Geração de chave defeituosa: Os números p e q não devem estar 'muito próximos', para que a fatoração de Fermat para n não seja bem-sucedida. Se p - q for menor que 2n1/4, a resolução para p e q é trivial. Além disso, se p - 1 ou q - 1 tiverem apenas fatores primos pequenos, n pode ser fatorado rapidamente pelo algoritmo p - 1 de Pollard e, portanto, tais valores de p ou q devem ser descartados.;Expoente privado pequeno: Se p estiver entre q e 2q (o que é bastante típico) e d < n1/4/3, então d pode ser calculado eficientemente a partir de n e e.;Expoente público pequeno: Não há ataque conhecido contra expoentes públicos pequenos, como e = 3, desde que o preenchimento adequado seja usado. O ataque de Coppersmith tem muitas aplicações no ataque ao RSA, especificamente se o expoente público e for pequeno e se a mensagem criptografada for curta e não preenchida.;Vulnerabilidade ROCA: Afeta as chaves RSA geradas por um algoritmo incorporado em uma biblioteca da Infineon conhecida como RSALib.;Geração de número aleatório fraca: Se um gerador de número aleatório criptograficamente forte, que foi devidamente semeado com entropia adequada, não for usado para gerar os primos p e q, o sistema fica vulnerável.;Ataques de temporização: Se o invasor Eve conhecer o hardware de Alice em detalhes suficientes e for capaz de medir os tempos de descriptografia para vários textos cifrados conhecidos, Eve poderá deduzir a chave de descriptografia d rapidamente.;Ataques de texto cifrado escolhido adaptativos: O primeiro ataque prático de texto cifrado escolhido adaptativo contra mensagens criptografadas com RSA usando o esquema de preenchimento PKCS #1 v1 foi descrito em 1998.;Ataques de análise de canal lateral: Um ataque de canal lateral usando análise de previsão de ramificação (BPA) foi descrito. Muitos processadores usam um preditor de ramificação para determinar se uma ramificação condicional no fluxo de instruções de um programa provavelmente será executada ou não. Frequentemente, esses processadores também implementam multithreading simultâneo (SMT). Os ataques de análise de previsão de ramificação usam um processo espião para descobrir (estatisticamente) a chave privada quando processada com esses processadores.;Ataque de injeção de falhas: Um invasor pode induzir falhas de hardware no dispositivo que está executando a descriptografia RSA para recuperar a chave privada.
Ron Rivest, Leonard Adleman, Weizmann Institute of Science, Jens Berlips, W Q Chen, Ivan Damgård, Kevin M. Esvelt, Urban Larsson, Lior Goldberg, Haiyan Li, Sanyang Liu, Wen, Moni Naor, Eli Biham, Don Coppersmith, Steven Levy, NSA, GCHQ, IBM


---

## Relatório: 8_ROmzyiwStQYStuiddFMOhD_1766816564982_na1fn_L2hvbWUvdWJ1bnR1L3RlY2huaWNhbF9yZXBvcnQ.md

# Informações sobre o Algoritmo RSA


## Equações e Fórmulas (LaTeX)

- Geração e Relação de Chaves: `(m^e)^d \equiv m \pmod{n}`
- Módulo: `n = p \cdot q`
- Função Totiente de Carmichael: `\lambda(n) = \text{lcm}(p-1, q-1)`
- Relação dos expoentes: `e \cdot d \equiv 1 \pmod{\lambda(n)}`
- Criptografia: `c \equiv m^e \pmod{n}`
- Decriptografia: `m \equiv c^d \pmod{n}`
- Assinatura Digital: `s \equiv h(m)^d \pmod{n}`
- Verificação de Assinatura: `h(m) \equiv s^e \pmod{n}`
- Otimização com o Teorema Chinês do Resto (CRT):
  - `d_p = d \pmod{p-1}`
  - `d_q = d \pmod{q-1}`
  - `q_{inv} = q^{-1} \pmod{p}`
  - `m_1 = c^{d_p} \pmod{p}`
  - `m_2 = c^{d_q} \pmod{q}`
  - `h = q_{inv} \cdot (m_1 - m_2) \pmod{p}`
  - `m = m_2 + h \cdot q`

## Variáveis e Parâmetros

- `p, q`: Dois números primos grandes e distintos (secretos).
- `n`: Módulo para as operações de criptografia e decriptografia (público).
- `e`: Expoente público, usado para criptografar mensagens (público).
- `d`: Expoente privado, usado para decriptografar mensagens (secreto).
- `\lambda(n)`: Função totiente de Carmichael, usada para garantir a reversibilidade da operação (secreta).
- `m`: Mensagem original em formato numérico.
- `c`: Mensagem criptografada (ciphertext).
- `h(m)`: Função de hash aplicada à mensagem `m`.
- `s`: Assinatura digital da mensagem.
- `d_p, d_q, q_{inv}`: Coeficientes pré-calculados para acelerar a decriptografia usando o Teorema Chinês do Resto (secretos).

## Algoritmos

1.  **Geração de Chaves:**
    1.  Escolher dois números primos grandes, `p` e `q`.
    2.  Calcular `n = p \cdot q`.
    3.  Calcular `\lambda(n) = \text{lcm}(p-1, q-1)`.
    4.  Escolher um inteiro `e` tal que `1 < e < \lambda(n)` e `gcd(e, \lambda(n)) = 1`.
    5.  Calcular `d` como o inverso multiplicativo modular de `e` módulo `\lambda(n)`.
    6.  A chave pública é `(n, e)` e a chave privada é `(d)` (ou a forma otimizada com `p, q, d_p, d_q, q_{inv}`).

2.  **Criptografia:**
    1.  A mensagem `m` é convertida em um número.
    2.  O ciphertext `c` é calculado como `c = m^e \pmod{n}`.

3.  **Decriptografia:**
    1.  A mensagem original `m` é recuperada calculando `m = c^d \pmod{n}`.
    2.  A decriptografia pode ser otimizada usando o Teorema Chinês do Resto com os parâmetros pré-calculados.

## Vulnerabilidades

- **Ataques de Fatoração:** A segurança do RSA depende da dificuldade de fatorar o módulo `n`. Se `n` for fatorado, a chave privada `d` pode ser calculada. Algoritmos como o General Number Field Sieve (GNFS) são usados para isso, e a computação quântica com o algoritmo de Shor representa uma ameaça futura.
- **Expoentes de Criptografia Baixos:** Se um expoente público `e` pequeno (como 3) for usado sem padding adequado, mensagens pequenas `m` podem resultar em `m^e < n`, permitindo a recuperação de `m` simplesmente calculando a raiz e-ésima inteira de `c`.
- **Ataques de Texto Plano Escolhido (Chosen-Plaintext Attacks):** Como o RSA sem padding é determinístico, um atacante pode criptografar prováveis textos planos e comparar com o ciphertext para adivinhar a mensagem.
- **Propriedade Multiplicativa:** A propriedade `(m1^e \cdot m2^e) \equiv (m1 \cdot m2)^e \pmod{n}` permite ataques de texto cifrado escolhido, onde um atacante pode enganar o detentor da chave privada para decifrar uma mensagem aparentemente inofensiva, que na verdade revela informações sobre uma mensagem alvo.
- **Ataques de Timing:** Variações no tempo de decriptografia podem vazar informações sobre a chave privada. Técnicas como o *cryptographic blinding* são usadas para mitigar isso.
- **Ataques de Canal Lateral (Side-Channel Attacks):** Ataques que exploram informações vazadas pela implementação física do hardware, como consumo de energia ou predição de desvios (branch prediction).
- **Geração de Chaves Fraca:** Se os primos `p` e `q` não forem gerados com aleatoriedade suficiente ou estiverem muito próximos, a fatoração de `n` pode ser facilitada. A vulnerabilidade ROCA é um exemplo de falha na geração de chaves.
- **Ataques a Esquemas de Padding:** Versões mais antigas do padrão PKCS#1 eram vulneráveis a ataques de texto cifrado escolhido adaptativos (como o ataque de Bleichenbacher).
# Informações sobre a Computação de DNA de Adleman

## Algoritmo Molecular para o Problema do Caminho Hamiltoniano

O experimento de Adleman resolveu uma instância do problema do caminho Hamiltoniano direcionado para um grafo com 7 vértices e 14 arestas.

### Codificação do Grafo em DNA

1.  **Vértices:** Cada vértice `i` do grafo foi associado a uma sequência de 20 bases de DNA (20-mer) gerada aleatoriamente, denotada como `O_i`.
2.  **Arestas:** Para cada aresta direcionada de um vértice `i` para um vértice `j`, uma sequência de DNA `O_{i->j}` foi criada. Essa sequência era composta pela metade 3' (10 bases) da sequência `O_i` e pela metade 5' (10 bases) da sequência `O_j`. Isso cria uma "ponte" ou "splint" que pode conectar as sequências dos vértices.
3.  **Complementos:** Para cada vértice `i`, uma sequência complementar de Watson-Crick, denotada `O'_i`, foi sintetizada.

### Passos Computacionais (Operações Moleculares)

O algoritmo para encontrar o caminho Hamiltoniano foi implementado através dos seguintes passos moleculares:

1.  **Geração de Caminhos Aleatórios:**
    *   As sequências de DNA representando os vértices (`O_i`) e as arestas (`O_{i->j}`) foram misturadas em uma reação de ligação (ligation). As sequências de arestas atuam como "splints", conectando as sequências de vértices compatíveis. O resultado é uma "sopa" de moléculas de DNA, onde cada molécula representa um caminho aleatório através do grafo.

2.  **Seleção de Caminhos Válidos (Início e Fim):**
    *   A Reação em Cadeia da Polimerase (PCR) foi usada para amplificar seletivamente apenas os caminhos que começavam no vértice de início (`v_in`) e terminavam no vértice de fim (`v_out`). Isso foi feito usando os primers `O_{v_in}` e `O'_{v_out}`.

3.  **Seleção por Comprimento:**
    *   Eletroforese em gel foi usada para separar as moléculas de DNA por tamanho. Como o grafo tinha `n=7` vértices, um caminho Hamiltoniano deveria conter 7 vértices, correspondendo a um comprimento de `7 * 20 = 140` pares de bases. A banda de 140 bp foi extraída do gel.

4.  **Verificação de Passagem por Todos os Vértices:**
    *   Para garantir que cada caminho continha todos os `n` vértices, foi realizado um processo de purificação por afinidade sequencial. O produto do passo 3 foi desnaturado para obter fitas simples. Em seguida, essas fitas foram expostas a esferas magnéticas às quais as sequências complementares de cada vértice (`O'_1`, `O'_2`, ..., `O'_n`) foram anexadas, uma de cada vez. Apenas as moléculas que se ligaram (hibridizaram) a todas as sequências de vértices foram retidas.

5.  **Detecção do Resultado:**
    *   Se alguma molécula de DNA restasse após o passo 4, isso indicaria a existência de um caminho Hamiltoniano. O resultado foi verificado por PCR e eletroforese em gel para confirmar a presença da sequência correta.

## Vulnerabilidades e Limitações

- **Escalabilidade:** O método de Adleman, embora demonstre a prova de conceito, não é escalável para problemas grandes. Para um grafo com 200 vértices, a quantidade de DNA necessária seria maior que a massa da Terra.
- **Erros:** As operações bioquímicas (ligação, PCR, hibridização) são propensas a erros, como ligações incorretas, mutações durante a amplificação e hibridização imperfeita. Isso pode levar a falsos positivos ou negativos.
- **Eficiência:** O algoritmo é descrito como "ingênuo e ineficiente". A geração de todos os caminhos possíveis para depois filtrá-los é um método de força bruta que consome uma quantidade exponencial de recursos (moléculas).
- **Intensidade de Trabalho:** O processo é manual e demorado, exigindo vários dias de trabalho de laboratório, especialmente os passos de separação por esferas magnéticas.
# Contribuições de Adleman para Números Primos e Fatoração


## Teste de Primalidade Adleman-Pomerance-Rumely (APR)

O teste de primalidade Adleman-Pomerance-Rumely (APR) é um algoritmo determinístico para determinar se um número é primo. Foi uma melhoria significativa sobre os testes de primalidade anteriores, que eram probabilísticos (como Miller-Rabin) ou ineficientes.

### Conceitos Matemáticos Fundamentais

O teste APR e sua variante aprimorada, APR-CL (por Cohen-Lenstra), baseiam-se em conceitos da teoria algébrica dos números, especificamente:

- **Corpos Ciclotômicos:** O teste opera em anéis de inteiros de corpos ciclotômicos. Um corpo ciclotômico `Q(ζ_p)` é formado pela adjunção de uma raiz p-ésima da unidade, `ζ_p`, aos números racionais.
- **Somas de Jacobi:** São somas de caracteres sobre corpos finitos, que generalizam as somas de Gauss. Elas são usadas para construir análogos do pequeno teorema de Fermat em corpos ciclotômicos, que formam a base do teste.
- **Caracteres de Potência Residual:** O teste verifica uma série de congruências envolvendo caracteres de potência, que são análogos às potências no teste de Fermat.

### Estrutura do Algoritmo (Visão Geral)

O algoritmo é complexo, mas a ideia central é a seguinte:

1.  **Seleção de Primos:** Para um número `n` a ser testado, o algoritmo seleciona um conjunto de pequenos números primos `q` cujo produto `s` excede `sqrt(n)`.
2.  **Verificação de Congruências:** O teste verifica se `n` se comporta como um número primo em relação a uma série de congruências em vários corpos ciclotômicos `Z[ζ_q]`. Essas congruências são análogas à congruência de Fermat `a^(n-1) ≡ 1 (mod n)`.
3.  **Uso de Somas de Jacobi:** As somas de Jacobi são usadas para relacionar o comportamento de `n` em diferentes corpos ciclotômicos e para derivar as congruências necessárias para o teste.
4.  **Decisão:** Se `n` passar em todos os testes de congruência para o conjunto de primos `q` selecionado, então `n` é declarado primo. Caso contrário, é composto.

### Complexidade

O tempo de execução do algoritmo APR-CL é quase polinomial, dado por:

`O((\log n)^{c \log \log \log n})`

Onde `c` é uma constante. Embora não seja estritamente um tempo polinomial (como o teste AKS, que foi descoberto mais tarde), na prática, o APR-CL é muito mais rápido que o AKS para números que podem ser manipulados por computadores atuais.

### Fatoração

Embora Adleman tenha contribuído significativamente para os testes de primalidade, seu trabalho principal relacionado à fatoração está implicitamente ligado à segurança do RSA. A dificuldade de fatorar grandes números é o que torna o RSA seguro. O desenvolvimento de testes de primalidade eficientes foi crucial para a geração de chaves RSA, que requer a localização de grandes números primos.

Não há um "algoritmo de fatoração de Adleman" específico que seja amplamente conhecido da mesma forma que o teste de primalidade APR. Sua pesquisa focou-se mais em *distinguir* primos de compostos do que em *fatorar* compostos.
# Conexões e Colaboradores de Leonard Adleman

## Colaboradores Notáveis

- **Ron Rivest:** Co-criador do algoritmo RSA. A colaboração ocorreu enquanto ambos estavam no Massachusetts Institute of Technology (MIT).
- **Adi Shamir:** Co-criador do algoritmo RSA. A colaboração ocorreu enquanto ambos estavam no Massachusetts Institute of Technology (MIT).
- **Carl Pomerance:** Colaborador no desenvolvimento do teste de primalidade Adleman-Pomerance-Rumely (APR).
- **Robert Rumely:** Colaborador no desenvolvimento do teste de primalidade Adleman-Pomerance-Rumely (APR).
- **Henri Cohen:** Aprimorou o teste APR, resultando na versão APR-CL.
- **Hendrik Willem Lenstra:** Aprimorou o teste APR, resultando na versão APR-CL.

## Afiliações Institucionais

- **University of Southern California (USC):** Adleman é Professor Catedrático Henry Salvatori de Ciência da Computação e Professor de Biologia Molecular na USC. Esta é sua principal afiliação acadêmica há muitos anos.
- **Massachusetts Institute of Technology (MIT):** Foi professor assistente no MIT, onde conheceu Rivest e Shamir e desenvolveu o algoritmo RSA.
- **University of California, Berkeley:** Obteve seu Ph.D. em ciência da computação em Berkeley em 1976.

## Conexões com Governos e Corporações

- **RSA Security:** A empresa RSA Security (originalmente RSA Data Security, Inc.) foi fundada por Rivest, Shamir e Adleman para comercializar o algoritmo RSA. A empresa se tornou uma das mais influentes em segurança digital. Embora a pesquisa inicial tenha sido acadêmica, ela rapidamente levou a uma aplicação comercial massiva.
- **Governo dos EUA (Patente):** O MIT obteve a patente do algoritmo RSA em 1983 (U.S. Patent 4,405,829). O algoritmo foi posteriormente liberado para o domínio público em 2000, pouco antes da expiração da patente. Isso indica uma interação com o sistema de patentes do governo dos EUA, mas não uma colaboração direta em pesquisa.
- **GCHQ (Government Communications Headquarters - Reino Unido):** É importante notar que um sistema equivalente ao RSA foi desenvolvido secretamente em 1973 por Clifford Cocks no GCHQ, a agência de inteligência de sinais do Reino Unido. Este trabalho foi mantido em segredo e não teve impacto no desenvolvimento público do RSA por Adleman, Rivest e Shamir. Não há evidências de uma conexão ou colaboração direta entre Adleman e o GCHQ ou a NSA. A descoberta do trabalho de Cocks foi posterior e independente.


---

## Relatório: 9_dIss7wT3yp0bRGG6nA5VDF_1766816359730_na1fn_L2hvbWUvdWJ1bnR1L3RlY2huaWNhbF9yZXBvcnQ.md

# Relatório Técnico: Hal Finney

## Assunto

Hal Finney - Reusable Proof of Work (RPOW), PGP, primeira transação Bitcoin, cypherpunks

## Equações e Fórmulas

- `SHA-1(text_string) = 0...0<hash_value>` (O hash SHA-1 de uma string de texto resultando em N bits zero iniciais)
- Probabilidade de encontrar N bits zero iniciais: `1 / (2^N)`

## Variáveis e Parâmetros

- `N`: O número de bits zero iniciais na colisão do hashcash.
- `collision size`: O número de bits zero iniciais, determinando o valor do hashcash.
- `resource string`: Uma string incorporada em um token hashcash para identificar seu uso pretendido e prevenir a reutilização em outros contextos.

## Algoritmos

### Criação de Hashcash

1.  Comece com uma string base.
2.  Modifique iterativamente a string (por exemplo, incrementando um contador).
3.  Para cada string modificada, calcule seu hash SHA-1.
4.  Verifique se o hash possui o número desejado de bits zero iniciais (N).
5.  Se possuir, a string é um token hashcash válido. Caso contrário, continue a iteração.

### Verificação de Hashcash

1.  Receba um token hashcash.
2.  Calcule o hash SHA-1 do token.
3.  Conte o número de bits zero iniciais.
4.  Verifique se o número de bits zero atende à dificuldade exigida.
5.  Verifique a `resource string` para garantir que o token está sendo usado para o propósito pretendido.
6.  Consulte um banco de dados local para garantir que o token não foi usado anteriormente.

### Troca de Tokens RPOW

1.  Um usuário envia um token POW (hashcash) para um servidor RPOW.
2.  O servidor verifica o token POW.
3.  O servidor cria um novo token RPOW de valor igual.
4.  O servidor registra a propriedade do novo token RPOW para o usuário.
5.  O usuário pode então transferir o token RPOW para outro usuário, assinando uma ordem de transferência.
6.  O destinatário pode então trocar o token RPOW no servidor por um novo, continuando a cadeia.

## Vulnerabilidades

- **Gasto duplo de hashcash:** Um token hashcash poderia ser usado várias vezes se não fossem as verificações da `resource string` e do banco de dados local.
- **Falsificação de tokens RPOW:** O sistema depende de um servidor confiável (executando em um coprocessador criptográfico seguro) para prevenir a falsificação. Um servidor comprometido poderia potencialmente criar tokens RPOW fraudulentos.

## Conexões

- Adam Back (inventor do hashcash)
- Nick Szabo (criador do conceito de 'bit gold')
- Wei Dai (criador do 'b-money')
- PGP Corporation (onde Hal Finney trabalhou)
- IBM (fabricante do coprocessador criptográfico seguro 4758)


## PGP (Pretty Good Privacy)

### Equações e Fórmulas

- `m = SK^e mod n`
- `M = m + k*n`
- `m = M mod n`

### Variáveis e Parâmetros

- `L`: Uma potência de 256 acima do módulo n. Para segurança, a próxima potência de 256 acima de n*(2^64).
- `n`: O módulo RSA.
- `t`: A parte inteira de L/n.
- `s`: O resto da divisão de L por n (ou seja, L = n*t + s).
- `SK`: A chave de sessão IDEA do PGP.
- `m`: A versão criptografada em RSA da chave de sessão.
- `k`: Um número aleatório no intervalo [0,t].
- `M`: A chave criptografada "oculta" (stegged).

### Algoritmos

#### Algoritmo PGP "Truly Stealthy"

1.  Escolha um SK aleatório em [0,n).
2.  Criptografe-o com RSA para formar `m = SK^e mod n`.
3.  Escolha um k aleatório em [0,t].
4.  Calcule a chave criptografada "oculta" como `M = m + k*n`.
5.  Se M não estiver em [0,L) (ou seja, se M >= L), falhe. A chance de isso acontecer é menor que 1 em 2^64.
6.  Caso contrário, armazene M como um número binário bruto, ocupando `log base 256 de L` bytes.

#### Recuperação da Chave

1.  Pegue os primeiros `log base 256 de L` bytes como M.
2.  Calcule `m = M mod n`.

### Vulnerabilidades

- **Distribuição não uniforme do byte de ordem superior:** No PGP "Stealth" original, o byte de ordem superior da chave de sessão criptografada tinha uma distribuição não uniforme, tornando-o distinguível de ruído aleatório.

### Conexões

- Eric Hughes (propôs a solução para a distribuição não uniforme)
- Philip Zimmermann (autor do PGP)

## Primeira Transação de Bitcoin

### Detalhes da Transação

- **TXID:** f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16
- **Timestamp:** 2009-01-12 03:30:25
- **Valor:** 10.00 BTC
- **Taxa:** 0 BTC

### Inputs

- **Endereço de Origem:** (Coinbase - Bloco 170)
- **Valor:** 50.00 BTC

### Outputs

- **Endereço de Destino (Hal Finney):** 1Q2TWHE3GMdB6BZKafqwxXtWAWgFt5Jvm3
- **Valor:** 10.00 BTC
- **Endereço de Troco (Satoshi Nakamoto):** 12cbQLTFMXRnSzktFkuoG3eHoMeFtpTu3S
- **Valor:** 40.00 BTC

### Scripts

#### Script de Saída (Output Script) - Para Hal Finney

- **ScriptPubKey (ASM):** `OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG`
- **ScriptPubKey (HEX):** `76a9147821c322f27439cef888df3359168a1b74582a5288ac`

#### Script de Entrada (Input Script) - Da Coinbase

- **ScriptSig (ASM):** `<signature> <pubKey>`
- **ScriptSig (HEX):** `47304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3`

### Conexões

- Satoshi Nakamoto (remetente da transação)


---

