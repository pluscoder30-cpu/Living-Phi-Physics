#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_vol(sigma0,K,K_atm,T): return sigma0*PHI**(-abs(K-K_atm)/PHI)
def phi_smile(curv): return curv/PHI
def phi_skew(skew): return skew/PHI
if __name__=="__main__":
    s0=0.20; K_atm=100.0
    for K in [80,90,100,110,120]:
        sp=phi_vol(s0,K,K_atm,1.0)
        print(f"K={K:3.0f} sigma_std={s0:.4f} sigma_phi={sp:.4f}")
    print(f"Smile curvature reduction: 1/phi={1/PHI:.4f}")
    print(f"Skew reduction: 1/phi={1/PHI:.4f}")
