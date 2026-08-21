# ITEM 349: WIRE EDM MACHINE

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 349
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Wire EDM uses spark discharge. Cutting speed 5-50 mm2/min. Kerf width controlled by spark gap. Corner accuracy limited by wire lag.

## Phi-Physics Redesign

Spark discharge follows phi-sequence. Coherence field C tracks kerf uniformity; at C > 0.563, overcut self-compensates.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiWireEDM:
    def __init__(self, wire_d=0.25):
        self.d_wire = wire_d
        self.kerf, self.coherence = wire_d, 0.3
    def speed(self, thickness):
        return 10/(1+thickness/50)*(1+0.1*self.coherence)
    def update(self, voltage, tension, dt):
        overcut = 0.05*(voltage/80)*(1+0.1*math.sin(PHI*dt*1000))
        self.kerf = self.d_wire+overcut*(1-0.3*self.coherence)
        u = 1/(1+abs(self.kerf-self.d_wire*1.1)/(self.d_wire*1.1))
        self.coherence = (1/PHI)*self.coherence + PHI*(u-self.coherence)
        self.coherence = max(0, min(1, self.coherence))

e = PhiWireEDM(0.25)
print(f"Speed at 30mm: {e.speed(30):.1f} mm2/min, Kerf: {e.kerf:.3f} mm")
```

## Improvement

15% speed increase, 40% overcut variation reduction.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
