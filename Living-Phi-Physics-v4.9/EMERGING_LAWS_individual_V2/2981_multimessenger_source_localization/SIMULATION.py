#!/usr/bin/env python3
"""Law 2981: Multi-Messenger Source Localization"""
import math
PHI = 1.618033988749895

def localization_area(D_mpc, sigma_t_ms=1.0, n_det=3):
    D = D_mpc * 3.0857e22
    c = 299792458.0
    sigma_t = sigma_t_ms * 1e-3
    return 4 * math.pi * c**2 * sigma_t**2 / (D**2 * PHI**n_det)

def simulate():
    print("=== Law 2981: Multi-Messenger Source Localization ===")
    for D in [10, 40, 100, 500]:
        area = localization_area(D, 1.0, 4)
        print(f"  D = {D:>3} Mpc: ΔΩ = {area:.4f} deg²")
    print(f"  φ-improvement for 4 detectors: {PHI**4:.2f}x")

if __name__ == "__main__":
    simulate()
