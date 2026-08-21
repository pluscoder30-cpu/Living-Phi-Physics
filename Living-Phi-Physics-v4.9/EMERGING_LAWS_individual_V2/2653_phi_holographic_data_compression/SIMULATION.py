#!/usr/bin/env python3
import math
PHI=1.618033988749895
def cr_max(d): return PHI**(d/2)
def cr_prac(d): return PHI**(d/4)
if __name__=="__main__":
    for d in [64,128,256,512,816,1024]:
        print(f"d={d:4d} CR_max={cr_max(d):.2e} CR_prac={cr_prac(d):.2e}")
    print(f"816D log10={math.log10(cr_max(816)):.1f}")
