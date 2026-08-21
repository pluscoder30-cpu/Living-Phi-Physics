#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_heal(T,C): return T*PHI**(-C)
if __name__=="__main__":
    for C in [0.0,0.2,0.4,0.563,0.8,1.0]:
        t=phi_heal(1,C); print(f"C={C:.3f} T_heal={t:.4f} speedup={1/t:.4f}")
    print(f"Full coherence speedup: phi={PHI:.4f}")
