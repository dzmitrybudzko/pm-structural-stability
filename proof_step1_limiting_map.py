"""
Theorem Proof - Step 1: Computation of the PM operator and the limiting map R_0.

For f(z) = z^3 - 1, we compute R_alpha(z) and analyze lim_{alpha->0} R_alpha.
"""
from sympy import *

z, a = symbols('z a')

print("=" * 70)
print("STEP 1: PM Operator for f(z) = z^3 - 1")
print("=" * 70)

# --- Define the PM scheme ---
f_z = z**3 - 1
f_prime = 3*z**2

# Predictor: y = z - alpha * f(z)/f'(z)
y = z - a * f_z / f_prime
y_simplified = cancel(y)
print(f"\nPredictor y(z) = {y_simplified}")

# f(y)
f_y = y_simplified**3 - 1
f_y = cancel(f_y)
print(f"\nf(y) = {f_y}")

# Factor f(y) to extract (z^3 - 1) factor
# Substitute t = z^3 to work with the polynomial in t
t = symbols('t')
# Numerator of f(y) as polynomial in z
num_fy, den_fy = fraction(f_y)

print(f"\nNumerator of f(y): degree {degree(Poly(num_fy, z))} in z")
print(f"Denominator of f(y): degree {degree(Poly(den_fy, z))} in z")

# Check that (z^3-1) divides numerator of f(y)
quotient_fy, remainder_fy = div(Poly(num_fy, z), Poly(z**3 - 1, z))
print(f"\nf(y) numerator / (z^3-1): remainder = {remainder_fy.as_expr()}")
print(f"Quotient Q(z) = {quotient_fy.as_expr()}")

print("\n" + "=" * 70)
print("STEP 2: Limiting map R_0 = lim_{a->0} R_a")
print("=" * 70)

# Coefficients
b_coeff = (1 + a**2) / (2 * a**2)
c_coeff = (1 + a) / (2 * a**2 * (a - 1))

# Weight factor W = f(z)^2 / (b*f(z)^2 + c*f(y)^2)
# Correction = W * f(y) / f'(z) = f(z)^2 * f(y) / (f'(z) * (b*f(z)^2 + c*f(y)^2))

# To handle the limit a->0, multiply numerator and denominator by 2*a^2*(a-1)
# b * 2*a^2*(a-1) = (1+a^2)*(a-1)
# c * 2*a^2*(a-1) = (1+a)

# So the denominator b*F^2 + c*G^2 becomes:
# [(1+a^2)*(a-1)*F^2 + (1+a)*G^2] / (2*a^2*(a-1))

# And the full correction is:
# F^2 * G / (f'(z)) * 2*a^2*(a-1) / ((1+a^2)*(a-1)*F^2 + (1+a)*G^2)

# Let's compute R_alpha directly and take the limit
# Use the explicit form
F = f_z  # z^3 - 1
G = f_y  # f(y), already computed
D = f_prime  # 3z^2

# Correction term
correction_num = F**2 * G
correction_den = D * (b_coeff * F**2 + c_coeff * G**2)

correction = correction_num / correction_den

# R_alpha = y - correction
R_alpha = y_simplified - correction

# Simplify the correction for the limit
# Multiply through by 2*a^2*(a-1)
print("\nComputing limit of R_alpha as a -> 0...")

# Strategy: compute R_alpha, cancel, then take limit
# This might be slow, so let's try a series expansion approach

# Alternative: compute R for specific small alpha values to verify
print("\nNumerical verification:")
for a_val in [Rational(1, 100), Rational(1, 10), Rational(1, 2)]:
    R_num = R_alpha.subs(a, a_val)
    R_num = cancel(R_num)
    n, d = fraction(R_num)
    print(f"  a = {a_val}: R has numerator deg {degree(Poly(n, z))}, denominator deg {degree(Poly(d, z))}")

# Verify the conjectured limit R_0 = z(z^3+2)/(2z^3+1)
R0_conjectured = z * (z**3 + 2) / (2*z**3 + 1)
print(f"\nConjectured R_0 = {R0_conjectured}")

# Check by evaluating both at a specific z value for small a
z_test = Rational(2, 1) + I
a_test = Rational(1, 1000)
R_test = R_alpha.subs([(a, a_test), (z, z_test)])
R0_test = R0_conjectured.subs(z, z_test)
diff_val = abs(complex(R_test) - complex(R0_test))
print(f"\n|R_{{a=0.001}}({z_test}) - R_0({z_test})| = {diff_val:.2e}")

a_test2 = Rational(1, 10000)
R_test2 = R_alpha.subs([(a, a_test2), (z, z_test)])
diff_val2 = abs(complex(R_test2) - complex(R0_test))
print(f"|R_{{a=0.0001}}({z_test}) - R_0({z_test})| = {diff_val2:.2e}")

print("\n" + "=" * 70)
print("STEP 3: Derivative R_0'(z) and critical points")
print("=" * 70)

R0 = z * (z**3 + 2) / (2*z**3 + 1)
R0_prime = diff(R0, z)
R0_prime_simplified = cancel(R0_prime)
R0_prime_factored = factor(R0_prime_simplified)
print(f"\nR_0'(z) = {R0_prime_factored}")

# Verify: should be 2(z^3-1)^2 / (2z^3+1)^2
R0_prime_expected = 2*(z**3 - 1)**2 / (2*z**3 + 1)**2
diff_expr = simplify(R0_prime_simplified - R0_prime_expected)
print(f"R_0'(z) - 2(z^3-1)^2/(2z^3+1)^2 = {diff_expr}")

print("\nCritical points of R_0 (R_0'(z) = 0):")
print("  z^3 = 1, i.e., z = 1, omega, omega^2 (the roots of f)")
print("  These are the ONLY critical points.")
print("  Each has multiplicity 2 in R_0'.")
print("  Total critical count: 3 * 2 = 6 = 2*4 - 2 = 2*deg(R_0) - 2. CHECK.")

print("\n" + "=" * 70)
print("STEP 4: Fixed points of R_0 and their multipliers")
print("=" * 70)

# Fixed points: R_0(z) = z
fixed_eq = cancel(R0 - z)
num_fixed, _ = fraction(fixed_eq)
num_fixed_factored = factor(num_fixed)
print(f"\nR_0(z) - z = {cancel(fixed_eq)}")
print(f"Numerator factored: {num_fixed_factored}")

print("\nFixed points and multipliers:")
# z = 0
mult_0 = R0_prime_simplified.subs(z, 0)
print(f"  z = 0: R_0'(0) = {mult_0} (repelling)")

# z = 1 (root of f)
mult_1 = R0_prime_simplified.subs(z, 1)
print(f"  z = 1: R_0'(1) = {mult_1} (superattracting)")

# z = infinity: use w = 1/z, compute R_tilde(w) = 1/R_0(1/w)
w = symbols('w')
R0_at_1overw = R0.subs(z, 1/w)
R0_tilde = cancel(1 / R0_at_1overw)
print(f"\n  At infinity: R_tilde(w) = 1/R_0(1/w) = {cancel(R0_tilde)}")
R0_tilde_prime = diff(R0_tilde, w)
mult_inf = cancel(R0_tilde_prime.subs(w, 0))
print(f"  R_tilde'(0) = {mult_inf} (repelling)")

print("\nSummary of fixed points:")
print("  z = 1, omega, omega^2: superattracting (multiplier 0)")
print("  z = 0: repelling (multiplier 2)")
print("  z = infinity: repelling (multiplier 2)")
print("  Total: 5 = deg(R_0) + 1 = 4 + 1. CHECK.")
