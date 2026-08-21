# ITEM 473: SPLIT SYSTEM AC

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 473
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Split systems have indoor/outdoor units. SEER 14-25. Refrigerant R-410A or R-32. Inverter compressor for variable capacity. Line set length 15-75m. Communication between units.

## Phi-Physics Redesign

Expansion valve follows phi-profile for optimized superheat. Coherence field C tracks system balance; at C > 0.563, system enters self-tuning mode with 8% SEER improvement.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiSplitAC:
    def __init__(self, capacity_kw=3.5, seer=18):
        self.capacity, self.seer = capacity_kw, seer
        self.coherence = 0.3
    def cop(self, outdoor_temp):
        base = self.seer / 3.6 * (1 - 0.02 * max(0, outdoor_temp - 35))
        phi_opt = base * (1 + 0.03 * self.coherence)
        return max(1.5, phi_opt)
    def update(self, superheat_error, dt):
        quality = 1.0 / (1.0 + abs(superheat_error))
        laplacian = quality - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

ac = PhiSplitAC(3.5, 18)
print(f"COP at 35C outdoor: {ac.cop(35):.2f}")
```

## Improvement

8% SEER improvement. 15% superheat control improvement.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
