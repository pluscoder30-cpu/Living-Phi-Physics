#!/usr/bin/env python3
"""
ITEM 474: VARIABLE REFRIGERANT FLOW SYSTEM — Simulation
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

class PhiVRF:
    def __init__(self, capacity_kw=20, n_zones=8):
        self.capacity, self.n_zones = capacity_kw, n_zones
        self.coherence = 0.3
    def zone_distribution(self):
        return [self.capacity / self.n_zones * (1 + 0.05 * math.sin(PHI * i)) for i in range(self.n_zones)]
    def system_efficiency(self, load_balance):
        base = 0.85
        balance_factor = 1 - 0.3 * abs(load_balance - 0.5)
        return base * balance_factor * (1 + 0.05 * self.coherence)
    def update(self, balance_error, dt):
        quality = 1.0 / (1.0 + balance_error)
        laplacian = quality - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

vrf = PhiVRF(20, 8)
dist = vrf.zone_distribution()
print(f"Zone distribution: {[round(d,1) for d in dist[:4]]} kW")
print(f"Efficiency at balanced load: {vrf.system_efficiency(0.5)*100:.0f}%")


def run_simulation():
    """Run phi-harmonic parameter sweep for this item."""
    results = {
        "item": 474,
        "name": "VARIABLE REFRIGERANT FLOW SYSTEM",
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
