#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_fc(eta,D,W,T): return eta*PHI**(1-1/PHI), D*PHI**2, W*PHI, T/PHI
if __name__=="__main__":
    eta=0.55; D=5000.0; W=0.80; T=5.0
    etap,Dp,Wp,Tp=phi_fc(eta,D,W,T)
    print(f"Efficiency: {eta:.4f} -> {etap:.4f}")
    print(f"Durability: {D:.0f} -> {Dp:.0f}hrs")
    print(f"Water management: {W:.4f} -> {Wp:.4f}")
    print(f"Startup: {T:.1f} -> {Tp:.2f}s")
    print(f"Efficiency improvement: phi^(1-1/phi)={PHI**(1-1/PHI):.4f}")
