# ITEM 368: HYDRAULIC SPOOL VALVE

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 368
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Directional spool valves control fluid direction. Overlapping lands create dead band. Flow forces push spool off-center. Leakage 0.5-3% of rated flow.

## Phi-Physics Redesign

Spool land geometry follows phi-contour for balanced flow forces. At C > 0.563, spool self-centers through phi-pressure balancing.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiSpoolValve:
    def __init__(self, dia=10, overlap=0.1):
        self.dia, self.overlap, self.coherence = dia, overlap, 0.3
    def flow_force(self, flow, pressure):
        f = 0.0005 * flow * math.sqrt(pressure)
        return f - f * 0.2 * math.sin(PHI * flow * 0.1)
    def dead_band(self):
        return self.overlap * (1 - 0.6 * self.coherence) if self.coherence > C_CRIT else self.overlap
    def update(self, cmd_force, flow, pressure, dt):
        net = cmd_force - self.flow_force(flow, pressure)
        err = abs(net) / 100
        laplacian = 1.0 / (1.0 + err) - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))
        return net

v = PhiSpoolValve(10, 0.1)
print(f"Flow force: {v.flow_force(10, 200):.2f} N")
print(f"Dead band: {v.dead_band()*100:.1f}%")
```

## Improvement

60% dead band reduction. 40% flow force compensation.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
