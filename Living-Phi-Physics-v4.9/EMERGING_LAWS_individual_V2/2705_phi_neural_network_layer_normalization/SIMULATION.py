#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_ln(x,eps=1e-5):
    d=len(x); m=sum(x)/d
    v=sum((xi-m)**2 for xi in x)/d
    ns=sum(xi**2 for xi in x)/d
    sig=math.sqrt(v+ns/PHI**2+eps)
    return [(xi-m)/sig for xi in x]
if __name__=="__main__":
    x=[1.0,2.0,3.0,4.0,5.0]
    r=phi_ln(x); mr=sum(r)/len(r); vr=sum((ri-mr)**2 for ri in r)/len(r)
    print(f"Input: {x}")
    print(f"Phi-norm: {[f'{ri:.4f}' for ri in r]}")
    print(f"mean={mr:.6f} var={vr:.6f}")
