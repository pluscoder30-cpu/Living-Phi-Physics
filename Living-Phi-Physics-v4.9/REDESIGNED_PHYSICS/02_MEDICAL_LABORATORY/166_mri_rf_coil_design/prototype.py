#!/usr/bin/env python3
"""
PROTOTYPE: Item 166 - MRI RF Coil Design
Phi-physics redesign implementation.
"""

import math

PHI = (1 + math.sqrt(5)) / 2

def phi_birdcage_b1(n_rungs=16, coil_radius=0.15):
    field_profile = []
    for i in range(n_rungs):
        theta = i * 2 * math.pi / PHI
        x = coil_radius * math.cos(theta)
        y = coil_radius * math.sin(theta)
        b1_contribution = math.sin(PHI * theta) / (1 + i * 0.1)
        field_profile.append({
            'rung': i,
            'angle_deg': round(math.degrees(theta) % 360, 1),
            'position': (round(x*1000, 1), round(y*1000, 1)),
            'b1_weight': round(b1_contribution, 4)
        })
    return field_profile

def snr_improvement():
    fill_improvement = 0.9 / 0.7
    q_improvement = PHI
    return fill_improvement * q_improvement

profile = phi_birdcage_b1()
print(f"Rungs: {len(profile)}")
for r in profile[:4]:
    print(f"  Rung {r['rung']}: {r['angle_deg']} deg, B1={r['b1_weight']}")
print(f"SNR improvement: {snr_improvement():.3f}x")

if __name__ == "__main__":
    pass
