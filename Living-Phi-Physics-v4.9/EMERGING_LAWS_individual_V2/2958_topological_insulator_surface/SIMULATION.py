#!/usr/bin/env python3
"""Law 2958: Topological Insulator Surface State"""
import math
PHI = 1.618033988749895

def dirac_energy(kx, ky, vF=5e5):
    return vF * math.sqrt((kx * PHI)**2 + (ky / PHI)**2)

def simulate():
    print("=== Law 2958: Topological Insulator Surface State ===")
    print(f"  Anisotropy ratio v_Fx/v_Fy = φ = {PHI:.6f}")
    for k in [0.1, 0.5, 1.0]:
        E_iso = 5e5 * k * math.sqrt(2)
        E_phi = dirac_energy(k, k)
        print(f"  k={k} A⁻¹: E_iso={E_iso:.2e}, E_phi={E_phi:.2e}")

if __name__ == "__main__":
    simulate()
