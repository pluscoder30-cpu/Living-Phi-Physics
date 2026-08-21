#!/usr/bin/env python3
"""Law 2967: Neutron Star Gravitational Redshift"""
import math
PHI = 1.618033988749895
G = 6.67430e-11
C = 299792458.0

def gravitational_redshift(M, R):
    x = G * M / (R * C**2)
    return 1.0 / math.sqrt(1 - 2*x) - 1

def phi_corrected_redshift(M, R, M_max):
    z_g = gravitational_redshift(M, R)
    return z_g * (1 + PHI**(-M / M_max))

def simulate():
    print("=== Law 2967: Neutron Star Gravitational Redshift ===")
    M_SUN = 1.989e30
    R_km = 12
    M_max = 2.8 * M_SUN
    for M_msun in [1.4, 2.0, 2.5, 2.8]:
        M = M_msun * M_SUN
        z_std = gravitational_redshift(M, R_km*1000)
        z_phi = phi_corrected_redshift(M, R_km*1000, M_max)
        print(f"  M={M_msun} M_sun: z_std={z_std:.4f}, z_phi={z_phi:.4f}")

if __name__ == "__main__":
    simulate()
