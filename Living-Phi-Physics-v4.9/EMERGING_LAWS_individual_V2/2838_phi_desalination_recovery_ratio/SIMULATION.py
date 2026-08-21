import math

PHI = 1.618033988749895
R0_base = 0.3

def recovery_phi(E):
    R0 = R0_base * (1 - math.exp(-E / 3.0))
    return 1 - (1 - R0) / PHI

def recovery_std(E):
    return R0_base * (1 - math.exp(-E / 3.0))

energies = [1, 2, 3, 5, 8, 10]
print("Desalination recovery ratio:")
print(f"{'E(kWh/m³)':>12} {'R_PHI':>8} {'R_std':>8} {'Improvement':>12}")
print("-" * 44)
for E in energies:
    rp = recovery_phi(E)
    rs = recovery_std(E)
    imp = (rp - rs) / rs * 100 if rs > 0 else 0
    print(f"{E:>12} {rp:>8.4f} {rs:>8.4f} {imp:>11.1f}%")

rp = recovery_phi(5)
rs = recovery_std(5)
print(f"\nAt 5 kWh/m³:")
print(f"  PHI: {rp:.4f}")
print(f"  Standard: {rs:.4f}")
print(f"  Improvement: {(rp/rs-1)*100:.1f}%")
test = rp > rs
print(f"Test: {'PASS' if test else 'FAIL'}")
