#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_path(eta,T,E,C): return eta*PHI**(1/PHI), T/PHI, E/PHI, C*PHI
if __name__=="__main__":
    eta=0.70; T=10.0; E=100.0; C=0.99
    etap,Tp,Ep,Cp=phi_path(eta,T,E,C)
    print(f"Efficiency: {eta:.4f} -> {etap:.4f}")
    print(f"Cycle time: {T:.2f} -> {Tp:.4f}s")
    print(f"Energy: {E:.1f} -> {Ep:.4f}J")
    print(f"Collision-free: {C:.4f} -> {Cp:.4f}")
    print(f"Cycle reduction: 1/phi={1/PHI:.4f}")
