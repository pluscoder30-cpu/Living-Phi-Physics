#!/usr/bin/env python3
"""Law 2969: Cosmic Ray Knee Spectrum"""
import math
PHI = 1.618033988749895

def spectrum(E, E_knee=3e15, gamma_1=2.7):
    gamma_2 = gamma_1 + 1/PHI
    if E < E_knee:
        return E**(-gamma_1)
    return E_knee**(gamma_2 - gamma_1) * E**(-gamma_2)

def simulate():
    print("=== Law 2969: Cosmic Ray Knee Spectrum ===")
    gamma_1 = 2.7
    gamma_2 = gamma_1 + 1/PHI
    print(f"  γ_1 = {gamma_1}")
    print(f"  γ_2 = {gamma_2:.4f} = γ_1 + 1/φ")
    print(f"  Δγ = {1/PHI:.4f}")
    for E_exp in [14, 15, 15.5, 16, 17]:
        E = 10**E_exp
        flux = spectrum(E)
        print(f"  E = 10^{E_exp} eV: dN/dE ∝ {flux:.3e}")

if __name__ == "__main__":
    simulate()
