#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_sw(lam,T,F,E): return lam*PHI, T/PHI, F*PHI, E/PHI
if __name__=="__main__":
    lam=1.0; T=10.0; F=4; E=1e-18
    lamp,Tp,Fp,Ep=phi_sw(lam,T,F,E)
    print(f"Wavelength: {lam:.2f} -> {lamp:.4f} um")
    print(f"Gate delay: {T:.1f} -> {Tp:.2f} ps")
    print(f"Fan-out: {F} -> {Fp:.0f}")
    print(f"Energy/bit: {E:.2e} -> {Ep:.2e} J")
    print(f"Fan-out gain: phi={PHI:.4f}")
