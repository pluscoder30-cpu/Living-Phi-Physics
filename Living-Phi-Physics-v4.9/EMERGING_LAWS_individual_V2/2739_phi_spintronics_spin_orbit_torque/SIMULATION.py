#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_sot(xi,alpha,I,D):
    return xi*PHI, alpha*PHI**(1/PHI), I/PHI, D*PHI
if __name__=="__main__":
    xi=0.1; alpha=0.15; I=100.0; D=40.0
    xip,ap,ip,dp=phi_sot(xi,alpha,I,D)
    print(f"SOT efficiency: {xi:.4f} -> {xip:.4f} (x{xip/xi:.4f})")
    print(f"Spin Hall angle: {alpha:.4f} -> {ap:.4f} (x{ap/alpha:.4f})")
    print(f"Switching current: {I:.1f} -> {ip:.2f} (x{ip/I:.4f})")
    print(f"Thermal stability: {D:.1f} -> {dp:.2f} (x{dp/D:.4f})")
