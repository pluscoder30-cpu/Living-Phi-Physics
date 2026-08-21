#!/usr/bin/env python3
"""
PROTOTYPE: Item 164 - Ultrasound Transducer Array
Phi-physics redesign implementation.
"""

import math

PHI = (1 + math.sqrt(5)) / 2

def phi_ultrasound_array(n_elements=64, aperture=40e-3):
    positions = []
    for i in range(n_elements):
        theta = 2 * math.pi * i / PHI
        r = aperture * math.sqrt(i / n_elements)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        positions.append((round(x*1000, 2), round(y*1000, 2)))
    return positions

def grating_lobe_suppression(n_elements=64):
    sidelobe_dB = -20 * math.log10(PHI) * math.log(PHI, n_elements)
    return sidelobe_dB

positions = phi_ultrasound_array()
print(f"Array elements: {len(positions)}")
for i, (x, y) in enumerate(positions[:4]):
    print(f"  Element {i}: ({x}, {y}) mm")
print(f"Grating lobe suppression: {grating_lobe_suppression():.1f} dB")

if __name__ == "__main__":
    pass
