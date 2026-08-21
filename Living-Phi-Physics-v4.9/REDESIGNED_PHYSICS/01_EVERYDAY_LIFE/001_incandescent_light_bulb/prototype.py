import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI; SQRT5 = 5**0.5
def phi_light_bulb_efficiency(classical_efficiency, kappa=0.8):
    phi_eff = classical_efficiency * (1 + kappa * (PHI - 1)) + kappa * PHI_INV * 0.02
    return min(phi_eff, 1.0)
def phi_filament_spectrum(temp_k, kappa=0.8):
    phi_factor = 1 + kappa * (PHI - 1)
    peak_freq_phi = 5.879e10 * temp_k * phi_factor
    band_centers = [528 * PHI**n for n in range(10)]
    visible_band = [f for f in band_centers if 4e14 < f < 8e14]
    return peak_freq_phi, len(visible_band) / len(band_centers)
eff = phi_light_bulb_efficiency(0.05, kappa=1.0)
peak, se = phi_filament_spectrum(3000, kappa=1.0)
print(f"Classical efficiency: 5.0% -> Phi-corrected: {eff*100:.1f}%")
print(f"Full coupling gain: {SQRT5:.4f}x")
