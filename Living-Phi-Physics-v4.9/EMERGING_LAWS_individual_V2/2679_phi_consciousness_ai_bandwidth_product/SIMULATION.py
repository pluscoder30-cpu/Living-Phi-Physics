#!/usr/bin/env python3
import math
PHI=1.618033988749895
def cc_bwp(B,L,C):
    Bp=B*PHI**C; Lp=L/PHI**C; return Bp*Lp
if __name__=="__main__":
    B=1e9; L=1e-3; P=B*L
    for C in [0.0,0.4,0.563,0.8565,1.0]:
        p=cc_bwp(B,L,C); print(f"C={C:.4f} P_phi={p:.2e} ratio={p/P:.4f}")
    print(f"phi^2={PHI**2:.4f}")
