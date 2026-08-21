#!/usr/bin/env python3
"""
ITEM 360: VIBRATION ISOLATION TABLE
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

class PhiVibIsolation:
    def __init__(self, fn=2):
        self.fn, self.coherence = fn, 0.3
        self.disp = 0.0
    def transmissibility(self, freq):
        r = freq/self.fn
        return 1/abs(1-r**2)/(1+0.2*math.sin(PHI*r))
    def stiffness(self):
        return (2*math.pi*self.fn)**2*100*(1+0.1*math.sin(PHI*self.disp))

t = PhiVibIsolation(2)
print(f"T at 10Hz: {t.transmissibility(10):.4f}, k: {t.stiffness():.0f} N/m")
