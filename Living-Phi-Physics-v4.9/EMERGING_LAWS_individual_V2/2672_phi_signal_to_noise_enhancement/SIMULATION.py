#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_snr(S,C): return S*PHI**C
if __name__=="__main__":
    S=100  # linear
    for C in [0.0,0.2,0.4,0.563,0.8,1.0]:
        s=phi_snr(S,C); print(f"C={C:.3f} SNR_phi={10*math.log10(s):.2f}dB imp={10*math.log10(s/S):.2f}dB")
    print(f"Max improvement: {10*math.log10(PHI):.2f}dB")
