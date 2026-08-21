#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_mse(m): return m/PHI
if __name__=="__main__":
    for db in [0,5,10,15,20,25]:
        nv=1/10**(db/10); ms=nv; mp=phi_mse(ms)
        print(f"SNR={db:2d}dB MSE_std={ms:.6f} MSE_phi={mp:.6f} imp={ms/mp:.4f}x")
    print(f"Improvement: 1/phi={1/PHI:.4f}")
