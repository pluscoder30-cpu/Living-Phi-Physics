#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_cnc(W,F,L,V): return W*PHI, F*PHI, L*PHI, V/PHI
if __name__=="__main__":
    W=0.80; F=0.90; L=100.0; V=1.0
    Wp,Fp,Lp,Vp=phi_cnc(W,F,L,V)
    print(f"Wear prediction: {W:.4f} -> {Wp:.4f}")
    print(f"Surface finish: {F:.4f} -> {Fp:.4f}")
    print(f"Tool life: {L:.0f} -> {Lp:.0f}min")
    print(f"Vibration: {V:.2f} -> {Vp:.4f}mm/s")
    print(f"Tool life gain: phi={PHI:.4f}")
