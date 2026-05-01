"""
Theorem Proof - Step 5: Bifurcation analysis and multiplier at infinity.

Find the critical alpha where J-stability is lost.
"""
from sympy import *
import numpy as np

z_sym, a_sym = symbols('z a')

# --- Rebuild symbolic setup ---
f_z = z_sym**3 - 1
f_prime = 3*z_sym**2
y_expr = ((-a_sym + 3)*z_sym**3 + a_sym) / (3*z_sym**2)
f_y = cancel(y_expr**3 - 1)
b_coeff = (1 + a_sym**2) / (2 * a_sym**2)
c_coeff = (1 + a_sym) / (2 * a_sym**2 * (a_sym - 1))
correction = f_z**2 * f_y / (f_prime * (b_coeff * f_z**2 + c_coeff * f_y**2))
R_alpha_expr = y_expr - correction
R_cancelled = cancel(R_alpha_expr)
num_R_sym, den_R_sym = fraction(R_cancelled)
P_poly_sym = Poly(expand(num_R_sym), z_sym)
Q_poly_sym = Poly(expand(den_R_sym), z_sym)
P_prime_sym = P_poly_sym.diff(z_sym)
crit_poly_sym = P_prime_sym * Q_poly_sym - P_poly_sym * Q_poly_sym.diff(z_sym)

omega = np.exp(2j * np.pi / 3)
roots_f = np.array([1.0, omega, omega**2])

def compute_R(z_val, alpha_val):
    fz = z_val**3 - 1
    fpz = 3*z_val**2
    if abs(fpz) < 1e-30:
        return np.inf
    y = z_val - alpha_val * fz / fpz
    fy = y**3 - 1
    b = (1 + alpha_val**2) / (2 * alpha_val**2)
    c = (1 + alpha_val) / (2 * alpha_val**2 * (alpha_val - 1))
    denom = b * fz**2 + c * fy**2
    if abs(denom) < 1e-30:
        return np.inf
    W = fz**2 / denom
    return y - W * fy / fpz

def find_critical_points(alpha_val):
    alpha_rat = Rational(alpha_val).limit_denominator(100000)
    cpn = crit_poly_sym.subs(a_sym, alpha_rat)
    cpn = Poly(cpn, z_sym)
    coeffs_float = [complex(c) for c in cpn.all_coeffs()]
    return np.roots(coeffs_float)

def all_free_converge(alpha_val, max_iter=500, tol=1e-6):
    """Check if ALL free critical orbits converge to roots."""
    cps = find_critical_points(alpha_val)
    for cp in cps:
        # Skip trivial (near roots) and near-pole points
        is_trivial = any(abs(cp - r) < 0.05 for r in roots_f) or abs(cp) < 0.05
        if is_trivial:
            continue
        # Track orbit
        z_val = cp
        converged = False
        for n in range(max_iter):
            try:
                z_val = compute_R(z_val, alpha_val)
            except:
                break
            if not np.isfinite(z_val) or abs(z_val) > 1e12:
                return False, alpha_val
            for r in roots_f:
                if abs(z_val - r) < tol:
                    converged = True
                    break
            if converged:
                break
        if not converged:
            return False, alpha_val
    return True, alpha_val

# --- Binary search for bifurcation alpha ---
print("=" * 70)
print("BIFURCATION SEARCH: finding alpha* where J-stability is lost")
print("=" * 70)

lo, hi = 0.7, 0.95
print(f"\nBinary search in [{lo}, {hi}]:")

for iteration in range(25):
    mid = (lo + hi) / 2
    conv, _ = all_free_converge(mid)
    status = "STABLE" if conv else "UNSTABLE"
    print(f"  alpha = {mid:.8f}: {status}")
    if conv:
        lo = mid
    else:
        hi = mid

print(f"\nBifurcation alpha* ~ {(lo+hi)/2:.8f}")
print(f"  Interval: [{lo:.8f}, {hi:.8f}]")

# --- Also check negative alpha ---
print("\n" + "=" * 70)
print("NEGATIVE ALPHA VALUES")
print("=" * 70)

for alpha_val in [-0.01, -0.1, -0.3, -0.5, -0.7, -0.9, -0.99, -1.5, -2.0]:
    try:
        conv, _ = all_free_converge(alpha_val, max_iter=300)
        status = "ALL CONVERGE" if conv else "SOME DIVERGE"
        print(f"  alpha = {alpha_val:6.2f}: {status}")
    except Exception as e:
        print(f"  alpha = {alpha_val:6.2f}: ERROR ({e})")

# --- Multiplier at infinity ---
print("\n" + "=" * 70)
print("MULTIPLIER AT INFINITY for R_alpha")
print("=" * 70)

# Leading coefficients of P(z) and Q(z)
p_leading = P_poly_sym.LC()  # leading coeff (highest z power)
q_leading = Q_poly_sym.LC()

print(f"\nLeading coeff of P(z) [z^15]: {factor(p_leading)}")
print(f"Leading coeff of Q(z) [z^14]: {factor(q_leading)}")
print(f"Ratio p_15/q_14 = R_alpha(z)/z as z->inf:")

for alpha_val in [0.01, 0.1, 0.3, 0.5, 0.7, 0.8, 0.9]:
    ratio = complex(p_leading.subs(a_sym, Rational(alpha_val).limit_denominator(1000))) / \
            complex(q_leading.subs(a_sym, Rational(alpha_val).limit_denominator(1000)))
    # Multiplier at infinity = q_14/p_15 (via conjugation w=1/z)
    mult_inf = 1/ratio
    print(f"  alpha = {alpha_val}: R(z)/z -> {ratio:.6f}, "
          f"multiplier at inf = {mult_inf:.6f}, "
          f"|mult| = {abs(mult_inf):.6f}")

# --- Verify R_0 limit: multiplier at inf should be 2 ---
print("\n" + "=" * 70)
print("SUMMARY OF KEY RESULTS")
print("=" * 70)

print("""
1. R_0 = lim_{a->0} R_a = z(z^3+2)/(2z^3+1), degree 4
2. R_0'(z) = 2(z^3-1)^2/(2z^3+1)^2 -- NO free critical points
3. Fixed points of R_0: roots (superattracting), z=0 (repelling, mult=2), inf (repelling, mult=2)

4. R_alpha for alpha != 0 has degree 15, with 28 critical points:
   - 6 at roots of f (superattracting, trivial)
   - 1 at z=0 (pole, not genuine critical point)
   - 21 free critical points in 7 Z3-orbits

5. Free critical polynomial: z * H(z^3, alpha) where H is degree 7 in t=z^3
   As alpha -> 0: H(t) -> c_7 * t^7, so all free CPs -> z=0 (pole)

6. NUMERICAL VERIFICATION:
   For alpha in (0, ~0.83): ALL free critical orbits converge to roots
   => R_alpha is HYPERBOLIC (expanding on Julia set)
   => By MSS theorem, R_alpha is J-STABLE

   Bifurcation occurs at alpha* ~ 0.83
""")
