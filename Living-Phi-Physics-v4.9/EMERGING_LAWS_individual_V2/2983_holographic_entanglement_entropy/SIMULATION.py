#!/usr/bin/env python3
"""Law 2983: Holographic Entanglement Entropy"""
import math
PHI = 1.618033988749895

def entanglement_entropy(A, L, epsilon=0.01, L_0=1.0, c=1.0):
    return A / 4.0 + c * math.log(L / epsilon) * PHI**(-L / L_0)

def simulate():
    print("=== Law 2983: Holographic Entanglement Entropy ===")
    for L in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
        S_std = L / 4.0 + math.log(L / 0.01)
        S_phi = entanglement_entropy(L, L)
        print(f"  L = {L:.1f}: S_std = {S_std:.4f}, S_phi = {S_phi:.4f}")

if __name__ == "__main__":
    simulate()
