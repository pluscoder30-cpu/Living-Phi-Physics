import math

PHI = 1.618033988749895
C0 = 1.0

def C_phi(n):
    return C0 * (1 - PHI ** (-n)) / (1 - 1.0 / PHI)

def C_std(n):
    return C0 * (1 - 0.5 ** n) / 0.5

print("Hydrogen storage capacity:")
print(f"{'Phases':>7} {'C_PHI':>10} {'C_std':>10} {'Improvement':>12}")
print("-" * 42)
for n in range(1, 7):
    cp = C_phi(n)
    cs = C_std(n)
    imp = (cp / cs - 1) * 100
    print(f"{n:>7} {cp:>10.3f} {cs:>10.3f} {imp:>11.1f}%")

print(f"\nMax capacity: C_0 * phi/(phi-1) = {C0 * PHI / (PHI - 1):.3f}")
print(f"4-phase: PHI={C_phi(4):.3f}, std={C_std(4):.3f}")
test = C_phi(4) > C_std(4)
print(f"Test: {'PASS' if test else 'FAIL'}")
