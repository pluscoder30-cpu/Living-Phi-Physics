#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_qled(EQE,SP,L,V):
    return EQE*PHI**(1-1/PHI), SP*PHI, L*PHI**2, V/PHI
if __name__=="__main__":
    EQE=0.20; SP=0.95; L=50000.0; V=3.0
    EQEp,SPp,Lp,Vp=phi_qled(EQE,SP,L,V)
    print(f"EQE: {EQE:.4f} -> {EQEp:.4f}")
    print(f"Spectral purity: {SP:.4f} -> {SPp:.4f}")
    print(f"Lifetime: {L:.0f} -> {Lp:.0f}hrs")
    print(f"Turn-on voltage: {V:.2f} -> {Vp:.4f}V")
    print(f"EQE improvement: phi^(1-1/phi)={PHI**(1-1/PHI):.4f}")
