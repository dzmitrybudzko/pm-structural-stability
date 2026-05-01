"""
Theorem Proof - Step 2: Critical points of R_alpha for f(z) = z^3 - 1.

R_alpha has degree 15, so 2*15-2 = 28 critical points.
We need to classify them and track their orbits.
"""
from sympy import *
import numpy as np

z, a = symbols('z a')

print("=" * 70)
print("STEP 5: R_alpha as a rational function of degree 15")
print("=" * 70)

# Build R_alpha
f_z = z**3 - 1
f_prime = 3*z**2
y_expr = cancel(z - a * f_z / f_prime)

b_coeff = (1 + a**2) / (2 * a**2)
c_coeff = (1 + a) / (2 * a**2 * (a - 1))

f_y = cancel(y_expr**3 - 1)

F = f_z
G = f_y
D = f_prime

correction = F**2 * G / (D * (b_coeff * F**2 + c_coeff * G**2))
R_alpha = y_expr - correction

# Cancel and extract numerator/denominator
print("Cancelling R_alpha (this may take a moment)...")
R_cancelled = cancel(R_alpha)
num_R, den_R = fraction(R_cancelled)

# Expand as polynomials in z
num_poly = Poly(expand(num_R), z)
den_poly = Poly(expand(den_R), z)

print(f"deg(numerator) = {num_poly.degree()}")
print(f"deg(denominator) = {den_poly.degree()}")

# Check for common factors
print("\nChecking for common factors in numerator and denominator...")
g = gcd(num_poly, den_poly)
print(f"GCD degree = {g.degree()}")

if g.degree() > 0:
    num_reduced = quo(num_poly, g)
    den_reduced = quo(den_poly, g)
    print(f"After cancellation: deg(num) = {num_reduced.degree()}, deg(den) = {den_reduced.degree()}")
    print(f"True degree of R_alpha = {max(num_reduced.degree(), den_reduced.degree())}")
else:
    print(f"No common factors. True degree of R_alpha = {max(num_poly.degree(), den_poly.degree())}")

print("\n" + "=" * 70)
print("STEP 6: Numerical computation of critical points for specific alpha")
print("=" * 70)

def compute_R_numeric(z_val, alpha_val):
    """Compute R_alpha(z) numerically."""
    f_val = z_val**3 - 1
    fp_val = 3*z_val**2
    y_val = z_val - alpha_val * f_val / fp_val
    fy_val = y_val**3 - 1
    b_val = (1 + alpha_val**2) / (2 * alpha_val**2)
    c_val = (1 + alpha_val) / (2 * alpha_val**2 * (alpha_val - 1))
    W = f_val**2 / (b_val * f_val**2 + c_val * fy_val**2)
    return y_val - W * fy_val / fp_val

def compute_R_deriv_numeric(z_val, alpha_val, h=1e-8):
    """Compute R_alpha'(z) numerically via finite differences."""
    return (compute_R_numeric(z_val + h, alpha_val) - compute_R_numeric(z_val - h, alpha_val)) / (2*h)

# Roots of z^3 - 1
omega = np.exp(2j * np.pi / 3)
roots = [1.0 + 0j, omega, omega**2]

print("\nFor alpha = 0.1:")
alpha_val = 0.1

# Verify roots are superattracting
for k, root in enumerate(roots):
    mult = compute_R_deriv_numeric(root, alpha_val)
    print(f"  R'(omega^{k}) = {mult:.6e} (should be ~0)")

# Check z = 0
z0_val = compute_R_numeric(0.001 + 0.001j, alpha_val)  # near 0
z0_mult = compute_R_deriv_numeric(0.001 + 0.001j, alpha_val)
print(f"  R(~0) = {z0_val:.6f}, R'(~0) = {z0_mult:.4f}")

print("\n" + "=" * 70)
print("STEP 7: Orbit tracking for free critical points")
print("=" * 70)

def find_critical_points_numeric(alpha_val, N=200, R=10):
    """
    Find critical points of R_alpha numerically by finding zeros of R'_alpha.
    Search on a grid in the complex plane.
    """
    from numpy.polynomial import polynomial as P

    # Use a grid search + Newton's method
    critical_pts = []
    h = 1e-7

    # Grid in the complex plane
    for re in np.linspace(-R, R, N):
        for im in np.linspace(-R, R, N):
            z0 = complex(re, im)
            if abs(z0) < 0.01:
                continue
            try:
                Rp = compute_R_deriv_numeric(z0, alpha_val, h)
                if abs(Rp) < 0.1:
                    # Refine with Newton's method on R'
                    zn = z0
                    for _ in range(50):
                        Rp = compute_R_deriv_numeric(zn, alpha_val, h)
                        Rpp = (compute_R_deriv_numeric(zn + h, alpha_val, h) -
                               compute_R_deriv_numeric(zn - h, alpha_val, h)) / (2*h)
                        if abs(Rpp) < 1e-15:
                            break
                        zn = zn - Rp / Rpp
                        if abs(Rp) < 1e-12:
                            break

                    # Check if this is a new critical point
                    Rp_final = compute_R_deriv_numeric(zn, alpha_val, h)
                    if abs(Rp_final) < 1e-8:
                        is_new = True
                        for cp in critical_pts:
                            if abs(zn - cp) < 0.01:
                                is_new = False
                                break
                        if is_new:
                            critical_pts.append(zn)
            except (ZeroDivisionError, OverflowError, ValueError):
                continue

    return critical_pts

def iterate_orbit(z0, alpha_val, n_iter=200):
    """Iterate R_alpha starting from z0."""
    orbit = [z0]
    zn = z0
    for _ in range(n_iter):
        try:
            zn = compute_R_numeric(zn, alpha_val)
            if abs(zn) > 1e10:
                return orbit, "diverges"
            orbit.append(zn)
        except (ZeroDivisionError, OverflowError):
            return orbit, "pole"

    # Check convergence
    final = orbit[-1]
    for root in roots:
        if abs(final - root) < 1e-6:
            return orbit, f"-> root {root:.4f}"

    return orbit, f"unclear (last = {final:.4f})"

# Test for several alpha values
for alpha_val in [0.01, 0.1, 0.3, 0.5, 0.8, 0.99]:
    print(f"\nalpha = {alpha_val}:")

    # Find critical points (coarse grid for speed)
    cps = find_critical_points_numeric(alpha_val, N=50, R=5)

    # Separate trivial (near roots of f) from free
    free_cps = []
    for cp in cps:
        is_root = False
        for root in roots:
            if abs(cp - root) < 0.05:
                is_root = True
                break
        if not is_root:
            free_cps.append(cp)

    print(f"  Found {len(cps)} critical points total, {len(free_cps)} free")

    # Track orbits of free critical points
    for i, cp in enumerate(free_cps[:6]):  # show at most 6
        _, fate = iterate_orbit(cp, alpha_val)
        print(f"  Free CP z = {cp:.4f}: {fate}")

print("\n" + "=" * 70)
print("STEP 8: Special analysis at alpha = 1 (Newton limit)")
print("=" * 70)

# For Newton's method on z^3 - 1:
# N(z) = (2z^3+1)/(3z^2), free critical point z = 0
# Orbit of z = 0: N(0) = 1/(0) -> infinity, but N(z) near 0 is singular

# Let's check orbit of z = 0 under Newton
print("\nNewton's method N(z) = (2z^3+1)/(3z^2) on z^3 - 1:")
print("  z = 0 is a pole of N, so z = 0 maps to infinity")
print("  N(infinity) = infinity (repelling fixed point)")
print("  So the critical orbit 0 -> infinity -> infinity -> ...")
print("  This means the critical orbit is attracted to a repelling fixed point,")
print("  which by MSS theorem means the Julia set is NOT J-stable at alpha = 1.")

# For alpha close to 1 but not 1, check orbit of critical point near 0
print("\nOrbit of z near 0 for alpha close to 1:")
for alpha_val in [0.9, 0.95, 0.99]:
    # Find critical point near 0
    z0 = 0.01 + 0.01j
    _, fate = iterate_orbit(z0, alpha_val, n_iter=500)
    print(f"  alpha = {alpha_val}: orbit of z=0.01+0.01i: {fate}")
