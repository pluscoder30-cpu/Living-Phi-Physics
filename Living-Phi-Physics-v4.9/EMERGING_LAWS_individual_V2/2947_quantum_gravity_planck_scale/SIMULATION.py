#!/usr/bin/env python3
"""
Law 2947: Quantum Gravity Planck Scale Correction
Simulates modified dispersion relation with golden-ratio suppression
"""
import math

PHI = 1.618033988749895
E_Plg = 1.2209e19  # Planck energy in GeV
C = 299792458.0
MPC = 3.0857e22

def modified_dispersio(E_GeV, xi=1.0, n=1):
    """Modified dispersion relation correction"""
    E_ratio = E_GeV / E_Plg
    return xi * E_ratio**n * PHI**(-E_ratio)

def time_delay(E_GeV, D_mpc, xi=1.0, n=1):
    """Time delay from modified dispersion"""
    D = D_mpc * MPC
    delta = modified_dispersio(E_GeV, xi, n)
    return delta * D / C

def simulate_planck():
    print("=== Law 2947: Quantum Gravity Planck Scale Correction ===")
    print(f"Planck energy E_Plg = {E_Plg:.4e} GeV")
    print(f"Golden ratio φ = {PHI:.6f}")
    
    energies = [1e3, 1e6, 1e9, 1e12]  # GeV
    D = 1000  # Mpc
    
    print(f"\nDistance D = {D} Mpc")
    print(f"{'E (GeV)':>10} {'ξ correction':>12} {'Δt (s)':>12}")
    
    for E in energies:
        delta = modified_dispersio(E)
        dt = time_delay(E, D)
        print(f"{E:>10.0e} {delta:>12.4e} {dt:>12.4e}")
    
    print(f"\nAt E = 10 TeV (CTA sensitivity):")
    E = 1e4
    print(f"  Standard QG correction: {E/E_Plg:.4e}")
    print(f"  Phi-suppressed: {E/E_Plg * PHI**(-E/E_Plg):.4e}")
    print(f"  Suppression factor: {PHI**(-E/E_Plg):.4f}")

if __name__ == "__main__":
    simulate_planck()
