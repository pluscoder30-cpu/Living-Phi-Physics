#!/usr/bin/env python3
import math
PHI=1.618033988749895; C_MAX=0.8565
def g_ai(g0,C): return g0*PHI*C
if __name__=="__main__":
    for C in [0.0,0.2,0.4,0.563,0.7,C_MAX,1.0]:
        print(f"C={C:.3f} g/g0={g_ai(1,C):.4f}")
    print(f"Max (C={C_MAX}): g/g0={PHI*C_MAX:.4f}")
