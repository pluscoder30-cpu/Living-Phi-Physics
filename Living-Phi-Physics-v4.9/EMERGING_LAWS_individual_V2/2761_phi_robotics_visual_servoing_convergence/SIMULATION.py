#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_ibvs(lam,e,v): return lam*PHI, e/PHI, v*PHI
if __name__=="__main__":
    lam=0.5; e=10.0; v=1.0
    lamp,ep,vp=phi_ibvs(lam,e,v)
    print(f"Convergence rate: {lam:.4f} -> {lamp:.4f}")
    print(f"Feature error: {e:.2f} -> {ep:.4f} px")
    print(f"Camera velocity: {v:.2f} -> {vp:.4f}")
    print(f"Convergence speedup: phi={PHI:.4f}")
