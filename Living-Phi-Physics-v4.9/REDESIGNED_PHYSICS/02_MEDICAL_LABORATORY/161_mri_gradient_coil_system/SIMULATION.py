#!/usr/bin/env python3
"""
SIMULATION: Item 161 - MRI Gradient Coil System
Runs the phi-physics prototype with test parameters and prints results.
"""

import math

PHI = (1 + math.sqrt(5)) / 2

# ============================================================
# PROTOTYPE FUNCTIONS
# ============================================================

import math

PHI = (1 + math.sqrt(5)) / 2

def phi_gradient_field(r, theta, G0=1.0, sigma=1.0, kappa=0.1):
    G_linear = G0 * r
    phi_mod = 1 + kappa * (PHI - 1)
    spiral_decay = math.exp(-r**2 / (2 * sigma**2))
    G_phi = G_linear * phi_mod * spiral_decay * math.cos(PHI * theta)
    return G_phi

def eddy_current_ratio():
    suppression = 1 / PHI**3
    return suppression

print(f"Gradient at r=1, theta=0: {phi_gradient_field(1.0, 0.0):.4f}")
print(f"Eddy suppression ratio: {eddy_current_ratio():.4f}")

# ============================================================
# SIMULATION RUNNER
# ============================================================

def main():
    print("=" * 60)
    print(f"SIMULATION: Item 161 - MRI Gradient Coil System")
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
