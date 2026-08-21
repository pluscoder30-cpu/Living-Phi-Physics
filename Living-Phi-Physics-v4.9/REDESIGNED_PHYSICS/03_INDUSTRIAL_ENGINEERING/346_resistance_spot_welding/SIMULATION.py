#!/usr/bin/env python3
"""
ITEM 346: RESISTANCE SPOT WELDING — Simulation
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

class PhiSpotWeld:
    def __init__(self, t_mm=1.0):
        self.t = t_mm
        self.nugget, self.coherence = 0.0, 0.3
    def phi_pulse(self, t, dur=5):
        I = 8000
        return I*(1+0.1*(PHI-1)*math.exp(-t/(dur*0.3))-0.08*math.exp(-t/(dur*0.7)))
    def update(self, I, force, dt):
        g = (I*dt*1000)**0.5*0.1/math.sqrt(force)*(1+0.05*self.coherence)
        self.nugget = min(g, 6.0)
        r = min(self.nugget/(5*math.sqrt(self.t)), 1.0)
        self.coherence = (1/PHI)*self.coherence + PHI*(r-self.coherence)
        self.coherence = max(0, min(1, self.coherence))

w = PhiSpotWeld(1.0)
for i in range(50): w.update(w.phi_pulse(i*0.1), 3000, 0.1)
print(f"Nugget: {w.nugget:.2f} mm, Coherence: {w.coherence:.4f}")


def run_simulation():
    """Run phi-harmonic parameter sweep for this item."""
    results = {
        "item": 346,
        "name": "RESISTANCE SPOT WELDING",
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
