#!/usr/bin/env python3
"""Law 2955: CMB Anisotropy Peaks"""
import math
PHI = 1.618033988749895

def phi_peaks(l_0=220, n_peaks=6):
    return [l_0 * PHI**n for n in range(n_peaks)]

def simulate():
    print("=== Law 2955: CMB Anisotropy Peaks ===")
    peaks = phi_peaks()
    for i, l in enumerate(peaks):
        ratio = l/peaks[0] if i > 0 else 1.0
        print(f"  Peak {i}: ℓ = {l:.0f} (ratio to first: {ratio:.3f})")
    print(f"  ℓ_2/ℓ_1 = {peaks[1]/peaks[0]:.4f} ≈ φ = {PHI:.4f}")

if __name__ == "__main__":
    simulate()
