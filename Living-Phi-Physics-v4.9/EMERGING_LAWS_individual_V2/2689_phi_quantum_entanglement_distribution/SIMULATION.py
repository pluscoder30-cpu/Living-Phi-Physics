#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_ent(E,L,Lc): return E*PHI**(1-L/Lc)
if __name__=="__main__":
    for L in [10,25,50,75,100,150,200]:
        print(f"L={L:3d}km E_phi={phi_ent(1,L,100):.4f}")
    print(f"At L=L_coh: E_phi=E_std")
