#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_qec(k=1): n=round(k*PHI**2); d=round(PHI**3); return n,d,d//2
if __name__=="__main__":
    for k in [1,2,3,4,5]:
        n,d,t=phi_qec(k); print(f"k={k} n={n} d={d} t={t} ratio={n/k:.3f}")
    print(f"Ratio converges to phi^2={PHI**2:.4f}")
