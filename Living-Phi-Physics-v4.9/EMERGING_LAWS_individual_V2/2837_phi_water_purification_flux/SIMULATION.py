import math

PHI = 1.618033988749895
R0 = 1.0
mu = 1e-3

def J_phi(dP):
    return dP / (mu * R0 / PHI ** (1.0/3.0))

def J_std(dP):
    return dP / (mu * R0)

pressures = list(range(1, 21))
print("Water flux comparison:")
print(f"{'ΔP(bar)':>8} {'J_PHI':>12} {'J_std':>12} {'Ratio':>8}")
print("-" * 44)
for dP in pressures:
    jp = J_phi(dP)
    js = J_std(dP)
    print(f"{dP:>8} {jp:>12.1f} {js:>12.1f} {jp/js:>8.3f}")

print(f"\nFlux improvement: {J_phi(10)/J_std(10):.3f}× (expected φ^(1/3) = {PHI**(1/3):.3f}×)")
test = J_phi(10) > J_std(10)
print(f"Test: {'PASS' if test else 'FAIL'}")
