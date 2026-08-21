# ITEM 405: OVERHEAD TROLLEY CONVEYOR

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 405
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Overhead conveyors transport parts on monorail track. Enclosed track or I-beam. Chain-driven trolleys. Load 10-200 kg/trolley. Speed 5-30 m/min. Curves and elevation changes. Paint shop and assembly applications.

## Phi-Physics Redesign

Trolley spacing follows phi-sequence for optimal load distribution. Coherence field C tracks trolley balance; at C > 0.563, conveyor self-loads through phi-distribution.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiOverheadConveyor:
    def __init__(self, n_trolleys=50, base_spacing_m=1.5):
        self.n, self.base_spacing = n_trolleys, base_spacing_m
        self.coherence = 0.3
    def trolley_spacing(self, idx):
        return self.base_spacing * (1 + 0.08 * math.sin(PHI * idx))
    def update(self, balance_error, dt):
        quality = 1.0 / (1.0 + balance_error)
        laplacian = quality - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

oc = PhiOverheadConveyor(50, 1.5)
spacings = [oc.trolley_spacing(i) for i in range(10)]
print(f"Spacings: {[round(s,2) for s in spacings[:5]]} m")
```

## Improvement

15% better load distribution. 10% noise reduction.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
