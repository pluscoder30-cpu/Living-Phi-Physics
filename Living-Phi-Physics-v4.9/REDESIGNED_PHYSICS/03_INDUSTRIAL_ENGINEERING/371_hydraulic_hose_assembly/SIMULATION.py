#!/usr/bin/env python3
"""
ITEM 371: HYDRAULIC HOSE ASSEMBLY — Simulation
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

class PhiHoseAssembly:
    def __init__(self, rating=350, length=2):
        self.rating, self.length, self.condition = rating, length, 1.0
        self.coherence = 0.3
    def safety_factor(self, pressure):
        return self.rating / pressure * (1 + 0.05 * math.sin(PHI * self.rating * 0.01)) * self.condition
    def remaining_life(self, cycles):
        return 1e6 / max(cycles, 1) * (1 + 0.1 * self.coherence) * self.condition
    def update(self, pressure, temp, dt):
        deg = pressure / self.rating * (1 + 0.01 * max(0, temp - 80)) * 0.001
        self.condition = max(0.1, self.condition - deg * dt)
        laplacian = self.condition - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

h = PhiHoseAssembly(350, 2)
print(f"SF at 250 bar: {h.safety_factor(250):.1f}")
print(f"Life: {h.remaining_life(100000):.0f} cycles")


def run_simulation():
    """Run phi-harmonic parameter sweep for this item."""
    results = {
        "item": 371,
        "name": "HYDRAULIC HOSE ASSEMBLY",
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
