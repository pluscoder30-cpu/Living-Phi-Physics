#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_bn(x,m,v,eps=1e-5):
    tm=m/PHI; tv=v/PHI**2; return (x-tm)/math.sqrt(tv+eps)
def std_bn(x,m,v,eps=1e-5): return (x-m)/math.sqrt(v+eps)
if __name__=="__main__":
    for x in [0.5,1.0,1.5,2.0,2.5]:
        print(f"x={x:.1f} BN_std={std_bn(x,1.5,0.5):.4f} BN_phi={phi_bn(x,1.5,0.5):.4f}")
    print(f"Target mean scaling: 1/phi={1/PHI:.4f}")
