#!/usr/bin/env python3
"""
Law 2936: Cosmic Ray Air Shower Scaling
Simulates longitudinal shower development with phi-modulation
"""
import math

PHI = 1.618033988749895
X_0 = 36.7  # Radiation length in air (g/cm^2)
E_C = 85e6  # Critical energy in eV

def x_max_standard(E_eV):
    """Standard Heitler X_max"""
    return X_0 * math.log(E_eV / E_C)

def x_max_phi_modified(E_eV, alpha=0.12):
    """X_max with golden-ratio hadronic correction"""
    return x_max_standard(E_eV) * PHI**(-alpha)

def shower_size(X, X_max, Lambda=70):
    """Approximate shower size at depth X"""
    return math.exp(-(X - X_max)**2 / (2 * Lambda**2))

def simulate_showers():
    print("=== Law 2936: Cosmic Ray Air Shower Scaling ===")
    energies = [1e18, 1e19, 5e19, 1e20, 3e20]  # eV
    
    print(f"X_0 = {X_0} g/cm², E_C = {E_C:.0e} eV")
    print(f"\n{'Energy (eV)':>12} {'X_max std':>10} {'X_max phi':>10} {'Depth ratio':>10}")
    
    for E in energies:
        xm_std = x_max_standard(E)
        xm_phi = x_max_phi_modified(E)
        ratio = xm_phi / xm_std
        print(f"{E:>12.0e} {xm_std:>10.1f} {xm_phi:>10.1f} {ratio:>10.4f}")
    
    print(f"\nAt E = 10^20 eV:")
    print(f"  Standard X_max: {x_max_standard(1e20):.1f} g/cm²")
    print(f"  Phi-modified:   {x_max_phi_modified(1e20):.1f} g/cm²")
    print(f"  Deeper penetration: {(1 - PHI**(-0.12))*100:.1f}%")
    print(f"\nGolden-ratio correction to hadronic multiplicity:")
    print(f"  Secondary particle ratio: 1/φ = {1/PHI:.4f}")

if __name__ == "__main__":
    simulate_showers()
