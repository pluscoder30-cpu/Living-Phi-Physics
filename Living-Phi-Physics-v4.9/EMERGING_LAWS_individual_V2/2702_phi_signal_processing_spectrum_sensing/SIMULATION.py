#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_pd(P,snr): return min(1.0,P*PHI**(snr/PHI**2))
if __name__=="__main__":
    P=0.8
    for db in [-10,-5,0,5,10]:
        sl=10**(db/10); pp=phi_pd(P,sl); print(f"SNR={db:3d}dB P_d={pp:.4f} ratio={pp/P:.4f}")
    print(f"Enhancement: phi^(SNR/phi^2)")
