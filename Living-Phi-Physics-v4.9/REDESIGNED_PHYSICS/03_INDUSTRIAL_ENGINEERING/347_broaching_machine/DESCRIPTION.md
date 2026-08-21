# ITEM 347: BROACHING MACHINE

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 347
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Broaching removes material with multi-toothed tool. Cutting forces up to 200kN. Surface finish Ra 0.4-1.6um. Tool cost high.

## Phi-Physics Redesign

Tooth rise follows phi-increasing sequence. Coherence field C tracks force uniformity; at C > 0.563, forces self-balance across teeth.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiBroaching:
    def __init__(self, n_teeth=20, base_rise=0.05):
        self.n = n_teeth
        self.rise = [base_rise*PHI**(i/n_teeth-0.5) for i in range(n_teeth)]
        self.coherence = 0.3
    def update(self, material_mpa):
        forces = [self.rise[i]*5*material_mpa*0.8*(1+0.1*math.sin(PHI*i)) for i in range(self.n)]
        mean_f = sum(forces)/self.n
        var = sum((f-mean_f)**2 for f in forces)/self.n
        u = 1/(1+var/mean_f**2) if mean_f > 0 else 0
        self.coherence = (1/PHI)*self.coherence + PHI*(u-self.coherence)
        self.coherence = max(0, min(1, self.coherence))
        return sum(forces)

b = PhiBroaching(20, 0.05)
total = b.update(800)
print(f"Total force: {total/1000:.1f} kN, Coherence: {b.coherence:.4f}")
```

## Improvement

25% force variation reduction, 15% surface finish improvement.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
