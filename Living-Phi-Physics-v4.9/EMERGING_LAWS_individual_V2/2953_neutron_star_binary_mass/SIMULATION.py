#!/usr/bin/env python3
"""Law 2953: Neutron Star Binary Mass"""
import math
PHI = 1.618033988749895

def max_mass_binary(M_iso, q):
    return M_iso * (1 + PHI**(-q))

def simulate():
    print("=== Law 2953: Neutron Star Binary Mass ===")
    M_iso = 2.17
    for q in [0.5, 1/PHI, 0.8, 1.0]:
        print(f"  q={q:.3f}: M_max = {max_mass_binary(M_iso, q):.3f} M_sun")
    print(f"  Peak enhancement at q=1/φ: {max_mass_binary(M_iso, 1/PHI)/M_iso:.4f}x")

if __name__ == "__main__":
    simulate()
