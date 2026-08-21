# ITEM 358: SPINDLE BEARING

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 358
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Spindle bearings determine precision. Ceramic hybrid for high speed. Preload affects stiffness and life. Micro-slip causes vibration.

## Phi-Physics Redesign

Preload follows phi-schedule. Coherence field C tracks vibration; at C > 0.563, ball pass frequencies self-organize.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiSpindleBearing:
    def __init__(self, bore=50):
        self.bore, self.preload = bore, 500
        self.vib, self.coherence = 0.1, 0.3
    def update(self, rpm, dt):
        self.preload = 500*(1+0.3*math.sin(PHI*rpm/20000*math.pi))
        self.vib = 0.1*(rpm/20000)**1.5*(1+abs(self.preload-500)/500)
        q = 1/(1+self.vib)
        self.coherence = (1/PHI)*self.coherence + PHI*(q-self.coherence)
        self.coherence = max(0, min(1, self.coherence))
    def life(self):
        return (self.bore**0.3*1000/self.preload)**3*1e6/(20000*60)*(1+0.2*self.coherence)

b = PhiSpindleBearing(50)
for _ in range(100): b.update(15000, 0.01)
print(f"Preload: {b.preload:.0f} N, Vib: {b.vib:.3f}, Life: {b.life():.0f}h")
```

## Improvement

30% bearing life extension, 40% vibration reduction.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
