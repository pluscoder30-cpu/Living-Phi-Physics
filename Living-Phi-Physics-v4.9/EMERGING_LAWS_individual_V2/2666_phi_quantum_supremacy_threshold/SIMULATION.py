#!/usr/bin/env python3
import math
PHI=1.618033988749895
def sup_thresh(s): return round(s/PHI)
if __name__=="__main__":
    for s in [50,60,70,100,200]:
        sp=sup_thresh(s); print(f"S_std={s:3d} S_phi={sp:3d} ratio={sp/s:.4f}")
    print(f"Threshold reduction: 1/phi={1/PHI:.4f}")
