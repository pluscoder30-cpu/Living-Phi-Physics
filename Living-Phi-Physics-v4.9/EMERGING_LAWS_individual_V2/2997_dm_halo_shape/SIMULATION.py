#!/usr/bin/env python3
"""Law 2997: Dark Matter Halo Shape"""
import math
PHI = 1.618033988749895

def ellipticity(M, M_0=1e12, e_0=0.5):
    return e_0 * (1 - PHI**(-M / M_0))

def simulate():
    print("=== Law 2997: Dark Matter Halo Shape ===")
    for M_exp in [10, 11, 12, 13, 14]:
        M = 10**M_exp
        e = ellipticity(M)
        print(f"  M = 10^{M_exp} M_sun: e = {e:.4f}")

if __name__ == "__main__":
    simulate()
