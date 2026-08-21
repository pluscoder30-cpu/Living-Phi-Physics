import math

PHI = 1.618033988749895
Rs0 = 1.0

def Rs_phi(alpha):
    return Rs0 * PHI ** (alpha - 1)

def Rs_std(alpha):
    return Rs0 * alpha

alphas = [1.0, 1.1, 1.2, 1.5, 2.0]
print("Chromatographic resolution:")
print(f"{'α':>6} {'Rs_PHI':>10} {'Rs_std':>10} {'Ratio':>8}")
print("-" * 38)
for a in alphas:
    rp = Rs_phi(a)
    rs = Rs_std(a)
    print(f"{a:>6.1f} {rp:>10.4f} {rs:>10.4f} {rp/rs:>8.3f}")

print(f"\nAt α=1.2: PHI={Rs_phi(1.2):.4f}, std={Rs_std(1.2):.4f}")
print(f"PHI/Std ratio: {Rs_phi(1.2)/Rs_std(1.2):.3f}")
test = Rs_phi(1.2) > Rs0
print(f"Test: {'PASS' if test else 'FAIL'}")
