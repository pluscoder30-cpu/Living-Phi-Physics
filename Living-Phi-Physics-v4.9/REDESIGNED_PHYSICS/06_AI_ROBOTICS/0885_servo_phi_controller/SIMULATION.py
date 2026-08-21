#!/usr/bin/env python3
"""SIMULATION: 885 - Phi-Harmonic Servo Controller"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from prototype import phi_optimize, PHI

def simulate():
    print("=" * 60)
    print(f"SIMULATION: 885 - Phi-Harmonic Servo Controller")
    print("=" * 60)

    configs = [("Baseline", 1.0), ("Moderate", 0.5), ("Aggressive", 0.3), ("Ultra", 0.15)]

    for label, delta in configs:
        result = phi_optimize(100.0, delta=delta)
        reduction = phi_optimize(100.0, delta=delta, direction="reduce")
        print(f"\n--- {label} (delta={delta}) ---")
        print(f"  Phi-improved: {result:.2f}")
        print(f"  Phi-reduced: {reduction:.2f}")

    print("\n" + "=" * 60)
    print("VALIDATION CHECKS")
    print("=" * 60)
    r1 = phi_optimize(100.0, delta=0.5)
    r2 = phi_optimize(100.0, delta=0.3)
    assert r1 > 100.0, "Improvement should exceed baseline"
    assert r1 > r2, "Larger delta = larger improvement"
    print("All assertions passed.")

if __name__ == "__main__":
    simulate()
