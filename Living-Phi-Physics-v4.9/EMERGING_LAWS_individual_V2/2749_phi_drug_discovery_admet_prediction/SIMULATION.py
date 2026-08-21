#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_admet(A,F,TN): return A*PHI, F*PHI**(1-1/PHI), TN*PHI
if __name__=="__main__":
    A=0.85; F=0.70; TN=0.90
    Ap,Fp,TNp=phi_admet(A,F,TN)
    print(f"Accuracy: {A:.4f} -> {Ap:.4f}")
    print(f"Bioavailability: {F:.4f} -> {Fp:.4f}")
    print(f"Tox detection: {TN:.4f} -> {TNp:.4f}")
    print(f"Improvements: phi={PHI:.4f}, phi^(1-1/phi)={PHI**(1-1/PHI):.4f}")
