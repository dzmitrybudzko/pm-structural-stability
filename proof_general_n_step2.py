"""
Generalization to f(z) = z^n - 1: orbit tracking for n = 2, 3, 4, 5.

For each n, verify that all free critical orbits converge to roots
for alpha in the stable region.
"""
from sympy import *
import numpy as np

z_sym, a_sym = symbols('z a')

def build_pm_system(n_val):
    """Build symbolic R_alpha and critical polynomial for f(z) = z^n - 1."""
    f_z = z_sym**n_val - 1
    f_prime = n_val * z_sym**(n_val - 1)
    y_expr = cancel(z_sym - a_sym * f_z / f_prime)
    f_y = cancel(y_expr**n_val - 1)
    b = (1 + a_sym**2) / (2 * a_sym**2)
    c = (1 + a_sym) / (2 * a_sym**2 * (a_sym - 1))
    corr = f_z**2 * f_y / (f_prime * (b * f_z**2 + c * f_y**2))
    R = y_expr - corr
    R_canc = cancel(R)
    num_R, den_R = fraction(R_canc)
    P = Poly(expand(num_R), z_sym)
    Q = Poly(expand(den_R), z_sym)
    Pp = P.diff(z_sym)
    crit = Pp * Q - P * Q.diff(z_sym)
    return P, Q, crit

def compute_R_numeric(z_val, alpha, n_val):
    """Compute R_alpha(z) for f(z) = z^n - 1."""
    fz = z_val**n_val - 1
    fpz = n_val * z_val**(n_val - 1)
    if abs(fpz) < 1e-30:
        return np.inf
    y = z_val - alpha * fz / fpz
    fy = y**n_val - 1
    b = (1 + alpha**2) / (2 * alpha**2)
    c = (1 + alpha) / (2 * alpha**2 * (alpha - 1))
    denom = b * fz**2 + c * fy**2
    if abs(denom) < 1e-30:
        return np.inf
    W = fz**2 / denom
    return y - W * fy / fpz

def track_orbit(z0, alpha, n_val, max_iter=500, tol=1e-6):
    """Track orbit and check if it converges to a root of z^n - 1."""
    roots = [np.exp(2j * np.pi * k / n_val) for k in range(n_val)]
    z_val = z0
    for it in range(max_iter):
        try:
            z_val = compute_R_numeric(z_val, alpha, n_val)
        except:
            return "pole", it
        if not np.isfinite(z_val) or abs(z_val) > 1e12:
            return "diverges", it
        for k, r in enumerate(roots):
            if abs(z_val - r) < tol:
                return f"root_{k}", it
    return f"unclear(|z|={abs(z_val):.2f})", max_iter

def analyze_n(n_val, alpha_values, crit_poly_sym):
    """Full analysis for a given n."""
    roots_f = [np.exp(2j * np.pi * k / n_val) for k in range(n_val)]

    for alpha_val in alpha_values:
        alpha_rat = Rational(alpha_val).limit_denominator(100000)
        cp = crit_poly_sym.subs(a_sym, alpha_rat)
        cp = Poly(cp, z_sym)
        coeffs = [complex(c) for c in cp.all_coeffs()]
        all_cps = np.roots(coeffs)

        # Classify
        free_cps = []
        for cp_val in all_cps:
            is_trivial = any(abs(cp_val - r) < 0.05 for r in roots_f)
            is_pole = abs(cp_val) < 0.05
            if not is_trivial and not is_pole:
                free_cps.append(cp_val)

        # Group by Z_n symmetry
        omega = np.exp(2j * np.pi / n_val)
        processed = set()
        orbits = []
        for i, cp_val in enumerate(free_cps):
            if i in processed:
                continue
            group = [cp_val]
            processed.add(i)
            for j, cp2 in enumerate(free_cps):
                if j in processed:
                    continue
                for k in range(1, n_val):
                    if abs(cp2 - omega**k * cp_val) < 0.1 * max(abs(cp_val), 0.01):
                        group.append(cp2)
                        processed.add(j)
                        break
            orbits.append(group)

        # Track orbits
        all_converge = True
        orbit_fates = []
        for orb in orbits:
            rep = orb[0]
            fate, n_iter = track_orbit(rep, alpha_val, n_val)
            converges = "root" in fate
            if not converges:
                all_converge = False
            orbit_fates.append((rep, fate, converges, n_iter))

        status = "ALL CONVERGE" if all_converge else "SOME FAIL"
        print(f"  a={alpha_val:6.3f}: {len(all_cps)} CPs, {len(free_cps)} free, "
              f"{len(orbits)} Z{n_val}-orbits -> {status}")

        if not all_converge:
            for rep, fate, conv, nit in orbit_fates:
                if not conv:
                    print(f"         FAILED: z={rep:.4f}, |z|={abs(rep):.4f} -> {fate}")

    return

# ============================================================
# MAIN
# ============================================================

print("Building symbolic systems (this may take a few minutes for n=4,5)...")

systems = {}
for n_val in [2, 3, 4, 5]:
    print(f"\n  Building n = {n_val}...", end="", flush=True)
    P, Q, crit = build_pm_system(n_val)
    systems[n_val] = (P, Q, crit)
    print(f" done (crit poly degree = {crit.degree()})")

alpha_test = [0.01, 0.05, 0.1, 0.3, 0.5, 0.7, 0.8, 0.9, -0.1, -0.5, -1.0]

for n_val in [2, 3, 4, 5]:
    print(f"\n{'='*60}")
    print(f"  n = {n_val}: f(z) = z^{n_val} - 1")
    print(f"  deg(R_alpha) = {n_val*(2*n_val-1)}, deg(R_0) = {n_val+1}")
    print(f"  Free critical polynomial: z^{n_val-2} * H(z^{n_val}), deg H = {4*n_val-5}")
    print(f"  Number of Z{n_val}-orbits of free CPs: {4*n_val-5}")
    print(f"{'='*60}")

    _, _, crit = systems[n_val]
    analyze_n(n_val, alpha_test, crit)

# ============================================================
# BIFURCATION SEARCH for each n
# ============================================================
print(f"\n{'='*60}")
print("BIFURCATION SEARCH: alpha* for each n")
print(f"{'='*60}")

def all_free_converge_general(alpha_val, n_val, crit_poly_sym, max_iter=500, tol=1e-6):
    roots_f = [np.exp(2j * np.pi * k / n_val) for k in range(n_val)]
    alpha_rat = Rational(alpha_val).limit_denominator(100000)
    cp = crit_poly_sym.subs(a_sym, alpha_rat)
    cp = Poly(cp, z_sym)
    coeffs = [complex(c) for c in cp.all_coeffs()]
    all_cps = np.roots(coeffs)

    for cp_val in all_cps:
        is_trivial = any(abs(cp_val - r) < 0.05 for r in roots_f)
        is_pole = abs(cp_val) < 0.05
        if is_trivial or is_pole:
            continue
        fate, _ = track_orbit(cp_val, alpha_val, n_val, max_iter=max_iter)
        if "root" not in fate:
            return False
    return True

for n_val in [2, 3, 4, 5]:
    print(f"\n  n = {n_val}:", end=" ", flush=True)
    _, _, crit = systems[n_val]

    # Quick scan
    lo, hi = 0.5, 0.99
    # First find upper bound where it fails
    found_unstable = False
    for a_test in [0.5, 0.7, 0.8, 0.85, 0.9, 0.95, 0.99]:
        if not all_free_converge_general(a_test, n_val, crit):
            hi = a_test
            found_unstable = True
            break
        lo = a_test

    if not found_unstable:
        print(f"STABLE for all alpha in (0, 0.99)")
        continue

    # Binary search
    for _ in range(20):
        mid = (lo + hi) / 2
        if all_free_converge_general(mid, n_val, crit):
            lo = mid
        else:
            hi = mid

    print(f"alpha* ~ {(lo+hi)/2:.6f}  (interval [{lo:.6f}, {hi:.6f}])")

# ============================================================
# MULTIPLIER AT INFINITY for general n
# ============================================================
print(f"\n{'='*60}")
print("MULTIPLIER AT INFINITY: general formula")
print(f"{'='*60}")

for n_val in [2, 3, 4, 5]:
    P_poly, Q_poly, _ = systems[n_val]
    p_lead = P_poly.LC()
    q_lead = Q_poly.LC()
    print(f"\n  n = {n_val}:")
    print(f"    p_lead = {factor(p_lead)}")
    print(f"    q_lead = {factor(q_lead)}")

    for a_val in [0.1, 0.5, 0.8, 0.9]:
        a_rat = Rational(a_val).limit_denominator(1000)
        ratio = complex(p_lead.subs(a_sym, a_rat)) / complex(q_lead.subs(a_sym, a_rat))
        mult_inf = 1 / ratio if abs(ratio) > 1e-15 else float('inf')
        print(f"    a={a_val}: |R/z|_inf = {abs(ratio):.4f}, |mult_inf| = {abs(mult_inf):.4f} "
              f"({'repelling' if abs(mult_inf) > 1 else 'ATTRACTING'})")
