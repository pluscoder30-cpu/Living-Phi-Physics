#!/usr/bin/env python3
"""
Law 2935: Dark Matter Halo Density Profile
Compares NFW vs phi-modified halo profiles
"""
import math

PHI = 1.618033988749895
KPC = 3.0857e19  # meters per kpc

def nfw_profile(r, r_s, rho_0):
    """Standard NFW density profile"""
    x = r / r_s
    return rho_0 / (x * (1 + x)**2)

def phi_modified_profile(r, r_s, rho_0):
    """NFW with golden-ratio suppression"""
    x = r / r_s
    return rho_0 / (x * (1 + x)**2) * PHI**(-x)

def annihilation_flux(r, r_s, rho_0, sigma_v=1e-26):
    """J-factor for dark matter annihilation"""
    rho_nfw = nfw_profile(r, r_s, rho_0)
    rho_phi = phi_modified_profile(r, r_s, rho_0)
    return rho_nfw**2, rho_phi**2

def simulate_halo():
    print("=== Law 2935: Dark Matter Halo Density Profile ===")
    r_s = 20 * KPC  # Scale radius
    rho_0 = 0.3  # GeV/cm^3
    
    radii_kpc = [1, 2, 5, 10, 20, 50, 100]
    print(f"Scale radius r_s = {r_s/KPC:.0f} kpc, rho_0 = {rho_0} GeV/cm^3")
    print(f"\n{'r (kpc)':>8} {'NFW':>12} {'Phi-mod':>12} {'Ratio':>8}")
    
    for r_kpc in radii_kpc:
        r = r_kpc * KPC
        rho_n = nfw_profile(r, r_s, rho_0)
        rho_p = phi_modified_profile(r, r_s, rho_0)
        ratio = rho_p / rho_n if rho_n > 0 else 0
        print(f"{r_kpc:>8} {rho_n:>12.4e} {rho_p:>12.4e} {ratio:>8.4f}")
    
    print(f"\nAt r = 2*r_s: phi suppression = {PHI**(-2):.4f} ({(1-PHI**(-2))*100:.1f}% reduction)")
    print(f"Annihilation flux scales as rho^2, so 23.6% density drop = {(1-PHI**(-2)**2)*100:.1f}% flux reduction")

if __name__ == "__main__":
    simulate_halo()
