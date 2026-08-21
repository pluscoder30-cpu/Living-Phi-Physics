#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_cloud(r,r0,A,P): return A*PHI, P*PHI**(1-1/PHI)
def droplet_dist(n0,r,r0): return n0*PHI**(r/r0)
if __name__=="__main__":
    A=1.0; P=0.3
    Ap,Pp=phi_cloud(0,0,A,P)
    print(f"Autoconversion: {A:.2f} -> {Ap:.4f}")
    print(f"Precipitation efficiency: {P:.4f} -> {Pp:.4f}")
    for r in [5,10,20,30,40]:
        d=droplet_dist(100,r,10)
        print(f"r={r:3d}um n_phi={d:.2f}")
    print(f"Efficiency improvement: phi^(1-1/phi)={PHI**(1-1/PHI):.4f}")
