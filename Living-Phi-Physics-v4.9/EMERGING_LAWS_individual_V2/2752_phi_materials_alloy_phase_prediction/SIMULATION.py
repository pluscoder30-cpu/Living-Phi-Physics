#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_alloy(P,E,S): return P*PHI, E/PHI, S*PHI**(1/PHI)
if __name__=="__main__":
    P=0.75; E=100.0; S=1000
    Pp,Ep,Sp=phi_alloy(P,E,S)
    print(f"Accuracy: {P:.4f} -> {Pp:.4f}")
    print(f"Exploration cost: {E:.0f} -> {Ep:.2f}kcal/mol")
    print(f"Search space: {S} -> {Sp:.0f}")
    print(f"Accuracy gain: phi={PHI:.4f}")
