"""
Theorem Proof - Step 6: Hausdorff dimension estimation of J(R_alpha).

Uses the box-counting method to estimate dim_H(J) for R_0 and R_alpha.
"""
import numpy as np

omega = np.exp(2j * np.pi / 3)
roots_f = np.array([1.0, omega, omega**2])

def R0(z):
    """R_0(z) = z(z^3+2)/(2z^3+1)"""
    return z * (z**3 + 2) / (2*z**3 + 1)

def R_alpha(z, alpha):
    """PM operator R_alpha(z) for f(z) = z^3 - 1."""
    fz = z**3 - 1
    fpz = 3*z**2
    if abs(fpz) < 1e-30:
        return np.inf
    y = z - alpha * fz / fpz
    fy = y**3 - 1
    b = (1 + alpha**2) / (2 * alpha**2)
    c = (1 + alpha) / (2 * alpha**2 * (alpha - 1))
    denom = b * fz**2 + c * fy**2
    if abs(denom) < 1e-30:
        return np.inf
    W = fz**2 / denom
    return y - W * fy / fpz

def newton(z):
    """Newton's method for z^3 - 1."""
    return z - (z**3 - 1) / (3*z**2)

def classify_point(z0, method, alpha=None, max_iter=200, tol=1e-4):
    """Iterate z0 and classify which root it converges to (0,1,2) or -1 if unclear."""
    z = z0
    for _ in range(max_iter):
        try:
            if method == 'R0':
                z = R0(z)
            elif method == 'newton':
                z = newton(z)
            else:
                z = R_alpha(z, alpha)
        except:
            return -1
        if not np.isfinite(z) or abs(z) > 1e10:
            return -1
        for i, r in enumerate(roots_f):
            if abs(z - r) < tol:
                return i
    return -1

def estimate_hausdorff_box_counting(method, alpha=None, sizes=None, region=3.0, max_iter=200):
    """
    Estimate Hausdorff dimension via box-counting on basin boundaries.

    For each grid resolution N, count how many boxes contain points from
    different basins (i.e., are on the boundary).
    """
    if sizes is None:
        sizes = [100, 200, 400, 800, 1600]

    results = []

    for N in sizes:
        # Create grid
        x = np.linspace(-region, region, N)
        y = np.linspace(-region, region, N)

        # Classify each grid point
        grid = np.zeros((N, N), dtype=int)
        for i in range(N):
            for j in range(N):
                z0 = x[i] + 1j * y[j]
                grid[i, j] = classify_point(z0, method, alpha, max_iter=max_iter)

        # Count boundary boxes: a box is on the boundary if any of its
        # 4 neighbors has a different basin classification
        boundary_count = 0
        for i in range(1, N-1):
            for j in range(1, N-1):
                val = grid[i, j]
                neighbors = [grid[i-1,j], grid[i+1,j], grid[i,j-1], grid[i,j+1]]
                if any(n != val for n in neighbors):
                    boundary_count += 1

        box_size = 2 * region / N
        results.append((box_size, boundary_count))

    return results

def compute_dimension(results):
    """Compute dimension from box-counting data using linear regression."""
    log_eps = np.array([np.log(r[0]) for r in results])
    log_N = np.array([np.log(r[1]) for r in results])

    # dim = -slope of log(N) vs log(eps)
    coeffs = np.polyfit(log_eps, log_N, 1)
    return -coeffs[0], coeffs[1]

print("=" * 70)
print("HAUSDORFF DIMENSION ESTIMATION (box-counting)")
print("=" * 70)

# R_0
print("\n--- R_0 = z(z^3+2)/(2z^3+1) ---")
sizes_R0 = [50, 100, 200, 400, 800]
results_R0 = estimate_hausdorff_box_counting('R0', sizes=sizes_R0)
dim_R0, _ = compute_dimension(results_R0)
print(f"Box-counting results:")
for eps, N in results_R0:
    print(f"  eps = {eps:.6f}, N(eps) = {N}")
print(f"Estimated dim_H(J(R_0)) = {dim_R0:.4f}")

# Newton
print("\n--- Newton's method (z^3-1) ---")
results_newton = estimate_hausdorff_box_counting('newton', sizes=sizes_R0)
dim_newton, _ = compute_dimension(results_newton)
print(f"Box-counting results:")
for eps, N in results_newton:
    print(f"  eps = {eps:.6f}, N(eps) = {N}")
print(f"Estimated dim_H(J(Newton)) = {dim_newton:.4f}")

# R_alpha for various alpha
for alpha_val in [0.01, 0.1, 0.3, 0.5, 0.7]:
    print(f"\n--- R_alpha, alpha = {alpha_val} ---")
    results_Ra = estimate_hausdorff_box_counting('pm', alpha=alpha_val, sizes=[50, 100, 200, 400])
    dim_Ra, _ = compute_dimension(results_Ra)
    print(f"Box-counting results:")
    for eps, N in results_Ra:
        print(f"  eps = {eps:.6f}, N(eps) = {N}")
    print(f"Estimated dim_H(J(R_{alpha_val})) = {dim_Ra:.4f}")

print("\n" + "=" * 70)
print("COMPARISON")
print("=" * 70)
print(f"  Newton:     dim_H(J) ~ {dim_newton:.4f}  (theory: = 2.0, Shishikura)")
print(f"  R_0:        dim_H(J) ~ {dim_R0:.4f}")
print(f"  Expected: dim_H(J(R_alpha)) << dim_H(J(Newton)) for small alpha")
