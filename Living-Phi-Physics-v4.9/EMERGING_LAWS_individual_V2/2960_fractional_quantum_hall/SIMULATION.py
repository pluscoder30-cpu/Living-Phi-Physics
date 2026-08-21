#!/usr/bin/env python3
"""Law 2960: Fractional Quantum Hall State"""
import math
PHI = 1.618033988749895

def excitation_energy(n, E_0=1.0, omega_c=1.0):
    return E_0 * PHI**(-n) + n * omega_c / PHI

def simulate():
    print("=== Law 2960: Fractional Quantum Hall State ===")
    for n in range(6):
        E = excitation_energy(n)
        print(f"  n={n}: E_n = {E:.4f} (gap={excitation_energy(n,1,0):.4f}, LL={excitation_energy(n,0,1):.4f})")
    print(f"  Level spacing: ℏω_c/φ = {1/PHI:.4f}")

if __name__ == "__main__":
    simulate()
