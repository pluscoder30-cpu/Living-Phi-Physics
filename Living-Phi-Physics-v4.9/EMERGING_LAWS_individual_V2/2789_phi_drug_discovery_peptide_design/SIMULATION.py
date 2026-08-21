#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_pep(K,S,SEL,P): return K/PHI, S*PHI**2, SEL*PHI, P*PHI**(1/PHI)
if __name__=="__main__":
    K=100.0; S=1.0; SEL=10.0; P=0.30
    Kp,Sp,SELp,Pp=phi_pep(K,S,SEL,P)
    print(f"Binding affinity: {K:.1f} -> {Kp:.2f}nM")
    print(f"Stability: {S:.2f} -> {Sp:.4f}")
    print(f"Selectivity: {SEL:.1f} -> {SELp:.2f}")
    print(f"Permeability: {P:.4f} -> {Pp:.4f}")
    print(f"Stability improvement: phi^2={PHI**2:.4f}")
