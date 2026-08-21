#!/usr/bin/env python3
"""Law 2962: Measurement-Based Quantum Computing"""
import math
PHI = 1.618033988749895

def qubits_required(d, standard=True):
    if standard:
        return d**2
    return int(d**2 / PHI) + 1

def measurement_angles(n_max):
    return [n * math.pi / PHI for n in range(n_max)]

def simulate():
    print("=== Law 2962: Measurement-Based Quantum Computing ===")
    for d in [3, 5, 7, 11]:
        q_std = qubits_required(d, True)
        q_phi = qubits_required(d, False)
        print(f"  d={d}: standard={q_std}, phi={q_phi}, savings={q_std-q_phi}")
    angles = measurement_angles(5)
    print(f"  φ-optimized angles: {[f'{a:.3f}' for a in angles]}")

if __name__ == "__main__":
    simulate()
