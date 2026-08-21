#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_gain(G,N): return G*PHI**(N/816)
if __name__=="__main__":
    for N in [64,128,256,512,816,1024]:
        gu=N; gp=phi_gain(gu,N)
        print(f"N={N:4d} G_std={gu:5d} G_phi={gp:.2f} ratio={gp/gu:.4f}")
    print(f"At N=816: ratio=phi={PHI:.4f}")
