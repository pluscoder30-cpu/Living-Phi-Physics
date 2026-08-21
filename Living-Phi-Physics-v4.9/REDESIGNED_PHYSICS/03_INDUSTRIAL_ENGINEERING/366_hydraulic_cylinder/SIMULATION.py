#!/usr/bin/env python3
"""
ITEM 366: HYDRAULIC CYLINDER — Simulation
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

class PhiHydraulicCylinder:
    def __init__(self, bore_mm=100, stroke_mm=500):
        self.bore, self.stroke = bore_mm, stroke_mm
        self.seal_wear, self.coherence = 0.0, 0.3
    def force_output(self, pressure_bar):
        area = math.pi * (self.bore/2)**2 * 1e-6
        return pressure_bar * 1e5 * area * (1 - 0.02 * (1 + 0.1 * math.sin(PHI * self.seal_wear * 100)))
    def cushioning(self, pos_pct):
        if pos_pct > 0.9:
            return (1 - pos_pct) * 10 * (1 + 0.2 * math.sin(PHI * pos_pct * 100))
        return 1.0
    def update_seal(self, cycles, dt):
        self.seal_wear = min(1.0, self.seal_wear + dt * cycles * 1e-6)
        laplacian = (1 - self.seal_wear) - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

cyl = PhiHydraulicCylinder(100, 500)
print(f"Force at 200 bar: {cyl.force_output(200)/1000:.1f} kN")
print(f"Cushion at 95%: {cyl.cushioning(0.95):.3f}")


def run_simulation():
    """Run phi-harmonic parameter sweep for this item."""
    results = {
        "item": 366,
        "name": "HYDRAULIC CYLINDER",
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
