#!/usr/bin/env python3
"""Law 2961: Quantum Spin Liquid Frustration"""
import math
PHI = 1.618033988749895

def spinon_dispersion(k_a, J=1.0):
    return J * abs(math.sin(k_a)) * PHI**(-abs(k_a)/math.pi)

def simulate():
    print("=== Law 2961: Quantum Spin Liquid Frustration ===")
    k_vals = [0, 0.25*math.pi, 0.5*math.pi, 0.75*math.pi, math.pi]
    for k in k_vals:
        E = spinon_dispersion(k)
        print(f"  k*a/π = {k/math.pi:.2f}: E = {E:.4f} J")
    print(f"  Bandwidth W = 2J/φ = {2/PHI:.4f} J")

if __name__ == "__main__":
    simulate()
