#!/usr/bin/env python3
"""Law 2972: Holographic Superconductor"""
import math
PHI = 1.618033988749895

def critical_temperature(T_H, lam_g2=1.0):
    return 0.2 * T_H * PHI**(-lam_g2)

def simulate():
    print("=== Law 2972: Holographic Superconductor ===")
    for lam_g2 in [0.5, 1.0, 2.0, 3.0]:
        T_c_ratio = critical_temperature(1.0, lam_g2)
        print(f"  λ/g² = {lam_g2:.1f}: T_c/T_H = {T_c_ratio:.4f}")
    print(f"  At λ/g²=1: T_c = {critical_temperature(1.0, 1.0):.4f} T_H")

if __name__ == "__main__":
    simulate()
