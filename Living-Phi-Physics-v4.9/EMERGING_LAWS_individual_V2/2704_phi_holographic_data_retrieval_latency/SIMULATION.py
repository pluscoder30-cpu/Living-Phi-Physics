#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_lat(L,d): return L/PHI**(d/816)
if __name__=="__main__":
    L=100
    for d in [64,128,256,512,816,1024]:
        print(f"d={d:4d} L_phi={phi_lat(L,d):.2f}ms speedup={L/phi_lat(L,d):.4f}")
    print(f"At d=816: speedup=phi={PHI:.4f}")
