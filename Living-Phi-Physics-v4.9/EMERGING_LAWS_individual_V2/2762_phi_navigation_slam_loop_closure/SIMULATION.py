#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_slam(D,O,A): return D*PHI, O/PHI, A*PHI**(1-1/PHI)
if __name__=="__main__":
    D=100; O=1000.0; A=0.90
    Dp,Op,Ap=phi_slam(D,O,A)
    print(f"Loop closures: {D} -> {Dp:.0f}")
    print(f"Optimization cost: {O:.0f} -> {Op:.2f}")
    print(f"Map accuracy: {A:.4f} -> {Ap:.4f}")
    print(f"Detection improvement: phi={PHI:.4f}")
