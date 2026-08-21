#!/usr/bin/env python3
"""
SIMULATION: Item 165 - X-Ray Tube Collimator
Runs the phi-physics prototype with test parameters and prints results.
"""

import math

PHI = (1 + math.sqrt(5)) / 2

# ============================================================
# PROTOTYPE FUNCTIONS
# ============================================================

import math

PHI = (1 + math.sqrt(5)) / 2

def phi_collimator_leaves(n_leaves=32):
    leaves = []
    for i in range(n_leaves):
        theta = i * 2 * math.pi / PHI
        thickness_mm = 2.0 * (1 + (1/PHI)**i)
        leakage = 1.0 / PHI**(2 * (i % 3 + 1))
        leaves.append({
            'leaf': i,
            'theta_deg': round(math.degrees(theta) % 360, 1),
            'thickness_mm': round(thickness_mm, 3),
            'leakage_pct': round(leakage * 100, 3)
        })
    return leaves

def penumbra_improvement():
    return 1.0 / PHI

leaves = phi_collimator_leaves()
print(f"Collimator leaves: {len(leaves)}")
for l in leaves[:3]:
    print(f"  Leaf {l['leaf']}: theta={l['theta_deg']} deg, thick={l['thickness_mm']}mm, leak={l['leakage_pct']}%")
print(f"Effective penumbra: {penumbra_improvement():.3f}mm")

# ============================================================
# SIMULATION RUNNER
# ============================================================

def main():
    print("=" * 60)
    print(f"SIMULATION: Item 165 - X-Ray Tube Collimator")
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
