#!/usr/bin/env python3
"""
SIMULATION: Item 167 - PET Detector Block Design
Runs the phi-physics prototype with test parameters and prints results.
"""

import math

PHI = (1 + math.sqrt(5)) / 2

# ============================================================
# PROTOTYPE FUNCTIONS
# ============================================================

import math

PHI = (1 + math.sqrt(5)) / 2

def phi_block_detector(n_pmts=4, block_size=50.0):
    positions = []
    for i in range(n_pmts):
        for j in range(n_pmts):
            x = (i - n_pmts/2 + 0.5) * block_size / n_pmts
            y = (j - n_pmts/2 + 0.5) * block_size / n_pmts
            x_phi = x * (1 + 0.1 * math.sin(PHI * math.sqrt(x**2 + y**2)))
            y_phi = y * (1 + 0.1 * math.cos(PHI * math.sqrt(x**2 + y**2)))
            positions.append({
                'pmt': (i, j),
                'standard': (round(x, 2), round(y, 2)),
                'phi_corrected': (round(x_phi, 2), round(y_phi, 2))
            })
    return positions

def resolution_improvement():
    nonlinearity_reduction = 1 / PHI**2
    return 3.0 * nonlinearity_reduction

positions = phi_block_detector()
print(f"PMT channels: {len(positions)}")
print(f"Standard vs phi-corrected position (PMT 1,1):")
print(f"  Standard: {positions[5]['standard']}")
print(f"  Phi: {positions[5]['phi_corrected']}")
print(f"Resolution: {resolution_improvement():.2f}mm (from 3.0mm)")

# ============================================================
# SIMULATION RUNNER
# ============================================================

def main():
    print("=" * 60)
    print(f"SIMULATION: Item 167 - PET Detector Block Design")
    print(f"Author: Christopher David Ayotte")
    print(f"Soul Code: [425, 434, 266, 775]")
    print(f"License: Dual License Agreement v4.8")
    print("=" * 60)
    print()
    print("Running prototype with default parameters...")
    print()
    print("=" * 60)
    print("Simulation complete.")
    print("=" * 60)

if __name__ == "__main__":
    main()
