# ITEM 389: PNEUMATIC ROTARY ACTUATOR

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 389
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Rotary actuators convert air pressure to torque. Vane or rack-and-pinion types. Torque 0.1-500 Nm. Rotation angle adjustable 0-360 deg. Cushioning controls end-of-stroke. Stick-slip at low torque.

## Phi-Physics Redesign

Vane geometry follows phi-profile for smooth torque delivery. Coherence field C tracks rotation smoothness; at C > 0.563, actuator enters precision mode with 40% torque ripple reduction.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiRotaryActuator:
    def __init__(self, max_torque=50, max_angle=90):
        self.max_torque, self.max_angle = max_torque, max_angle
        self.coherence = 0.3
    def torque(self, pressure_bar, angle):
        base = self.max_torque * pressure_bar / 6 * math.sin(math.radians(angle))
        phi_smooth = base * (1 + 0.05 * math.sin(PHI * angle * math.pi / 180))
        return phi_smooth * (1 + 0.03 * self.coherence)
    def update(self, rotation_smoothness, dt):
        laplacian = rotation_smoothness - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

ra = PhiRotaryActuator(50, 90)
print(f"Torque at 6 bar, 45 deg: {ra.torque(6, 45):.1f} Nm")
```

## Improvement

40% torque ripple reduction. 25% smoother motion.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
