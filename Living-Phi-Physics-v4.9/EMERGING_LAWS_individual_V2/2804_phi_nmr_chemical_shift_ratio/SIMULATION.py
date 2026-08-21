import math

PHI = 1.618033988749895
deltad0 = 40.0
J0 = 7.0
N = 5

shifts = []
couplings = []
for n in range(N):
    dd = deltad0 / PHI ** n
    shifts.append(dd)
    couplings.append(J0 / PHI ** n)

print("PHI-harmonic NMR chemical shifts and J-couplings:")
print(f"{'n':>3} {'Δδ(ppm)':>10} {'Ratio':>8} {'J(Hz)':>8} {'J Ratio':>8}")
print("-" * 40)
for n in range(N):
    print(f"{n:>3} {shifts[n]:>10.2f} {shifts[n]/deltad0:>8.4f} {couplings[n]:>8.2f} {couplings[n]/J0:>8.4f}")

dd_ratio = shifts[0] / shifts[1]
j_ratio = couplings[0] / couplings[1]
print(f"\nChemical shift ratio (n=0/1): {dd_ratio:.4f} (expected {PHI:.4f})")
print(f"J-coupling ratio (n=0/1): {j_ratio:.4f} (expected {PHI:.4f})")
test = abs(dd_ratio - PHI) < 0.01 and abs(j_ratio - PHI) < 0.01
print(f"Test: {'PASS' if test else 'FAIL'}")
