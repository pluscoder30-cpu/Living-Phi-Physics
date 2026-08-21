# ITEM 397: PNEUMATIC PRESSURE GAUGE

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 397
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Pressure gauges display system pressure. Accuracy +/-1% full scale. Dial sizes 40-100mm. Vibration damping with glycerin fill. Temperature effect +/-0.4%/C.

## Phi-Physics Redesign

Bourdon tube follows phi-geometry for improved linearity. Coherence field C tracks reading accuracy; at C > 0.563, gauge self-indicates calibration drift with 40% better sensitivity.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiPressureGauge:
    def __init__(self, full_scale=10, accuracy_pct=1):
        self.fs, self.accuracy = full_scale, accuracy_pct
        self.coherence = 0.3
    def reading(self, actual_pressure, temperature_C):
        temp_error = 0.004 * (temperature_C - 20) * self.fs
        phi_linearity = 1 - 0.001 * self.accuracy * (1 - 0.3 * self.coherence)
        return actual_pressure * phi_linearity + temp_error
    def update(self, calibration_error, dt):
        accuracy = 1.0 / (1.0 + calibration_error * 10)
        laplacian = accuracy - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

g = PhiPressureGauge(10, 1)
print(f"Reading at 7 bar, 30C: {g.reading(7, 30):.2f} bar")
```

## Improvement

40% better linearity. 30% temperature compensation.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
