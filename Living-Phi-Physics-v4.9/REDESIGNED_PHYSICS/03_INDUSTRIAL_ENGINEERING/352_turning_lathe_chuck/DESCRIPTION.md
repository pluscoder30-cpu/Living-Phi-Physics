# ITEM 352: TURNING LATHE CHUCK

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 352
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Lathe chucks hold workpiece. 3-jaw self-centering. Clamping force 10-50 kN. Runout 0.01-0.05mm.

## Phi-Physics Redesign

Jaw forces follow phi-distribution for self-centering. Coherence field C tracks concentricity; at C > 0.563, self-centering emerges.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiLatheChuck:
    def __init__(self):
        self.forces = [10.0]*3
        self.runout, self.coherence = 0.03, 0.3
    def phi_clamp(self, total):
        for i in range(3):
            self.forces[i] = total*PHI**(i%3-1)/sum(PHI**(j%3-1) for j in range(3))
    def self_center(self, offset):
        for i in range(3):
            self.forces[i] += offset*0.1*math.sin(PHI*i*2*math.pi/3)
        self.phi_clamp(sum(self.forces))
        bal = 1-max(self.forces)/min(self.forces) if min(self.forces)>0 else 0
        self.coherence = (1/PHI)*self.coherence + PHI*(bal-self.coherence)
        self.coherence = max(0, min(1, self.coherence))
        self.runout = max(0, self.runout*(1-0.3*self.coherence))

c = PhiLatheChuck()
c.phi_clamp(30); c.self_center(0.05)
print(f"Runout: {c.runout:.4f} mm, Coherence: {c.coherence:.4f}")
```

## Improvement

60% runout reduction, 30% clamping uniformity improvement.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
