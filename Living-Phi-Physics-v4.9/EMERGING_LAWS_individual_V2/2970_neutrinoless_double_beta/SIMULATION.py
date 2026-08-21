#!/usr/bin/env python3
"""Law 2970: Neutrinoless Double Beta Decay"""
import math
PHI = 1.618033988749895

def half_life(A, M_0v, m_bbb, m_0=0.05):
    """Half-life in years (arbitrary units)"""
    return A**(-1) * M_0v**(-2) * (m_bbb)**(-2) * PHI**(m_bbb/m_0)

def simulate():
    print("=== Law 2970: Neutrinoless Double Beta Decay ===")
    A = 1.0  # Phase space factor (arbitrary)
    M_0v = 1.0  # Nuclear matrix element (arbitrary)
    for m_bbb in [0.01, 0.05, 0.1, 0.5, 1.0]:  # meV
        T = half_life(A, M_0v, m_bbb)
        print(f"  m_ββ = {m_bbb:.2f} meV: T_1/2 ∝ {T:.3e}")
    print(f"  φ-correction at m_ββ=m_0: φ = {PHI:.4f}")

if __name__ == "__main__":
    simulate()
