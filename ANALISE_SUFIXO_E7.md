# Análise Observacional: O Sufixo E7 e a Cascata de Carries

## Resumo

Ao observar os dados de 100.000 nonces, descobrimos que **100% dos h_work que produzem ≥8 zeros líderes terminam em E7**.

Este documento apresenta a análise observacional pura dos dados, sem tentar criar métodos ou forçar padrões.

---

## Observação 1: A Onipresença do E7

```
ZEROS = 17 (1 nonce)    → 100% sufixo E7
ZEROS = 15 (2 nonces)   → 100% sufixo E7
ZEROS = 14 (2 nonces)   → 100% sufixo E7
ZEROS = 13 (4 nonces)   → 100% sufixo E7
ZEROS = 12 (10 nonces)  → 100% sufixo E7
ZEROS = 11 (19 nonces)  → 100% sufixo E7
ZEROS = 10 (51 nonces)  → 100% sufixo E7
ZEROS = 9  (111 nonces) → 100% sufixo E7
ZEROS = 8  (186 nonces) → 100% sufixo E7
```

A transição é abrupta:
- **8+ zeros: apenas E7**
- **7 zeros: apenas E8**
- **6 zeros: E9 (50.4%) e EA (49.6%)**
- **5 zeros: EB, EE, EC, ED (~25% cada)**

---

## Observação 2: Por que E7?

A resposta está na aritmética simples:

```
IV[7] = 0x5BE0CD19
Byte LSB de IV[7] = 0x19 = 25

0xE7 + 0x19 = 231 + 25 = 256 = 0x100
             │
             └─→ Byte resultante: 0x00 (ZERO!)
                 Carry: 1
```

O sufixo E7 é o **único** valor que, somado ao byte LSB de IV[7], produz exatamente 256 - zerando o byte e propagando um carry.

Comparação com vizinhos:
```
0xE6 + 0x19 = 255 = 0x0FF → byte=0xFF, carry=0
0xE7 + 0x19 = 256 = 0x100 → byte=0x00, carry=1  ← ESPECIAL
0xE8 + 0x19 = 257 = 0x101 → byte=0x01, carry=1
```

---

## Observação 3: A Cascata de Carries

O melhor exemplo é o nonce 8603 (17 zeros):

```
h_work = 0x6A9B32E7
IV[7]  = 0x5BE0CD19

Soma byte-a-byte (LSB → MSB):

Byte 0: 0xE7 + 0x19     = 256 = 0x100 → resultado: 0x00, carry: 1
Byte 1: 0x32 + 0xCD + 1 = 256 = 0x100 → resultado: 0x00, carry: 1
Byte 2: 0x9B + 0xE0 + 1 = 380 = 0x17C → resultado: 0x7C, carry: 1
Byte 3: 0x6A + 0x5B + 1 = 198 = 0x0C6 → resultado: 0xC6, carry: 0

final_h7 = 0xC67C0000
byteswap = 0x00007CC6  → 17 zeros líderes!
```

Observe: **os bytes 0 e 1 ambos somam exatamente 256**, propagando carries e criando dois bytes zero.

---

## Observação 4: Os Valores Ideais

A estrutura de IV[7] = 0x5BE0CD19 **define** os valores ideais para cada byte:

| Byte | IV[7] byte | Para zerar | Valor ideal |
|------|------------|------------|-------------|
| 0    | 0x19       | +0x19=256  | **0xE7**    |
| 1    | 0xCD       | +0xCD+1=256| **0x32**    |
| 2    | 0xE0       | +0xE0+1=256| **0x1F**    |
| 3    | 0x5B       | +0x5B+1=256| **0xA4**    |

O h_work ideal para 32 zeros seria: **0xA41F32E7**

Verificação:
```
0xA41F32E7 + 0x5BE0CD19 = 0x00000000  ✓
```

---

## Observação 5: A Progressão do Byte 1

Para nonces com sufixo E7, o **byte 1 determina quantos zeros adicionais** conseguimos:

```
Zeros vs Distância média do byte 1 ao ideal (0x32):

  17 zeros: dist_média=  0.0  
  15 zeros: dist_média=  1.0  
  14 zeros: dist_média=  3.0  
  13 zeros: dist_média=  6.2  █
  12 zeros: dist_média= 11.7  ██
  11 zeros: dist_média= 23.0  ████
  10 zeros: dist_média= 49.5  █████████
   9 zeros: dist_média= 97.0  ███████████████████
   8 zeros: dist_média=111.8  ██████████████████████
```

A relação é quase linear:
- Byte 1 = 0x32 → 17 zeros
- Byte 1 = 0x33 → 15 zeros
- Byte 1 = 0x35 → 14 zeros
- Byte 1 = 0x3x → 12-13 zeros
- Byte 1 = 0x4x → 11 zeros
- Byte 1 > 0x80 → 8-9 zeros

---

## Observação 6: Estrutura Completa dos Top 20 h_work

```
Nonce      h_work         Zeros  B3    B2    B1    B0    Match
---------- -------------- ------ ----- ----- ----- ----- -------
8603       0x6A9B32E7     17     0x6A  0x9B  0x32  0xE7  b0✓ b1✓
87595      0xA91033E7     15     0xA9  0x10  0x33  0xE7  b0✓
96887      0xEFD533E7     15     0xEF  0xD5  0x33  0xE7  b0✓
28898      0xDF2B35E7     14     0xDF  0x2B  0x35  0xE7  b0✓
62127      0xB5CB35E7     14     0xB5  0xCB  0x35  0xE7  b0✓
4200       0x167337E7     13     0x16  0x73  0x37  0xE7  b0✓
23519      0x2D1D39E7     13     0x2D  0x1D  0x39  0xE7  b0✓
...
```

**Todos os top 20 têm byte 0 = E7** (100%)

---

## Conclusão

O sufixo E7 não é coincidência - é consequência direta da aritmética:

1. **zeros = f(h_work + IV[7])**

2. **Para muitos zeros, precisamos que a soma tenha bytes pequenos após byteswap**

3. **Isso acontece quando h_work tem bytes que, somados aos de IV[7], produzem carries em cascata**

4. **O byte 0 ideal é 0xE7 porque 0xE7 + 0x19 = 256 (carry perfeito)**

5. **O byte 1 ideal é 0x32 porque 0x32 + 0xCD + 1 = 256 (outro carry)**

6. **Não há magia - é aritmética modular pura**

A distribuição de nonces sobre h_work é uniforme (SHA-256 faz isso).
Mas os h_work que produzem muitos zeros são **estruturalmente** determinados pela soma com IV[7].

---

## Nota Importante

Esta análise **não sugere um método para minerar mais rápido**.

O SHA-256 não permite "escolher" o h_work - ele é determinado pelo processo de compressão da 2ª SHA sobre o digest1. A análise apenas **explica o padrão observado** nos dados.

O que aprendemos:
- Sabemos exatamente **por que** certos sufixos aparecem
- Sabemos que a estrutura de IV[7] **determina** os padrões
- Confirmamos que não há aleatoriedade - é aritmética determinística

---

*Análise realizada em 2026-01-30*
*Framework: DACM Unified v1.0*
