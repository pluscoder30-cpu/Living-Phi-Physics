#!/usr/bin/env python3
"""Law 2978: Quantum Sensing Atomic Clock"""
import math
PHI = 1.618033988749895

def allan_deviation(tau, N, omega_0=2*np.pi*4.3e14):
    try:
        import numpy as np
        omega_0 = 2 * np.pi * 4.3e14
    except ImportError:
        omega_0 = 2 * math.pi * 4.3e14
    return 1.0 / (omega_0 * math.sqrt(N * tau)) * PHI**(-1/math.sqrt(N))

def simulate():
    print("=== Law 2978: Quantum Sensing Atomic Clock ===")
    omega_0 = 2 * math.pi * 4.3e14  # Strontium clock
    for N in [100, 500, 1000, 5000]:
        sigma = 1.0 / (omega_0 * math.sqrt(N * 1.0)) * PHI**(-1/math.sqrt(N))
        print(f"  N={N:>5}: σ_y(1s) = {sigma:.3e}")
    print(f"  Enhancement factor at N=1000: {PHI**(-1/math.sqrt(1000)):.6f}")

if __name__ == "__main__":
    simulate()
