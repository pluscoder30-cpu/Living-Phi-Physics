#!/usr/bin/env python3
import math
PHI=1.618033988749895
def D(): return 2-1/PHI
def saddles(N): return N/PHI
if __name__=="__main__":
    print(f"Fractal dimension: {D():.4f}")
    for N in [100,500,1000,5000]:
        print(f"N_std={N:5d} N_phi={saddles(N):.1f}")
    print(f"Saddle reduction: 1/phi={1/PHI:.4f}")
