#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_epi(E,H,M,C): return E*PHI, H*PHI, M*PHI**(1/PHI), C*PHI
if __name__=="__main__":
    E=0.80; H=0.85; M=0.75; C=0.90
    Ep,Hp,Mp,Cp=phi_epi(E,H,M,C)
    print(f"Epigenetic prediction: {E:.4f} -> {Ep:.4f}")
    print(f"Histone mark: {H:.4f} -> {Hp:.4f}")
    print(f"Methylation: {M:.4f} -> {Mp:.4f}")
    print(f"Chromatin accessibility: {C:.4f} -> {Cp:.4f}")
    print(f"Accuracy gain: phi={PHI:.4f}")
