#!/usr/bin/env python3
"""Law 2995: Quantum Field Phase Transition"""
import math
PHI = 1.618033988749895

def critical_temperature(g, g_0=1.0, T_c0=1.0):
    return T_c0 * PHI**(-(g/g_0)**2)

def simulate():
    print("=== Law 2995: Quantum Field Phase Transition ===")
    for g_ratio in [0.0, 0.5, 1.0, 1.5, 2.0]:
        T_c = critical_temperature(g_ratio)
        print(f"  g/g_0 = {g_ratio:.1f}: T_c/T_c0 = {T_c:.4f}")

if __name__ == "__main__":
    simulate()
