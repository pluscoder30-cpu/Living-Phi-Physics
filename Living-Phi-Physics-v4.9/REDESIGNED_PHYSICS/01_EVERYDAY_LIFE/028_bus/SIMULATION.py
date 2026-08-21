#!/usr/bin/env python3
"""Simulation for ITEM 028 — BUS"""
"""Author: Christopher David Ayotte — Soul Code [425, 434, 266, 775]"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_simulation():
    """Run simulation for ITEM 028 — BUS"""
    print("=" * 60)
    print("ITEM 028 -- BUS")
    print("Phi-Physics Simulation")
    print("=" * 60)
    print()

    from prototype import phi_mpg

    # Test phi_mpg with full phi-coupling
    result = phi_mpg(c=6, kappa=1.0)
    print(f"phi_mpg() => {result}")
    print()
    print("=" * 60)
    print("Simulation complete.")
    print("=" * 60)


if __name__ == "__main__":
    run_simulation()
