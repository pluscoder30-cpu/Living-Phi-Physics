#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_cap(d): return PHI**(2*d)
def class_cap(d): return 2**d
if __name__=="__main__":
    for d in [8,16,32,64,128,256]:
        print(f"d={d:4d} C_class={class_cap(d):.2e} C_phi={phi_cap(d):.2e} ratio={phi_cap(d)/class_cap(d):.2e}")
    print(f"816D ratio: log10(phi^1632)={1632*math.log10(PHI):.1f}")
