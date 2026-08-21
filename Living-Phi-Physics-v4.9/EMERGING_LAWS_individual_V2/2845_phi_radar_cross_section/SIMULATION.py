import math, cmath

PHI = 1.618033988749895
N = 10
d0 = 1.0

def RCS_phi(theta):
    total = 0+0j
    for n in range(N):
        total += PHI ** (-n) * cmath.exp(1j * 2 * math.pi * d0 * n * math.sin(theta))
    return abs(total) ** 2

def RCS_std(theta):
    total = 0+0j
    for n in range(N):
        total += cmath.exp(1j * 2 * math.pi * d0 * n * math.sin(theta))
    return abs(total) ** 2 / N

angles = [i * 5 for i in range(-18, 19)]
print("RCS pattern comparison:")
print(f"{'θ(°)':>6} {'RCS_PHI':>10} {'RCS_std':>10} {'Ratio':>8}")
print("-" * 38)
for a in angles[::3]:
    rp = RCS_phi(math.radians(a))
    rs = RCS_std(math.radians(a))
    print(f"{a:>6} {rp:>10.3f} {rs:>10.3f} {rp/rs:>8.3f}")

rcs_0_phi = RCS_phi(0)
rcs_0_std = RCS_std(0)
print(f"\nBroadside RCS: PHI={rcs_0_phi:.3f}, std={rcs_0_std:.3f}")
print(f"Enhancement: {rcs_0_phi/rcs_0_std:.2f}x (expected φ²={PHI**2:.2f}x)")
test = rcs_0_phi > rcs_0_std
print(f"Test: {'PASS' if test else 'FAIL'}")
