#!/usr/bin/env python3
"""Law 2986: Gravitational Wave Stochastic Background"""
import math
PHI = 1.618033988749895

def omega_gw(f, f_0=1e-8, Omega_0=1e-9, alpha=-2/3):
    return Omega_0 * (f / f_0)**alpha * PHI**(-f / f_0)

def simulate():
    print("=== Law 2986: Gravitational Wave Stochastic Background ===")
    f_0 = 1e-8
    for f_exp in [-9, -8.5, -8, -7.5, -7]:
        f = 10**f_exp
        Omega = omega_gw(f, f_0)
        print(f"  f = 10^{f_exp:.1f} Hz: Ω_gw = {Omega:.3e}")

if __name__ == "__main__":
    simulate()
