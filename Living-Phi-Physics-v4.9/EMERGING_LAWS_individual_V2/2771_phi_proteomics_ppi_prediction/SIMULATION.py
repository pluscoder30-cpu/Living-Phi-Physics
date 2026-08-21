#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_ppi(A,I,K,S): return A*PHI, I*PHI**(1-1/PHI), K/PHI, S*PHI
if __name__=="__main__":
    A=0.80; I=0.75; K=100.0; S=0.85
    Ap,Ip,Kp,Sp=phi_ppi(A,I,K,S)
    print(f"Accuracy: {A:.4f} -> {Ap:.4f}")
    print(f"Interface: {I:.4f} -> {Ip:.4f}")
    print(f"Binding affinity: {K:.1f} -> {Kp:.2f}nM")
    print(f"Specificity: {S:.4f} -> {Sp:.4f}")
    print(f"Accuracy gain: phi={PHI:.4f}")
