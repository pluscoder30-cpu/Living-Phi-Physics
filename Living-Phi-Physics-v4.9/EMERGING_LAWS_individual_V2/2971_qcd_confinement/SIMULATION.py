#!/usr/bin/env python3
"""Law 2971: QCD Confinement"""
import math
PHI = 1.618033988749895

def string_tension(r, sigma_0=0.18, r_0=1.0):
    return sigma_0 * (1 + PHI**(-r/r_0))

def quark_potential(r, sigma_0=0.18, r_0=1.0):
    sigma = string_tension(r, sigma_0, r_0)
    return sigma * r - math.pi / (12 * max(r, 0.1))

def simulate():
    print("=== Law 2971: QCD Confinement ===")
    for r in [0.5, 1.0, 2.0, 5.0, 10.0]:
        sigma = string_tension(r)
        V = quark_potential(r)
        print(f"  r = {r:.1f} fm: σ = {sigma:.4f} GeV², V = {V:.4f} GeV")

if __name__ == "__main__":
    simulate()
