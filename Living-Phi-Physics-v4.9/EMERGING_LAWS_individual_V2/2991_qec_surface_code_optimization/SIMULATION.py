#!/usr/bin/env python3
"""Law 2991: QEC Surface Code Optimization"""
import math
PHI = 1.618033988749895

def threshold(d, p_0=0.011):
    return p_0 * (1 + PHI**(-d/2))

def simulate():
    print("=== Law 2991: QEC Surface Code Optimization ===")
    for d in [3, 5, 7, 9, 11, 13]:
        p_th = threshold(d)
        improvement = (p_th / 0.011 - 1) * 100
        print(f"  d={d}: p_th = {p_th*100:.3f}% (improvement: {improvement:.1f}%)")

if __name__ == "__main__":
    simulate()
