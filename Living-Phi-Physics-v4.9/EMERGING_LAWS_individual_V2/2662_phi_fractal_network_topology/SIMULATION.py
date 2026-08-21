#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_frac(g): return int(PHI**(2*g)), PHI**2, 2*g
if __name__=="__main__":
    for g in range(1,9):
        N,k,d=phi_frac(g); print(f"g={g} N={N:8d} <k>={k:.4f} D={d}")
    print(f"d_f=2*log(phi)/log(phi^2)={2*math.log(PHI)/math.log(PHI**2):.4f}")
