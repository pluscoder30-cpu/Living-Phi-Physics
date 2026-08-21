#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_screen(E,H,FP,T): return E*PHI, H*PHI, FP/PHI, T*PHI**(1/PHI)
if __name__=="__main__":
    E=10.0; H=0.02; FP=0.30; T=1e6
    Ep,Hp,FPp,Tp=phi_screen(E,H,FP,T)
    print(f"Enrichment: {E:.1f} -> {Ep:.2f}")
    print(f"Hit rate: {H:.4f} -> {Hp:.4f}")
    print(f"False positives: {FP:.4f} -> {FPp:.4f}")
    print(f"Throughput: {T:.0e} -> {Tp:.2e}")
    print(f"Enrichment gain: phi={PHI:.4f}")
