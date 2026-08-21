#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_retain(): return 1-1/PHI
def perf(r):
    pr=phi_retain()
    if r>=pr: return 1.0
    return 1.0/PHI**((pr-r)*PHI)
if __name__=="__main__":
    print(f"Phi-optimal retention: {phi_retain():.4f} ({phi_retain()*100:.2f}%)")
    for r in [1.0,0.9,0.8,0.618,0.5,0.382,0.3,0.2]:
        print(f"retain={r:.3f} perf={perf(r):.4f}")
