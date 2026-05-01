"""
Theorem Proof - Step 4: Complete orbit tracking for ALL critical points.

Uses the symbolic expressions with numerical alpha substitution to find
all 28 critical points via polynomial root-finding, then tracks every orbit.
"""
from sympy import *
import numpy as np

z_sym, a_sym = symbols('z a')

# --- Build R_alpha symbolically (reuse from step 3) ---
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

# Critical polynomial
P_prime_sym = P_poly_sym.diff(z_sym)
crit_poly_sym = P_prime_sym * Q_poly_sym - P_poly_sym * Q_poly_sym.diff(z_sym)

print("Symbolic setup complete.")
print(f"P degree = {P_poly_sym.degree()}, Q degree = {Q_poly_sym.degree()}")
print(f"Critical polynomial degree = {crit_poly_sym.degree()}")

# --- Numerical analysis for specific alpha values ---
omega = np.exp(2j * np.pi / 3)
roots_f = np.array([1.0, omega, omega**2])

def compute_R_alpha_numeric(z_val, alpha_val):
    """Compute R_alpha(z) numerically with high precision."""
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

def find_all_critical_points(alpha_val):
    """Find ALL critical points by substituting alpha into the symbolic
    critical polynomial and finding roots numerically."""
    alpha_rat = Rational(alpha_val).limit_denominator(100000)
    crit_poly_num = crit_poly_sym.subs(a_sym, alpha_rat)
    crit_poly_num = Poly(crit_poly_num, z_sym)
    coeffs = crit_poly_num.all_coeffs()
    coeffs_float = [complex(c) for c in coeffs]
    roots = np.roots(coeffs_float)
    return roots

def classify_critical_point(z_val, tol=0.05):
    """Classify: 'root' if near a root of f, 'pole' if near 0, else 'free'."""
    for i, r in enumerate(roots_f):
        if abs(z_val - r) < tol:
            return f"root_{i}"
    if abs(z_val) < tol:
        return "pole_origin"
    return "free"

def track_orbit(z0, alpha_val, max_iter=500, tol=1e-6):
    """Track orbit and determine its fate."""
    z_val = z0
    for n in range(max_iter):
        try:
            z_val = compute_R_alpha_numeric(z_val, alpha_val)
        except (ZeroDivisionError, OverflowError, FloatingPointError):
            return "pole", n

        if not np.isfinite(z_val):
            return "diverges", n
        if abs(z_val) > 1e12:
            return "diverges", n

        # Check convergence to roots
        for i, r in enumerate(roots_f):
            if abs(z_val - r) < tol:
                return f"-> root omega^{i} ({r:.4f})", n

    return f"unclear (z={z_val:.4f}, |z|={abs(z_val):.4f})", max_iter

# --- Main analysis ---
print("\n" + "=" * 70)
print("COMPLETE CRITICAL POINT AND ORBIT ANALYSIS")
print("=" * 70)

test_alphas = [0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 0.99]

for alpha_val in test_alphas:
    print(f"\n{'='*50}")
    print(f"  alpha = {alpha_val}")
    print(f"{'='*50}")

    cps = find_all_critical_points(alpha_val)

    # Classify
    at_roots = []
    at_origin = []
    free = []

    for cp in cps:
        cls = classify_critical_point(cp)
        if cls.startswith("root"):
            at_roots.append(cp)
        elif cls == "pole_origin":
            at_origin.append(cp)
        else:
            free.append(cp)

    print(f"  Total critical points found: {len(cps)}")
    print(f"  At roots of f: {len(at_roots)}")
    print(f"  Near z=0 (pole): {len(at_origin)}")
    print(f"  Free: {len(free)}")

    # Group free critical points by Z3 symmetry
    # z and omega*z and omega^2*z are in the same orbit
    processed = set()
    orbit_groups = []
    for i, cp in enumerate(free):
        if i in processed:
            continue
        group = [cp]
        processed.add(i)
        for j, cp2 in enumerate(free):
            if j in processed:
                continue
            # Check if cp2 = omega^k * cp for some k
            for k in range(1, 3):
                if abs(cp2 - omega**k * cp) < 0.1 * max(abs(cp), 0.01):
                    group.append(cp2)
                    processed.add(j)
                    break
        orbit_groups.append(group)

    print(f"  Free critical points form {len(orbit_groups)} Z3-orbits")

    # Track orbits (one representative per Z3-orbit)
    all_converge = True
    for i, group in enumerate(orbit_groups):
        rep = group[0]
        fate, n_iter = track_orbit(rep, alpha_val)
        converges = "root" in fate
        if not converges:
            all_converge = False
        status = "CONVERGES" if converges else "DOES NOT CONVERGE"
        print(f"  Orbit {i+1}: z={rep:.4f}, |z|={abs(rep):.4f} -> {fate} ({status}, {n_iter} iter)")

    if all_converge:
        print(f"\n  *** ALL free critical orbits CONVERGE to roots for alpha={alpha_val} ***")
    else:
        print(f"\n  *** Some free critical orbits DO NOT converge for alpha={alpha_val} ***")

# --- Summary ---
print("\n" + "=" * 70)
print("MULTIPLIER AT INFINITY")
print("=" * 70)

for alpha_val in [0.01, 0.1, 0.3, 0.5, 0.9]:
    # Compute R_alpha at large z
    z_large = 1e6
    R_large = compute_R_alpha_numeric(z_large, alpha_val)
    mult_inf_approx = R_large / z_large

    # Also via conjugation: R_tilde(w) = 1/R(1/w), R_tilde'(0)
    w_small = 1e-6
    R_at_1overw = compute_R_alpha_numeric(1/w_small, alpha_val)
    R_tilde_w = 1/R_at_1overw if abs(R_at_1overw) > 1e-15 else np.inf
    # R_tilde'(0) ≈ R_tilde(w_small) / w_small
    mult_inf = R_tilde_w / w_small if np.isfinite(R_tilde_w) else np.inf

    print(f"  alpha = {alpha_val}: R(z)/z for z=1e6 ≈ {mult_inf_approx:.6f}, "
          f"|multiplier at inf| ≈ {abs(mult_inf):.6f}")
