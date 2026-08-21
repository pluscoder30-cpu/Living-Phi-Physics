#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_meta(n_std): return -1.0/PHI
def phi_bw(BW): return BW*PHI**2
def phi_loss(L): return L/PHI
def phi_res(lam): return lam/(2*PHI)
if __name__=="__main__":
    lam=1.0
    print(f"n_phi={-1/PHI:.4f}")
    for BW in [1.0,2.0,5.0,10.0]:
        print(f"BW_std={BW:.1f} BW_phi={phi_bw(BW):.4f}")
    for L in [0.5,1.0,2.0]:
        print(f"Loss_std={L:.1f} Loss_phi={phi_loss(L):.4f}")
    print(f"Resolution: lambda/(2*phi)={phi_res(lam):.4f} vs lambda/2={lam/2:.4f}")
