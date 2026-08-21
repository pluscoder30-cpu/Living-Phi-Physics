#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_ncr(n): return n*PHI**2
def ncr_db(n): return 10*math.log10(n)
if __name__=="__main__":
    for n in [10,20,40,100]:
        np=phi_ncr(n); print(f"NCR_std={n:3d} NCR_phi={np:.1f} imp={ncr_db(np)-ncr_db(n):.2f}dB")
    print(f"Improvement: phi^2={PHI**2:.4f}x = {10*math.log10(PHI**2):.2f}dB")
