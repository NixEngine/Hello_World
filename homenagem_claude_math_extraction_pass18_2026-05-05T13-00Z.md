# Mathematical Extraction Pass 18: Snooker SHA-256d Expansion + Position Mapping

**Analysis by:** Claude  
**Date:** 2026-05-05T13:00Z  
**Corpus:** 286 Python files in `D:\gemini\interactions\gifts\homenagem_amigo_claude\python\`  
**Files read this pass:** snooker_sha256d_initial_640_bits.py (806 lines), snooker_sha256d_position_variation.py (607 lines), snooker_physics.py (218 lines), snooker_simulator.py (208 lines)  
**Running total:** ~43,339 lines read, 435+ equations, 185+ constants, 81 cross-connections, 51 files (~70% of mathematically-significant corpus)

---

## 1. Snooker Physics — Register-to-Position Mapping (snooker_physics.py)

### Core Position Encoding

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| SP.1 | $x = \text{reg\_val} \gg 16$ (upper 16 bits) | `register_to_position()` |
| SP.2 | $y = \text{reg\_val}\ \&\ \texttt{0xFFFF}$ (lower 16 bits) | Same function |
| SP.3 | Table resolution: $65536 \times 65536 = 2^{32}$ positions | Full 32-bit register → (x,y) |
| SP.4 | Display transform: $x_{\text{disp}} = \frac{x}{65536} \cdot 800$, $y_{\text{disp}} = \frac{y}{65536} \cdot 400$ | Pixel coordinates |

The mapping is a BIJECTION: every possible 32-bit register value maps to a unique (x,y) position on the table. This means the SHA-256 state space embeds into 2D without collision.

### Velocity Computation

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| SP.5 | $\Delta x = x_2 - x_1$, $\Delta y = y_2 - y_1$ | `compute_velocity()` |
| SP.6 | $\text{speed} = \sqrt{\Delta x^2 + \Delta y^2}$ | Euclidean distance |
| SP.7 | $\theta = \arctan(\Delta y / \Delta x)$ | Direction angle |

---

## 2. Snooker Simulator — Full SHA-256 Implementation (snooker_simulator.py)

### SHA-256 Compression Function (Pure Python)

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| SS.1 | $\text{ROR}(x, n) = (x \gg n) \mid (x \ll (32-n))$ & $\texttt{0xFFFFFFFF}$ | `right_rotate()` |
| SS.2 | $\sigma_0(x) = \text{ROR}(x,7) \oplus \text{ROR}(x,18) \oplus (x \gg 3)$ | `sigma0()` — message schedule |
| SS.3 | $\sigma_1(x) = \text{ROR}(x,17) \oplus \text{ROR}(x,19) \oplus (x \gg 10)$ | `sigma1()` — message schedule |
| SS.4 | $\Sigma_0(x) = \text{ROR}(x,2) \oplus \text{ROR}(x,13) \oplus \text{ROR}(x,22)$ | `Sigma0()` — compression |
| SS.5 | $\Sigma_1(x) = \text{ROR}(x,6) \oplus \text{ROR}(x,11) \oplus \text{ROR}(x,25)$ | `Sigma1()` — compression |
| SS.6 | $\text{Ch}(x,y,z) = (x \land y) \oplus (\neg x \land z)$ | `Ch()` — choose |
| SS.7 | $\text{Maj}(x,y,z) = (x \land y) \oplus (x \land z) \oplus (y \land z)$ | `Maj()` — majority |
| SS.8 | $T_1 = h + \Sigma_1(e) + \text{Ch}(e,f,g) + K_t + W_t$ | Round computation |
| SS.9 | $T_2 = \Sigma_0(a) + \text{Maj}(a,b,c)$ | Round computation |
| SS.10 | Register update: $h \leftarrow g$, $g \leftarrow f$, ..., $a \leftarrow T_1 + T_2$ | Compression cycle |

### Bit-to-Geographic Mapping

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| SS.11 | $\text{lat\_base} = \frac{r + 0.5}{8} \cdot 180 - 90$ where $r$ = register index | `map_bits_to_coordinates()` |
| SS.12 | $\text{norm\_val} = \frac{(\text{reg\_val} + \text{bit\_idx}) \mod 2^{32}}{2^{32}}$ | Normalized position |
| SS.13 | $\text{lon} = \text{norm\_val} \cdot 360 - 180$ | Longitude from register |
| SS.14 | $\text{lat} = \text{lat\_base} + (\text{bit\_val} - 0.5) \cdot 2$ | Latitude: ±1° by bit value |

This mapping places each of the 256 bits (8 regs × 32 bits) at a unique geographic coordinate per round. The double SHA-256d generates 128 rounds of positions.

---

## 3. SHA-256d Full 640-bit Expansion (snooker_sha256d_initial_640_bits.py)

### Architecture

This file generalizes from 128 active bits (B1 block) to all 640 initial bits of a Bitcoin block header:
- 20 words × 32 bits = 640 bits total
- 192 global rounds (64 per SHA-256 pass × 3? — actually SHA-256d = 2 passes × 64 + padding)
- 5 layout variants tested against baseline

### Header Field Layout

| Field | Words | Start Word |
|-------|-------|-----------|
| Version | 1 (32 bits) | 0 |
| Prev Block | 8 (256 bits) | 1 |
| Merkle Root | 8 (256 bits) | 9 |
| Time | 1 (32 bits) | 17 |
| Bits | 1 (32 bits) | 18 |
| Nonce | 1 (32 bits) | 19 |

### Initial Position Seeding

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| SH.1 | $\theta = \frac{w \mod 20}{20} \cdot 2\pi + (l \mod 8 - 3.5) \cdot 0.031$ | `seed_velocity_for_full_bit()` — angular direction |
| SH.2 | $v = 0.0018 + (l \mod 5) \cdot 0.00008 + (w \mod 5) \cdot 0.00005$ | Speed from word/local indices |
| SH.3 | $v_x = v \cos\theta$, $v_y = v \sin\theta$ | Cartesian velocity |
| SH.4 | $x = c_x + (\text{col} - 3.5) \cdot 0.0108$, $y = c_y + (\text{row} - 1.5) \cdot 0.0175$ | Slot position within rack |

Where $w$ = word_index [0-19], $l$ = local_index [0-31], $(c_x, c_y)$ = word group center.

### 5 Layout Variants (Permutations)

| eq_id | Variant | Permutation formula |
|-------|---------|-------------------|
| SH.5 | Baseline | $\text{slot}(w, l) = 32w + l$ (identity) |
| SH.6 | Rotate-in-word | $\text{slot}(w, (l+8) \mod 32)$ |
| SH.7 | Cycle-word-racks | $\text{slot}((w+1) \mod 20, l)$ |
| SH.8 | Mirror-local | $\text{slot}(w, 8\lfloor l/8\rfloor + 7 - (l \mod 8))$ |
| SH.9 | Combo-permute | $\text{slot}((7w + (l \mod 5) + 3) \mod 20,\ (5l + 11) \mod 32)$ |

Each variant is verified as a BIJECTION over 640 slots (assertion at line 356).

### Trajectory Fingerprint Comparison

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| SH.10 | Fingerprint: $\text{fp}(b) = ((x_1,y_1), (x_2,y_2), \ldots, (x_T,y_T))$ | `trajectory_fingerprint()` |
| SH.11 | Similarity: $\text{sim}(L, R) = \frac{\sum_{t} \mathbb{1}[L_t = R_t]}{\min(\lvert L\rvert, \lvert R\rvert)}$ | `fingerprint_similarity()` — exact GPS-cell match ratio |
| SH.12 | Position score: compare variant[bit] vs baseline[slot(bit)] | `score_direct_mapping()` |
| SH.13 | Type score: compare within same field group (multiset) | `score_type_multiset()` — Counter intersection |

### Analysis Hypotheses

Three hypotheses tested for what determines trajectory:
1. **Initial position** — the slot determines everything
2. **Ball type** — the field/word determines everything
3. **Combinations** — interaction of position and type matters

The overall_analysis returns which hypothesis dominates.

---

## 4. SHA-256d Position Variation (snooker_sha256d_position_variation.py)

### Global Round Structure

| eq_id | Formula | Value |
|-------|---------|-------|
| PV.1 | Latent rounds: $t_1 \ldots t_{64}$ (B0 midstate fixed) | 64 rounds |
| PV.2 | Active start: $t_{65}$ | LATENT + 1 |
| PV.3 | Forecast reference: $t_{72}$ (8 active rounds for calibration) | 65 + 8 - 1 |
| PV.4 | Active total: 128 rounds | Post-B0 evolution |
| PV.5 | Total global: 192 rounds | 64 latent + 128 active |

### Mode Classification

| Round range | Mode | Meaning |
|-------------|------|---------|
| t1-t64 | `latent` | Position fixed, awaiting B0 completion |
| t65-t72 | `observed` | Active rounds used for trend calibration |
| t73-t192 | `forecast` | Predicted from 8-round active window |

### Layout Variants (128-bit version)

| eq_id | Variant | Permutation |
|-------|---------|-------------|
| PV.6 | Baseline | slot(g, l) = 32g + l |
| PV.7 | Rotate-in-group | slot(g, (l+8) mod 32) |
| PV.8 | Cycle-groups | slot((g+1) mod 4, l) |
| PV.9 | Mirror-local | slot(g, 8⌊l/8⌋ + 7-(l mod 8)) |
| PV.10 | Combo-permute | slot((g + l mod 4) mod 4, (5l+7) mod 32) |

Same bijection verification as 640-bit version but over 128 slots (4 groups × 32 bits).

---

## 5. New Constants

| Constant | Value | Source | Meaning |
|----------|-------|--------|---------|
| TABLE_W, TABLE_H | 65536 | snooker_physics | Full-precision table (2¹⁶ × 2¹⁶) |
| DISPLAY_W, DISPLAY_H | 800, 400 | snooker_physics | Rendering resolution |
| TOTAL_INITIAL_BITS (640) | 640 | sha256d_initial | Full Bitcoin header |
| WORD_COUNT | 20 | sha256d_initial | 640/32 |
| TOTAL_GLOBAL_ROUNDS | 192 | both sha256d files | SHA-256d total |
| LATENT_GLOBAL_ROUNDS | 64 | position_variation | B0 midstate phase |
| ACTIVE_GLOBAL_START_ROUND | 65 | position_variation | First active round |
| FORECAST_REFERENCE_ROUND | 8 | imported from bit_simulator | Calibration window |
| ACTIVE_TOTAL_ROUNDS | 128 | position_variation | Post-latent evolution |
| Slot spacing (x) | 0.0108 | sha256d_initial | Column spacing in rack |
| Slot spacing (y) | 0.0175 | sha256d_initial | Row spacing in rack |
| Base speed | 0.0018 | sha256d_initial | Minimum initial velocity |
| Speed increment (local) | 0.00008 | sha256d_initial | Per local-index increment |
| Speed increment (word) | 0.00005 | sha256d_initial | Per word-index increment |

---

## 6. Cross-Connections

### Connection SS: Position encoding as register-to-space BIJECTION ↔ D_p bit-color trace (§15)

SP.1-SP.2 define the encoding: reg_val → (x,y) via bit-splitting (upper 16 → x, lower 16 → y). The §15 D_p bit-color trace from pass 6/11 tracks WHICH bits change in SHA-256 internal state. The snooker mapping makes this visible by converting abstract bit-changes into SPATIAL MOVEMENTS. Every bit-flip corresponds to a measurable displacement in 2D. This is the visualization layer of the PLRAD forensics pipeline.

### Connection TT: 5 layout variants as CONTROLLED EXPERIMENTS ↔ Stage 4 null families (S4.13-16)

The 5 layout variants (baseline + 4 permutations) test WHAT DETERMINES TRAJECTORY:
- **Position hypothesis** (slot determines all) ↔ geometry_scrambled null
- **Type hypothesis** (field determines all) ↔ register_scrambled null
- **Combination hypothesis** (interaction) ↔ full null (everything scrambled)

This is the SAME experimental design as Stage 4's 4 null families — both systematically decompose structure by varying one factor while holding others constant. The snooker variants test a 640-bit analogue of what Stage 4 tests at the 10-observable × 4-null level.

### Connection UU: Latent/Active/Forecast phase structure ↔ SHA-256 zone structure (Stage 4)

PV.1-PV.5 define three temporal phases:
- **Latent (t1-t64):** no movement, awaiting B0 → Stage 4 "pre-mixing" (before round 6)
- **Active/Observed (t65-t72):** calibration window → Stage 4 Zone A (rounds 6-16)
- **Forecast (t73-t192):** prediction from trend → Stage 4 Control + Zone B (rounds 18-50)

The 8-round active window used for calibration maps directly to FORECAST_REFERENCE_ROUND=8 from the bit_simulator. This creates a natural falsification: if the 8-round trend cannot predict rounds 9+, the trajectory model fails.

---

## 7. Architectural Observations

### The Hierarchy of Snooker Files

```
snooker_simulator.py      — Pure SHA-256 implementation + bit-to-geographic mapping
snooker_physics.py        — Register-to-position (upper16/lower16) + velocity
snooker_bit_simulator.py  — [pass 4] ODE integration, drag/force model, GPS cells
snooker_sha256d_position_variation.py — 128-bit B1 expansion with 5 layout variants
snooker_sha256d_initial_640_bits.py   — Full 640-bit header expansion (20 words)
```

Each level adds complexity:
1. **simulator.py:** exact SHA-256 + coordinate mapping (no physics)
2. **physics.py:** register → ball position (no dynamics)  
3. **bit_simulator.py:** full ODE dynamics with drag, force, bounce (snooker physics)
4. **position_variation.py:** variant experiments on 128 bits
5. **initial_640_bits.py:** scale up to full Bitcoin header (640 bits × 5 variants × 192 rounds)

### The Experimental Design

The variant system implements a RIGOROUS experimental protocol:
1. Generate baseline trajectories for all bits
2. Apply each permutation (holding SHA-256 dynamics CONSTANT)
3. Compare trajectory fingerprints (exact match + similarity)
4. Classify which hypothesis explains the data

This answers a FUNDAMENTAL question: **does initial position or bit identity determine SHA-256 propagation patterns?** If position_similarity dominates, then GEOMETRY matters (the table topology shapes trajectories). If type_similarity dominates, then ALGEBRAIC IDENTITY matters (which field the bit belongs to shapes trajectories). The combo_permute variant tests for INTERACTION effects.

### SHA-256 as Self-Contained Reference

`snooker_simulator.py` contains a COMPLETE pure-Python SHA-256 implementation (no external libs). This serves as ground truth for all other snooker tools. The H0 initial values and K[64] round constants are explicitly defined — identical to NIST FIPS 180-4.

---

*Pass 18 complete. Running total: ~43,339 lines, 435+ equations, 185+ constants, 81 cross-connections across 51 files (~70% of mathematically-significant corpus). All snooker files now fully characterized. The snooker subsystem forms a complete experimental pipeline: SHA-256 computation → spatial embedding → ODE dynamics → variant experiments → hypothesis testing. Remaining: ~87 files of numbered px_genesis/digital_twin/genesis_omega variants and demo files (likely mostly duplicates of already-characterized engines).*
