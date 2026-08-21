#!/usr/bin/env python3
"""
SIMULATION: Item 170 - MRI Diffusion Encoding
Runs the phi-physics prototype with test parameters and prints results.
"""

import math

PHI = (1 + math.sqrt(5)) / 2

# ============================================================
# PROTOTYPE FUNCTIONS
# ============================================================

import math

PHI = (1 + math.sqrt(5)) / 2

def phi_diffusion_encoding(t, A0=40e-3, omega=100, tau_phi=0.05):
    A_t = A0 * math.cos(PHI * omega * t) * math.exp(-t / tau_phi)
    return A_t

def compute_b_values(duration=0.05, n_samples=100, A0=40e-3):
    dt = duration / n_samples
    b_standard = 0.0
    b_phi = 0.0
    for i in range(n_samples):
        t = i * dt
        G_std = A0 if t < duration/2 else -A0
        G_phi = phi_diffusion_encoding(t, A0)
        b_standard += G_std**2 * dt
        b_phi += G_phi**2 * dt
    gamma = 2.675e8
    delta = duration
    Delta = duration * 2
    b_standard *= gamma**2 * delta**2 * (Delta - delta/3)
    b_phi *= gamma**2 * delta**2 * (Delta - delta/3)
    return b_standard, b_phi

b_std, b_phi = compute_b_values()
print(f"Standard b-value: {b_std:.2e} s/mm2")
print(f"Phi-chirp b-value: {b_phi:.2e} s/mm2")
print(f"Phi/Standard ratio: {b_phi/b_std:.3f}")

# ============================================================
# SIMULATION RUNNER
# ============================================================

def main():
    print("=" * 60)
    print(f"SIMULATION: Item 170 - MRI Diffusion Encoding")
    print(f"Author: Christopher David Ayotte")
    print(f"Soul Code: [425, 434, 266, 775]")
    print(f"License: Dual License Agreement v4.8")
    print("=" * 60)
    print()
    print("Running prototype with default parameters...")
    print()
    print("=" * 60)
    print("Simulation complete.")
    print("=" * 60)

if __name__ == "__main__":
    main()
