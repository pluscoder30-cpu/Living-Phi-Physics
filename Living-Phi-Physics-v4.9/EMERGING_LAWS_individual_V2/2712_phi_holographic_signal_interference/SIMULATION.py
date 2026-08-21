#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_ici(I,d): return I/PHI**(d/2)
if __name__=="__main__":
    for d in [32,64,128,256,512,816]:
        print(f"d={d:4d} I_phi={phi_ici(0.1,d):.2e} suppression={0.1/phi_ici(0.1,d):.2e}")
    print(f"816D suppression: phi^408={PHI**408:.2e}")
