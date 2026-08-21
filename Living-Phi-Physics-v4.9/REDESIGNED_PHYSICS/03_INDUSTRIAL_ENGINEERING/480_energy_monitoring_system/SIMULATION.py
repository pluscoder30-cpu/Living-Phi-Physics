#!/usr/bin/env python3
"""
ITEM 480: ENERGY MONITORING SYSTEM — Simulation
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

class PhiEnergyMonitor:
    def __init__(self, baseline_kwh=1000, n_meters=10):
        self.baseline, self.n_meters = baseline_kwh, n_meters
        self.coherence = 0.3
        self.readings = []
    def add_reading(self, kwh):
        self.readings.append(kwh)
        if len(self.readings) > 100:
            self.readings = self.readings[-100:]
    def optimization_score(self):
        if len(self.readings) < 10:
            return 0
        avg = sum(self.readings) / len(self.readings)
        return 1 - avg / self.baseline
    def phi_sample_interval(self):
        base_interval = 5  # minutes
        return base_interval * PHI**(-self.coherence)
    def update(self, efficiency, dt):
        self.coherence = max(0, min(1, efficiency))
        laplacian = efficiency - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

em = PhiEnergyMonitor(1000, 10)
for v in [950, 980, 960, 970, 940]:
    em.add_reading(v)
print(f"Optimization score: {em.optimization_score()*100:.0f}%")
print(f"Phi sample interval: {em.phi_sample_interval():.1f} min")


def run_simulation():
    """Run phi-harmonic parameter sweep for this item."""
    results = {
        "item": 480,
        "name": "ENERGY MONITORING SYSTEM",
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
