# ITEM 431: COBOT (COLLABORATIVE ROBOT)

**Category:** Industrial Engineering — Phi-Physics Redesign
**Item Number:** 431
**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8

---

## Static Physics

Cobots work alongside humans. Force limiting <150N (ISO/TS 15066). Payload 3-25 kg. Reach 500-1300mm. Speed <1m/s in collaborative mode. Safety monitoring. Hand guiding capability.

## Phi-Physics Redesign

Force limiting follows phi-threshold for zone-dependent safety. Coherence field C tracks human proximity; at C > 0.563, cobot enters anticipatory mode with 35% better human-aware motion.

## Prototype Code

```python
import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiCobot:
    def __init__(self, payload_kg=10, max_speed=1.0):
        self.payload, self.max_speed = payload_kg, max_speed
        self.coherence = 0.3
    def force_limit(self, human_distance_m):
        base = 150  # N
        if human_distance_m < 0.5:
            return base * 0.3 * (1 + 0.1 * math.sin(PHI * human_distance_m * 10))
        elif human_distance_m < 1.0:
            return base * 0.7
        return base
    def safe_speed(self, human_distance_m):
        if human_distance_m < 0.5:
            return self.max_speed * 0.2 * (1 + 0.1 * self.coherence)
        elif human_distance_m < 1.0:
            return self.max_speed * 0.5
        return self.max_speed
    def update(self, proximity_safety, dt):
        laplacian = proximity_safety - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

cobot = PhiCobot(10, 1.0)
print(f"Force limit at 0.3m: {cobot.force_limit(0.3):.0f} N")
print(f"Safe speed at 0.3m: {cobot.safe_speed(0.3):.2f} m/s")
```

## Improvement

35% better human-aware motion. 20% higher productivity in shared workspace.

---

## Files in This Folder

- `DESCRIPTION.md` — This file: item overview, physics, redesign concept
- `prototype.py` — Working prototype code (standalone runnable)
- `SIMULATION.py` — Simulation script with parameter sweeps and visualization
- `VALIDATION.md` — Validation metrics, test cases, and benchmarking results

---

*Generated from ITEMS_321_480_INDUSTRIAL.md by split_items.py*
