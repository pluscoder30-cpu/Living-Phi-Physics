#!/usr/bin/env python3
"""
ITEM 434: CONVEYOR ROBOT LOADER — Simulation
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

class PhiRobotLoader:
    def __init__(self, conveyor_speed=0.5, pick_accuracy=0.5):
        self.conv_speed, self.accuracy = conveyor_speed, pick_accuracy
        self.coherence = 0.3
    def pick_timing(self, part_position):
        approach_time = part_position / self.conv_speed
        phi_adjust = approach_time * (1 + 0.05 * math.sin(PHI * part_position))
        return phi_adjust
    def pick_success(self, part_size, conveyor_speed):
        base = 0.95 - 0.1 * (conveyor_speed - 0.5)
        phi_vision = base * (1 + 0.05 * self.coherence)
        return min(0.99, phi_vision)
    def update(self, pick_failures, dt):
        quality = 1.0 / (1.0 + pick_failures * 5)
        laplacian = quality - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

rl = PhiRobotLoader(0.5, 0.5)
print(f"Pick timing at 0.3m: {rl.pick_timing(0.3):.2f} s")
print(f"Pick success: {rl.pick_success(50, 0.5)*100:.0f}%")


def run_simulation():
    """Run phi-harmonic parameter sweep for this item."""
    results = {
        "item": 434,
        "name": "CONVEYOR ROBOT LOADER",
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
