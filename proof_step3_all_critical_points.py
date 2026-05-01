"""
Theorem Proof - Step 3: Complete critical point analysis.

R_alpha has degree 15, so 2*15-2 = 28 critical points.
We compute the critical point polynomial P'Q - PQ' and find ALL roots.
"""
from sympy import *

z, a = symbols('z a')

print("=" * 70)
print("Computing R_alpha symbolically and extracting P(z), Q(z)")
print("=" * 70)

f_z = z**3 - 1
f_prime = 3*z**2

y_expr = ((-a + 3)*z**3 + a) / (3*z**2)

f_y = y_expr**3 - 1
f_y = cancel(f_y)

b_coeff = (1 + a**2) / (2 * a**2)
c_coeff = (1 + a) / (2 * a**2 * (a - 1))

correction = f_z**2 * f_y / (f_prime * (b_coeff * f_z**2 + c_coeff * f_y**2))
R_alpha_expr = y_expr - correction
R_alpha_cancelled = cancel(R_alpha_expr)

num_R, den_R = fraction(R_alpha_cancelled)
print("R_alpha computed. Extracting polynomial coefficients...")

# Expand as polynomials in z
P_poly = Poly(expand(num_R), z)
Q_poly = Poly(expand(den_R), z)
print(f"P(z) has degree {P_poly.degree()}, Q(z) has degree {Q_poly.degree()}")

# Compute the critical point polynomial: P'Q - PQ'
print("\nComputing P'Q - PQ' (critical point polynomial)...")
P_prime = P_poly.diff(z)
Q_prime = Q_poly.diff(z)

crit_poly = P_prime * Q_poly - P_poly * Q_prime
print(f"Critical polynomial has degree {crit_poly.degree()}")

# Factor out (z^3-1)^2
z3m1_sq = Poly((z**3 - 1)**2, z)
quotient, remainder = div(crit_poly, z3m1_sq)
remainder_simplified = remainder.as_expr()
print(f"Remainder after dividing by (z^3-1)^2: {simplify(remainder_simplified)}")

if remainder_simplified == 0 or simplify(remainder_simplified) == 0:
    print("(z^3-1)^2 divides the critical polynomial exactly!")
    free_crit_poly = quotient
    print(f"Free critical polynomial has degree {free_crit_poly.degree()}")
else:
    print("(z^3-1)^2 does NOT divide exactly. Let me check (z^3-1)...")
    z3m1 = Poly(z**3 - 1, z)
    q1, r1 = div(crit_poly, z3m1)
    r1_s = simplify(r1.as_expr())
    print(f"  Remainder after (z^3-1): {r1_s}")
    if r1_s == 0:
        print("  (z^3-1) divides but (z^3-1)^2 does not")
        # Try to understand the multiplicity
        q2, r2 = div(q1, z3m1)
        r2_s = simplify(r2.as_expr())
        print(f"  Remainder after second (z^3-1): {r2_s}")
    free_crit_poly = crit_poly  # fallback

# Extract coefficients of the free critical polynomial as functions of alpha
print("\n" + "=" * 70)
print("Coefficients of free critical polynomial (as functions of alpha)")
print("=" * 70)
if remainder_simplified == 0 or simplify(remainder_simplified) == 0:
    coeffs = free_crit_poly.all_coeffs()
    print(f"Number of coefficients: {len(coeffs)} (degree {free_crit_poly.degree()})")
    for i, c in enumerate(coeffs):
        c_simplified = factor(c)
        print(f"  z^{free_crit_poly.degree()-i}: {c_simplified}")
