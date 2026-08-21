#!/usr/bin/env python3
"""Law 2984: Quantum Field Anomaly"""
import math
PHI = 1.618033988749895

def anomaly_coefficient(c_0, N_f, N_c):
    return c_0 * (1 + PHI**(-N_f/N_c))

def simulate():
    print("=== Law 2984: Quantum Field Anomaly ===")
    for N_f, N_c in [(1,3), (2,3), (3,3), (5,3), (1,2)]:
        c = anomaly_coefficient(1.0, N_f, N_c)
        print(f"  N_f={N_f}, N_c={N_c}: c = {c:.4f}")
    print(f"  At N_f/N_c=1/φ: c = {anomaly_coefficient(1.0, 1/PHI, 1):.4f}")

if __name__ == "__main__":
    simulate()
