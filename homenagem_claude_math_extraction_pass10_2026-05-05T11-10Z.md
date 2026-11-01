# Mathematical Extraction Pass 10: PLRAD Stage 4 Microscope + Tesla Simulations

**Analysis by:** Claude  
**Date:** 2026-05-05T11:10Z  
**Corpus:** 286 Python files in `D:\gemini\interactions\gifts\homenagem_amigo_claude\python\`  
**Files read this pass:** plrad_stage4_microscope.py (1056 lines, complete), tesla_simulations.py (177 lines, complete)  
**Running total:** ~29,150 lines read, 237+ equations, 106+ constants, 50 cross-connections, 35 files (~58% of mathematically-significant corpus)

---

## 1. PLRAD Stage 4 Microscope — Micro-Local Carry Forensics

### Stage 4 Configuration

| Parameter | Value | Meaning |
|-----------|-------|---------|
| `N_WINDOWS` | 8 per round | Sliding windows per round for local analysis |
| `WINDOW_LEN` | 4 rounds | Each window spans 4 consecutive rounds |
| `OVERLAP` | 2 rounds | 50% overlap between consecutive windows |
| `zoneA_starts` | {6, 8, 10, 12, 14, 16} | Round windows in early-mixing zone |
| `zoneB_starts` | {44, 46, 48, 50} | Round windows in late-saturation zone |
| `alpha_BH` | 0.05 | Benjamini-Hochberg FDR target |
| `N_NULL` | 200 | Null samples per window |

### Correction: Benjamini-Hochberg FDR

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| S4.1 | $q_k = \frac{k}{m} \alpha$ where $k$ = rank, $m$ = total tests | `benjamini_hochberg(pvals, alpha=0.05)` |
| S4.2 | Reject $H_0$ for all $p_{(k)} \leq q_k$ where $k^* = \max\{k : p_{(k)} \leq q_k\}$ | Returns boolean mask of significant windows |

### 10 Window Observables

| eq_id | Observable | Formula | Meaning |
|-------|-----------|---------|---------|
| S4.3 | `carry_delta` | $\Delta C = \lvert C_{\text{end}} - C_{\text{start}}\rvert$ | Carry vector change across window |
| S4.4 | `carry_var` | $\text{Var}(C_r)$ for $r \in W$ | Carry variance within window |
| S4.5 | `J_delta` | $\Delta J = \lVert J_{\text{end}} - J_{\text{start}}\rVert_F$ | Jacobian Frobenius norm change |
| S4.6 | `J_var` | $\text{Var}(\lVert J_r\rVert_F)$ for $r \in W$ | Jacobian norm variance |
| S4.7 | `diff_delta` | $\Delta D = \lvert D_{\text{end}} - D_{\text{start}}\rvert$ | Diffusion tensor change |
| S4.8 | `reg_repeat` | $\max_r \sum_{i} \mathbb{1}[s_{r,i} = s_{r-1,i}]$ | Maximum register-bit repeat count |
| S4.9 | `ccol_repeat` | $\max_r \sum_{i} \mathbb{1}[c_{r,i} = c_{r-1,i}]$ | Maximum carry-column repeat count |
| S4.10 | `geo_straight` | $\frac{\lVert x_{\text{end}} - x_{\text{start}}\rVert}{\sum_r \lVert x_r - x_{r-1}\rVert}$ | Geometric straightness (1 = geodesic) |
| S4.11 | `align_cJ` | $\text{corr}(C_r, \lVert J_r\rVert_F)$ | Carry-Jacobian alignment |
| S4.12 | `anis` | $\frac{\lambda_{\max}}{\lambda_{\min}}$ of local diffusion | Anisotropy ratio |

### 4 Null Families (Local)

| eq_id | Null type | Destruction target | Preserves |
|-------|-----------|-------------------|-----------|
| S4.13 | `round_shuffle_local` | Temporal order within window | Marginal distributions |
| S4.14 | `carry_scrambled_local` | Carry vector correlations | Register states |
| S4.15 | `register_scrambled_local` | Register-register correlations | Carry vectors |
| S4.16 | `geometry_scrambled_local` | Geometric embedding | All algebraic structure |

### Curtain Score

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| S4.17 | $H_{\text{curtain}} = H_{\text{pre}} + 0.35 \cdot Z_{\text{meso}} + 0.25 \cdot (\nu - 1)_+$ | `compute_curtain_score()` |

Where:
- $H_{\text{pre}}$ = pre-existing evidence from Stages 1-3 (inherited)
- $Z_{\text{meso}}$ = mesoscopic z-score (window-level departure from null)
- $\nu$ = cluster multiplicity (number of significant windows in connected component)
- $(\nu-1)_+ = \max(0, \nu-1)$ = bonus for multi-window clusters

### BFS Cluster Detection

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| S4.18 | Adjacent if $\lvert r_i - r_j\rvert \leq$ OVERLAP | `bfs_clusters(significant_windows)` |
| S4.19 | Cluster = connected component under adjacency | BFS on window-lattice graph |

### Zone-vs-Control Mann-Whitney

| eq_id | Formula | Purpose |
|-------|---------|---------|
| S4.20 | $U = \sum_{i=1}^{n_z}\sum_{j=1}^{n_c} \mathbb{1}[x_i > y_j]$ | Non-parametric zone significance |
| S4.21 | Zone significant if $p_U < 0.05$ after BH correction | FDR-controlled zone labeling |

### Topological Follow-Up

| eq_id | Formula | Purpose |
|-------|---------|---------|
| S4.22 | $z_{\text{topo}} = \frac{\text{obs} - \mu_{\text{null}}}{\sigma_{\text{null}}}$ | Per-window topological departure |
| S4.23 | $p = 2\Phi(-\lvert z\rvert)$ | Two-sided p-value from normal approx |

---

## 2. Tesla Simulations — GPE + Schumann + ERC Validation

### GPE Simulation (Tesla-BEC Ether Model)

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| TS.1 | $i\hbar\frac{\partial\Psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\Psi + g\lvert\Psi\rvert^2\Psi$ | `gpe_simulation()` — 2D Split-Step Fourier |
| TS.2 | $\Psi_{\text{vortex}} = \tanh(r/\xi) \cdot e^{i\theta}$ | Initial condition: quantized vortex, $\xi=1.0$ |
| TS.3 | $\hat{U}_K = \exp(-iK^2 \Delta t / 4)$ | Kinetic propagator in Fourier space |
| TS.4 | $\hat{U}_V = \exp(-ig\lvert\Psi\rvert^2 \Delta t / 2)$ | Nonlinear propagator in real space |
| TS.5 | Split-step: $\Psi(t+\Delta t) = \hat{U}_V \cdot \mathcal{F}^{-1}[\hat{U}_K^2 \cdot \mathcal{F}[\hat{U}_V \cdot \Psi(t)]]$ | Strang splitting (2nd order) |

Parameters: Nx=Ny=64, Lx=Ly=20.0, dt=0.01, n_steps=500, g=1.0

### Schumann-Tesla Analysis

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| TS.6 | $f_{\text{Schumann}} = \frac{c}{2\pi R_{\oplus}} \sqrt{n(n+1)}$ for $n=1$: $\frac{c}{2\pi R_{\oplus}}\sqrt{2}$ | Theoretical Schumann fundamental |
| TS.7 | $c_s = f_{\text{Tesla}} \cdot 2\pi R_{\oplus}$ | Sound speed in "ether" required for Tesla's 8 Hz |
| TS.8 | Test: $c_s / c > 1$ → superluminal propagation | `schumann_analysis()` |

### ERC Simulation (Kuramoto + Holonomy)

| eq_id | Formula | Implementation |
|-------|---------|---------------|
| TS.9 | $\dot{\theta}_i = \omega_i + \frac{K}{N}\sum_{j=1}^{N}\sin(\theta_j - \theta_i)$ | `kuramoto(theta, t, K, omega)` via `odeint` |
| TS.10 | PLV$_{ij} = \left\lvert\frac{1}{T}\sum_{t} e^{i(\theta_i(t) - \theta_j(t))}\right\rvert$ | Phase-locking value between oscillator pairs |
| TS.11 | $R_\triangle = \left\lvert\frac{1}{T}\sum_{t} e^{i\Phi_\triangle(t)}\right\rvert$ where $\Phi_\triangle = (\theta_1-\theta_2)+(\theta_2-\theta_3)+(\theta_3-\theta_1)$ | Triadic phase closure |
| TS.12 | ERC-OK criterion: $R_\triangle > 0.90$ | Holonomic coherence threshold |

Parameters: N=3 oscillators, $\omega_0 = 2\pi \cdot 7.83$ Hz (Schumann), K tested at {0.5, 1.0, 2.0}

---

## 3. New Constants

| Constant | Value | Source | Meaning |
|----------|-------|--------|---------|
| Stage4 N_WINDOWS | 8 | plrad_stage4 | Windows per round |
| Stage4 WINDOW_LEN | 4 | plrad_stage4 | Rounds per window |
| Stage4 OVERLAP | 2 | plrad_stage4 | Window overlap (50%) |
| Stage4 N_NULL | 200 | plrad_stage4 | Null samples per test |
| Stage4 alpha_BH | 0.05 | plrad_stage4 | FDR target |
| Curtain Z_meso weight | 0.35 | plrad_stage4 | Mesoscopic z-score contribution |
| Curtain cluster bonus | 0.25 | plrad_stage4 | Per extra cluster member |
| ERC-OK threshold | 0.90 | tesla_simulations | Holonomic coherence pass |
| Tesla Schumann base | 7.83 Hz | tesla_simulations | ω₀ for Kuramoto |
| GPE grid | 64×64 | tesla_simulations | Spatial discretization |
| GPE coupling g | 1.0 | tesla_simulations | Nonlinear interaction |

---

## 4. Cross-Connections

### Connection U: Stage 4 curtain score ↔ Beast hypothesis confidence

The curtain score formula $H_{\text{curtain}} = H_{\text{pre}} + 0.35 \cdot Z_{\text{meso}} + 0.25 \cdot (\nu-1)_+$ is structurally identical to how Beast accumulates hypothesis confidence:
- **$H_{\text{pre}}$** = prior evidence (equivalent to hypothesis status before new data)
- **$Z_{\text{meso}}$** = new evidence strength (equivalent to a new experimental result)
- **$(\nu-1)_+$** = corroboration bonus (equivalent to multiple independent confirmations)

This is Bayesian-like updating with explicit "clustering bonus" — evidence that clusters spatially (in windows) or conceptually (across experiments) gets extra weight.

### Connection V: 4 null families ↔ 4 aspects of SHA-256 structure

The 4 local null types decompose SHA-256 structure into orthogonal components:
- **round_shuffle** destroys temporal causality → tests if ORDER matters
- **carry_scrambled** destroys carry correlations → tests if CARRY matters (H45 target)
- **register_scrambled** destroys inter-register coupling → tests if TOPOLOGY matters
- **geometry_scrambled** destroys geometric embedding → tests if GEOMETRY matters

This is a systematic decomposition analogous to ANOVA: each null removes ONE factor while preserving all others. The carry_scrambled null specifically targets H45's claim.

### Connection W: Tesla GPE ↔ Px-Genesis GPE-Caputo

The Tesla simulation's GPE (TS.1-5) is the INTEGER-ORDER version of Px-Genesis's GPE-Caputo (PX.1 from pass 7):
- **Tesla:** $i\hbar\partial_t\Psi = (-\frac{\hbar^2}{2m}\nabla^2 + g|\Psi|^2)\Psi$ (standard NLS)
- **Px-Genesis:** $i\hbar\partial_t\Psi = (\hat{H}_{\text{kin}} + \hat{H}_{\text{nl}} + \hat{H}_{\text{narr}} + D^\beta[\Psi])\Psi$ (fractional + narrative)

The Tesla version is the physical baseline; Px-Genesis extends it with: (1) fractional memory via Caputo $D^\beta$, (2) narrative coupling $\hat{H}_{\text{narr}}$. Both use identical Split-Step Fourier for time evolution.

### Connection X: Zone structure ↔ SHA-256 phase transitions

Stage 4's zone definitions directly encode the SHA-256 phase structure:
- **Zone A (rounds 6-16):** early mixing → corresponds to C<0.3 (low coherence) regime
- **Control (rounds 18-42):** full mixing → corresponds to C>0.6 (high coherence) regime  
- **Zone B (rounds 44-50):** late saturation → transition to final hash compression

This mirrors Connection Q from pass 8 (phase diagram regimes ↔ SHA-256 round phases), now with EXACT round boundaries from empirical analysis.

### Connection Y: ERC-OK threshold 0.90 ↔ ERC threshold from fused_v3

The tesla_simulations.py ERC-OK criterion ($R_\triangle > 0.90$) provides a concrete threshold for the holonomy closure test. Combined with the fused_v3 ERC formalism (28.2.1) and the Stage 4 carry-Jacobian alignment (S4.11), we have three scales of ERC measurement:
- **Tesla scale:** 3-oscillator Kuramoto, threshold 0.90 (simple, demonstrative)
- **fused_v3 scale:** N-oscillator PLV closure on SHA-256 registers
- **Stage 4 scale:** micro-local window-level carry-Jacobian correlation

All three measure the same invariant (holonomic closure) at different resolutions.

---

## 5. Architectural Observations

### The Microscope Hierarchy

The PLRAD system implements a 4-stage zoom hierarchy:
1. **Stage 1:** Global statistics (full 64-round view)
2. **Stage 2:** Round-by-round analysis (per-round metrics)
3. **Stage 3:** Carry-specific forensics (carry vector extraction + persistent homology)
4. **Stage 4:** Micro-local windows (4-round sliding windows with 10 observables × 4 nulls)

Each stage inherits evidence ($H_{\text{pre}}$) from previous stages and adds resolution. This is a multi-scale analysis framework where the carry chain's signal can be detected at any zoom level but becomes increasingly precise at deeper stages.

### The "Projection" Principle

The tesla_simulations.py file demonstrates the same physics (GPE + Kuramoto + ERC) applied to Tesla/ether theory as the main corpus applies to SHA-256 and consciousness. The equations are identical — only the interpretation changes:
- In Tesla context: GPE models ether as superfluid, Kuramoto models Earth resonances
- In SHA-256 context: GPE models state evolution, Kuramoto models register synchronization  
- In consciousness context: GPE models neural field, Kuramoto models neural oscillator networks

This confirms the "projection" architecture: one mathematical framework, multiple interpretive projections.

---

*Pass 10 complete. Running total: ~29,150 lines, 237+ equations, 106+ constants, 50 cross-connections across 35 files. Remaining priority: turr_complete.py, validate_all_math.py, remaining digital_twin/snooker/px_genesis variants, _sections_09_15.py (2001 lines — §9-§15 implementations).*
