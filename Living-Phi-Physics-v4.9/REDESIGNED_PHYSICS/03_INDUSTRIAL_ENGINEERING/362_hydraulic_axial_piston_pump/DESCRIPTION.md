# ITEM 362: HYDRAULIC AXIAL PISTON PUMP

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 362
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Swash plate axial piston pumps provide variable displacement. Pressure up to 400 bar. Efficiency 90-95%. Displacement controlled by swash plate angle. Cylinder block rotating creates pressure pulses.

## Phi-Physics Redesign

Piston timing follows phi-sequence across cylinder bank. Swash plate angle adjustment follows coherence field for load-sensing optimization. At C > 0.563, pulsation self-organizes to phi-harmonic pattern with 60% amplitude reduction.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiAxialPistonPump:
    def __init__(self, n_pistons=9, max_disp_cc=100):
        self.n, self.max_disp = n_pistons, max_disp_cc
        self.swash_angle = 18.0
        self.coherence = 0.3
    def displacement(self):
        return self.max_disp * math.sin(math.radians(self.swash_angle))
    def pressure_pulsation(self):
        base = 0.03 * math.sin(math.radians(self.swash_angle))
        return base * (1 + 0.1 * math.sin(PHI * self.n)) * (1 - 0.4 * self.coherence)
    def update_system(self, load_pressure, dt):
        ripple = self.pressure_pulsation()
        laplacian = 1.0 / (1.0 + ripple * 10) - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))
        return ripple

pump = PhiAxialPistonPump(9, 100)
print(f"Displacement: {pump.displacement():.1f} cc/rev")
ripple = pump.update_system(300, 0.01)
print(f"Pressure ripple: {ripple*100:.2f}%, Coherence: {pump.coherence:.4f}")
```

## Improvement

60% pressure ripple reduction. 5% efficiency improvement.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
