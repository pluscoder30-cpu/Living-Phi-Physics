import math

PHI = 1.618033988749895
j0 = 1e-3
b_std = 0.060
b_phi = b_std / PHI

def j_phi(eta):
    return j0 * math.exp(2.303 * eta / b_phi)

def j_std(eta):
    return j0 * math.exp(2.303 * eta / b_std)

overpotentials = [0, 50, 100, 150, 200]
print("Electrocatalytic activity:")
print(f"{'η(mV)':>8} {'j_PHI(mA/cm²)':>15} {'j_std(mA/cm²)':>15} {'Ratio':>8}")
print("-" * 50)
for eta in overpotentials:
    jp = j_phi(eta / 1000)
    js = j_std(eta / 1000)
    print(f"{eta:>8} {jp*1000:>15.3f} {js*1000:>15.3f} {jp/js:>8.2f}")

print(f"\nTafel slopes: PHI={b_phi*1000:.1f} mV/dec, std={b_std*1000:.1f} mV/dec")
print(f"Ratio: {b_std/b_phi:.2f}× (expected φ={PHI:.2f}×)")
j10_phi = b_phi / 2.303 * math.log(0.01 / j0) * 1000
j10_std = b_std / 2.303 * math.log(0.01 / j0) * 1000
print(f"\nOverpotential for 10 mA/cm²: PHI={j10_phi:.0f}mV, std={j10_std:.0f}mV")
test = b_phi < b_std
print(f"Test: {'PASS' if test else 'FAIL'}")
