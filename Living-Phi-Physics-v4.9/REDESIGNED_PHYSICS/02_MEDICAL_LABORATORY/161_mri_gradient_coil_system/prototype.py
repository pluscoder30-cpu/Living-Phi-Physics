#!/usr/bin/env python3
"""
PROTOTYPE: Item 161 - MRI Gradient Coil System
Phi-physics redesign implementation.
"""

import math

PHI = (1 + math.sqrt(5)) / 2

def phi_gradient_field(r, theta, G0=1.0, sigma=1.0, kappa=0.1):
    G_linear = G0 * r
    phi_mod = 1 + kappa * (PHI - 1)
    spiral_decay = math.exp(-r**2 / (2 * sigma**2))
    G_phi = G_linear * phi_mod * spiral_decay * math.cos(PHI * theta)
    return G_phi

def eddy_current_ratio():
    suppression = 1 / PHI**3
    return suppression

print(f"Gradient at r=1, theta=0: {phi_gradient_field(1.0, 0.0):.4f}")
print(f"Eddy suppression ratio: {eddy_current_ratio():.4f}")

if __name__ == "__main__":
    pass
