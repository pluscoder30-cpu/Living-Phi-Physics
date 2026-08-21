#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_ae(T,C): return T*PHI**(-C)
if __name__=="__main__":
    for C in [0.0,0.3,0.5,0.7,0.8565,1.0]:
        t=phi_ae(1,C); print(f"C={C:.4f} T_ae={t:.4f} speedup={1/t:.4f}")
    print(f"Full coherence speedup: phi={PHI:.4f}")
