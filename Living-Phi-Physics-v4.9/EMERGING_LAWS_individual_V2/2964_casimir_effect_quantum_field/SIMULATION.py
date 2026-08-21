#!/usr/bin/env python3
"""Law 2964: Quantum Field Casimir Effect"""
import math
PHI = 1.618033988749895

def casimir_force_fractal(d, a, F_0=-1.0):
    return F_0 * (1 + PHI**(-d/a))

def simulate():
    print("=== Law 2964: Quantum Field Casimir Effect ===")
    for d_a in [0.5, 1.0, 2.0, 5.0, 10.0]:
        F = casimir_force_fractal(d_a, 1.0)
        print(f"  d/a = {d_a:.1f}: F/F_0 = {F:.4f}")
    print(f"  Enhancement at d=a: {(1+PHI**(-1))*100:.1f}%")

if __name__ == "__main__":
    simulate()
