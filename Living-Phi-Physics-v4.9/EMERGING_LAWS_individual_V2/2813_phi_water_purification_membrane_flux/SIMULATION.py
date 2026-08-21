import math

PHI = 1.618033988749895
J0 = 10.0
dP0 = 1.0

def J_phi(dP):
    return J0 * PHI * (dP / dP0) ** (1.0 / PHI)

def J_linear(dP):
    return J0 * (dP / dP0)

pressures = list(range(1, 21))
print("Membrane flux comparison:")
print(f"{'ΔP(bar)':>8} {'J_PHI':>10} {'J_linear':>10} {'Ratio':>8}")
print("-" * 40)
for dP in pressures:
    jp = J_phi(dP)
    jl = J_linear(dP)
    print(f"{dP:>8} {jp:>10.2f} {jl:>10.2f} {jp/jl:>8.3f}")

crossover = 0
for dP in [i * 0.1 for i in range(1, 200)]:
    if J_phi(dP) > J_linear(dP):
        crossover = dP
        break

print(f"\nCrossover pressure: {crossover:.1f} bar")
print(f"J_PHI at 10 bar: {J_phi(10):.2f} L/m²h")
print(f"J_linear at 10 bar: {J_linear(10):.2f} L/m²h")
print(f"Exponent: {1/PHI:.4f} (expected 1/φ)")
test = 1/PHI > 0.6 and 1/PHI < 0.65
print(f"Test: {'PASS' if test else 'FAIL'}")
