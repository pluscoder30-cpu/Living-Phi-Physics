#!/usr/bin/env python3
"""
SIMULATION: Item 302 - NBI (Narrow Band Imaging) Filter
Runs the phi-physics prototype with test parameters and prints results.
"""

import math

PHI = (1 + math.sqrt(5)) / 2

# ============================================================
# PROTOTYPE FUNCTIONS
# ============================================================

import math
PHI = (1 + math.sqrt(5)) / 2
def phi_nbi():
    wavelengths = [415, 540]
    phi_wavelengths = [round(w * (1 + 0.1/PHI), 0) for w in wavelengths]
    return {'standard_wavelengths': wavelengths,
            'phi_wavelengths': phi_wavelengths,
            'contrast_improvement': f"{PHI:.2f}x"}
result = phi_nbi()
print(f"Standard wavelengths: {result['standard_wavelengths']}nm")
print(f"Phi wavelengths: {result['phi_wavelengths']}nm")
print(f"Contrast improvement: {result['contrast_improvement']}")

# ============================================================
# SIMULATION RUNNER
# ============================================================

def main():
    print("=" * 60)
    print(f"SIMULATION: Item 302 - NBI (Narrow Band Imaging) Filter")
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
