#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_decay(dist): return 1.0/PHI**(dist/816)
if __name__=="__main__":
    for sl in [128,256,512,1024,2048,4096]:
        d=phi_decay(sl); print(f"Seq={sl:5d} decay_end={d:.4f} eff_ctx={sl*PHI:.0f}")
    print(f"Context extension: {PHI:.4f}x")
