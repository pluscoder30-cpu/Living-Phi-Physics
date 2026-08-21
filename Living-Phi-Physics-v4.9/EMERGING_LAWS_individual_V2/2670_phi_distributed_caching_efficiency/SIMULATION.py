#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_hit(H,d): return H*PHI**(1-1/d)
if __name__=="__main__":
    H=0.75
    for d in [1,2,3,5,8,13,21]:
        h=phi_hit(H,d); print(f"depth={d:2d} H_phi={h:.4f} ratio={h/H:.4f}")
    print(f"phi^(1-1/phi)={PHI**(1-1/PHI):.4f}")
