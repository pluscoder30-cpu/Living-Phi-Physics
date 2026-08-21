#!/usr/bin/env python3
import math
PHI=1.618033988749895
def gossip_rounds(N,V): return math.ceil(math.log(N)/math.log(V))
if __name__=="__main__":
    Vs=2.0; Vp=Vs*PHI
    for N in [100,500,1000,5000,10000]:
        rs=gossip_rounds(N,Vs); rp=gossip_rounds(N,Vp)
        print(f"N={N:5d} rounds_std={rs:3d} rounds_phi={rp:3d}")
    print(f"Gossip speedup: phi={PHI:.4f}x")
