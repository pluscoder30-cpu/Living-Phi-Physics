#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_mux(M,d): return M*PHI**(d/2)
if __name__=="__main__":
    M=1000
    for d in [32,64,128,256,512,816]:
        print(f"d={d:4d} M_phi={phi_mux(M,d):.2e}")
    print(f"816D: {phi_mux(M,816):.2e} pages")
