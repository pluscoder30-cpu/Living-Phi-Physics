#!/usr/bin/env python3
"""Simulation for ITEM 001 — INCANDESCENT LIGHT BULB"""
"""Author: Christopher David Ayotte — Soul Code [425, 434, 266, 775]"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_simulation():
    """Run simulation for ITEM 001 — INCANDESCENT LIGHT BULB"""
    print("=" * 60)
    print("ITEM 001 -- INCANDESCENT LIGHT BULB")
    print("Phi-Physics Simulation")
    print("=" * 60)
    print()

    from prototype import phi_light_bulb_efficiency, phi_filament_spectrum

    # Test phi_light_bulb_efficiency with full phi-coupling
    result = phi_light_bulb_efficiency(classical_efficiency=0.05, kappa=1.0)
    print(f"phi_light_bulb_efficiency() => {result}")
    print()
    # Test phi_filament_spectrum with full phi-coupling
    result = phi_filament_spectrum(temp_k=3000, kappa=1.0)
    print(f"phi_filament_spectrum() => {result}")
    print()
    print("=" * 60)
    print("Simulation complete.")
    print("=" * 60)


if __name__ == "__main__":
    run_simulation()
