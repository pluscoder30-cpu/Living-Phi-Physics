#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_pd(R,Id,NEP,Ds): return R*PHI, Id/PHI, NEP/PHI, Ds*PHI**2
if __name__=="__main__":
    R=0.8; Id=1e-9; NEP=1e-14; Ds=1e11
    Rp,Idp,NEPp,Dsp=phi_pd(R,Id,NEP,Ds)
    print(f"Responsivity: {R:.4f} -> {Rp:.4f} A/W")
    print(f"Dark current: {Id:.2e} -> {Idp:.2e} A")
    print(f"NEP: {NEP:.2e} -> {NEPp:.2e} W/Hz^0.5")
    print(f"Detectivity: {Ds:.2e} -> {Dsp:.2e} Jones")
    print(f"D* improvement: phi^2={PHI**2:.4f}")
