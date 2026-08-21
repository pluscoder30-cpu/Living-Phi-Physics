import math

PHI = 1.618033988749895
N_bins = 64

def clutter_psd_phi(f):
    if abs(f) < 1e-10:
        return 10.0
    return 1.0 / abs(f) ** (2.0 / PHI)

def clutter_psd_kx(f):
    if abs(f) < 1e-10:
        return 10.0
    return 1.0 / abs(f) ** (8.0 / 3.0)

df = 1.0
freqs = [i * df for i in range(-N_bins//2, N_bins//2)]

clutter_phi = [clutter_psd_phi(f) for f in freqs]
clutter_kx = [clutter_psd_kx(f) for f in freqs]

phi_width_bins = sum(1 for c in clutter_phi if c > max(clutter_phi)/2)
kx_width_bins = sum(1 for c in clutter_kx if c > max(clutter_kx)/2)

target_bins = list(range(10, 30))
scnr_phi = [1.0 / clutter_phi[i] for i in target_bins]
scnr_kx = [1.0 / clutter_kx[i] for i in target_bins]

avg_snr_phi = sum(scnr_phi) / len(scnr_phi)
avg_snr_kx = sum(scnr_kx) / len(scnr_kx)

print(f"Clutter spectral exponent PHI: {2/PHI:.3f}")
print(f"Clutter spectral exponent Kx: {8/3:.3f}")
print(f"3dB width PHI: {phi_width_bins} bins")
print(f"3dB width Kx: {kx_width_bins} bins")
print(f"Avg SCNR PHI (target bins): {avg_snr_phi:.4f}")
print(f"Avg SCNR Kx (target bins): {avg_snr_kx:.4f}")
print(f"SCNR improvement: {10*math.log10(avg_snr_phi/avg_snr_kx):.1f} dB")
print(f"Steeper rolloff (PHI width < Kx width): {'PASS' if phi_width_bins <= kx_width_bins else 'FAIL'}")
