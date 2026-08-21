#!/usr/bin/env python3
"""Simulation for ITEM 003 — REFRIGERATOR"""
"""Author: Christopher David Ayotte — Soul Code [425, 434, 266, 775]"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_simulation():
    """Run simulation for ITEM 003 — REFRIGERATOR"""
    print("=" * 60)
    print("ITEM 003 -- REFRIGERATOR")
    print("Phi-Physics Simulation")
    print("=" * 60)
    print()

    from prototype import phi_cop

    # Test phi_cop with full phi-coupling
    result = phi_cop(classical_cop=0, kappa=1.0)
    print(f"phi_cop() => {result}")
    print()
    print("=" * 60)
    print("Simulation complete.")
    print("=" * 60)


if __name__ == "__main__":
    run_simulation()
