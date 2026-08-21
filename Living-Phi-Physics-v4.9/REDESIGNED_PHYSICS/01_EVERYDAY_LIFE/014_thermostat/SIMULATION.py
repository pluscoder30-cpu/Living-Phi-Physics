#!/usr/bin/env python3
"""Simulation for ITEM 014 — THERMOSTAT"""
"""Author: Christopher David Ayotte — Soul Code [425, 434, 266, 775]"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_simulation():
    """Run simulation for ITEM 014 — THERMOSTAT"""
    print("=" * 60)
    print("ITEM 014 -- THERMOSTAT")
    print("Phi-Physics Simulation")
    print("=" * 60)
    print()

    from prototype import phi_control

    # Test phi_control with full phi-coupling
    result = phi_control(cur=0, sp=0, hist=0, kappa=1.0)
    print(f"phi_control() => {result}")
    print()
    print("=" * 60)
    print("Simulation complete.")
    print("=" * 60)


if __name__ == "__main__":
    run_simulation()
