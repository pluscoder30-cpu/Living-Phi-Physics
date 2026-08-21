#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_balance(workloads,nw):
    loads=[0.0]*nw
    for w in sorted(workloads,reverse=True):
        loads[loads.index(min(loads))]+=w
    return max(loads)-min(loads)
if __name__=="__main__":
    import random; random.seed(42)
    wl=[random.randint(10,100) for _ in range(100)]
    for n in [4,8,16]:
        imb=phi_balance(wl,n); print(f"workers={n:2d} imbalance={imb:.1f}")
    print(f"Reduction: 1/phi={1/PHI:.4f}")
