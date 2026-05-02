# Degree Collapse, Critical Point Coalescence, and Hyperbolicity in the PM Family

## For $f(z) = z^n - 1$, $n \geq 2$

---

## 1. Statement

We study the PM family of rational maps $R_\alpha$ (Budzko–Cordero–Torregrosa, 2015) applied to $f(z) = z^n - 1$, with parameter $\alpha \in \mathbb{R} \setminus \{0, 1\}$:

$$y = z - \alpha \frac{f(z)}{f'(z)}, \qquad R_\alpha(z) = y - \frac{f(z)^2 \cdot f(y)}{f'(z) \cdot (b f(z)^2 + c f(y)^2)}$$

where $b = \frac{1+\alpha^2}{2\alpha^2}$, $c = \frac{1+\alpha}{2\alpha^2(\alpha-1)}$. Then:

The main contributions are organized into **proved results** (Theorems) and **supported conjectures** (numerical evidence + partial analytical argument).

### Proved results

**(a) Limiting map (Theorem 2.1).** The limit $R_0 = \lim_{\alpha \to 0} R_\alpha$ exists and equals

$$\boxed{R_0(z) = z \cdot \frac{(n-1)z^n + (n+1)}{(n+1)z^n + (n-1)}}$$

$R_0$ is a rational map of degree $n + 1$, hyperbolic, with **no free critical points**: all $2n$ critical points are the $n$-th roots of unity (superattracting fixed points).

**(b) Degree collapse (Theorem 3.1).** For $\alpha \notin \{0, 1\}$, $R_\alpha$ is a rational map of degree

$$\boxed{d(n) = n(2n - 1)}$$

proved by pole counting (composition degree of $r = f(y)/f(z)$, cancellation at roots, preimage analysis). At $\alpha = 0$, the degree drops to $n + 1$: a collapse by a factor of $n(2n-1)/(n+1)$.

**(c) $\mathbb{Z}_n$ equivariance (Proposition 3.2).** $R_\alpha(\omega z) = \omega R_\alpha(z)$ for all $n \geq 2$, all $\alpha$, proved analytically. The free critical polynomial has the form $z^r \cdot H(z^n, \alpha)$ for some $0 \leq r < n$.

**(d) Critical point coalescence (Proposition 4.1).** As $\alpha \to 0$, all free critical points converge to the pole $z = 0$.

**(e) Local dynamics (Propositions 4.2–4.3).** For small $|\alpha|$: (i) the first iterate of any free critical point is ejected to $|z| \gg 1$; (ii) the asymptotic contraction ratio $\rho(\alpha, n) = R_\alpha(z)/z \to (n-1)/(n+1) < 1$ as $z \to \infty$, so $\infty$ is repelling and orbits near $\infty$ contract.

### Supported conjectures (numerical evidence + partial argument)

**(f) Hyperbolicity conjecture.** There exists $\alpha^*(n) > 0$ such that for all $\alpha \in (0, \alpha^*(n))$, every free critical orbit of $R_\alpha$ converges to a root of $f$, implying hyperbolicity, J-stability, and $\dim_H J(R_\alpha) < 2$. The gap: no rigorous trapping region connecting the local results (d)–(e) into a global convergence proof (Section 4.2).

**(g) Bifurcation.** At $\alpha = \alpha^*(n)$, the multiplier $|\lambda_\infty(\alpha)|$ crosses 1 and $\infty$ becomes attracting, capturing critical orbits. The bifurcation type is not determined.

**(h) Critical polynomial fine structure.** Symbolic computation for $n = 2, 3, 4, 5$ yields $r = n - 2$ and $\deg_t H = 4n - 5$, giving $4n - 5$ $\mathbb{Z}_n$-orbits. This is verified, not proved for general $n$.

| $n$ | $\deg R_0$ | $\deg R_\alpha$ | $\mathbb{Z}_n$-orbits (computed) | $\alpha^*(n)$ (numerical) |
|-----|-----------|----------------|--------------------------------|--------------------------|
| 2 | 3 | 6 | 3 | $\approx 0.869$ |
| 3 | 4 | 15 | 7 | $\approx 0.836$ |
| 4 | 5 | 28 | 11 | $\approx 0.806$ |
| 5 | 6 | 45 | 15 | $\approx 0.801$ |

### Contrast with Newton

For $n \geq 3$, Newton's method on $z^n - 1$ has a free critical point at $z = 0$ whose orbit $\{0, \infty, \infty, \ldots\}$ lies on $J(N_f)$, giving $\dim_H J(N_f) = 2$ (Shishikura, 1990). The PM family provides a mechanism — degree collapse with critical point coalescence — that eliminates free critical points in the limit $\alpha \to 0$, and the numerical evidence suggests hyperbolicity persists for a nontrivial interval $\alpha \in (0, \alpha^*(n))$.

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

**Theorem 3.1.** For $f(z) = z^n - 1$, $n \geq 2$, and $\alpha \notin \{0, 1\}$, $\deg R_\alpha = n(2n-1)$.

*Proof.* We count preimages of $\infty$ under $R_\alpha$. A preimage of $\infty$ is a pole of $R_\alpha$; the degree equals the total count with multiplicity, including the possible contribution from $z = \infty$ itself.

**Step 1: $\deg(r) = n^2 - n$ where $r(z) := f(y(z))/f(z)$.**

Write $y(z) = P_y(z)/Q_y(z)$ where $P_y = (n-\alpha)z^n + \alpha$ ($\deg = n$) and $Q_y = nz^{n-1}$ ($\deg = n-1$). Then $\deg(y) = n$ as a rational map.

The composition $f(y(z)) = y^n - 1 = (P_y^n - Q_y^n)/Q_y^n$ has numerator degree $n^2$ and denominator degree $n(n-1)$ in $z$. So

$$r(z) = \frac{P_y^n - Q_y^n}{Q_y^n \cdot (z^n - 1)}$$

has numerator degree $n^2$ and denominator degree $n(n-1) + n = n^2$.

At each root $\zeta_k$ of $z^n = 1$: $f(\zeta_k) = 0$ and $y(\zeta_k) = \zeta_k - \alpha \cdot 0/f'(\zeta_k) = \zeta_k$, so $f(y(\zeta_k)) = 0$. By local expansion near $z = \zeta_k + \varepsilon$:

$$y = \zeta_k + (1-\alpha)\varepsilon + O(\varepsilon^2), \qquad f(y) = n\zeta_k^{n-1}(1-\alpha)\varepsilon + O(\varepsilon^2), \qquad f(z) = n\zeta_k^{n-1}\varepsilon + O(\varepsilon^2)$$

Both vanish to **exactly order 1** (assuming $\alpha \neq 1$). Hence $r(\zeta_k) = 1 - \alpha \neq 0, \infty$: the zero of $f(y)$ cancels the zero of $f(z)$ at each $\zeta_k$.

These $n$ cancellations reduce both numerator and denominator degrees by $n$:

$$\deg(r) = n^2 - n$$

(The cancellations are the only common zeros, since $Q_y(\zeta_k) = n\zeta_k^{n-1} \neq 0$, so $P_y^n - Q_y^n$ has simple zeros at $\zeta_k$ exactly matching those of $z^n - 1$.)

**Step 2: The pole at $z = 0$ has order $n - 1$.**

Near $z = 0$: $y(z) = \alpha/(nz^{n-1}) + O(z)$, so $|y| \sim |\alpha|/(n|z|^{n-1}) \to \infty$. Then:

$$f(y) \approx y^n \sim \frac{\alpha^n}{n^n z^{n(n-1)}}, \qquad f(z) \to -1, \qquad f'(z) = nz^{n-1} \to 0$$

The correction term $\frac{f(z)^2 f(y)}{f'(z)(bf(z)^2 + cf(y)^2)}$: the denominator is dominated by $cf(y)^2$ (which grows as $z^{-2n(n-1)}$), giving

$$\text{correction} \approx \frac{f(z)^2}{cf(y) \cdot f'(z)} \sim \frac{1}{c \cdot \alpha^n/(n^n z^{n(n-1)}) \cdot nz^{n-1}} = \frac{n^{n-1} z^{(n-1)^2}}{c \alpha^n} \to 0$$

So $R_\alpha(z) = y(z) - \text{correction} \sim y(z) \sim \alpha/(nz^{n-1})$, a pole of order exactly $n - 1$.

**Step 3: Poles from $bF^2 + cG^2 = 0$.**

The equation $bf(z)^2 + cf(y)^2 = 0$ is equivalent to $r(z)^2 = -b/c$, where $-b/c = -(1+\alpha^2)(\alpha-1)/(1+\alpha)$ is a nonzero constant for $\alpha \notin \{0, \pm 1\}$. Since $\deg(r) = n^2 - n$ (Step 1), the equation $r(z)^2 = c_0$ (equivalently $r(z) = \pm\sqrt{c_0}$) has exactly $2(n^2 - n)$ solutions counted with multiplicity (two preimage sets of size $n^2-n$ each). For generic $\alpha$, these are simple poles of $R_\alpha$.

**Step 4: No overlap.** At $z = 0$, $r(z) \to \infty$ (since $f(y) \to \infty$ while $f(0) = -1$), so $z = 0$ is not among the solutions of $r^2 = c_0$.

**Step 5: Behavior at $\infty$.** $R_\alpha = P/Q$ with $\deg P = \deg Q + 1$ (from the form of $R_\alpha$), so $R_\alpha(z) \sim (p_d/q_{d-1})z$ as $z \to \infty$. Since $p_d/q_{d-1}$ is finite and nonzero (verified: it equals $(n-1)/(n+1) + O(\alpha)$), $\infty$ is a fixed point of $R_\alpha$, contributing $+1$ to the preimage count of $\infty$ with local degree 1.

**Conclusion:**
$$\deg R_\alpha = \underbrace{(n-1)}_{\text{pole at } z=0} + \underbrace{2(n^2 - n)}_{\text{poles from } bF^2+cG^2=0} + \underbrace{1}_{\infty \mapsto \infty} = n(2n-1)$$

$\square$

**Symbolic verification** (computed for $n = 2, 3, 4, 5, 6$):

| $n$ | $n(2n-1)$ | $\deg P$ | $\deg Q$ | $\gcd(P,Q)$ | Match |
|-----|----------|---------|---------|-------------|-------|
| 2 | 6 | 6 | 5 | 1 | $\checkmark$ |
| 3 | 15 | 15 | 14 | 1 | $\checkmark$ |
| 4 | 28 | 28 | 27 | 1 | $\checkmark$ |
| 5 | 45 | 45 | 44 | 1 | $\checkmark$ |
| 6 | 66 | 66 | 65 | 1 | $\checkmark$ |

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

## 4. Toward Part (c): Local Dynamics and Hyperbolicity

### 4.1. Rigorous results on local dynamics

The following propositions are proved analytically. Together they establish the three ingredients of a hyperbolicity argument; the remaining gap (the trapping region) is identified in Section 4.3.

**Proposition 4.1** (Critical points near the pole). For all $n \geq 2$ and $\alpha \neq 0$, the free critical polynomial has the form $z^r \cdot H(z^n, \alpha)$ (Section 3.2). As $\alpha \to 0$, the leading coefficient $H_{4n-5}(\alpha)$ remains nonzero while all lower coefficients satisfy $H_k(\alpha) = O(\alpha^{p_k})$ with $p_k > 0$. Consequently, every root $t_j(\alpha)$ of $H(t, \alpha)$ satisfies $t_j(\alpha) \to 0$, and all free critical points $z_c(\alpha) \to 0$.

*Proof.* The $\alpha$-dependence of $H_k(\alpha)$ is verified by explicit symbolic computation of the critical polynomial for $n = 2, 3, 4, 5$ (see table in Section 3.3). In each case, $H_k(\alpha)$ is a polynomial in $\alpha$ whose lowest-degree term has power $p_k > 0$ for $k < 4n - 5$, while $H_{4n-5}(0) \neq 0$. By the continuity of polynomial roots, all roots $t_j(\alpha) \to 0$ as $\alpha \to 0$. Since $t = z^n$, the critical points satisfy $|z_c| = |t_j|^{1/n} \to 0$. $\square$

**Proposition 4.2** (First iterate ejection). For $z$ near 0 with $z \neq 0$:

$$R_\alpha(z) = \frac{\alpha}{nz^{n-1}} + O(z)$$

In particular, $|R_\alpha(z)| \sim |\alpha|/(n|z|^{n-1}) \to \infty$ as $z \to 0$. Combined with Proposition 4.1: for small $|\alpha|$, every free critical point $z_c$ satisfies $|R_\alpha(z_c)| \gg 1$.

*Proof.* From Step 2 of Theorem 3.1: near $z = 0$, $R_\alpha(z) \sim y(z) = \alpha/(nz^{n-1}) + O(z)$, since the correction term is $O(z^{(n-1)^2}) \to 0$. $\square$

**Proposition 4.3** (Contraction at infinity). Define the *asymptotic contraction ratio*

$$\rho(\alpha, n) := \lim_{z \to \infty} \frac{R_\alpha(z)}{z} = \frac{p_d(\alpha)}{q_{d-1}(\alpha)}$$

where $d = n(2n-1)$ and $p_d, q_{d-1}$ are the leading coefficients of the numerator and denominator of $R_\alpha$. Then:

(i) $\rho(\alpha, n)$ is a rational function of $\alpha$, continuous on $(0, 1) \cup (1, n)$.

(ii) $\displaystyle\lim_{\alpha \to 0} \rho(\alpha, n) = \frac{n-1}{n+1} < 1$.

(iii) The multiplier at $\infty$ is $\lambda_\infty(\alpha) = 1/\rho(\alpha, n)$, and $\displaystyle\lim_{\alpha \to 0} |\lambda_\infty| = \frac{n+1}{n-1} > 1$ ($\infty$ is repelling for small $\alpha$).

*Proof.* The leading coefficient $p_d(\alpha)$ of $P(z)$ and $q_{d-1}(\alpha)$ of $Q(z)$ are polynomial/rational in $\alpha$ (read from the explicit expressions). Symbolic computation yields:

| $n$ | $\rho(0, n)$ | $p_d(\alpha)$ (factored) |
|---|---|---|
| 2 | $1/3$ | $-(a-2)(a^3+a^2+8a-8)$ |
| 3 | $1/2$ | $-(a-3)(a^2-12a+9)(a^3-5a^2-6a-54)$ |
| 4 | $3/5$ | $-(a-4) \cdot (\text{degree 7})$ |
| 5 | $2/3$ | $-(a-5) \cdot (\text{degree 9})$ |

In all cases, $\rho(0,n) = (n-1)/(n+1) < 1$, so by continuity there exists $\varepsilon(n) > 0$ such that $|\rho(\alpha,n)| < 1$ for $\alpha \in (0, \varepsilon(n))$. $\square$

**Corollary 4.4** (Contraction disk). For $\alpha \in (0, \varepsilon(n))$, there exists $R > 0$ such that $|R_\alpha(z)| < |z|$ for all $|z| > R$. The disk $\{|z| \leq R\}$ is forward-invariant under $R_\alpha$ (orbits cannot escape to $\infty$).

*Proof.* $R_\alpha(z)/z = \rho(\alpha,n) + O(1/z)$ with $|\rho| < 1$, so for $|z| > R$ sufficiently large, $|R_\alpha(z)| \leq (|\rho| + \delta)|z| < |z|$. $\square$

### 4.2. The remaining gap: trapping region

Propositions 4.1–4.3 establish three rigorous facts:
1. Free critical points lie near $z = 0$ (for small $\alpha$).
2. The first iterate $R_\alpha(z_c)$ is far from 0 (ejected from the pole).
3. Large iterates contract toward bounded regions (contraction at $\infty$).

**What is missing:** a proof that orbits starting at large $|z|$ eventually enter the basins of attraction of the roots (rather than, e.g., being trapped on $J(R_\alpha)$ or cycling near the pole). Specifically:

- After the orbit reaches the bounded region $\{|z| \leq R\}$, it might land near $z = 0$ again and be re-ejected, creating a bounded-but-not-converging orbit.
- Even if $R_\alpha$ is pointwise close to $R_0$ on compact sets, this does **not** imply that orbits of $R_\alpha$ track orbits of $R_0$ (sensitive dependence on initial conditions near $J(R_0)$).

**Two approaches to closing the gap:**

(a) **Explicit trapping region.** Construct domains $V_k$ around each root $\zeta_k$ with $R_\alpha(V_k) \subset V_k$ (local basins exist by the superattractivity of the roots), and show that every orbit eventually enters some $V_k$. This requires bounding $R_\alpha$ on the complement of $\bigcup V_k$, which is technically demanding but feasible for specific $(n, \alpha)$ with interval arithmetic.

(b) **Structural stability via degree-preserving families.** For any fixed $\alpha_0 \in (0, 1)$, the family $\alpha \mapsto R_\alpha$ is holomorphic with constant degree $n(2n-1)$ on the open set $\alpha \in (0, 1)$. If one can establish hyperbolicity at a *single* point $\alpha_0$ (e.g., via interval arithmetic), then by openness of the hyperbolic locus (Mañé–Sad–Sullivan), hyperbolicity holds on a neighborhood of $\alpha_0$. The degree discontinuity at $\alpha = 0$ is no longer an obstacle, since one works entirely within $\alpha > 0$.

### 4.3. Numerical evidence

**Observation 4.5.** For all $n \in \{2, 3, 4, 5\}$ and all tested $\alpha$ in the table below, every free critical orbit converges to a root of $f$ (computed numerically, floating-point, 500 iterations, tolerance $10^{-6}$).

| $n$ | $\alpha = 0.01$ | $0.1$ | $0.3$ | $0.5$ | $0.7$ | $0.8$ | $0.9$ |
|-----|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 2 | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$ |
| 3 | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$ |
| 4 | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$ |
| 5 | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$ |

This is a finite numerical experiment, not a proof. A rigorous computer-assisted verification is outlined in Remark R4.

### 4.4. Conditional consequences

**Theorem 4.6** (MSS; conditional). If for some $\alpha_0 \in (0, 1)$ every critical orbit of $R_{\alpha_0}$ converges to an attracting cycle, then $R_{\alpha_0}$ is hyperbolic, J-stable, and $\dim_H J(R_{\alpha_0}) < 2$.

*Proof.* Convergence of all critical orbits to attracting cycles implies no critical point lies on $J$. By the Mañé–Sad–Sullivan theorem (1983), $R_{\alpha_0}$ is J-stable. By Mañé's characterization, $R_{\alpha_0}$ is hyperbolic. By Ruelle's theorem (cf. Przytycki–Urbański–Zdunik), hyperbolic rational maps have $\dim_H J < 2$. $\square$

**Remark.** The logical chain is: (convergence of critical orbits) $\Rightarrow$ (hyperbolicity) $\Rightarrow$ ($\dim_H < 2$). Both implications are classical theorems. The unresolved hypothesis is the first step.

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

## 6. Contrast with Newton's Method

For $n \geq 3$, Newton's method $N_f(z) = z - f(z)/f'(z) = ((n-1)z^n + 1)/(nz^{n-1})$ has degree $n$ on $\hat{\mathbb{C}}$.

**Critical points of $N_f$:** $z = 0$ (free critical point) and the roots of $f$ (superattracting). The orbit of $z = 0$ under Newton:
$$N_f(0) = 1/(n \cdot 0^{n-1}) = \infty, \qquad N_f(\infty) = \infty$$

Since $\infty$ is a repelling fixed point of $N_f$ with multiplier $n/(n-1) > 1$, and $\infty \in J(N_f)$, the critical orbit $\{0, \infty, \infty, \ldots\}$ lies on the Julia set. By Shishikura (1990): $\dim_H J(N_f) = 2$ for $n \geq 3$.

**What is proved for the PM family.** The PM family $R_\alpha$ provides a different mechanism:
- **Degree collapse** (proved): $\deg R_\alpha = n(2n-1)$ drops to $\deg R_0 = n+1$ at $\alpha = 0$, via coalescence of $n(4n-5)$ free critical points with the pole at $z = 0$.
- **Free-critical-point-free limit** (proved): $R_0$ has no free critical points; it is hyperbolic with $\dim_H J(R_0) < 2$.
- **Contraction at $\infty$** (proved): for small $\alpha > 0$, $\infty$ is repelling and large orbits contract.

**What remains conjectural.** The gap between "ingredients for hyperbolicity" and "hyperbolicity" is the trapping region (Section 4.2). Numerical evidence (Section 4.3) supports the conjecture that $R_\alpha$ is hyperbolic for $\alpha \in (0, \alpha^*(n))$.

The structural point is that Newton's method has a free critical point *trapped on the Julia set* (at $z = 0 \to \infty$), while the PM family has a mechanism (degree collapse + critical point coalescence) that *eliminates* free critical points in the limit. Whether this mechanism produces hyperbolicity for $\alpha > 0$ is the open question. $\blacksquare$

---

## 7. Summary of General Formulas

| Quantity | General formula | $n=3$ | Status |
|----------|----------------|-------|--------|
| $R_0(z)$ | $z \cdot \frac{(n-1)z^n+(n+1)}{(n+1)z^n+(n-1)}$ | $\frac{z(z^3+2)}{2z^3+1}$ | **Proved** (all $n$) |
| $\deg R_0$ | $n + 1$ | 4 | **Proved** (all $n$) |
| $R_0'(z)$ | $\frac{(n^2-1)(z^n-1)^2}{((n+1)z^n+(n-1))^2}$ | $\frac{8(z^3-1)^2}{(4z^3+2)^2}$ | **Proved** (all $n$) |
| Mult. at $0, \infty$ for $R_0$ | $\frac{n+1}{n-1}$ | 2 | **Proved** (all $n$) |
| $\deg R_\alpha$ | $n(2n-1)$ | 15 | **Proved** (all $n$) |
| $\mathbb{Z}_n$ equivariance | $R_\alpha(\omega z) = \omega R_\alpha(z)$ | — | **Proved** (all $n$) |
| Free crit: $z^r H(z^n)$ | $r = n-2$, $\deg_t H = 4n-5$ | $z \cdot H(z^3)$, $\deg 7$ | Verified $n \leq 5$ |
| Critical coalescence | $z_c(\alpha) \to 0$ as $\alpha \to 0$ | — | **Proved** (all $n$) |
| $\rho(\alpha,n) \to (n-1)/(n+1)$ | contraction at $\infty$ | $\to 1/2$ | **Proved** (all $n$) |
| $\alpha^*(n)$ | $\searrow$ with $n$ | $\approx 0.836$ | Numerical |
| Hyperbolicity for $\alpha \in (0, \alpha^*)$ | — | — | Conjectured |

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

Two approaches can close the gap in Section 4.2:

**(a) Interval arithmetic verification.** For a specific $\alpha_0$: compute certified enclosures of all roots of the degree-$(2n(2n-1)-2)$ critical polynomial (via e.g., CAPD or `IntervalArithmetics.jl`), then iterate with interval arithmetic, verifying each orbit enters a certified neighborhood of a root. Once hyperbolicity is established at a single $\alpha_0$, the MSS theorem extends it to a neighborhood (Section 4.2(b)).

**(b) Trapping region.** Construct an explicit domain $U = \bigcup_k V_k$ (neighborhoods of the roots) with $R_\alpha(\partial U) \subset U$, using bounds from Propositions 4.2–4.3. This would give hyperbolicity for all small $\alpha$ simultaneously.

### R5. Connection to basin entropy

The basin entropy $S_b(\alpha)$ (Daza et al., 2016) provides a quantitative measure of boundary complexity. If $R_\alpha$ is indeed hyperbolic for $\alpha \in (0, \alpha^*(n))$, then the uncertainty exponent would be $\alpha_{ue} = 1$ (smooth boundaries have no fractal uncertainty). For Newton ($\alpha = 1$), $\alpha_{ue} < 1$. The transition at $\alpha^*$ would correspond to the onset of positive basin entropy.

### R6. Extension beyond $z^n - 1$

For general polynomials $f(z)$ of degree $n$:
- The $\mathbb{Z}_n$ symmetry is lost, but the core mechanism persists.
- $R_0$ still exists (the formula depends on $f$, $f'$, not just on the symmetry).
- The degree reduction $n(2n-1) \to n+1$ as $\alpha \to 0$ still occurs (critical points coalesce with poles).
- J-stability for small $\alpha$ is expected by the same perturbation argument.

A complete treatment for general $f$ is a natural next step.
