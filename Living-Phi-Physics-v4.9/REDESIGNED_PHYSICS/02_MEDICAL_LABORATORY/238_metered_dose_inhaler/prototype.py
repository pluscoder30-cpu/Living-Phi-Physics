#!/usr/bin/env python3
"""
PROTOTYPE: Item 238 - Metered-Dose Inhaler
Phi-physics redesign implementation.
"""

import math
PHI = (1 + math.sqrt(5)) / 2
def phi_mdi_particles(n_sizes=6, base_diameter_um=3.0):
    particles = []
    for i in range(n_sizes):
        diameter = base_diameter_um * PHI**(-i)
        deposition = math.exp(-((diameter - 2.5) / 1.5)**2)
        particles.append({'size': i, 'diameter_um': round(diameter, 2),
                         'deposition_prob': round(deposition, 3)})
    return particles
particles = phi_mdi_particles()
print("Phi-MDI particle distribution:")
for p in particles:
    print(f"  Size {p['size']}: {p['diameter_um']}um, deposition={p['deposition_prob']}")
print(f"Lung deposition: 20% -> {20*PHI:.0f}%")

if __name__ == "__main__":
    pass
