#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_rate(k,n): return k/n
def phi_redund(k,n): return 1-k/n
if __name__=="__main__":
    for k in [100,256,512,1024]:
        n=round(k*PHI); print(f"k={k:5d} n={n:5d} rate={phi_rate(k,n):.4f} redund={phi_redund(k,n):.4f}")
    print(f"Phi redundancy floor: 1/phi={1/PHI:.4f}")
