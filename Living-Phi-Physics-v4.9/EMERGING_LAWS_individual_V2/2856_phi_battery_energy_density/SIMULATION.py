import math

PHI = 1.618033988749895
E0 = 1.0

def E_phi(n):
    return E0 * PHI ** (n / 3.0)

def E_std(n):
    return E0 * n / 3.0

layers = [3, 6, 9, 12, 15, 18]
print("Battery energy density:")
print(f"{'Layers':>7} {'E_PHI':>10} {'E_std':>10} {'Improvement':>12}")
print("-" * 42)
for n in layers:
    ep = E_phi(n)
    es = E_std(n)
    imp = (ep / es - 1) * 100
    print(f"{n:>7} {ep:>10.3f} {es:>10.3f} {imp:>11.1f}%")

print(f"\n6-layer: PHI={E_phi(6):.3f}, std={E_std(6):.3f}")
print(f"Improvement: {(E_phi(6)/E_std(6)-1)*100:.1f}%")
test = E_phi(6) > E_std(6)
print(f"Test: {'PASS' if test else 'FAIL'}")
