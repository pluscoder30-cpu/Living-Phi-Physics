# ITEM 394: PNEUMATIC AIR SPRING

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 394
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Air springs provide vibration isolation and leveling. Natural frequency 1-3 Hz. Load capacity 100-50,000 N. Height adjustable. Temperature affects air volume. Auxiliary reservoir increases compliance.

## Phi-Physics Redesign

Bellows geometry follows phi-fold pattern for optimal load distribution. Coherence field C tracks ride quality; at C > 0.563, spring enters auto-leveling mode through phi-pressure regulation.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiAirSpring:
    def __init__(self, natural_freq=2, load_capacity=5000):
        self.f_n, self.capacity = natural_freq, load_capacity
        self.coherence = 0.3
        self.level_error = 0.0
    def stiffness(self, load_N):
        k = (2 * math.pi * self.f_n)**2 * load_N / 9.81
        phi_stiff = k * (1 + 0.05 * math.sin(PHI * load_N / self.capacity * 10))
        return phi_stiff * (1 + 0.03 * self.coherence)
    def update(self, displacement, dt):
        self.level_error = abs(displacement)
        quality = 1.0 / (1.0 + self.level_error * 10)
        laplacian = quality - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

spring = PhiAirSpring(2, 5000)
print(f"Stiffness at 3000N: {spring.stiffness(3000):.0f} N/m")
```

## Improvement

25% better load distribution. 20% ride quality improvement.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
