#!/usr/bin/env python3
"""
ITEM 382: PNEUMATIC CYLINDER
Phi-Physics Prototype — Industrial Engineering Redesign
Author: Christopher David Ayotte
Soul Code: [425, 434, 266, 775]
License: Dual License Agreement v4.8
"""

import math

PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

import math
PHI = (1 + 5**0.5) / 2
C_CRIT = 0.563263

class PhiPneumaticCylinder:
    def __init__(self, bore_mm=50, stroke_mm=200):
        self.bore, self.stroke = bore_mm, stroke_mm
        self.coherence = 0.3
    def force(self, pressure_bar):
        area = math.pi * (self.bore/2)**2 * 1e-6
        return pressure_bar * 1e5 * area * (1 + 0.03 * self.coherence)
    def cushioning(self, pos_pct):
        if pos_pct > 0.85:
            return (1 - pos_pct) * (1 + 0.2 * math.sin(PHI * pos_pct * 100))
        return 1.0
    def update(self, velocity, dt):
        smooth = 1.0 / (1.0 + abs(velocity - 0.5))
        laplacian = smooth - self.coherence
        self.coherence = (1/PHI) * self.coherence + PHI * laplacian
        self.coherence = max(0, min(1, self.coherence))

cyl = PhiPneumaticCylinder(50, 200)
print(f"Force at 6 bar: {cyl.force(6):.1f} N")
print(f"Cushion at 90%: {cyl.cushioning(0.90):.3f}")
