#!/usr/bin/env python3
"""
Law 2940: Adiabatic Quantum Computing Sweep Rate
Simulates optimal sweep rate for quantum annealing
"""
import math

PHI = 1.618033988749895

def diabatic_error(delta_min, L, v):
    """Probability of diabatic transition"""
    exponent = -math.pi * delta_min**2 * L / (2 * v)
    return math.exp(exponent)

def decoherence_error(v, Gamma=0.001):
    """Error from decoherence during evolution"""
    L = delta_min**2 / (v * PHI) if v > 0 else float('inf')
    return Gamma * L

def total_error(delta_min, L, v, Gamma=0.001):
    """Total error = diabatic + decoherence"""
    p_diab = diabatic_error(delta_min, L, v)
    p_deco = Gamma * L
    return p_diab + p_deco

def optimal_sweep_rate(delta_min, L):
    """Optimal sweep rate per phi-law"""
    return delta_min**2 / (PHI * L)

def simulate_sweep():
    print("=== Law 2940: Adiabatic Quantum Computing Sweep Rate ===")
    delta_min = 0.1  # Minimum gap in units of J
    L_total = 1000.  # Total evolution time
    
    v_opt = optimal_sweep_rate(delta_min, L_total)
    print(f"Minimum gap Δ_min = {delta_min} J")
    print(f"Total time L = {L_total}")
    print(f"Optimal sweep rate v_opt = {v_opt:.6f}")
    
    sweep_rates = [v_opt * f for f in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]]
    print(f"\n{'v/v_opt':>8} {'Diabatic':>12} {'Decoherence':>12} {'Total':>12}")
    
    for v in sweep_rates:
        ratio = v / v_opt
        p_diab = diabatic_error(delta_min, L_total, v)
        p_deco = decoherence_error(v)
        p_total = total_error(delta_min, L_total, v)
        print(f"{ratio:>8.1f} {p_diab:>12.4e} {p_deco:>12.4e} {p_total:>12.4e}")
    
    print(f"\nAt v = v_opt:")
    print(f"  Fidelity: {1 - total_error(delta_min, L_total, v_opt):.4f}")
    print(f"  Improvement over v_opt/φ: {total_error(delta_min, L_total, v_opt/PHI) / total_error(delta_min, L_total, v_opt):.2f}x")

if __name__ == "__main__":
    simulate_sweep()
