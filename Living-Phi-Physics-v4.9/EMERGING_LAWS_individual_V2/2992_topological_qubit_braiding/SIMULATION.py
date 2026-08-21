#!/usr/bin/env python3
"""Law 2992: Topological Qubit Braiding"""
import math
PHI = 1.618033988749895

def gate_fidelity(L_a, epsilon=0.01):
    return 1 - epsilon * PHI**(-L_a)

def simulate():
    print("=== Law 2992: Topological Qubit Braiding ===")
    for L_a in [1, 2, 5, 10, 20]:
        F = gate_fidelity(L_a)
        print(f"  L/a = {L_a:>2}: F = {F:.6f}")
    print(f"  At L/a=10: F = {gate_fidelity(10):.6f}")

if __name__ == "__main__":
    simulate()
