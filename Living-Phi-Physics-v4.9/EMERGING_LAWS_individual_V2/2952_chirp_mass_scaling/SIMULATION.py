#!/usr/bin/env python3
"""
Law 2952: Gravitational Wave Chirp Mass
Simulates golden-ratio corrected chirp mass extraction
"""
import math

PHI = 1.618033988749895
M_SUN = 1.989e30

def chirp_mass_standard(m1, m2):
    """Standard chirp mass"""
    return (m1 * m2)**(3/5) / (m1 + m2)**(1/5)

def chirp_mass_phi(m1, m2):
    """Phi-modified chirp mass"""
    M_c = chirp_mass_standard(m1, m2)
    delta_m = abs(m1 - m2)
    m_avg = (m1 + m2) / 2
    return M_c * PHI**(-delta_m / m_avg)

def mass_ratio(m1, m2):
    return min(m1, m2) / max(m1, m2)

def simulate_chirp():
    print("=== Law 2952: Gravitational Wave Chirp Mass ===")
    systems = [
        (36, 29, "GW150914"),
        (31, 25, "GW151226"),
        (85, 66, "GW190521"),
        (1.46, 1.27, "GW170817"),
    ]
    
    print(f"{'System':>12} {'q':>6} {'M_c std':>10} {'M_c phi':>10} {'Error%':>8}")
    for m1, m2, name in systems:
        q = mass_ratio(m1, m2)
        Mc_s = chirp_mass_standard(m1, m2)
        Mc_p = chirp_mass_phi(m1, m2)
        err = (Mc_s - Mc_p) / Mc_s * 100
        print(f"{name:>12} {q:>6.3f} {Mc_s:>10.3f} {Mc_p:>10.3f} {err:>8.3f}")
    
    print(f"\nAt q = 0.8: error from neglecting phi = {chirp_mass_phi(36, 28.8)/chirp_mass_standard(36, 28.8)*100 - 100:.2f}%")

if __name__ == "__main__":
    simulate_chirp()
