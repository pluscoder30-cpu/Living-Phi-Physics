#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_mem(T): return T*PHI**2
if __name__=="__main__":
    for T in [10,50,100,500,1000]:
        print(f"T_std={T:5d}us T_phi={phi_mem(T):.1f}us ratio={phi_mem(T)/T:.4f}")
    print(f"Extension: phi^2={PHI**2:.4f}")
