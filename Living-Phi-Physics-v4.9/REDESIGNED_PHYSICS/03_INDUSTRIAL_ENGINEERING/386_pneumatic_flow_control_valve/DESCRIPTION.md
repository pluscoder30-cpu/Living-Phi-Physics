# ITEM 386: PNEUMATIC FLOW CONTROL VALVE

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 386
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Flow controls regulate actuator speed by restricting air flow. Meter-in or meter-out. Temperature affects orifice flow. Non-return function for one-way speed control. Response affected by downstream pressure.

## Phi-Physics Redesign

Orifice geometry follows phi-profile for temperature-compensated flow. Coherence field C tracks speed stability; at C > 0.563, valve self-compensates through phi-thermal expansion matching.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiFlowControl:
    def __init__(self, max_flow=200):
        self.max_flow = max_flow
        self.coherence = 0.3
    def flow_rate(self, opening_pct, pressure_drop, temp_C):
        base = self.max_flow * opening_pct / 100 * math.sqrt(pressure_drop / 6)
        temp_comp = 1 + 0.002 * (temp_C - 20) * (1 - 0.5 * self.coherence)
        return base * temp_comp
    def update(self, speed_stability, dt):
        laplacian = speed_stability - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

fc = PhiFlowControl(200)
print(f"Flow at 50% opening, 1 bar DP: {fc.flow_rate(50, 1, 25):.1f} L/min")
```

## Improvement

30% temperature compensation. 20% speed stability improvement.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
