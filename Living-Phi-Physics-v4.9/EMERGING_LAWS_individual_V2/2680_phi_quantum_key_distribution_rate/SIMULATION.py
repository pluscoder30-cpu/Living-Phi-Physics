#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_rate(R,e): return R*PHI**(1-e)
if __name__=="__main__":
    R=1e6
    for e in [0.01,0.05,0.1,0.15,0.2]:
        print(f"QBER={e:.2f} R_phi={phi_rate(R,e):.0f} ratio={phi_rate(R,e)/R:.4f}")
    print(f"phi^0.95={PHI**0.95:.4f}")
