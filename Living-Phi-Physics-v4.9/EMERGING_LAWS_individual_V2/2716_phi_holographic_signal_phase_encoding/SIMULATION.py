#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_rho(r): return r*PHI**2
if __name__=="__main__":
    r=1e6
    print(f"Standard: {r:.2e} bits/mm3")
    print(f"Phi: {phi_rho(r):.2e} bits/mm3")
    print(f"Improvement: {phi_rho(r)/r:.4f}x = phi^2")
