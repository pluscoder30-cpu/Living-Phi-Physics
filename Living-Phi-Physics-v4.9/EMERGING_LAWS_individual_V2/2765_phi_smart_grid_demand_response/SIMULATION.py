#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_dr(F,PS,I,S): return F*PHI, PS*PHI**(1/PHI), I*PHI, S*PHI
if __name__=="__main__":
    F=100.0; PS=50.0; I=1.0; S=0.90
    Fp,PSp,Ip,Sp=phi_dr(F,PS,I,S)
    print(f"Flexibility: {F:.1f} -> {Fp:.2f} MW")
    print(f"Peak shaving: {PS:.1f} -> {PSp:.2f} MW")
    print(f"Incentive efficiency: {I:.2f} -> {Ip:.4f}")
    print(f"Grid stability: {S:.4f} -> {Sp:.4f}")
    print(f"Flexibility gain: phi={PHI:.4f}")
