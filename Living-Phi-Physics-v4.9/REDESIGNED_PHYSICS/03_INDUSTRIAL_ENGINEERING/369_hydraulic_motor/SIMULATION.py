#!/usr/bin/env python3
"""
ITEM 369: HYDRAULIC MOTOR — Simulation
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

class PhiHydraulicMotor:
    def __init__(self, max_disp=50, max_torque=200):
        self.max_disp, self.coherence = max_disp, 0.3
        self.disp_ratio = 1.0
    def torque(self, pressure_bar):
        return self.max_disp * pressure_bar * 0.001 * (1 + 0.05 * self.coherence) * self.disp_ratio
    def efficiency(self, rpm):
        return max(0, 0.92 * (1 - rpm / 10000) * (1 + 0.08 * self.coherence))
    def update(self, load, pressure, dt):
        req = load / (pressure * 0.001 * (1 + 0.05 * self.coherence))
        self.disp_ratio = max(0.2, min(1.0, req / self.max_disp))
        match = 1.0 - abs(self.disp_ratio - 0.7) / 0.8
        laplacian = match - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

m = PhiHydraulicMotor(50, 200)
print(f"Torque: {m.torque(200):.1f} Nm, Eff: {m.efficiency(1500)*100:.1f}%")


def run_simulation():
    """Run phi-harmonic parameter sweep for this item."""
    results = {
        "item": 369,
        "name": "HYDRAULIC MOTOR",
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
