#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_ocean(Q,dTdz,eta,v): return Q*PHI**(dTdz), eta*PHI, v*PHI
if __name__=="__main__":
    Q=1.0; dTdz=0.5; eta=0.3; v=1.0
    Qp,etap,vp=phi_ocean(Q,dTdz,eta,v)
    print(f"Heat transport: {Q:.2f} -> {Qp:.4f} PW")
    print(f"Efficiency: {eta:.4f} -> {etap:.4f}")
    print(f"Anomaly velocity: {v:.2f} -> {vp:.4f} cm/s")
    print(f"Efficiency gain: phi={PHI:.4f}")
