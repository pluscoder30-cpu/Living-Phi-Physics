#!/usr/bin/env python3
"""Law 2977: Adiabatic Quantum Computation"""
import math
PHI = 1.618033988749895

def runtime(N, T_0=1.0, beta=0.5):
    return T_0 * PHI**(N**beta)

def classical_runtime(N):
    return 2**N

def simulate():
    print("=== Law 2977: Adiabatic Quantum Computation ===")
    for N in [10, 20, 50, 100]:
        T_aq = runtime(N)
        T_cl = classical_runtime(N)
        speedup = T_cl / T_aq if T_aq > 0 else float('inf')
        print(f"  N={N:>3}: T_AQC={T_aq:.3e}, T_classical={T_cl:.3e}, speedup={speedup:.3e}")

if __name__ == "__main__":
    simulate()
