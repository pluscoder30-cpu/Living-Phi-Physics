#!/usr/bin/env python3
"""Law 2963: Quantum Sensing Squeezed State"""
import math
PHI = 1.618033988749895

def optimal_squeezing(N):
    return 0.5 * math.log(N / PHI)

def phase_sensitivity(r, N):
    return math.exp(-r) / math.sqrt(N)

def simulate():
    print("=== Law 2963: Quantum Sensing Squeezed State ===")
    for N in [100, 500, 1000, 5000, 10000]:
        r = optimal_squeezing(N)
        dB = 20 * r / math.log(10)
        sens = phase_sensitivity(r, N)
        print(f"  N={N:>5}: r_opt={r:.3f} ({dB:.1f} dB), Δθ={sens:.4e}")

if __name__ == "__main__":
    simulate()
