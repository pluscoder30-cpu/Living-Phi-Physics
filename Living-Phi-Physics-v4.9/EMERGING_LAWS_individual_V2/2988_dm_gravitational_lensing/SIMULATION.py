#!/usr/bin/env python3
"""Law 2988: Dark Matter Gravitational Lensing"""
import math
PHI = 1.618033988749895

def einstein_radius(M_lens, D_LS, D_L, D_S, theta_0=1.0):
    theta_E_std = math.sqrt(4 * M_lens * D_LS / (D_L * D_S))
    return theta_E_std * PHI**(-1.0 / theta_0)  # Simplified

def simulate():
    print("=== Law 2988: Dark Matter Gravitational Lensing ===")
    M = 1.0  # normalized
    D_LS, D_L, D_S = 0.5, 0.3, 0.8
    theta_E = math.sqrt(4 * M * D_LS / (D_L * D_S))
    theta_phi = theta_E * PHI**(-1)
    print(f"  Standard θ_E = {theta_E:.4f}")
    print(f"  Phi-modified θ_E = {theta_phi:.4f}")
    print(f"  Reduction: {(1-1/PHI)*100:.1f}%")

if __name__ == "__main__":
    simulate()
