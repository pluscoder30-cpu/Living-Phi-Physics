#!/usr/bin/env python3
"""Law 2954: Dark Matter Annihilation Cross Section"""
import math
PHI = 1.618033988749895
M_Z = 91.1876

def cross_section(m_DM, sigma_0=3e-26):
    return sigma_0 * (1 + PHI**(-m_DM/M_Z))

def simulate():
    print("=== Law 2954: Dark Matter Annihilation Cross Section ===")
    for m_DM in [10, 50, 100, 500, 1000]:
        print(f"  m_DM={m_DM:>5} GeV: <σv> = {cross_section(m_DM):.3e} cm³/s")
    print(f"  Enhancement at m_Z/φ: {cross_section(M_Z/PHI)/3e-26:.4f}x")

if __name__ == "__main__":
    simulate()
