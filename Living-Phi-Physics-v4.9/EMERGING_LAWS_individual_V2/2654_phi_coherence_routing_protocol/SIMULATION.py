#!/usr/bin/env python3
import math,random
PHI=1.618033988749895
def coh_target(k): return PHI**(-k)
if __name__=="__main__":
    for k in range(8): print(f"k={k} C_target={coh_target(k):.6f}")
    N=50; random.seed(42)
    print(f"Routing table entries: O({PHI:.2f}*log({N})) = O({PHI*math.log(N):.1f})")
