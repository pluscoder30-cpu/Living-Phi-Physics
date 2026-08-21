#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_causal(W): return W*PHI
if __name__=="__main__":
    W=1000
    for n in [500,1000,2000,5000,10000]:
        ws=max(0,n-W); wp=max(0,n-int(phi_causal(W)))
        print(f"events={n:5d} viol_std={ws:5d} viol_phi={wp:5d}")
    print(f"Window extension: phi={PHI:.4f}")
