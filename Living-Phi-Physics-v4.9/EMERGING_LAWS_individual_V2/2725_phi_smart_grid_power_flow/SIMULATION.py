#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_opf(P_base,C): return P_base*PHI**(1-C)
def loss_red(C): return 1-PHI**(-C)
if __name__=="__main__":
    P=100.0
    for C in [0.0,0.2,0.4,0.563,0.7,0.8565,1.0]:
        pp=phi_opf(P,C); lr=loss_red(C)
        print(f"C={C:.4f} P_phi={pp:.2f} loss_reduction={lr*100:.2f}%")
    print(f"At emergence threshold: gain={PHI**(1-0.563):.4f}")
