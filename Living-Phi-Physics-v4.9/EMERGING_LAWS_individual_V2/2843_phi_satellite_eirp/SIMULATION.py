import math

PHI = 1.618033988749895
P_tx = 10.0
G0 = 100.0
theta_phi = 5.0

def EIRP_phi(theta):
    return P_tx * G0 * PHI ** (-abs(theta) / theta_phi)

def EIRP_std(theta):
    return P_tx * G0 * math.exp(-theta ** 2 / (2 * theta_phi ** 2))

angles = [0, 2, 5, 8, 10, 15, 20]
print("Satellite EIRP pattern:")
print(f"{'θ(°)':>6} {'EIRP_PHI(W)':>12} {'EIRP_std(W)':>12} {'Ratio(dB)':>10}")
print("-" * 44)
for a in angles:
    ep = EIRP_phi(a)
    es = EIRP_std(a)
    ratio = 10 * math.log10(ep / es) if es > 0 else 0
    print(f"{a:>6} {ep:>12.2f} {es:>12.2f} {ratio:>10.2f}")

print(f"\nMain beam EIRP: PHI={EIRP_phi(0):.2f}W, std={EIRP_std(0):.2f}W")
print(f"Ratio: {EIRP_phi(0)/EIRP_std(0):.2f} (expected {PHI:.2f})")
off_axis = 10
print(f"\nOff-axis at {off_axis}°: PHI={EIRP_phi(off_axis):.2f}W, std={EIRP_std(off_axis):.2f}W")
print(f"Suppression: {10*math.log10(EIRP_phi(off_axis)/EIRP_std(off_axis)):.1f} dB")
test = EIRP_phi(0) > EIRP_std(0)
print(f"Test: {'PASS' if test else 'FAIL'}")
