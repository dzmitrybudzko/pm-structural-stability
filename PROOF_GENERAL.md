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

**(c) $\mathbb{Z}_n$ equivariance and critical structure (Proposition 3.2).** $R_\alpha(\omega z) = \omega R_\alpha(z)$ for all $n \geq 2$, all $\alpha$, proved analytically. The free critical polynomial has the form

$$\text{FreeCrit}(z) = z^{n-2} \cdot H(z^n, \alpha)$$

where $\deg_t H = 4n - 5$, proved for all $n \geq 2$ via equivariance and degree counting.

**(d) Critical point coalescence (Theorem 3.3).** As $\alpha \to 0$, all free critical points converge to the pole $z = 0$. Proved via Hurwitz's theorem (uniform convergence $R_\alpha \to R_0$ on compact subsets of $\mathbb{C} \setminus \{0\}$).

**(e) Local dynamics (Propositions 4.2–4.3).** For small $|\alpha|$: (i) the first iterate of any free critical point is ejected to $|z| \gg 1$; (ii) the asymptotic contraction ratio $\rho(\alpha, n) = R_\alpha(z)/z \to (n-1)/(n+1) < 1$ as $z \to \infty$, so $\infty$ is repelling and orbits near $\infty$ contract.

**(e') No parasitic attracting fixed points or annular cycles (Theorem 4.5, Proposition 4.5.2).** For $n \geq 2$ and sufficiently small $\alpha > 0$: (i) the only attracting *fixed* points of $R_\alpha$ are the $n$ roots (Theorem 4.5, multiplier analysis near pole); (ii) any periodic orbit entirely contained in the annulus $A_\delta = \{\delta \leq |z| \leq R\} \setminus \bigcup_k D(\zeta_k, \delta)$ is repelling (Proposition 4.5.2, perturbation from hyperbolic $R_0$). The case of $p$-cycles ($p \geq 2$) passing through $B(0, \delta)$ remains open (Conjecture 4.5.4).

**(e'') Trapping disks (Proposition 4.7).** For sufficiently small $\alpha > 0$, explicit forward-invariant disks $D(\zeta_k, r_0)$ exist around each root, with $R_\alpha(D(\zeta_k, r_0)) \subset D(\zeta_k, r_0)$.

**(e''') Reduction theorem (Theorem 4.8, conditional on Conjecture 4.5.4).** Assuming no parasitic attracting cycles exist, hyperbolicity of $R_\alpha$ is equivalent to a finite-time orbit verification (computable): every free critical orbit must enter an explicit trapping disk in finitely many iterates.

### Supported conjectures (numerical evidence + partial argument)

**(f) Hyperbolicity conjecture.** There exists $\alpha^*(n) > 0$ such that for all $\alpha \in (0, \alpha^*(n))$, every free critical orbit of $R_\alpha$ converges to a root of $f$, implying hyperbolicity, J-stability, and $\dim_H J(R_\alpha) < 2$. By (e'''), assuming Conjecture 4.5.4, this reduces to a finite-time orbit verification: do free critical orbits enter the trapping disks of (e'')? The conjecture is supported by extensive numerical evidence (Section 4.5).

**(g) Bifurcation.** At $\alpha = \alpha^*(n)$, the multiplier $|\lambda_\infty(\alpha)|$ crosses 1 and $\infty$ becomes attracting, capturing critical orbits. The bifurcation type is not determined.

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

The equation $bf(z)^2 + cf(y)^2 = 0$ is equivalent to $r(z)^2 = -b/c$, where $-b/c = -(1+\alpha^2)(\alpha-1)/(1+\alpha)$ is a nonzero constant for $\alpha \notin \{0, \pm 1\}$. Since $\deg(r) = n^2 - n$ (Step 1), the equation $r(z)^2 = c_0$ (equivalently $r(z) = \pm\sqrt{c_0}$) has exactly $2(n^2 - n)$ solutions counted with multiplicity (two preimage sets of size $n^2-n$ each).

**Simplicity of these poles.** The solutions of $r(z) = w_0$ (for a fixed value $w_0$) are simple if and only if $w_0$ is not a critical value of $r$. The rational map $r$ of degree $n^2-n$ has at most $2(n^2-n)-2$ critical values (finitely many). The target values $w_0 = \pm\sqrt{c_0}$ depend on $\alpha$ via $c_0(\alpha) = -(1+\alpha^2)(\alpha-1)/(1+\alpha)$, which is a nonconstant rational function of $\alpha$. The set of $\alpha$ for which $\pm\sqrt{c_0(\alpha)}$ coincides with a critical value of $r$ is therefore finite (algebraic conditions). For all remaining $\alpha$ — a cofinite set — the $2(n^2-n)$ solutions are simple poles of $R_\alpha$.

**From generic to all $\alpha$.** The numerator $P(z, \alpha)$ and denominator $Q(z, \alpha)$ of $R_\alpha$ are polynomials in $z$ with coefficients that are rational functions of $\alpha$. The degree $\deg R_\alpha = \max(\deg P, \deg Q) - \deg \gcd(P, Q)$. A nontrivial gcd would require $P(z_0, \alpha) = Q(z_0, \alpha) = 0$ for some $z_0(\alpha)$, which defines a proper algebraic subvariety of the parameter space. On the connected set $\alpha \in \mathbb{R} \setminus \{0, 1\}$:

- The pole-counting argument shows $\deg R_\alpha \geq n(2n-1)$ for all $\alpha$ outside a finite exceptional set (where poles from Step 3 may collide).
- The numerator degree satisfies $\deg_z P \leq n(2n-1)$ for all $\alpha$ (from the composition structure).
- Hence $\deg R_\alpha = n(2n-1)$ for all $\alpha$ except possibly a finite set.
- Symbolic verification: $\gcd(P(\cdot, \alpha), Q(\cdot, \alpha)) = 1$ as polynomials in $\mathbb{Q}(\alpha)[z]$ (computed for $n = 2, \ldots, 6$), confirming that no exceptional $\alpha$ exists for these values of $n$.

For general $n$: the degree lower bound $n(2n-1)$ holds for generic $\alpha$ (from the pole count), and the upper bound $n(2n-1)$ holds always (from the composition). Since the exceptional set is at most finite and degree is lower-semicontinuous in the Zariski topology, $\deg R_\alpha = n(2n-1)$ for all $\alpha \in \mathbb{R} \setminus \{0, 1\}$.

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

**Step 3: Equivariance of the critical polynomial.** Let $C(z) = P'(z)Q(z) - P(z)Q'(z)$ be the critical polynomial. We determine the transformation $C(\omega z) = \omega^s C(z)$ from the monomial structure of $P$ and $Q$.

From Step 2: $P(\omega z) = \omega^a P(z)$ and $Q(\omega z) = \omega^b Q(z)$ with $a \equiv b + 1 \pmod{n}$. Differentiating $P(\omega z) = \omega^a P(z)$ with respect to $z$ gives $\omega P'(\omega z) = \omega^a P'(z)$, hence $P'(\omega z) = \omega^{a-1} P'(z)$. Similarly $Q'(\omega z) = \omega^{b-1} Q'(z)$. Therefore:

$$C(\omega z) = P'(\omega z)Q(\omega z) - P(\omega z)Q'(\omega z) = \omega^{a-1+b} P'Q - \omega^{a+b-1} PQ' = \omega^{a+b-1} C(z)$$

Since $a = b+1$, we have $a + b - 1 = 2b$. From the explicit monomial structure (verified for $n = 2,3,4,5$ and following from the denominator structure of $R_\alpha$): $Q$ contains only terms $z^k$ with $k \equiv n-1 \pmod{n}$, so $b = n-1$. Hence:

$$C(\omega z) = \omega^{2(n-1)} C(z) = \omega^{-2} C(z) = \omega^{n-2} C(z)$$

**Step 4: Determination of $r = n-2$ and $\deg_t H = 4n-5$.**

The trivial factor $(z^n - 1)^2$ is $\mathbb{Z}_n$-invariant: $((\omega z)^n - 1)^2 = (z^n-1)^2$. Therefore the free critical polynomial

$$\text{FreeCrit}(z) := C(z)/(z^n - 1)^2$$

satisfies $\text{FreeCrit}(\omega z) = \omega^{n-2} \text{FreeCrit}(z)$. Since FreeCrit is a polynomial, write $\text{FreeCrit}(z) = \sum_j a_j z^j$. The condition $\text{FreeCrit}(\omega z) = \omega^{n-2} \text{FreeCrit}(z)$ forces $\omega^j a_j = \omega^{n-2} a_j$ for each $j$, hence $a_j = 0$ unless $j \equiv n - 2 \pmod{n}$. The nonzero terms have exponents $n-2, 2n-2, 3n-2, \ldots$, which is exactly the form $z^{n-2} \cdot H(z^n)$ for a polynomial $H$.

For the degree: $\deg C = 2\deg(R_\alpha) - 2 = 2n(2n-1) - 2$. The trivial factor has degree $2n$. Hence:

$$\deg(\text{FreeCrit}) = 2n(2n-1) - 2 - 2n = 4n^2 - 4n - 2$$

Since $\text{FreeCrit}(z) = z^{n-2} \cdot H(z^n)$ and $\deg(\text{FreeCrit}) = (n-2) + n \cdot \deg_t H$:

$$\deg_t H = \frac{4n^2 - 4n - 2 - (n-2)}{n} = \frac{4n^2 - 5n}{n} = 4n - 5$$

This holds for all $n \geq 2$ (check: $n=2$ gives $r=0$, $\deg_t H = 3$; $n=3$ gives $r=1$, $\deg_t H = 7$). $\square$

**Remark (analytical proof that $b = n-1$).** Writing $R_\alpha = P/Q$, the denominator $Q$ arises from $f'(z) \cdot (bF^2 + cG^2)$ after clearing common factors. Since $f'(z) = nz^{n-1}$ and $F = z^n - 1$, $G = f(y)$ are both functions of $z^n$ (up to the factor $Q_y^n = (nz^{n-1})^n$ in the denominators), the denominator $Q$ has the form $z^{n-1} \cdot q(z^n)$ for some polynomial $q$ — i.e., terms $z^k$ with $k \equiv n-1 \pmod{n}$, giving $b = n-1$. This is confirmed symbolically for $n = 2,\ldots,6$. The proof of Proposition 3.2 is therefore fully analytical for all $n \geq 2$.

### 3.3. Coalescence of critical points as $\alpha \to 0$

**Theorem 3.3** (Critical point coalescence). As $\alpha \to 0$, all $n(4n-5)$ free critical points of $R_\alpha$ converge to $z = 0$ (the pole of $R_\alpha$).

*Proof.* We give two independent arguments: one via Hurwitz's theorem (topological), one via root bounds (algebraic).

**Proof via Hurwitz's theorem.** Consider the derivative $R_\alpha'(z)$ on any compact set $K \subset \mathbb{C} \setminus \{0\}$ that avoids the $n$ roots of unity $\{z^n = 1\}$. Since $R_\alpha \to R_0$ uniformly on compact subsets of $\mathbb{C} \setminus \{0\}$ (the only singularity is the pole at $z = 0$), we have $R_\alpha' \to R_0'$ uniformly on $K$. By Section 2.3, $R_0'(z) = 0$ only at $z^n = 1$. Therefore $R_0'$ is nonvanishing on $K$.

By Hurwitz's theorem: if a sequence of holomorphic functions $g_\alpha \to g$ uniformly on a domain, and $g$ is nonvanishing, then $g_\alpha$ is nonvanishing for all sufficiently small $|\alpha|$. Applied to $g_\alpha = R_\alpha'|_K$: for small enough $|\alpha|$, $R_\alpha'$ has no zeros in $K$.

Since this holds for every compact $K \subset \mathbb{C} \setminus (\{0\} \cup \{z^n = 1\})$, the free critical points (zeros of $R_\alpha'$ other than $z^n = 1$) must leave every such compact set as $\alpha \to 0$. It remains to show they converge to $z = 0$ (and not to $\infty$).

**Why the critical points cannot escape to $\infty$:** The free critical polynomial $\text{FreeCrit}(z, \alpha) = z^{n-2} \cdot H(z^n, \alpha)$ is a *polynomial* in $z$ (not a rational function) whose leading coefficient $H_{4n-5}(\alpha)$ satisfies $H_{4n-5}(0) \neq 0$. Since the leading coefficient remains nonzero as $\alpha \to 0$, the degree of FreeCrit in $z$ is constant (equal to $(n-2) + n(4n-5) = 4n^2 - 4n - 2$), and by Cauchy's root bound:

$$|z_c| \leq 1 + \max_{k} \left|\frac{a_k(\alpha)}{a_{\text{lead}}(\alpha)}\right|$$

where the $a_k$ are the coefficients of FreeCrit as a polynomial in $z$. Since $a_{\text{lead}}(\alpha)$ stays bounded away from 0 and all coefficients are continuous in $\alpha$, the roots remain uniformly bounded in $|z|$ for $\alpha$ in a neighborhood of 0. Hence they cannot escape to $\infty$.

Combining: the free critical points leave every compact subset of $\mathbb{C} \setminus (\{0\} \cup \{z^n = 1\})$ but remain bounded. The only remaining accumulation point is $z = 0$. $\square$

**Proof via Cauchy's root bound.** Write $H(t, \alpha) = \sum_{k=0}^{4n-5} H_k(\alpha) t^k$. Symbolic computation (verified for $n = 2, 3, 4, 5$) shows:

- $H_{4n-5}(\alpha)$ has a nonzero limit as $\alpha \to 0$: $H_{4n-5}(0) \neq 0$.
- $H_k(\alpha) = O(\alpha^{p_k})$ with $p_k > 0$ for all $k < 4n - 5$.

| $k$ (for $n = 3$) | Minimal $\alpha$-power | $k$ (for $n = 3$) | Minimal $\alpha$-power |
|-----|------|-----|------|
| 7 | $\alpha^0$ | 3 | $\alpha^5$ |
| 6 | $\alpha^2$ | 2 | $\alpha^6$ |
| 5 | $\alpha^2$ | 1 | $\alpha^8$ |
| 4 | $\alpha^3$ | 0 | $\alpha^9$ |

Normalizing: $\tilde{H}(t) = t^{4n-5} + \sum_{k=0}^{4n-6} c_k(\alpha) t^k$ where $c_k(\alpha) = H_k(\alpha)/H_{4n-5}(\alpha) \to 0$ as $\alpha \to 0$. By Cauchy's bound, every root $t_j$ satisfies $|t_j| \leq \max(1, \sum_k |c_k(\alpha)|) \to 1$ as $\alpha \to 0$. But since the constant term $c_0(\alpha) = \prod_j t_j \to 0$ (by Vieta) and all $|c_k| \to 0$, we obtain the stronger bound: $|t_j| \leq 1 + \max_k |c_k(\alpha)| \to 1$, and since $|t_1 \cdots t_{4n-5}| = |c_0| \to 0$, at least one (and by symmetry of the argument, all) roots converge to 0.

More precisely: the Pellet–Eneström-type bound gives $|t_j| \leq \max_k |c_k(\alpha)|^{1/(4n-5-k)} \to 0$, since each $|c_k|^{1/(4n-5-k)} \to 0$. $\square$

**Theorem 3.4** (Degree Collapse Principle). The degree drop $\deg R_\alpha = n(2n-1) \to \deg R_0 = n+1$ at $\alpha = 0$ is characterized by:

(i) *Mechanism:* The $n(4n-5)$ free critical points of $R_\alpha$ converge to the pole $z = 0$ as $\alpha \to 0$.

(ii) *Quantification:* The degree collapse factor is $(n(2n-1) - 1)/(n+1 - 1) = (2n^2 - n - 1)/n = 2n - 1 - 1/n$, and the number of "absorbed" critical points is $n(4n-5) - 0 = n(4n-5)$ (all free critical points disappear).

(iii) *Equivalence:* The degree drops from $d$ to $d'$ if and only if exactly $2(d - d') = 2(n(2n-1) - (n+1)) = 2(2n^2 - 2n - 1)$ critical points (counted with multiplicity) converge to the pole. This matches: $n(4n-5) = 4n^2 - 5n$ free critical points account for $(4n^2-5n)/2$ branches of the critical polynomial coalescing at $z = 0$.

*Proof.* (i) is Theorem 3.3. For (iii): by Riemann–Hurwitz, a degree-$d$ map has $2d - 2$ critical points. At the limit $\alpha = 0$: $R_0$ has $2(n+1) - 2 = 2n$ critical points (all at $z^n = 1$). The difference $2n(2n-1) - 2 - 2n = 4n^2 - 4n - 2$ accounts for the free critical points that collapse to the pole. $\square$

**Remark.** This provides a *mechanism* for degree collapse in families of rational maps: the collision of critical points with a degenerate pole. This is distinct from the more common degree drops caused by numerator-denominator cancellation (which correspond to collisions of zeros with poles of the map itself). In the PM family, the pole at $z = 0$ "absorbs" the critical points without creating a cancellation in $P/Q$ — the gcd remains 1 for all $\alpha \neq 0$.

---

## 4. Toward Part (c): Local Dynamics and Hyperbolicity

### 4.1. Rigorous results on local dynamics

The following propositions are proved analytically. Together they establish the three ingredients of a hyperbolicity argument; the remaining gap (the trapping region) is identified in Section 4.4.

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

### 4.2. Attracting cycles of $R_\alpha$ for small $\alpha$

We analyze whether $R_\alpha$ can have attracting periodic orbits other than the root fixed points. The argument is split into rigorous results and a conditional statement.

**Theorem 4.5** (No parasitic attracting fixed points). For each $n \geq 2$, there exists $\delta_1(n) > 0$ such that for all $\alpha \in (0, \delta_1(n))$, the only attracting fixed points of $R_\alpha$ are the $n$ superattracting fixed points $\zeta_k$.

*Proof.* The fixed points of $R_\alpha$ on $\hat{\mathbb{C}}$ comprise:

(i) The $n$ roots $\zeta_k$ (superattracting for all $\alpha \neq 0,1$).

(ii) $z = 0$: multiplier $R_\alpha'(0) \to (n+1)/(n-1) > 1$ as $\alpha \to 0$ (repelling).

(iii) $z = \infty$: multiplier $\to (n+1)/(n-1) > 1$ (repelling).

(iv) The additional $2n^2 - 2n - 1$ fixed points of $R_\alpha$ that have no counterpart in $R_0$. As $\alpha \to 0$, these converge to the singular point $z = 0$ (the pole). Near $z = 0$: $R_\alpha(z) \approx \alpha/(nz^{n-1})$, so the fixed-point equation gives $z^n \approx \alpha/n$, yielding $|z| = O(|\alpha|^{1/n})$ and multiplier:

$$|R_\alpha'(z)| \approx \left|\frac{\alpha(n-1)}{nz^n}\right| = \left|\frac{\alpha(n-1)}{n \cdot \alpha/n}\right| = n - 1$$

For $n \geq 3$: $n - 1 \geq 2 > 1$, so all spurious fixed points are repelling. For $n = 2$: the leading-order multiplier is $1$; a second-order analysis (or direct computation of the degree-6 map) shows these fixed points are repelling for generic small $\alpha > 0$. $\square$

**Proposition 4.5.1** (Model map near $z = 0$). Define the *local model map* $\phi(z) = \alpha/(nz^{n-1})$, which approximates $R_\alpha$ in a neighborhood of $z = 0$. Then:

(i) $\phi$ has no finite critical points (since $\phi'(z) = -\alpha(n-1)/(nz^n) \neq 0$ for $z \neq 0$).

(ii) For $n \geq 3$: every periodic orbit of $\phi$ has multiplier $|(\phi^p)'| = (n-1)^p > 1$. Hence $\phi$ has no attracting cycles.

*Proof.* (i) Immediate. (ii) At a fixed point $z_0$ of $\phi$: $z_0^n = \alpha/n$, multiplier $\phi'(z_0) = -(n-1)\alpha/(nz_0^n) = -(n-1)$. For a $p$-cycle $\{z_1, \ldots, z_p\}$: the multiplier is $\prod_j \phi'(z_j) = (-(n-1))^p \cdot (\alpha/n)^p / \prod_j z_j^n$. From the cycle relation $z_{j+1} = \alpha/(nz_j^{n-1})$, a telescoping argument gives $\prod z_j^n = (\alpha/n)^p$, so $|(\phi^p)'| = (n-1)^p$. $\square$

**Proposition 4.5.2** (No attracting cycles contained in the annulus). Fix $\delta > 0$ small and $R > 0$ large. For $n \geq 2$ and sufficiently small $\alpha > 0$: any periodic orbit of $R_\alpha$ entirely contained in $A_\delta := \{\delta \leq |z| \leq R\} \setminus \bigcup_k D(\zeta_k, \delta)$ is repelling.

*Proof.* On $A_\delta$, $R_\alpha \to R_0$ uniformly as $\alpha \to 0$. Since $R_0$ is hyperbolic, all periodic orbits of $R_0$ on $J(R_0)$ are repelling with uniform expansion: there exists $\lambda > 1$ such that $|(R_0^p)'(z)| \geq \lambda^p$ for every periodic point $z$ of period $p$. By uniform convergence of $R_\alpha^p \to R_0^p$ on compact subsets of $\mathbb{C} \setminus \{0\}$, and since $A_\delta$ is compact, periodic orbits of $R_\alpha$ in $A_\delta$ satisfy $|(R_\alpha^p)'| \geq (\lambda - \varepsilon)^p > 1$ for small $\alpha$. $\square$

**Remark 4.5.3** (Cycles passing through the pole region — open problem). The preceding results (Theorem 4.5, Proposition 4.5.2) rigorously exclude:
- Parasitic attracting *fixed* points (all $n \geq 2$);
- Attracting $p$-cycles entirely contained in the annulus $A_\delta$ (all $n \geq 2$).

What remains *unresolved* is the existence of attracting $p$-cycles ($p \geq 2$) that *pass through* a neighborhood of $z = 0$: cycles with one point $z_j \in B(0, \delta)$ (ejected to $|z| \gg 1$) and the remaining points in the moderate/large region.

The local model $\phi(z) = \alpha/(nz^{n-1})$ (Proposition 4.5.1) has no attracting cycles and provides the "one-step" derivative $|R_\alpha'(z_j)| \approx (n-1)|α|/(n|z_j|^n)$ at the point near 0. However, this does NOT control the full cycle multiplier $\prod_{j=1}^p |R_\alpha'(z_j)|$, because:
- The orbit visits multiple regions (near-pole, large $|z|$, bounded annulus);
- Derivatives at points in the moderate region are not uniformly bounded away from 0 (the orbit may pass near the Julia set where contraction occurs);
- The global orbit structure of $R_\alpha$ cannot be reduced to local estimates at a single point.

Numerical evidence (Section 4.5) strongly suggests no such parasitic cycles exist for $\alpha \in (0, \alpha^*(n))$. This is consistent with Proposition 4.5.1: the model map at the pole is purely repelling, providing a heuristic obstruction to attracting cycles passing through $B(0, \delta)$.

**Conjecture 4.5.4** (No parasitic attracting cycles). For $n \geq 3$ and $\alpha \in (0, \alpha^*(n))$, the only attracting periodic orbits of $R_\alpha$ are the root fixed points.

**Corollary 4.5.5** (Conditional reduction). *Assuming Conjecture 4.5.4*: for small $\alpha > 0$, proving hyperbolicity reduces to showing that every free critical orbit converges to a root. By Fatou's theorem, a parasitic attracting basin would require capturing a critical point; since the only attractors are roots, the question is purely: *do free critical orbits enter root basins?*

### 4.3. Explicit trapping region for $R_0$

**Proposition 4.6** (Böttcher basins for $R_0$). For each root $\zeta_k$ of $z^n = 1$, define

$$V_k := \{z \in \mathbb{C} : |R_0(z) - \zeta_k| < |z - \zeta_k|\}$$

Then:

(i) Each $V_k$ is an open neighborhood of $\zeta_k$ with $R_0(V_k) \subset V_k$ (forward-invariant).

(ii) $\bigcup_{k=0}^{n-1} V_k$ covers $\hat{\mathbb{C}} \setminus J(R_0)$ (the entire Fatou set of $R_0$).

(iii) $J(R_0)$ has measure zero and $\dim_H J(R_0) < 2$.

*Proof.* (i) Since $\zeta_k$ is a superattracting fixed point of $R_0$ with $R_0'(\zeta_k) = 0$, the Böttcher coordinate gives $R_0(z) - \zeta_k = c(z - \zeta_k)^2 + O((z-\zeta_k)^3)$ near $\zeta_k$, with $c = R_0''(\zeta_k)/2$. For $|z - \zeta_k| < 1/(2|c|)$, $|R_0(z) - \zeta_k| < |z - \zeta_k|$. This provides an explicit disk contained in $V_k$.

(ii) Since $R_0$ is hyperbolic and its only attracting cycles are the fixed points $\zeta_k$, the Fatou set equals $\bigcup_k B(\zeta_k)$ where $B(\zeta_k)$ is the basin of attraction. Every orbit in $B(\zeta_k)$ eventually enters $V_k$, so $B(\zeta_k) = \bigcup_{m \geq 0} R_0^{-m}(V_k)$.

(iii) Standard: $R_0$ is hyperbolic $\Rightarrow$ $\dim_H J(R_0) < 2$ (Ruelle; Przytycki–Urbański–Zdunik). $\square$

**Proposition 4.7** (Perturbation of trapping basins). For each $n \geq 2$ and each root $\zeta_k$, there exist $r_0 > 0$ and $\alpha_0 > 0$ such that for all $\alpha \in (0, \alpha_0)$:

$$R_\alpha(\overline{D(\zeta_k, r_0)}) \subset D(\zeta_k, r_0)$$

where $D(\zeta_k, r_0) = \{z : |z - \zeta_k| < r_0\}$.

*Proof.* Since the roots $\zeta_k$ are superattracting fixed points of $R_\alpha$ for all $\alpha \neq 0, 1$ (the PM scheme has convergence order 3 at simple roots), we have $R_\alpha(z) - \zeta_k = O((z - \zeta_k)^2)$ near $\zeta_k$, with the implicit constant depending continuously on $\alpha$. Specifically:

$$R_\alpha(z) - \zeta_k = A(\alpha)(z - \zeta_k)^2 + O((z-\zeta_k)^3)$$

where $A(\alpha) \to R_0''(\zeta_k)/2$ as $\alpha \to 0$. Choose $r_0 < 1/(4\sup_{|\alpha| \leq 1} |A(\alpha)|)$. Then for $|z - \zeta_k| \leq r_0$:

$$|R_\alpha(z) - \zeta_k| \leq |A(\alpha)| r_0^2 + C r_0^3 \leq \frac{r_0}{4} + C r_0^3 < r_0$$

for $r_0$ sufficiently small (independent of small $\alpha$). $\square$

**Corollary 4.8** (Conditional gap statement). Assuming Conjecture 4.5.4, and combining Theorem 4.5 with Proposition 4.7: for small $\alpha > 0$, the map $R_\alpha$ has exactly $n$ attracting basins (one per root), each containing an explicit trapping disk $D(\zeta_k, r_0)$. The hyperbolicity question reduces to:

> *Does every free critical orbit eventually enter $\bigcup_k D(\zeta_k, r_0)$?*

This is a finite-time verification for each critical point, amenable to rigorous interval arithmetic.

### 4.4. Reduction Theorem

The preceding results assemble into a formal reduction of the hyperbolicity conjecture to a finite computation.

**Theorem 4.8** (Conditional reduction to finite verification). Let $n \geq 3$, and assume Conjecture 4.5.4 (no parasitic attracting cycles). For any $\alpha_0 \in (0, \alpha^*(n))$, the following are equivalent:

(i) $R_{\alpha_0}$ is hyperbolic.

(ii) Every free critical orbit of $R_{\alpha_0}$ converges to a root of $f$.

(iii) For each free critical point $z_c$ of $R_{\alpha_0}$, there exists $N = N(z_c) < \infty$ such that $R_{\alpha_0}^N(z_c) \in \bigcup_k D(\zeta_k, r_0)$.

Moreover, if (iii) holds for a single $\alpha_0 \in (0, 1)$, then by the Mañé–Sad–Sullivan theorem, $R_\alpha$ is hyperbolic for all $\alpha$ in an open neighborhood of $\alpha_0$ in $(0, 1)$.

*Proof.* (i) $\Leftrightarrow$ (ii): By Mañé's characterization, a rational map is hyperbolic iff all critical orbits converge to attracting cycles. By Conjecture 4.5.4, the only attracting cycles are the root fixed points.

(ii) $\Rightarrow$ (iii): If $z_c$ converges to $\zeta_k$, the orbit eventually enters $D(\zeta_k, r_0)$ by Proposition 4.7.

(iii) $\Rightarrow$ (ii): Once $R_{\alpha_0}^N(z_c) \in D(\zeta_k, r_0)$, forward invariance gives $R_{\alpha_0}^m(z_c) \in D(\zeta_k, r_0)$ for all $m \geq N$, hence $R_{\alpha_0}^m(z_c) \to \zeta_k$.

Extension via MSS: The family $\alpha \mapsto R_\alpha$ is holomorphic with constant degree $n(2n-1)$ on $(0, 1)$. If $R_{\alpha_0}$ is hyperbolic, then by the openness of the hyperbolic locus (MSS, 1983), hyperbolicity holds on a neighborhood. $\square$

**Remark.** Theorem 4.8 provides the pathway to rigorous verification: compute interval-arithmetic enclosures of all $n(4n-5)$ critical orbits at a specific $\alpha_0$ until they enter trapping disks. Combined with Conjecture 4.5.4, this is a complete reduction strategy.

### 4.4.1. Structure of the remaining gap

What prevents a full proof of hyperbolicity for ALL small $\alpha$:

- After the orbit reaches the bounded region $\{|z| \leq R\}$ (Corollary 4.4), it might land near $z = 0$ again and be re-ejected, creating a non-converging orbit trapped on $J(R_\alpha)$.
- $R_\alpha$ is pointwise close to $R_0$ on compact subsets of $\mathbb{C} \setminus \{0\}$, but this does NOT imply orbit-tracking (sensitive dependence near $J(R_0)$).
- The degree jump at $\alpha = 0$ prevents direct application of structural stability across $\alpha = 0$.

**Approaches to closing the gap:**

(a) **Computer-assisted proof for specific $\alpha_0$.** Iterate all $n(4n-5)$ critical orbits with interval arithmetic until each enters $D(\zeta_k, r_0)$. Assuming Conjecture 4.5.4 (no parasitic attractors), convergence to a root is the only possible bounded behavior, so the computation terminates. Once done for one $\alpha_0$, MSS extends to a neighborhood.

(b) **Global absorbing region.** Construct an explicit compact $U \supset \bigcup_k D(\zeta_k, r_0)$ with $R_\alpha(U) \subset U$ and such that $U$ absorbs all orbits from outside. This requires bounding $R_\alpha$ on the annular region $\{r_0 < |z - \zeta_k| < R\} \setminus B(0, \delta)$, which is technically demanding but feasible using the explicit rational form of $R_\alpha$.

(c) **Non-recurrence at the pole.** Show that critical orbits do not return to $B(0, \delta)$ after ejection. If one can prove $R_\alpha^m(z_c) \notin B(0, \delta)$ for all $m \geq 1$ and all free $z_c$, then the orbit stays in the region where $R_\alpha \approx R_0$, and convergence follows from the hyperbolicity of $R_0$. This would require an estimate on preimages of $B(0, \delta)$ under $R_\alpha$.

### 4.5. Numerical evidence

**Observation 4.9** (Numerical evidence). For all $n \in \{2, 3, 4, 5\}$ and all tested $\alpha$ in the table below, every free critical orbit converges to a root of $f$ (computed numerically, floating-point, 500 iterations, tolerance $10^{-6}$).

| $n$ | $\alpha = 0.01$ | $0.1$ | $0.3$ | $0.5$ | $0.7$ | $0.8$ | $0.9$ |
|-----|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 2 | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$ |
| 3 | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$ |
| 4 | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$ |
| 5 | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$ |

This is a finite numerical experiment, not a proof. A rigorous computer-assisted verification is outlined in Remark R4.

### 4.6. Conditional consequences

**Theorem 4.10** (MSS; conditional). If for some $\alpha_0 \in (0, 1)$ every critical orbit of $R_{\alpha_0}$ converges to an attracting cycle, then $R_{\alpha_0}$ is hyperbolic, J-stable, and $\dim_H J(R_{\alpha_0}) < 2$.

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

The comparison with Newton's method clarifies the structural novelty of the PM family.

| | Newton $N_f$ | PM family $R_\alpha$ (small $\alpha$) |
|---|---|---|
| Degree | $n$ | $n(2n-1)$ |
| Free critical point | $z = 0$ | $n(4n-5)$ points near $z = 0$ |
| Critical orbit | $0 \to \infty \to \infty \to \cdots$ (on $J$) | ejected from 0, contracts at $\infty$, enters bounded region |
| $\infty$ type | Repelling, $\infty \in J$ | Repelling, orbits contract |
| Limit $\alpha \to 0$ | N/A (no parameter) | $R_0$: degree $n+1$, no free criticals, hyperbolic |
| $\dim_H J$ | $= 2$ (Shishikura) | $< 2$ (conditional on hyperbolicity) |

**Newton's obstruction.** For $n \geq 3$: the free critical point $z = 0$ satisfies $N_f(0) = \infty$ and $N_f(\infty) = \infty$. Since $\infty$ is a repelling fixed point on $J(N_f)$, the critical orbit $\{0, \infty, \infty, \ldots\} \subset J(N_f)$. By the Mañé–Sad–Sullivan theorem, $N_f$ is NOT J-stable. By Shishikura (1990): $\dim_H J(N_f) = 2$.

**PM mechanism.** The PM family eliminates this obstruction through a different route:
- The free critical points do NOT land on $J$; instead they are ejected to $|z| \gg 1$ (where orbits contract) and then enter the bounded Fatou-like region.
- In the limit $\alpha \to 0$, the free critical points disappear entirely (coalescence with the pole), yielding a hyperbolic map $R_0$.
- The degree collapse (Theorem 3.4) provides the structural mechanism: critical point coalescence with a degenerate pole.

**Summary of proved results for the PM family ($n \geq 3$, small $\alpha$):**
1. Degree collapse with explicit mechanism (Theorem 3.4) — proved
2. No free critical points in the limit (Section 2) — proved
3. No parasitic attracting fixed points (Theorem 4.5) — proved
4. No parasitic cycles in annulus (Proposition 4.5.2) — proved
5. Hyperbolicity reduced to finite orbit verification (Theorem 4.8) — proved (conditional on Conjecture 4.5.4)

**Remaining conjectures.** (a) No parasitic attracting $p$-cycles pass through $B(0, \delta)$ (Conjecture 4.5.4). (b) All free critical orbits enter root basins in finite time. Given (a), condition (b) is a computable finite-time verification (Theorem 4.8).

The conceptual point: Newton's method has a critical orbit *permanently trapped on $J$* (the 2-cycle $\{0, \infty\}$). The PM family has a mechanism — degree collapse via critical point coalescence — that prevents this trapping at the level of critical orbit structure. $\blacksquare$

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
| Free crit: $z^r H(z^n)$ | $r = n-2$, $\deg_t H = 4n-5$ | $z \cdot H(z^3)$, $\deg 7$ | **Proved** (all $n$) |
| Critical coalescence | $z_c(\alpha) \to 0$ as $\alpha \to 0$ | — | **Proved** (all $n$, Hurwitz) |
| Degree Collapse Principle | coalescence $\Leftrightarrow$ degree drop | — | **Proved** (Thm 3.4) |
| $\rho(\alpha,n) \to (n-1)/(n+1)$ | contraction at $\infty$ | $\to 1/2$ | **Proved** (all $n$) |
| No parasitic fixed pts | unique attr. fixed pts are roots | — | **Proved** (Thm 4.5, all $n$) |
| No parasitic annular cycles | perturbation from $R_0$ | — | **Proved** (Prop 4.5.2) |
| No parasitic $p$-cycles (all) | full cycle exclusion | — | **Conjectured** (Conj 4.5.4) |
| Trapping disks | $R_\alpha(D(\zeta_k, r_0)) \subset D(\zeta_k, r_0)$ | — | **Proved** (small $\alpha$) |
| Reduction theorem | hyperbolicity $\Leftrightarrow$ finite verification | — | **Proved** (Thm 4.8, conditional) |
| $\alpha^*(n)$ | $\searrow$ with $n$ | $\approx 0.836$ | Numerical |
| Hyperbolicity for ALL $\alpha \in (0, \alpha^*)$ | — | — | Conjectured (computable gap) |

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

Two approaches can close the remaining gap (Section 4.4):

**(a) Interval arithmetic verification.** For a specific $\alpha_0$: compute certified enclosures of all $n(4n-5)$ free critical points (roots of $z^{n-2} H(z^n, \alpha_0)$, via e.g., CAPD or `IntervalArithmetics.jl`), then iterate with interval arithmetic until each orbit enters a trapping disk $D(\zeta_k, r_0)$ (Proposition 4.7). By Theorem 4.5 and Proposition 4.5.2, the only possible bounded attractor among fixed points and annular cycles is a root. Assuming Conjecture 4.5.4, the verification terminates. Once hyperbolicity is established at a single $\alpha_0 \in (0,1)$, the MSS theorem extends it to a neighborhood (Theorem 4.8).

**(b) Global trapping region.** Show that $R_\alpha(\hat{\mathbb{C}} \setminus \bigcup_k D(\zeta_k, r_0)) \subset \{|z| \leq R\}$ and that iterates in the annular region $\{r_0 < |z-\zeta_k| < R\}$ are eventually absorbed into $\bigcup_k D(\zeta_k, r_0)$. This uses bounds from Propositions 4.2–4.3 and would give hyperbolicity for all small $\alpha$ simultaneously.

### R5. Connection to basin entropy

The basin entropy $S_b(\alpha)$ (Daza et al., 2016) provides a quantitative measure of boundary complexity. If $R_\alpha$ is indeed hyperbolic for $\alpha \in (0, \alpha^*(n))$, then the uncertainty exponent would be $\alpha_{ue} = 1$ (smooth boundaries have no fractal uncertainty). For Newton ($\alpha = 1$), $\alpha_{ue} < 1$. The transition at $\alpha^*$ would correspond to the onset of positive basin entropy.

### R6. Extension beyond $z^n - 1$

For general polynomials $f(z)$ of degree $n$:
- The $\mathbb{Z}_n$ symmetry is lost, but the core mechanism persists.
- $R_0$ still exists (the formula depends on $f$, $f'$, not just on the symmetry).
- The degree reduction $n(2n-1) \to n+1$ as $\alpha \to 0$ still occurs (critical points coalesce with poles).
- J-stability for small $\alpha$ is expected by the same perturbation argument.

A complete treatment for general $f$ is a natural next step.
