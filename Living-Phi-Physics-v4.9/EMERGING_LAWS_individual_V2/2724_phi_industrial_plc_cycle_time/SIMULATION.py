#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_scan(T_base,n_tasks): return T_base*PHI**(-1/PHI)
def phi_det(T_scan): return T_scan/PHI
if __name__=="__main__":
    T=10.0; tasks=[10,50,100,200,500]
    for n in tasks:
        ts=phi_scan(T,n); td=phi_det(ts)
        print(f"tasks={n:4d} T_scan={ts:.4f}ms T_det={td:.4f}ms")
    print(f"Scan reduction: phi^(1/phi)={PHI**(1/PHI):.4f}")
