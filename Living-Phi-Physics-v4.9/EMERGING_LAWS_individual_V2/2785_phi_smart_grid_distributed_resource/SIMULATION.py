#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_der(D,C,V,R): return D*PHI, C/PHI, V*PHI, R*PHI**(1/PHI)
if __name__=="__main__":
    D=100.0; C=0.20; V=0.95; R=0.90
    Dp,Cp,Vp,Rp=phi_der(D,C,V,R)
    print(f"Dispatch: {D:.1f} -> {Dp:.2f}MW")
    print(f"Curtailment: {C:.4f} -> {Cp:.4f}")
    print(f"Voltage: {V:.4f} -> {Vp:.4f}pu")
    print(f"Resilience: {R:.4f} -> {Rp:.4f}")
    print(f"Dispatch gain: phi={PHI:.4f}")
