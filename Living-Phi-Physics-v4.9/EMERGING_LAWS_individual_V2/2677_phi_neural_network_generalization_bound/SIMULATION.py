#!/usr/bin/env python3
import math
PHI=1.618033988749895
def gen_bound(N,dvc,phi_mode=False):
    d=dvc/PHI if phi_mode else dvc
    if 2*N<=d: return float('inf')
    return math.sqrt(d*(math.log(2*N/d)+1)/N)
if __name__=="__main__":
    dvc=100
    for N in [200,500,1000,5000,10000]:
        gs=gen_bound(N,dvc); gp=gen_bound(N,dvc,True); print(f"N={N:5d} G_std={gs:.6f} G_phi={gp:.6f} ratio={gp/gs:.4f}")
    print(f"Expected: 1/sqrt(phi)={1/math.sqrt(PHI):.4f}")
