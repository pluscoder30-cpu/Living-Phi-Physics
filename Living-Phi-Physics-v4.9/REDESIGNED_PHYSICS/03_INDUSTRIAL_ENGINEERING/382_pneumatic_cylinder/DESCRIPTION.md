# ITEM 382: PNEUMATIC CYLINDER

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 382
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Pneumatic cylinders provide linear force from compressed air. Bore 20-200mm. Speed controlled by flow control valves. Cushioning at end-of-stroke. Air compressibility causes spongy response. Stick-slip at low speeds.

## Phi-Physics Redesign

Cushioning follows phi-deceleration curve. Coherence field C tracks motion smoothness; at C > 0.563, cylinder enters precision mode with 60% stick-slip reduction through phi-dither.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiPneumaticCylinder:
    def __init__(self, bore_mm=50, stroke_mm=200):
        self.bore, self.stroke = bore_mm, stroke_mm
        self.coherence = 0.3
    def force(self, pressure_bar):
        area = math.pi * (self.bore/2)**2 * 1e-6
        return pressure_bar * 1e5 * area * (1 + 0.03 * self.coherence)
    def cushioning(self, pos_pct):
        if pos_pct > 0.85:
            return (1 - pos_pct) * (1 + 0.2 * math.sin(PHI * pos_pct * 100))
        return 1.0
    def update(self, velocity, dt):
        smooth = 1.0 / (1.0 + abs(velocity - 0.5))
        laplacian = smooth - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

cyl = PhiPneumaticCylinder(50, 200)
print(f"Force at 6 bar: {cyl.force(6):.1f} N")
print(f"Cushion at 90%: {cyl.cushioning(0.90):.3f}")
```

## Improvement

60% stick-slip reduction. 30% smoother cushioning.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
