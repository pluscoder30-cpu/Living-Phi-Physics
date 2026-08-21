#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_fold(t_std,co): return t_std/PHI, math.exp(-co)*PHI
def native_prob(P0,co): return P0*PHI**(1-co)
if __name__=="__main__":
    for co in [0.1,0.2,0.3,0.4,0.5,0.6]:
        tp,nf=phi_fold(100,co); pn=native_prob(0.5,co)
        print(f"contact_order={co:.1f} t_fold={tp:.2f}ms P_native={pn:.4f}")
    print(f"Folding speedup: phi={PHI:.4f}")
