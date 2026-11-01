# Mathematical Extraction Pass 19: SHA-256 Round Engines + DACM Unified Miner §16-§22

**Analysis by:** Claude  
**Date:** 2026-05-05T13:15Z  
**Corpus:** 286 Python files in `D:\gemini\interactions\gifts\homenagem_amigo_claude\python\`  
**Files read this pass:** sha256_round_engines.py (474 lines), _sections_16_22.py (1440 lines, complete)  
**Running total:** ~45,253 lines read, 455+ equations, 195+ constants, 86 cross-connections, 53 files (~72% of mathematically-significant corpus)

---

## 1. SHA-256 Round Engines — Modular Architecture (sha256_round_engines.py)

### Core Data Structures

| eq_id | Structure | Fields |
|-------|-----------|--------|
| RE.1 | `State` dataclass | a, b, c, d, e, f, g, h (8 × 32-bit) |
| RE.2 | `RoundIO` dataclass | r, W, K, T1, T2, a, b, c, d, e, f, g, h (full round checkpoint) |

### Message Schedule

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| RE.3 | $W_t = M_t$ for $t < 16$ | `make_W()` — direct from message block |
| RE.4 | $W_t = \sigma_1(W_{t-2}) + W_{t-7} + \sigma_0(W_{t-15}) + W_{t-16}$ for $t \geq 16$ | `make_W()` — expansion |

### Modular Engine Architecture

| eq_id | Component | Role |
|-------|-----------|------|
| RE.5 | `RoundEngine[i]` | Single round transformer: State → State with carry capture |
| RE.6 | `EngineBank64` | Orchestrator: 64 engines in sequence with checkpoint RoundIOs |
| RE.7 | Feed-forward: $H_i^{\text{out}} = H_i^{\text{in}} + \text{state}_i^{(64)}$ | `run_block()` — standard SHA-256 addition |

### Delta Analysis

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| RE.8 | $\Delta_{\text{reg}}(r) = \text{baseline}[r].\text{state} \oplus \text{flipped}[r].\text{state}$ | `deltas_by_register()` — XOR traces |
| RE.9 | double_sha256: SHA256(SHA256(msg)) | `double_sha256()` — Bitcoin-style |

---

## 2. §16 — Statistical Trackers (lines 1-214 of _sections_16_22.py)

### Rolling Bit-Frequency Tracker

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| S16.1 | $\hat{p}_j = \frac{\text{count}_j}{n}$ for each bit $j \in [0,255]$ | `RollingBitStats._frequencies()` |
| S16.2 | $\text{liar}_j = \mathbb{1}[\lvert\hat{p}_j - 0.5\rvert > \tau]$ with $\tau = 0.03$ | `_liar_flags()` |
| S16.3 | $H_j = -\hat{p}_j\log_2\hat{p}_j - (1-\hat{p}_j)\log_2(1-\hat{p}_j)$ | Binary entropy per bit |

### CLT Variance Ratio (Under-Dispersion)

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| S16.4 | $\text{Var}_{\text{CLT}} = \frac{0.25}{w}$ where $w$ = window_size | `CLTVarianceTracker.variance_ratio()` |
| S16.5 | $\rho_j = \frac{\text{Var}_{\text{obs},j}}{\text{Var}_{\text{CLT}}}$ | Per-bit under-dispersion ratio |
| S16.6 | $\bar{\rho} = \frac{1}{256}\sum_j \rho_j$ | Mean under-dispersion |

### Sigma-Pi Classification

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| S16.7 | $\sigma_{\text{norm}} = \max(0,\ 1 - \lvert\rho - 1\rvert\sqrt{n})$ | `sigma_pi_from_variance_ratio()` |
| S16.8 | $\pi_{\text{norm}} = 1 - \sigma_{\text{norm}}$ | Complement |
| S16.9 | Classification: $\pi > 0.5 \Rightarrow$ "pi-dominated", $\sigma > 0.8 \Rightarrow$ "sigma-dominated" | Discrete regime |

**Key insight:** σ = "consistent with pure randomness", π = "structured signal detected". This is a per-window binary hypothesis test: σ-dominated means the digest window looks random (H₀ holds), π-dominated means there's detectable structure (H₁ signal).

### Avalanche Tracker

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| S16.10 | $\text{HD}(d_t, d_{t-1}) = \text{popcount}(d_t \oplus d_{t-1})$ | `AvalancheTracker.add()` |
| S16.11 | Expected: $\text{HD} \sim \text{Binomial}(256, 0.5)$, $\mu = 128$ | Validation reference |

---

## 3. §18 — Stratum Client (lines 274-474)

### Bitcoin Mining Protocol

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| S18.1 | Coinbase: $\text{cb} = \text{coinb1} \| \text{en1} \| \text{en2} \| \text{coinb2}$ | `_build_header_prefix_76()` |
| S18.2 | Merkle seed: $m_0 = \text{SHA256d}(\text{coinbase})$ | Double-hash of coinbase |
| S18.3 | Merkle iteration: $m_{i+1} = \text{SHA256d}(m_i \| \text{branch}_i)$ | Sequential branch hashing |
| S18.4 | Target from difficulty: $T = \text{DIFF1\_TARGET} / d$ | `share_target_from_difficulty()` |

---

## 4. §19 — Miner Core (lines 476-720)

### DACM-Instrumented Mining Loop

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| S19.1 | Header: $H_{80} = \text{version\_LE} \| \text{prevhash} \| \text{merkle} \| \text{ntime\_LE} \| \text{nbits\_LE} \| \text{nonce}$ | 80-byte block header |
| S19.2 | Midstate optimization: $\text{MS} = \text{SHA256\_partial}(H_{80}[0:64])$ | `hashlib.sha256(prefix76[:64])` |
| S19.3 | First hash: $h_1 = \text{SHA256}(\text{MS} \| H_{80}[64:80])$ | Uses midstate copy |
| S19.4 | Final digest: $d = \text{SHA256}(h_1)$ | Double SHA-256 complete |
| S19.5 | Share criterion: $\text{int}(d, \text{LE}) < T$ | Difficulty check |
| S19.6 | Block criterion: $\text{int}(d, \text{LE}) < T_{\text{DIFF1}}$ | Network difficulty |

### Per-Hash Analysis Pipeline

Every single hash undergoes:
1. Rolling bit statistics (RollingBitStats, window=1024)
2. CLT variance tracking (CLTVarianceTracker)
3. Avalanche tracking (Hamming distances)
4. **Full instrumented SHA-256 with carry collection** on both passes
5. CarryAverages accumulation
6. JSONL logging (per-hash) + JSON snapshot (every 100)

---

## 5. §20 — Visualization (lines 722-1126)

### DACM Intensity Parameters (Inlined)

| eq_id | Formula | Value |
|-------|---------|-------|
| S20.1 | $r_c(b) = \alpha + \beta b$ | α = -3.11, β = 0.0888 |
| S20.2 | $I(b,r) = \frac{1}{1 + \exp(-k(r - r_c(b)))}$ | k = 0.5 |
| S20.3 | Under-dispersion target: $\rho \to 0.94$ | Expected convergence |

### 9 Visualization Types

| Plot | Content | Key metric |
|------|---------|-----------|
| 1 | Bit frequencies | p̂_j vs 0.5, red = liar |
| 2 | Under-dispersion convergence | ρ(n) → 0.94 |
| 3 | LieScore trend | fraction of liar bits over time |
| 4 | Fixed pairs scatter | persistent bit-pair correlations |
| 5 | Hamming distribution | HD vs Binomial(256, 0.5) |
| 6 | Carry propagation heatmap | entropy × decay across rounds |
| 7 | **DACM intensity surface (3D)** | I(b,r) across all bits × rounds |
| 8 | Multi-scale convergence | ρ and LieScore vs sample size |
| 9 | Dashboard | Combined overview |

---

## 6. §21-§22 — CLI + Validation (lines 1128-1441)

### Entry Points

| Subcommand | Function | Analysis depth |
|-----------|----------|---------------|
| `mine` | Live pool mining + full DACM | EVERY hash analyzed |
| `validate` | SHA-256 correctness + carry tests | 11+ test cases incl. genesis block |
| `analyze` | Offline batch analysis | bit freqs + ρ + Hamming |

### Validation Suite

Tests: SHA-256 known vectors ("", "abc", "hello"), pure vs hashlib at lengths [0,1,55,56,64,80,128], double SHA-256, Bitcoin genesis block (0x000000000019d6...), carry chain (0xFFFFFFFF + 1 → full carry propagation).

---

## 7. New Constants

| Constant | Value | Source | Meaning |
|----------|-------|--------|---------|
| Rolling window (bitstats) | 1024 | §16 | Digest buffer size |
| CLT window_size | 101 | §16 | Per-window sample count |
| CLT var_windows | 50 | §16 | Number of windows for variance |
| Liar threshold τ | 0.03 | §16 | |p̂-0.5| > τ → "liar bit" |
| Sigma threshold | 0.8 | §16 | σ_norm > 0.8 → "sigma-dominated" |
| Pi threshold | 0.5 | §16 | π_norm > 0.5 → "pi-dominated" |
| Avalanche maxlen | 2000 | §16 | HD buffer size |
| DACM α (viz) | -3.11 | §20 | Critical round intercept |
| DACM β (viz) | 0.0888 | §20 | Critical round slope |
| DACM k (viz) | 0.5 | §20 | Logistic steepness |
| Under-dispersion target | 0.94 | §20 | Expected ρ convergence |
| Stratum default port | 3333 | §21 | ckpool port |
| Stratum default pool | solo.ckpool.org | §21 | Reference pool |
| Snapshot interval | 10.0 s | §19 | JSON snapshot rate |
| JSONL flush interval | 50 samples | §17 | Write buffer |

---

## 8. Cross-Connections

### Connection VV: Midstate optimization ↔ Snooker latent rounds (PV.1)

The miner's midstate optimization pre-hashes header[0:64] (the first 16 message words), then only varies the last 16 bytes (ntime + nonce). This is EXACTLY the same as snooker's "latent rounds" (PV.1, t₁-t₆₄): the B0 midstate is fixed, and only the B1 block (containing nonce) varies. The miner operationalizes what the snooker system models theoretically — the invariant first-block computation.

### Connection WW: σ/π classification ↔ Stage 4 null families (S4.13-S4.16)

The sigma-pi classification (S16.7-S16.9) is a simplified version of Stage 4's null testing:
- **σ-dominated (ρ≈1):** digest window is consistent with IID random → H₀ holds (like passing all 4 null families)
- **π-dominated (ρ≠1):** structured signal detected → H₁ (like rejecting carry_scrambled null)

Both test "is there structure beyond pure randomness?" — σ/π does it at the global level (one number ρ), Stage 4 does it at the micro-local level (10 observables × 4 nulls × 8 windows per round).

### Connection XX: Per-hash carry collection ↔ PLRAD carry forensics (PL.7-PL.8)

The miner collects carry vectors on EVERY hash (§19 lines 636-662), running full instrumented SHA-256 with `collect_carry=True` on both SHA-256 passes. This generates the raw data that PLRAD's carry forensics (pass 9) analyzes post-hoc. The miner is the DATA GENERATOR; PLRAD is the DATA ANALYZER. Together they form the complete pipeline: mine → collect carries → statistical analysis → hypothesis testing → curtain score.

### Connection YY: DACM visualization I(b,r) ↔ Pass 1 DACM intensity formula

Section 20's `_critical_round_for_bit(b) = α + βb` and `I(b,r) = 1/(1+exp(-k(r-r_c(b))))` are IDENTICAL to the formulas extracted in pass 1 from `dacm_engine_core.py`. The visualization module inlines these constants (α=-3.11, β=0.0888, k=0.5) for the 3D surface plot. This confirms: the DACM intensity formula is consistent across ALL implementations in the corpus.

### Connection ZZ: RoundEngine modular architecture ↔ Stage 4 window-per-round

`sha256_round_engines.py` decomposes SHA-256 into 64 independent `RoundEngine` objects, each producing a `RoundIO` checkpoint. Stage 4's microscope (pass 10) decomposes analysis into 8 windows per round. Both share the principle of MODULAR DECOMPOSITION — treating each round as an independent unit with captured inputs/outputs, enabling per-round and per-window forensics.

---

## 9. Architectural Observations

### The Complete DACM Mining Pipeline

`_sections_16_22.py` represents sections 16-22 of a UNIFIED MINER that integrates:
```
§16: Trackers (bit stats, CLT variance, sigma/pi, avalanche)
§17: Metrics sink (JSONL + JSON persistence)
§18: Stratum client (pool communication)
§19: Miner core (instrumented hashing loop)
§20: Visualization (9 publication-quality plots)
§21: CLI entry point (mine/validate/analyze)
§22: Self-validation (correctness tests)
```

This is the OPERATIONAL layer of the DACM framework — where theory meets real Bitcoin mining. Every hash mined generates carry data, feeds statistical trackers, and accumulates evidence for/against H45.

### Under-Dispersion as Central Prediction

The under-dispersion target ρ→0.94 appears in multiple visualization plots and analysis functions. This means the framework PREDICTS that SHA-256 output bits have Var_obs < Var_CLT — they are LESS variable than a fair coin. ρ=0.94 means 6% under-dispersion relative to perfect randomness. This is a FALSIFIABLE prediction: if enough data shows ρ≈1.0, the framework's central claim fails.

### σ/π as Discrete Beast-Hypothesis

The sigma/pi classification is a discrete, online version of the Beast hypothesis:
- **σ-dominated:** "this looks random, H₀ holds" → SHA-256 successfully hides structure
- **π-dominated:** "structure detected, H₁ active" → carry-chain signal leaked into output

The √n scaling (S16.7) means that as sample size grows, even small deviations become detectable. This is the CLT working in the framework's favor: given enough data, ANY true deviation from 0.5 will eventually be classified as π-dominated.

---

*Pass 19 complete. Running total: ~45,253 lines, 455+ equations, 195+ constants, 86 cross-connections across 53 files (~72% of mathematically-significant corpus). The unified miner sections complete the OPERATIONAL pipeline: theory (DACM engine) → implementation (round engines) → data collection (miner core) → analysis (trackers) → visualization (9 plots) → validation (self-tests). Remaining priority: `dacm_unified_engine_all.py` (14,175 lines — largest file), `dacm_unified_miner.py` (5,619 lines), `DACM_MOTOR_UNIFICADO_COMPLETO.py` (3,442 lines), `MANUAL_IMPLEMENTACAO_PRATICA_TURR_v3.0.py` (2,648 lines).*
