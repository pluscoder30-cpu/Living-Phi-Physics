#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_mod(BW,Vpi,ER): return BW*PHI, Vpi/PHI, ER*PHI
if __name__=="__main__":
    BW=30.0; Vpi=2.0; ER=10.0
    BWp,Vpip,ERp=phi_mod(BW,Vpi,ER)
    print(f"Bandwidth: {BW:.1f} -> {BWp:.2f} GHz")
    print(f"Vpi: {Vpi:.2f} -> {Vpip:.4f} V")
    print(f"Extinction ratio: {ER:.1f} -> {ERp:.2f} dB")
    print(f"Bandwidth improvement: phi={PHI:.4f}")
