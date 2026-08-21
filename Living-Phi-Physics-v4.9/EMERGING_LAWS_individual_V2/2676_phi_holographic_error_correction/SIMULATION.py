#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_ecc(d,E): return E*PHI**d
def class_ecc(d,E): return E*2**(d/2)
if __name__=="__main__":
    for d in [8,16,32,64,128]:
        print(f"d={d:3d} E_phi={phi_ecc(0.01,d):.2e} E_class={class_ecc(0.01,d):.2e}")
    print(f"phi^64={PHI**64:.2e}")
