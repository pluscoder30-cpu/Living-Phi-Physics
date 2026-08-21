#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_impedance(Z,BW,e): return Z*PHI**(-1/PHI), BW*PHI, e/PHI
if __name__=="__main__":
    Z=100.0; BW=100.0; e=0.5
    Zp,BWp,ep=phi_impedance(Z,BW,e)
    print(f"Impedance: {Z:.1f} -> {Zp:.2f} N/m")
    print(f"Bandwidth: {BW:.1f} -> {BWp:.2f} Hz")
    print(f"Force error: {e:.4f} -> {ep:.4f} N")
    print(f"Error reduction: 1/phi={1/PHI:.4f}")
