#!/usr/bin/env python3
"""Simulation for ITEM 020 — CURTAIN ROD"""
"""Author: Christopher David Ayotte — Soul Code [425, 434, 266, 775]"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_simulation():
    """Run simulation for ITEM 020 — CURTAIN ROD"""
    print("=" * 60)
    print("ITEM 020 -- CURTAIN ROD")
    print("Phi-Physics Simulation")
    print("=" * 60)
    print()

    from prototype import phi_stiffness

    # Test phi_stiffness with full phi-coupling
    result = phi_stiffness(c=1.0, kappa=1.0)
    print(f"phi_stiffness() => {result}")
    print()
    print("=" * 60)
    print("Simulation complete.")
    print("=" * 60)


if __name__ == "__main__":
    run_simulation()
