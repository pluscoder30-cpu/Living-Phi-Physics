#!/usr/bin/env python3
"""Simulation for ITEM 006 — WASHING MACHINE"""
"""Author: Christopher David Ayotte — Soul Code [425, 434, 266, 775]"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_simulation():
    """Run simulation for ITEM 006 — WASHING MACHINE"""
    print("=" * 60)
    print("ITEM 006 -- WASHING MACHINE")
    print("Phi-Physics Simulation")
    print("=" * 60)
    print()

    from prototype import phi_water_usage

    # Test phi_water_usage with full phi-coupling
    result = phi_water_usage(c=60, kappa=1.0)
    print(f"phi_water_usage() => {result}")
    print()
    print("=" * 60)
    print("Simulation complete.")
    print("=" * 60)


if __name__ == "__main__":
    run_simulation()
