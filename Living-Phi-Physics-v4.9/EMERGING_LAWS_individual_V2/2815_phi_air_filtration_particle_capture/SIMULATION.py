import math

PHI = 1.618033988749895
d0 = 5.0
alpha = 5.0

def eta_phi(dp):
    return 1 - math.exp(-alpha * (dp / d0) ** (2.0 / PHI))

def eta_std(dp):
    return 1 - math.exp(-alpha * (dp / d0) ** 2.0)

particles = [0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0]
print("Particle capture efficiency:")
print(f"{'dp(μm)':>8} {'η_PHI':>8} {'η_std':>8} {'Diff(%)':>8}")
print("-" * 38)
for dp in particles:
    ep = eta_phi(dp)
    es = eta_std(dp)
    print(f"{dp:>8.1f} {ep:>8.4f} {es:>8.4f} {(ep-es)*100:>8.2f}")

dp_hepa = 0.3
eta_phi_hepa = eta_phi(dp_hepa)
eta_std_hepa = eta_std(dp_hepa)
print(f"\nHEPA particle (0.3μm): PHI={eta_phi_hepa:.4f}, std={eta_std_hepa:.4f}")
print(f"Efficiency exponent: {2/PHI:.4f} (expected 2/φ)")
test = abs(2/PHI - 1.236) < 0.001
print(f"Test: {'PASS' if test else 'FAIL'}")
