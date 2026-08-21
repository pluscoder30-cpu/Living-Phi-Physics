#!/usr/bin/env python3
"""Law 2974: Quantum Error Correction Surface Code"""
import math
PHI = 1.618033988749895

def physical_qubits_standard(d):
    return d**2

def physical_qubits_phi(d):
    return int(d**2 / PHI) + 1

def simulate():
    print("=== Law 2974: Quantum Error Correction Surface Code ===")
    for d in [3, 5, 7, 9, 11, 13]:
        q_std = physical_qubits_standard(d)
        q_phi = physical_qubits_phi(d)
        savings = (1 - q_phi/q_std) * 100
        print(f"  d={d}: standard={q_std}, phi={q_phi}, savings={savings:.1f}%")

if __name__ == "__main__":
    simulate()
