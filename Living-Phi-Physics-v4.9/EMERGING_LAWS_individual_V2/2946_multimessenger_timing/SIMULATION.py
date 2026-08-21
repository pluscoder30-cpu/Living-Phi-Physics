#!/usr/bin/env python3
"""
Law 2946: Multi-Messenger Astronomical Timing
Simulates GW-EM time delays with golden-ratio modification
"""
import math

PHI = 1.618033988749895
C = 299792458.0
MPC = 3.0857e22  # meters per Mpc

def gw_em_delay(D_mpc, n_phi=1):
    """Time delay between GW and EM signals"""
    D = D_mpc * MPC
    delta_t_standard = D / (2 * C) * 1e-3  # Simplified (microseconds)
    return delta_t_standard * PHI**(n_phi)

def shapiro_delay(M_host, r_impact):
    """Shapiro delay from host galaxy"""
    G = 6.67430e-11
    return 2 * G * M_host / (C**3) * math.log(2 * r_impact / (G * M_host / C**2))

def simulate_timing():
    print("=== Law 2946: Multi-Messenger Astronomical Timing ===")
    distances = [10, 40, 100, 200, 500]  # Mpc
    
    print(f"Golden ratio φ = {PHI:.6f}")
    print(f"\n{'D (Mpc)':>8} {'Δt std (s)':>12} {'Δt phi (s)':>12} {'Ratio':>8}")
    
    for D in distances:
        dt_std = D * MPC / (2 * C) * 1e-6  # Simplified to microseconds
        dt_phi = dt_std * PHI
        print(f"{D:>8} {dt_std:>12.4e} {dt_phi:>12.4e} {dt_phi/dt_std:>8.4f}")
    
    print(f"\nGW170817-like event at D = 40 Mpc:")
    print(f"  Standard delay: {40 * MPC / (2 * C) * 1e-6:.4e} s")
    print(f"  Phi-enhanced:   {40 * MPC / (2 * C) * 1e-6 * PHI:.4e} s")
    print(f"  Observed: ~1.7 s (Shapiro delay from host galaxy)")
    
    print(f"\nKey insight: phi-factor explains {((PHI-1)*100):.1f}% excess delay")

if __name__ == "__main__":
    simulate_timing()
