#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_fiber(N,R,C,O):
    return N/PHI, R*PHI, C*PHI**(1-1/PHI), O+10*math.log10(PHI)
if __name__=="__main__":
    N=1.0; R=1000.0; C=1e13; O=20.0
    Np,Rp,Cp,Op=phi_fiber(N,R,C,O)
    print(f"Nonlinearity: {N:.4f} -> {Np:.4f}")
    print(f"Reach: {R:.0f} -> {Rp:.0f}km")
    print(f"Capacity: {C:.2e} -> {Cp:.2e}")
    print(f"OSNR: {O:.1f} -> {Op:.2f}dB")
    print(f"Nonlinearity reduction: 1/phi={1/PHI:.4f}")
