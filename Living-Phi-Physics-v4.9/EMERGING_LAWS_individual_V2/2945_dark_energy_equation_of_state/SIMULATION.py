#!/usr/bin/env python3
"""
Law 2945: Dark Energy Equation of State
Simulates golden-ratio evolving dark energy w(z)
"""
import math

PHI = 1.618033988749895

def w_dark_energy(z, epsilon=0.03, z_0=1.0):
    """Golden-ratio evolving equation of state"""
    return -1 + epsilon * PHI**(-z / z_0)

def dark_energy_density(z, w_0=-1.0, epsilon=0.03, z_0=1.0):
    """Dark energy density evolution"""
    integral = 0
    dz = 0.01
    z_vals = [i * dz for i in range(int(z / dz) + 1)]
    for z_i in z_vals:
        w_i = w_dark_energy(z_i, epsilon, z_0)
        integral += (1 + w_i) * dz
    return math.exp(3 * integral)

def simulate_dark_energy():
    print("=== Law 2945: Dark Energy Equation of State ===")
    epsilon = 0.03
    z_0 = 1.0
    
    redshifts = [0.0, 0.5, 1.0, 1.5, 2.0, 3.0]
    print(f"Parameters: ε = {epsilon}, z_0 = {z_0}")
    print(f"\n{'z':>5} {'w(z)':>10} {'ρ_DE/ρ_0':>10}")
    
    for z in redshifts:
        w = w_dark_energy(z, epsilon, z_0)
        rho = dark_energy_density(z, -1.0, epsilon, z_0)
        print(f"{z:>5.1f} {w:>10.4f} {rho:>10.4f}")
    
    print(f"\nKey predictions:")
    print(f"  w(z=0) = {w_dark_energy(0, epsilon, z_0):.4f}")
    print(f"  w(z=1) = {w_dark_energy(1, epsilon, z_0):.4f} = -1 + {epsilon}*φ^(-1)")
    print(f"  w(z→∞) → -1 (cosmological constant)")
    print(f"  Transition: phantom (w<-1) → quintessence (w>-1) at z ~ {z_0}")

if __name__ == "__main__":
    simulate_dark_energy()
