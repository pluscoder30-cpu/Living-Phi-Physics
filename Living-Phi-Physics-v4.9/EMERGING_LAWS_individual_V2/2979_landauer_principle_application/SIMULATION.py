#!/usr/bin/env python3
"""Law 2979: Landauer Principle Application"""
import math
PHI = 1.618033988749895
K_B = 1.380649e-23

def erasure_work(n, T=0.01, n_0=10):
    return n * K_B * T * math.log(2) * (1 + PHI**(-n/n_0))

def simulate():
    print("=== Law 2979: Landauer Principle Application ===")
    for n in [10, 50, 100, 500, 1000]:
        W = erasure_work(n)
        W_std = n * K_B * 0.01 * math.log(2)
        print(f"  n={n:>4}: W = {W:.4e} J (correction: {(W/W_std-1)*100:.2f}%)")

if __name__ == "__main__":
    simulate()
