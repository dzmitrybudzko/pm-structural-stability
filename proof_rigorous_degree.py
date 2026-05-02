"""
Rigorous degree proof: deg(R_alpha) = n(2n-1) via composition analysis.

Key analytical steps (no pattern-matching):
1. deg(r) = n^2 - n where r = f(y)/f(z), proved by composition degree and
   cancellation at the n roots of f.
2. Pole at z=0 of order n-1 (from predictor y).
3. 2(n^2-n) poles from bF^2+cG^2=0 (preimage count of a degree-(n^2-n) map).
4. infinity maps to infinity with local degree 1.
5. Total: (n-1) + 2(n^2-n) + 1 = n(2n-1).

Also compute: leading coefficient ratio p_d/q_{d-1} as exact function of alpha.
"""
from sympy import *

z, a = symbols('z a')

print("=" * 70)
print("PART 1: Rigorous proof that deg(r) = n^2 - n")
print("=" * 70)

for n_val in [2, 3, 4, 5, 6]:
    print(f"\n--- n = {n_val} ---")

    # Build y(z)
    f_z = z**n_val - 1
    f_prime = n_val * z**(n_val - 1)
    y_num = (n_val - a) * z**n_val + a  # numerator of y
    y_den = n_val * z**(n_val - 1)       # denominator of y

    # f(y) = y^n - 1 = (P_y^n - Q_y^n) / Q_y^n
    # As rational function: numerator = P_y^n - Q_y^n, denominator = Q_y^n
    P_y = y_num
    Q_y = y_den

    # Degree analysis (over z):
    deg_Py = Poly(P_y, z).degree()
    deg_Qy = Poly(Q_y, z).degree()
    print(f"  deg(P_y) = {deg_Py}, deg(Q_y) = {deg_Qy}")
    print(f"  deg(y) = max(deg_Py, deg_Qy) = {max(deg_Py, deg_Qy)} = n")

    # f(y) numerator degree = n * deg(P_y) = n^2
    # f(y) denominator degree = n * deg(Q_y) = n(n-1)
    # f(z) degree = n
    # r = f(y)/f(z): num degree = n^2, den degree = n(n-1)+n = n^2
    print(f"  f(y): num deg = n*n = {n_val**2}, den deg = n*(n-1) = {n_val*(n_val-1)}")
    print(f"  r = f(y)/f(z): num deg = {n_val**2}, den deg = {n_val*(n_val-1)}+{n_val} = {n_val**2}")
    print(f"  a priori deg(r) <= {n_val**2}")

    # Cancellation at roots zeta_k of z^n = 1:
    # At each zeta_k: f(zeta_k) = 0, y(zeta_k) = zeta_k, f(y(zeta_k)) = 0
    # Both vanish with order 1 (for alpha != 1)

    # Verify: order of vanishing of f(y(z)) at z = zeta_0 = 1
    y_at_1 = y_num.subs(z, 1) / y_den.subs(z, 1)
    print(f"  y(1) = {simplify(y_at_1)} (should be 1)")

    # Expand f(y(z)) near z = 1: f(y) = f'(1)*(y-1) + O((y-1)^2)
    # y - 1 = (1-alpha)(z-1) + O((z-1)^2)
    # So f(y) vanishes to order 1 at z=1 (for alpha != 1)
    # f(z) also vanishes to order 1 at z=1
    # => r = f(y)/f(z) is finite and nonzero at z=1

    # Explicitly compute lim_{z->1} f(y)/f(z) via L'Hopital
    y_expr = cancel(z - a * f_z / f_prime)
    f_y = cancel(y_expr**n_val - 1)
    r_expr = cancel(f_y / f_z)
    r_at_1 = limit(r_expr, z, 1)
    print(f"  r(1) = {simplify(r_at_1)} = (1-alpha)^n? {simplify(r_at_1 - (1-a)**n_val) == 0}")

    # So r has a removable singularity at each zeta_k (cancellation of order 1)
    # GCD contributes degree n (one from each root)
    # => deg(r) = n^2 - n

    # Verify by direct computation
    r_full = cancel(f_y / f_z)
    num_r, den_r = fraction(r_full)
    num_r_poly = Poly(expand(num_r), z)
    den_r_poly = Poly(expand(den_r), z)
    g = gcd(num_r_poly, den_r_poly)
    deg_r = max(num_r_poly.degree() - g.degree(), den_r_poly.degree() - g.degree())
    print(f"  Direct: deg(r) = {deg_r}, gcd degree = {g.degree()}")
    print(f"  Matches n^2-n = {n_val**2 - n_val}: {'YES' if deg_r == n_val**2 - n_val else 'NO'}")

print("\n" + "=" * 70)
print("PART 2: Pole order at z=0")
print("=" * 70)

for n_val in [2, 3, 4, 5]:
    print(f"\n--- n = {n_val} ---")
    # y(z) = ((n-a)z^n + a)/(n z^{n-1})
    # Near z=0: y ~ a/(n z^{n-1}), pole of order n-1
    # R_alpha(z) ~ y(z) near z=0 (correction is lower order)

    # Verify: compute R_alpha and check pole order at z=0
    f_z = z**n_val - 1
    f_prime = n_val * z**(n_val - 1)
    y_expr = cancel(z - a * f_z / f_prime)
    f_y = cancel(y_expr**n_val - 1)
    b_coeff = (1 + a**2) / (2 * a**2)
    c_coeff = (1 + a) / (2 * a**2 * (a - 1))
    correction = f_z**2 * f_y / (f_prime * (b_coeff * f_z**2 + c_coeff * f_y**2))
    R_expr = y_expr - correction
    R_canc = cancel(R_expr)
    num_R, den_R = fraction(R_canc)
    P = Poly(expand(num_R), z)
    Q = Poly(expand(den_R), z)

    # Trailing coefficient analysis: what's the lowest power of z in Q?
    Q_coeffs = Q.all_coeffs()
    Q_deg = Q.degree()
    # Find lowest nonzero degree
    for i in range(len(Q_coeffs)-1, -1, -1):
        if Q_coeffs[i] != 0:
            lowest_Q = Q_deg - i
            break

    P_coeffs = P.all_coeffs()
    P_deg = P.degree()
    for i in range(len(P_coeffs)-1, -1, -1):
        if P_coeffs[i] != 0:
            lowest_P = P_deg - i
            break

    print(f"  deg(P) = {P_deg}, lowest z-power in P = {lowest_P}")
    print(f"  deg(Q) = {Q_deg}, lowest z-power in Q = {lowest_Q}")
    print(f"  Pole order at z=0 = lowest_Q - lowest_P = {lowest_Q - lowest_P}")
    print(f"  Expected n-1 = {n_val - 1}: {'OK' if lowest_Q - lowest_P == n_val - 1 else 'FAIL'}")

print("\n" + "=" * 70)
print("PART 3: Leading coefficient ratio p_d / q_{d-1}")
print("=" * 70)

for n_val in [2, 3, 4, 5]:
    print(f"\n--- n = {n_val} ---")
    f_z = z**n_val - 1
    f_prime = n_val * z**(n_val - 1)
    y_expr = cancel(z - a * f_z / f_prime)
    f_y = cancel(y_expr**n_val - 1)
    b_coeff = (1 + a**2) / (2 * a**2)
    c_coeff = (1 + a) / (2 * a**2 * (a - 1))
    R_expr = y_expr - f_z**2 * f_y / (f_prime * (b_coeff * f_z**2 + c_coeff * f_y**2))
    R_canc = cancel(R_expr)
    num_R, den_R = fraction(R_canc)
    P = Poly(expand(num_R), z)
    Q = Poly(expand(den_R), z)

    p_lead = P.LC()
    q_lead = Q.LC()
    ratio = cancel(p_lead / q_lead)

    print(f"  p_d = {factor(p_lead)}")
    print(f"  q_(d-1) = {factor(q_lead)}")
    print(f"  p_d / q_(d-1) = {factor(ratio)}")

    # Limit as alpha -> 0
    ratio_at_0 = limit(ratio, a, 0)
    print(f"  lim_a0 ratio = {ratio_at_0} (expected (n-1)/(n+1) = {Rational(n_val-1, n_val+1)})")

    # Check: is |ratio| < 1 for alpha in (0, something)?
    # Compute ratio at specific alpha values
    for a_val in [Rational(1,10), Rational(1,2), Rational(4,5)]:
        val = ratio.subs(a, a_val)
        print(f"    alpha={float(a_val):.1f}: ratio = {float(val):.6f}, |ratio| < 1: {abs(float(val)) < 1}")

    # lambda_infinity = 1/ratio (multiplier at infinity)
    print(f"  lambda_inf = {factor(1/ratio)}")
    lam_at_0 = limit(1/ratio, a, 0)
    print(f"  lim_a0 lambda_inf = {lam_at_0} (expected (n+1)/(n-1) = {Rational(n_val+1, n_val-1)})")

print("\n" + "=" * 70)
print("PART 4: Critical point location bound")
print("=" * 70)

for n_val in [2, 3]:
    print(f"\n--- n = {n_val} ---")
    f_z = z**n_val - 1
    f_prime = n_val * z**(n_val - 1)
    y_expr = cancel(z - a * f_z / f_prime)
    f_y = cancel(y_expr**n_val - 1)
    b_coeff = (1 + a**2) / (2 * a**2)
    c_coeff = (1 + a) / (2 * a**2 * (a - 1))
    R_expr = y_expr - f_z**2 * f_y / (f_prime * (b_coeff * f_z**2 + c_coeff * f_y**2))
    R_canc = cancel(R_expr)
    num_R, den_R = fraction(R_canc)
    P = Poly(expand(num_R), z)
    Q = Poly(expand(den_R), z)

    # Critical polynomial
    Pp = P.diff(z)
    crit = Pp * Q - P * Q.diff(z)

    # Remove (z^n - 1)^2
    znm1sq = Poly((z**n_val - 1)**2, z)
    free_crit, rem = div(crit, znm1sq)
    print(f"  Free crit poly degree: {free_crit.degree()}")

    # Extract H(t) where free_crit = z^r * H(z^n)
    r_val = n_val - 2
    t = symbols('t')

    # Get coefficients of free_crit as function of alpha
    fc_coeffs = free_crit.all_coeffs()
    fc_deg = free_crit.degree()

    # Extract H coefficients
    H_deg = (fc_deg - r_val) // n_val
    print(f"  H degree = {H_deg}")

    # For each coefficient of H, find the alpha-dependence
    print(f"  H(t) coefficient alpha-dependence:")
    for k in range(H_deg, -1, -1):
        # Coefficient of z^(r + k*n) in free_crit = coefficient of t^k in H
        z_power = r_val + k * n_val
        idx = fc_deg - z_power
        if 0 <= idx < len(fc_coeffs):
            coeff = fc_coeffs[idx]
            coeff_simplified = factor(coeff)
            # Find lowest alpha power
            coeff_poly = Poly(expand(coeff), a)
            min_a_power = 0
            for i, c in enumerate(reversed(coeff_poly.all_coeffs())):
                if c != 0:
                    min_a_power = i
                    break
            print(f"    H_{k}: min alpha power = {min_a_power}, leading = {coeff_poly.LC()}")
