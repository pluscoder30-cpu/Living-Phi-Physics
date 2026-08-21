#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_tele(F,e): return F*PHI**(1-e)
if __name__=="__main__":
    F=0.95
    for e in [0.01,0.05,0.1,0.2,0.3,0.5]:
        print(f"err={e:.2f} F_phi={phi_tele(F,e):.4f} ratio={phi_tele(F,e)/F:.4f}")
    print(f"phi^0.9={PHI**0.9:.4f}")
