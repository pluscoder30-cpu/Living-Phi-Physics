#!/usr/bin/env python3
"""Law 2993: Quantum Sensing Magnetometer"""
import math
PHI = 1.618033988749895

def sensitivity(B, T_2=1e-3, N=1e6, gamma=2.8e6, B_0=1e-3):
    return 1.0 / (gamma * math.sqrt(T_2 * N)) * PHI**(-B / B_0)

def simulate():
    print("=== Law 2993: Quantum Sensing Magnetometer ===")
    for B_uT in [0, 1, 10, 100, 1000]:
        B = B_uT * 1e-6
        sens = sensitivity(B)
        print(f"  B = {B_uT:>5} μT: δB = {sens:.3e} T/√Hz")
    print(f"  Enhancement at B=0: {PHI**0:.4f}x")

if __name__ == "__main__":
    simulate()
