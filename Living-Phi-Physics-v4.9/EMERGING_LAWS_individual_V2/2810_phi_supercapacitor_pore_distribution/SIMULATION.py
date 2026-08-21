import math

PHI = 1.618033988749895
d_min, d_max = 1.0, 50.0
N_pores = 5
exponent = -1.0 / PHI

diameters = [d_min * PHI ** i for i in range(N_pores)]
diameters = [d for d in diameters if d <= d_max]

def phi_distribution(d):
    return d ** exponent

def uniform_distribution(d):
    return 1.0

def surface_area(d, n):
    return n * 4 * math.pi * (d / 2) ** 2

def mobility(d):
    return d ** 2

phi_weights = [phi_distribution(d) for d in diameters]
uni_weights = [uniform_distribution(d) for d in diameters]

phi_total = sum(phi_weights)
uni_total = sum(uni_weights)

phi_n = [w / phi_total * 1000 for w in phi_weights]
uni_n = [w / uni_total * 1000 for w in uni_weights]

phi_sa = sum(surface_area(d, n) for d, n in zip(diameters, phi_n))
uni_sa = sum(surface_area(d, n) for d, n in zip(diameters, uni_n))

phi_access = sum(n * mobility(d) for d, n in zip(diameters, phi_n))
uni_access = sum(n * mobility(d) for d, n in zip(diameters, uni_n))

print("PHI-harmonic pore distribution:")
for d, w, n in zip(diameters, phi_weights, phi_n):
    print(f"  d={d:.1f}nm: weight={w:.3f}, count={n:.0f}")
print(f"\nUniform pore distribution:")
for d, w, n in zip(diameters, uni_weights, uni_n):
    print(f"  d={d:.1f}nm: weight={w:.3f}, count={n:.0f}")

print(f"\nPHI total SA: {phi_sa:.0f}")
print(f"Uniform total SA: {uni_sa:.0f}")
print(f"PHI ion accessibility: {phi_access:.0f}")
print(f"Uniform ion accessibility: {uni_access:.0f}")
print(f"SA ratio: {phi_sa/uni_sa:.2f}")
print(f"Accessibility ratio: {phi_access/uni_access:.2f}")
print(f"Exponent used: {exponent:.4f} (expected -1/φ = {-1/PHI:.4f})")
test = abs(exponent - (-1/PHI)) < 0.001
print(f"Test: {'PASS' if test else 'FAIL'}")
