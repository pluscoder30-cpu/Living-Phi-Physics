#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_vc(N): return math.ceil(N/PHI)
if __name__=="__main__":
    for N in [10,20,50,100,200,500]:
        vp=phi_vc(N); savings=(N-vp)/N*100
        print(f"N={N:3d} V_std={N:3d} V_phi={vp:3d} savings={savings:.1f}%")
    print(f"Reduction: 1-1/phi={1-1/PHI:.4f}")
