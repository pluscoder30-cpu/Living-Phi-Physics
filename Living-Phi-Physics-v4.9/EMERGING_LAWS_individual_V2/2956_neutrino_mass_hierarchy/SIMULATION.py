#!/usr/bin/env python3
"""Law 2956: Neutrino Mass Hierarchy"""
import math
PHI = 1.618033988749895

def mass_splittings(dM2_0=7.5e-5):
    return dM2_0 / PHI, dM2_0 * PHI

def simulate():
    print("=== Law 2956: Neutrino Mass Hierarchy ===")
    d21, d31 = mass_splittings()
    print(f"  Δm²_21 = {d21:.3e} eV²")
    print(f"  |Δm²_31| = {d31:.3e} eV²")
    print(f"  Ratio: {d31/d21:.4f} ≈ φ² = {PHI**2:.4f}")

if __name__ == "__main__":
    simulate()
