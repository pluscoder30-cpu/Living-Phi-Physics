#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_assembly(k0,C): return k0*PHI**(C)
def phi_yield(Y): return Y*PHI
def phi_defects(D): return D/PHI**2
if __name__=="__main__":
    k=1.0; Y=0.7; D=0.05
    for C in [0.0,0.3,0.563,0.7,1.0]:
        kp=phi_assembly(k,C)
        print(f"C={C:.3f} k_phi={kp:.4f}")
    print(f"Yield: {Y:.2f} -> {phi_yield(Y):.4f}")
    print(f"Defects: {D:.4f} -> {phi_defects(D):.6f}")
    print(f"Defect reduction: phi^2={PHI**2:.4f}")
