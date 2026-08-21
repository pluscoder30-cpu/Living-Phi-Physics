#!/usr/bin/env python3
"""Law 2990: Neutrino Astrophysics Source"""
import math
PHI = 1.618033988749895

def neutrino_luminosity(E_ν, E_0=1e6, L_0=1.0, alpha=-2.0, E_cut=1e7):
    return L_0 * (E_ν / E_0)**alpha * PHI**(-E_ν / E_cut)

def simulate():
    print("=== Law 2990: Neutrino Astrophysics Source ===")
    for E_exp in [5, 6, 7, 8]:
        E = 10**E_exp
        L = neutrino_luminosity(E)
        print(f"  E_ν = 10^{E_exp} eV: L_ν = {L:.3e}")

if __name__ == "__main__":
    simulate()
