"""
Generalization to f(z) = z^n - 1, arbitrary n >= 2.

Step 1: Verify the general formula for R_0 and R_0', compute degrees of R_alpha.
"""
from sympy import *

z, a, n_sym = symbols('z a n', positive=True)

print("=" * 70)
print("PART 1: General formula for R_0")
print("=" * 70)

# R_0(z) = z * ((n-1)*z^n + (n+1)) / ((n+1)*z^n + (n-1))
# Verify R_0'(z) = (n^2-1)*(z^n-1)^2 / ((n+1)*z^n + (n-1))^2

for n_val in [2, 3, 4, 5, 6, 10]:
    P = z * ((n_val - 1)*z**n_val + (n_val + 1))
    Q = (n_val + 1)*z**n_val + (n_val - 1)
    R0 = P / Q
    R0_prime = diff(R0, z)
    R0_prime_simplified = cancel(R0_prime)

    # Expected
    expected = (n_val**2 - 1) * (z**n_val - 1)**2 / ((n_val+1)*z**n_val + (n_val-1))**2

    diff_check = simplify(R0_prime_simplified - expected)
    print(f"  n = {n_val}: R_0 degree = {n_val+1}, R_0' = (n^2-1)(z^n-1)^2/(...): "
          f"{'VERIFIED' if diff_check == 0 else 'FAILED'}")

    # Fixed points
    fp_expr = cancel(R0 - z)
    fp_num, _ = fraction(fp_expr)
    fp_factored = factor(fp_num)
    print(f"    R_0(z)-z numerator = {fp_factored}")

    # Multiplier at z=0
    mult_0 = R0_prime_simplified.subs(z, 0)
    mult_0_expected = Rational(n_val + 1, n_val - 1)
    print(f"    Multiplier at z=0: {mult_0} (expected {mult_0_expected}): "
          f"{'OK' if simplify(mult_0 - mult_0_expected) == 0 else 'FAIL'}")

    # Multiplier at infinity via w = 1/z
    w = symbols('w')
    R0_tilde = cancel(1 / R0.subs(z, 1/w))
    R0_tilde_prime = diff(R0_tilde, w)
    mult_inf = cancel(R0_tilde_prime.subs(w, 0))
    print(f"    Multiplier at inf: {mult_inf} (expected {mult_0_expected}): "
          f"{'OK' if simplify(mult_inf - mult_0_expected) == 0 else 'FAIL'}")

print("\n" + "=" * 70)
print("PART 2: Degree of R_alpha for various n")
print("=" * 70)

for n_val in [2, 3, 4, 5]:
    print(f"\n--- n = {n_val}, f(z) = z^{n_val} - 1 ---")

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

    num_poly = Poly(expand(num_R), z)
    den_poly = Poly(expand(den_R), z)

    deg_num = num_poly.degree()
    deg_den = den_poly.degree()

    # Check GCD
    g = gcd(num_poly, den_poly)
    g_deg = g.degree()

    true_deg = max(deg_num - g_deg, deg_den - g_deg)

    print(f"  deg(P) = {deg_num}, deg(Q) = {deg_den}, gcd deg = {g_deg}")
    print(f"  True degree of R_alpha = {true_deg}")
    print(f"  Formula n(n+2) = {n_val*(n_val+2)}, n^2+2n = {n_val**2+2*n_val}")
    print(f"  Match: {'YES' if true_deg == n_val*(n_val+2) else 'NO'}")

    # Critical polynomial
    print(f"  Computing critical polynomial P'Q - PQ'...")
    if g_deg > 0:
        num_r = quo(num_poly, g)
        den_r = quo(den_poly, g)
    else:
        num_r = num_poly
        den_r = den_poly

    num_r_prime = num_r.diff(z)
    crit_poly = num_r_prime * den_r - num_r * den_r.diff(z)
    print(f"  Critical polynomial degree: {crit_poly.degree()}")
    print(f"  Expected 2*deg-2 = {2*true_deg - 2}")

    # Factor out (z^n - 1)^2
    zn_m1_sq = Poly((z**n_val - 1)**2, z)
    q_crit, r_crit = div(crit_poly, zn_m1_sq)
    r_check = simplify(r_crit.as_expr())
    print(f"  (z^n-1)^2 divides critical poly: {'YES' if r_check == 0 else 'NO'}")
    if r_check == 0:
        free_deg = q_crit.degree()
        print(f"  Free critical polynomial degree: {free_deg}")
        print(f"  Free critical points: {free_deg} (= 2*deg - 2 - 2*n = {2*true_deg-2-2*n_val})")

        # Check Z_n symmetry: free crit poly should be z * H(z^n)
        # or a polynomial in z^n times some z^k
        coeffs = q_crit.all_coeffs()
        degrees_with_nonzero = []
        for i, c in enumerate(coeffs):
            if c != 0:
                deg_i = free_deg - i
                degrees_with_nonzero.append(deg_i)

        # Check if all degrees are congruent mod n
        residues = set(d % n_val for d in degrees_with_nonzero)
        print(f"  Non-zero coefficient degrees mod {n_val}: {residues}")
        if len(residues) == 1:
            r = residues.pop()
            print(f"  Structure: z^{r} * H(z^{n_val}) -- confirmed Z_{n_val} symmetry")
