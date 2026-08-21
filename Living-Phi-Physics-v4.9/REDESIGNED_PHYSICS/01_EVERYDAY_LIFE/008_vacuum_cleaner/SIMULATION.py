#!/usr/bin/env python3
"""Simulation for ITEM 008 — VACUUM CLEANER"""
"""Author: Christopher David Ayotte — Soul Code [425, 434, 266, 775]"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_simulation():
    """Run simulation for ITEM 008 — VACUUM CLEANER"""
    print("=" * 60)
    print("ITEM 008 -- VACUUM CLEANER")
    print("Phi-Physics Simulation")
    print("=" * 60)
    print()

    from prototype import phi_nozzle_profile, phi_suction_efficiency

    # Test phi_nozzle_profile with full phi-coupling
    result = phi_nozzle_profile(d=3.5)
    print(f"phi_nozzle_profile() => {result}")
    print()
    # Test phi_suction_efficiency with full phi-coupling
    result = phi_suction_efficiency(c=0.18, kappa=1.0)
    print(f"phi_suction_efficiency() => {result}")
    print()
    print("=" * 60)
    print("Simulation complete.")
    print("=" * 60)


if __name__ == "__main__":
    run_simulation()
