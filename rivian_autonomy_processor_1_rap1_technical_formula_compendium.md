## Page 1

# Rivian Autonomy Processor 1 (RAP1) – Technical Formula Compendium

---

## [0] Notation

Vectors: bold lower-case (e.g., x), matrices: bold upper-case (e.g., K, R).
Transpose: A^T. Inverse: A^{-1}. Element-wise (Hadamard) product: a ⨂ b.
Norms: ||x||_2 (Euclidean), ||x||_1 (L1), ||x||_∞ (max).
Expectation: E[·]. Variance: Var[·].

## [1] RAP1 / ACM3 HARDWARE-LEVEL MATH

### [1.1] Throughput and TOPS

Variables:
N_MAC : number of INT8 multiply-accumulate units.
f_clk : core clock frequency [Hz].
ops_MAC : operations per MAC per cycle (2 for multiply+add).
s : effective sparsity (fraction of pruned / zero weights or activations, 0 ≤ s < 1)
n_chip : number of RAP1 chips in ACM3.
T_inf : inference latency per frame [s].

Dense theoretical throughput:
TOPS_dense = N_MAC * ops_MAC * f_clk / 1e12

Sparse-effective throughput (approximate):
TOPS_sparse = TOPS_dense / (1 - s)

Multi-chip effective throughput:
TOPS_cluster = n_chip * TOPS_sparse

MAC budget per inference:
MACs_max = TOPS_cluster * 1e12 * T_inf / 2

Utilization:
util = MACs_used / MACs_max

Latency from pipeline depth D (in cycles):
latency_seconds = D / f_clk

### [1.2] Pixel throughput constraint (ACM3, 5e9 pixels/s)

For camera i:
W_i : image width [pixels]
H_i : image height [pixels]
fps_i : frame rate [frames/s]

Pixels per second, camera i:
Φ_i = W_i * H_i * fps_i

Total throughput over all cameras (and image streams):
Φ_total = Σ_i Φ_i

Constraint for RAP1 + ACM3:
Φ_total ≤ 5 × 10^9 (pixels/s)

### [1.3] Memory bandwidth and capacity

Per-channel parameters:
B_bus : bus width [bits]
f_bus : bus clock [Hz]

---


## Page 2

Per-channel bandwidth:
BW_bytes = (B_bus / 8) * f_bus [bytes/s]

Total bandwidth over channels j:
BW_total = Σ_j BW_bytes_j

Peak feature-map bandwidth (one direction):
BW_feat = bytes_per_feature * features_per_second

On-chip SRAM capacity:
C_cells : number of bit-cells
bits_per_cell : typically 1
C_bytes = C_cells * bits_per_cell / 8

[1.4] Energy and power (digital CMOS, RAP1 core)

Variables:
C_eff : effective switching capacitance [F]
V_dd : supply voltage [V]
f_clk : clock frequency [Hz]
α : average switching activity (0 ≤ α ≤ 1)
P_leak : leakage / static power [W]

Dynamic power:
P_dyn = α * C_eff * V_dd^2 * f_clk

Energy per operation (approximate, INT8 MAC-bound):
E_op ≈ C_eff * V_dd^2 / N_switches_per_op

Total power:
P_total = P_dyn + P_leak

Thermal steady-state (simplified single-node model):
T_junc = T_ambient + θ_JA * P_total
where θ_JA is junction-to-ambient thermal resistance [°C/W].

[1.5] RivLink multi-chip interconnect

Variables:
B_link : link width [bits]
f_Tink : symbol rate [Hz]
η_code : coding efficiency (0 < η_code ≤ 1)
n_links : number of independent RivLink lanes
L_hop : average number of hops between chips

Per-link raw bandwidth:
BW_link_raw = (B_link / 8) * f_link

Effective payload bandwidth (with coding):
BW_link_eff = η_code * BW_link_raw

Aggregate inter-chip bandwidth:
BW_interchip = n_links * BW_link_eff

Per-message latency (simple store-and-forward model):
t_link = payload_bytes / BW_link_eff
t_end_to_end ≈ L_hop * t_link

[1.6] Reliability / ASIL-related basic quantities (component level)

Variables:
λ : constant failure rate [1/h]
t : operating time [h]

Reliability function (no repair):

---


## Page 3

R(t) = exp(-λ t)

Mean Time To Failure (MTTF):
MTTF = 1 / λ

Series system (independent components k):
R_series(t) = Π_k R_k(t)

Parallel redundant system:
R_parallel(t) = 1 - Π_k (1 - R_k(t))

Safety integrity (probability of dangerous failure per hour, simplified):
PFH ≈ Σ_i λ_i_dangerous

[2] SENSORS: CAMERAS, LIDAR, RADAR
---

[2.1] Pinhole camera model and intrinsics

World point (homogeneous):
X_world = [X, Y, Z, 1]^T

Camera extrinsics (world → camera):
R_wc : 3×3 rotation, t_wc : 3×1 translation
T_wc = [R_wc t_wc ;
         0 0 0 1]

Camera intrinsics (pinhole):
K = [f_x s c_x ;
     0 f_y c_y ;
     0 0 1]

Projection to normalized camera coordinates:
x_cam = R_wc * [X, Y, Z]^T + t_wc
x_norm = x_cam / Z_cam

Projection to pixel coordinates (homogeneous):
x_img_h = K * [x_norm_x, x_norm_y, 1]^T
x_pixelT = x_img_h / x_img_h(3)

[2.2] Lens distortion (Brown-Conrady form)

Variables:
(x_u, y_u) : undistorted normalized coords
(x_d, y_d) : distorted normalized coords
r^2 = x_u^2 + y_u^2
k1, k2, k3 : radial coefficients
p1, p2 : tangential coefficients

Radial distortion:
x_r = x_u * (1 + k1 r^2 + k2 r^4 + k3 r^6)
y_r = y_u * (1 + k1 r^2 + k2 r^4 + k3 r^6)

Tangential distortion:
x_t = 2 p1 x_u y_u + p2 (r^2 + 2 x_u^2)
y_t = p1 (r^2 + 2 y_u^2) + 2 p2 x_u y_u

Total distorted coordinates:
x_d = x_r + x_t
y_d = y_r + y_t

[2.3] Homogeneous rigid transforms (SE(3))

Transform T_ab (frame b → frame a):
T_ab = [R_ab t_ab ;

---


## Page 4

0 0 0 1]

Composition (a -> b, b -> c => a -> c):
T_ac = T_ab * T_bc

Point transform:
X_a = T_ab * X_b

Inverse transform:
T_ba = [ R_ab^T -R_ab^T t_ab ;
          0 0 0 1 ]

[2.4] LiDAR time-of-flight and point cloud coordinates

Variables:
Δt : round-trip time-of-flight [s]
c : speed of light ≈ 2.99792458×10^8 m/s
θ, φ : azimuth, elevation angles

Range from TOF:
R = (c * Δt) / 2

LiDAR spherical to Cartesian (sensor frame):
x = R cos φ cos θ
y = R cos φ sin θ
z = R sin φ

Transform to camera/world using SE(3):
X_world = T_wl * X_lidar

[2.5] Radar range and Doppler

Classical monostatic radar range equation (free-space):
P_r = (P_t * G_t * G_r * λ^2 * σ) / ((4π)^3 * R^4 * L)

Variables:
P_r : received power
P_t : transmitted power
G_t,G_r : transmit / receive antenna gains
λ : wavelength
σ : radar cross-section
R : range
L : system / propagation losses (linear)

Doppler frequency shift from relative radial velocity v_r:
f_D = (2 v_r) / λ

Radial velocity estimate:
v_r = (f_D * λ) / 2

[2.6] Image sensor SNR and dynamic range

Signal-to-noise ratio (power form):
SNR = P_signal / P_noise

In decibels:
SNR_dB = 10 log10(SNR)

Amplitude-based (e.g., voltage or intensity):
SNR_dB = 20 log10(A_signal / A_noise)

Alternative (mean μ, standard deviation σ):
SNR = μ / σ

Dynamic range of n-bit ideal quantizer (approx):

---


## Page 5

DR_dB ≈ 6.02 n

[2.7] Rolling shutter timing (simplified)

Variables:
H : image height [rows]
T_frame : total frame time [s]
T_readout : sensor readout time [s]
t_row : time offset between adjacent rows

Approximate row time:
t_row ≈ T_readout / H

Exposure time for row r (0-based):
t_r_start = r * t_row
t_r_end = t_r_start + T_exposure

[2.8] Motion-induced rolling-shutter displacement (vertical)

Variables:
V : platform speed [m/s]
h : altitude or distance to scene [m]
f : focal length [mm]
p : pixel size [mm/pixel]

Approximate vertical displacement in pixels:
Δ_pixels ≈ (V * T_readout * f) / (h * p)

[3] PERCEPTION NEURAL NETWORKS (CNNs, TRANSFORMERS)
---

[3.1] Discrete convolution (2D, single channel)

Input:
x[m, n]
Kernel:
h[i, j]

Output:
y[m, n] = Σ_i Σ_j h[i, j] * x[m - i, n - j]

[3.2] 2D convolution (multi-channel, NCHW layout)

Input tensor:
x[c_in, h, w]

Kernel tensor:
w[c_out, c_in, k_h, k_w]

Output tensor:
y[c_out, h_out, w_out] = Σ_{c_in} Σ_{u=0}^{k_h-1} Σ_{v=0}^{k_w-1}
w[c_out, c_in, u, v]^*
x[c_in, h_out + u - p_h, w_out + v - p_w]

Per-layer MAC count:
MACs_layer = C_out * C_in * k_h * k_w * H_out * W_out

[3.3] 3D convolution (spatiotemporal)

Input:
x[c_in, t, h, w]
Kernel:
w[c_out, c_in, k_t, k_h, k_w]

Output:

---


## Page 6

mermaid
y[c_out, t_out, h_out, w_out] =
Σ_{c_in} Σ_{τ=0} Σ_{u=0} Σ_{v=0}
w[c_out, c_in, τ, u, v] *
x[c_in, t_out + τ - p_t, h_out + u - p_h, w_out + v - p_w]
```

[3.4] Common activation functions

ReLU:
ReLU(z) = max(0, z)

Leaky ReLU (slope a on negative side):
LReLU(z) = max(z, a z)

Sigmoid:
σ(z) = 1 / (1 + exp(-z))

Hyperbolic tangent:
tanh(z) = (exp(z) - exp(-z)) / (exp(z) + exp(-z))

GELU (approximate):
GELU(z) ≈ 0.5 z [1 + erf(z / sqrt(2))]

[3.5] Normalization layers

Batch Normalization (per-channel over batch and spatial):

Given mini-batch B of N values for one channel:
μ_B = (1/N) Σ_i x_i
σ_B^2 = (1/N) Σ_i (x_i - μ_B)^2

Normalized:
x̄_i = (x_i - μ_B) / sqrt(σ_B^2 + ε)

Affine output:
y_i = γ x̄_i + β

Layer Normalization (per-sample over features):

For feature vector x ∈ R^d:
μ = (1/d) Σ_j x_j
σ^2 = (1/d) Σ_j (x_j - μ)^2
x̄_j = (x_j - μ) / sqrt(σ^2 + ε)
y_j = γ_j x̄_j + β_j

[3.6] Scaled dot-product attention (single head)

Queries, keys, values:
Q ∈ R^{n_q×d_k}
K ∈ R^{n_k×d_k}
V ∈ R^{n_k×d_v}

Attention weights:
A = softmax(Q K^T / sqrt(d_k))

Output:
O = A V

[3.7] Multi-head attention

Heads i = 1..h, linear projections:

Q_i = Q W_i^Q
K_i = K W_i^K
V_i = V W_i^V

---


## Page 7

Per-head output:
head_i = Attention(Q_i, K_i, V_i)

Concatenation and output projection:
O = Concat(head_1, ..., head_h) W^O

[3.8] Transformer encoder block (pre-norm form)

Input:
X ∈ R^{T×d}

Self-attention sub-layer:
SA = MultiHeadAttention(X, X, X)
X1 = X + Dropout(SA)
X1_norm = LayerNorm(X1)

Feed-forward sub-layer (position-wise MLP):
FF = MLP(X1_norm)
X2 = X1_norm + Dropout(FF)
Y = LayerNorm(X2)

[3.9] Quantization to INT8 (per-tensor linear)

Variables:
x : real-valued tensor
q : quantized int8 tensor
s : scale (>0)
z : zero-point (int)

Quantization:
q = round(x / s) + z

Dequantization:
x☐ = s (q - z)

Quantization error:
e = x☐ - x

Mean squared quantization error (per-element):
MSE_q = E[e^2]

[3.10] Per-layer compute and memory footprint

For layer ☐:
MACs_☐ : MAC operations
params_☐ : number of parameters
b_param : bits per parameter (e.g., 8)
act_☐ : number of activation values

Parameter memory:
M_param_☐ = params_☐ * b_param / 8

Activation memory (per batch):
M_act_☐ = act_☐ * b_act / 8

Total MACs and memory (over layers):
MACs_total = Σ☐ MACs_☐
M_param_total = Σ☐ M_param_☐

[4] LARGE DRIVING MODEL (LDM) TRAINING AND GRPO

[4.1] Supervised pretraining losses

Cross-entropy loss for token prediction:

---


## Page 8

Given logits z ∈ R^V, target token index y:
p = softmax(z)
L_CE = -log p_y

Sequence loss (average over tokens t with mask m_t ∈ {0,1}):
L_seq = (1 / Σ_t m_t) Σ_t m_t * L_CE(t)

[4.2] Reinforcement learning with PPO (reference)

Policy π_θ(a_t | s_t), old policy π_old(a_t | s_t).

Probability ratio:
r_t(θ) = π_θ(a_t | s_t) / π_old(a_t | s_t)

Clipped surrogate objective:
L_PPO(θ) = E_t [ min( r_t(θ) A_t,
clip(r_t(θ), 1 - ε, 1 + ε) A_t ) ]
where A_t is advantage estimate and ε is clip parameter.

[4.3] Group Relative Policy Optimization (GRPO) core equations

For question q, generate K candidate trajectories o_i with rewards r_i.

Group baseline (per question):
b = (1 / K) Σ_{i=1}^K r_i

Group-relative advantages:
A_i = r_i - b

Token-level decomposition (length |o_i|):
A_{i,t} = w_t A_i
where w_t is a per-position weighting (e.g., uniform or last-token focus).

Policy ratio for token t of output i:
r_{i,t}(θ) = π_θ(o_{i,t} | q, o_{i,<t}) / π_old(o_{i,t} | q, o_{i,<t})

Clipped group-relative objective (schematic):
L_GRPO(θ) = E_{i,t} [ min( r_{i,t}(θ) A_{i,t},
clip(r_{i,t}(θ), 1 - ε, 1 + ε) A_{i,t} )
- β KL(π_θ || π_ref) ]

where π_ref is a frozen reference policy and β is a KL regularization weight.

Policy gradient (conceptual):
∇_θ L_GRPO ≈ E_{i,t} [ ∇_θ log π_θ(o_{i,t} | q, o_{i,<t}) * A_{i,t} ]
- β ∇_θ KL(π_θ || π_ref)

[4.4] Reward model scoring (pairwise preferences)

Given pair of responses y_a, y_b to prompt q with human/auto preference d ∈ {+1, -1}.

Model produces scalar scores s_a, s_b.

Preference loss (logistic):
L_RM = -log σ(d (s_a - s_b))

where σ is sigmoid. Reward model is used to map sequences to scalar rewards r_i.

[5] SENSOR FUSION AND STATE ESTIMATION

[5.1] Linear Kalman filter (discrete time)

---


## Page 9

State dynamics:
x_{k+1} = F x_k + B u_k + w_k
Measurement model:
z_k = H x_k + v_k

Noise:
w_k ~ N(0, Q)
v_k ~ N(0, R)

Predict step:
x[k|k-1] = F x[k-1|k-1] + B u[k-1]
P[k|k-1] = F P[k-1|k-1] F^T + Q

Innovation:
y_k = z_k - H x[k|k-1]
S_k = H P[k|k-1] H^T + R

Kalman gain:
K_k = P[k|k-1] H^T S_k^{-1}

Update step:
x[k|k] = x[k|k-1] + K_k y_k
P[k|k] = (I - K_k H) P[k|k-1]

[5.2] Extended Kalman filter (EKF) – notation

Nonlinear dynamics and measurements:
x_{k+1} = f(x_k, u_k) + w_k
z_k = h(x_k) + v_k

Linearize at x[k|k]:
F_k = ∂f/∂x |{x[k|k], u_k}
H_k = ∂h/∂x |{x[k|k]}

Then apply Kalman update with F_k, H_k.

[5.3] Multi-sensor fusion (cameras, LiDAR, radar)

State vector example (ego pose and velocities):
x = [x, y, z, v_x, v_y, v_z, roll, pitch, yaw]^T

Measurement functions:
z_cam = h_cam(x) (project 3D points to image plane)
z_lidar = h_lidar(x) (transform into LiDAR frame)
z_radar = h_radar(x) (range, bearing, range rate)

Combined measurement likelihood (assuming independent Gaussian noise):
p(z | x) ∝ exp(-0.5 (z - h(x))^T R^{-1} (z - h(x)))

[6] VEHICLE DYNAMICS AND CONTROL

[6.1] Kinematic bicycle model (flat road, front wheel steering)

State:
x : global x position
y : global y position
ψ : yaw / heading angle
v : longitudinal speed
Control inputs:
a : longitudinal acceleration
δ : front-wheel steering angle
Parameters:
L : wheelbase (distance between front and rear axle)

---


## Page 10

Continuous-time dynamics:
x☐ = v cos ψ
y☐ = v sin ψ
ψ☐ = (v / L) tan δ
v☐ = a

Discrete-time (Euler, step Δt):
x_{k+1} = x_k + Δt v_k cos ψ_k
y_{k+1} = y_k + Δt v_k sin ψ_k
ψ_{k+1} = ψ_k + Δt (v_k / L) tan δ_k
v_{k+1} = v_k + Δt a_k

[6.2] Pure pursuit lateral control

Variables:
L : wheelbase
l_d : lookahead distance
(x_tp,y_tp): target point coordinates in vehicle frame
α : angle between vehicle heading and line to target

Angle to target:
α = atan2(y_tp, x_tp)

Front wheel steering command:
δ = atan( (2 L sin α) / l_d )

[6.3] PID controller (scalar form)

Error:
e(t) = SP - PV(t)

Control law:
u(t) = K_p e(t) + K_i ∫_0^t e(τ) dτ + K_d de(t)/dt

Discrete-time approximation (sample period Δt):
e_k = SP - PV_k
I_k = I_{k-1} + e_k Δt
D_k = (e_k - e_{k-1}) / Δt
u_k = K_p e_k + K_i I_k + K_d D_k

[6.4] Model predictive control (MPC) cost (linear-quadratic form)

Horizon:
N steps, index k = 0..N-1

State and input:
x_k ∈ R^n, u_k ∈ R^m
Reference trajectory:
x_ref_k

Cost matrices:
Q ≥ 0 (state weight), R > 0 (input weight), P ≥ 0 (terminal weight)

Cost function:
J = Σ_{k=0}^{N-1} (x_k - x_ref_k)^T Q (x_k - x_ref_k)
+ Σ_{k=0}^{N-1} u_k^T R u_k
+ (x_N - x_ref_N)^T P (x_N - x_ref_N)

Subject to linear dynamics (for linear MPC):
x_{k+1} = A x_k + B u_k

Input and state constraints (polyhedral):
u_min ≤ u_k ≤ u_max
x_min ≤ x_k ≤ x_max

---


## Page 11

Quadratic program form:
minimize (1/2) z^T H z + f^T z
subject to Gz ≤ g, Az = b
where z stacks decision variables [x_0..x_N, u_0..u_{N-1}].

[6.5] A* path planning heuristic

Search graph nodes n, start s, goal g.

Path cost from start:
g(n)

Heuristic estimate to goal:
h(n)

Evaluation function:
f(n) = g(n) + h(n)

Admissible heuristic condition:
0 ≤ h(n) ≤ h*(n)
where h*(n) is true minimal cost from n to goal.

[7] ADDITIONAL GEOMETRIC AND PERCEPTION METRICS
---

[7.1] Euclidean distance and norm

Two points p, q ∈ R^d:
d(p, q) = ||p - q||_2 = sqrt( Σ_i (p_i - q_i)^2 )

[7.2] Angle between headings

Heading angles ψ_1, ψ_2 (wrapped to [-π, π]):
Difference (wrapped):
Δψ = wrap_to_pi(ψ_2 - ψ_1)

[7.3] Cross-track and along-track error w.r.t. path segment

Given segment from P0 to P1, vehicle position P.

Direction vector:
v = P1 - P0
u = v / ||v||

Projection scalar:
s = u^T (P - P0)

Closest point on segment (clamped):
s_clamped = clip(s, 0, ||v||)
P_proj = P0 + (s_clamped / ||v||) v

Cross-track error (signed using path normal n):
e_ct = n^T (P - P_proj)

Along-track error:
e_at = s_clamped

[7.4] Bounding box intersection-over-union (IoU)

Axis-aligned 2D boxes A and B:

Intersection dimensions:
w_int = max(0, min(x2_A, x2_B) - max(x1_A, x1_B))
h_int = max(0, min(y2_A, y2_B) - max(y1_A, y1_B))

---


## Page 12

**Areas:**
area_int = w_int * h_int
area_A = (x2_A - x1_A) * (y2_A - y1_A)
area_B = (x2_B - x1_B) * (y2_B - y1_B)

**Union area:**
area_union = area_A + area_B - area_int

**IoU:**
IoU = area_int / area_union (if area_union > 0)

3D bounding boxes use analogous formula with volumes instead of areas.

[7.5] **Occupancy grid mapping (probabilistic update)**

For occupancy cell c with prior probability p_{k-1} = P(occ_c | z_{1:k-1}).

Using log-odds:
l_{k-1} = log( p_{k-1} / (1 - p_{k-1}) )

Measurement inverse sensor model gives:
l_z = log( P(occ_c | z_k) / (1 - P(occ_c | z_k)) )

Log-odds update:
l_k = l_{k-1} + l_z - l_0
where l_0 = log( p_0 / (1 - p_0) ) is prior log-odds.

Convert back to probability:
p_k = 1 - 1 / (1 + exp(l_k))

---

[8] **SIMPLE RAP1-SPECIFIC AGGREGATE RELATIONS**

Given ACM3 specs:
TOPS_cluster ≈ 1600 (sparse INT8 TOPS)
Φ_totalT_max ≈ 5 × 10^9 pixels/s

Approximate per-pixel compute budget (dense-equivalent MACs):

Assume each INT8 MAC counts as 2 operations.
Let TOPS_dense_equiv be an estimate of effective dense compute.

For a time interval T seconds with N_pixels processed:

N_pixels = Φ_total * T
N_ops_max = TOPS_cluster * 10^12 * T
ops_per_pixel_max = N_ops_max / N_pixels

Substituting:
ops_per_pixel_max = (TOPS_cluster * 10^12) / Φ_total

For Φ_total = 5 × 10^9 pixels/s and TOPS_cluster = 1600:

ops_per_pixel_max ≈ (1600 × 10^12) / (5 × 10^9)
≈ 3.2 × 10^5 operations per pixel

(Actual budget is lower due to overheads, memory stalls, safety redundancy, etc., but this is a useful upper bound for RAP1-class hardware budgeting.)

END OF FORMULA COMPENDIUM