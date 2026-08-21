import math

PHI = 1.618033988749895
D0 = 10.0
z0 = 100.0
z_phi = z0 / math.log(PHI)

def dose_phi(z):
    return D0 * math.exp(-abs(z) / z_phi) * math.cos(math.pi * z / (PHI * z0)) ** 2

def dose_uniform(z):
    return D0 * math.cos(math.pi * z / z0) ** 2

z_range = [i * 5 for i in range(-20, 21)]

print("CT dose profile comparison:")
print(f"{'z(mm)':>8} {'D_PHI':>10} {'D_uniform':>10} {'Ratio':>8}")
print("-" * 40)
for z in z_range[::4]:
    dp = dose_phi(z)
    du = dose_uniform(z)
    print(f"{z:>8} {dp:>10.3f} {du:>10.3f} {dp/du:>8.3f}")

center_dose_phi = dose_phi(0)
center_dose_uni = dose_uniform(0)
periph_dose_phi = dose_phi(z0)
periph_dose_uni = dose_uniform(z0)

print(f"\nCenter dose: PHI={center_dose_phi:.3f}, uni={center_dose_uni:.3f}")
print(f"Peripheral dose: PHI={periph_dose_phi:.3f}, uni={periph_dose_uni:.3f}")
print(f"Peripheral reduction: {(1-periph_dose_phi/periph_dose_uni)*100:.1f}%")
print(f"Decay length: {z_phi:.1f} mm")
test = periph_dose_phi < periph_dose_uni
print(f"Test: {'PASS' if test else 'FAIL'}")
