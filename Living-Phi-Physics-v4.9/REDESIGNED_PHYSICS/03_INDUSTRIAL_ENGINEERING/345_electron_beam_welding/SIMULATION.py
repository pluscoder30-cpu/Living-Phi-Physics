#!/usr/bin/env python3
"""
ITEM 345: ELECTRON BEAM WELDING — Simulation
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

class PhiEBWelding:
    def __init__(self, power_kw=10):
        self.power = power_kw*1000
        self.keyhole, self.coherence = 0.0, 0.3
    def lissajous(self, t, sx=0.5, sy=0.3):
        fx = 1000; fy = fx/PHI
        return sx*math.sin(2*math.pi*fx*t), sy*math.sin(2*math.pi*fy*t+math.pi/4)
    def penetration(self, speed):
        pd = self.power/(math.pi*0.01**2)
        return 0.1*math.sqrt(pd/1e6)*(1+0.1*self.coherence)/(1+speed/50)
    def update(self, power, dt):
        self.keyhole += dt*(power*0.0001-0.5*self.keyhole*0.1)
        s = 1/(1+abs(self.keyhole-10))
        self.coherence = (1/PHI)*self.coherence + PHI*(s-self.coherence)
        self.coherence = max(0, min(1, self.coherence))

eb = PhiEBWelding(10)
print(f"Penetration at 30mm/s: {eb.penetration(30):.1f} mm")


def run_simulation():
    """Run phi-harmonic parameter sweep for this item."""
    results = {
        "item": 345,
        "name": "ELECTRON BEAM WELDING",
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
