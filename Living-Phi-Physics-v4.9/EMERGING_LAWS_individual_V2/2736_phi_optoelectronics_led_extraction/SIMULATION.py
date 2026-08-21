#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_led(eta,iqe): return eta*PHI, iqe*PHI**(1-1/PHI)
if __name__=="__main__":
    eta=0.04; iqe=0.80
    ep,ip=phi_led(eta,iqe)
    print(f"Extraction: {eta:.4f} -> {ep:.4f} (x{ep/eta:.4f})")
    print(f"IQE: {iqe:.4f} -> {ip:.4f} (x{ip/iqe:.4f})")
    print(f"Extraction target: phi={PHI:.4f}")
    print(f"IQE target: phi^(1-1/phi)={PHI**(1-1/PHI):.4f}")
