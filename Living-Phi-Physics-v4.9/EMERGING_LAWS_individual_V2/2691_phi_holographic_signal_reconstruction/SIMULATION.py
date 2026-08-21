#!/usr/bin/env python3
import math
PHI=1.618033988749895
def recon_f(F,d): return F*PHI**(d/816)
if __name__=="__main__":
    F=0.9
    for d in [64,128,256,512,816,1024]:
        print(f"d={d:4d} F_recon={recon_f(F,d):.6f} ratio={recon_f(F,d)/F:.4f}")
    print(f"At d=816: ratio={PHI:.4f}")
