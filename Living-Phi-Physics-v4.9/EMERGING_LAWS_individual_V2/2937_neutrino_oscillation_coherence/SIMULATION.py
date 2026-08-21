#!/usr/bin/env python3
"""
Law 2937: Neutrino Oscillation Phase Coherence
Simulates matter-enhanced neutrino coherence with golden ratio
"""
import math

PHI = 1.618033988749895
EV2_TO_KG = 1.78266192e-36  # eV^2 to kg conversion
DELTA_M21 = 7.53e-5  # Solar mass splitting eV^2
THETA_12 = 33.44  # degrees
L_KM = 1.496e8  # Sun to Earth km

def oscillation_probability(E_eV, L_m, V=0):
    """Two-flavor oscillation probability in matter"""
    theta = math.radians(THETA_12)
    delta_m2 = DELTA_M21
    sin2t = math.sin(2 * theta)
    cos2t = math.cos(2 * theta)
    delta_m2_eff = math.sqrt(delta_m2**2 * cos2t**2 + (delta_m2 * cos2t - 2 * E_eV * V)**2)
    sin2t_eff = delta_m2 * sin2t / delta_m2_eff
    return 1 - sin2t_eff**2 * math.sin(delta_m2_eff * L_m / (4 * E_eV))**2

def coherence_length(E_eV, V=0):
    """Coherence length with phi-enhancement"""
    theta = math.radians(THETA_12)
    L_coh_vac = 4 * math.pi * E_eV**2 / (DELTA_M21 * math.sin(2 * theta))
    phi_factor = PHI**(V / DELTA_M21) if DELTA_M21 > 0 else 1
    return L_coh_vac * phi_factor

def simulate_neutrinos():
    print("=== Law 2937: Neutrino Oscillation Phase Coherence ===")
    energies = [0.1e6, 1e6, 10e6, 100e6]  # eV
    V_solar = 1e-11  # Solar matter potential eV
    
    print(f"Δm²_21 = {DELTA_M21:.2e} eV², θ_12 = {THETA_12}°")
    print(f"Solar matter potential V = {V_solar:.0e} eV")
    print(f"\n{'E (MeV)':>8} {'L_coh vac':>12} {'L_coh phi':>12} {'Ratio':>8}")
    
    for E in energies:
        Lc_vac = coherence_length(E, 0)
        Lc_phi = coherence_length(E, V_solar)
        ratio = Lc_phi / Lc_vac
        print(f"{E/1e6:>8.1f} {Lc_vac:>12.3e} {Lc_phi:>12.3e} {ratio:>8.4f}")
    
    print(f"\nSolar neutrino survival probability at 1 MeV:")
    print(f"  Standard MSW:  P_ee ≈ {oscillation_probability(1e6, L_KM*1e3, 0):.3f}")
    print(f"  Phi-enhanced:  P_ee ≈ {oscillation_probability(1e6, L_KM*1e3, V_solar):.3f}")

if __name__ == "__main__":
    simulate_neutrinos()
