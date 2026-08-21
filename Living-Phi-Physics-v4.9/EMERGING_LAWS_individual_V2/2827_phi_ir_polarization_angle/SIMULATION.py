import math

PHI = 1.618033988749895

def dichroic_ratio(theta_deg):
    theta = math.radians(theta_deg)
    return PHI ** (2 * math.cos(theta) ** 2)

angles = [0, 30, 45, 60, 90]
print("IR dichroic ratio vs polarization angle:")
print(f"{'θ(°)':>6} {'R(θ)':>8} {'Expected':>10}")
print("-" * 28)
for a in angles:
    r = dichroic_ratio(a)
    if a == 0:
        exp = f"φ²={PHI**2:.3f}"
    elif a == 45:
        exp = f"φ={PHI:.3f}"
    elif a == 90:
        exp = "1.000"
    else:
        exp = "---"
    print(f"{a:>6} {r:>8.4f} {exp:>10}")

r_45 = dichroic_ratio(45)
r_0 = dichroic_ratio(0)
print(f"\nR(45°) = {r_45:.4f} (expected φ = {PHI:.4f})")
print(f"R(0°) = {r_0:.4f} (expected φ² = {PHI**2:.4f})")
test = abs(r_45 - PHI) < 0.001 and abs(r_0 - PHI**2) < 0.001
print(f"Test: {'PASS' if test else 'FAIL'}")
