#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_radar(A,D,C): return A*PHI, D/PHI, C*PHI**2
if __name__=="__main__":
    A=0.90; D=10.0; C=1.0
    Ap,Dp,Cp=phi_radar(A,D,C)
    print(f"Accuracy: {A:.4f} -> {Ap:.4f}")
    print(f"Init delay: {D:.1f} -> {Dp:.2f}s")
    print(f"Clutter: {C:.2f} -> {Cp:.4f}")
    print(f"Improvements: phi={PHI:.4f}, phi^2={PHI**2:.4f}")
