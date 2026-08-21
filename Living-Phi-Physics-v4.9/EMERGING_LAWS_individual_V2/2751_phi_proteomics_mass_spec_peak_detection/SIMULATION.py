#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_ms(S,R,FDR,DR): return S*PHI, R*PHI, FDR/PHI, DR*PHI**2
if __name__=="__main__":
    S=0.80; R=10000.0; FDR=0.05; DR=1e4
    Sp,Rp,FDRp,DRp=phi_ms(S,R,FDR,DR)
    print(f"Sensitivity: {S:.4f} -> {Sp:.4f}")
    print(f"Resolution: {R:.0f} -> {Rp:.0f}")
    print(f"FDR: {FDR:.4f} -> {FDRp:.4f}")
    print(f"Dynamic range: {DR:.0e} -> {DRp:.2e}")
    print(f"DR improvement: phi^2={PHI**2:.4f}")
