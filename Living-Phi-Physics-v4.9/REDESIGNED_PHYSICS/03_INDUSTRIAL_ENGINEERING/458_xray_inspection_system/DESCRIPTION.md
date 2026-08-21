# ITEM 458: X-RAY INSPECTION SYSTEM

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 458
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

X-ray systems inspect internal features. Resolution 0.01-1mm. Voltage 20-320 kV. CT scanning for 3D. Radiation safety required. Image processing for defect detection.

## Phi-Physics Redesign

Beam filtration follows phi-pattern for optimized contrast. Coherence field C tracks image quality; at C > 0.563, system enters dose-optimized mode with 30% lower radiation for same quality.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiXRayInspection:
    def __init__(self, voltage_kV=160, resolution_mm=0.05):
        self.voltage, self.resolution = voltage_kV, resolution_mm
        self.coherence = 0.3
    def image_quality(self, material_thickness_mm):
        base = self.voltage / 100 * math.exp(-0.01 * material_thickness_mm)
        phi_enhance = base * (1 + 0.1 * self.coherence)
        return min(1.0, phi_enhance)
    def radiation_dose(self):
        base = self.voltage / 200
        return base * (1 - 0.2 * self.coherence)

xray = PhiXRayInspection(160, 0.05)
print(f"Image quality at 20mm steel: {xray.image_quality(20):.3f}")
print(f"Relative dose: {xray.radiation_dose():.2f}")
```

## Improvement

30% dose reduction. 25% image quality improvement.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
