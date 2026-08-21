#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_depth(Ls): return math.ceil(Ls/PHI)
if __name__=="__main__":
    for Ls in [6,10,16,24,40,64,100]:
        Lp=phi_depth(Ls); print(f"L_std={Ls:3d} L_phi={Lp:3d} ratio={Lp/Ls:.4f}")
    print(f"Target: 1/phi={1/PHI:.4f}")
