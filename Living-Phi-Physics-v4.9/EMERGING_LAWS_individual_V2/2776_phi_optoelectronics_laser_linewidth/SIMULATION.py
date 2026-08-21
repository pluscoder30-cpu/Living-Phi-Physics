#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_laser(dn,RIN,P,PN): return dn/PHI, RIN/PHI**2, P*PHI, PN/PHI
if __name__=="__main__":
    dn=1e6; RIN=-155.0; P=10.0; PN=-120.0
    dnp,RINp,Pp,PNp=phi_laser(dn,RIN,P,PN)
    print(f"Linewidth: {dn:.0f} -> {dnp:.0f}Hz")
    print(f"RIN: {RIN:.1f} -> {RINp:.2f}dB/Hz")
    print(f"Coherent power: {P:.1f} -> {Pp:.2f}mW")
    print(f"Phase noise: {PN:.1f} -> {PNp:.2f}dBc/Hz")
    print(f"Linewidth reduction: 1/phi={1/PHI:.4f}")
