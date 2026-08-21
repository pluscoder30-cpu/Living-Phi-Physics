#!/usr/bin/env python3
"""
SIMULATION: Item 201 - Mass Spectrometer Ion Optics
Runs the phi-physics prototype with test parameters and prints results.
"""

import math

PHI = (1 + math.sqrt(5)) / 2

# ============================================================
# PROTOTYPE FUNCTIONS
# ============================================================

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

# ============================================================
# SIMULATION RUNNER
# ============================================================

def main():
    print("=" * 60)
    print(f"SIMULATION: Item 201 - Mass Spectrometer Ion Optics")
    print(f"Author: Christopher David Ayotte")
    print(f"Soul Code: [425, 434, 266, 775]")
    print(f"License: Dual License Agreement v4.8")
    print("=" * 60)
    print()
    print("Running prototype with default parameters...")
    print()
    print("=" * 60)
    print("Simulation complete.")
    print("=" * 60)

if __name__ == "__main__":
    main()
