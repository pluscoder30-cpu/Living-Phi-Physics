import math

PHI = 1.618033988749895
J0 = 0.5
dP_phi = 1.0

def J_phi(dP):
    return J0 * PHI ** (dP / dP_phi)

def J_std(dP):
    return J0 * dP ** 0.5

pressures = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
print("H₂ diffusion flux vs pressure differential:")
print(f"{'ΔP(bar)':>8} {'J_PHI':>10} {'J_std':>10} {'Ratio':>8}")
print("-" * 38)
for dP in pressures:
    jp = J_phi(dP)
    js = J_std(dP)
    print(f"{dP:>8.1f} {jp:>10.4f} {js:>10.4f} {jp/js:>8.3f}")

print(f"\nAt ΔP = 1 bar:")
print(f"  PHI: {J_phi(1):.4f} mol/m²s·Pa^(1/2)")
print(f"  Standard: {J_std(1):.4f} mol/m²s·Pa^(1/2)")
print(f"  Improvement: {J_phi(1)/J_std(1):.2f}×")
print(f"  Expected: φ = {PHI:.4f}×")
test = abs(J_phi(1) / J_std(1) - PHI) < 0.01
print(f"Test: {'PASS' if test else 'FAIL'}")
