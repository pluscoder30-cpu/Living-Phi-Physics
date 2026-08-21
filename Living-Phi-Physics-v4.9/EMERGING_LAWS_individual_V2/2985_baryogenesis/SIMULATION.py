#!/usr/bin/env python3
"""Law 2985: Particle Physics Baryogenesis"""
import math
PHI = 1.618033988749895

def baryon_asymmetry(Gamma_L, Gamma_R, s, T, T_EW=100.0):
    return (Gamma_L - Gamma_R) / s * PHI**(-T / T_EW)

def simulate():
    print("=== Law 2985: Particle Physics Baryogenesis ===")
    s = 1.0
    Gamma_L = 1e-6
    for T_ratio in [0.5, 0.8, 1.0, 1.2, 1.5]:
        eta = baryon_asymmetry(Gamma_L, 0.999*Gamma_L, s, T_ratio*100)
        print(f"  T/T_EW = {T_ratio:.1f}: η = {eta:.3e}")
    print(f"  Observed η ≈ 6×10^-10")

if __name__ == "__main__":
    simulate()
