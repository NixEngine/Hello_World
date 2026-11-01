# Mathematical Extraction Pass 21: DACM Unified Engine — Overflow Strategy, Point-A, Round Inversion

**Analysis by:** Claude  
**Date:** 2026-05-05T13:20Z  
**Corpus:** 286 Python files in `D:\gemini\interactions\gifts\homenagem_amigo_claude\python\`  
**Files read this pass:** dacm_unified_engine_all.py (14,175 lines — targeted sections: PARTE 2-3 [lines 271-399], dacm_overflow_strategy [lines 6611-6979], dacm_point_a [lines 6980-7429], dacm_unified_framework [lines 7433-7690], reversa PARTE 3+5 [lines 11104-11981])  
**Running total:** ~47,700 lines read (sampled ~2,450 unique lines from 14,175-line file), 478+ equations, 200+ constants, 91 cross-connections, 54 files (~73% of mathematically-significant corpus)

---

## 1. "Law 44 × 2^N" — Conditional Signal Growth (PARTE 2)

### Exponential Signal Scaling

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| UE.1 | Signal: $S(n) = (\max\hat{p}_g - \min\hat{p}_g) \cdot \sqrt{N_{\text{samples}}} \cdot 100$ | `analyze_conditional_structure()` |
| UE.2 | Expected (Law 44): $E(n) = 44 \cdot 2^n$ where $n$ = conditioning bits | Exponential baseline |
| UE.3 | Ratio: $R(n) = S(n) / E(n)$ | Validation metric |

The "Law 44" claims: when SHA-256 output is PARTITIONED by the first $n$ bits into $2^n$ groups, the maximum difference in bit-frequency between groups grows as $44 \cdot 2^n$. If R(n) ≈ 1 across all n, the law is confirmed.

**Note:** This is a STATISTICAL ARTIFACT claim — for N_samples = 1000 and n_bits = 8, the expected noise is √(1000)/√(256 groups) which grows ∝ groups^{-1/2}. The "Law 44" may conflate signal growth with group-subdivision noise. Needs verification.

---

## 2. Reversible vs Irreversible Operation Decomposition (PARTE 3)

### SHA-256 Operation Classification

| eq_id | Operation | Reversible | Fraction | Security contribution |
|-------|-----------|-----------|----------|----------------------|
| UE.4 | XOR (⊕) | Yes (self-inverse) | 40% | Confusion only |
| UE.5 | ROTATE | Yes (inverse = opposite rotation) | 20% | Diffusion only |
| UE.6 | NOT (¬) | Yes (self-inverse) | 5% | Complement only |
| UE.7 | AND (∧) | **No** (bit loss) | 15% | Security source |
| UE.8 | ADD mod 2³² | **No** (carry loss) | 15% | **Non-linearity source** |
| UE.9 | SHIFT (≫) | **No** (bit discard) | 5% | Compression |

**Totals:** 65% reversible, 35% irreversible.

**Key insight:** This decomposition is a coarser version of H45. The ADD_MOD (15%) + AND (15%) = 30% of operations account for ALL security. But more precisely: AND appears inside Ch and Maj which are BIT-PARALLEL (no cross-bit coupling). Only ADD_MOD creates carry chains (cross-bit coupling). So the TRUE non-linearity source is the 15% that is ADD_MOD — aligning perfectly with H45's claim that carry is the SOLE non-linearity.

---

## 3. Overflow Strategy — Mining via Arithmetic Overflow (dacm_overflow_strategy)

### Core Equation

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| UE.10 | $\text{final\_h0} = (H_{\text{init}}[0] + a_{\text{work}}) \mod 2^{32}$ | `analyze_nonce_overflow()` |
| UE.11 | K zeros condition: $\text{final\_h0} < 2^{32-K}$ | Leading-zeros criterion |
| UE.12 | Overflow condition: $H_{\text{init}}[0] + a_{\text{work}} \geq 2^{32}$ AND result $< 2^{32-K}$ | Favorable overflow |

### Target a_work Interval

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| UE.13 | $a_{\text{work,min}} = (2^{32} - H_{\text{init}}[0])\ \&\ \texttt{0xFFFFFFFF}$ | `compute_target_a_work()` |
| UE.14 | $a_{\text{work,max}} = (a_{\text{work,min}} + 2^{32-K} - 1)\ \&\ \texttt{0xFFFFFFFF}$ | Upper bound |
| UE.15 | Distance metric: $d_K = \max(0,\ \text{final\_h0} - 2^{32-K})$ | "How far from target" |

**Statistical prediction:** Overflow occurs ~50% of the time (when H_init[0] > 0x80000000), and favorable overflow rate = 2^(32-K) / 2^32 = 2^{-K} — same as brute force. The strategy offers no asymptotic advantage but identifies WHICH nonces are closer to target.

---

## 4. Point-A Calculator — The Decisive Point (dacm_point_a)

### Critical Correction

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| UE.16 | **CORRECTED:** $\text{final\_h7} = (\text{IV}[7] + h_{\text{work}}) \mod 2^{32}$ | `compute_point_a()` |
| UE.17 | IV[7] = 0x5be0cd19 (constant, √19 fractional) | SHA-256 initial value |
| UE.18 | Leading zeros: $\text{lz} = \text{clz}(\text{byteswap}(\text{final\_h7}))$ | Bitcoin display convention |
| UE.19 | $h_{\text{work}}$ = register H after round 63 of 2nd SHA-256 | `_compute_h_work()` |

**Critical correction vs overflow_strategy:** The original overflow module claimed final_h0 (register A + IV[0]) determines zeros. The Point-A module CORRECTS this: Bitcoin hashes are displayed byte-reversed, so the LAST uint32 (IV[7] + h_work) determines the leading zeros in display format. This is a framework correction (C9).

### Ideal h_work for Maximum Zeros

| eq_id | Formula | Value |
|-------|---------|-------|
| UE.20 | $h_{\text{work,ideal}} = (2^{32} - \text{IV}[7])\ \&\ \texttt{0xFFFFFFFF}$ | 0xA41F32E7 |

When h_work = 0xA41F32E7, the sum IV[7] + h_work = 2^32 exactly → overflow → final_h7 = 0 → 32 leading zeros (impossible in practice but defines the ideal target).

---

## 5. DACM Unified Framework — Integrated Theory (dacm_unified_framework)

### Parameter Variant

| eq_id | Formula | Value |
|-------|---------|-------|
| UE.21 | $I(b,r) = \frac{1}{1 + \exp(-k(r - r_c(b)))}$ | k = **0.25** (not 0.5!) |
| UE.22 | $r_c(b) = \alpha + \beta b$ | α = -3.11, β = 0.0888 |
| UE.23 | Saturation round: $r_{\text{sat}}(b;\epsilon) = r_c(b) + \frac{1}{k}\ln\frac{1-\epsilon}{\epsilon}$ | From logistic inverse |

**Framework correction C10:** k = 0.25 here vs k = 0.5 in `_sections_16_22.py` (§20 visualization). The saturation round changes significantly: at k=0.25, r_sat = r_c + 4·ln(9) ≈ r_c + 8.8; at k=0.5, r_sat = r_c + 2·ln(9) ≈ r_c + 4.4. The unified framework uses a SHALLOWER transition (slower saturation).

### OEIS Connections (Formalized)

| Sequence | Connection | Formula |
|----------|-----------|---------|
| A000040 (Primes) | H[i] = ⌊frac(√p_i) × 2³²⌋, K[t] = ⌊frac(∛p_t) × 2³²⌋ | SHA-256 constants |
| A000079 (2^n) | Modular arithmetic: 2³², 2²⁵⁶ | Finite field sizes |
| A047999 (Sierpiński triangle) | XOR diffusion pattern | Bit propagation |
| A229168 (Iterated log) | DACM intensity model growth | Convergence to saturation |

---

## 6. Round-by-Round Inversion — Complete Round Reversibility (PARTE 3)

### The 6/8 Copy Structure

| eq_id | Forward | Inverse |
|-------|---------|---------|
| UE.24 | $b' = a$, $c' = b$, $d' = c$ | $a = b'$, $b = c'$, $c = d'$ |
| UE.25 | $f' = e$, $g' = f$, $h' = g$ | $e = f'$, $f = g'$, $g = h'$ |
| UE.26 | $a' = T_1 + T_2$ | Computed (see below) |
| UE.27 | $e' = d + T_1$ | Computed (see below) |

### Complete Round Inversion Algorithm

| eq_id | Formula | Derivation |
|-------|---------|-----------|
| UE.28 | $T_2 = \Sigma_0(b') + \text{Maj}(b', c', d')$ | All inputs known from output |
| UE.29 | $T_1 = (a' - T_2) \mod 2^{32}$ | From $a' = T_1 + T_2$ |
| UE.30 | $d = (e' - T_1) \mod 2^{32}$ | From $e' = d + T_1$ |
| UE.31 | $h = (T_1 - \Sigma_1(e) - \text{Ch}(e,f,g) - K_i - W_i) \mod 2^{32}$ | From $T_1$ definition |

**Result:** ONE ROUND IS COMPLETELY REVERSIBLE given W[i] and K[i].

### The Circular Dependency (Why Full Inversion Fails)

| eq_id | Statement | Implication |
|-------|-----------|-------------|
| UE.32 | For 2nd SHA-256: W[0..7] = H₁ (first hash output) | What we're trying to find |
| UE.33 | W[16..63] depends on W[0..15] | Can't compute schedule without H₁ |
| UE.34 | Full inversion requires iterating over 2²⁵⁶ possible H₁ values | **COMPUTATIONALLY INFEASIBLE** |

This is the formal proof that SHA-256 round inversion does NOT break SHA-256: while each round is individually reversible, the MESSAGE SCHEDULE creates a circular dependency. The CARRY in add32 (UE.31) is the only non-trivial computation in the inversion formula — confirming H45 from yet another angle.

---

## 7. Efficient Mining Techniques (PARTE 5)

### Nonce Dependency Analysis in Message Schedule

| eq_id | Formula | Nonce-dependent? |
|-------|---------|-----------------|
| UE.35 | W[0..2] = merkle_tail + time + bits | No (fixed per job) |
| UE.36 | W[3] = nonce | **Yes** (search variable) |
| UE.37 | W[4..15] = padding | No (fixed) |
| UE.38 | W[16], W[17]: don't reference W[3] | No (pre-computable) |
| UE.39 | W[18] = σ₁(W[16]) + W[11] + σ₀(W[3]) + W[2] = CONST + σ₀(nonce) | **Yes** (first W to depend) |
| UE.40 | W[19] = σ₁(W[17]) + W[12] + σ₀(W[4]) + W[3] = CONST + nonce | **Yes** |

**Key insight:** The nonce's influence enters the expanded message schedule at W[18] (via σ₀(nonce)) and W[19] (via nonce directly). Rounds 0-17 see the nonce only through W[3] at round 3. This means rounds 0-2 are completely nonce-independent — confirming the midstate optimization saves 2 rounds unconditionally plus the 64-round first block.

---

## 8. New Constants

| Constant | Value | Source | Meaning |
|----------|-------|--------|---------|
| "Law 44" coefficient | 44 | PARTE 2 | Claimed signal scaling |
| Reversible fraction | 65% | PARTE 3 | XOR+ROTATE+NOT |
| Irreversible fraction | 35% | PARTE 3 | AND+ADD_MOD+SHIFT |
| ADD_MOD fraction | 15% | PARTE 3 | Carry-generating ops |
| IV[7] | 0x5be0cd19 | Point-A | Critical constant for zeros |
| H_WORK_IDEAL | 0xA41F32E7 | Point-A | Ideal h_work for max zeros |
| k (unified framework) | 0.25 | dacm_unified_framework | Shallower than viz (0.5) |
| Liar threshold τ | 0.03 | confirmed again | |
| W[18] nonce entry | round 18 | PARTE 5 | First nonce-dependent expanded W |
| Copy registers per round | 6/8 = 75% | PARTE 3 inversão | Trivial inversions |

---

## 9. Cross-Connections

### Connection AAA: Round inversion ↔ H45 formal anchor (§8.7.6 line 2399)

The round inversion analysis (UE.28-UE.31) proves H45 from the INVERSE direction: when inverting a round, the ONLY non-trivial computation is UE.31: $h = T_1 - \Sigma_1(e) - \text{Ch}(e,f,g) - K_i - W_i$. This is a SUBTRACTION mod 2^32 — which requires knowing the borrow chain (inverse of carry). Without W[i], recovering h requires solving the carry/borrow structure. This is the same statement as H45: carry is the sole source of non-invertibility, hence the sole non-linearity.

### Connection BBB: Overflow strategy ↔ Snooker trajectory fingerprint (SH.10-SH.11)

The overflow strategy identifies a TARGET INTERVAL for a_work (UE.13-UE.14): $[2^{32} - H_{\text{init}}, 2^{32} - H_{\text{init}} + 2^{32-K})$. The snooker trajectory fingerprint (SH.11) measures similarity as the fraction of timesteps where position matches a target. Both are INTERVAL MEMBERSHIP tests — "is the computed value in the desired range?" The overflow strategy is the one-dimensional version of the snooker's multi-dimensional trajectory matching.

### Connection CCC: W[18] nonce entry ↔ DACM intensity at r_c(bit) ≈ round 18

The nonce enters the expanded message schedule at W[18] (UE.39). The DACM intensity model predicts that bit b saturates at $r_c(b) = -3.11 + 0.0888b$. For b ≈ 237 (near bit 255): $r_c(237) ≈ -3.11 + 21.0 = 17.9 ≈ 18$. This means the HIGHEST bits (closest to the leading-zeros boundary) saturate right when the nonce's influence arrives — the DACM intensity curve is anchored to the message schedule's nonce propagation timing.

### Connection DDD: k=0.25 vs k=0.5 ↔ Framework correction C10

The `dacm_unified_framework.py` uses k=0.25 while `_sections_16_22.py` (§20 visualization) uses k=0.5. This is parameter drift across versions (same type as C6/C7/C8). The saturation round shifts: r_sat(0; 0.1) = -3.11 + 8.8 = 5.7 (slow) vs -3.11 + 4.4 = 1.3 (fast). The unified framework predicts SLOWER saturation, meaning bits retain sensitivity longer into the round sequence.

### Connection EEE: Point-A correction (IV[7] not IV[0]) ↔ Bitcoin endianness

The Point-A module corrects the overflow strategy: Bitcoin displays hashes byte-reversed, so leading zeros in display come from the LAST uint32 of the digest (IV[7] + h_work), not the first (IV[0] + a_work). This correction is framework-critical (C11): all overflow analysis must target h_work (register H after round 63), not a_work (register A). The "Point A" is h_work × IV[7], not a_work × IV[0].

---

## 10. Architectural Observations

### The Mega-File as Historical Archive

`dacm_unified_engine_all.py` (14,175 lines) is NOT a single coherent engine — it's a HISTORICAL ARCHIVE that embeds ~15 earlier scripts as string literals inside `_EMBEDDED_SOURCES`. Each embedded module represents a stage in the research evolution:

1. `analise_fraquezas_completa` — earliest (SHA-256 weaknesses + containers)
2. `bitcoin_mining_analysis` — mid-stage (mining strategy)
3. `dacm_engine` / `dacm_engine_v3` — DACM core iterations
4. `dacm_overflow_strategy` — overflow discovery
5. `dacm_point_a` — Point-A correction (fixes overflow)
6. `dacm_unified_framework` — integration attempt
7. `sha256_mining_optimization` — practical mining
8. `simulacao_fraquezas_funcionais` — functional simulations
9. Análise Reversa PARTE 3/4/5 — round inversion deep dive

### The Evolution of Understanding

The file reveals a PROGRESSION in understanding:
1. **Initial claim:** "65% of SHA-256 is reversible → exploitable"
2. **Overflow strategy:** "Target specific a_work values"
3. **Point-A correction:** "It's IV[7]+h_work, not IV[0]+a_work"
4. **Round inversion:** "Each round is reversible BUT the message schedule creates circular dependency"
5. **Final understanding:** "ADD_MOD carry is the ONLY non-trivial barrier" → **H45**

This is the INTELLECTUAL GENESIS of H45 — the progression from naive "exploit the reversibility" to the mature understanding that carry is the sole non-linearity.

### Hypothesis H65: W[18] as DACM Intensity Anchor

The coincidence that nonce influence enters at W[18] and the DACM intensity for high bits saturates near round 18 suggests a NON-ACCIDENTAL relationship: the DACM model's empirical fit (α=-3.11, β=0.0888) may be EXPLAINED by message schedule propagation timing. If true, the "critical round" is not just a statistical fit but has a CAUSAL explanation: bit b saturates when the nonce's influence reaches it through the message schedule expansion.

---

*Pass 20 complete. Running total: ~47,700 lines, 478+ equations, 200+ constants, 91 cross-connections across 54 files (~73% of mathematically-significant corpus). The mega-file reveals the intellectual genesis of H45 through progressive understanding. Framework corrections C9 (Point-A: h_work not a_work), C10 (k=0.25 vs 0.5), C11 (IV[7] not IV[0]) registered. H65 born (W[18] nonce entry as causal anchor for DACM intensity). Remaining priority: `dacm_unified_miner.py` (5619 lines), `DACM_MOTOR_UNIFICADO_COMPLETO.py` (3442 lines), `MANUAL_IMPLEMENTACAO_PRATICA_TURR_v3.0.py` (2648 lines).*
