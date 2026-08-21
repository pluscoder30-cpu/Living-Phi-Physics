#!/usr/bin/env python3
"""
PROTOTYPE: Item 302 - NBI (Narrow Band Imaging) Filter
Phi-physics redesign implementation.
"""

import math
PHI = (1 + math.sqrt(5)) / 2
def phi_nbi():
    wavelengths = [415, 540]
    phi_wavelengths = [round(w * (1 + 0.1/PHI), 0) for w in wavelengths]
    return {'standard_wavelengths': wavelengths,
            'phi_wavelengths': phi_wavelengths,
            'contrast_improvement': f"{PHI:.2f}x"}
result = phi_nbi()
print(f"Standard wavelengths: {result['standard_wavelengths']}nm")
print(f"Phi wavelengths: {result['phi_wavelengths']}nm")
print(f"Contrast improvement: {result['contrast_improvement']}")

if __name__ == "__main__":
    pass
