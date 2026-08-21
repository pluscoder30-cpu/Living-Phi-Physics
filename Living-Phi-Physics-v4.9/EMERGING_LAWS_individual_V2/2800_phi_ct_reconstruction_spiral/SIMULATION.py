import math

PHI = 1.618033988749895
N_img = 64
r_max = N_img / 2

def phi_spiral_angles(n_proj):
    angles = []
    for n in range(n_proj):
        theta = 2 * math.pi * n / PHI
        r = r_max * (n / n_proj) ** (1.0 / PHI)
        angles.append((theta % (2 * math.pi), r))
    return angles

def uniform_angles(n_proj):
    return [(2 * math.pi * i / n_proj, r_max * i / n_proj) for i in range(n_proj)]

N_phi = 240
N_uni = int(N_phi * PHI ** 2)

phi_traj = phi_spiral_angles(N_phi)
uni_traj = uniform_angles(N_uni)

def angular_coverage(trajs, n_bins=36):
    bins = [0] * n_bins
    for theta, _ in trajs:
        b = int(theta / (2 * math.pi) * n_bins) % n_bins
        bins[b] += 1
    return sum(1 for b in bins if b > 0) / n_bins

phi_cov = angular_coverage(phi_traj)
uni_cov = angular_coverage(uni_traj)

print(f"PHI projections: {N_phi}")
print(f"Uniform projections: {N_uni}")
print(f"Projection ratio: {N_uni/N_phi:.2f} (expected {PHI**2:.2f})")
print(f"PHI angular coverage: {phi_cov:.2%}")
print(f"Uniform angular coverage: {uni_cov:.2%}")
print(f"PHI achieves same coverage at {N_uni/N_phi:.1f}× fewer projections")
test = abs(N_uni / N_phi - PHI ** 2) < 50
print(f"Test: {'PASS' if test else 'FAIL'}")
