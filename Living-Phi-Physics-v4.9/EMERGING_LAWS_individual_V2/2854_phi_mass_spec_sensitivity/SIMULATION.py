import math

PHI = 1.618033988749895
Sens0 = 1.0

def transmission_phi(N):
    return PHI ** (N / 3.0)

def transmission_std(N):
    return 1.5 ** N

lenses = [2, 4, 6, 8, 10]
print("Ion optics transmission:")
print(f"{'Lenses':>8} {'T_PHI':>10} {'T_std':>10} {'Ratio':>8}")
print("-" * 38)
for N in lenses:
    tp = transmission_phi(N)
    ts = transmission_std(N)
    print(f"{N:>8} {tp:>10.3f} {ts:>10.3f} {tp/ts:>8.3f}")

print(f"\nPer-lens-pair improvement: φ^(2/3) = {PHI**(2/3):.3f}×")
print(f"Standard per-pair: 1.5² = 2.25×")
test = transmission_phi(6) > transmission_std(6)
print(f"Test: {'PASS' if test else 'FAIL'}")
