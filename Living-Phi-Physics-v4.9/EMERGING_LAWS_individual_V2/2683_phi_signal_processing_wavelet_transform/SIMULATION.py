#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_scales(n=6): return [PHI**a for a in range(n)]
if __name__=="__main__":
    for i,s in enumerate(phi_scales(6)):
        print(f"a={i} scale={s:.2f} time_res={1024/s:.2f} freq_res={1/s:.6f}")
    print(f"Joint resolution improvement: {PHI:.4f}x")
