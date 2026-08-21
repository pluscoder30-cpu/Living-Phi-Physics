#!/usr/bin/env python3
"""Simulation for ITEM 002 — CEILING FAN"""
"""Author: Christopher David Ayotte — Soul Code [425, 434, 266, 775]"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_simulation():
    """Run simulation for ITEM 002 — CEILING FAN"""
    print("=" * 60)
    print("ITEM 002 -- CEILING FAN")
    print("Phi-Physics Simulation")
    print("=" * 60)
    print()

    from prototype import phi_blade_angles, phi_fan_efficiency

    # Test phi_blade_angles with full phi-coupling
    result = phi_blade_angles(n_blades=5, base_pitch_deg=15)
    print(f"phi_blade_angles() => {result}")
    print()
    # Test phi_fan_efficiency with full phi-coupling
    result = phi_fan_efficiency(classical_eta=0, kappa=1.0)
    print(f"phi_fan_efficiency() => {result}")
    print()
    print("=" * 60)
    print("Simulation complete.")
    print("=" * 60)


if __name__ == "__main__":
    run_simulation()
