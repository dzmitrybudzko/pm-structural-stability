# Theorem: Structural Stability of the PM Iterative Scheme (Scalar Case)

## Goal

Prove that for the one-parameter family of iterative methods PM (Budzko-Cordero-Torregrosa, 2015), there exists a neighborhood of α = 0 in which the iteration operator generates structurally stable dynamics — i.e., basins of attraction have smooth (non-fractal) boundaries (Jordan curve Julia set).

---

## 1. The PM Scheme (from Budzko et al. 2015)

### 1.1 Definition

For solving f(x) = 0, the PM family is a two-step predictor-corrector:

**Step 1 (predictor):**
$$y_k = x_k - \alpha \frac{f(x_k)}{f'(x_k)}$$

**Step 2 (corrector):**
$$x_{k+1} = y_k - \frac{f(x_k)^2}{b \cdot f(x_k)^2 + c \cdot f(y_k)^2} \cdot \frac{f(y_k)}{f'(x_k)}$$

where the third-order convergence is achieved when:
$$b = \frac{1 + \alpha^2}{2\alpha^2}, \quad c = \frac{1 + \alpha}{2\alpha^2(\alpha - 1)}$$

with α ∉ {0, 1}.

### 1.2 Error equation (Theorem 1 from the paper)

$$e_{k+1} = \left(\frac{1}{2}(2 - 2\alpha + \alpha^2 + \alpha^3) c_2^2 + 2(1-\alpha)c_3\right) e_k^3 + O(e_k^4)$$

where $c_k = \frac{1}{k!} \frac{f^{(k)}(\xi)}{f'(\xi)}$.

**Key observation:** the coefficient of $e_k^3$ depends on α. At small |α|, the factor $(2 - 2\alpha + \alpha^2 + \alpha^3)$ is minimized, which correlates with the empirically observed stability improvement.

### 1.3 Connection to Ermakov-Kalitkin damping

The PM scheme generalizes the Ermakov-Kalitkin damped Newton method (1981):

$$x_{k+1} = x_k - \beta_k [f'(x_k)]^{-1} f(x_k)$$

where:
$$\beta_k = \frac{\|f(x_k)\|^2}{\|f(x_k)\|^2 + \|f(x_k) - [f'(x_k)]^{-1}f(x_k)\|^2}$$

This $\beta_k$ automatically reduces the step when the iterate is far from the root (poor initial approximation), and approaches 1 near the root (recovering Newton's quadratic convergence locally).

### 1.4 Special cases

- α = 1, b = 1: reduces to classical Newton (dropped due to singular denominators)
- α → 0: empirically produces widest basins with smoothest boundaries
- The family is defined for all α ∉ {0, 1}

---

## 2. Background: Holomorphic Dynamics and Julia Sets

### 2.1 Setup

Given an iterative method applied to a polynomial f, the iteration defines a rational map $R: \hat{\mathbb{C}} \to \hat{\mathbb{C}}$ on the Riemann sphere $\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$.

For Newton's method applied to $f(z) = z^n - 1$:
$$N_f(z) = z - \frac{f(z)}{f'(z)} = z - \frac{z^n - 1}{nz^{n-1}} = \frac{(n-1)z^n + 1}{nz^{n-1}}$$

This is a rational map of degree n.

### 2.2 Key definitions

**Fixed point:** $z^*$ is a fixed point of R if $R(z^*) = z^*$.

**Classification by multiplier λ = R'(z*):**
- |λ| < 1: attracting (|λ| = 0: superattracting)
- |λ| > 1: repelling
- |λ| = 1: neutral (parabolic if λ is a root of unity, irrationally neutral otherwise)

**Basin of attraction:** $\mathcal{A}(z^*) = \{z_0 \in \hat{\mathbb{C}} : R^n(z_0) \to z^*, n \to \infty\}$

**Fatou set F(R):** union of all basins of attraction (where dynamics is "stable").

**Julia set J(R):** $J(R) = \hat{\mathbb{C}} \setminus F(R)$ — boundary between basins, where dynamics is chaotic.

### 2.3 Properties of Julia sets

- J(R) is always closed and non-empty
- J(R) is the closure of the set of repelling periodic points
- J(R) is completely invariant: $R^{-1}(J) = J = R(J)$
- If R has degree d, then J(R) is either:
  - (a) a smooth Jordan curve, or
  - (b) a fractal set with Hausdorff dimension > 1, or
  - (c) the entire Riemann sphere $\hat{\mathbb{C}}$

### 2.4 Structural stability (J-stability)

A rational map $R_\lambda$ (depending on parameter λ) is **J-stable** at $\lambda_0$ if:
- The Julia set $J(R_\lambda)$ moves continuously (in the Hausdorff metric) as λ varies near $\lambda_0$
- The topological dynamics on $J(R_\lambda)$ is conjugate to that on $J(R_{\lambda_0})$ for nearby λ

**Mañé-Sad-Sullivan theorem (1983):** J-stability is equivalent to:
1. All periodic points of R_λ move holomorphically
2. No critical point of R_λ lies on J(R_λ)
3. The Julia set does not contain a parabolic periodic point

**Equivalent formulation:** $R_\lambda$ is J-stable at $\lambda_0$ if and only if no critical orbit of $R_\lambda$ "collides" with the Julia set as λ passes through $\lambda_0$.

This is a key theorem. It reduces J-stability to tracking critical orbits.

### 2.5 Smooth vs fractal Julia sets — known results

**For Newton's method on $z^n - 1$:**
- Roots of f are superattracting fixed points of $N_f$
- ∞ is a repelling fixed point
- J(N_f) is connected and has Hausdorff dimension > 1 for n ≥ 3
- For n = 2: J is a straight line (smooth boundary)
- For n ≥ 3: J is a fractal

**Theorem (Shishikura, 1990):** For Newton's method on any polynomial of degree n ≥ 3, the Julia set has Hausdorff dimension 2 (maximal fractality).

This means Newton's method is inherently structurally unstable for polynomials of degree ≥ 3.

---

## 3. PM as a Rational Map

### 3.1 Construction

For a polynomial f of degree n, the PM operator $R_\alpha(z)$ is obtained by substituting f into the PM scheme:

$$R_\alpha(z) = y(z) - \frac{f(z)^2}{b \cdot f(z)^2 + c \cdot f(y(z))^2} \cdot \frac{f(y(z))}{f'(z)}$$

where $y(z) = z - \alpha \frac{f(z)}{f'(z)}$ and $b = \frac{1+\alpha^2}{2\alpha^2}$, $c = \frac{1+\alpha}{2\alpha^2(\alpha-1)}$.

$R_\alpha$ is a rational map on $\hat{\mathbb{C}}$. Its degree depends on n and the specific form of f.

### 3.2 Fixed points

- The roots of f are superattracting fixed points of $R_\alpha$ (since PM has order 3, multiplier = 0)
- ∞ may be a fixed point (depends on degree of f)
- There may be extraneous fixed points (not roots of f)

### 3.3 Critical points

The critical points of $R_\alpha$ are solutions of $R_\alpha'(z) = 0$.

For Newton's method on $z^3 - 1$, there is one free critical point (after accounting for symmetry). For PM, the number and location of critical points depend on α.

**This is the key quantity to track:** by the Mañé-Sad-Sullivan theorem, J-stability depends on whether critical orbits hit the Julia set.

---

## 4. Statement of the Theorem to Prove

### 4.1 Precise formulation (proposed)

**Theorem.** Let $f(z) = z^n - 1$ with $n \geq 3$, and let $R_\alpha$ be the PM operator defined by scheme (4) with $b(\alpha), c(\alpha)$ as in Theorem 1 of Budzko et al. (2015). Then:

(a) For α = 1 (Newton's method), the Julia set $J(R_1)$ is a fractal with Hausdorff dimension > 1.

(b) There exists $\alpha^* > 0$ such that for all $\alpha \in (-\alpha^*, 0) \cup (0, \alpha^*)$, the Julia set $J(R_\alpha)$ is a Jordan curve (smooth boundary between basins).

(c) The transition from fractal to smooth boundary is associated with all free critical orbits of $R_\alpha$ converging to attracting fixed points (roots of f) for small |α|.

### 4.2 Weaker version (more realistic first step)

**Theorem (weak).** For $f(z) = z^3 - 1$ and the PM operator $R_\alpha$:

(a) At α = 1, $R_\alpha$ has a free critical point whose orbit does not converge to any root, and $J(R_1)$ is fractal.

(b) There exists $\alpha_0 \neq 1$ such that all critical orbits of $R_{\alpha_0}$ converge to roots of f, and consequently $R_{\alpha_0}$ is J-stable and $J(R_{\alpha_0})$ is connected with dimension 1 (smooth boundary).

### 4.3 Alternative: basin entropy decay theorem

**Theorem (quantitative).** Let $S_b(\alpha, \varepsilon)$ denote the basin entropy of $R_\alpha$ at scale $\varepsilon$, and $\alpha_{ue}(\alpha)$ the uncertainty exponent. Then:

(a) $\alpha_{ue}(1) < 1$ (fractal boundary for Newton)

(b) $\lim_{\alpha \to 0} \alpha_{ue}(\alpha) = 1$ (smooth boundary in PM limit)

(c) $S_b(\alpha, \varepsilon) < S_b(1, \varepsilon)$ for all sufficiently small |α| and all ε > 0.

This is provable numerically with mathematical rigor (interval arithmetic).

---

## 5. Proof Strategy

### 5.1 Strategy A: Critical orbit tracking (via Mañé-Sad-Sullivan)

**Step 1.** Compute $R_\alpha(z)$ explicitly for $f(z) = z^3 - 1$.

The Newton operator is:
$$N(z) = \frac{2z^3 + 1}{3z^2}$$

The PM predictor:
$$y(z) = z - \alpha \frac{z^3 - 1}{3z^2}$$

The full PM operator $R_\alpha(z)$ is a rational function of z (with α as parameter).

**Step 2.** Find all critical points of $R_\alpha$: solve $R_\alpha'(z) = 0$.

For Newton on $z^3 - 1$: critical points are the three roots (superattracting, hence trivial) plus z = 0 (the "free" critical point). The orbit of z = 0 under Newton does not converge to any root — it is attracted to a repelling cycle, contributing to fractality.

For PM: the critical points will depend on α. Track them as functions of α.

**Step 3.** Show that for small |α|, all free critical orbits converge to roots.

If this is true, by Mañé-Sad-Sullivan, $R_\alpha$ is J-stable and the Julia set cannot be fractal (no critical point on J).

**Step 4.** Apply the Fatou theorem: if all critical points are attracted to attracting cycles, then the Fatou set is the union of the basins of these cycles, and J is a thin set (dimension < 2).

To show J is a Jordan curve specifically, one additionally needs that each basin is simply connected and the basins tile the sphere — this follows from the Riemann-Hurwitz formula if the degree of $R_\alpha$ and the number of attracting fixed points satisfy the right relation.

### 5.2 Strategy B: Perturbation from identity

**Observation:** as α → 0, the predictor $y_k = x_k - \alpha \frac{f(x_k)}{f'(x_k)}$ approaches $y_k = x_k$ (identity). The corrector step then also approaches a near-identity map.

If we can show that $R_\alpha \to \text{Id}$ in some sense as α → 0, then for small α the dynamics is a small perturbation of the identity, which has trivial dynamics (no Julia set). By structural stability of trivial dynamics, sufficiently small perturbations also have trivial dynamics.

**Problem:** $R_\alpha$ is not defined at α = 0 (division by α² in b and c). Need to analyze the limit carefully — the limit $R_0$ may exist after cancellation.

### 5.3 Strategy C: Parameter space analysis

Study the parameter space of the family $\{R_\alpha\}$ and identify the **bifurcation set** — values of α where the dynamics changes qualitatively.

In the parameter plane, J-stability holds on an open dense set (Mañé-Sad-Sullivan). The bifurcation set consists of isolated points (or curves in higher dimensions). If we can show that α = 1 (Newton) is in the bifurcation set and small α is in the J-stable component, we're done.

**Concrete approach:** plot the orbit of each free critical point as a function of α. At bifurcation values, a critical orbit hits J. Between bifurcations, the dynamics is stable.

---

## 6. Concrete Computations Needed

### 6.1 For $f(z) = z^3 - 1$

1. **Compute $R_\alpha(z)$ explicitly.** Substitute $f(z) = z^3 - 1$, $f'(z) = 3z^2$ into PM scheme. Simplify the rational function. Determine its degree.

2. **Find critical points.** Differentiate $R_\alpha(z)$ with respect to z, solve $R_\alpha'(z) = 0$. Separate trivial critical points (roots of f) from free critical points.

3. **Track free critical orbits.** For each free critical point $c(\alpha)$, compute the orbit $\{R_\alpha^n(c(\alpha))\}_{n=0}^{\infty}$ as a function of α. Determine for which α the orbit converges to a root.

4. **Identify bifurcation values.** Values of α where a free critical orbit changes its asymptotic behavior (e.g., from converging to root 1 to converging to root ω).

5. **Compute Hausdorff dimension of $J(R_\alpha)$.** Numerically for several values of α, to support the theorem.

### 6.2 For general $f(z) = z^n - 1$

Same program but more complex. Start with n = 3 as the simplest nontrivial case.

### 6.3 Computer algebra

Much of this can be done in Mathematica or SymPy:
- Symbolic computation of $R_\alpha(z)$ and $R_\alpha'(z)$
- Numerical root finding for critical points
- Orbit computation with arbitrary precision arithmetic (as in the 2015 paper)

---

## 7. Known Results to Build On

### 7.1 Newton's method dynamics (well-studied)

- **Blanchard (1994)** "The dynamics of Newton's method" — comprehensive treatment for polynomials. Julia set structure, classification of critical orbits.
- **Devaney (1999)** — Mandelbrot set connections, Farey tree structure.
- **Shishikura (1990)** — Hausdorff dimension of Julia sets for Newton's method.
- **Hubbard, Schleicher, Sutherland (2001)** "How to find all roots of complex polynomials by Newton's method" — Inventiones Mathematicae. Proved that Newton's method can be made to converge for almost all starting points with appropriate modifications.

### 7.2 Damped Newton dynamics (less studied)

- **Buff and Henriksen (2003)** — studied perturbations of Newton's method and their effect on Julia sets.
- **Honorato, Plaza, Romero (2013)** — dynamics of damped Newton's method $z - \lambda \frac{f(z)}{f'(z)}$ for polynomials. Showed that for some λ values, Julia set simplifies. This is directly relevant — their damping parameter λ plays a role similar to your α.

### 7.3 Families of iterative methods

- **Cordero, Torregrosa et al. (2013)** "Drawing dynamical and parameters planes of iterative families and methods" — the software you used in the 2015 paper.
- **Campos, Cordero, Torregrosa et al.** — multiple papers on dynamical study of iterative families, including basins of attraction analysis.

### 7.4 Basin entropy

- **Daza et al. (2016)** — basin entropy definition, sufficient condition for fractality ($S_b > \log 2$).
- **Daza et al. (2022)** — classification of basins using basin entropy, uncertainty exponent.

---

## 8. Key Mathematical Questions

### Q1: What is the degree of $R_\alpha$ for $f(z) = z^3 - 1$?
Newton has degree 3. PM involves composition and division — degree will be higher. The degree determines the maximum number of critical points (2d - 2 by Riemann-Hurwitz).

### Q2: How many free critical points does $R_\alpha$ have?
Newton on $z^3 - 1$ has 1 free critical point (z = 0, by symmetry). PM will have more. Need to classify them.

### Q3: Does $\lim_{\alpha \to 0} R_\alpha(z)$ exist?
The coefficients $b(\alpha) = \frac{1+\alpha^2}{2\alpha^2}$ and $c(\alpha) = \frac{1+\alpha}{2\alpha^2(\alpha-1)}$ blow up as α → 0. But the full expression may have a well-defined limit after cancellation. This is crucial for Strategy B.

### Q4: Is there a connection between the error equation coefficient $(2 - 2\alpha + \alpha^2 + \alpha^3)$ and the Hausdorff dimension of J?
The error equation governs local convergence rate. The Julia set structure is a global property. But there may be a connection through the multiplier of fixed points — if PM has smaller asymptotic error, the fixed points are "more superattracting" which pulls critical orbits in more strongly.

### Q5: Does the Z₃ symmetry of $z^3 - 1$ simplify the analysis?
Yes. The PM operator inherits the Z₃ symmetry: $R_\alpha(\omega z) = \omega R_\alpha(z)$ where $\omega = e^{2\pi i/3}$. This reduces the number of independent critical orbits to track.

---

## 9. Potential Obstacles

### O1: High degree of $R_\alpha$
If $R_\alpha$ has degree >> 3, there may be many free critical points. Tracking all of them is hard. Symmetry helps but may not be sufficient.

### O2: The limit α → 0 may be singular
If $R_\alpha$ does not have a well-defined limit, Strategy B fails. Need to work with small but nonzero α.

### O3: Extraneous attracting cycles
PM might create attracting cycles that are not roots of f — "parasitic" solutions. These would complicate the basin structure. Need to verify they don't exist for small |α|.

### O4: The theorem may be false
It's possible that PM boundaries are smoother but still fractal (Hausdorff dimension between 1 and 2). In this case, the theorem should be reformulated quantitatively: Hausdorff dimension of $J(R_\alpha)$ is a decreasing function of |α| near α = 0.

---

## 10. Suggested Order of Work

1. **Explicit computation of $R_\alpha(z)$ for $f(z) = z^3 - 1$.** Symbolic computation, simplification, determine degree.

2. **Find critical points of $R_\alpha$.** Symbolic + numerical. Classify into trivial and free.

3. **Numerical experiment:** for α ∈ {-0.45, -0.1, -0.01, 0.01, 0.1, 0.45, 1.0}, compute free critical orbits and Julia set (or basin boundaries). Confirm the empirical observation from the 2015 paper in this specific setting.

4. **Analyze the limit α → 0.** Is there a removable singularity? What is the limiting map?

5. **Apply Mañé-Sad-Sullivan:** verify the criterion for J-stability at specific α values.

6. **Formulate and prove the theorem** (or a weaker version if obstacles arise).

---

## 11. What Would Be the Impact

### If proved for $z^3 - 1$ (weak version):
A clean result showing that a specific modification of Newton's method transitions from fractal to smooth basin boundaries. Publishable in a dynamics journal (Nonlinearity, Journal of Difference Equations and Applications, or Chaos).

### If proved for $z^n - 1$ general n:
A significant result in holomorphic dynamics. Could go to Communications in Mathematical Physics or Inventiones Mathematicae.

### If connected to PINN training:
The theoretical backbone for the empirical results in Articles 1 and 2. Elevates the entire project from applied ML to mathematical ML with rigorous foundations.

### Combined impact:
Three papers forming a coherent program: empirical diagnostic tool (Article 1), practical optimizer (Article 2), mathematical foundation (Article 3). This is a research agenda, not just a project.
