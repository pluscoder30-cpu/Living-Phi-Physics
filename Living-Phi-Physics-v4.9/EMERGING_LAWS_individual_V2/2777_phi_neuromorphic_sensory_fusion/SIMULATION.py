#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_sensory(BW,L,M,A): return BW*PHI, L/PHI, M*PHI, A*PHI**(1/PHI)
if __name__=="__main__":
    BW=1e6; L=10.0; M=1.0; A=0.90
    BWp,Lp,Mp,Ap=phi_sensory(BW,L,M,A)
    print(f"Bandwidth: {BW:.2e} -> {BWp:.2e} events/s")
    print(f"Latency: {L:.1f} -> {Lp:.2f}ms")
    print(f"Multimodal: {M:.2f} -> {Mp:.4f}")
    print(f"Attention: {A:.4f} -> {Ap:.4f}")
    print(f"Bandwidth gain: phi={PHI:.4f}")
