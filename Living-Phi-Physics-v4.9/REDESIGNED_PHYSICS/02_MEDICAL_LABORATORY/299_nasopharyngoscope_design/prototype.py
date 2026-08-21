#!/usr/bin/env python3
"""
PROTOTYPE: Item 299 - Nasopharyngoscope Design
Phi-physics redesign implementation.
"""

import math
PHI = (1 + math.sqrt(5)) / 2
def phi_nasopharyngoscope():
    return {'angulation_std': 130, 'angulation_phi': round(130 * PHI, 0),
            'precision_std': 5, 'precision_phi': round(5 / PHI, 1)}
result = phi_nasopharyngoscope()
print(f"Angulation: ±{result['angulation_std']} -> ±{result['angulation_phi']} deg")
print(f"Precision: ±{result['precision_std']} -> ±{result['precision_phi']} deg")

if __name__ == "__main__":
    pass
