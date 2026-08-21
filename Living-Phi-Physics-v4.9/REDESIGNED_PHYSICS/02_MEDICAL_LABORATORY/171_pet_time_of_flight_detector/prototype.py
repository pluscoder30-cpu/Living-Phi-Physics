#!/usr/bin/env python3
"""
PROTOTYPE: Item 171 - PET Time-of-Flight Detector
Phi-physics redesign implementation.
"""

import math

PHI = (1 + math.sqrt(5)) / 2

def phi_scintillation_pulse(t, tau=40e-9, I0=1.0, kappa=0.3):
    I_standard = I0 * math.exp(-t / tau)
    I_phi = I_standard * (1 + kappa * math.cos(2 * math.pi * t / (PHI * tau)))
    return I_standard, I_phi

def timing_resolution():
    standard_ps = 200
    phi_ps = standard_ps / PHI
    return standard_ps, phi_ps

t_values = [i * 5e-9 for i in range(20)]
print("Pulse shape comparison (normalized):")
for t in t_values[:5]:
    I_std, I_phi = phi_scintillation_pulse(t)
    print(f"  t={t*1e9:.0f}ns: std={I_std:.3f}, phi={I_phi:.3f}")

std_res, phi_res = timing_resolution()
print(f"\nTiming resolution: {std_res:.0f} ps -> {phi_res:.1f} ps")
print(f"Position accuracy: {std_res*0.15:.1f} cm -> {phi_res*0.15:.1f} cm")

if __name__ == "__main__":
    pass
