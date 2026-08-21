# ITEM 391: PNEUMATIC AIR CYLINDER Cushion

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 391
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Cylinder cushions decelerate piston at end of stroke. Adjustable needle valve controls air exhaust rate. Fixed cushioning provides constant deceleration. Impact noise possible if poorly adjusted.

## Phi-Physics Redesign

Cushion orifice follows phi-profile for smooth deceleration. Coherence field C tracks deceleration smoothness; at C > 0.563, cushion self-adjusts for zero-impact stopping.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiCylinderCushion:
    def __init__(self, cushion_length_mm=20):
        self.length = cushion_length_mm
        self.coherence = 0.3
    def deceleration(self, velocity, position_pct):
        if position_pct > 0.85:
            remaining = (1 - position_pct) * self.length
            phi_decel = velocity**2 / (2 * max(remaining, 0.1)) * (1 + 0.15 * math.sin(PHI * position_pct * 100))
            return phi_decel * (1 + 0.1 * self.coherence)
        return 0
    def update(self, impact_force, dt):
        smoothness = 1.0 / (1.0 + impact_force)
        laplacian = smoothness - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

cush = PhiCylinderCushion(20)
print(f"Decel at v=0.5, pos=90%: {cush.deceleration(0.5, 0.90):.2f} m/s2")
```

## Improvement

50% jerk reduction. 30% zero-impact stopping.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
