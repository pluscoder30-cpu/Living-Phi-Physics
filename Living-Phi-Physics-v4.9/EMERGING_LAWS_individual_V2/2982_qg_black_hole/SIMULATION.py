#!/usr/bin/env python3
"""Law 2982: Quantum Gravity Black Hole"""
import math
PHI = 1.618033988749895
L_P = 1.616255e-35
G = 6.67430e-11
C = 299792458.0

def hawking_temp_lqg(M, alpha=1.0):
    T_H = 1.0  # normalized
    r_s = 2 * G * M / C**2
    correction = alpha * (L_P / r_s)**2 * PHI**(-r_s / L_P)
    return T_H * (1 - correction)

def simulate():
    print("=== Law 2982: Quantum Gravity Black Hole ===")
    M_SUN = 1.989e30
    for M_msun in [1, 10, 1e6, 1e10]:
        M = M_msun * M_SUN
        r_s = 2 * G * M / C**2
        correction = (L_P / r_s)**2 * PHI**(-r_s / L_P)
        print(f"  M = {M_msun:.0e} M_sun: r_s = {r_s:.3e} m, correction = {correction:.3e}")

if __name__ == "__main__":
    simulate()
