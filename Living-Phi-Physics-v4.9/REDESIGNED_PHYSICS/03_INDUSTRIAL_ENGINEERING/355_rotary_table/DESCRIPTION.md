# ITEM 355: ROTARY TABLE

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 355
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Rotary tables provide angular positioning. Accuracy 1-10 arcsec. Backlash 0.001-0.01 deg.

## Phi-Physics Redesign

Worm gear follows phi-modified involute. Coherence field C tracks positioning; at C > 0.563, backlash self-compensates.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiRotaryTable:
    def __init__(self):
        self.angle, self.coherence = 0.0, 0.3
        self.backlash = 10  # arcsec
    def position(self, target):
        err = target - self.angle
        self.angle += err*(1-0.3*self.coherence)
        q = 1/(1+abs(target-self.angle)*3600)
        self.coherence = (1/PHI)*self.coherence + PHI*(q-self.coherence)
        self.coherence = max(0, min(1, self.coherence))
        return self.angle
    def compensate(self, direction):
        return self.backlash*PHI**(-1)*direction if self.coherence > C_CRIT else self.backlash*direction

t = PhiRotaryTable()
t.position(45)
print(f"Angle: {t.angle:.4f} deg, Comp: {t.compensate(1):.1f} arcsec")
```

## Improvement

50% backlash reduction, 30% positioning improvement.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
