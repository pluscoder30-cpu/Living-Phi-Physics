#!/usr/bin/env python3
"""
PROTOTYPE: Item 201 - Mass Spectrometer Ion Optics
Phi-physics redesign implementation.
"""

import math

PHI = (1 + math.sqrt(5)) / 2

def phi_multipole_transmission(kinetic_energy_ev, n_rods=4):
    E0 = 10.0
    T_standard = 1.0 / (1 + (kinetic_energy_ev / E0)**2)
    T_phi = T_standard * PHI
    space_charge_limit = 1e6 * PHI**2
    return T_standard, T_phi, space_charge_limit

def mass_resolution():
    standard_res = 1000
    phi_res = standard_res * PHI
    return standard_res, phi_res

print("Phi-multipole transmission vs energy:")
for E in [1, 5, 10, 20, 50]:
    T_std, T_phi, limit = phi_multipole_transmission(E)
    print(f"  E={E}eV: T_std={T_std:.3f}, T_phi={T_phi:.3f}, limit={limit:.0e}")
std_res, phi_res = mass_resolution()
print(f"\nMass resolution: {std_res} -> {phi_res:.0f}")

if __name__ == "__main__":
    pass
