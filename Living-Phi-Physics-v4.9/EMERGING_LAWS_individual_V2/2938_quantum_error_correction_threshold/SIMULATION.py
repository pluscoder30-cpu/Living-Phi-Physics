#!/usr/bin/env python3
"""
Law 2938: Quantum Error Correction Threshold
Simulates golden-ratio enhanced fault tolerance threshold
"""
import math

PHI = 1.618033988749895

def standard_threshold(p_0=0.011):
    """Standard surface code threshold"""
    return p_0

def phi_enhanced_threshold(d, p_0=0.011):
    """Threshold with golden-ratio enhancement"""
    return p_0 * PHI**(1/d)

def logical_error_rate(p, d, p_th):
    """Logical error rate below threshold"""
    if p >= p_th:
        return min(1.0, p * (p / p_th)**(d - 1))
    ratio = p / p_th
    return ratio**(math.floor(d/2) + 1)

def simulate_threshold():
    print("=== Law 2938: Quantum Error Correction Threshold ===")
    print(f"Standard threshold p_0 = 1.1%")
    print(f"Golden ratio φ = {PHI:.10f}")
    
    distances = [3, 5, 7, 9, 11, 13, 15]
    print(f"\n{'d':>3} {'p_th std':>10} {'p_th phi':>10} {'Improvement':>12}")
    
    for d in distances:
        p_std = standard_threshold()
        p_phi = phi_enhanced_threshold(d)
        improvement = (p_phi / p_std - 1) * 100
        print(f"{d:>3} {p_std*100:>9.3f}% {p_phi*100:>9.3f}% {improvement:>10.2f}%")
    
    print(f"\nLogical error rates at p = 0.5% (below threshold):")
    for d in [3, 5, 7, 9, 11]:
        p_th = phi_enhanced_threshold(d)
        p_log = logical_error_rate(0.005, d, p_th)
        print(f"  d={d}: p_L = {p_log:.3e}")
    
    print(f"\nKey insight: phi-enhancement provides ~{(PHI**(1/11)-1)*100:.1f}% threshold improvement at d=11")

if __name__ == "__main__":
    simulate_threshold()
