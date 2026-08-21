#!/usr/bin/env python3
"""Law 2968: Dark Matter Direct Detection"""
import math
PHI = 1.618033988749895

def event_rate(E_R, R_0=1.0, E_0=30.0, F2=1.0):
    return R_0 * PHI**(-E_R / E_0) * F2

def simulate():
    print("=== Law 2968: Dark Matter Direct Detection ===")
    E_0 = 30.0  # keV
    for E_R in [0, 10, 30, 60, 100]:
        F2 = math.exp(-E_R / 50.0)  # Simple form factor
        R = event_rate(E_R, E_0=E_0, F2=F2)
        print(f"  E_R = {E_R:>3} keV: dR/dE_R = {R:.4f}")
    print(f"  φ-structured peaks at E_0/φ^n")

if __name__ == "__main__":
    simulate()
