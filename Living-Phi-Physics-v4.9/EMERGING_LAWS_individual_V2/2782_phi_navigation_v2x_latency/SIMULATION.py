#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_v2x(L,T,PL,S): return L/PHI, T*PHI, PL/PHI**2, S*PHI
if __name__=="__main__":
    L=20.0; T=1e6; PL=0.01; S=100.0
    Lp,Tp,PLp,Sp=phi_v2x(L,T,PL,S)
    print(f"Latency: {L:.1f} -> {Lp:.2f}ms")
    print(f"Throughput: {T:.2e} -> {Tp:.2e}")
    print(f"Packet loss: {PL:.4f} -> {PLp:.6f}")
    print(f"Safety margin: {S:.1f} -> {Sp:.2f}m")
    print(f"Packet loss reduction: phi^2={PHI**2:.4f}")
