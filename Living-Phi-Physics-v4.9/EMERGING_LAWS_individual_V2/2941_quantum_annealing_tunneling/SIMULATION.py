#!/usr/bin/env python3
"""
Law 2941: Quantum Annealing Tunneling Barrier
Simulates optimal tunneling barrier for quantum annealing
"""
import math

PHI = 1.618033988749895
HBAR = 1.054571817e-34

def optimal_barrier(J, N):
    """Optimal tunneling barrier height"""
    return J * PHI**(-N / 2)

def tunneling_rate(B, w, m_eff=1.0):
    """Tunneling rate through barrier"""
    exponent = -w * math.sqrt(2 * m_eff * B) / HBAR
    return math.exp(exponent)

def success_probability(h, J, N, w=1.0):
    """Success probability for spin glass problem"""
    B_eff = J * (1 - h / J) if h < J else 0.01 * J
    return tunneling_rate(B_eff, w) * math.exp(-N / PHI)

def simulate_tunneling():
    print("=== Law 2941: Quantum Annealing Tunneling Barrier ===")
    J = 1.0  # Coupling strength
    N_spins = [10, 20, 50, 100, 200]
    
    print(f"Coupling J = {J}")
    print(f"\n{'N':>4} {'B_opt':>12} {'B_opt/J':>10} {'ln(B_opt/J)':>12}")
    
    for N in N_spins:
        B = optimal_barrier(J, N)
        print(f"{N:>4} {B:>12.6f} {B/J:>10.6f} {math.log(B/J):>12.4f}")
    
    print(f"\nScaling: B_opt ∝ φ^(-N/2)")
    print(f"For N=100: B_opt = {optimal_barrier(J, 100):.6e} J")
    
    print(f"\nTunneling rates for N=100:")
    barriers = [0.001, 0.01, 0.1, 1.0]
    for B in barriers:
        rate = tunneling_rate(B, 1.0)
        print(f"  B = {B:.3f} J: Γ = {rate:.3e}")

if __name__ == "__main__":
    simulate_tunneling()
