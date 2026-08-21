#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_grn_motifs(M,L): return M*PHI**(1-L/PHI)
def phi_burst(B): return B/PHI
if __name__=="__main__":
    M=100
    for L in [10,20,50,100,200,500]:
        mp=phi_grn_motifs(M,L)
        print(f"genes={L:4d} motifs_std={M:4d} motifs_phi={mp:.2f}")
    for B in [10,50,100,500]:
        bp=phi_burst(B)
        print(f"burst_std={B:4d} burst_phi={bp:.2f} ratio={bp/B:.4f}")
    print(f"Burst reduction: 1/phi={1/PHI:.4f}")
