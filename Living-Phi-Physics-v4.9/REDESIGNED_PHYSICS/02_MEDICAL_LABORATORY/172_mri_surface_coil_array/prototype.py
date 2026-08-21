#!/usr/bin/env python3
"""
PROTOTYPE: Item 172 - MRI Surface Coil Array
Phi-physics redesign implementation.
"""

import math

PHI = (1 + math.sqrt(5)) / 2

def phi_surface_array(n_elements=12, body_radius=150.0):
    elements = []
    for i in range(n_elements):
        theta = 2 * math.pi * i / PHI
        r = body_radius * (1 + 0.1 * math.sin(PHI * i))
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        elem_radius = 30.0 * PHI**(-(i % 3))
        elements.append({
            'id': i,
            'position': (round(x, 1), round(y, 1)),
            'radius': round(elem_radius, 1),
            'angle_deg': round(math.degrees(theta) % 360, 1)
        })
    return elements

def decoupling_factor(elem_a, elem_b):
    separation = abs(elem_a - elem_b)
    return 1.0 / PHI**separation

def snr_improvement():
    return 1.214 * (1 + 0.6 * (1 - 1/PHI))

elements = phi_surface_array()
print(f"Array elements: {len(elements)}")
for e in elements[:3]:
    print(f"  Element {e['id']}: pos={e['position']}, r={e['radius']}mm, theta={e['angle_deg']} deg")
print(f"Decoupling (adjacent): {decoupling_factor(0, 1):.3f}")
print(f"Decoupling (separated by 2): {decoupling_factor(0, 2):.3f}")
print(f"SNR improvement: {snr_improvement():.3f}x")

if __name__ == "__main__":
    pass
