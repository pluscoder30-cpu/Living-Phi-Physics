#!/usr/bin/env python3
"""Law 2976: Quantum Annealing Minimum Gap"""
import math
PHI = 1.618033988749895

def minimum_gap(N, Delta_0=1.0, alpha=0.5):
    return Delta_0 * N**(-alpha/PHI)

def simulate():
    print("=== Law 2976: Quantum Annealing Minimum Gap ===")
    print(f"  Scaling exponent: α/φ = {0.5/PHI:.4f}")
    for N in [10, 50, 100, 500, 1000]:
        gap = minimum_gap(N)
        print(f"  N={N:>5}: Δ_min = {gap:.4e}")

if __name__ == "__main__":
    simulate()
