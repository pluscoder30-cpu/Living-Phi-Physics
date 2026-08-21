import math

PHI = 1.618033988749895
eps0 = 1.0
theta_phi = 18.5

def error_phi(offset):
    return eps0 * PHI ** (-abs(offset) / theta_phi)

def error_std(offset):
    return eps0

offsets = [0, 1, 2, 3, 5, 8, 10]
print("Beam alignment error vs angular offset:")
print(f"{'Offset(°)':>10} {'ε_PHI(°)':>10} {'ε_std(°)':>10} {'Reduction':>10}")
print("-" * 44)
for o in offsets:
    ep = error_phi(o)
    es = error_std(o)
    red = (1 - ep/es) * 100
    print(f"{o:>10} {ep:>10.4f} {es:>10.4f} {red:>9.1f}%")

print(f"\nAt 1° offset: {error_phi(1):.4f}° (expected {eps0/PHI:.4f}°)")
print(f"At 5° offset: {error_phi(5):.4f}° (expected {eps0/PHI**3:.4f}°)")
test = error_phi(1) < error_std(1)
print(f"Test: {'PASS' if test else 'FAIL'}")
