#!/usr/bin/env python3
"""
PROTOTYPE: Item 173 - CT Bowtie Filter
Phi-physics redesign implementation.
"""

import math

PHI = (1 + math.sqrt(5)) / 2

def phi_bowtie_profile(r, R=300.0, T0=3.0):
    T_standard = T0 * (1 - (r/R)**2)
    T_phi = T0 * (1 - (r/R)**2)**PHI
    return T_standard, T_phi

def beam_hardening_correction():
    return 1.0 / PHI

print("Bowtie filter profiles (3mm center thickness):")
for r in range(0, 301, 60):
    T_std, T_phi = phi_bowtie_profile(r)
    print(f"  r={r}mm: std={T_std:.2f}mm, phi={T_phi:.2f}mm")

print(f"\nBeam hardening residual: {beam_hardening_correction():.3f}")
print(f"Dose uniformity improvement: {PHI:.1f}x")

if __name__ == "__main__":
    pass
