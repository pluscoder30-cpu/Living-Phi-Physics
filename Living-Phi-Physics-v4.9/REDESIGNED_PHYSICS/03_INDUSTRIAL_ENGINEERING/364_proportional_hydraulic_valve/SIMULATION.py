#!/usr/bin/env python3
"""
ITEM 364: PROPORTIONAL HYDRAULIC VALVE — Simulation
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

class PhiProportionalValve:
    def __init__(self, max_flow=50, dead_band=0.1):
        self.max_flow, self.dead_band = max_flow, dead_band
        self.hysteresis, self.coherence, self.last = 0.05, 0.3, 0.0
    def flow_output(self, cmd):
        db = self.dead_band * (1 - 0.8 * self.coherence) if self.coherence > C_CRIT else self.dead_band
        adj = max(0, abs(cmd) - db) * (1 if cmd >= 0 else -1)
        hyst = self.hysteresis * (1 - 0.5 * self.coherence) * (1 if cmd > self.last else -1)
        self.last = cmd
        return max(-self.max_flow, min(self.max_flow, self.max_flow * (adj + hyst) / 100))
    def update_cal(self, measured, commanded, dt):
        err = abs(measured - commanded) / max(abs(commanded), 0.1)
        laplacian = 1.0 / (1.0 + err * 10) - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

valve = PhiProportionalValve(50, 0.1)
print(f"Flow at 75%: {valve.flow_output(75):.1f} L/min")
print(f"Hysteresis: {valve.hysteresis*100*(1-0.5*valve.coherence):.1f}%")


def run_simulation():
    """Run phi-harmonic parameter sweep for this item."""
    results = {
        "item": 364,
        "name": "PROPORTIONAL HYDRAULIC VALVE",
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
