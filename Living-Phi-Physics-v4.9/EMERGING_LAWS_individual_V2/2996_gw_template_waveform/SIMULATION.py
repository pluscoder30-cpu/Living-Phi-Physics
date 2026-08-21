#!/usr/bin/env python3
"""Law 2996: Gravitational Wave Template Waveform"""
import math
PHI = 1.618033988749895

def pn_correction(v_c, n_PN):
    return PHI**(-n_PN) * v_c**n_PN

def simulate():
    print("=== Law 2996: Gravitational Wave Template Waveform ===")
    v_c = 0.1  # v/c at last stable orbit
    for n in range(1, 6):
        corr = pn_correction(v_c, n)
        print(f"  n_PN = {n}: correction = {corr:.6e}")
    print(f"  φ^(-1) enhancement at n=1: {PHI**(-1):.4f}")

if __name__ == "__main__":
    simulate()
