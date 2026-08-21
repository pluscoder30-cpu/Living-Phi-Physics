#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_ti(G,BS,v,D): return G*PHI, BS/PHI**2, v*PHI, D*PHI
if __name__=="__main__":
    G=1.0; BS=0.1; v=1e6; D=0.01
    Gp,BSp,vp,Dp=phi_ti(G,BS,v,D)
    print(f"Conductance: {G:.2f} -> {Gp:.4f} e^2/h")
    print(f"Backscattering: {BS:.4f} -> {BSp:.6f}")
    print(f"Chiral velocity: {v:.2e} -> {vp:.2e} m/s")
    print(f"Topological gap: {D:.4f} -> {Dp:.4f} eV")
    print(f"BS suppression: phi^2={PHI**2:.4f}")
