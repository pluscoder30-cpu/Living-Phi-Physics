#!/usr/bin/env python3
"""
Law 2942: Quantum Sensing Heisenberg Limit
Simulates golden-ratio enhanced quantum measurement precision
"""
import math

PHI = 1.618033988749895

def shot_noise_limit(N):
    """Standard quantum limit (shot noise)"""
    return 1.0 / math.sqrt(N)

def heisenberg_limit(N):
    """Standard Heisenberg limit"""
    return 1.0 / N

def phi_heisenberg_limit(N):
    """Golden-ratio enhanced Heisenberg limit"""
    return 1.0 / (N**(1/PHI) * math.sqrt(PHI))

def quantum_fisher_information(N, depth=PHI):
    """Quantum Fisher information for phi-depth entangled states"""
    return N**(2/depth) * depth

def simulate_sensing():
    print("=== Law 2942: Quantum Sensing Heisenberg Limit ===")
    particles = [10, 50, 100, 500, 1000, 5000]
    
    print(f"{'N':>6} {'Shot noise':>12} {'Heisenberg':>12} {'Phi-limit':>12} {'Improvement':>12}")
    
    for N in particles:
        snl = shot_noise_limit(N)
        hl = heisenberg_limit(N)
        phi_hl = phi_heisenberg_limit(N)
        improvement = snl / phi_hl
        print(f"{N:>6} {snl:>12.6f} {hl:>12.6f} {phi_hl:>12.6f} {improvement:>12.4f}")
    
    print(f"\nAt N = 1000 particles:")
    print(f"  Shot noise:     {shot_noise_limit(1000):.6f}")
    print(f"  Heisenberg:     {heisenberg_limit(1000):.6f}")
    print(f"  Phi-enhanced:   {phi_heisenberg_limit(1000):.6f}")
    print(f"  Improvement:    {shot_noise_limit(1000)/phi_heisenberg_limit(1000):.2f}x over shot noise")
    
    print(f"\nQuantum Fisher information at N=1000:")
    F_Q = quantum_fisher_information(1000)
    print(f"  F_Q = {F_Q:.2f}")
    print(f"  Δθ = 1/√F_Q = {1/math.sqrt(F_Q):.6f}")

if __name__ == "__main__":
    simulate_sensing()
