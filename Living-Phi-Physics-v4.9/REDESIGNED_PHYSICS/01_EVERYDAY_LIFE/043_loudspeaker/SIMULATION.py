#!/usr/bin/env python3
"""Simulation for ITEM 043 — LOUDSPEAKER"""
"""Author: Christopher David Ayotte — Soul Code [425, 434, 266, 775]"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_simulation():
    """Run simulation for ITEM 043 — LOUDSPEAKER"""
    print("=" * 60)
    print("ITEM 043 -- LOUDSPEAKER")
    print("Phi-Physics Simulation")
    print("=" * 60)
    print()

    from prototype import phi_resp

    # Test phi_resp with full phi-coupling
    result = phi_resp(freqs=[100,500,1000,5000,10000], kappa=1.0)
    print(f"phi_resp() => {result}")
    print()
    print("=" * 60)
    print("Simulation complete.")
    print("=" * 60)


if __name__ == "__main__":
    run_simulation()
