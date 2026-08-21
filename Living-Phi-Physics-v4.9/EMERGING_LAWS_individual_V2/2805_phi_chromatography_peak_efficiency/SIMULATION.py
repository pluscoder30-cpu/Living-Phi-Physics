import math

PHI = 1.618033988749895
A = 5.0
B = 0.1
C = 2.0
L = 100e3

def van_deemter_std(u):
    return A / u + B * u + C * u

def van_deemter_phi(u):
    return A / u + B * u + C * u / PHI

velocities = [i * 0.05 for i in range(1, 100)]

H_std = [van_deemter_std(u) for u in velocities]
H_phi = [van_deemter_phi(u) for u in velocities]

u_opt_std = velocities[H_std.index(min(H_std))]
u_opt_phi = velocities[H_phi.index(min(H_phi))]
H_min_std = min(H_std)
H_min_phi = min(H_phi)

N_std = L / H_min_std
N_phi = L / H_min_phi

print(f"Standard: u_opt = {u_opt_std:.2f} mm/s, H_min = {H_min_std:.2f} μm")
print(f"PHI:      u_opt = {u_opt_phi:.2f} mm/s, H_min = {H_min_phi:.2f} μm")
print(f"Velocity ratio: {u_opt_phi/u_opt_std:.4f} (expected {PHI:.4f})")
print(f"Plate height ratio: {H_min_std/H_min_phi:.4f} (expected {PHI:.4f})")
print(f"N_std = {N_std:.0f}, N_phi = {N_phi:.0f}")
print(f"N improvement: {N_phi/N_std:.2f}x (expected {PHI:.2f}x)")
test = abs(u_opt_phi / u_opt_std - PHI) < 0.1 and abs(H_min_std / H_min_phi - PHI) < 0.1
print(f"Test: {'PASS' if test else 'FAIL'}")
