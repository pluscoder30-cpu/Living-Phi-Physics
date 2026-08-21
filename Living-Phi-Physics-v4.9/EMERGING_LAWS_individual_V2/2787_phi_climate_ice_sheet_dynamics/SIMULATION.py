#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_ice(v,C,B,S): return v*PHI, C/PHI, B*PHI**(1/PHI), S*PHI
if __name__=="__main__":
    v=1000.0; C=0.50; B=0.80; S=1.0
    vp,Cp,Bp,Sp=phi_ice(v,C,B,S)
    print(f"Flow velocity: {v:.0f} -> {vp:.0f}m/yr")
    print(f"Calving rate: {C:.4f} -> {Cp:.4f}")
    print(f"Basal sliding: {B:.4f} -> {Bp:.4f}")
    print(f"Sea level: {S:.2f} -> {Sp:.4f}mm/yr")
    print(f"Calving reduction: 1/phi={1/PHI:.4f}")
