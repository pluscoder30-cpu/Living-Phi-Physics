import math

PHI = 1.618033988749895
MERV0 = 8

def MERV_phi(n):
    return MERV0 + 10 * math.log10(PHI) * n

def MERV_std(n):
    return MERV0 + 3 * n

print("MERV rating vs filter layers:")
print(f"{'Layers':>7} {'MERV_PHI':>10} {'MERV_std':>10} {'Diff':>8}")
print("-" * 38)
for n in range(1, 6):
    mp = MERV_phi(n)
    ms = MERV_std(n)
    print(f"{n:>7} {mp:>10.1f} {ms:>10.1f} {ms-mp:>8.1f}")

print(f"\nPer-layer MERV increase:")
print(f"  PHI: {10*math.log10(PHI):.2f} points")
print(f"  Standard: 3.00 points")
print(f"  3-layer: PHI={MERV_phi(3):.1f}, std={MERV_std(3):.1f}")
test = abs(10 * math.log10(PHI) - 2.1) < 0.1
print(f"Test: {'PASS' if test else 'FAIL'}")
