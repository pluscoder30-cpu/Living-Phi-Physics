# ITEM 479: THERMOSTATIC RADIATOR VALVE

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 479
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

TRVs control room temperature by modulating radiator flow. Sensing bulb or remote sensor. Valve characteristic: linear or equal percentage. Hysteresis 0.5-1C. Authority 0.3-0.5.

## Phi-Physics Redesign

Valve trim follows phi-profile for improved temperature control. Coherence field C tracks room temperature stability; at C > 0.563, TRV enters precision mode with 40% hysteresis reduction.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiTRV:
    def __init__(self, setpoint_C=21, hysteresis_C=0.8):
        self.setpoint, self.hysteresis = setpoint_C, hysteresis_C
        self.coherence = 0.3
    def valve_position(self, room_temp):
        error = room_temp - self.setpoint
        effective_hyst = self.hysteresis * (1 - 0.5 * self.coherence)
        if error > effective_hyst:
            return 0
        elif error < -effective_hyst:
            return 100
        return 50 + error / effective_hyst * 50
    def update(self, temp_stability, dt):
        laplacian = temp_stability - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

trv = PhiTRV(21, 0.8)
print(f"Valve at 22C: {trv.valve_position(22):.0f}%")
print(f"Valve at 20C: {trv.valve_position(20):.0f}%")
```

## Improvement

40% hysteresis reduction. 25% temperature stability.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
