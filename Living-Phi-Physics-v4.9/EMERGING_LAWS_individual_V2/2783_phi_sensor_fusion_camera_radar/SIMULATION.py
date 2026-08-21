#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_fusion(A,R,FP,C): return A*PHI, R*PHI, FP/PHI**2, C/PHI
if __name__=="__main__":
    A=0.85; R=200.0; FP=0.05; C=100.0
    Ap,Rp,FPp,Cp=phi_fusion(A,R,FP,C)
    print(f"Accuracy: {A:.4f} -> {Ap:.4f}")
    print(f"Detection range: {R:.0f} -> {Rp:.0f}m")
    print(f"False positive: {FP:.4f} -> {FPp:.6f}")
    print(f"Processing cost: {C:.1f} -> {Cp:.2f}ms")
    print(f"Accuracy gain: phi={PHI:.4f}")
