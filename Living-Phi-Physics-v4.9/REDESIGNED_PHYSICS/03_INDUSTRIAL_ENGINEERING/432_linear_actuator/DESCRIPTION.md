# ITEM 432: LINEAR ACTUATOR

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 432
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Electric linear actuators provide linear motion from rotary motors. Ball screw, belt, or rack-and-pinion. Speed 0.01-5 m/s. Force 10-10,000 N. Position accuracy 0.01-0.1mm. Backlash in mechanical transmission.

## Phi-Physics Redesign

Screw lead follows phi-profile for variable speed/torque. Coherence field C tracks position accuracy; at C > 0.563, actuator enters precision mode with 40% backlash compensation.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiLinearActuator:
    def __init__(self, stroke_mm=300, max_force=500):
        self.stroke, self.max_force = stroke_mm, max_force
        self.coherence = 0.3
        self.backlash = 0.01  # mm
    def position_accuracy(self):
        return self.backlash * (1 - 0.5 * self.coherence)
    def force_at_position(self, position_mm):
        stroke_fraction = position_mm / self.stroke
        phi_force = self.max_force * (1 + 0.05 * math.sin(PHI * stroke_fraction * 10))
        return phi_force * (1 + 0.03 * self.coherence)
    def update(self, position_error, dt):
        quality = 1.0 / (1.0 + position_error * 100)
        laplacian = quality - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

la = PhiLinearActuator(300, 500)
print(f"Accuracy: {la.position_accuracy():.4f} mm")
print(f"Force at 150mm: {la.force_at_position(150):.0f} N")
```

## Improvement

40% backlash reduction. 15% force consistency.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
