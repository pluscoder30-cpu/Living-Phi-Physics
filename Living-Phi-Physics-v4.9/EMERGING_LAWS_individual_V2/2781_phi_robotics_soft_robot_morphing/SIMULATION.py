#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_soft(v,A,E,F): return v*PHI, A*PHI, E/PHI, F*PHI**(1/PHI)
if __name__=="__main__":
    v=1.0; A=0.90; E=100.0; F=12
    vp,Ap,Ep,Fp=phi_soft(v,A,E,F)
    print(f"Speed: {v:.2f} -> {vp:.4f}m/s")
    print(f"Accuracy: {A:.4f} -> {Ap:.4f}")
    print(f"Energy: {E:.1f} -> {Ep:.4f}J")
    print(f"DoF: {F} -> {Fp:.0f}")
    print(f"Speed gain: phi={PHI:.4f}")
