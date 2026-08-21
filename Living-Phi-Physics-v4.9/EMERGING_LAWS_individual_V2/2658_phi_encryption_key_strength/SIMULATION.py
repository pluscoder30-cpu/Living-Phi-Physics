#!/usr/bin/env python3
import math
PHI=1.618033988749895
def key_str(n): return n+n/PHI, n/PHI
def key_mult(n): return PHI**(n/PHI)
if __name__=="__main__":
    for n in [128,192,256,512,1024]:
        eff,add=key_str(n); print(f"n={n:4d} eff={eff:.2f} add={add:.2f} mult={key_mult(n):.2e}")
    print(f"Additional bits for 256-bit key: {256/PHI:.2f}")
