#!/usr/bin/env python3
"""Law 2998: Cosmic Ray Anisotropy"""
import math
PHI = 1.618033988749895

def dipole_anisotropy(E, E_0=1e18, delta_0=0.01, alpha=1.0, E_c=1e19):
    return delta_0 * (E / E_0)**alpha * PHI**(-E / E_c)

def simulate():
    print("=== Law 2998: Cosmic Ray Anisotropy ===")
    for E_exp in [17, 17.5, 18, 18.5, 19, 19.5, 20]:
        E = 10**E_exp
        delta = dipole_anisotropy(E)
        print(f"  E = 10^{E_exp:.1f} eV: δ = {delta*100:.3f}%")

if __name__ == "__main__":
    simulate()
