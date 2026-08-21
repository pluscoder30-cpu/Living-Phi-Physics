#!/usr/bin/env python3
"""
Law 2933: Gravitational Wave Memory Effect
Computes memory displacement with golden-ratio mode suppression
"""
import math

PHI = 1.618033988749895
C = 299792458.0
G = 6.67430e-11
MPC = 3.0857e22
M_SUN = 1.989e30

def memory_strain(E_gw, distance, frequency, n_phi=2):
    """Gravitational wave memory strain with phi-suppression"""
    return (2 * G * E_gw) / (C**4 * distance * frequency**2) * PHI**(-n_phi)

def memory_displacement(strain, arm_length=4000):
    """Displacement in meters for given strain and arm length"""
    return strain * arm_length

def chirp_energy(M1, M2):
    """Energy radiated in gravitational waves during merger"""
    eta = M1 * M2 / (M1 + M2)**2
    return 0.05 * eta * (M1 + M2) * M_SUN * C**2

def simulate_memory_events():
    print("=== Law 2933: Gravitational Wave Memory ===")
    events = [
        ("GW150914-like", 36 * M_SUN, 29 * M_SUN, 410 * MPC),
        ("GW170817-like", 1.46 * M_SUN, 1.27 * M_SUN, 40 * MPC),
        ("Massive BBH", 100 * M_SUN, 80 * M_SUN, 1000 * MPC),
    ]
    for name, m1, m2, d in events:
        E = chirp_energy(m1, m2)
        freq = 100.0 if m1 > 10 * M_SUN else 1000.0
        h_mem = memory_strain(E, d, freq)
        dx = memory_displacement(h_mem)
        print(f"\nEvent: {name}")
        print(f"  GW energy: {E:.3e} J")
        print(f"  Memory strain: {h_mem:.3e}")
        print(f"  Memory displacement: {dx:.3e} m")
        print(f"  Phi^(-2) correction: {PHI**(-2):.4f}")
    print("\nMemory effects quantified for three source types.")

if __name__ == "__main__":
    simulate_memory_events()
