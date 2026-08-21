#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_credit(D,A,E,L): return D*PHI, A*PHI**(1-1/PHI), E/PHI, L/PHI
if __name__=="__main__":
    D=0.85; A=0.80; E=50000.0; L=0.60
    Dp,Ap,Ep,Lp=phi_credit(D,A,E,L)
    print(f"Default prediction: {D:.4f} -> {Dp:.4f}")
    print(f"AUC: {A:.4f} -> {Ap:.4f}")
    print(f"Exposure: {E:.0f} -> {Ep:.0f}")
    print(f"Loss given default: {L:.4f} -> {Lp:.4f}")
    print(f"AUC improvement: phi^(1-1/phi)={PHI**(1-1/PHI):.4f}")
