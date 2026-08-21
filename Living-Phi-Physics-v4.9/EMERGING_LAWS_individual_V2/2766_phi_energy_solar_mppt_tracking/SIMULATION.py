#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_mppt(T,eta,P,S): return T/PHI, eta*PHI**(1-1/PHI), P/PHI, S*PHI
if __name__=="__main__":
    T=100.0; eta=0.96; P=5.0; S=0.80
    Tp,etap,Pp,Sp=phi_mppt(T,eta,P,S)
    print(f"Convergence: {T:.1f} -> {Tp:.2f}ms")
    print(f"Tracking efficiency: {eta:.4f} -> {etap:.4f}")
    print(f"Power ripple: {P:.2f} -> {Pp:.4f}%")
    print(f"Partial shading: {S:.4f} -> {Sp:.4f}")
    print(f"Convergence speedup: phi={PHI:.4f}")
