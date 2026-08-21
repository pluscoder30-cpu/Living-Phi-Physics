#!/usr/bin/env python3
import math
PHI=1.618033988749895
def coherence_nn(L,C=0.85): return C*PHI**(1-math.exp(-L/816))
if __name__=="__main__":
    for L in [12,24,48,96,192,384,768]:
        c=coherence_nn(L); print(f"L={L:4d} C_phi={c:.4f} ratio={c/0.85:.4f}")
    print(f"L->inf: ratio={coherence_nn(10**6)/0.85:.4f} target={PHI:.4f}")
