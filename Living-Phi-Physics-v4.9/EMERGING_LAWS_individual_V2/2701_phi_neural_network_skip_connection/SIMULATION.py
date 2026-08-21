#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_dens(): return 1/PHI
if __name__=="__main__":
    d=phi_dens(); print(f"Phi skip density: {d:.4f} ({d*100:.2f}%)")
    for L in [10,20,50,100,200]:
        s=int(L*d); print(f"L={L:3d} skips={s:3d} ratio={s/L:.4f}")
    print(f"Optimal: 1/phi={1/PHI:.4f}")
