#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_bw(B,snr): return B*PHI**(snr/PHI)
if __name__=="__main__":
    B=1e6
    for db in [0,3,6,10,13,20]:
        sl=10**(db/10); print(f"SNR={db:2d}dB B_phi={phi_bw(B,sl)/1e6:.4f}MHz ratio={phi_bw(B,sl)/B:.4f}")
    print(f"SNR=phi: ratio={PHI**PHI:.4f}")
