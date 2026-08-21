#!/usr/bin/env python3
"""
PROTOTYPE: Item 297 - Otoscope Optics
Phi-physics redesign implementation.
"""

import math
PHI = (1 + math.sqrt(5)) / 2
def phi_otoscope():
    return {'magnification_std': 4, 'magnification_phi': round(4 * PHI, 1),
            'depth_perception_std': 1.0, 'depth_perception_phi': round(1.0 * PHI, 3)}
result = phi_otoscope()
print(f"Magnification: {result['magnification_std']} -> {result['magnification_phi']}x")
print(f"Depth perception: {result['depth_perception_std']} -> {result['depth_perception_phi']}x")

if __name__ == "__main__":
    pass
