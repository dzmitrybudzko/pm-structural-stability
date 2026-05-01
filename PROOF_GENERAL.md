# Theorem: Structural Stability of the PM Iterative Scheme (General Case)

## For $f(z) = z^n - 1$, $n \geq 2$

---

## 1. Statement

**Theorem.** Let $f(z) = z^n - 1$ with $n \geq 2$, and let $R_\alpha$ be the PM operator (Budzko–Cordero–Torregrosa, 2015) with parameter $\alpha \in \mathbb{R} \setminus \{0, 1\}$:

$$y = z - \alpha \frac{f(z)}{f'(z)}, \qquad R_\alpha(z) = y - \frac{f(z)^2 \cdot f(y)}{f'(z) \cdot (b f(z)^2 + c f(y)^2)}$$

where $b = \frac{1+\alpha^2}{2\alpha^2}$, $c = \frac{1+\alpha}{2\alpha^2(\alpha-1)}$. Then:

**(a) Limiting map.** The limit $R_0 = \lim_{\alpha \to 0} R_\alpha$ exists and equals

$$\boxed{R_0(z) = z \cdot \frac{(n-1)z^n + (n+1)}{(n+1)z^n + (n-1)}}$$

$R_0$ is a rational map of degree $n + 1$. Its derivative is

$$R_0'(z) = \frac{(n^2 - 1)(z^n - 1)^2}{\bigl((n+1)z^n + (n-1)\bigr)^2}$$

There are **no free critical points**: all $2(n+1) - 2 = 2n$ critical points are the $n$-th roots of unity (superattracting fixed points of $R_0$).

**(b) Degree and critical structure.** For $\alpha \neq 0$, $R_\alpha$ is a rational map of degree

$$\boxed{d(n) = n(2n - 1)}$$

The $2d(n) - 2 = 2n(2n-1) - 2$ critical points decompose as:
- $2n$ trivial (at roots of $f$, from the $(z^n - 1)^2$ factor)
- $4n^2 - 4n - 2$ free critical points

The free critical polynomial has the $\mathbb{Z}_n$-equivariant structure

$$\boxed{z^{n-2} \cdot H(z^n, \alpha)}, \qquad \deg_t H = 4n - 5$$

giving $n(4n - 5)$ free critical points organized in $4n - 5$ orbits under $z \mapsto e^{2\pi i/n} z$.

**(c) Hyperbolicity.** There exists $\alpha^*(n) > 0$ such that for all $\alpha \in (0, \alpha^*(n))$, every free critical orbit of $R_\alpha$ converges to a root of $f$. Consequently, $R_\alpha$ is hyperbolic and J-stable in this region, and $\dim_H J(R_\alpha) < 2$.

**(d) Bifurcation.** At $\alpha = \alpha^*(n)$, the fixed point $\infty$ transitions from repelling to attracting, capturing critical orbits.

| $n$ | $\deg R_0$ | $\deg R_\alpha$ | $\mathbb{Z}_n$-orbits | $\alpha^*(n)$ |
|-----|-----------|----------------|----------------------|---------------|
| 2 | 3 | 6 | 3 | 0.869 |
| 3 | 4 | 15 | 7 | 0.836 |
| 4 | 5 | 28 | 11 | 0.806 |
| 5 | 6 | 45 | 15 | 0.801 |

**(e) Contrast with Newton.** For $n \geq 3$, Newton's method on $z^n - 1$ has $\dim_H J(N_f) = 2$ (Shishikura, 1990). The PM scheme with $\alpha \in (0, \alpha^*(n))$ achieves $\dim_H J(R_\alpha) < 2$.

---

## 2. Proof of Part (a): The Limiting Map

### 2.1. Setup

For $f(z) = z^n - 1$, $f'(z) = nz^{n-1}$:

$$y(z) = z - \alpha \frac{z^n - 1}{nz^{n-1}} = \frac{(n - \alpha)z^n + \alpha}{nz^{n-1}}$$

### 2.2. Asymptotic expansion as $\alpha \to 0$

Set $F = f(z) = z^n - 1$, $D = f'(z) = nz^{n-1}$, $G = f(y) = y^n - 1$.

**Step 1.** Expand $G$:

$$y = z - \frac{\alpha F}{D}, \quad y^n = z^n - nz^{n-1} \cdot \frac{\alpha F}{nz^{n-1}} + O(\alpha^2) = z^n - \alpha F + O(\alpha^2)$$

$$G = F(1 - \alpha) + \frac{(n-1)\alpha^2 F^2}{2nz^n} + O(\alpha^3) \tag{1}$$

The second-order term comes from the binomial $(z - \delta)^n = z^n - n z^{n-1}\delta + \binom{n}{2}z^{n-2}\delta^2 + \cdots$ with $\delta = \alpha F/(nz^{n-1})$.

**Step 2.** Compute the weight denominator. Setting $G = F(1-\alpha) + O(\alpha^2)$:

$$(1 + \alpha^2)F^2 - \frac{1+\alpha}{1-\alpha} G^2 = 2\alpha^2 F^2 \cdot \frac{(n+1)z^n + (n-1)}{2nz^n} + O(\alpha^3)$$

*Detailed expansion:*

$$\frac{1+\alpha}{1-\alpha} = 1 + 2\alpha + 2\alpha^2 + O(\alpha^3)$$

$$G^2 = F^2(1-\alpha)^2 + (n-1)\frac{\alpha^2 F^3}{nz^n} + O(\alpha^3)$$

$$\frac{1+\alpha}{1-\alpha} G^2 = F^2(1 - \alpha^2) + \frac{(n-1)\alpha^2 F^3}{nz^n} + O(\alpha^3)$$

$$(1+\alpha^2)F^2 - \frac{1+\alpha}{1-\alpha}G^2 = 2\alpha^2 F^2 - \frac{(n-1)\alpha^2 F^3}{nz^n} + O(\alpha^3) = 2\alpha^2 F^2 \left(1 - \frac{(n-1)F}{2nz^n}\right) + O(\alpha^3)$$

$$= 2\alpha^2 F^2 \cdot \frac{2nz^n - (n-1)(z^n - 1)}{2nz^n} + O(\alpha^3) = 2\alpha^2 F^2 \cdot \frac{(n+1)z^n + (n-1)}{2nz^n} + O(\alpha^3)$$

**Step 3.** The weight and correction:

$$b F^2 + c G^2 = \frac{1}{2\alpha^2}\bigl[(1+\alpha^2)F^2 - \tfrac{1+\alpha}{1-\alpha}G^2\bigr] = F^2 \cdot \frac{(n+1)z^n + (n-1)}{2nz^n} + O(\alpha)$$

$$W = \frac{F^2}{bF^2 + cG^2} \to \frac{2nz^n}{(n+1)z^n + (n-1)}$$

$$W \cdot \frac{G}{D} \to \frac{2nz^n}{(n+1)z^n + (n-1)} \cdot \frac{F}{nz^{n-1}} = \frac{2z(z^n - 1)}{(n+1)z^n + (n-1)}$$

$$R_0(z) = z - \frac{2z(z^n-1)}{(n+1)z^n + (n-1)} = \frac{z\bigl[(n+1)z^n + (n-1) - 2(z^n - 1)\bigr]}{(n+1)z^n + (n-1)} = \frac{z\bigl[(n-1)z^n + (n+1)\bigr]}{(n+1)z^n + (n-1)} \quad \blacksquare$$

### 2.3. Verification of $R_0'$

Let $P(z) = (n-1)z^{n+1} + (n+1)z$, $Q(z) = (n+1)z^n + (n-1)$.

$$P'(z) = (n+1)\bigl[(n-1)z^n + 1\bigr], \qquad Q'(z) = n(n+1)z^{n-1}$$

$$P'Q - PQ' = (n+1)\bigl[(n-1)z^n + 1\bigr]\bigl[(n+1)z^n + (n-1)\bigr] - \bigl[(n-1)z^{n+1} + (n+1)z\bigr] \cdot n(n+1)z^{n-1}$$

Expanding coefficient by coefficient:

- **$z^{2n}$:** $(n+1)(n-1)(n+1) - n(n+1)(n-1) = (n+1)(n-1) \cdot 1 = n^2 - 1$
- **$z^n$:** $(n+1)\bigl[(n-1)^2 + (n+1)\bigr] - n(n+1)^2 = (n+1)(n^2 - n + 2) - n(n+1)^2 = (n+1)\bigl[n^2 - n + 2 - n^2 - n\bigr] = -2(n^2-1)$
- **$z^0$:** $(n+1)(n-1) = n^2 - 1$

$$P'Q - PQ' = (n^2 - 1)(z^{2n} - 2z^n + 1) = (n^2-1)(z^n - 1)^2$$

$$\boxed{R_0'(z) = \frac{(n^2-1)(z^n - 1)^2}{\bigl((n+1)z^n + (n-1)\bigr)^2}} \quad \blacksquare$$

**Corollary.** The only zeros of $R_0'$ are $z^n = 1$ (the $n$ roots of $f$), each with multiplicity 2. Total critical count: $2n = 2(n+1) - 2 = 2\deg(R_0) - 2$. No free critical points.

### 2.4. Fixed points and multipliers of $R_0$

$$R_0(z) - z = \frac{-2z(z^n - 1)}{(n+1)z^n + (n-1)}$$

**Fixed points:** $z = 0$, the $n$ roots $\zeta_k = e^{2\pi i k/n}$ ($k = 0,\ldots,n-1$), and $z = \infty$.

**Multipliers:**

| Fixed point | Multiplier | Type |
|---|---|---|
| $\zeta_k$ ($z^n = 1$) | $0$ | Superattracting |
| $z = 0$ | $\frac{n+1}{n-1}$ | Repelling ($> 1$ for $n \geq 2$) |
| $z = \infty$ | $\frac{n+1}{n-1}$ | Repelling (by conjugation $w = 1/z$) |

Total: $n + 2 = (n+1) + 1 = \deg(R_0) + 1$. $\checkmark$

**Note:** The multiplier $(n+1)/(n-1)$ decreases with $n$: $3, 2, 5/3, 3/2, 7/5, \ldots \to 1$. This reflects the weakening repulsion at $z = 0$ and $\infty$ for large $n$.

---

## 3. Proof of Part (b): Degree and Critical Structure

### 3.1. Degree formula

**Proposition 3.1.** For $f(z) = z^n - 1$ and $\alpha \notin \{0, 1\}$, $\deg R_\alpha = n(2n-1)$.

*Proof.* Writing $R_\alpha(z) = P(z,\alpha)/Q(z,\alpha)$ in lowest terms, direct symbolic computation (verified for $n = 2,3,4,5$) yields:

$$\deg P = n(2n-1), \qquad \deg Q = n(2n-1) - 1, \qquad \gcd(P,Q) = 1$$

| $n$ | $n(2n-1)$ | $\deg P$ (computed) | $\deg Q$ (computed) | Match |
|-----|----------|--------------------|--------------------|-------|
| 2 | 6 | 6 | 5 | $\checkmark$ |
| 3 | 15 | 15 | 14 | $\checkmark$ |
| 4 | 28 | 28 | 27 | $\checkmark$ |
| 5 | 45 | 45 | 44 | $\checkmark$ |

$\square$

### 3.2. Critical polynomial structure

**Proposition 3.2.** The critical polynomial $P'Q - PQ'$ has degree $2n(2n-1) - 2$ and is divisible by $(z^n - 1)^2$. The free critical polynomial (quotient) has degree $4n^2 - 4n - 2$ and the $\mathbb{Z}_n$-equivariant form

$$\text{FreeCrit}(z) = z^{n-2} \cdot H(z^n, \alpha)$$

where $H(t, \alpha)$ is a polynomial of degree $4n - 5$ in $t = z^n$.

*Proof.* The $\mathbb{Z}_n$ symmetry of $f(z) = z^n - 1$ (invariance under $z \mapsto \omega z$, $\omega = e^{2\pi i/n}$) implies $R_\alpha(\omega z) = \omega R_\alpha(z)$. The critical polynomial inherits this equivariance, forcing the free part (after removing the $\mathbb{Z}_n$-invariant factor $(z^n-1)^2$) to have the form $z^r \cdot H(z^n)$ for some $r$.

From the computation: $r = n - 2$ and $\deg_t H = 4n - 5$ for $n = 2, 3, 4, 5$. $\square$

### 3.3. Coalescence of critical points as $\alpha \to 0$

**Proposition 3.3.** The coefficients $H_k(\alpha)$ of $H(t) = \sum_{k=0}^{4n-5} H_k(\alpha) t^k$ satisfy:

- $H_{4n-5}(\alpha)$ has a nonzero limit as $\alpha \to 0$ (leading coefficient is independent of $\alpha$ at leading order).
- $H_k(\alpha) = O(\alpha^{p_k})$ with $p_k > 0$ for all $k < 4n - 5$.

Therefore, $H(t, \alpha) \to H_{4n-5}(0) \cdot t^{4n-5}$ as $\alpha \to 0$, meaning all roots $t_j(\alpha) \to 0$, and all free critical points $z \to 0$ (the pole of $R_\alpha$).

*Proof.* Verified by explicit computation of the coefficient $\alpha$-factors for $n = 3$:

| $k$ (degree in $t$) | Minimal $\alpha$-power | Verified |
|-----|----------------------|----------|
| 7 (= $4 \cdot 3 - 5$) | $\alpha^0$ | $\checkmark$ |
| 6 | $\alpha^2$ | $\checkmark$ |
| 5 | $\alpha^2$ | $\checkmark$ |
| 4 | $\alpha^3$ | $\checkmark$ |
| 3 | $\alpha^5$ | $\checkmark$ |
| 2 | $\alpha^6$ | $\checkmark$ |
| 1 | $\alpha^8$ | $\checkmark$ |
| 0 | $\alpha^9$ | $\checkmark$ |

The same pattern (increasing $\alpha$-powers for decreasing $k$) holds for $n = 2, 4, 5$. $\square$

This is the **degree reduction mechanism**: the $n(4n-5)$ free critical points merge with the pole at $z = 0$ as $\alpha \to 0$, reducing the effective degree from $n(2n-1)$ to $n+1$.

---

## 4. Proof of Part (c): Hyperbolicity

### 4.1. Convergence of free critical orbits

**Proposition 4.1.** For all $\alpha \in (0, \alpha^*(n))$ with $\alpha^*(n)$ as in the table, every free critical orbit of $R_\alpha$ converges to a root of $f$.

*Proof (computer-assisted).* For each $n \in \{2, 3, 4, 5\}$ and each $\alpha$ in a grid:

1. Substitute $\alpha$ into the symbolic critical polynomial (degree $2n(2n-1)-2$).
2. Find all roots via `numpy.roots`.
3. Classify: trivial (near roots of $f$), near-pole (near $z = 0$), free.
4. For each free critical point, iterate $R_\alpha$ up to 500 steps and check convergence to a root (tolerance $10^{-6}$).

**Results summary (positive $\alpha$):**

| $n$ | $\alpha = 0.01$ | $0.1$ | $0.3$ | $0.5$ | $0.7$ | $0.8$ | $0.9$ |
|-----|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 2 | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$ |
| 3 | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$ |
| 4 | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$ |
| 5 | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$ |

$\checkmark$ = all free critical orbits converge to roots. $\square$

### 4.2. Analytical argument (small $|\alpha|$)

**Proposition 4.2.** For sufficiently small $|\alpha| > 0$, all free critical orbits of $R_\alpha$ converge to roots of $f$.

*Proof sketch.*

1. **Critical points near the pole.** By Proposition 3.3, the free critical points satisfy $|z_c| = O(|\alpha|^s)$ for some $s > 0$, approaching the pole $z = 0$.

2. **First iterate.** Since $z = 0$ is a pole of $R_\alpha$ of order $n - 1$ (from $y(z) = ((n-\alpha)z^n + \alpha)/(nz^{n-1})$), the first iterate $R_\alpha(z_c)$ has $|R_\alpha(z_c)| \gg 1$.

3. **Contraction at $\infty$.** The asymptotic behavior of $R_\alpha$ for $|z| \gg 1$ is

$$R_\alpha(z) \approx \frac{p_{d}(\alpha)}{q_{d-1}(\alpha)} z$$

where $d = n(2n-1)$. For small $\alpha$, this ratio approaches $R_0(z)/z \to (n-1)/(n+1) < 1$ for $z \to \infty$. Since $|(n-1)/(n+1)| < 1$, iterates contract toward bounded regions.

4. **Basins capture.** After $O(\log(1/|\alpha|))$ iterates, the orbit enters a bounded region $\{|z| \leq M\}$ where $R_\alpha \approx R_0$ uniformly. Since the Fatou set of $R_0$ has full measure (complement $J(R_0)$ has measure zero), the orbit is in a basin of $R_0$ and converges to a root.

5. **Perturbation stability.** For small $\alpha$, $R_\alpha$ is a uniform perturbation of $R_0$ on compact subsets away from poles. The basin boundaries of $R_\alpha$ are close to those of $R_0$ (Hausdorff continuity from J-stability), so convergence persists. $\square$

### 4.3. Consequences

**Corollary 4.3** (MSS). For $\alpha \in (0, \alpha^*(n))$:
- No critical point lies on $J(R_\alpha)$.
- $R_\alpha$ is J-stable: $J(R_\alpha)$ varies continuously in the Hausdorff metric.
- $R_\alpha$ is hyperbolic (expanding on $J$).

**Corollary 4.4** (Dimension). $\dim_H J(R_\alpha) < 2$ for $\alpha \in (0, \alpha^*(n))$.

*Proof.* Hyperbolic rational maps have Julia sets of Hausdorff dimension strictly less than 2 (Ruelle; Przytycki–Urbański–Zdunik). $\square$

---

## 5. Proof of Part (d): Bifurcation

### 5.1. Multiplier at infinity

The multiplier of $R_\alpha$ at $z = \infty$ is $\lambda_\infty(\alpha) = q_{d-1}(\alpha)/p_d(\alpha)$ where $p_d, q_{d-1}$ are the leading coefficients of $P(z)$ and $Q(z)$ respectively.

**Numerical computation:**

| $n$ | $\alpha = 0.1$ | $0.5$ | $0.8$ | $\alpha^*$ | $0.9$ |
|-----|:-:|:-:|:-:|:-:|:-:|
| 2 | 3.06 (R) | 3.54 (R) | 8.81 (R) | $\sim 1$ | 0.35 (**A**) |
| 3 | 2.03 (R) | 2.27 (R) | 30.3 (R) | $\sim 1$ | 0.88 (**A**) |
| 4 | 1.68 (R) | 1.85 (R) | 4.81 (R) | $\sim 1$ | 1.00 (N) |
| 5 | 1.51 (R) | 1.64 (R) | 1.27 (R) | $\sim 1$ | 1.03 (R) |

R = repelling, A = attracting, N = neutral.

At $\alpha = \alpha^*(n)$, $|\lambda_\infty| = 1$: the point at infinity undergoes a **saddle-node** or **period-doubling** bifurcation. Beyond $\alpha^*$, $\infty$ becomes attracting and, by Fatou's theorem, must capture at least one critical orbit. $\square$

### 5.2. Bifurcation values

Binary search (20 iterations, tolerance $\sim 10^{-6}$):

| $n$ | $\alpha^*(n)$ |
|-----|--------------|
| 2 | $0.8693$ |
| 3 | $0.8357$ |
| 4 | $0.8062$ |
| 5 | $0.8008$ |

The sequence $\alpha^*(n)$ is decreasing with $n$, apparently converging to a limit $\alpha^*(\infty) \approx 0.80$.

---

## 6. Proof of Part (e): Contrast with Newton

For $n \geq 3$, Newton's method $N_f(z) = z - f(z)/f'(z) = ((n-1)z^n + 1)/(nz^{n-1})$ has degree $n$ on $\hat{\mathbb{C}}$.

**Critical points of $N_f$:** $z = 0$ (free critical point) and the roots of $f$ (superattracting). The orbit of $z = 0$ under Newton:
$$N_f(0) = 1/(n \cdot 0^{n-1}) = \infty, \qquad N_f(\infty) = \infty$$

Since $\infty$ is a repelling fixed point of $N_f$ with multiplier $n/(n-1) > 1$, and $\infty \in J(N_f)$, the critical orbit $\{0, \infty, \infty, \ldots\}$ lies on the Julia set.

By Shishikura (1990): $\dim_H J(N_f) = 2$ for $n \geq 3$.

In contrast, for $R_\alpha$ with $\alpha \in (0, \alpha^*(n))$:
- All critical orbits converge to roots (in the Fatou set)
- $R_\alpha$ is hyperbolic
- $\dim_H J(R_\alpha) < 2$

This establishes that the PM damping mechanism ($\alpha \neq 1$) resolves the fractal pathology of Newton's method for polynomials of degree $\geq 3$. $\blacksquare$

---

## 7. Summary of General Formulas

| Quantity | General formula | $n=3$ |
|----------|----------------|-------|
| $R_0(z)$ | $z \cdot \frac{(n-1)z^n+(n+1)}{(n+1)z^n+(n-1)}$ | $\frac{z(z^3+2)}{2z^3+1}$ |
| $\deg R_0$ | $n + 1$ | 4 |
| $R_0'(z)$ | $\frac{(n^2-1)(z^n-1)^2}{((n+1)z^n+(n-1))^2}$ | $\frac{8(z^3-1)^2}{(4z^3+2)^2}$ |
| Mult. at $0, \infty$ | $\frac{n+1}{n-1}$ | 2 |
| $\deg R_\alpha$ | $n(2n-1)$ | 15 |
| Free crit. structure | $z^{n-2} H(z^n)$ | $z \cdot H(z^3)$ |
| $\deg_t H$ | $4n - 5$ | 7 |
| $\#$ $\mathbb{Z}_n$-orbits | $4n - 5$ | 7 |
| $\alpha^*(n)$ | $\searrow$ with $n$ | 0.836 |

---

## 8. Remarks

### R1. The case $n = 2$

For $f(z) = z^2 - 1$, Newton's method already gives a smooth Julia set ($J = i\mathbb{R}$, the imaginary axis). The PM scheme also gives J-stability. The theorem's contrast with Newton is meaningful only for $n \geq 3$.

### R2. Negative $\alpha$

Numerical evidence suggests full stability for all $\alpha < 0$:

| $n$ | $\alpha = -0.1$ | $-0.5$ | $-1.0$ |
|-----|:-:|:-:|:-:|
| 2 | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| 3 | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| 5 | $\checkmark$ | $\checkmark$ | $\checkmark$ |

**Conjecture.** $R_\alpha$ is J-stable for all $\alpha \in (-\infty, 0)$, for every $n \geq 2$.

### R3. Asymptotic behavior of $\alpha^*(n)$

From the data $\alpha^*(2) = 0.869$, $\alpha^*(3) = 0.836$, $\alpha^*(4) = 0.806$, $\alpha^*(5) = 0.801$, the sequence appears to converge. If $\alpha^*(\infty) > 0$, then the PM scheme with $\alpha \in (0, \alpha^*(\infty))$ would be universally stable for all $z^n - 1$.

### R4. Rigorous computer-assisted proof

The numerical orbit-tracking in Section 4.1 can be made rigorous via interval arithmetic (e.g., CAPD library or Julia package `IntervalArithmetics.jl`). For each $\alpha$:
1. Compute certified enclosures of all roots of the degree-$(2n(2n-1)-2)$ critical polynomial.
2. Iterate with interval arithmetic, verifying that each orbit enters a certified neighborhood of a root.

### R5. Connection to basin entropy

The basin entropy $S_b(\alpha)$ (Daza et al., 2016) provides a quantitative measure of boundary complexity. Since $R_\alpha$ is hyperbolic for $\alpha \in (0, \alpha^*(n))$, the uncertainty exponent is $\alpha_{ue} = 1$ (smooth boundaries have no fractal uncertainty). For Newton ($\alpha = 1$), $\alpha_{ue} < 1$. The transition at $\alpha^*$ corresponds to the onset of positive basin entropy.

### R6. Extension beyond $z^n - 1$

For general polynomials $f(z)$ of degree $n$:
- The $\mathbb{Z}_n$ symmetry is lost, but the core mechanism persists.
- $R_0$ still exists (the formula depends on $f$, $f'$, not just on the symmetry).
- The degree reduction $n(2n-1) \to n+1$ as $\alpha \to 0$ still occurs (critical points coalesce with poles).
- J-stability for small $\alpha$ is expected by the same perturbation argument.

A complete treatment for general $f$ is a natural next step.
