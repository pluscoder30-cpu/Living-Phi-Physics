import math

PHI = 1.618033988749895
d_CO2 = 3.3
d_N2 = 3.64

def selectivity_phi(d):
    if d < d_CO2 or d > d_N2:
        return 1.0
    return PHI ** (2 * (d_N2 - d_CO2) / (d_N2 * (1 - 1/PHI)))

def selectivity_std(d):
    if d < d_CO2 or d > d_N2:
        return 1.0
    return (d_N2 / d_CO2) ** 2

diameters = [3.0 + i * 0.1 for i in range(11)]
print("CO₂/N₂ selectivity vs pore diameter:")
print(f"{'d(Å)':>8} {'S_PHI':>8} {'S_std':>8}")
print("-" * 28)
for d in diameters:
    sp = selectivity_phi(d)
    ss = selectivity_std(d)
    print(f"{d:>8.1f} {sp:>8.3f} {ss:>8.3f}")

max_s_phi = max(selectivity_phi(d) for d in diameters)
opt_d = next(d for d in diameters if selectivity_phi(d) == max_s_phi)
max_s_std = max(selectivity_std(d) for d in diameters)

print(f"\nOptimal PHI diameter: {opt_d:.1f} Å")
print(f"Max PHI selectivity: {max_s_phi:.3f}")
print(f"Max std selectivity: {max_s_std:.3f}")
print(f"Improvement: {max_s_phi/max_s_std:.2f}×")
print(f"Expected: φ^2.3 = {PHI**2.3:.3f}")
test = max_s_phi > max_s_std
print(f"Test: {'PASS' if test else 'FAIL'}")
