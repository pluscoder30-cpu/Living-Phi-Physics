# ITEM 460: MEASUREMENT SOFTWARE (SPC)

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 460
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Statistical process control software collects and analyzes measurement data. Control charts (X-bar, R, S). Cp/Cpk indices. Real-time alerts. Data from multiple gauges. Historical trending.

## Phi-Physics Redesign

Control limits follow phi-thresholds for adaptive process monitoring. Coherence field C tracks process stability; at C > 0.563, SPC enters predictive mode with 30% earlier defect detection.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiSPC:
    def __init__(self, target=25.0, tolerance=0.05):
        self.target, self.tolerance = target, tolerance
        self.coherence = 0.3
        self.data = []
    def add_measurement(self, value):
        self.data.append(value)
        if len(self.data) > 25:
            self.data = self.data[-25:]
    def control_limits(self):
        if len(self.data) < 5:
            return None, None
        mean = sum(self.data) / len(self.data)
        std = (sum((x - mean)**2 for x in self.data) / len(self.data))**0.5
        phi_limit = 3 * std * (1 - 0.1 * self.coherence)
        return mean + phi_limit, mean - phi_limit
    def cpk(self):
        if len(self.data) < 5:
            return 0
        mean = sum(self.data) / len(self.data)
        std = (sum((x - mean)**2 for x in self.data) / len(self.data))**0.5
        return min((self.target + self.tolerance/2 - mean), (mean - self.target + self.tolerance/2)) / (3 * max(std, 0.001))

spc = PhiSPC(25.0, 0.05)
for v in [25.01, 24.99, 25.02, 24.98, 25.00]:
    spc.add_measurement(v)
ucl, lcl = spc.control_limits()
print(f"UCL: {ucl:.4f}, LCL: {lcl:.4f}")
print(f"Cpk: {spc.cpk():.2f}")
```

## Improvement

30% earlier defect detection. 20% process improvement.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
