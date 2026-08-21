import math

PHI = 1.618033988749895
ESR0 = 1.0

def ESR_phi(n):
    return ESR0 / PHI ** (n / 3.0)

def ESR_std(n):
    return ESR0 / n if n > 0 else ESR0

print("ESR vs electrode layers:")
print(f"{'Layers':>7} {'ESR_PHI':>10} {'ESR_std':>10} {'Ratio':>8}")
print("-" * 38)
for n in range(1, 7):
    ep = ESR_phi(n)
    es = ESR_std(n)
    print(f"{n:>7} {ep:>10.4f} {es:>10.4f} {ep/es:>8.3f}")

print(f"\n3-layer design:")
print(f"  PHI: {ESR_phi(3):.4f} (expected 1/φ = {1/PHI:.4f})")
print(f"  Standard: {ESR_std(3):.4f} (expected 1/3 = {1/3:.4f})")
print(f"  PHI/Std ratio: {ESR_phi(3)/ESR_std(3):.3f}")
test = abs(ESR_phi(3) - 1/PHI) < 0.001
print(f"Test: {'PASS' if test else 'FAIL'}")
