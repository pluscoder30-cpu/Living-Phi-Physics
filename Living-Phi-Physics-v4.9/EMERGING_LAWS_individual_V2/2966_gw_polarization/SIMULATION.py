#!/usr/bin/env python3
"""Law 2966: Gravitational Wave Polarization"""
import math
PHI = 1.618033988749895
G = 6.67430e-11
C = 299792458.0

def scalar_mode(h_plus, r, M):
    r_H = 2 * G * M / C**2
    return h_plus * PHI**(-r / r_H)

def simulate():
    print("=== Law 2966: Gravitational Wave Polarization ===")
    M_SUN = 1.989e30
    M = 30 * M_SUN
    r_H = 2 * G * M / C**2
    print(f"  Schwarzschild radius: {r_H:.3e} m")
    for r_km in [100, 1000, 10000]:
        r = r_km * 1000
        ratio = PHI**(-r / r_H)
        print(f"  r = {r_km} km: h_0/h_+ = {ratio:.4e}")

if __name__ == "__main__":
    simulate()
