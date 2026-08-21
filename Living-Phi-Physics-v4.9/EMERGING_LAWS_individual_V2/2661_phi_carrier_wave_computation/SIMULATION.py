#!/usr/bin/env python3
import math
PHI=1.618033988749895
def cw_fidelity(C,gates):
    pf=1+PHI**(-1)*(1-C)
    return min(1.0,0.999*gates*pf), min(1.0,0.999*gates)
if __name__=="__main__":
    C=0.8565; print(f"C={C}")
    for g in [10,50,100,500,1000]:
        fc,fg=cw_fidelity(C,g); print(f"gates={g:4d} F_gate={fg:.4f} F_cw={fc:.4f}")
    print(f"Phi factor at C=0.8565: {1+PHI**(-1)*(1-C):.4f}")
