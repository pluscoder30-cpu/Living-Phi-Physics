#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_acoustic(a,TL,BW): return a*PHI**2, TL+10*math.log10(PHI), BW*PHI
if __name__=="__main__":
    a=0.1; TL=20.0; BW=100.0
    ap,TLp,BWp=phi_acoustic(a,TL,BW)
    print(f"Damping: {a:.4f} -> {ap:.4f}")
    print(f"Transmission loss: {TL:.1f} -> {TLp:.2f} dB")
    print(f"Bandwidth: {BW:.1f} -> {BWp:.2f} Hz")
    print(f"Damping improvement: phi^2={PHI**2:.4f}")
