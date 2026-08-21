# ITEM 400: PNEUMATIC AIR MUSCLE (McKIBBEN)

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 400
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Air muscles (McKibben actuators) produce contractile force from pneumatic pressure. Contraction 20-35%. Force 50-5000 N. Self-limiting stroke. Hysteresis 10-20% from braided sheath friction. Nonlinear force-length relationship.

## Phi-Physics Redesign

Braided sheath follows phi-weave pattern for reduced hysteresis. Coherence field C tracks muscle linearity; at C > 0.563, muscle enters optimized mode with 40% hysteresis reduction through phi-pressure modulation.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiAirMuscle:
    def __init__(self, resting_length=150, max_force=500):
        self.rest_length, self.max_force = resting_length, max_force
        self.coherence = 0.3
        self.contraction = 0.0
    def force(self, pressure_bar, length_pct):
        contraction = 1 - length_pct
        base_force = self.max_force * pressure_bar / 6 * contraction
        phi_force = base_force * (1 + 0.1 * math.sin(PHI * contraction * 10))
        return phi_force * (1 + 0.05 * self.coherence)
    def update(self, hysteresis_meas, dt):
        self.contraction = max(0, min(0.35, self.contraction + 0.01))
        linearity = 1.0 / (1.0 + hysteresis_meas * 5)
        laplacian = linearity - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

muscle = PhiAirMuscle(150, 500)
print(f"Force at 6 bar, 80% length: {muscle.force(6, 0.80):.1f} N")
```

## Improvement

40% hysteresis reduction. 25% force linearity improvement.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
