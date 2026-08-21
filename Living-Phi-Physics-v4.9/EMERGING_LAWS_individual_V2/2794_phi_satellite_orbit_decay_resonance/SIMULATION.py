import math

PHI = 1.618033988749895
mu = 3.986e14
Re = 6371e3
H = 50e3
rho0 = 3e-11
h0 = 400e3
Cd = 2.2
A_m = 0.01

def decay_rate(h):
    rho = rho0 * math.exp(-(h - h0) / H)
    r = Re + h
    v = math.sqrt(mu / r)
    return 0.5 * rho * v * Cd * A_m

h_min, h_max = 380e3, 420e3
dh = 1e3
altitudes = [h_min + i * dh for i in range(int((h_max - h_min) / dh) + 1)]
decays = [decay_rate(h) for h in altitudes]
mean_decay = sum(decays) / len(decays)

phi_shelves = []
for i, d in enumerate(decays):
    if d < mean_decay / PHI:
        phi_shelves.append(altitudes[i] / 1e3)

print(f"Mean decay rate: {mean_decay:.2e} m/s")
print(f"PHI-shelf threshold: {mean_decay/PHI:.2e} m/s")
print(f"PHI-shelf altitudes (km): {[f'{a:.0f}' for a in phi_shelves]}")
if len(phi_shelves) >= 2:
    spacings = [phi_shelves[i+1] - phi_shelves[i] for i in range(len(phi_shelves)-1)]
    print(f"Spacings: {[f'{s:.0f}' for s in spacings]}")
    avg_spacing = sum(spacings) / len(spacings)
    print(f"Average spacing: {avg_spacing:.1f} km (expected ~12)")
    print(f"Test: {'PASS' if 10 < avg_spacing < 14 else 'FAIL'}")
else:
    print("Insufficient PHI-shelves detected")
    print("Test: FAIL")
