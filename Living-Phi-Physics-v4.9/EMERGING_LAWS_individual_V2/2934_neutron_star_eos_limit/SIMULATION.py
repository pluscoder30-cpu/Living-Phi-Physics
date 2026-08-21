#!/usr/bin/env python3
"""
Law 2934: Neutron Star Equation of State Limit
Computes maximum mass with golden-ratio quark matter enhancement
"""
import math

PHI = 1.618033988749895
C = 299792458.0
G = 6.67430e-11
M_SUN = 1.989e30
RHO_QCD = 2.7e17  # QCD critical density kg/m^3

def maximum_neutron_star_mass():
    """Maximum mass with phi-enhanced quark matter packing"""
    M_max_kg = (PHI * C**3) / (4 * G**(1.5) * math.sqrt(math.pi * RHO_QCD))
    return M_max_kg / M_SUN

def tov_pressure_gradient(r, M, P, rho):
    """Simplified TOV equation for mass integration"""
    denom = r * (r - 2 * G * M / C**2)
    if denom <= 0:
        return 0
    return -G * (rho + P / C**2) * (M + 4 * math.pi * r**3 * P / C**2) / denom

def quark_core_fraction(M_star):
    """Fraction of star that is quark matter"""
    M_max = maximum_neutron_star_mass() * M_SUN
    if M_star > M_max:
        return 1.0
    x = M_star / M_max
    return x**3  # Volume fraction scales cubically

def simulate_neutron_stars():
    print("=== Law 2934: Neutron Star EOS Limit ===")
    M_max = maximum_neutron_star_mass()
    print(f"Maximum NS mass (phi-enhanced): {M_max:.2f} M_sun")
    print(f"Standard TOV limit: ~{2.17:.2f} M_sun")
    print(f"Phi enhancement factor: {PHI:.4f}")
    
    stars = [1.4, 2.0, 2.5, 2.8, 3.1]
    print("\nQuark core fractions:")
    for M in stars:
        fq = quark_core_fraction(M * M_SUN)
        print(f"  {M:.1f} M_sun: quark fraction = {fq:.3f} ({fq*100:.1f}%)")
    
    print(f"\nStars above {M_max:.2f} M_sun are unstable to collapse.")
    print(f"Detection threshold: oscillation splitting Δf = f_0 / {PHI:.4f}")

if __name__ == "__main__":
    simulate_neutron_stars()
