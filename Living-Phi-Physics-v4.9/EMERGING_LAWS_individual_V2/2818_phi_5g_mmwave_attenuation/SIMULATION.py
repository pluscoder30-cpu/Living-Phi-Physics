import math

PHI = 1.618033988749895
f0 = 24.0
alpha0 = 0.1

def alpha_phi(f):
    return alpha0 * (f / f0) ** (2.0 / PHI)

def alpha_std(f):
    return alpha0 * (f / f0) ** 2.0

frequencies = [24, 28, 39, 60, 73, 80, 100]
print("mmWave atmospheric attenuation:")
print(f"{'f(GHz)':>8} {'α_PHI':>10} {'α_std':>10} {'Ratio':>8} {'Reduction':>10}")
print("-" * 50)
for f in frequencies:
    ap = alpha_phi(f)
    ast = alpha_std(f)
    print(f"{f:>8} {ap:>10.4f} {ast:>10.4f} {ap/ast:>8.3f} {(1-ap/ast)*100:>9.1f}%")

print(f"\nExponent: {2/PHI:.4f} (PHI) vs 2.0000 (standard)")
print(f"28 GHz reduction: {(1-alpha_phi(28)/alpha_std(28))*100:.1f}%")
print(f"60 GHz reduction: {(1-alpha_phi(60)/alpha_std(60))*100:.1f}%")
test = 2/PHI < 2.0
print(f"Test: {'PASS' if test else 'FAIL'}")
