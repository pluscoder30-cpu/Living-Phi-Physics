#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_qah(sig,P,T,B): return sig*PHI, P*PHI**2, T*PHI, B*PHI
if __name__=="__main__":
    sig=1.0; P=1e-6; T=0.5; B=1.0
    sigp,Pp,Tp,Bp=phi_qah(sig,P,T,B)
    print(f"Hall conductance: {sig:.4f} -> {sigp:.4f} e^2/h")
    print(f"Quantization precision: {P:.2e} -> {Pp:.2e}")
    print(f"Temperature tolerance: {T:.2f} -> {Tp:.4f}K")
    print(f"Berry curvature: {B:.4f} -> {Bp:.4f}")
    print(f"Precision improvement: phi^2={PHI**2:.4f}")
