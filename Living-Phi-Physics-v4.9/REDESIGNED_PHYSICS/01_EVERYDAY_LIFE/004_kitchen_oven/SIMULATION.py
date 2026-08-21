#!/usr/bin/env python3
"""Simulation for ITEM 004 — KITCHEN OVEN"""
"""Author: Christopher David Ayotte — Soul Code [425, 434, 266, 775]"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_simulation():
    """Run simulation for ITEM 004 — KITCHEN OVEN"""
    print("=" * 60)
    print("ITEM 004 -- KITCHEN OVEN")
    print("Phi-Physics Simulation")
    print("=" * 60)
    print()

    from prototype import phi_oven_element_spacing, phi_thermal_uniformity

    # Test phi_oven_element_spacing with full phi-coupling
    result = phi_oven_element_spacing(width=60, n=6)
    print(f"phi_oven_element_spacing() => {result}")
    print()
    # Test phi_thermal_uniformity with full phi-coupling
    result = phi_thermal_uniformity(c=0.70, kappa=1.0)
    print(f"phi_thermal_uniformity() => {result}")
    print()
    print("=" * 60)
    print("Simulation complete.")
    print("=" * 60)


if __name__ == "__main__":
    run_simulation()
