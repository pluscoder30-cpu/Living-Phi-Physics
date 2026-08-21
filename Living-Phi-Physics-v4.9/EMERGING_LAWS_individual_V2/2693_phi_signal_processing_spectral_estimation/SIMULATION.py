#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_acc(s): return s/math.sqrt(PHI)
if __name__=="__main__":
    s=0.1
    print(f"std sigma={s:.4f} phi sigma={phi_acc(s):.4f} improvement={s/phi_acc(s):.4f}x")
    print(f"Target: sqrt(phi)={math.sqrt(PHI):.4f}")
