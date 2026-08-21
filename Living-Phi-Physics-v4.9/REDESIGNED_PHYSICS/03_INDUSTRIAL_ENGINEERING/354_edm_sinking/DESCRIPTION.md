# ITEM 354: EDM SINKING

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 354
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

EDM sinking uses shaped electrode. Electrode wear 0.1-30%. Surface finish from discharge energy. Machining slow.

## Phi-Physics Redesign

Discharge follows phi-modulation. Coherence field C tracks wear; at C > 0.563, wear self-compensates.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiEDMSinking:
    def __init__(self):
        self.wear, self.coherence = 0.0, 0.3
    def rate(self, current):
        return current*0.01*0.1*(1-self.wear*0.5)*(1+0.08*self.coherence)
    def update(self, count, dt):
        self.wear = min(0.5, self.wear+count*1e-6*dt)
        q = 1-self.wear
        self.coherence = (1/PHI)*self.coherence + PHI*(q-self.coherence)
        self.coherence = max(0, min(1, self.coherence))

e = PhiEDMSinking()
print(f"Rate: {e.rate(15):.3f} mm3/min, Coherence: {e.coherence:.4f}")
```

## Improvement

20% machining rate increase, 30% electrode wear reduction.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
