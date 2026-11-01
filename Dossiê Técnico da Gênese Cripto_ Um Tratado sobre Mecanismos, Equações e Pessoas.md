# Dossiê Técnico da Gênese Cripto: Um Tratado sobre Mecanismos, Equações e Pessoas

**Autor**: Manus AI  
**Data**: 04 de Janeiro de 2026

---

## Sumário Executivo

Este dossiê apresenta uma análise técnica exaustiva dos mecanismos, equações, fórmulas e conceitos criptográficos que formam a base das criptomoedas. A pesquisa, conduzida com processamento paralelo em 24 subtarefas, investigou as contribuições acadêmicas e técnicas de 23 pessoas e tópicos chave, desde os pioneiros Cypherpunks até os desenvolvedores do Bitcoin Core. O resultado é um compêndio de 226 equações, 371 variáveis e 80 algoritmos, detalhando a evolução das ideias que culminaram no Bitcoin e no Ethereum, e fornecendo um guia de referência para os fundamentos matemáticos e criptográficos que sustentam a revolução dos ativos digitais.

---

## 1. Fundamentos da Criptografia de Chave Pública

### 1.1 Troca de Chaves Diffie-Hellman

- **Conceito**: Permite que duas partes estabeleçam uma chave secreta compartilhada sobre um canal de comunicação inseguro.
- **Equação**: `s = (B^a) mod p = (g^b)^a mod p = g^(ab) mod p`
- **Pessoas Chave**: Whitfield Diffie, Martin Hellman

### 1.2 Criptografia de Curva Elíptica (ECC)

- **Conceito**: Uma abordagem de chave pública baseada na estrutura algébrica de curvas elípticas sobre corpos finitos.
- **Equação da Curva (secp256k1)**: `y^2 = x^3 + 7 (mod p)`
- **Geração de Chave Pública**: `K = k * G`
- **Pessoas Chave**: Neal Koblitz, Victor S. Miller

---

## 2. Os Blocos de Construção

### 2.1 Funções Hash (SHA-256)

- **Conceito**: Uma função que mapeia dados de tamanho arbitrário para uma saída de tamanho fixo.
- **Propriedades**: Resistência à pré-imagem, segunda pré-imagem e colisão.
- **Equação (Simplificada)**: `H(x) = SHA256(SHA256(x))`
- **Pessoas Chave**: Ralph Merkle (Construção Merkle-Damgård)

### 2.2 Assinaturas Digitais (ECDSA)

- **Conceito**: Um análogo matemático de uma assinatura manuscrita, que garante autenticidade, integridade e não-repúdio.
- **Equação de Verificação**: `(x1, y1) = (u1*G + u2*Q)` e `r ≡ x1 (mod n)`
- **Pessoas Chave**: Scott Vanstone

### 2.3 Árvores de Merkle

- **Conceito**: Uma estrutura de dados em árvore onde cada nó folha é um hash de um bloco de dados, e cada nó não-folha é um hash de seus nós filhos.
- **Equação**: `ParentHash = Hash(LeftChildHash + RightChildHash)`
- **Pessoas Chave**: Ralph Merkle

---

## 3. Os Precursores e Suas Mecânicas

| Pessoa | Contribuição | Mecanismo Chave | Equação/Fórmula Representativa |
|---|---|---|---|
| **David Chaum** | DigiCash | Assinaturas Cegas | `s' = m^e * r^e (mod n)` |
| **Adam Back** | Hashcash | Prova de Trabalho (PoW) | `H(c) < 2^(256-d)` |
| **Wei Dai** | b-money | Livro-razão distribuído | N/A (conceitual) |
| **Nick Szabo** | Bit Gold | Prova de Trabalho (PoW) | N/A (conceitual) |

---

## 4. Bitcoin: A Síntese de Satoshi Nakamoto

### 4.1 Consenso Nakamoto

- **Conceito**: Uma solução para o problema dos Generais Bizantinos, onde a cadeia mais longa (com mais prova de trabalho acumulada) é considerada a versão correta da história.
- **Probabilidade de Sucesso do Atacante**: `P = 1 - Σ(k=0 to z) [λ^k * e^(-λ) / k!]` onde `λ = z * (p/q)`

### 4.2 Mineração e Ajuste de Dificuldade

- **Conceito**: O processo de encontrar um hash de bloco válido que atenda a um determinado alvo de dificuldade.
- **Equação do Alvo**: `Target = max_target / difficulty`
- **Equação de Ajuste de Dificuldade**: `new_difficulty = old_difficulty * (2016 * 10 * 60) / actual_time`

### 4.3 Modelo UTXO

- **Conceito**: O estado do sistema é mantido como um conjunto de Saídas de Transação Não Gastas (UTXOs), em vez de saldos de contas.

---

## 5. Ethereum: O Computador Mundial

### 5.1 Ethereum Virtual Machine (EVM)

- **Conceito**: Uma máquina de estado Turing-completa que executa o código dos contratos inteligentes.

### 5.2 Mecanismo de Gás

- **Conceito**: Um sistema de precificação para a execução de transações e contratos inteligentes, para alocar recursos da EVM.
- **Equação da Taxa**: `TxFee = GasUsed * GasPrice`

### 5.3 Função de Transição de Estado

- **Conceito**: A função que define como o estado do sistema muda de um bloco para o outro.
- **Equação**: `σ_t+1 = Υ(σ_t, T)`

---

## 6. Pessoas Chave e Suas Contribuições Técnicas

| Pessoa | Contribuição Técnica Principal |
|---|---|
| **Hal Finney** | RPOW (Prova de Trabalho Reutilizável), primeiro receptor de uma transação Bitcoin. |
| **Gavin Andresen** | Desenvolvedor líder do Bitcoin após Satoshi, fundador da Bitcoin Foundation. |
| **Pieter Wuille** | Desenvolvedor do Bitcoin Core, autor do SegWit, Taproot e libsecp256k1. |

---

## 7. Referências

1. [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf)
2. [Untraceable Electronic Mail, Return Addresses, and Digital Pseudonyms](https://www.cypherpunks.to/faq/chaum-mix.pdf)
3. [b-money by Wei Dai](http://www.weidai.com/bmoney.txt)
4. [Hashcash - A Denial of Service Counter-Measure](http://www.hashcash.org/papers/hashcash.pdf)
5. [Ethereum Whitepaper](https://ethereum.org/en/whitepaper/)

---

*Documento gerado por Manus AI em 04 de Janeiro de 2026.*
