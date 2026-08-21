#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_eta(e): return e*PHI**2
if __name__=="__main__":
    e=1.0; ep=phi_eta(e)
    for s in [100,500,1000,5000]:
        print(f"steps={s:5d} K_std={e*s:8.0f} K_phi={ep*s:8.0f} ratio={ep/e:.4f}")
    print(f"Efficiency: phi^2={PHI**2:.4f}")
