#!/usr/bin/env python3
"""
ITEM 341: CNC MILLING SPINDLE
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

class PhiCNCSpindle:
    def __init__(self, max_rpm=20000):
        self.max_rpm = max_rpm
        self.imbalance = [0.5, 0.3]
        self.coherence = 0.3
    def vibration(self, rpm):
        return sum(self.imbalance[i] * (rpm/100)**2 * (1 - 0.4*math.sin(PHI*i*math.pi)) for i in range(2))
    def update(self, rpm, dt):
        vib = self.vibration(rpm)
        for i in range(2):
            self.imbalance[i] = max(0, self.imbalance[i] - vib*0.01*math.sin(PHI*i)*dt)
        self.coherence = (1/PHI)*self.coherence + PHI*(1/(1+vib)-self.coherence)
        self.coherence = max(0, min(1, self.coherence))
    def surface_finish(self, feed):
        return feed**2 / 80 * (1 - 0.2*self.coherence)

s = PhiCNCSpindle(20000)
s.update(10000, 0.01)
print(f"Vibration: {s.vibration(10000):.4f}, Coherence: {s.coherence:.4f}")
