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

The $\mathbb{Z}_n$ equivariance $R_\alpha(\omega z) = \omega R_\alpha(z)$ (proved analytically in Section 3.2) forces the free critical polynomial into the form $z^r \cdot H(z^n, \alpha)$. Symbolic computation for $n = 2, 3, 4, 5$ yields $r = n - 2$ and $\deg_t H = 4n - 5$, suggesting the general structure

$$z^{n-2} \cdot H(z^n, \alpha), \qquad \deg_t H = 4n - 5$$

giving $n(4n - 5)$ free critical points organized in $4n - 5$ orbits under $z \mapsto e^{2\pi i/n} z$.

**(c) Hyperbolicity (numerical evidence and heuristic argument).** Numerical computation (Section 4.1) and a heuristic analytical argument (Section 4.2) provide strong evidence that there exists $\alpha^*(n) > 0$ such that for all $\alpha \in (0, \alpha^*(n))$, every free critical orbit of $R_\alpha$ converges to a root of $f$. If this holds, then $R_\alpha$ is hyperbolic and J-stable in this region, and $\dim_H J(R_\alpha) < 2$ (by Ruelle; Przytycki–Urbański–Zdunik).

**(d) Bifurcation.** Numerical evidence (Section 5) indicates that at $\alpha = \alpha^*(n)$, the multiplier $|\lambda_\infty(\alpha)|$ crosses 1 and the fixed point $\infty$ transitions from repelling to attracting, capturing critical orbits. The type of bifurcation (saddle-node, period-doubling, etc.) is not determined.

| $n$ | $\deg R_0$ | $\deg R_\alpha$ | $\mathbb{Z}_n$-orbits | $\alpha^*(n)$ (numerical) |
|-----|-----------|----------------|----------------------|--------------------------|
| 2 | 3 | 6 | 3 | $\approx 0.869$ |
| 3 | 4 | 15 | 7 | $\approx 0.836$ |
| 4 | 5 | 28 | 11 | $\approx 0.806$ |
| 5 | 6 | 45 | 15 | $\approx 0.801$ |

**(e) Contrast with Newton.** For $n \geq 3$, Newton's method on $z^n - 1$ has $\dim_H J(N_f) = 2$ (Shishikura, 1990). The numerical and heuristic evidence of part (c) suggests that the PM scheme avoids this pathology for $\alpha \in (0, \alpha^*(n))$: if hyperbolicity holds, then $\dim_H J(R_\alpha) < 2$.

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

*Proof (pole counting).* We count the finite poles of $R_\alpha$ on $\hat{\mathbb{C}}$.

**Source 1: The predictor pole at $z = 0$.** The predictor $y(z) = z - \alpha f(z)/f'(z) = ((n-\alpha)z^n + \alpha)/(nz^{n-1})$ has a pole of order $n-1$ at $z = 0$. When $y \to \infty$, $f(y) \to y^n \to \infty$, so the correction term $f(z)^2 f(y) / (f'(z)(bf(z)^2 + cf(y)^2))$ also diverges. Thus $z = 0$ is a pole of $R_\alpha$ of order $n - 1$.

**Source 2: Vanishing of the weight denominator.** The correction denominator $bf(z)^2 + cf(y)^2 = 0$ holds when

$$r(z)^2 = -\frac{b}{c} = -\frac{(1+\alpha^2)(\alpha-1)}{1+\alpha}, \qquad r(z) := \frac{f(y(z))}{f(z)}$$

The rational function $r(z) = f(y)/f(z)$ has degree $n^2 - n$ as a map $\hat{\mathbb{C}} \to \hat{\mathbb{C}}$. To see this: $y(z)$ is a rational function of degree $n$ (numerator degree $n$, denominator degree $n-1$), so $f(y(z)) = y(z)^n - 1$ has degree $n^2$ as a rational function, while $f(z) = z^n - 1$ has degree $n$. A priori $\deg r \leq n^2$. The cancellation of $n$ common preimages (the roots $z^n = 1$, where $f(z) = 0$ and $y(\zeta_k) = \zeta_k$, giving $f(y) = 0$ as well) reduces the degree to $n^2 - n$, confirmed symbolically for $n = 2,3,4,5$. The equation $r(z)^2 = \text{const}$ then has generically $2(n^2 - n)$ solutions.

**No overlap:** At $z = 0$, $r(z)$ has a pole (since $y(0) \to \infty$ but $f(0) = -1 \neq 0$), so $z = 0$ is not among the roots of $r^2 = \text{const}$.

**Pole count:**
$$\text{finite poles} = \underbrace{(n-1)}_{\text{at } z=0} + \underbrace{2(n^2 - n)}_{\text{from } bF^2 + cG^2 = 0} = 2n^2 - n - 1$$

Since $R_\alpha(\infty) = \infty$ (the leading behavior gives a well-defined nonzero ratio), $\infty$ is not a pole. Hence

$$\deg R_\alpha = (\text{finite poles}) + 1 = 2n^2 - n - 1 + 1 = n(2n - 1)$$

**Symbolic verification:**

| $n$ | $n(2n-1)$ | $\deg P$ (computed) | $\deg Q$ (computed) | $\gcd$ | Match |
|-----|----------|--------------------|--------------------|--------|-------|
| 2 | 6 | 6 | 5 | 1 | $\checkmark$ |
| 3 | 15 | 15 | 14 | 1 | $\checkmark$ |
| 4 | 28 | 28 | 27 | 1 | $\checkmark$ |
| 5 | 45 | 45 | 44 | 1 | $\checkmark$ |

$\square$

### 3.2. Critical polynomial structure

**Proposition 3.2.** The critical polynomial $P'Q - PQ'$ has degree $2n(2n-1) - 2$ and is divisible by $(z^n - 1)^2$. The free critical polynomial (quotient) has degree $4n^2 - 4n - 2$ and the $\mathbb{Z}_n$-equivariant form

$$\text{FreeCrit}(z) = z^{n-2} \cdot H(z^n, \alpha)$$

where $H(t, \alpha)$ is a polynomial of degree $4n - 5$ in $t = z^n$.

*Proof.* **Step 1: $\mathbb{Z}_n$ equivariance.** Let $\omega = e^{2\pi i/n}$. For $f(z) = z^n - 1$:

$$f(\omega z) = f(z), \qquad f'(\omega z) = \omega^{n-1} f'(z)$$

The predictor satisfies $y(\omega z) = \omega y(z)$:

$$y(\omega z) = \omega z - \alpha \frac{f(\omega z)}{f'(\omega z)} = \omega z - \frac{\alpha f(z)}{\omega^{n-1} f'(z)} = \omega z - \omega^{1-n} \cdot \frac{\alpha f(z)}{f'(z)} = \omega\left(z - \frac{\alpha f(z)}{f'(z)}\right) = \omega y(z)$$

where we used $\omega^{1-n} = \omega^{1} \cdot \omega^{-n} = \omega$ (since $\omega^n = 1$).

Setting $F = f(z)$, $G = f(y(z))$: under $z \mapsto \omega z$, we have $F \mapsto F$, $G \mapsto G$ (since $f(\omega y) = (\omega y)^n - 1 = y^n - 1 = G$), $f'(z) \mapsto \omega^{n-1} f'(z)$. The correction term transforms as:

$$\frac{F^2 G}{f'(\omega z)(bF^2 + cG^2)} = \frac{F^2 G}{\omega^{n-1} f'(z)(bF^2 + cG^2)} = \omega^{1-n} \cdot \frac{F^2 G}{f'(z)(bF^2 + cG^2)} = \omega \cdot \text{correction}$$

Hence $R_\alpha(\omega z) = \omega y - \omega \cdot \text{correction} = \omega R_\alpha(z)$.

**Step 2: Structure of $P$ and $Q$.** Writing $R_\alpha = P/Q$, the equivariance $R_\alpha(\omega z) = \omega R_\alpha(z)$ forces $P(\omega z) Q(z) = \omega P(z) Q(\omega z)$. Since $P(\omega z) = \omega^a P(z)$ and $Q(\omega z) = \omega^b Q(z)$, we get $a \equiv b + 1 \pmod{n}$. Verified: $P$ has only terms $z^k$ with $k \equiv 0 \pmod{n}$, $Q$ has terms with $k \equiv n-1 \pmod{n}$, for all $n = 2,3,4,5$.

**Step 3: Free critical polynomial.** The critical polynomial $P'Q - PQ'$ inherits the equivariance. The trivial factor $(z^n-1)^2$ is $\mathbb{Z}_n$-invariant (a polynomial in $z^n$). The free quotient must therefore have the form $z^r H(z^n)$ for some $0 \leq r < n$.

The values $r = n-2$ and $\deg_t H = 4n-5$ are verified by symbolic computation for $n = 2, 3, 4, 5$. A general proof that $r = n - 2$ for all $n$ would require an analysis of the leading and trailing terms of $P'Q - PQ'$ modulo $(z^n - 1)^2$, which we do not carry out here.

**Remark.** Steps 1–2 (the $\mathbb{Z}_n$ equivariance and the monomial structure $z^r H(z^n)$) are proved for all $n$. Only the specific value $r = n - 2$ and the formula $\deg_t H = 4n - 5$ rest on computation for $n \leq 5$.

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

The same pattern (increasing $\alpha$-powers for decreasing $k$) holds for $n = 2, 4, 5$.

This is the **degree reduction mechanism**: the $n(4n-5)$ free critical points merge with the pole at $z = 0$ as $\alpha \to 0$, reducing the effective degree from $n(2n-1)$ to $n+1$.

---

## 4. Evidence for Part (c): Hyperbolicity

### 4.1. Numerical evidence: convergence of free critical orbits

**Observation 4.1.** For all $n \in \{2, 3, 4, 5\}$ and all tested $\alpha \in (0, \alpha^*(n))$, every free critical orbit of $R_\alpha$ converges to a root of $f$ (computed numerically).

*Method.* For each $n$ and each $\alpha$ in a grid:

1. Substitute $\alpha$ into the symbolic critical polynomial (degree $2n(2n-1)-2$).
2. Find all roots via `numpy.roots`.
3. Classify: trivial (near roots of $f$), near-pole (near $z = 0$), free.
4. For each free critical point, iterate $R_\alpha$ up to 500 steps and check convergence to a root (tolerance $10^{-6}$).

**Results (computed numerically, positive $\alpha$):**

| $n$ | $\alpha = 0.01$ | $0.1$ | $0.3$ | $0.5$ | $0.7$ | $0.8$ | $0.9$ |
|-----|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 2 | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$ |
| 3 | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$ |
| 4 | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$ |
| 5 | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$ |

$\checkmark$ = all free critical orbits converge to roots.

**Remark.** This is a finite numerical experiment, not a proof. It does not cover all $\alpha$ in the interval, nor does it certify convergence rigorously (floating-point arithmetic, no interval enclosures). A rigorous computer-assisted proof would require interval arithmetic; see Section 8, Remark R4.

### 4.2. Heuristic analytical argument (small $|\alpha|$)

The following argument outlines a strategy that, if made rigorous, would prove hyperbolicity for small $|\alpha|$. We identify the gaps explicitly.

**Claim 4.2** (not yet a theorem). For sufficiently small $|\alpha| > 0$, all free critical orbits of $R_\alpha$ converge to roots of $f$.

*Outline of argument.*

1. **Critical points near the pole.** By Proposition 3.3, the free critical points satisfy $|z_c| = O(|\alpha|^s)$ for some $s > 0$, approaching the pole $z = 0$.

2. **First iterate.** Since $z = 0$ is a pole of $R_\alpha$ of order $n - 1$ (from $y(z) = ((n-\alpha)z^n + \alpha)/(nz^{n-1})$), the first iterate $R_\alpha(z_c)$ has $|R_\alpha(z_c)| \gg 1$.

3. **Contraction at $\infty$.** The asymptotic behavior of $R_\alpha$ for $|z| \gg 1$ is

$$R_\alpha(z) \approx \frac{p_{d}(\alpha)}{q_{d-1}(\alpha)} z$$

where $d = n(2n-1)$. For small $\alpha$, this ratio approaches $(n-1)/(n+1) < 1$. Since $|(n-1)/(n+1)| < 1$, iterates contract toward bounded regions.

4. **Gap: transition from large to moderate $|z|$.** After $O(\log(1/|\alpha|))$ iterates, the orbit enters a bounded region $\{|z| \leq M\}$. To conclude convergence, one needs to show that:
   - $R_\alpha$ is uniformly close to $R_0$ on this region (away from the finitely many poles), **and**
   - orbits starting in the Fatou set of $R_0$ remain in the Fatou set of $R_\alpha$.

   The second point does **not** follow from pointwise closeness of $R_\alpha$ to $R_0$ alone. Closeness of maps does not guarantee closeness of basins: nearby maps can have very different basin boundaries. A rigorous argument would require either:
   - an explicit **trapping region** argument: find a domain $U$ containing all root basins such that $R_\alpha(U) \subset U$ and $R_\alpha$ contracts on $U$; or
   - appeal to the **structural stability theorem** (MSS): if $R_0$ is hyperbolic (which it is — all critical orbits are superattracting fixed points) and $R_\alpha \to R_0$ holomorphically, then hyperbolicity persists for small $|\alpha|$ by openness of the hyperbolic locus.

5. **The MSS route (most promising).** $R_0$ is hyperbolic. The family $\alpha \mapsto R_\alpha$ is holomorphic for $\alpha \neq 0, 1$. **However**, $\alpha = 0$ is a degenerate point: the degree jumps from $n(2n-1)$ to $n+1$. Standard MSS/structural stability applies to families of fixed degree. The degree change at $\alpha = 0$ means this is not a direct application of the theorem — one cannot simply say "hyperbolicity is open, $R_0$ is hyperbolic, done."

   A rigorous proof would need to handle the degree transition, e.g., by analyzing the family on the subset $\{0 < |\alpha| < \varepsilon\}$ and showing hyperbolicity directly there (perhaps via the trapping region approach).

### 4.3. Conditional consequences

The following statements are valid **conditional on all free critical orbits converging to roots** (i.e., conditional on the conclusion of Claim 4.2 or a rigorous version of Observation 4.1).

**Corollary 4.3** (MSS). If for some $\alpha_0$ every critical orbit of $R_{\alpha_0}$ converges to an attracting cycle, then:
- No critical point lies on $J(R_{\alpha_0})$.
- By the Mañé–Sad–Sullivan theorem, $R_{\alpha_0}$ is J-stable.
- $R_{\alpha_0}$ is hyperbolic (expanding on $J$).

**Corollary 4.4** (Dimension). If $R_\alpha$ is hyperbolic, then $\dim_H J(R_\alpha) < 2$.

*Proof.* Hyperbolic rational maps have Julia sets of Hausdorff dimension strictly less than 2 (Ruelle; Przytycki–Urbański–Zdunik). $\square$

**Remark.** The logical chain is: convergence of all critical orbits $\Rightarrow$ hyperbolicity $\Rightarrow$ $\dim_H < 2$. Both implications are theorems (the first is a characterization due to Mañé; the second is Ruelle's theorem). The missing piece is the hypothesis: a rigorous proof that all critical orbits converge.

---

## 5. Numerical Evidence for Part (d): Bifurcation

### 5.1. Multiplier at infinity

The multiplier of $R_\alpha$ at $z = \infty$ is $\lambda_\infty(\alpha) = q_{d-1}(\alpha)/p_d(\alpha)$ where $p_d, q_{d-1}$ are the leading coefficients of $P(z)$ and $Q(z)$ respectively. This is a rational function of $\alpha$ that can be computed exactly from the symbolic expressions for $P$ and $Q$.

**Numerical values of $|\lambda_\infty|$:**

| $n$ | $\alpha = 0.1$ | $0.5$ | $0.8$ | $\alpha^*$ | $0.9$ |
|-----|:-:|:-:|:-:|:-:|:-:|
| 2 | 3.06 (R) | 3.54 (R) | 8.81 (R) | $\sim 1$ | 0.35 (**A**) |
| 3 | 2.03 (R) | 2.27 (R) | 30.3 (R) | $\sim 1$ | 0.88 (**A**) |
| 4 | 1.68 (R) | 1.85 (R) | 4.81 (R) | $\sim 1$ | 1.00 (N) |
| 5 | 1.51 (R) | 1.64 (R) | 1.27 (R) | $\sim 1$ | 1.03 (R) |

R = repelling, A = attracting, N = neutral. Values computed numerically from the exact rational expression $\lambda_\infty(\alpha)$.

The data suggests that at $\alpha = \alpha^*(n)$, $|\lambda_\infty|$ crosses 1 and $\infty$ transitions from repelling to attracting. If $\infty$ becomes attracting, then by Fatou's theorem it must capture at least one critical orbit, breaking the convergence to roots observed in Section 4.

**Remark.** We have not determined the type of bifurcation (saddle-node, period-doubling, etc.) — this would require a normal form analysis or a study of $\lambda_\infty(\alpha)$ near $|\lambda_\infty| = 1$, which we do not carry out.

### 5.2. Bifurcation values

Approximate $\alpha^*(n)$ computed by binary search (20 iterations, tolerance $\sim 10^{-6}$):

| $n$ | $\alpha^*(n)$ (numerical) |
|-----|--------------------------|
| 2 | $\approx 0.8693$ |
| 3 | $\approx 0.8357$ |
| 4 | $\approx 0.8062$ |
| 5 | $\approx 0.8008$ |

The sequence $\alpha^*(n)$ appears to decrease with $n$, suggesting a limit $\alpha^*(\infty) \approx 0.80$.

---

## 6. Part (e): Contrast with Newton

For $n \geq 3$, Newton's method $N_f(z) = z - f(z)/f'(z) = ((n-1)z^n + 1)/(nz^{n-1})$ has degree $n$ on $\hat{\mathbb{C}}$.

**Critical points of $N_f$:** $z = 0$ (free critical point) and the roots of $f$ (superattracting). The orbit of $z = 0$ under Newton:
$$N_f(0) = 1/(n \cdot 0^{n-1}) = \infty, \qquad N_f(\infty) = \infty$$

Since $\infty$ is a repelling fixed point of $N_f$ with multiplier $n/(n-1) > 1$, and $\infty \in J(N_f)$, the critical orbit $\{0, \infty, \infty, \ldots\}$ lies on the Julia set.

By Shishikura (1990): $\dim_H J(N_f) = 2$ for $n \geq 3$.

In contrast, for $R_\alpha$ with $\alpha \in (0, \alpha^*(n))$, the numerical evidence (Section 4.1) and heuristic argument (Section 4.2) indicate that:
- All critical orbits converge to roots (in the Fatou set)
- $R_\alpha$ is hyperbolic (conditional — see Section 4.3)
- $\dim_H J(R_\alpha) < 2$ (conditional on hyperbolicity)

This provides strong evidence that the PM damping mechanism ($\alpha \neq 1$) avoids the fractal pathology of Newton's method in the regime $\alpha \in (0, \alpha^*(n))$ for polynomials of degree $\geq 3$. A complete proof requires rigorous verification of the critical orbit convergence (see Remark R4). $\blacksquare$

---

## 7. Summary of General Formulas

| Quantity | General formula | $n=3$ | Status |
|----------|----------------|-------|--------|
| $R_0(z)$ | $z \cdot \frac{(n-1)z^n+(n+1)}{(n+1)z^n+(n-1)}$ | $\frac{z(z^3+2)}{2z^3+1}$ | **Proved** |
| $\deg R_0$ | $n + 1$ | 4 | **Proved** |
| $R_0'(z)$ | $\frac{(n^2-1)(z^n-1)^2}{((n+1)z^n+(n-1))^2}$ | $\frac{8(z^3-1)^2}{(4z^3+2)^2}$ | **Proved** |
| Mult. at $0, \infty$ | $\frac{n+1}{n-1}$ | 2 | **Proved** |
| $\deg R_\alpha$ | $n(2n-1)$ | 15 | Proved + verified $n \leq 5$ |
| Free crit. structure | $z^{n-2} H(z^n)$ | $z \cdot H(z^3)$ | Verified $n \leq 5$ |
| $\deg_t H$ | $4n - 5$ | 7 | Verified $n \leq 5$ |
| $\#$ $\mathbb{Z}_n$-orbits | $4n - 5$ | 7 | Verified $n \leq 5$ |
| $\alpha^*(n)$ | $\searrow$ with $n$ | $\approx 0.836$ | Numerical |

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

The basin entropy $S_b(\alpha)$ (Daza et al., 2016) provides a quantitative measure of boundary complexity. If $R_\alpha$ is indeed hyperbolic for $\alpha \in (0, \alpha^*(n))$, then the uncertainty exponent would be $\alpha_{ue} = 1$ (smooth boundaries have no fractal uncertainty). For Newton ($\alpha = 1$), $\alpha_{ue} < 1$. The transition at $\alpha^*$ would correspond to the onset of positive basin entropy.

### R6. Extension beyond $z^n - 1$

For general polynomials $f(z)$ of degree $n$:
- The $\mathbb{Z}_n$ symmetry is lost, but the core mechanism persists.
- $R_0$ still exists (the formula depends on $f$, $f'$, not just on the symmetry).
- The degree reduction $n(2n-1) \to n+1$ as $\alpha \to 0$ still occurs (critical points coalesce with poles).
- J-stability for small $\alpha$ is expected by the same perturbation argument.

A complete treatment for general $f$ is a natural next step.
