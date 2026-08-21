#!/usr/bin/env python3
import math
PHI=1.618033988749895; TAU=PHI**5
def retro_err(E0,t,n): return E0*math.exp(-t/TAU)*(1+PHI**(-n/816))
if __name__=="__main__":
    for n in [0,1,2,5,10,20,50]:
        print(f"steps={n:2d} E(t=1)={retro_err(1,1,n):.6f} E(t=10)={retro_err(1,10,n):.6f}")
    print(f"tau_retro={TAU:.4f}")
