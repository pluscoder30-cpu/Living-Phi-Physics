import math

PHI = 1.618033988749895
BW = 20e6
f0 = 30e3
delta_f_std = f0
delta_f_phi = PHI * f0

N_std = int(BW / delta_f_std)
N_phi = int(BW / delta_f_phi)

def ici_power(k, m, delta_f, T):
    x = math.pi * (k - m) * delta_f * T
    if abs(x) < 1e-10:
        return 1.0
    return (math.sin(x) / x) ** 2

T = 1 / delta_f_std

ici_std_total = sum(ici_power(0, m, delta_f_std, T) for m in range(1, min(N_std, 20)))
ici_phi_total = sum(ici_power(0, m, delta_f_phi, T) for m in range(1, min(N_phi, 20)))

print(f"Standard: N={N_std}, delta_f={delta_f_std/1e3:.0f} kHz")
print(f"PHI:      N={N_phi}, delta_f={delta_f_phi/1e3:.1f} kHz")
print(f"Subcarrier reduction: {(1 - N_phi/N_std)*100:.1f}%")
print(f"Expected: 38.2%")
print(f"ICI std sum (first 20): {ici_std_total:.6f}")
print(f"ICI phi sum (first 20): {ici_phi_total:.6f}")
print(f"ICI reduction: {(1 - ici_phi_total/ici_std_total)*100:.1f}%")
print(f"Reduction ~38.2%: {'PASS' if 35 < (1 - N_phi/N_std)*100 < 41 else 'FAIL'}")
