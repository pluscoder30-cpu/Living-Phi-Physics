#!/usr/bin/env python3
"""Simulation for ITEM 017 — WATER HEATER"""
"""Author: Christopher David Ayotte — Soul Code [425, 434, 266, 775]"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_simulation():
    """Run simulation for ITEM 017 — WATER HEATER"""
    print("=" * 60)
    print("ITEM 017 -- WATER HEATER")
    print("Phi-Physics Simulation")
    print("=" * 60)
    print()

    from prototype import phi_standby_loss

    # Test phi_standby_loss with full phi-coupling
    result = phi_standby_loss(c=0.15, kappa=1.0)
    print(f"phi_standby_loss() => {result}")
    print()
    print("=" * 60)
    print("Simulation complete.")
    print("=" * 60)


if __name__ == "__main__":
    run_simulation()
