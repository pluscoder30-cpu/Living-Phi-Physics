import math

PHI = 1.618033988749895
dnu0 = 0.5
n_phi = 2 * math.pi / PHI

def precision_phi(n_scans):
    return dnu0 / PHI ** (n_scans / n_phi)

def precision_std(n_scans):
    return dnu0 / math.sqrt(n_scans)

scans = [100, 200, 388, 500, 700, 1000]
print("IR wavenumber precision:")
print(f"{'Scans':>8} {'δν_PHI':>10} {'δν_std':>10} {'Ratio':>8}")
print("-" * 38)
for n in scans:
    pp = precision_phi(n)
    ps = precision_std(n)
    print(f"{n:>8} {pp:>10.4f} {ps:>10.4f} {pp/ps:>8.3f}")

print(f"\nn_φ = {n_phi:.1f} scans")
print(f"At 388 scans: PHI={precision_phi(388):.4f}, std={precision_std(388):.4f}")
test = precision_phi(388) > precision_std(388)
print(f"Test: {'PASS' if test else 'FAIL'}")
