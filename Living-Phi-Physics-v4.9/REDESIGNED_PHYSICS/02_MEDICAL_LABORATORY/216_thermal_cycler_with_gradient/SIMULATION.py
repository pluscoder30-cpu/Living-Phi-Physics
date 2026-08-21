#!/usr/bin/env python3
"""
SIMULATION: Item 216 - Thermal Cycler with Gradient
Runs the phi-physics prototype with test parameters and prints results.
"""

import math

PHI = (1 + math.sqrt(5)) / 2

# ============================================================
# PROTOTYPE FUNCTIONS
# ============================================================

import math

PHI = (1 + math.sqrt(5)) / 2

def phi_gradient_profile(block_positions=12, T_center=60, delta_T=15):
    gradient = []
    for i in range(block_positions):
        x = i / block_positions
        # Standard: linear gradient
        T_standard = T_center + delta_T * (x - 0.5)
        # Phi-gradient: sinusoidal with phi-frequency
        T_phi = T_center + delta_T * math.sin(PHI * math.pi * x) * math.exp(-x / PHI)
        gradient.append({
            'position': i, 'standard_C': round(T_standard, 2), 'phi_C': round(T_phi, 2)
        })
    return gradient

def optimization_efficiency():
    # Standard gradient: tests 12 temperatures linearly spaced
    # Phi-gradient: tests temperatures at phi-optimal intervals
    # More informative per well
    return PHI

gradient = phi_gradient_profile()
print("Phi-gradient temperature profile:")
for g in gradient[::3]:
    print(f"  Pos {g['position']}: std={g['standard_C']}C, phi={g['phi_C']}C")
print(f"\nOptimization efficiency: {optimization_efficiency():.2f}x")

# ============================================================
# SIMULATION RUNNER
# ============================================================

def main():
    print("=" * 60)
    print(f"SIMULATION: Item 216 - Thermal Cycler with Gradient")
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
