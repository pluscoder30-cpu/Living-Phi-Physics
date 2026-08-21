#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_cnt(gm,SS,R): return gm*PHI, SS/PHI, R*PHI**(1/PHI)
if __name__=="__main__":
    gm=1.0; SS=70.0; R=1e6
    gmp,SSp,Rp=phi_cnt(gm,SS,R)
    print(f"Transconductance: {gm:.4f} -> {gmp:.4f} mS")
    print(f"Subthreshold swing: {SS:.1f} -> {SSp:.2f} mV/dec")
    print(f"On/off ratio: {R:.0e} -> {Rp:.2e}")
    print(f"gm improvement: phi={PHI:.4f}")
