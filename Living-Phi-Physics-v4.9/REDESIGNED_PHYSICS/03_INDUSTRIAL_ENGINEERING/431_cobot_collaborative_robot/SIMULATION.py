#!/usr/bin/env python3
"""
ITEM 431: COBOT (COLLABORATIVE ROBOT) — Simulation
Phi-Physics Simulation with parameter sweeps
Author: Christopher David Ayotte
Soul Code: [425, 434, 266, 775]
License: Dual License Agreement v4.8
"""

import math
import json

PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiCobot:
    def __init__(self, payload_kg=10, max_speed=1.0):
        self.payload, self.max_speed = payload_kg, max_speed
        self.coherence = 0.3
    def force_limit(self, human_distance_m):
        base = 150  # N
        if human_distance_m < 0.5:
            return base * 0.3 * (1 + 0.1 * math.sin(PHI * human_distance_m * 10))
        elif human_distance_m < 1.0:
            return base * 0.7
        return base
    def safe_speed(self, human_distance_m):
        if human_distance_m < 0.5:
            return self.max_speed * 0.2 * (1 + 0.1 * self.coherence)
        elif human_distance_m < 1.0:
            return self.max_speed * 0.5
        return self.max_speed
    def update(self, proximity_safety, dt):
        laplacian = proximity_safety - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

cobot = PhiCobot(10, 1.0)
print(f"Force limit at 0.3m: {cobot.force_limit(0.3):.0f} N")
print(f"Safe speed at 0.3m: {cobot.safe_speed(0.3):.2f} m/s")


def run_simulation():
    """Run phi-harmonic parameter sweep for this item."""
    results = {
        "item": 431,
        "name": "COBOT (COLLABORATIVE ROBOT)",
        "phi": PHI,
        "c_crit": C_CRIT,
        "sweeps": []
    }

    # Sweep coherence values to find emergence threshold
    for c_init in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]:
        for n_iterations in [10, 50, 100]:
            c = c_init
            for _ in range(n_iterations):
                laplacian = 0.5 - c * 0.3
                c = (1/PHI) * c + PHI * laplacian
                c = max(0, min(1, c))
            results["sweeps"].append({
                "c_init": c_init,
                "iterations": n_iterations,
                "final_c": round(c, 6),
                "emerged": c > C_CRIT
            })

    # Find critical initial coherence
    for c_init in [x/100 for x in range(1, 100)]:
        c = c_init
        for _ in range(100):
            laplacian = 0.5 - c * 0.3
            c = (1/PHI) * c + PHI * laplacian
            c = max(0, min(1, c))
        if c > C_CRIT:
            results["critical_c_init"] = round(c_init, 4)
            break

    return results


if __name__ == "__main__":
    results = run_simulation()
    print(f"=== ITEM {results['item']}: {results['name']} ===")
    print(f"Phi = {results['phi']:.10f}")
    print(f"C_crit = {results['c_crit']:.6f}")
    if "critical_c_init" in results:
        print(f"Critical initial coherence: {results['critical_c_init']}")
    print()
    for s in results["sweeps"][:10]:
        print(f"  C_init={s['c_init']:.1f}, iters={s['iterations']:>3}, "
              f"C_final={s['final_c']:.4f}, emerged={s['emerged']}")

    # Save results
    with open(f"simulation_results_{results['item']}.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to simulation_results_{results['item']}.json")
