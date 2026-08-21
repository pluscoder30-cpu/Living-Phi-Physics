#!/usr/bin/env python3
"""Law 2965: Black Hole Area Theorem"""
import math
PHI = 1.618033988749895
G = 6.67430e-11
C = 299792458.0

def area_increase(m1, m2, E_rad_frac=0.05):
    delta_A = 8 * math.pi * G**2 * m1 * m2 / C**4
    return delta_A * PHI**(-E_rad_frac)

def simulate():
    print("=== Law 2965: Black Hole Area Theorem ===")
    M_SUN = 1.989e30
    for m1, m2 in [(36,29), (85,66), (100,100)]:
        dA = area_increase(m1*M_SUN, m2*M_SUN)
        print(f"  ({m1}+{m2}) M_sun: ΔA = {dA:.4e} m²")
    print(f"  Enhancement: φ^(-0.05) = {PHI**(-0.05):.4f}")

if __name__ == "__main__":
    simulate()
