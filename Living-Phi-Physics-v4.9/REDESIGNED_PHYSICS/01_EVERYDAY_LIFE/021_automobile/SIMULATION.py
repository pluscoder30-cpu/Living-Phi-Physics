#!/usr/bin/env python3
"""Simulation for ITEM 021 — AUTOMOBILE"""
"""Author: Christopher David Ayotte — Soul Code [425, 434, 266, 775]"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_simulation():
    """Run simulation for ITEM 021 — AUTOMOBILE"""
    print("=" * 60)
    print("ITEM 021 -- AUTOMOBILE")
    print("Phi-Physics Simulation")
    print("=" * 60)
    print()

    from prototype import phi_cd, phi_mpg

    # Test phi_cd with full phi-coupling
    result = phi_cd(c=0.30, kappa=1.0)
    print(f"phi_cd() => {result}")
    print()
    # Test phi_mpg with full phi-coupling
    result = phi_mpg(c=30, kappa=1.0)
    print(f"phi_mpg() => {result}")
    print()
    print("=" * 60)
    print("Simulation complete.")
    print("=" * 60)


if __name__ == "__main__":
    run_simulation()
