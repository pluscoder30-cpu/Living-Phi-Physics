#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_dock(D,N): return D*PHI**(N/PHI)
def fp_rate(N_atoms): return 0.3/PHI**(N_atoms/10)
if __name__=="__main__":
    D=-8.5
    for N in [10,20,30,40,50,60]:
        dp=phi_dock(D,N); fp=fp_rate(N)
        print(f"heavy_atoms={N:3d} D_phi={dp:.2f} FP_rate={fp:.4f}")
    print(f"FP reduction per 10 atoms: 1/phi={1/PHI:.4f}")
