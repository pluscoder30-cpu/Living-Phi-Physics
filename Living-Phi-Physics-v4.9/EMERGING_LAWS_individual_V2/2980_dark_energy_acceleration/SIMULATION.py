#!/usr/bin/env python3
"""Law 2980: Dark Energy Acceleration"""
import math
PHI = 1.618033988749895

def deceleration_param(z, Omega_m=0.3, z_star=0.7):
    return -1 + 1.5 * Omega_m * (1 + PHI**(-z/z_star))

def simulate():
    print("=== Law 2980: Dark Energy Acceleration ===")
    for z in [0.0, 0.3, 0.7, 1.0, 1.5, 2.0]:
        q = deceleration_param(z)
        state = "acceleration" if q < 0 else "deceleration"
        print(f"  z={z:.1f}: q = {q:.4f} ({state})")
    print(f"  Transition at z ≈ 0.7 where q ≈ 0")

if __name__ == "__main__":
    simulate()
