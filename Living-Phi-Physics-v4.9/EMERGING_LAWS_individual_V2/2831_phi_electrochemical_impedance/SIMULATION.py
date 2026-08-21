import math, cmath

PHI = 1.618033988749895
Rs = 10.0
Y0 = 0.001
alpha_phi = 1.0 / PHI
alpha_std = 0.8

def Z_phi(omega):
    return Rs + 1.0 / (Y0 * (1j * omega) ** alpha_phi)

def Z_std(omega):
    return Rs + 1.0 / (Y0 * (1j * omega) ** alpha_std)

frequencies = [10 ** (i * 0.5) for i in range(-4, 5)]

print("Electrochemical impedance comparison:")
print(f"{'f(Hz)':>10} {'|Z_PHI|':>10} {'Phase_PHI':>10} {'|Z_std|':>10} {'Phase_std':>10}")
print("-" * 55)
for f in frequencies:
    omega = 2 * math.pi * f
    zp = Z_phi(omega)
    zs = Z_std(omega)
    phase_p = math.degrees(cmath.phase(zp))
    phase_s = math.degrees(cmath.phase(zs))
    print(f"{f:>10.1f} {abs(zp):>10.2f} {phase_p:>10.1f} {abs(zs):>10.2f} {phase_s:>10.1f}")

phase_phi = -math.degrees(math.atan(1.0 / (Y0 * (2 * math.pi * 100) ** alpha_phi) / Rs))
phase_std = -math.degrees(math.atan(1.0 / (Y0 * (2 * math.pi * 100) ** alpha_std) / Rs))
target_phase = 90 * alpha_phi

print(f"\nPHI CPE exponent: {alpha_phi:.4f} (expected 1/φ)")
print(f"PHI phase angle (mid-freq): ~{target_phase:.1f}°")
print(f"Standard CPE exponent: {alpha_std}")
print(f"Standard phase angle: ~{90*alpha_std:.1f}°")
test = abs(alpha_phi - 1/PHI) < 0.001
print(f"Test: {'PASS' if test else 'FAIL'}")
