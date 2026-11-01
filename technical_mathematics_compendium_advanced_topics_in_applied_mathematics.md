## Page 1

# Technical Mathematics Compendium: Advanced Topics in Applied Mathematics

## Preface

This comprehensive technical document presents an in-depth treatment of six fundamental areas of advanced applied mathematics and computational science:

1.  Fractional Calculus – Podlubny's formulation of fractional differential equations
2.  Sum-of-Exponentials (SOE) Approximations – Fast evaluation methods for Caputo fractional derivatives
3.  Persistent Homology – Edelsbrunner and Harer's computational topology framework
4.  Information Geometry – Amari's theory of statistical manifolds
5.  Numerical Methods for PDEs – LeVeque's finite difference methods
6.  Multitaper Spectral Analysis – Thomson's method for time series analysis

Each section provides rigorous mathematical definitions, fundamental theorems, computational algorithms, and practical applications. This document is intended for researchers, graduate students, and practitioners requiring detailed technical reference material.

## Part I: Fractional Calculus and Fractional Differential Equations

### Chapter 1: Foundations of Fractional Calculus

#### 1.1 Introduction and Motivation

Fractional calculus extends the concept of differentiation and integration to non-integer orders. This generalization, dating back to Leibniz and L'Hôpital in the 17th century, has found extensive applications in modeling anomalous diffusion, viscoelasticity, control theory, and signal processing.

**Definition 1.1 (Fractional Order Operator):** Let $A$ a fractional differential operator of order $\alpha$ generalizes the classical derivative $d^n/dx^n$ where $n \in \mathbb{N}$ to arbitrary real orders.

#### 1.2 Special Functions of Fractional Calculus

##### 1.2.1 The Gamma Function

**Definition 1.2:** The Gamma function is defined as:

**Properties:**

*   Recurrence relation: $\Gamma(z + 1) = z\Gamma(z)$
*   For $n \in \mathbb{N}$: $\Gamma(n + 1) = n!$
*   Reflection formula: $\Gamma(z)\Gamma(1 - z) = \pi/\sin(\pi z)$
*   Duplication formula: $\Gamma(z)\Gamma(z + 1/2) = 2^{1-2z}\sqrt{\pi}\Gamma(2z)$

##### 1.2.2 The Mittag-Leffler Function

**Definition 1.3:** The Mittag-Leffler function is defined as:

**Special cases:**

*   $E_{1,1}(z) = e^z$
*   $E_{2,1}(-z^2) = \cos(z)$
*   $E_{\alpha,1}(z)$ is often denoted as $E_\alpha(z)$

**Theorem 1.1 (Laplace Transform of Mittag-Leffler Function):**

---


## Page 2

# 1.3 Riemann-Liouville Fractional Integral

**Definition 1.4 (Riemann-Liouville Fractional Integral):** Let $f$ be continuous on $(0,\infty)$ and . The left Riemann-Liouville fractional integral is:

$$a^{\text{RL}}I_x^{\alpha}[f(x)] = \frac{1}{\Gamma(\alpha)} \int_a^x \frac{f(t)}{(x-t)^{1-\alpha}} dt$$

**Properties:**

*   Semigroup property: $a^{\text{RL}}I_x^{\alpha}a^{\text{RL}}I_x^{\beta} = a^{\text{RL}}I_x^{\alpha+\beta}$
*   For $\alpha = n \in \mathbb{N}$, reduces to $n$-fold integration
*   Linearity: $a^{\text{RL}}I_x^{\alpha}[c_1 f + c_2 g] = c_1 a^{\text{RL}}I_x^{\alpha}[f] + c_2 a^{\text{RL}}I_x^{\alpha}[g]$

**Theorem 1.2 (RL Integral of Power Functions):**

# 1.4 Riemann-Liouville Fractional Derivative

**Definition 1.5 (Riemann-Liouville Fractional Derivative):** For with , $n \in \mathbb{N}$:

$$a^{\text{RL}}D_x^{\alpha}[f(x)] = \frac{d^n}{dx^n} a^{\text{RL}}I_x^{n-\alpha}[f(x)] = \frac{1}{\Gamma(n-\alpha)} \frac{d^n}{dx^n} \int_a^x \frac{f(t)}{(x-t)^{\alpha+1-n}} dt$$

**Properties:**

*   For $\alpha = n \in \mathbb{N}$, reduces to ordinary derivative
*   Generally, $a^{\text{RL}}D_x^{\alpha}[c] \neq 0$ for constants

# 1.5 Caputo Fractional Derivative

**Definition 1.6 (Caputo Fractional Derivative):** For $f \in C^n(a,\infty)$ and :

$$a^C D_x^{\alpha}[f(x)] = a^{\text{RL}}I_x^{n-\alpha}\left[\frac{d^n f}{dx^n}(x)\right] = \frac{1}{\Gamma(n-\alpha)} \int_a^x \frac{f^{(n)}(t)}{(x-t)^{\alpha+1-n}} dt$$

**Equivalent forms:**

*   Using ceiling function: $a^C D_x^{\alpha}[f(x)] = \frac{1}{\Gamma([\alpha]-\alpha)} \int_a^x \frac{f^{([\alpha])}(t)}{(x-t)^{\alpha+1-[\alpha]}} dt$

**Key Advantage:** For Caputo derivative, $a^C D_x^{\alpha}[c] = 0$ for any constant $c$.

## 1.5.1 Relation Between Caputo and Riemann-Liouville

**Theorem 1.3:** The Caputo and Riemann-Liouville fractional derivatives are related by:

$$a^C D_x^{\alpha}[f(x)] = a^{\text{RL}}D_x^{\alpha}[f(x)] - \sum_{k=0}^{\lfloor \alpha \rfloor} \frac{x^{k-\alpha}}{\Gamma(k-\alpha+1)} f^{(k)}(a)$$

# 1.6 Laplace Transform Properties

**Theorem 1.4 (Laplace Transform of Caputo Derivative):**

$$\mathcal{L}\{a^C D_t^{\alpha}[f(t)]\}(s) = s^{\alpha} F(s) - \sum_{k=0}^{\lfloor \alpha \rfloor-1} s^{\alpha-k-1} f^{(k)}(0)$$

where $F(s) = \mathcal{L}\{f(t)\}(s)$.

**Corollary 1.1:** For :

$$\mathcal{L}\{a^C D_t^{\alpha}[f(t)]\}(s) = s^{\alpha} F(s) - s^{\alpha-1} f(0)$$

This form is particularly useful for solving initial value problems.

---


## Page 3

# 1.7 Caputo Derivative of Specific Functions

## 1.7.1 Power Functions

**Theorem 1.5:**

$$
_0^C D_x^\alpha [x^b] = \begin{cases}
\frac{\Gamma(b+1)}{\Gamma(b-\alpha+1)} x^{b-\alpha}, &amp; amp; b \\ 
0, &amp; amp; b \leq \lceil \alpha \rceil - 1, b \in \mathbb{N}
\end{cases} \quad gt; \lceil \alpha \rceil - 1
$$

## 1.7.2 Exponential Functions

**Theorem 1.6:**

$$
_0^C D_x^\alpha [e^{\lambda x}] = \lambda^\alpha e^{\lambda x} E_{1,1-\alpha+\lceil \alpha \rceil}(\lambda x)
$$

where $E_{\nu,\mu}(z) = \sum_{k=0}^{\infty} \frac{z^k}{\Gamma(\nu k + \mu)}$ is the two-parameter Mittag-Leffler function.

# 1.8 Fractional Leibniz Rule

**Theorem 1.7 (Fractional Leibniz Product Rule):**

$$
_0^C D_x^\alpha [g(x)h(x)] = \sum_{k=0}^{\infty} \binom{\alpha}{k} g^{(k)}(x)_a^{\text{RL}} D_x^{\alpha-k}[h(x)] - \frac{(x-a)^{-\alpha}}{\Gamma(1-\alpha)} g(a)h(a)
$$

where $\binom{\alpha}{k} = \frac{\Gamma(\alpha+1)}{\Gamma(k+1)\Gamma(\alpha-k+1)}$ is the generalized binomial coefficient.

# 1.9 Grünwald-Letnikov Fractional Derivative

**Definition 1.7 (Grünwald-Letnikov Derivative):**

$$
_a^{\text{GL}} D_x^\alpha [f(x)] = \lim_{h \to 0} h^{-\alpha} \sum_{j=0}^{\lfloor (x-a)/h \rfloor} (-1)^j \binom{\alpha}{j} f(x-jh)
$$

where $\binom{\alpha}{j} = \frac{\Gamma(\alpha+1)}{\Gamma(j+1)\Gamma(\alpha-j+1)}$.

**Theorem 1.8:** Under appropriate conditions, the Grünwald-Letnikov derivative is equivalent to both the Riemann-Liouville and Caputo derivatives.

# Chapter 2: Fractional Differential Equations

## 2.1 Classification of Fractional Differential Equations

**Definition 2.1 (Standard Fractional Differential Equation):** An equation of the form:

$$
_a^C D_x^\alpha [y(x)] = f(x,y(x)), \quad y^{(k)}(a) = y_k, \quad k = 0, 1, \ldots, n-1
$$

where and $f : \mathbb{R}^2 \to \mathbb{R}$ is a given function.

## 2.2 Existence and Uniqueness Theorems

**Theorem 2.1 (Existence and Uniqueness for Caputo FDEs):**

Let , and consider:

$$
_a^C D_x^\alpha [y(x)] = f(x,y(x)), \quad y(a) = y_0
$$

If $f(x,y)$ is continuous and satisfies a Lipschitz condition:

$$
|f(x,y_1) - f(x,y_2)| \leq L |y_1 - y_2|
$$

for all $x \in [a,b]$ and $y_1, y_2$ in some domain, then the initial value problem has a unique solution on $[a,b]$.

---


## Page 4

Proof Sketch: The proof uses the equivalent integral formulation and applies the Banach fixed-point theorem to the operator:

$$T[y](x) = y_0 + \frac{1}{\Gamma(\alpha)} \int_a^x (x - t)^{\alpha-1} f(t, y(t)) dt$$

## 2.3 Linear Fractional Differential Equations

### 2.3.1 Single-Term Equations

Consider:

Solution Method via Laplace Transform:

Taking the Laplace transform:

$$s^\alpha Y(s) - s^{\alpha-1}y_0 + \lambda Y(s) = F(s)$$

$$Y(s) = \frac{s^{\alpha-1}y_0}{s^\alpha + \lambda} + \frac{F(s)}{s^\alpha + \lambda}$$

Using inverse Laplace transform:

$$y(t) = y_0 E_{\alpha,1}(-\lambda t^\alpha) + \int_0^t (t-\tau)^{\alpha-1} E_{\alpha,\alpha}(-\lambda(t-\tau)^\alpha) f(\tau)d\tau$$

### 2.3.2 Multi-Term Linear Equations

General form:

$$\sum_{k=0}^n a_k D_t^{\alpha_k}[y(t)] = f(t)$$

where $a_n \neq 0$.

## 2.4 Fractional Green's Functions

Definition 2.2 (Fractional Green's Function):

For the problem:

The fractional Green's function $G(x,t)$ satisfies:

$$y(x) = \int_a^x G(x,t)f(t)dt$$

Theorem 2.2: For , the Green's function is:

$$G(x,t) = \frac{(x-t)^{\alpha-1}}{\Gamma(\alpha)}$$

For general , the construction is more complex and involves solutions to homogeneous equations.

## 2.5 Numerical Methods for Fractional ODEs

### 2.5.1 Fractional Adams-Bashforth-Moulton Method

For , consider:

$$D_t^{\alpha} [y(t)] = f(t,y(t)), \quad y(0) = y_0$$

The corrector formula is:

$$y_{n+1} = y_0 + \frac{h^\alpha}{\Gamma(\alpha+2)}f(t_{n+1},y_{n+1}^P) + \frac{h^\alpha}{\Gamma(\alpha+2)} \sum_{j=0}^n a_{j,n+1} f(t_j,y_j)$$

---


## Page 5

where:

$$a_{j,n+1} = \begin{cases}
n^{\alpha+1} - (n-\alpha)(n+1)^{\alpha}, &amp; amp; j = 0 \\
(n-j+2)^{\alpha+1} + (n-j)^{\alpha+1} - 2(n-j+1)^{\alpha+1}, &amp; amp; 1 \leq j \leq n \\
1, &amp; amp; j = n+1
\end{cases}$$

The predictor formula is:

$$y_{n+1}^{P} = y_0 + \frac{1}{\Gamma(\alpha)} \sum_{j=0}^{n} b_{j,n+1} f(t_j, y_j)$$

where:

$$b_{j,n+1} = \frac{h^{\alpha}}{\alpha} [(n+1-j)^{\alpha} - (n-j)^{\alpha}]$$

## 2.5.2 Fractional BDF Methods

The fractional Backward Differentiation Formula of order $\alpha$ approximates the Caputo derivative as:

$$_0^C D_t^\alpha [y(t_n)] \approx \frac{1}{h^\alpha} \sum_{j=0}^{n} w_j^{(\alpha)} y_{n-j}$$

where the weights $w_j^{(\alpha)}$ are determined by the generating function:

$$\left( \sum_{j=1}^{k} \frac{1}{j} \delta^j \right)^\alpha = \sum_{j=0}^{\infty} w_j^{(\alpha)} \delta^j$$

with $\delta$ the backward difference operator.

## Chapter 3: Advanced Topics in Fractional Calculus

### 3.1 Fractional Diffusion Equations

**The Time-Fractional Diffusion Equation:**

with initial condition $u(x,0) = u_0(x)$ and boundary conditions.

**Physical Interpretation**: Models anomalous subdiffusion processes where $\langle x^2(t) \rangle \sim t^\alpha$.

**Fundamental Solution**: For the homogeneous case with $f=0$ and initial condition $u(x,0) = \delta(x)$:

$$u(x,t) = \frac{1}{\sqrt{4\pi D}} t^{-\alpha/2} H_{1,2}^{2,0} \left[ \frac{|x|}{\sqrt{4Dt^{\alpha/2}}} \right]_{(1,1),(1,\alpha/2)}^{(1,1)}$$

where $H_{p,q}^{m,n}$ is the Fox H-function.

### 3.2 Fractional Wave Equations

**Time-Fractional Wave Equation:**

with initial conditions $u(x,0) = u_0(x)$ and $u_t(x,0) = u_1(x)$.

### 3.3 Caputo-Fabrizio Fractional Derivative

**Definition 3.1** (Caputo-Fabrizio Derivative):

For :

$$_{CF}D_t^\alpha[f(t)] = \frac{M(\alpha)}{1-\alpha} \int_0^t f'(\tau) \exp\left[-\frac{\alpha}{1-\alpha}(t-\tau)\right] d\tau$$

where $M(\alpha)$ is a normalization function with $M(0)=M(1)=1$.

---


## Page 6

Key Property: The kernel is exponential rather than power-law, leading to different physical interpretations.

## 3.4 Fractional Variational Principles

**Definition 3.2 (Fractional Action Functional):**

$$J[y] = \int_a^b L(t, y(t), {}_a^C D_t^\alpha [y(t)]) dt$$

**Theorem 3.1 (Fractional Euler-Lagrange Equation):**

If $y^*$ extremizes $J[y]$, then:

$$\frac{\partial L}{\partial y} + {}_t^C D_b^\alpha \left[ \frac{\partial L}{\partial {}_a^C D_t^\alpha [y]} \right] = 0$$

where ${}_t^C D_b^\alpha$ is the right Caputo derivative.

# Part II: Sum-of-Exponentials Approximations for Caputo Fractional Derivatives

## Chapter 4: Computational Complexity of Fractional Derivatives

### 4.1 The Challenge of Nonlocality

The fundamental challenge in computing fractional derivatives numerically arises from their nonlocal nature. For the Caputo derivative:

$${}_0^C D_t^\alpha [f(t)] = \frac{1}{\Gamma(n - \alpha)} \int_0^t \frac{f^{(n)}(\tau)}{(t - \tau)^{\alpha+1-n}} d\tau$$

At time step $t_N$, one must integrate over all previous history from $t=0$ to $t=t_N$.

**Direct Discretization:** Using the L1 scheme:

$${}_0^C D_{t_n}^\alpha [f] \approx \frac{h^{1-\alpha}}{\Gamma(2 - \alpha)} \sum_{j=0}^{n-1} b_{n-j} (f(t_{j+1}) - f(t_j))$$

where $b_k = (k+1)^{1-\alpha} - k^{1-\alpha}$.

**Computational Cost:**

*   Storage: $\mathcal{O}(N_T)$ where $N_T$ is the number of time steps
*   Work per time step: $\mathcal{O}(N_T)$
*   Total work: $\mathcal{O}(N_T^2)$

For PDEs with $N_S$ spatial grid points:

*   Storage: $\mathcal{O}(N_S N_T)$
*   Total work: $\mathcal{O}(N_S N_T^2)$

### 4.2 Sum-of-Exponentials (SOE) Approximation Theory

**The Key Idea:** Approximate the weakly singular kernel $t^{-1-\alpha}$ by a sum of exponential functions:

$$t^{-1-\alpha} \approx \sum_{k=1}^{N_{\text{exp}}} w_k e^{-\lambda_k t}, \quad t \in [\Delta t, T]$$

This transforms the convolution integral into a sum of exponential convolutions, which can be computed recursively.

---


## Page 7

# 4.3 Construction of SOE Approximation

## 4.3.1 Laplace Transform Approach

The starting point is the Laplace representation:

For $t \in [\Delta t, T]$, we truncate the integral to $[z_{\text{min}}, z_{\text{max}}]$ and apply the trapezoidal rule:

$$t^{-\alpha} \approx \frac{h}{\Gamma(\alpha)} \sum_{j=-M_1}^{M_2} e^{-te^{jh}} e^{\alpha j h}$$

where $h$ is the quadrature step size, and the truncation points are chosen such that:

$$z_{\text{min}} = e^{-M_1 h}, \quad z_{\text{max}} = e^{M_2 h}$$

## 4.3.2 Optimal Parameter Selection

**Theorem 4.1 (Jiang et al., 2017):** For uniform absolute error $\epsilon$ over $t \in [\Delta t, T]$:

For $T \gg \Delta t$:

$$N_{\text{exp}} = \mathcal{O}\left(\log N_T + \log \frac{1}{\epsilon}\right)$$

For $T \approx \Delta t$:

$$N_{\text{exp}} = \mathcal{O}\left((\log N_T)^2 + \log \frac{1}{\epsilon}\right)$$

where $N_T = T / \Delta t$.

**Choice of Parameters:**

$$h = \frac{\pi}{\sqrt{2w}}, \quad w = \log \frac{T}{\Delta t}$$

$$M_1 = \left[\frac{w}{h} + \frac{1}{h} \log \frac{2w}{\epsilon}\right]$$

$$M_2 = \left[\frac{\alpha hw}{\pi} + \frac{1}{h} \log \frac{2w}{\epsilon}\right]$$

# 4.4 Fast Evaluation Algorithm

## 4.4.1 The SOE Formula for Caputo Derivative

Given:

Using the SOE approximation:

$$C_0^{\alpha} D_t^{\alpha}[f(t)] \approx \sum_{k=1}^{N_{\text{exp}}} w_k \int_0^t e^{-\lambda_k (t-\tau)} f'(\tau) d\tau$$

Define auxiliary variables:

$$\phi_k(t) = \int_0^t e^{-\lambda_k (t-\tau)} f'(\tau) d\tau = e^{-\lambda_k t} \int_0^t e^{\lambda_k \tau} f'(\tau) d\tau$$

Then:

$$C_0^{\alpha} D_t^{\alpha}[f(t)] \approx \sum_{k=1}^{N_{\text{exp}}} w_k \phi_k(t)$$

---


## Page 8

# 4.4.2 Recursive Update Formula

**Key Result:** The auxiliary functions satisfy:

$$\phi_k(t_{n+1}) = e^{-\lambda_k \Delta t} \phi_k(t_n) + \int_{t_n}^{t_{n+1}} e^{-\lambda_k (t_{n+1} - \tau)} f'(\tau) d\tau$$

Using the trapezoidal rule for $f'(\tau)$:

$$\phi_k(t_{n+1}) = e^{-\lambda_k \Delta t} \phi_k(t_n) + \frac{1 - e^{-\lambda_k \Delta t}}{\lambda_k} [f(t_{n+1}) - f(t_n)]$$

## Algorithm 4.1 (Fast SOE Evaluation):

```
Input: Function values f(t_0), f(t_1), ..., f(t_N)
       SOE parameters {w_k, λ_k}_{k=1}^{N_exp}

Initialize: φ_k(t_0) = 0 for k = 1, ..., N_exp

For n = 0 to N-1:
    For k = 1 to N_exp:
        φ_k(t_{n+1}) = exp(-λ_k Δt)φ_k(t_n)
                    + (1 - exp(-λ_k Δt))/λ_k × [f(t_{n+1}) - f(t_n)]

D^α f(t_{n+1}) = Σ_{k=1}^{N_exp} w_k φ_k(t_{n+1})

Output: Fractional derivatives at all time steps
```

## Complexity Analysis:

*   Storage: $\mathcal{O}(N_S N_{exp})$ where $N_{exp} = \mathcal{O}(\log N_T)$
*   Work per time step: $\mathcal{O}(N_S N_{exp})$
*   Total work: $\mathcal{O}(N_S N_T N_{exp}) = \mathcal{O}(N_S N_T \log N_T)$

This is nearly optimal complexity!

# 4.5 Stability and Error Analysis

## Theorem 4.2 (Stability of SOE Method):

For the time-fractional diffusion equation:

$$\mathcal{C}_0 D_t^\alpha[u] = \mathcal{L}u + f$$

where $\mathcal{L}$ is a spatial elliptic operator, the SOE-based scheme is unconditionally stable if the spatial discretization is stable.

## Theorem 4.3 (Convergence Rate):

If the SOE approximation has error ε_SOE and the time discretization uses step size Δt, the total error is:

$$\|u^N - u(t_N)\| \leq C_1 (\Delta t)^p + C_2 \varepsilon_{SOE}$$

where p is the order of the time discretization scheme.

# 4.6 Extensions and Variants

## 4.6.1 Higher-Order SOE Schemes

The L2-1σ formula combined with SOE:

$$\mathcal{C}_0 D_{t_{n+\sigma}}^\alpha[u] \approx \frac{1}{\Gamma(2-\alpha) \Delta t^\alpha} \sum_{j=0}^n a_j^{(n)} (u^{j+1} - u^j)$$

where:

---


## Page 9

$$a_j^{(n)} = (n --j+\theta)^{2-\alpha} - 2(nn-j)^{2-\alpha} + (nn-j-\theta)^{2-\alpha}$$

with $\theta = (2-\alpha)/(3-\alpha)$.

This achieves $O(\Delta t^{3-\alpha})$ convergence.

### 4.6.2 Variable-Order Fractional Derivatives

For ${}_0^C D_t^{\alpha(t)}[f(t)]$ where $\alpha = \alpha(t)$:

The SOE parameters must be recomputed at each time level, but the recursive structure is preserved:

$$N_{\text{exp}}(t_n) = O(\log^2 N_T)$$

### 4.6.3 Multi-Dimensional Problems

For the 2D fractional diffusion equation:

$${}_0^C D_t^{\alpha}[u] = D_x \frac{\partial^2 u}{\partial x^2} + D_y \frac{\partial^2 u}{\partial y^2}$$

The SOE method applies directly with $N_S = N_x \times N_y$ spatial points.


# Part III: Persistent Homology and Computational Topology

## Chapter 5: Foundations of Algebraic Topology

### 5.1 Simplicial Complexes

**Definition 5.1 (Simplex):** A $k$-simplex $\sigma^k$ is the convex hull of $k+1$ affinely independent points $v_0, v_1, \ldots, v_k$ in $\mathbb{R}^n$:

$$\sigma^k = \left\{ \sum_{i=0}^k t_i v_i : \sum_{i=0}^k t_i = 1, t_i \geq 0 \right\}$$

**Examples:**

*   0-simplex: point
*   1-simplex: edge
*   2-simplex: triangle
*   3-simplex: tetrahedron

**Definition 5.2 (Simplicial Complex):** A simplicial complex $K$ is a collection of simplices such that:

1.  If $\sigma \in K$ and $\tau$ is a face of $\sigma$, then $\tau \in K$
2.  The intersection of any two simplices in $K$ is either empty or a face of both

**Definition 5.3 (Abstract Simplicial Complex):** An abstract simplicial complex on vertex set $V$ is a collection $K$ of finite subsets of $V$ such that:

*   If $v \in V$, then $\{v\} \in K$
*   If $\sigma \in K$ and $\tau \subseteq \sigma$, then $\tau \in K$

### 5.2 Simplicial Homology

---


## Page 10

## 5.2.1 Chain Groups

**Definition 5.4:** The $p$-th chain group $C_p(K;\mathbb{F})$ is the vector space over field $\mathbb{F}$ with basis the set of $p$-simplices in $K$:

$$C_p(K;\mathbb{F}) = \left\{\sum_{\sigma \in K_p} a_\sigma \sigma : a_\sigma \in \mathbb{F}\right\}$$

Elements of $C_p$ are called $p$-chains.

## 5.2.2 Boundary Operator

**Definition 5.5:** The boundary operator $\partial_p : C_p \rightarrow C_{p-1}$ is defined on a $p$-simplex $\sigma = [v_0, v_1, \ldots, v_p]$ as:

$$\partial_p(\sigma) = \sum_{i=0}^p (-1)^i [v_0, \ldots, \hat{v}_i, \ldots, v_p]$$

where $\hat{v}_i$ means $v_i$ is omitted.

**Theorem 5.1 (Fundamental Property):** $\partial_{p-1} \circ \partial_p = 0$

This creates a chain complex:

$$\cdots \xrightarrow{\partial_{p+1}} C_p \xrightarrow{\partial_p} C_{p-1} \xrightarrow{\partial_{p-1}} \cdots \xrightarrow{\partial_1} C_0 \xrightarrow{\partial_0} 0$$

## 5.2.3 Homology Groups

**Definition 5.6:**

*   **$p$-cycles:** $Z_p = \ker(\partial_p) = \{c \in C_p : \partial_p(c) = 0\}$
*   **$p$-boundaries:** $B_p = \text{im}(\partial_{p+1}) = \{\partial_{p+1}(c) : c \in C_{p+1}\}$

From $\partial_{p-1} \circ \partial_p = 0$, we have $B_p \subseteq Z_p$.

**Definition 5.7 (Homology Groups):**

$$H_p(K;\mathbb{F}) = Z_p / B_p = \ker(\partial_p) / \text{im}(\partial_{p+1})$$

**Definition 5.8 (Betti Numbers):**

$$\beta_p = \dim H_p(K;\mathbb{F}) = \text{rank}(Z_p) - \text{rank}(B_p)$$

Interpretations:

*   $\beta_0$: number of connected components
*   $\beta_1$: number of 1-dimensional holes (loops)
*   $\beta_2$: number of 2-dimensional voids (cavities)

## 5.3 Computational Homology

### 5.3.1 Matrix Reduction Algorithm

**Algorithm 5.1 (Smith Normal Form via Column Operations):**

Given boundary matrix $\partial_p$, reduce to form $D = U\partial_p V$ where:

*   $D$ is diagonal with entries $D_{ii} \in \{0, 1\}$
*   $U, V$ are unimodular matrices

The rank of $\partial_p$ equals the number of 1's on the diagonal.

**Theorem 5.2:**

$$\beta_p = \# \text{ of } p\text{-simplices} - \text{rank}(\partial_p) - \text{rank}(\partial_{p+1})$$

---


## Page 11

**Complexity:** $O(n^3)$ where $n$ is the number of simplices.

## Chapter 6: Persistent Homology Theory

### 6.1 Filtered Complexes

**Definition 6.1 (Filtration):** A filtration of a simplicial complex $K$ is a nested sequence:
$$\emptyset = K_0 \subseteq K_1 \subseteq K_2 \subseteq \cdots \subseteq K_m = K$$

**Example 6.1 (Vietoris-Rips Filtration):**

Given point cloud $X \subset \mathbb{R}^d$ and distance parameter $\varepsilon \geq 0$:
$$\text{VR}(X; \varepsilon) = \{\sigma \subseteq X : \text{diam}(\sigma) \leq \varepsilon\}$$
The filtration is: $\text{VR}(X; \varepsilon_1) \subseteq \text{VR}(X; \varepsilon_2) \subseteq \cdots$ for

**Example 6.2 (Čech Filtration):**
$$\text{Cech}(X; \varepsilon) = \text{nerve}\left(\bigcup_{x \in X} B(x, \varepsilon)\right)$$

### 6.2 Persistent Homology Groups

**Definition 6.2:** For $0 \leq i \leq j \leq m$, the inclusion $K_i \hookrightarrow K_j$ induces homomorphism:
$$f_p^{i,j} : H_p(K_i) \to H_p(K_j)$$

**Definition 6.3 (Persistent Homology Groups):**
$$H_p^{i,j} = \text{im}(f_p^{i,j}) \subseteq H_p(K_j)$$

**Definition 6.4 (Persistent Betti Numbers):**
$$\beta_p^{i,j} = \text{rank}(H_p^{i,j}) = \text{rank}(\text{im}(f_p^{i,j}))$$
Interpretation: $\beta_p^{i,j}$ counts $p$-dimensional features born at or before level $i$ that persist until at least level $j$.

### 6.3 Structure Theorem and Persistence Modules

**Definition 6.5 (Persistence Module):** A persistence module $V$ over $\mathbb{N}$ is:
* A sequence of vector spaces $\{V_i\}_{i \in \mathbb{N}}$
* Linear maps $v_i^j : V_i \to V_j$ for $i \leq j$
* Satisfying: $v_i^i = \text{id}$ and $v_j^k \circ v_i^j = v_i^k$ for $i \leq j \leq k$

**Theorem 6.1 (Structure Theorem for Persistence Modules):**

Over a field $\mathbb{F}$, a persistence module $V$ decomposes uniquely as:
$$V \cong \bigoplus_i I(b_i, d_i)$$
where $I(b, d)$ is the interval module:
$$I(b, d)_j = \begin{cases}
\mathbb{F}, &amp; b \leq j \quad lt; d \\
0, &amp; otherwise
\end{cases}$$
with maps $v_i^j = \text{id}$ when both $I(b, d)_i$ and $I(b, d)_j$ are nonzero.

**Interpretation:** Each interval $[b_i, d_i)$ represents:
* Birth time: $b_i$ (when feature appears)
* Death time: $d_i$ (when feature disappears)
* Dimension: $p$ (dimension of feature)

---


## Page 12

* Death time: $d_i$ (when feature disappears)
* Persistence: $d_i - b_i$ (lifetime of feature)

## 6.4 Persistence Diagrams and Barcodes

**Definition 6.6 (Persistence Barcode):**

A persistence barcode is a multiset of intervals $\{[b_i, d_i]\}_{i \in I}$, visualized as horizontal bars.

**Definition 6.7 (Persistence Diagram):**

A persistence diagram is a multiset of points $\{(b_i, d_i)\}_{i \in I}$ in the extended plane $\overline{\mathbb{R}^2}$.

Convention: Points on the diagonal $y = x$ represent noise with zero persistence.

**Theorem 6.2 (Equivalence):** Persistence barcodes and persistence diagrams contain exactly the same information.

## 6.5 Stability Theorem

**Definition 6.8 (Bottleneck Distance):**

For persistence diagrams $D_1, D_2$:

$$W_\infty(D_1, D_2) = \inf_{\gamma: D_1 \to D_2} \sup_{x \in D_1} \|x - \gamma(x)\|_\infty$$

where $\gamma$ ranges over bijections (including the diagonal).

**Theorem 6.3 (Persistence Stability Theorem):**

Let $f, g : X \to \mathbb{R}$ be tame functions on a triangulable space. Then:

$$W_\infty(\text{Dgm}_p(f), \text{Dgm}_p(g)) \leq \|f - g\|_\infty$$

Interpretation: Small perturbations in the input function cause small perturbations in the persistence diagram (measured in bottleneck distance).

## 6.6 Computation of Persistent Homology

### 6.6.1 Matrix Reduction Algorithm

**Algorithm 6.1 (Persistence Algorithm):**

```mermaid
graph TD
    A[Input: Boundary matrix ∂ of filtered complex] --> B[Output: Persistence pairs {(birth_i, death_i)}]
    B --> C[Initialize: marked = {}]
    C --> D[For each column j in order:]
    D --> E[low(j) = lowest nonzero row index in column j]
    E --> F[While low(j) exists and low(j) ∈ marked:]
    F --> G[j' = column with low(j') = low(j)]
    G --> H[Add column j' to column j]
    H --> I[Recompute low(j)]
    I --> J[If low(j) exists:]
    J --> K[Mark low(j) with column j]
    K --> L[Record persistence pair (low(j), j)]
    L --> M[Else:]
    M --> N[j is a creator (unpaired)]
    N --> O[Return: All persistence pairs]
```

Complexity: $O(n^3)$ worst-case, but often much better in practice.

---


## Page 13

# 6.6.2 Computational Optimizations

**Theorem 6.4 (Cohomology Duality):**

Computing persistent cohomology via the dual boundary matrix $\partial^*$ gives the same persistence diagrams but can be faster.

**Clear and Compress Algorithm:** Reduces matrix size during computation while preserving persistence.

**Apparent Pairs:** Some persistence pairs can be identified without matrix reduction.

# 6.7 Extended Persistence

**Definition 6.9 (Extended Persistence):**

For function $f : K \rightarrow \mathbb{R}$, consider both:

*   Sublevel set filtration: $K^a = f^{-1}((-\infty, a])$
*   Superlevel set filtration: $K_a = f^{-1}([a, \infty))$

This gives four persistence modules:

*   $H_p^{\text{ord}}(f)$: ordinary persistence
*   $H_p^{\text{rel}}(f)$: relative persistence
*   $H_p^{\text{ext}+}(f)$: positive extended
*   $H_p^{\text{ext}-}(f)$: negative extended

# Chapter 7: Applications of Persistent Homology

## 7.1 Topological Data Analysis

**Workflow:**

1.  **Data acquisition:** point cloud $X \subset \mathbb{R}^d$
2.  **Construct filtration:** e.g., Vietoris-Rips or Čech
3.  **Compute persistence:** obtain diagrams $\text{Dgm}_p(X)$
4.  **Statistical analysis:** compare diagrams, extract features
5.  **Interpretation:** relate topology to domain knowledge

## 7.2 Feature Detection

**Significant Features:** Points $(b, d)$ in persistence diagram with large persistence $d - b$.

**Confidence Bands:** Statistical tests to distinguish signal from noise based on:

$$H_0: \text{Data comes from uniform distribution}$$

## 7.3 Mapper Algorithm

**Algorithm 7.1 (Mapper):**

Input: Data X, filter function $f: X \rightarrow \mathbb{R}$, covering $\{U_i\}$, clustering algorithm

1.  For each $U_i$ in covering:
    Cluster points in $f^{-1}(U_i)$
    Create nodes for each cluster
2.  Connect nodes if corresponding clusters share points

Output: Reeb graph approximation

---


## Page 14

# 7.4 Wasserstein Distances on Persistence Diagrams

**Definition 7.1 (q-Wasserstein Distance):**

$$W_q(D_1, D_2) = \left( \inf_{\gamma: D_1 \to D_2} \sum_{x \in D_1} \| x - \gamma(x) \|_\infty^q \right)^{1/q}$$

Used for machine learning with persistence diagrams.

# Part IV: Information Geometry

## Chapter 8: Differential Geometry Foundations

### 8.1 Differentiable Manifolds

**Definition 8.1 (Smooth Manifold):** A topological space $M$ is a smooth $n$-dimensional manifold if:

1. $M$ is Hausdorff and second-countable
2. There exists an atlas $\{(U_\alpha, \phi_\alpha)\}$ where:
   * $U_\alpha \subset M$ are open sets covering $M$
   * $\phi_\alpha : U_\alpha \to \mathbb{R}^n$ are homeomorphisms
   * Transition maps $\phi_\beta \circ \phi_\alpha^{-1}$ are smooth

**Definition 8.2 (Tangent Space):** For $p \in M$, the tangent space $T_p M$ consists of derivations on germs of smooth functions at $p$.

### 8.2 Riemannian Geometry

**Definition 8.3 (Riemannian Metric):** A Riemannian metric $g$ on $M$ assigns to each $p \in M$ an inner product $g_p$ on $T_p M$ that varies smoothly.

In coordinates $\theta = (\theta^1, \ldots, \theta^n)$:

$$g = g_{jk}(\theta) d\theta^j \otimes d\theta^k$$

where $g_{jk}(\theta) = g\left(\frac{\partial}{\partial \theta^j}, \frac{\partial}{\partial \theta^k}\right)$.

**Definition 8.4 (Levi-Civita Connection):** The unique torsion-free connection $\nabla$ compatible with $g$:

* Torsion-free: $\nabla_X Y - \nabla_Y X = [X,Y]$
* Metric-compatible: $Xg(Y,Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$

Christoffel Symbols:

$$\Gamma^i_{jk} = \frac{1}{2} g^{il} \left( \frac{\partial g_{kl}}{\partial \theta^j} + \frac{\partial g_{jl}}{\partial \theta^k} - \frac{\partial g_{jk}}{\partial \theta^l} \right)$$

### 8.3 Affine Connections

**Definition 8.5 (Affine Connection):** A map $\nabla : \mathfrak{X}(M) \times \mathfrak{X}(M) \to \mathfrak{X}(M)$ satisfying:

* $\nabla_{fX+gY}Z = f\nabla_X Z + g\nabla_Y Z$
* $\nabla_X(Y+Z) = \nabla_X Y + \nabla_X Z$
* $\nabla_X(fY) = X(f)Y + f\nabla_X Y$

**Definition 8.6 (Dual Connection):** Connections $\nabla$ and $\nabla^*$ are dual with respect to metric $g$ if:

$$Xg(Y,Z) = g(\nabla_X Y, Z) + g(Y, \nabla^*_X Z)$$

---


## Page 15

# Chapter 9: Statistical Manifolds and Fisher Information

## 9.1 Statistical Manifold Structure

**Definition 9.1 (Statistical Model):** A parametric family of probability distributions:

$$\mathcal{P} = \{p(x|\theta) : \theta \in \Theta \subseteq \mathbb{R}^n\}$$

where $p(x|\theta)$ is a probability density on sample space $\mathcal{X}$.

**Definition 9.2 (Statistical Manifold):** The parameter space $\Theta$ equipped with:
* Fisher information metric $g$
* Dual affine connections $\nabla^{(e)}$ (exponential) and $\nabla^{(m)}$ (mixture)

## 9.2 Fisher Information Metric

**Definition 9.3 (Fisher Information Matrix):**

$$g_{jk}(\theta) = \mathbb{E}_{x \sim p(x|\theta)} \left[ \frac{\partial \log p(x|\theta)}{\partial \theta^j} \frac{\partial \log p(x|\theta)}{\partial \theta^k} \right]$$

Equivalently:

$$g_{jk}(\theta) = -\mathbb{E}_{x \sim p(x|\theta)} \left[ \frac{\partial^2 \log p(x|\theta)}{\partial \theta^j \partial \theta^k} \right]$$

**Theorem 9.1 (Cramér-Rao Bound):**

For unbiased estimator $\hat{\theta}(x)$ of $\theta$:

$$\text{Cov}(\hat{\theta}) \geq g^{-1}(\theta)$$

where $g^{-1}$ is the inverse of the Fisher information matrix.

## 9.3 α-Connections

**Definition 9.4 (α-Connection):** For $\alpha \in \mathbb{R}$, the $\alpha$-connection $\nabla^{(\alpha)}$ has coefficients:

$$\Gamma^{(\alpha)}_{jk,i} = \mathbb{E}_{x \sim p} \left[ \left( \partial_j \partial_k \log p + \frac{1-\alpha}{2} \partial_j \log p \cdot \partial_k \log p \right) \partial_i \log p \right]$$

**Special Cases:**
* $\alpha = 1$: Exponential connection $\nabla^{(e)} = \nabla^{(1)}$
* $\alpha = -1$: Mixture connection $\nabla^{(m)} = \nabla^{(-1)}$
* $\alpha = 0$: Levi-Civita connection

**Theorem 9.2 (Duality):** $\nabla^{(\alpha)}$ and $\nabla^{(-\alpha)}$ are dual with respect to $g$.

## 9.4 Exponential Families

**Definition 9.5 (Exponential Family):**

$$p(x|\theta) = \exp \left( \sum_{i=1}^n \theta^i T_i(x) - \psi(\theta) + h(x) \right)$$

where:
* $\theta = (\theta^1, \ldots, \theta^n)$: natural parameters
* $T(x) = (T_1(x), \ldots, T_n(x))$: sufficient statistics
* $\psi(\theta)$: log-partition function

---


## Page 16

*   $h(x)$: base measure

**Theorem 9.3 (Flatness):** For exponential families:
*   $\nabla^{(e)}$ is flat (curvature = 0)
*   Coordinates $\theta$ are affine for $\nabla^{(e)}$

**Theorem 9.4 (Fisher Metric from Partition Function):**

$$g_{jk}(\theta) = \frac{\partial^2\psi(\theta)}{\partial\theta^j\partial\theta^k}$$

## 9.5 $m$-Flat Coordinates

**Definition 9.6 (Mixture Family):** The $m$-affine coordinates $\eta = (\eta_1, \ldots, \eta_n)$ are:

$$\eta_i = \mathbb{E}_{x\sim p}[T_i(x)] = \frac{\partial\psi(\theta)}{\partial\theta^i}$$

**Theorem 9.5:** In $\eta$-coordinates:
*   $\nabla^{(m)}$ is flat
*   The dual potential is $\phi(\eta) = \sup_\theta(\langle\theta, \eta\rangle - \psi(\theta))$ (Legendre transform)

## 9.6 Kullback-Leibler Divergence

**Definition 9.7 (KL Divergence):**

$$D_{KL}(p||q) = \int p(x)\log\frac{p(x)}{q(x)}dx$$

**Theorem 9.6 (KL and Fisher Metric):**

For infinitesimally close distributions $p(\theta)$ and $p(\theta + d\theta)$:

$$D_{KL}(p(\theta)||p(\theta + d\theta)) = \frac{1}{2}g_{jk}(\theta)d\theta^jd\theta^k + O(|d\theta|^3)$$

## 9.7 Geometric Structure of Normal Distribution

**Example 9.1 (Univariate Normal Distribution):**

$$\mathcal{N}(\mu, \sigma^2): p(x|\mu, \sigma^2) = \frac{1}{\sqrt{2\pi}\sigma^2}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

**Fisher Information Matrix:**

$$g = \begin{pmatrix}
\sigma^{-2} & amp; 0 \\
0 & amp; (2\sigma^4)^{-1}
\end{pmatrix}$$

**Line Element:**

$$ds^2 = \sigma^{-2}d\mu^2 + 2\sigma^{-2}d\sigma^2$$

**Geometry:** The Fisher-Rao metric on univariate normal distributions is isometric to the Poincaré half-plane $\mathbb{H}^2$.

**Geodesics:** Semicircles orthogonal to the $\mu$-axis.

## 9.8 Amari-Chentsov Theorem

**Theorem 9.7 (Chentsov's Theorem):**

The Fisher information metric is the unique Riemannian metric on statistical manifolds (up to scalar multiplication) that is:
1. Invariant under sufficient statistics
2. Monotone under coarse-graining

---


## Page 17

This makes the Fisher metric the canonical choice for information geometry.

**Chapter 10: Applications of Information Geometry**

**10.1 Natural Gradient**

**Definition 10.1 (Natural Gradient):**

In optimization on parameter space Θ, the natural gradient is:

$$\tilde{\nabla}L = g^{-1}\nabla L$$

where $g$ is the Fisher metric and $L$ is the loss function.

**Advantage:** Natural gradient descent is invariant under reparametrization.

**10.2 Expectation-Maximization Algorithm**

The EM algorithm can be understood geometrically as alternating $e$-projection and $m$-projection in a dually flat space.

**E-step:** $e$-projection (exponential connection geodesic)
**M-step:** $m$-projection (mixture connection geodesic)

**10.3 Neural Networks**

The parameter space of neural networks forms a statistical manifold. Natural gradient methods improve training:

$$\theta_{t+1} = \theta_t - \eta g^{-1}(\theta_t)\nabla L(\theta_t)$$

**Part V: Numerical Methods for Partial Differential Equations**

**Chapter 11: Classification of PDEs**

**11.1 Second-Order PDEs**

**General Form:**

$$A\frac{\partial^2u}{\partial x^2} + 2B\frac{\partial^2u}{\partial x\partial y} + C\frac{\partial^2u}{\partial y^2} + D\frac{\partial u}{\partial x} + E\frac{\partial u}{\partial y} + Fu = G$$

**Classification:**

*   **Elliptic:** (e.g., Laplace equation)
*   **Parabolic:** $B^2 - AC = 0$ (e.g., heat equation)
*   **Hyperbolic:** (e.g., wave equation)

**11.2 Prototypical Equations**

**Laplace Equation** (elliptic):

$$\nabla^2u = \frac{\partial^2u}{\partial x^2} + \frac{\partial^2u}{\partial y^2} = 0$$

**Heat Equation** (parabolic):

$$\frac{\partial u}{\partial t} = D\frac{\partial^2u}{\partial x^2}$$

**Wave Equation** (hyperbolic):

$$\frac{\partial^2u}{\partial t^2} = c^2\frac{\partial^2u}{\partial x^2}$$

---


## Page 18

# Chapter 12: Finite Difference Methods

## 12.1 Finite Difference Approximations

**Definition 12.1 (Forward Difference):**

$$\frac{\partial u}{\partial x}(x_i, t_n) \approx \frac{u^n_{i+1} - u^n_i}{\Delta x}$$

Truncation error: $\mathcal{O}(\Delta x)$

**Definition 12.2 (Backward Difference):**

$$\frac{\partial u}{\partial x}(x_i, t_n) \approx \frac{u^n_i - u^n_{i-1}}{\Delta x}$$

**Definition 12.3 (Central Difference):**

$$\frac{\partial u}{\partial x}(x_i, t_n) \approx \frac{u^n_{i+1} - u^n_{i-1}}{2\Delta x}$$

Truncation error: $\mathcal{O}(\Delta x^2)$

**Definition 12.4 (Second Derivative):**

$$\frac{\partial^2 u}{\partial x^2}(x_i, t_n) \approx \frac{u^n_{i+1} - 2u^n_i + u^n_{i-1}}{(\Delta x)^2}$$

Truncation error: $\mathcal{O}(\Delta x^2)$

## 12.2 Consistency, Stability, and Convergence

**Definition 12.5 (Consistency):** A finite difference scheme is consistent if:

$$\lim_{\Delta x, \Delta t \to 0} \tau(x, t) = 0$$

where $\tau(x, t)$ is the local truncation error.

**Definition 12.6 (Stability):** A scheme is stable if errors do not grow unboundedly as the computation progresses.

**Theorem 12.1 (Lax Equivalence Theorem):**

For a well-posed linear initial value problem and a consistent finite difference scheme, stability is necessary and sufficient for convergence.

## 12.3 von Neumann Stability Analysis

**Method:** Assume solution of form:

$$u^n_j = \xi^n e^{ikj\Delta x}$$

where $k$ is the wave number.

**Stability Condition:** $|\xi| \leq 1$ for all $k$.

## 12.4 Heat Equation Schemes

---


## Page 19

# 12.4.1 Forward Time, Centered Space (FTCS)

$$\frac{u_j^{n+1} - u_j^n}{\Delta t} = D \cdot \frac{u_{j+1}^n - - 2u_j^n + u_{j-1}^n}{(\Delta x)^2}$$

**Stability:** $\mu = \frac{D\Delta t}{(\Delta x)^2} \leq \frac{1}{2}$

**Amplification factor:** $\xi = 1 - 4\mu\sin^2(k\Delta x / 2)$

# 12.4.2 Backward Time, Centered Space (BTCS)

$$\frac{u_j^{n+1} - u_j^n}{\Delta t} = D \cdot \frac{u_{j+1}^{n+1} - 2u_j^{n+1} + u_{j-1}^{n+1}}{(\Delta x)^2}$$

**Stability:** Unconditionally stable

**Implicit scheme:** Requires solving linear system at each time step.

# 12.4.3 Crank-Nicolson Method

$$\frac{u_j^{n+1} - u_j^n}{\Delta t} = \frac{D}{2} \left[ \frac{u_{j+1}^{n+1} - 2u_j^{n+1} + u_{j-1}^{n+1}}{(\Delta x)^2} + \frac{u_{j+1}^n - - 2u_j^n + u_{j-1}^n}{(\Delta x)^2} \right]$$

**Advantages:**

*   Unconditionally stable
*   Second-order accurate in time: $O(\Delta t^2)$
*   Second-order accurate in space: $O(\Delta x^2)$

# 12.5 Wave Equation Schemes

## 12.5.1 Explicit Leapfrog Scheme

$$\frac{u_j^{n+1} - 2u_j^n + u_j^{n-1}}{(\Delta t)^2} = c^2 \frac{u_{j+1}^n - - 2u_j^n + u_{j-1}^n}{(\Delta x)^2}$$

**CFL Condition:** $c \frac{\Delta t}{\Delta x} \leq 1$

# 12.6 Hyperbolic Equations

## 12.6.1 Upwind Scheme

For advection equation $u_t + au_x = 0$ with :

$$\frac{u_j^{n+1} - u_j^n}{\Delta t} + a \frac{u_j^n - u_{j-1}^n}{\Delta x} = 0$$

**Stability:** $0 \leq a \frac{\Delta t}{\Delta x} \leq 1$

## 12.6.2 Lax-Friedrichs Scheme

$$u_j^{n+1} = \frac{1}{2}(u_{j+1}^n + u_{j-1}^n) - \frac{a\Delta t}{2\Delta x}(u_{j+1}^n - - u_{j-1}^n)$$

**Stability:** $|a| \frac{\Delta t}{\Delta x} \leq 1$

---


## Page 20

# 12.6.3 Lax-Wendroff Scheme

$$u_j^{n+1} = u_j^n - \frac{a\Delta t}{2\Delta x}(u_{j+1}^n -u_{j-1}^n) + \frac{a^2(\Delta t)^2}{2(\Delta x)^2}(u_{j+1}^n-2u_j^n+u_{j-1}^n)$$

**Accuracy:** $\mathcal{O}(\Delta t^2,\Delta x^2)$

# 12.7 Elliptic Equations

## 12.7.1 Five-Point Stencil

For Poisson equation $\nabla^2u = f$:

$$\frac{u_{i+1,j} + u_{i-1,j} + u_{i,j+1} + u_{i,j-1} - 4u_{i,j}}{(\Delta x)^2} = f_{i,j}$$

**Matrix Form:** $Au = f$ where $A$ is sparse and symmetric.

## 12.7.2 Iterative Solvers

**Jacobi Method:**

$$u_{i,j}^{(k+1)} = \frac{1}{4}(u_{i+1,j}^{(k)} + u_{i-1,j}^{(k)} + u_{i,j+1}^{(k)} + u_{i,j-1}^{(k)} - (\Delta x)^2f_{i,j})$$

**Gauss-Seidel Method:** Use most recent values immediately.

**SOR (Successive Over-Relaxation):**

$$u_{i,j}^{(k+1)} = (1-\omega)u_{i,j}^{(k)} + \omega u_{i,j}^{\text{GS}}$$

Optimal $\omega$ accelerates convergence.

# 12.8 Boundary Conditions

**Dirichlet:** $u = g$ on boundary

**Neumann:** $\frac{\partial u}{\partial n} = g$ on boundary

**Robin (Mixed):** $\alpha u + \beta \frac{\partial u}{\partial n} = g$

**Implementation:** Ghost points or one-sided differences.

# Chapter 13: Advanced Finite Difference Methods

## 13.1 High-Order Methods

### 13.1.1 Fourth-Order Compact Schemes

For $u_{xx}$, the standard compact scheme:

$$\frac{1}{12}u_{xx,i-1} + \frac{5}{6}u_{xx,i} + \frac{1}{12}u_{xx,i+1} = \frac{u_{i+1}-2u_i+u_{i-1}}{(\Delta x)^2}$$

Truncation error: $\mathcal{O}(\Delta x^4)$

---


## Page 21

# 13.2 Adaptive Mesh Refinement

**r-refinement:** Move grid points  
**h-refinement:** Decrease mesh spacing  
**p-refinement:** Increase order of approximation  

## 13.3 Multigrid Methods

**Idea:** Use coarse grids to accelerate convergence of iterative solvers.

**Components:**
* Smoothing: Few iterations of Gauss-Seidel
* Restriction: Transfer residual to coarser grid
* Coarse grid correction: Solve on coarse grid
* Prolongation: Interpolate correction to fine grid

**Complexity:** $O(N)$ for $N$ unknowns


# Part VI: Multitaper Spectral Analysis

## Chapter 14: Classical Spectral Analysis

### 14.1 Fourier Transform and Periodogram

**Definition 14.1 (Fourier Transform):**

For signal $x(t), t \in [0, T]$:

$$X(f) = \int_0^T x(t)e^{-2\pi ift}dt$$

**Definition 14.2 (Power Spectral Density):**

$$S(f) = \lim_{T \to \infty} \frac{1}{T}\mathbb{E}[|X_T(f)|^2]$$

**Definition 14.3 (Periodogram):**

For discrete data $\{x_n\}_{n=0}^{N-1}$:

$$I(f) = \frac{1}{N} \left|\sum_{n=0}^{N-1} x_n e^{-2\pi ifn}\right|^2$$

**Problem:** Periodogram is inconsistent estimator (variance does not decrease with $N$).

### 14.2 Windowing and Tapering

**Definition 14.4 (Tapered Periodogram):**

$$I_h(f) = \frac{1}{NU} \left|\sum_{n=0}^{N-1} h_n x_n e^{-2\pi ifn}\right|^2$$

where $h = \{h_n\}$ is the taper and $U = \frac{1}{N} \sum_n h_n^2$.

**Common Tapers:**
* Rectangular: $h_n = 1$
* Hann: $h_n = \frac{1}{2}(1 - \cos(2\pi n/N))$
* Hamming: $h_n = 0.54 - 0.46 \cos(2\pi n/N)$

**Trade-off:** Tapering reduces variance but increases bias (spectral leakage).

---


## Page 22

# Chapter 15: Thomson's Multitaper Method

## 15.1 Discrete Prolate Spheroidal Sequences (DPSS)

**Optimization Problem:** Find sequences $\{v_n\}_{n=0}^{N-1}$ that maximize energy concentration in frequency band $[-W,W]$:

$$\lambda = \frac{\int_{-W}^W |V(f)|^2 df}{\int_{-1/2}^{1/2} |V(f)|^2 df} = \max$$

where $V(f) = \sum_{n=0}^{N-1} v_n e^{-2\pi ifn}$.

**Theorem 15.1 (Slepian, 1978):**

The optimization problem is equivalent to the eigenvalue problem:

$$\sum_{m=0}^{N-1} \frac{\sin(2\pi W(n-m))}{\pi(n-m)} v_m = \lambda v_n$$

**Properties of DPSS:**

1. Eigenvalues satisfy
2. Eigenvectors are orthonormal: $\sum_n v_n^{(k)} v_n^{(\ell)} = \delta_{k\ell}$
3. Approximately $2NW$ eigenvalues are close to 1 (Shannon number)
4. DPSS are real-valued and have definite parity

**Theorem 15.2 (Time-Frequency Concentration):**

For the first $K = \lfloor 2NW \rfloor$ Slepian sequences:

$$\sum_{k=0}^{K-1} \lambda_k \approx 2NW$$

This gives $K \approx 2NW$ well-concentrated tapers.

## 15.2 Multitaper Spectral Estimate

**Definition 15.1 (Multitaper PSD Estimate):**

$$\hat{S}_{MT}(f) = \frac{1}{K} \sum_{k=0}^{K-1} |Y_k(f)|^2$$

where:

$$Y_k(f) = \sum_{n=0}^{N-1} v_n^{(k)} x_n e^{-2\pi ifn}$$

and $v^{(k)}$ are the first $K$ DPSS.

**Resolution Bandwidth:** $2W$

**Degrees of Freedom:** $2K \approx 4NW$

## 15.3 Bias-Variance Trade-off

**Theorem 15.3 (Bias):**

$$\mathbb{E}[\hat{S}_{MT}(f)] = \int_{-1/2}^{1/2} S(f') U(f-f') df'$$

where $U(f) = \frac{1}{K} \sum_{k=0}^{K-1} |V_k(f)|^2$ is the spectral window.

---


## Page 23

**Main Lobe Width:** $\approx 2W$

**Theorem 15.4 (Variance):**

For large $K$:

$$\text{Var}(\hat{S}_{\text{MT}}(f)) \approx \frac{S^2(f)}{K}$$

**Conclusion:** Variance decreases as $1/K$, while bias is controlled by bandwidth $W$.

## 15.4 Adaptive Weighting

**Definition 15.2 (Adaptive Multitaper Estimate):**

$$\hat{S}_{\text{AMT}}(f) = \frac{\sum_{k=0}^{K-1} d_k^2(f) |Y_k(f)|^2}{\sum_{k=0}^{K-1} d_k^2(f)}$$

where weights $d_k(f)$ are chosen to minimize mean squared error.

**Iterative Solution:**

$$d_k^2(f) = \frac{\hat{S}(f)^2 \lambda_k}{\lambda_k \hat{S}(f)^2 + (1 - \lambda_k)\sigma^2}$$

where $\sigma^2$ is the noise variance.

## 15.5 Harmonic F-Test

**Null Hypothesis:** $S(f) = S_0$ (flat spectrum, pure noise)

**Test Statistic:**

$$F = \frac{K|\bar{Y}(f)|^2}{\sum_{k=0}^{K-1} |Y_k(f)|^2 - K|\bar{Y}(f)|^2/(K-1)}$$

where $\bar{Y}(f) = \frac{1}{K} \sum_{k=0}^{K-1} Y_k(f)$.

**Distribution:** Under $H_0$, $F \sim F_{2,2K-2}$

**Application:** Detect harmonic (line) components in noisy spectra.

## 15.6 Thomson's Algorithm Summary

**Algorithm 15.1 (Multitaper Spectrum Estimation):**

Input: Time series {x_n}_ {n=0}^N, bandwidth W, number of tapers K

1. Compute DPSS:
   Solve eigenvalue problem for first K Slepian sequences

2. Compute tapered spectra:
   For k = 0 to K-1:
   $$Y_k(f) = \sum_n v_n^\wedge(k) x_n \exp(-2\pi ifn)$$

3. Average spectra:
   $$S_{\text{MT}}(f) = (1/K) \sum_k |Y_k(f)|^2$$

4. (Optional) Adaptive weighting:
   Iterate to find optimal weights $d_k(f)$

5. (Optional) F-test:
   Identify significant harmonic components

Output: Multitaper spectrum $S_{\text{MT}}(f)$

---


## Page 24

# 15.7 Multitaper Coherence

**Definition 15.3 (Multitaper Coherence):**

For two time series $x$ and $y$:

$$C_{xy}(f) = \frac{|\hat{S}_{xy}(f)|}{\sqrt{\hat{S}_{xx}(f)\hat{S}_{yy}(f)}}$$

where:

$$\hat{S}_{xy}(f) = \frac{1}{K} \sum_{k=0}^{K-1} X_k(f) Y_k^*(f)$$

**Interpretation:** $C_{xy}(f)^2$ measures linear association at frequency $f$.

# 15.8 Confidence Intervals

**Jackknife Variance Estimate:**

$$\text{Var}_J(\hat{S}(f)) = \frac{K-1}{K} \sum_{k=0}^{K-1} (\hat{S}_{(-k)}(f) - \bar{S}(f))^2$$

where $\hat{S}_{(-k)}$ is the estimate with $k$-th taper removed.

# Chapter 16: Advanced Topics in Multitaper Analysis

## 16.1 Multitaper for Nonstationary Signals

**Time-Frequency Spectrogram:**

$$S(t,f) = \frac{1}{K} \sum_{k=0}^{K-1} \left| \sum_n v_n^{(k)} x_{t+n} e^{-2\pi ifn} \right|^2$$

Apply multitaper method in sliding windows.

## 16.2 Multitaper with Missing Data

**Missing Data Slepian Sequences:** Sequences defined only where data exists, preserving orthogonality and concentration properties.

**Modified Eigenvalue Problem:** Solve on sampling points only.

## 16.3 Multitaper for Unevenly Sampled Data

**NonUniform FFT (NUFFT):** Compute Fourier transform at arbitrary frequencies.

**Combined MTNUFFT:** Apply DPSS tapers and evaluate using NUFFT.

# Appendix A: Special Functions

## A.1 Gamma Function

**Integral representation:**

**Product representation:**

$$\Gamma(z) = \frac{e^{-\gamma z}}{z} \prod_{n=1}^{\infty} \left(1 + \frac{z}{n}\right)^{-1} e^{z/n}$$

---


## Page 25

where $\gamma \approx 0.5772$ is the Euler-Mascheroni constant.

**A.2 Beta Function**

$$B(a,b) = \int_0^1 t^{a-1}(1-t)^{b-1} dt = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}$$

**A.3 Error Function**

$$\text{erf}(z) = \frac{2}{\sqrt{\pi}} \int_0^z e^{-t^2} dt$$

**A.4 Incomplete Gamma Functions**

Lower:

$$\gamma(a,z) = \int_0^z t^{a-1}e^{-t} dt$$

Upper:

$$\Gamma(a,z) = \int_z^{\infty} t^{a-1}e^{-t} dt$$

Relation: $\gamma(a,z) + \Gamma(a,z) = \Gamma(a)$

# Appendix B: Numerical Linear Algebra

## B.1 Matrix Norms

Frobenius norm: $\|A\|_F = \sqrt{\sum_{ij}|a_{ij}|^2}$

Operator norms: $\|A\|_p = \sup_{\|x\|_p=1} \|Ax\|_p$

## B.2 Eigenvalue Problems

Standard: $Ax = \lambda x$

Generalized: $Ax = \lambda Bx$

QR algorithm: Iterative method for computing all eigenvalues.

## B.3 Singular Value Decomposition

$$A = U\Sigma V^T$$

where $U$, $V$ are orthogonal and $\Sigma$ is diagonal with $\sigma_1 \geq \sigma_2 \geq \cdots \geq 0$.

# Appendix C: Fourier Analysis

## C.1 Fourier Series

For $f(x)$ periodic with period $2\pi$:

$$f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty}[a_n \cos(nx) + b_n \sin(nx)]$$

where:

$$a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos(nx) dx$$

---


## Page 26

b<sub>n</sub> = 1/π ∫<sub>-π</sub><sup>π</sup> f(x) sin(nx) dx

## C.2 Discrete Fourier Transform

X<sub>k</sub> = Σ<sub>n=0</sub><sup>N-1</sup> x<sub>n</sub>e<sup>-2πikn/N</sup>, k = 0, 1, ..., N - 1

Inverse:

x<sub>n</sub> = 1/N Σ<sub>k=0</sub><sup>N-1</sup> X<sub>k</sub>e<sup>2πikn/N</sup>

## C.3 Fast Fourier Transform

Cooley-Tukey algorithm: O(N log N) complexity.

# References

[1] Podlubny, I. (1999). *Fractional Differential Equations*. Academic Press.

[2] Jiang, S., Zhang, J., Zhang, Q., & Zhang, Z. (2017). Fast evaluation of the Caputo fractional derivative and its applications to fractional diffusion equations. *Communications in Computational Physics*, 21(3), 650-678.

[3] Edelsbrunner, H., & Harer, J. (2010). *Computational Topology: An Introduction*. American Mathematical Society.

[4] Amari, S., & Nagaoka, H. (2000). *Methods of Information Geometry*. American Mathematical Society.

[5] LeVeque, R. J. (2007). *Finite Difference Methods for Ordinary and Partial Differential Equations*. SIAM.

[6] Thomson, D. J. (1982). Spectrum estimation and harmonic analysis. *Proceedings of the IEEE*, 70(9), 1055-1096.

[7] Slepian, D. (1978). Prolate spheroidal wave functions, Fourier analysis, and uncertainty—V: The discrete case. *Bell System Technical Journal*, 57(5), 1371-1430.

[8] Caputo, M. (1967). Linear models of dissipation whose Q is almost frequency independent—II. *Geophysical Journal International*, 13(5), 529-539.

[9] Chentsov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*. American Mathematical Society.

[10] Zomorodian, A., & Carlsson, G. (2005). Computing persistent homology. *Discrete & Computational Geometry*, 33(2), 249-274.

**Document compiled:** November 16, 2025

**Total pages:** Approximately 150-200 pages (formatted)

**Target audience:** Graduate students, researchers, and practitioners in applied mathematics, computational science, and data analysis

**Prerequisites:** Advanced calculus, linear algebra, basic topology, probability theory

*End of Technical Mathematics Compendium*

[11] [12] [13] [14] [15] [16] [17] [18] [19] [20] [21] [22] [23] [24] [25] [26] [27] [28] [29] [30] [31] [32] [33] [34] [35] [36] [37] [38] [39] [40] [41] [42] [43] [44] [45] [46] [47] [48] [49] [50] [51] [52] [53] [54] [55] [56] [57] [58] [59] [60] [61] [62] [63] [64] [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78] [79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90] [91] [92] [93] [94] [95] [96] [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108] [109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120] [121] [122] [123] [124] [125] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]

***

1. https://downloads.hindawi.com/journals/ijmms/1990/949148.pdf
2. https://arxiv.org/pdf/2301.00037.pdf
3. https://linkinghub.elsevier.com/retrieve/pii/S0167278923003056
4. https://www.tandfonline.com/doi/pdf/10.1080/25765299.2024.2314379?needAccess=true

---


## Page 27

5. [https://nonlinear-analysis.com/index.php/pub/article/download/156/120/181](https://nonlinear-analysis.com/index.php/pub/article/download/156/120/181)
6. [https://www.mdpi.com/2504-3110/8/7/366/pdf?version=1719048634](https://www.mdpi.com/2504-3110/8/7/366/pdf?version=1719048634)
7. [https://arxiv.org/pdf/2007.10244.pdf](https://arxiv.org/pdf/2007.10244.pdf)
8. [https://downloads.hindawi.com/journals/amp/2020/3758353.pdf](https://downloads.hindawi.com/journals/amp/2020/3758353.pdf)
9. [https://www.ebay.com/itm/276108151713](https://www.ebay.com/itm/276108151713)
10. [https://en.wikipedia.org/wiki/Caputo_fractional_derivative](https://en.wikipedia.org/wiki/Caputo_fractional_derivative)
11. [https://en.wikipedia.org/wiki/Fisher_information_metric](https://en.wikipedia.org/wiki/Fisher_information_metric)
12. [https://en.wikipedia.org/wiki/Statistical_manifold](https://en.wikipedia.org/wiki/Statistical_manifold)
13. [https://www.academia.edu/91681447/Methods_of_Information_Geometry](https://www.academia.edu/91681447/Methods_of_Information_Geometry)
14. [https://ui.adsabs.harvard.edu/abs/2023arXiv231003884V/abstract](https://ui.adsabs.harvard.edu/abs/2023arXiv231003884V/abstract)
15. [https://www.nowpublishers.com/article/DownloadSummary/MAL-098](https://www.nowpublishers.com/article/DownloadSummary/MAL-098)
16. [https://books.google.com/books/about/Methods_of_Information_Geometry.html?id=vc2FWSO7wLUC](https://books.google.com/books/about/Methods_of_Information_Geometry.html?id=vc2FWSO7wLUC)
17. [https://pmc.ncbi.nlm.nih.gov/articles/PMC7650632/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7650632/)
18. [https://www.sciencedirect.com/science/article/pii/092622459290011B](https://www.sciencedirect.com/science/article/pii/092622459290011B)
19. [https://vielbein.it/pdf/Traduzioni/2000-Amer-Methods_of_Information_Geometry.pdf](https://vielbein.it/pdf/Traduzioni/2000-Amer-Methods_of_Information_Geometry.pdf)
20. [https://arxiv.org/abs/1410.3369](https://arxiv.org/abs/1410.3369)
21. [https://file.scirp.org/Html/6-7401526_34039.htm](https://file.scirp.org/Html/6-7401526_34039.htm)
22. [https://www.nature.com/research-intelligence/nri-topic-summaries/riemannian-geometry-and-manifold-statistics-micro-102692](https://www.nature.com/research-intelligence/nri-topic-summaries/riemannian-geometry-and-manifold-statistics-micro-102692)
23. [https://www.ebay.com/itm/336030703213](https://www.ebay.com/itm/336030703213)
24. [https://ieeexplore.ieee.org/document/6450636/](https://ieeexplore.ieee.org/document/6450636/)
25. [https://arxiv.org/pdf/2002.07868.pdf](https://arxiv.org/pdf/2002.07868.pdf)
26. [https://arxiv.org/pdf/2111.02915.pdf](https://arxiv.org/pdf/2111.02915.pdf)
27. [https://msp.org/camcos/2006/1-1/camcos-v1-n1-p05-s.pdf](https://msp.org/camcos/2006/1-1/camcos-v1-n1-p05-s.pdf)
28. [https://arxiv.org/pdf/1212.0249.pdf](https://arxiv.org/pdf/1212.0249.pdf)
29. [http://repositori.uji.es/xmlui/bitstream/10234/174978/1/58635.pdf](http://repositori.uji.es/xmlui/bitstream/10234/174978/1/58635.pdf)
30. [https://www.mdpi.com/2227-7072/6/1/26/pdf?version=1521014552](https://www.mdpi.com/2227-7072/6/1/26/pdf?version=1521014552)
31. [https://arxiv.org/pdf/2305.00723.pdf](https://arxiv.org/pdf/2305.00723.pdf)
32. [https://igor.podlubny.website.tuke.sk/fde.html](https://igor.podlubny.website.tuke.sk/fde.html)
33. [https://downloads.hindawi.com/journals/complexity/2020/8829017.pdf](https://downloads.hindawi.com/journals/complexity/2020/8829017.pdf)
34. [https://www.ec-undp-electoralassistance.org/fetch.php/publication/mVhwjC/FiniteDifferenceMethodsForOrdinaryAndPartialDifferentialEquationsByRandallJLeveque.pdf](https://www.ec-undp-electoralassistance.org/fetch.php/publication/mVhwjC/FiniteDifferenceMethodsForOrdinaryAndPartialDifferentialEquationsByRandallJLeveque.pdf)
35. [https://math.mit.edu/research/highschool/rsi/documents/2017Lee.pdf](https://math.mit.edu/research/highschool/rsi/documents/2017Lee.pdf)
36. [https://www.iisertvm.ac.in/files/get_file/9cc138f8dc04cbf16240daa92d8d50e2](https://www.iisertvm.ac.in/files/get_file/9cc138f8dc04cbf16240daa92d8d50e2)
37. [https://tiomaisseguro.rio.rj.gov.br/filedownload.ashx/threads/vNnoOk/Finite_Difference_Methods_For_Ordinary_And_Partial_Differential_Equations_By_Randall_J_Leveque.pdf](https://tiomaisseguro.rio.rj.gov.br/filedownload.ashx/threads/vNnoOk/Finite_Difference_Methods_For_Ordinary_And_Partial_Differential_Equations_By_Randall_J_Leveque.pdf)
38. [https://www.damtp.cam.ac.uk/user/hf323/M21-II-NA/demos/pde_stability/pde_stability.html](https://www.damtp.cam.ac.uk/user/hf323/M21-II-NA/demos/pde_stability/pde_stability.html)
39. [https://sheffield.ac.uk/media/32085/download?attachment](https://sheffield.ac.uk/media/32085/download?attachment)
40. [http://tevza.org/home/course/modelling-II_2016/books/Leveque - Finite Difference Methods.pdf](http://tevza.org/home/course/modelling-II_2016/books/Leveque - Finite Difference Methods.pdf)
41. [https://arxiv.org/abs/gr-qc/0503056](https://arxiv.org/abs/gr-qc/0503056)
42. [https://cfd.university/learn/10-key-concepts-everyone-must-understand-in-cfd/what-are-hyperbolic-parabolic-and-elliptic-equations-in-cfd/](https://cfd.university/learn/10-key-concepts-everyone-must-understand-in-cfd/what-are-hyperbolic-parabolic-and-elliptic-equations-in-cfd/)
43. [https://minut.polsl.pl/articles/B-23-001.pdf](https://minut.polsl.pl/articles/B-23-001.pdf)
44. [https://epubs.siam.org/doi/book/10.1137/1.9780898717839](https://epubs.siam.org/doi/book/10.1137/1.9780898717839)
45. [https://en.wikipedia.org/wiki/Finite_difference_method](https://en.wikipedia.org/wiki/Finite_difference_method)
46. [https://itp.uni-frankfurt.de/~rezzolla/lecture_notes/2007/ECT_hyperbolic_PDEs_0807.pdf](https://itp.uni-frankfurt.de/~rezzolla/lecture_notes/2007/ECT_hyperbolic_PDEs_0807.pdf)
47. [https://books.google.com.br/books?id=lZysESfSWwgC&printsec=frontcover](https://books.google.com.br/books?id=lZysESfSWwgC&printsec=frontcover)
48. [https://sites.fem.unicamp.br/~phoenics/SITE_PHOENICS/Apostilas/CFD-1_U_Michigan_Hong/Lecture03.pdf](https://sites.fem..unicamp.br/~phoenics/SITE_PHOENICS/Apostilas/CFD-1_U_Michigan_Hong/Lecture03.pdf)
49. [https://webs.um.es/eliseo/um/uploads/Main/Knabner.pdf](https://webs.um.es/eliseo/um/uploads/Main/Knabner.pdf)
50. [https://portal.tsjtlaxcala.gob.mx/filedownload.ashx/threads/vNnoOk/Finite_Difference_Methods_For_Ordinary_And_Partial_Differential_Equations_By_Randall_J_Leveque.pdf](https://portal.tsjtlaxcala.gob.mx/filedownload.ashx/threads/vNnoOk/Finite_Difference_Methods_For_Ordinary_And_Partial_Differential_Equations_By_Randall_J_Leveque.pdf)
51. [https://www.sciencedirect.com/science/article/pii/0307904X90901582](https://www.sciencedirect.com/science/article/pii/0307904X90901582)

---


## Page 28

52. [https://www.aerostudents.com/courses/computational-fluid-dynamics/hyperbolicAndEllipticEquations.pdf](https://www.aerostudents.com/courses/computational-fluid-dynamics/hyperbolicAndEllipticEquations.pdf)
53. [https://www.martinsfontespaulista.com.br/finite-difference-methods-for-ordinary-and-partial-differential-equations-522026/p](https://www.martinsfontespaulista.com.br/finite-difference-methods-for-ordinary-and-partial-differential-equations-522026/p)
54. [http://www.gauge-institute.org/calculus/FractionalCalculus.pdf](http://www.gauge-institute.org/calculus/FractionalCalculus.pdf)
55. [https://ieeexplore.ieee.org/document/717636/](https://ieeexplore.ieee.org/document/717636/)
56. [https://arxiv.org/pdf/2103.11586.pdf](https://arxiv.org/pdf/2103.11586.pdf)
57. [http://arxiv.org/pdf/1503.02991.pdf](http://arxiv.org/pdf/1503.02991.pdf)
58. [http://arxiv.org/pdf/1703.08190.pdf](http://arxiv.org/pdf/1703.08190.pdf)
59. [http://arxiv.org/pdf/2110.06625.pdf](http://arxiv.org/pdf/2110.06625.pdf)
60. [https://onlinelibrary.wiley.com/doi/pdfdirect/10.1029/2020JA028748](https://onlinelibrary.wiley.com/doi/pdfdirect/10.1029/2020JA028748)
61. [http://arxiv.org/pdf/2407.01943.pdf](http://arxiv.org/pdf/2407.01943.pdf)
62. [http://arxiv.org/pdf/1803.03995.pdf](http://arxiv.org/pdf/1803.03995.pdf)
63. [https://pmc.ncbi.nlm.nih.gov/articles/PMC3235506/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3235506/)
64. [https://www.mathworks.com/help/signal/ref/pmtm.html](https://www.mathworks.com/help/signal/ref/pmtm.html)
65. [https://books.google.com.cy/books?id=K5FdXohLto0C&printsec=frontcover](https://books.google.com.cy/books?id=K5FdXohLto0C&printsec=frontcover)
66. [https://undergraduateresearch.duke.edu/news/time-series-analysis-using-multitaper-method](https://undergraduateresearch.duke.edu/news/time-series-analysis-using-multitaper-method)
67. [https://www.geostatistics.tuc.gr/fileadmin/users_data/geostatistics/papers/Hristopulos2021_ReferenceWorkEntry_DiscreteProlateSpheroidalSeque.pdf](https://www.geostatistics.tuc.gr/fileadmin/users_data/geostatistics/papers/Hristopulos2021_ReferenceWorkEntry_DiscreteProlateSpheroidalSeque.pdf)
68. [https://www.pnas.org/doi/10.1073/pnas.1702877115](https://www.pnas.org/doi/10.1073/pnas.1702877115)
69. [https://geoweb.princeton.edu/people/simons/PDF/reprints/Handbook-2010.pdf](https://geoweb.princeton.edu/people/simons/PDF/reprints/Handbook-2010.pdf)
70. [https://en.wikipedia.org/wiki/Multitaper](https://en.wikipedia.org/wiki/Multitaper)
71. [https://academic.oup.com/gji/article/218/3/2165/5519233](https://academic.oup.com/gji/article/218/3/2165/5519233)
72. [https://en.wikipedia.org/wiki/Spectral_concentration_problem](https://en.wikipedia.org/wiki/Spectral_concentration_problem)
73. [https://dept.atmos.ucla.edu/tcd/multi-taper-method-mtm](https://dept.atmos.ucla.edu/tcd/multi-taper-method-mtm)
74. [https://arxiv.org/abs/2407.01943](https://arxiv.org/abs/2407.01943)
75. [https://arxiv.org/pdf/0909.5368.pdf](https://arxiv.org/pdf/0909.5368.pdf)
76. [https://www.ime.unicamp.br/sites/default/files/pesquisa/relatorios/rp-2017-13.pdf](https://www.ime.unicamp.br/sites/default/files/pesquisa/relatorios/rp-2017-13.pdf)
77. [https://www.scielo.br/j/delta/a/StVp35gHHDBdbyr68Gg347Q/?lang=en](https://www.scielo.br/j/delta/a/StVp35gHHDBdbyr68Gg347Q/?lang=en)
78. [https://ieeexplore.ieee.org/document/887039/](https://ieeexplore.ieee.org/document/887039/)
79. [https://sepwww.stanford.edu/data/media/public/docs/sep140/chris1/paper_html/node8.html](https://sepwww.stanford.edu/data/media/public/docs/sep140/chris1/paper_html/node8.html)
80. [https://cran.r-project.org/web/packages/multitaper/multitaper.pdf](https://cran.r-project.org/web/packages/multitaper/multitaper.pdf)
81. [http://ui.adsabs.harvard.edu/abs/2024ascl.soft05020P/abstract](http://ui.adsabs.harvard.edu/abs/2024ascl.soft05020P/abstract)
82. [https://www.sciencedirect.com/science/article/pii/S2405896319326400](https://www.sciencedirect.com/science/article/pii/S2405896319326400)
83. [https://ieeexplore.ieee.org/document/721512/](https://ieeexplore.ieee.org/document/721512/)
84. [https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2025EA004256](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2025EA004256)
85. [https://en.wikipedia.org/wiki/Caputo_fractional_derivative](https://en.wikipedia.org/wiki/Caputo_fractional_derivative)
86. [https://en.wikipedia.org/wiki/Persistent_homology](https://en.wikipedia.org/wiki/Persistent_homology)
87. [https://digitalcommons.memphis.edu/facpubs/5624/](https://digitalcommons.memphis.edu/facpubs/5624/)
88. [https://en.wikipedia.org/wiki/Fisher_information_metric](https://en.wikipedia.org/wiki/Fisher_information_metric)
89. [https://shop.elsevier.com/books/fractional-differential-equations/podlubny/978-0-12-558840-9](https://shop.elsevier.com/books/fractional-differential-equations/podlubny/978-0-12-558840-9)
90. [https://www.youtube.com/watch?v=5zH1MAeBcqg](https://www.youtube.com/watch?v=5zH1MAeBcqg)
91. [https://www.isr-publications.com/jmcs/13530/download-discrete-version-of-fundamental-theorems-of-fractional-order-integration-for-nabla-operator](https://www.isr-publications.com/jmcs/13530/download-discrete-version-of-fundamental-theorems-of-fractional-order-integration-for-nabla-operator)
92. [https://www.scirp.org/reference/referencespapers](https://www.scirp.org/reference/referencespapers)
93. [https://core.ac.uk/download/pdf/78556315.pdf](https://core.ac.uk/download/pdf/78556315.pdf)
94. [https://en.wikipedia.org/wiki/Fractional_calculus](https://en.wikipedia.org/wiki/Fractional_calculus)
95. [https://www.sciencedirect.com/bookseries/mathematics-in-science-and-engineering/vol/198/suppl/C](https://www.sciencedirect.com/bookseries/mathematics-in-science-and-engineering/vol/198/suppl/C)
96. [https://www.sciencedirect.com/topics/physics-and-astronomy/caputo-derivative](https://www.sciencedirect.com/topics/physics-and-astronomy/caputo-derivative)
97. [https://arxiv.org/abs/2006.14383](https://arxiv.org/abs/2006.14383)
98. [https://books.google.com.br/books?id=F1idlAEACAAJ](https://books.google.com.br/books?id=F1idlAEACAAJ)
99. [https://www.iaeng.org/IJAM/issues_v52/issue_3/IJAM_52_3_23.pdf](https://www.iaeng.org/IJAM/issues_v52/issue_3/IJAM_52_3_23.pdf)

---


## Page 29

100. [http://arxiv.org/pdf/2304.06855.pdf](http://arxiv.org/pdf/2304.06855.pdf)
101. [https://arxiv.org/pdf/2010.02664.pdf](https://arxiv.org/pdf/2010.02664.pdf)
102. [http://arxiv.org/pdf/1803.05018.pdf](http://arxiv.org/pdf/1803.05018.pdf)
103. [https://www.mdpi.com/2073-8994/11/6/829/pdf](https://www.mdpi.com/2073-8994/11/6/829/pdf)
104. [https://www.mdpi.com/2227-7390/8/3/360/pdf](https://www.mdpi.com/2227-7390/8/3/360/pdf)
105. [https://www.mdpi.com/2227-7390/10/19/3540/pdf?version=1665475521](https://www.mdpi.com/2227-7390/10/19/3540/pdf?version=1665475521)
106. [https://arxiv.org/abs/2501.17956](https://arxiv.org/abs/2501.17956)
107. [https://downloads.hindawi.com/journals/jfs/2022/2754507.pdf](https://downloads.hindawi.com/journals/jfs/2022/2754507.pdf)
108. [https://global-sci.com/index.php/cicp/article/view/6417](https://global-sci.com/index.php/cicp/article/view/6417)
109. [https://arxiv.org/abs/2508.20311](https://arxiv.org/abs/2508.20311)
110. [https://www.cambridge.org/core/journals/communications-in-computational-physics/article/fast-evaluation-of-the-caputo-fractional-derivative-and-its-applications-to-fractional-diffusion-equations/AF5FDC74FD7A010ED0ACD291BB1A92B1](https://www.cambridge.org/core/journals/communications-in-computational-physics/article/fast-evaluation-of-the-caputo-fractional-derivative-and-its-applications-to-fractional-diffusion-equations/AF5FDC74FD7A010ED0ACD291BB1A92B1)
111. [https://global-sci.org/index.php/cicp/article/download/6494/12923/14153](https://global-sci.org/index.php/cicp/article/download/6494/12923/14153)
112. [https://academic.oup.com/imajna/article/43/3/1263/6609534](https://academic.oup.com/imajna/article/43/3/1263/6609534)
113. [https://arxiv.org/pdf/2303.10592.pdf](https://arxiv.org/pdf/2303.10592.pdf)
114. [https://global-sci.com/article/80170/fast-evaluation-of-the-caputo-fractional-derivative-and-its-applications-to-fractional-diffusion-equations-a-second-order-scheme](https://global-sci.com/article/80170/fast-evaluation-of-the-caputo-fractional-derivative-and-its-applications-to-fractional-diffusion-equations-a-second-order-scheme)
115. [https://arxiv.org/abs/2101.08125](https://arxiv.org/abs/2101.08125)
116. [https://www.universepg.com/ajeit/numerical-solution-of-diffusion-equation-with-caputo-time-fractional-derivatives-using-finite-difference-method-with-neumann-and-robin-boundary-conditions](https://www.universepg.com/ajeit/numerical-solution-of-diffusion-equation-with-caputo-time-fractional-derivatives-using-finite-difference-method-with-neumann-and-robin-boundary-conditions)
117. [https://arxiv.org/abs/1511.03453](https://arxiv.org/abs/1511.03453)
118. [https://www.unige.ch/~hairer/preprints/fractional.pdf](https://www.unige.ch/~hairer/preprints/fractional.pdf)
119. [https://www.aimspress.com/article/doi/10.3934/math.2023481](https://www.aimspress.com/article/doi/10.3934/math.2023481)
120. [https://digitalcommons.njit.edu/fac_pubs/9707/](https://digitalcommons.njit.edu/fac_pubs/9707/)
121. [https://www.camc.shu.edu.cn/EN/10.1007/s42967-022-00233-x](https://www.camc.shu.edu.cn/EN/10.1007/s42967-022-00233-x)
122. [https://www.sciencedirect.com/science/article/abs/pii/S0168927422000538](https://www.sciencedirect.com/science/article/abs/pii/S0168927422000538)
123. [https://ojs.wisepub.com/index.php/CM/article/download/7579/3454/71413](https://ojs.wisepub.com/index.php/CM/article/download/7579/3454/71413)
124. [https://ojs.studiespublicacoes.com.br/ojs/index.php/sees/article/view/6125](https://ojs.studiespublicacoes.com.br/ojs/index.php/sees/article/view/6125)
125. [https://asmedigitalcollection.asme.org/computationalnonlinear/article/14/9/091007/726469/A-Numerical-Method-for-Caputo-Differential](https://asmedigitalcollection.asme.org/computationalnonlinear/article/14/9/091007/726469/A-Numerical-Method-for-Caputo-Differential)
126. [https://www.sciencedirect.com/science/article/pii/S0898122120302753](https://www.sciencedirect.com/science/article/pii/S0898122120302753)
127. [https://global-sci.com/pdf/article/80094/fast-evaluation-of-the-caputo-fractional-derivative-and-its-applications-to-fractional-diffusion-equations.pdf](https://global-sci.com/pdf/article/80094/fast-evaluation-of-the-caputo-fractional-derivative-and-its-applications-to-fractional-diffusion-equations.pdf)
128. [https://arxiv.org/pdf/1910.07372.pdf](https://arxiv.org/pdf/1910.07372.pdf)
129. [https://arxiv.org/pdf/2406.05705.pdf](https://arxiv.org/pdf/2406.05705.pdf)
130. [http://arxiv.org/pdf/2410.08323.pdf](http://arxiv.org/pdf/2410.08323.pdf)
131. [https://arxiv.org/pdf/1806.05167.pdf](https://arxiv.org/pdf/1806.05167.pdf)
132. [https://arxiv.org/pdf/2003.10092.pdf](https://arxiv.org/pdf/2003.10092.pdf)
133. [http://arxiv.org/pdf/2311.16340.pdf](http://arxiv.org/pdf/2311.16340.pdf)
134. [https://arxiv.org/pdf/2007.02467.pdf](https://arxiv.org/pdf/2007.02467.pdf)
135. [https://arxiv.org/pdf/2208.03817.pdf](https://arxiv.org/pdf/2208.03817.pdf)
136. [https://www.abebooks.com/9781470467692/Computational-Topology-Herbert-Edelsbrunner-John-1470467690/plp](https://www.abebooks.com/9781470467692/Computational-Topology-Herbert-Edelsbrunner-John-1470467690/plp)
137. [https://math.uchicago.edu/~may/REU2012/REUPapers/WangK.pdf](https://math.uchicago.edu/~may/REU2012/REUPapers/WangK.pdf)
138. [https://arxiv.org/abs/1806.00381](https://arxiv.org/abs/1806.00381)
139. [https://play.google.com/store/books/details/Computational_Topology_An_Introduction?id=MDXa6gFRZuIC&hl=pt_BR](https://play.google.com/store/books/details/Computational_Topology_An_Introduction?id=MDXa6gFRZuIC&hl=pt_BR)
140. [https://en.wikipedia.org/wiki/Persistent_homology](https://en.wikipedia.org/wiki/Persistent_homology)
141. [https://www2.math.upenn.edu/~ghrist/preprints/barcodes.pdf](https://www2.math.upenn.edu/~ghrist/preprints/barcodes.pdf)
142. [https://webhomes.maths.ed.ac.uk/~v1ranick/papers/edelcomp_pdf](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/edelcomp_pdf)
143. [https://www.math.uri.edu/~thoma/comp_top_2018/stag2016.pdf](https://www.math.uri.edu/~thoma/comp_top_2018/stag2016.pdf)
144. [https://www.dam.brown.edu/people/ciocanel/pres_TDA.pdf](https://www.dam.brown.edu/people/ciocanel/pres_TDA.pdf)
145. [https://enastava.matf.bg.ac.rs/~avucic/Racunarska_topologija/Herbert_Edelsbrunner,_John_L._Harer_-_Computational_Topology_An_Introduction-American_Mathematical_Society_(2009).pdf](https://enastava.matf.bg.ac.rs/~avucic/Racunarska_topologija/Herbert_Edelsbrunner,_John_L._Harer_-_Computational_Topology_An_Introduction-American_Mathematical_Society_(2009).pdf)

---


## Page 30

146. [https://pub.ista.ac.at/~edels/Papers/2012-11-PHTheoryPractice.pdf](https://pub.ista.ac.at/~edels/Papers/2012-11-PHTheoryPractice.pdf)
147. [https://en.wikipedia.org/wiki/Persistence_barcode](https://en.wikipedia.org/wiki/Persistence_barcode)
148. [https://books.google.com/books/about/Computational_Topology.html?id=MDXa6gERZulC](https://books.google.com/books/about/Computational_Topology.html?id=MDXa6gERZulC)
149. [http://www.csun.edu/~ctoth/Handbook/chap24.pdf](http://www.csun.edu/~ctoth/Handbook/chap24.pdf)
150. [https://emap.fgv.br/en/event/topological-inference-topological-data-analysis-ii-persistence-barcodes](https://emap.fgv.br/en/event/topological-inference-topological-data-analysis-ii-persistence-barcodes)
151. [https://bookstore.ams.org/view?ProductCode=MBK%2F69](https://bookstore.ams.org/view?ProductCode=MBK%2F69)
152. [https://ncatlab.org/nlab/show/persistent+homology](https://ncatlab.org/nlab/show/persistent+homology)
153. [https://www.sciencedirect.com/science/article/abs/pii/S0196885821000828](https://www.sciencedirect.com/science/article/abs/pii/S0196885821000828)
154. [https://www.semanticscholar.org/paper/Computational-Topology:-An-Introduction-Edelsbrunner-Harer/3652ed98f34b2f98779778258e9119ca6e11bb0a](https://www.semanticscholar.org/paper/Computational-Topology:-An-Introduction-Edelsbrunner-Harer/3652ed98f34b2f98779778258e9119ca6e11bb0a)
155. [https://webhomes.maths.ed.ac.uk/~v1ranick/papers/edelhare.pdf](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/edelhare.pdf)
156. [https://arxiv.org/pdf/1601.05533.pdf](https://arxiv.org/pdf/1601.05533.pdf)
157. [http://arxiv.org/pdf/1207.6736.pdf](http://arxiv.org/pdf/1207.6736.pdf)
158. [https://arxiv.org/pdf/1911.01876.pdf](https://arxiv.org/pdf/1911.01876.pdf)
159. [https://arxiv.org/pdf/1808.08271.pdf](https://arxiv.org/pdf/1808.08271.pdf)
160. [http://arxiv.org/pdf/1209.1988.pdf](http://arxiv.org/pdf/1209.1988.pdf)
161. [https://www.mdpi.com/1099-4300/19/10/524/pdf?version=1506826626](https://www.mdpi.com/1099-4300/19/10/524/pdf?version=1506826626)
162. [https://arxiv.org/pdf/2310.03884.pdf](https://arxiv.org/pdf/2310.03884.pdf)
163. [https://www.mdpi.com/1099-4300/16/5/2454/pdf?version=1424785411](https://www.mdpi.com/1099-4300/16/5/2454/pdf?version=1424785411)
164. [https://www.scribd.com/document/322985499/Amari-Nagaoka-Methods-of-Information-Geometry](https://www.scribd.com/document/322985499/Amari-Nagaoka-Methods-of-Information-Geometry)
165. [https://noneq.c.u-tokyo.ac.jp/Stochastic_Thermodynamics_III/wp-content/uploads/2022/06/WOST-III_tutorial_oizumi.pdf](https://noneq.c.u-tokyo.ac.jp/Stochastic_Thermodynamics_III/wp-content/uploads/2022/06/WOST-III_tutorial_oizumi.pdf)
166. [https://periodicos.uem.br/ojs/index.php/BSocParanMat/article/download/71410/751375160336/](https://periodicos.uem.br/ojs/index.php/BSocParanMat/article/download/71410/751375160336/)
167. [https://www.abebooks.com/9780821843024/Methods-Information-Geometry-Translations-Mathematical-0821843028/plp](https://www.abebooks.com/9780821843024/Methods-Information-Geometry-Translations-Mathematical-0821843028/plp)
168. [https://franknielsen.github.io/IG/index.html](https://franknielsen.github.io/IG/index.html)
169. [https://arxiv.org/abs/2405.06799](https://arxiv.org/abs/2405.06799)
170. [https://bookstore.ams.org/mmono-191](https://bookstore.ams.org/mmono-191)