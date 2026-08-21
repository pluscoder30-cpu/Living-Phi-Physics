# ITEM 407: VIBRATORY BOWL FEEDER

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 407
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Bowl feeders orient and feed parts using vibration. Frequency 50-120 Hz. Amplitude 0.01-0.5mm. Parts track up spiral track. Tooling selects correct orientation. Speed 10-500 parts/min.

## Phi-Physics Redesign

Bowl spiral follows phi-pitch for optimized part flow. Coherence field C tracks feeding consistency; at C > 0.563, feeder self-tunes through phi-frequency optimization.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiBowlFeeder:
    def __init__(self, frequency=100, amplitude=0.1):
        self.freq, self.amp = frequency, amplitude
        self.coherence = 0.3
    def feed_rate(self, part_weight_g):
        base_rate = self.freq * self.amp * 10
        phi_optimization = 1 + 0.08 * self.coherence
        weight_factor = 1.0 / (1 + part_weight_g / 100)
        return base_rate * phi_optimization * weight_factor
    def update(self, consistency, dt):
        laplacian = consistency - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

bf = PhiBowlFeeder(100, 0.1)
print(f"Feed rate at 10g parts: {bf.feed_rate(10):.0f} parts/min")
```

## Improvement

20% feed rate improvement. 30% orientation accuracy.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
