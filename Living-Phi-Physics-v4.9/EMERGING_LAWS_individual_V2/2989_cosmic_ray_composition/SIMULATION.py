#!/usr/bin/env python3
"""Law 2989: Cosmic Ray Composition"""
import math
PHI = 1.618033988749895

def mean_mass(E, E_knee=3e15, ln_A_0=math.log(56)):
    return ln_A_0 * (1 + PHI**(-E / E_knee))

def simulate():
    print("=== Law 2989: Cosmic Ray Composition ===")
    for E_exp in [14, 15, 16, 17, 18, 19]:
        E = 10**E_exp
        ln_A = mean_mass(E)
        A = math.exp(ln_A)
        print(f"  E = 10^{E_exp} eV: ln(A) = {ln_A:.3f}, A = {A:.1f}")

if __name__ == "__main__":
    simulate()
