#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_emb(D,dm): return round(D*PHI**(-1/math.sqrt(dm)))
if __name__=="__main__":
    D=300
    for dm in [128,256,512,768,1024]:
        dp=phi_emb(D,dm); print(f"d_model={dm:4d} D_std={D:3d} D_phi={dp:3d} ratio={dp/D:.4f}")
    print(f"Approaches 1/phi={1/PHI:.4f}")
