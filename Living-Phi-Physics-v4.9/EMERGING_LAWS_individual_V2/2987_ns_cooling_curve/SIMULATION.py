#!/usr/bin/env python3
"""Law 2987: Neutron Star Cooling Curve"""
import math
PHI = 1.618033988749895

def temperature(t, t_0=1e5, T_0=1e9, n=1.0):
    return T_0 * (t / t_0)**(-n / PHI)

def simulate():
    print("=== Law 2987: Neutron Star Cooling Curve ===")
    t_0 = 1e5  # years
    T_0 = 1e9  # K
    for t_yr in [100, 1000, 1e4, 1e5, 1e6]:
        T = temperature(t_yr, t_0, T_0)
        print(f"  t = {t_yr:.0e} yr: T = {T:.3e} K")
    print(f"  Cooling exponent: -1/φ = {-1/PHI:.4f}")

if __name__ == "__main__":
    simulate()
