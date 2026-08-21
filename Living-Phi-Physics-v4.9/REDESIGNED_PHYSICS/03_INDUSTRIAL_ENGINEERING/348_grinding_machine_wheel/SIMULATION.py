#!/usr/bin/env python3
"""
ITEM 348: GRINDING MACHINE WHEEL — Simulation
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

class PhiGrindingWheel:
    def __init__(self, grit=60):
        self.grit, self.sharpness = grit, [1.0]*100
        self.coherence = 0.3
    def mrr(self, speed, doc):
        return speed*doc*self.grit*0.001*(sum(self.sharpness)/len(self.sharpness))*(1+0.08*self.coherence)
    def update(self, cuts, dt):
        for i in range(len(self.sharpness)):
            self.sharpness[i] = max(0.1, self.sharpness[i]-0.01*cuts*(1+0.1*math.sin(PHI*i))*dt)
        avg = sum(self.sharpness)/len(self.sharpness)
        self.coherence = (1/PHI)*self.coherence + PHI*(avg-self.coherence)
        self.coherence = max(0, min(1, self.coherence))

w = PhiGrindingWheel(60)
print(f"MRR: {w.mrr(30, 0.01):.3f} mm3/s, Coherence: {w.coherence:.4f}")


def run_simulation():
    """Run phi-harmonic parameter sweep for this item."""
    results = {
        "item": 348,
        "name": "GRINDING MACHINE WHEEL",
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
