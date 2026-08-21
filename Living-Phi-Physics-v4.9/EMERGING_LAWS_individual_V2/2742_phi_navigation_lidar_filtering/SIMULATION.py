#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_lidar(rho,FP,N,T): return rho*PHI, FP/PHI**2, T/PHI**(N/816)
if __name__=="__main__":
    for N in [10000,50000,100000,500000]:
        rp,fp,tp=phi_lidar(1.0,0.1,N,100.0)
        print(f"N={N:7d} density={rp:.4f} FP={fp:.6f} T_phi={tp:.4f}ms")
    print(f"FP suppression: phi^2={PHI**2:.4f}")
