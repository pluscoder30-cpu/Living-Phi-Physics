#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_eta(e,d): return e*PHI**(d/1632)
if __name__=="__main__":
    for d in [64,128,256,512,816,1024,1632]:
        print(f"d={d:5d} eta_phi={phi_eta(1,d):.4f} ratio={phi_eta(1,d):.4f}")
    print(f"At d=816: phi^0.5={PHI**0.5:.4f}")
