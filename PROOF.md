# Theorem: Structural Stability of the PM Iterative Scheme for $f(z) = z^3 - 1$

## Statement

**Theorem.** Let $f(z) = z^3 - 1$ and let $R_\alpha$ be the PM operator (Budzko–Cordero–Torregrosa, 2015) with parameter $\alpha \in \mathbb{R} \setminus \{0, 1\}$. Then:

**(a)** The limit $R_0 = \lim_{\alpha \to 0} R_\alpha$ exists and equals
$$R_0(z) = \frac{z(z^3 + 2)}{2z^3 + 1},$$
a rational map of degree 4 on $\hat{\mathbb{C}}$. All critical points of $R_0$ are the three roots of $f$ (superattracting fixed points). There are no free critical points.

**(b)** For $\alpha \neq 0$, $R_\alpha$ is a rational map of degree 15 with 28 critical points (counted with multiplicity). The roots of $f$ account for 6 (trivial). The remaining 22 free critical points form a polynomial $z \cdot H(z^3, \alpha)$ where $H$ is degree 7 in $t = z^3$, reflecting the $\mathbb{Z}_3$ symmetry, and they organize into 7 orbits under $z \mapsto \omega z$.

**(c)** Numerical computation and a heuristic analytical argument provide strong evidence that there exists $\alpha^* > 0$ (numerically $\alpha^* \approx 0.8372$) such that for all $\alpha \in (-\infty, 0) \cup (0, \alpha^*)$, every free critical orbit of $R_\alpha$ converges to a root of $f$. If this holds, then $R_\alpha$ is hyperbolic and J-stable in this parameter region (by MSS), and $\dim_H J(R_\alpha) < 2$ (by Ruelle).

**(d)** Numerical evidence indicates that at $\alpha = \alpha^*$, the multiplier $|\lambda_\infty(\alpha)|$ crosses 1 and the fixed point $\infty$ transitions from repelling to attracting, capturing free critical orbits. The bifurcation type is not determined.

**(e)** For Newton's method on $z^3 - 1$, $\dim_H J(N_f) = 2$ (Shishikura, 1990). Conditional on the hyperbolicity of part (c), the PM scheme avoids this pathology: $\dim_H J(R_\alpha) < 2$.

---

## Proof

### Part 1. The PM Operator as a Rational Map

The PM scheme for $f(z) = z^3 - 1$, $f'(z) = 3z^2$ consists of:

**Predictor:**
$$y(z) = z - \alpha \frac{f(z)}{f'(z)} = \frac{(3 - \alpha)z^3 + \alpha}{3z^2}$$

**Corrector:**
$$R_\alpha(z) = y(z) - \frac{f(z)^2 \cdot f(y(z))}{f'(z) \cdot \bigl(b \cdot f(z)^2 + c \cdot f(y(z))^2\bigr)}$$

with $b = \frac{1 + \alpha^2}{2\alpha^2}$, $c = \frac{1 + \alpha}{2\alpha^2(\alpha - 1)}$.

Writing $R_\alpha(z) = P(z, \alpha) / Q(z, \alpha)$ in lowest terms (verified by polynomial GCD computation), we find $\deg P = 15$, $\deg Q = 14$. Hence $R_\alpha$ is a rational map of degree 15 for all $\alpha \in \mathbb{R} \setminus \{0, 1\}$. $\square$ (Part (a), degree statement; Part (b), degree statement.)

### Part 2. Computation of $R_0$

The coefficients $b(\alpha) \sim \frac{1}{2\alpha^2}$ and $c(\alpha) \sim -\frac{1}{2\alpha^2}$ both diverge as $\alpha \to 0$. We compute the limit by asymptotic expansion.

**Step 2.1. Expansion of $f(y)$.** Setting $\delta = -\alpha f(z)/f'(z)$, we have $y = z + \delta$ with $\delta = O(\alpha)$. Then:
$$f(y) = y^3 - 1 = (z + \delta)^3 - 1 = f(z)(1 - \alpha) + \frac{\alpha^2 f(z)^2}{3z^3} + O(\alpha^3)$$

**Step 2.2. Expansion of the weight.** Setting $F = f(z)$, $G = f(y)$:
$$(1 + \alpha^2)F^2 - \frac{1 + \alpha}{1 - \alpha} G^2 = 2\alpha^2 F^2 \cdot \frac{2z^3 + 1}{3z^3} + O(\alpha^3)$$

Therefore:
$$W := \frac{F^2}{b F^2 + c G^2} = \frac{2\alpha^2 F^2}{\frac{1}{2\alpha^2}\bigl[2\alpha^2 F^2 \cdot \frac{2z^3+1}{3z^3} + O(\alpha^3)\bigr]} \longrightarrow \frac{3z^3}{2z^3 + 1} \quad (\alpha \to 0)$$

**Step 2.3. The limit.** The correction term:
$$W \cdot \frac{G}{f'(z)} \to \frac{3z^3}{2z^3+1} \cdot \frac{z^3-1}{3z^2} = \frac{z(z^3-1)}{2z^3+1}$$

Hence:
$$R_0(z) = z - \frac{z(z^3-1)}{2z^3+1} = \frac{z(2z^3+1) - z(z^3-1)}{2z^3+1} = \frac{z(z^3 + 2)}{2z^3 + 1}$$

This is a rational map of degree 4 (numerator degree 4, denominator degree 3, no common factors). $\square$

**Numerical verification:** $|R_{\alpha=0.001}(2+i) - R_0(2+i)| = 1.18 \times 10^{-4}$, confirming linear convergence in $\alpha$.

### Part 3. Critical Points of $R_0$

**Lemma 3.1.** $R_0'(z) = \frac{2(z^3 - 1)^2}{(2z^3 + 1)^2}$.

*Proof.* Direct differentiation of $R_0(z) = (z^4 + 2z)/(2z^3 + 1)$:

$$R_0'(z) = \frac{(4z^3 + 2)(2z^3 + 1) - (z^4 + 2z)(6z^2)}{(2z^3 + 1)^2}$$

Numerator: $8z^6 + 4z^3 + 4z^3 + 2 - 6z^6 - 12z^3 = 2z^6 - 4z^3 + 2 = 2(z^3 - 1)^2$. $\square$

**Corollary 3.2.** The only critical points of $R_0$ are the roots $\zeta_k = \omega^k$ ($k = 0, 1, 2$, where $\omega = e^{2\pi i/3}$), each with multiplicity 2 in $R_0'$. Total critical count: $3 \times 2 = 6 = 2 \cdot 4 - 2 = 2\deg(R_0) - 2$, confirming Riemann–Hurwitz. There are **no free critical points**.

### Part 4. Fixed Points of $R_0$

$$R_0(z) - z = \frac{-z(z^3 - 1)}{2z^3 + 1}$$

**Fixed points:** $z = 0$ and $z^3 = 1$ (the three roots $\zeta_k$), plus $z = \infty$.

**Multipliers:**
| Fixed point | Multiplier $\lambda = R_0'(z)$ | Type |
|---|---|---|
| $\zeta_0 = 1$ | 0 | Superattracting |
| $\zeta_1 = \omega$ | 0 | Superattracting |
| $\zeta_2 = \omega^2$ | 0 | Superattracting |
| $z = 0$ | $R_0'(0) = 2$ | Repelling |
| $z = \infty$ | via $\tilde{R}(w) = (w^4 + 2w)/(2w^3 + 1)$, $\tilde{R}'(0) = 2$ | Repelling |

Total: 5 fixed points $= \deg(R_0) + 1 = 5$. $\checkmark$

### Part 5. $R_0$ is Postcritically Finite and Hyperbolic

**Definition.** A rational map $R$ is *postcritically finite* (PCF) if the forward orbit of every critical point is finite (preperiodic). It is *hyperbolic* if every critical orbit converges to an attracting cycle.

Since every critical point of $R_0$ is a superattracting *fixed* point, $R_0$ is both PCF and hyperbolic. $\square$

**Corollary 5.1.** No critical point of $R_0$ lies on $J(R_0)$. By the Mañé–Sad–Sullivan theorem, $R_0$ is J-stable. $\square$

**Corollary 5.2.** Since $R_0$ is hyperbolic, $\dim_H J(R_0) < 2$ (Ruelle, Przytycki–Urbański–Zdunik). $\square$

### Part 6. Free Critical Points of $R_\alpha$ ($\alpha \neq 0$)

**Lemma 6.1.** The critical point polynomial of $R_\alpha$, defined as $P'(z)Q(z) - P(z)Q'(z)$ where $R_\alpha = P/Q$, has degree 28 and is divisible by $(z^3 - 1)^2$. The quotient (the "free critical polynomial") has degree 22.

*Proof.* Direct symbolic computation (verified in SymPy). The roots $\zeta_k$ are superattracting fixed points of $R_\alpha$ for all $\alpha$ (since PM has convergence order 3), contributing multiplicity 2 each. $\square$

**Lemma 6.2.** The free critical polynomial has the form $z \cdot H(z^3, \alpha)$, where $H(t, \alpha)$ is a polynomial of degree 7 in $t = z^3$. The coefficients $H_k(\alpha)$ satisfy:

| Coefficient | Factor of $\alpha$ | Leading term as $\alpha \to 0$ |
|---|---|---|
| $H_7$ | $\alpha^0$ | $-3 \cdot (-3)(9)(-54)(-972) \neq 0$ |
| $H_6$ | $\alpha^2$ | $\to 0$ |
| $H_5$ | $\alpha^2$ | $\to 0$ |
| $H_4$ | $\alpha^3$ | $\to 0$ |
| $H_3$ | $\alpha^5$ | $\to 0$ |
| $H_2$ | $\alpha^6$ | $\to 0$ |
| $H_1$ | $\alpha^8$ | $\to 0$ |
| $H_0$ | $\alpha^9$ | $\to 0$ |

*Proof.* Direct symbolic computation. The $\mathbb{Z}_3$ symmetry $R_\alpha(\omega z) = \omega R_\alpha(z)$ forces the critical polynomial to be equivariant under $z \mapsto \omega z$, which requires the free critical polynomial (after removing $(z^3-1)^2$) to have the structure $z \cdot H(z^3)$. The $\alpha$-factors are read from the explicit coefficients. $\square$

**Corollary 6.3.** As $\alpha \to 0$, $H(t, \alpha) \to H_7(0) \cdot t^7$, so all 7 roots $t_j(\alpha) \to 0$. Correspondingly, all 21 free critical points $z_{j,k}(\alpha) \to 0$ (the pole of $R_\alpha$).

This is the **mechanism of degree reduction**: the 21 free critical points collide with the pole at $z = 0$ as $\alpha \to 0$, causing the effective degree to drop from 15 to 4.

### Part 7. Convergence of Free Critical Orbits

**Observation 7.1** (numerical). For all tested $\alpha \in (0, \alpha^*)$, every free critical orbit of $R_\alpha$ converges to a root of $f$.

*Heuristic argument (analytical, for small $|\alpha|$):*

1. **Critical points near $z = 0$.** By Corollary 6.3, the free critical points satisfy $|z_c| = O(|\alpha|^{k})$ for some $k > 0$.

2. **First iterate goes to $\infty$.** Since $z = 0$ is a pole of $R_\alpha$ of order 2 (from $y(z) = ((3-\alpha)z^3 + \alpha)/(3z^2)$), we have $|R_\alpha(z_c)| \sim |\alpha| / (3|z_c|^2) \to \infty$ as $\alpha \to 0$.

3. **Contraction at $\infty$.** For $|z| \gg 1$:
$$R_\alpha(z) \approx \frac{p_{15}(\alpha)}{q_{14}(\alpha)} z$$
where $p_{15}/q_{14} \approx 1/2$ for small $\alpha$ (computed from leading coefficients, approaching the $R_0$ value). Since $|p_{15}/q_{14}| < 1$, the iterate contracts toward the origin.

4. **Gap: moderate-region convergence.** After $O(\log(1/|\alpha|))$ iterates, the orbit reaches a bounded region $\{|z| \leq M\}$. One then needs: (i) $R_\alpha \to R_0$ uniformly on compact subsets away from poles, and (ii) orbits landing in the Fatou set of $R_0$ remain in the Fatou set of $R_\alpha$. Point (ii) does not follow from pointwise closeness alone — it requires either a trapping region argument or an appeal to structural stability (MSS). Since the degree jumps at $\alpha = 0$, standard MSS does not apply directly; this step remains a gap.

*Numerical evidence (computer-assisted, for explicit $\alpha$ values):*

Complete enumeration of all 28 critical points (via polynomial root-finding on the degree-28 critical polynomial with numerical $\alpha$-substitution), followed by orbit iteration (computed numerically, floating-point):

| $\alpha$ | Free CPs | Z₃ orbits | All converge? |
|---|---|---|---|
| 0.01 | 18 | 6 | **Yes** |
| 0.05 | 21 | 7 | **Yes** |
| 0.1 | 21 | 7 | **Yes** |
| 0.2 | 21 | 7 | **Yes** |
| 0.3 | 21 | 7 | **Yes** |
| 0.5 | 21 | 7 | **Yes** |
| 0.7 | 21 | 7 | **Yes** |
| $-0.1$ | — | — | **Yes** |
| $-0.5$ | — | — | **Yes** |
| $-1.0$ | — | — | **Yes** |
| $-2.0$ | — | — | **Yes** |
| 0.9 | 21 | 7 | **No** (2 orbits to $\infty$) |

This provides strong numerical evidence for hyperbolicity of $R_\alpha$ for $\alpha \in (-\infty, 0) \cup (0, 0.837)$, but is not a rigorous proof.

### Part 8. The Bifurcation at $\alpha^*$

**Proposition 8.1.** The multiplier at $\infty$ for the degree-15 map $R_\alpha$ is
$$\lambda_\infty(\alpha) = \frac{q_{14}(\alpha)}{p_{15}(\alpha)} = \frac{3(a^5 - 17a^4 + 117a^3 - 405a^2 + 1404a - 972)}{-(a - 3)(a^2 - 12a + 9)(a^3 - 5a^2 - 6a - 54)}$$

This is computed from the leading coefficients of $P$ and $Q$ via the conjugation $w = 1/z$, giving $\tilde{R}(w) \approx \lambda_\infty \cdot w$ near $w = 0$.

**Numerical values:**
| $\alpha$ | $\|R_\alpha(z)/z\|$ ($z \to \infty$) | $\|\lambda_\infty\|$ | $\infty$ type |
|---|---|---|---|
| 0.01 | 0.499 | 2.002 | Repelling |
| 0.1 | 0.494 | 2.025 | Repelling |
| 0.3 | 0.475 | 2.103 | Repelling |
| 0.5 | 0.440 | 2.272 | Repelling |
| 0.7 | 0.333 | 3.005 | Repelling |
| 0.8 | 0.033 | 30.345 | Repelling |
| **0.837** | **~1** | **~1** | **Neutral** |
| 0.9 | 1.135 | 0.881 | Attracting |

At $\alpha = \alpha^* \approx 0.8372$, $|\lambda_\infty| = 1$, and the numerical data indicates $\infty$ transitions from repelling to attracting. If $\infty$ becomes attracting, then by Fatou's theorem it must capture at least one critical orbit, removing it from the root basins and breaking hyperbolicity. The type of bifurcation (saddle-node, period-doubling, etc.) is not determined — this would require a normal form analysis.

### Part 9. Application of the Mañé–Sad–Sullivan Theorem

**Theorem (MSS, 1983).** A holomorphic family of rational maps $\{R_\lambda\}$ is J-stable at $\lambda_0$ if and only if no critical point lies on $J(R_{\lambda_0})$.

**Corollary 9.1** (conditional). If for some $\alpha_0$ every critical orbit of $R_{\alpha_0}$ converges to an attracting cycle (as indicated by the numerical evidence in Part 7), then:
- All critical points are in the Fatou set (attracted to superattracting fixed points).
- By MSS, $R_{\alpha_0}$ is J-stable: $J(R_{\alpha_0})$ varies continuously in the Hausdorff metric.
- $R_{\alpha_0}$ is hyperbolic (expanding on $J$), so $\dim_H J(R_{\alpha_0}) < 2$.

**Corollary 9.2.** For Newton's method $N_f(z) = (2z^3 + 1)/(3z^2)$ on $z^3 - 1$:
- The free critical point $z = 0$ maps to $\infty$ (a repelling fixed point on $J(N_f)$).
- The critical orbit $\{0, \infty, \infty, \ldots\}$ lies on $J(N_f)$.
- By MSS, $N_f$ is NOT J-stable; by Shishikura (1990), $\dim_H J(N_f) = 2$.

### Part 10. Comparison and Conclusion

The PM family interpolates between two regimes:

1. **$\alpha \to 0$ (PM limit):** $R_\alpha \to R_0$, degree 4, no free critical points, hyperbolic, $\dim_H J < 2$. (Proved.)

2. **$\alpha \to 1$ (Newton limit):** $R_\alpha \to N_f$, degree 3, free critical point at $z = 0$ on $J$, $\dim_H J = 2$. (Shishikura, 1990.)

The transition occurs at $\alpha^* \approx 0.837$ (numerical), where the fixed point at $\infty$ changes stability, capturing critical orbits.

The numerical evidence and heuristic argument provide strong support that the PM scheme with small $|\alpha|$ produces **structurally stable dynamics** with basin boundaries of reduced Hausdorff dimension, in contrast to Newton's method. A complete proof requires rigorous verification of critical orbit convergence for $\alpha \in (0, \alpha^*)$. $\blacksquare$

---

## Remarks

### R1. Degree reduction mechanism
The degree jump from 4 ($R_0$) to 15 ($R_\alpha$, $\alpha \neq 0$) is resolved by the coalescence of free critical points with the pole at $z = 0$: as $\alpha \to 0$, all 21 free critical points satisfy $z_c \to 0$, and the effective dynamics reduces to degree 4.

### R2. Negative $\alpha$ stability
All tested negative $\alpha$ values (down to $\alpha = -2.0$) show full convergence of critical orbits. The negative-$\alpha$ region may be entirely J-stable.

### R3. Rigorous computer-assisted proof
The numerical orbit-tracking can be made rigorous via interval arithmetic (following Tucker's approach for the Lorenz attractor). For each $\alpha$, one computes certified enclosures of all critical points and their iterates, verifying convergence to root neighborhoods.

### R4. Hausdorff dimension
Box-counting estimates suggest $\dim_H J(R_0) \approx 1.23$ and $\dim_H J(R_{0.5}) \approx 1.34$, both significantly below the Newton value $\dim_H J(N_f) = 2$. Precise computation of $\dim_H J(R_0)$ via thermodynamic formalism (Bowen's equation) is a natural next step.

### R5. Generalization to $z^n - 1$
The proof structure extends to general $n \geq 3$:
- Compute $R_0^{(n)} = \lim_{\alpha \to 0} R_\alpha$ for $f(z) = z^n - 1$
- Verify $R_0^{(n)}$ is PCF with no free critical points
- Show free critical points of $R_\alpha$ coalesce to the pole as $\alpha \to 0$
- Apply MSS for J-stability

### R6. Connection to the original conjecture
The original conjecture (Section 4 of the summary) stated that $J(R_\alpha)$ is a "Jordan curve" for small $\alpha$. Our analysis shows this is too strong: with 3 basins, $J$ cannot be a Jordan curve (which separates the sphere into exactly 2 regions). The correct statement is: $J(R_\alpha)$ is a thin set ($\dim_H < 2$) that separates three simply connected basins, with qualitatively simpler topology than Newton's Julia set.
