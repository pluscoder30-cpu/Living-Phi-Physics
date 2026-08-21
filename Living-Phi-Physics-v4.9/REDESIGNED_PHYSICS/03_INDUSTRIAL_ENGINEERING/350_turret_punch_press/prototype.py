#!/usr/bin/env python3
"""
ITEM 350: TURRET PUNCH PRESS
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

class PhiTurretPunch:
    def __init__(self):
        self.coherence = 0.3
    def optimize_path(self, coords):
        if len(coords) < 2: return coords
        opt = [coords[0]]; rem = coords[1:]
        for _ in range(len(rem)):
            last = opt[-1]; best_i, best_d = 0, float('inf')
            for i, c in enumerate(rem):
                d = math.sqrt((c[0]-last[0])**2+(c[1]-last[1])**2)*(1-0.2*abs(math.sin(PHI*i)))
                if d < best_d: best_d, best_i = d, i
            opt.append(rem.pop(best_i))
        return opt
    def update(self, error, dt):
        q = 1/(1+error)
        self.coherence = (1/PHI)*self.coherence + PHI*(q-self.coherence)
        self.coherence = max(0, min(1, self.coherence))

p = PhiTurretPunch()
hits = [(i*10, i*10%30) for i in range(20)]
opt = p.optimize_path(hits)
orig = sum(math.sqrt((hits[i+1][0]-hits[i][0])**2+(hits[i+1][1]-hits[i][1])**2) for i in range(len(hits)-1))
new = sum(math.sqrt((opt[i+1][0]-opt[i][0])**2+(opt[i+1][1]-opt[i][1])**2) for i in range(len(opt)-1))
print(f"Path: {orig:.0f} -> {new:.0f} mm, Coherence: {p.coherence:.4f}")
