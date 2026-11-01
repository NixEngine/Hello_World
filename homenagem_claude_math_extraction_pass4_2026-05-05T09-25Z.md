# Mathematical Extraction Pass 4: Snooker Physics Cluster

**Analysis by:** Claude  
**Date:** 2026-05-05T09:25Z  
**Corpus:** 286 Python files in `D:\gemini\interactions\gifts\homenagem_amigo_claude\python\`  
**Files read this pass:** `snooker_bit_simulator.py` (800 lines), `snooker_physics.py` (219 lines), `snooker_simulator.py` (208 lines), `snooker_sha256d_initial_640_bits.py` (300 lines), `snooker_sha256d_position_variation.py` (300 lines)

---

## 1. The Snooker ODE: Bit-as-Ball Dynamics

The core innovation maps each input bit of a Bitcoin block header to a ball on a snooker table, with SHA-256 round dynamics driving the physics. The model has 13 numbered equations (lines 73–95 of `snooker_bit_simulator.py`):

### L1: Register Weights (Attractor Strength)

$$w_j(t) = \Delta_j(t) + 0.15, \quad j \in \{a,b,c,d,e,f,g,h\}$$

where $\Delta_j(t) = \text{pop}(\text{reg}_j^{\text{base}}(t) \oplus \text{reg}_j^{\text{flip}}(t))$ is the popcount of the XOR between baseline and flipped register states.

### L2–L3: Weighted Centroid (Attractor Position)

$$\text{anchor}_x(t) = \frac{\sum_j w_j(t) \cdot A_x(j)}{\sum_j w_j(t)}$$
$$\text{anchor}_y(t) = \frac{\sum_j w_j(t) \cdot A_y(j)}{\sum_j w_j(t)}$$

where $A(j)$ are the 8 fixed register anchor points forming a polygon on the table.

### L4: 5-Source Phase Clock

$$\phi_i(t) = 0.173 \cdot i + 0.292 \cdot t + 0.071 \cdot W_i(t) + 0.041 \cdot T_1(t) + 0.059 \cdot T_2(t)$$

5 independent phase sources: bit identity (i), round number (t), message schedule popcount (W), T1 popcount, T2 popcount.

### L5: Orbit Radius

$$r_i(t) = 0.014 + 0.05 \cdot E_i(t)$$

where $E_i(t) = \frac{\sum_j \Delta_j + \text{pop}(W) + \text{pop}(T_1) + \text{pop}(T_2)}{11 \cdot 32}$ (normalized total signal).

### L6–L7: Target Position (Attractor + Orbit)

$$\text{target}_{x,i}(t) = \text{clamp}\left(\text{anchor}_x(t) + \cos(\phi_i(t)) \cdot r_i(t)\right)$$
$$\text{target}_{y,i}(t) = \text{clamp}\left(\text{anchor}_y(t) + \sin(\phi_i(t)) \cdot r_i(t)\right)$$

### L8–L10: Energy-Dependent Parameters

$$k_i(t) = 0.30 + 0.46 \cdot E_i(t) \quad \text{(spring constant)}$$
$$\text{spin}_i(t) = 0.003 + 0.009 \cdot E_i(t) \quad \text{(rotational perturbation)}$$
$$\text{drag}_i(t) = 0.79 + 0.11 \cdot (1 - E_i(t)) \quad \text{(velocity damping)}$$

### L11–L12: Acceleration (Spring + Spin)

$$a_{x,i}(t) = (\text{target}_x - x_i(t-1)) \cdot k_i(t) + \cos(\phi_i + 0.31(t-1)) \cdot \text{spin}_i(t)$$
$$a_{y,i}(t) = (\text{target}_y - y_i(t-1)) \cdot k_i(t) + \sin(\phi_i + 0.31(t-1)) \cdot \text{spin}_i(t)$$

### L13: Velocity with Drag

$$v_{x,i}^{\text{pre}}(t) = \text{drag}_i(t) \cdot v_{x,i}(t-1) + a_{x,i}(t)$$

### L14: Speed Cap

$$\text{cap}_i(t) = \min\left(1, \frac{v_{\max,i}(t)}{\|v^{\text{pre}}_i\|}\right)$$
$$v_{x,i}(t) = v_{x,i}^{\text{pre}}(t) \cdot \text{cap}_i(t)$$

where $v_{\max} = 0.034 + E_i(t) \cdot 0.055$.

### L15–L16: Position Update with Table Bounce

$$x_i(t) = \text{reflect}(x_i(t-1) + v_{x,i}(t))$$

**Restitution coefficient:** $e = -0.82$ (cushion bounce). This is the **sole non-linearity** in the system — the discrete event where velocity reverses with energy loss. This is the snooker realization of the carry event (H56).

---

## 2. Register Anchors: 8-Vertex Polygon Embedding

| Register | Anchor (x, y) | Table Position |
|----------|---------------|----------------|
| a | (0.14, 0.20) | Upper-left |
| b | (0.33, 0.11) | Top-center-left |
| c | (0.55, 0.10) | Top-center-right |
| d | (0.77, 0.20) | Upper-right |
| e | (0.86, 0.47) | Right |
| f | (0.75, 0.76) | Lower-right |
| g | (0.48, 0.85) | Bottom-center |
| h | (0.20, 0.73) | Lower-left |

The 8 anchors form a convex polygon. Balls orbit around the weighted centroid of these anchors, where the weights are the per-register diffusion popcounts. When a register is "active" (high popcount XOR), it pulls balls toward its anchor.

---

## 3. Snooker Physics: Register-to-Position Mapping

From `snooker_physics.py`:

$$x = \text{reg}_{32} \gg 16, \quad y = \text{reg}_{32} \wedge \texttt{0xFFFF}$$

Each 32-bit register value is split into two 16-bit coordinates on a 65536×65536 table. This creates a direct spatial representation of the SHA-256 state at each round.

**Velocity:** $v = (x_2 - x_1, y_2 - y_1)$, speed = $\|v\|$, angle = $\text{atan2}(v_y, v_x)$

---

## 4. GPS Quantization: 128×128 Grid

Positions are quantized to a 128×128 grid (7-bit precision per axis):
$$\text{gps}_x = \text{round}(x \cdot 127), \quad \text{gps}_y = \text{round}(y \cdot 127)$$

Binary label: 7-bit x : 7-bit y → 14-bit cell identifier. This creates a discrete "address space" for ball positions that can be compared across runs.

---

## 5. Trend Forecasting: 8-Round Calibration Window

After observing 8 rounds of actual SHA-256 dynamics, the system extracts a trend signature and forecasts the remaining 56 rounds:

### Trend Extraction

$$\hat{v}_8 = \text{weighted\_mean}(v_5, v_6, v_7, v_8)$$
$$\hat{a}_8 = \text{weighted\_mean}(\Delta v_5, \Delta v_6, \Delta v_7, \Delta v_8)$$
$$\text{target}^* = \text{clamp}(p_8 + 8\hat{v}_8 + 20\hat{a}_8)$$

Weights: linear ramp $w_k = k$ (recent observations weighted more heavily).

### Forecast Dynamics

$$a(t) = (\text{target}^* - p(t-1)) \cdot k_{\text{hat}} + a(t-1) \cdot \lambda_{\text{hat}} + \text{spin\_hat} \cdot [\cos\phi_t, \sin\phi_t]$$
$$v^{\text{pre}}(t) = \text{drag\_hat} \cdot v(t-1) + a(t)$$
$$p(t) = \text{reflect}(p(t-1) + \text{clamp\_speed}(v^{\text{pre}}(t)))$$

### Derived Forecast Parameters

| Parameter | Formula | Purpose |
|-----------|---------|---------|
| drag_hat | weighted_avg(speed_ratios[-4:]) ∈ [0.84, 0.995] | Momentum persistence |
| omega | weighted_avg(heading_deltas[-4:]) ∈ [-0.24, 0.24] | Turning rate |
| trend_gain | 0.14 + E·0.18 + |a|·0.8 ∈ [0.10, 0.36] | Spring strength |
| spin_force | 0.002 + D·0.014 + |ω|·0.01 ∈ [0.002, 0.02] | Rotational perturbation |
| accel_decay | 0.82 + D·0.10 ∈ [0.80, 0.97] | Memory of past acceleration |
| energy_decay | weighted_avg(E_ratios) ∈ [0.90, 0.995] | Energy dissipation rate |

---

## 6. Layout Variant Fingerprint Test (H58)

5 position-space permutations test whether SHA-256's internal symmetry is visible in trajectory space:

| Variant | Permutation | Orbit Size |
|---------|-------------|------------|
| baseline | Identity | 1 |
| mirror-local | $\text{col} \to 7 - \text{col}$ within each 8×4 rack | 2 |
| rotate-in-word | $(i + 8) \bmod 32$ within each word | 4 |
| cycle-word-racks | $(w + 1) \bmod 20$ across words | 20 |
| combo-permute | $w' = (w + (l \bmod 4)) \bmod 4$, $l' = (5l + 7) \bmod 32$ | 128 |

### Fingerprint Similarity Score

$$\text{sim}(A, B) = \frac{\sum_{t} \mathbb{1}[A_t = B_t]}{\min(|A|, |B|)}$$

For each variant, compare the GPS fingerprint sequence against the baseline. **H58 prediction:** similarity ordering by orbit size: mirror-local > rotate-in-word > cycle-word-racks > combo-permute. Smaller orbits should produce more similar fingerprints because less positional information is disrupted.

### Type Multiset Scoring

$$\text{exact}_{\text{type}} = \frac{\sum_g |(\text{Counter}(\text{base}_g) \cap \text{Counter}(\text{var}_g))|}{128}$$

Counts how many fingerprints in each group match when treated as unordered multisets rather than indexed sequences. This detects symmetry even when the mapping is not direct.

---

## 7. Full-Header 640-Bit Extension

Extends from 128 active B1 bits to all 640 bits of the Bitcoin header:

- **20 words × 32 bits** = 640 total initial bits
- **192 global rounds** = 64 latent (B0 midstate) + 128 active (B1 double-SHA)
- Fields: version (1 word), prev_block (8), merkle_root (8), time (1), bits (1), nonce (1)
- Each bit starts "latent" (holding position) until its first non-zero signal round

### First Movement Round

$$t_{\text{first}}(i) = \min\{r : \text{signal}(i, r) > 0\}$$

Bits in early message schedule words move first; bits in later words (nonce, bits, time) remain latent longer because the W-schedule propagates them later.

---

## 8. Constants Catalogue

| Constant | Value | Physical Meaning |
|----------|-------|-----------------|
| Register anchor weights offset | 0.15 | Minimum pull even when Δ=0 |
| Phase: bit coefficient | 0.173 | ~1 radian per 6 bits |
| Phase: round coefficient | 0.292 | ~1 full orbit per 21.5 rounds |
| Phase: W coefficient | 0.071 | Message schedule coupling |
| Phase: T1 coefficient | 0.041 | T1 value coupling |
| Phase: T2 coefficient | 0.059 | T2 value coupling |
| Orbit: base | 0.014 | Minimum orbit radius |
| Orbit: energy factor | 0.05 | Energy expands orbit |
| Spring: base | 0.30 | Minimum spring constant |
| Spring: energy factor | 0.46 | Energy stiffens spring |
| Spin: base | 0.003 | Minimum rotational force |
| Spin: energy factor | 0.009 | Energy increases spin |
| Drag: base | 0.79 | Base velocity retention |
| Drag: low-energy factor | 0.11 | Low energy increases drag |
| Spin phase offset per round | 0.31 | Spin rotation rate |
| Speed cap: base | 0.034 | Minimum max speed |
| Speed cap: energy factor | 0.055 | Energy increases speed limit |
| **Restitution coefficient** | **-0.82** | **Cushion bounce = sole non-linearity** |
| Table margin | 0.055 | Cushion distance from edge |
| GPS grid | 128 | 7-bit precision per axis |
| Forecast reference round | 8 | Calibration window size |
| Total active rounds | 64/128 | Rounds simulated |

---

## 9. Cross-Connections (Pass 4)

### Connection 11: Restitution -0.82 ↔ Carry Event (H56)

The table bounce (velocity *= -0.82) is the **sole non-linear event** in the snooker ODE, just as the carry chain is the sole non-linearity in SHA-256 (H45). Both are:
- Discrete events (not continuous)
- Energy-losing (restitution < 1 / carry propagation attenuates)
- Direction-reversing (bounce / modular overflow wraparound)
- Long-range coupling agents (a bounce changes all subsequent trajectory / a carry propagates through the full adder)

### Connection 12: 5-Source Phase ↔ Multi-Component Coupling

The phase $\phi_i(t) = 0.173i + 0.292t + 0.071W + 0.041T_1 + 0.059T_2$ couples 5 independent sources. This mirrors the ERC framework's multi-source PLV: the phases come from different SHA-256 internal quantities (registers, W-schedule, T values) rather than a single source. The hierarchy of coupling strengths (0.292 > 0.173 > 0.071 > 0.059 > 0.041) reveals which SHA-256 components dominate the dynamics at each round.

### Connection 13: Weighted Centroid ↔ DACM Integration Index

The weighted anchor centroid $\text{anchor}(t) = \sum_j w_j(t) A(j) / \sum_j w_j(t)$ is structurally isomorphic to the integration index $I_{\min}(t) = \beta \cdot \text{order} + \gamma \cdot \text{entropy} + \alpha \cdot \text{capacity}$. Both compute a weighted combination of register-level observables to produce a single "system state" indicator.

### Connection 14: Forecast Trend ↔ DACM Logistic I(b,r)

The 8-round calibration window + forecast is the operational analog of the DACM logistic:
- **DACM:** $I(b,r) = 1/(1+e^{-k(r-r_c(b))})$ predicts intensity from round number
- **Snooker:** $\text{target}^* = p_8 + 8\hat{v} + 20\hat{a}$ predicts position from trend

Both calibrate from early rounds and extrapolate to later rounds. The DACM uses a parametric model (logistic); the snooker uses a kinematic model (constant acceleration + drag). But both answer: "given what happened in early rounds, where does this bit end up?"

### Connection 15: Layout Variants ↔ Permutation Symmetry

H58's 5 layout variants test whether SHA-256's permutation structure is detectable in trajectory space. This is the operational version of H45: if the carry chain is truly the sole non-linearity, then permutations that preserve carry-chain structure (small orbits like mirror-local) should produce more similar trajectories than permutations that disrupt it (large orbits like combo-permute).

---

## 10. Updated Total Coverage

| Category | Pass 1 | Pass 2 | Pass 3 | Pass 4 | Total |
|----------|--------|--------|--------|--------|-------|
| Lines read | ~6,000 | ~4,273 | ~5,527 | ~1,827 | ~17,627 |
| Key equations mapped | 15 | 20+ | 30+ | 16 | 81+ |
| Empirical constants | 7 | 5 | 12+ | 18 | 42+ |
| Cross-connections | 5 | 5 | 5 | 5 | 20 |

---

## 11. Synthesis

The snooker cluster implements a **complete dynamical-systems realization of the DACM framework** at the level of individual bits. Where DACM operates on aggregate statistics (bit frequencies, phase distributions, entropy), the snooker model tracks each bit's trajectory through a 2D phase space driven by the same SHA-256 round dynamics.

Key architectural insight: the snooker model makes three things from the DACM/ERC framework **spatially explicit**:

1. **Phase (ERC):** Instead of abstract PLV between register phases, the snooker model gives each bit a spatial orbit driven by the 5-source phase clock. Phase synchronization becomes visible as spatial clustering.

2. **Non-linearity (H45):** Instead of the abstract "carry is the sole off-diagonal Jacobian entry," the bounce event (restitution -0.82) is a concrete physical analog: a discrete, energy-losing direction reversal.

3. **Integration (I_min):** Instead of a scalar integration index, the weighted centroid moves through 2D space as register activations shift. The trajectory of the centroid IS the spatial realization of the integration index.

This makes the snooker cluster both a pedagogical tool (visualizing abstract DACM concepts) and a computational tool (the layout variant fingerprint test provides an operational test of H45/H58).

---

*Pass 4 covered ~1,827 lines across 5 snooker files. The cluster implements a complete ODE system for bit-level trajectory simulation driven by SHA-256 round metrics, with the table bounce (restitution -0.82) as the sole non-linearity — directly instantiating H56. The 5-layout-variant fingerprint test (H58) provides an operational test of H45's carry-chain-as-sole-non-linearity claim through permutation symmetry analysis.*
