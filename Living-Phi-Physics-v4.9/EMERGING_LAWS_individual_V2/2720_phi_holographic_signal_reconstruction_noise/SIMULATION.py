#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_noise(N,d): return N/PHI**d
def snr(sig,n): return sig/n if n>0 else float('inf')
if __name__=="__main__":
    sig=10.0
    for d in [8,16,32,64,128,256]:
        np=phi_noise(1,d); print(f"d={d:4d} N_phi={np:.2e} SNR_phi={snr(sig,np):.2f}")
    print(f"816D suppression: phi^816={PHI**816:.2e}")
