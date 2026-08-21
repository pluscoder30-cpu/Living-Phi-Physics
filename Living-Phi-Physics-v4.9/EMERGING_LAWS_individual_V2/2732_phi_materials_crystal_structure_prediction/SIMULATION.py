#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_csp(E0,search): return E0*PHI**(-1/3), search/PHI
if __name__=="__main__":
    for N in [13,38,55,75,100,150]:
        E=-(N*1.5); es,ss=phi_csp(E,N*1000)
        print(f"N={N:4d} E_std={E:.1f} E_phi={es:.1f} search_std={N*1000:6d} search_phi={ss:.0f}")
    print(f"Search reduction: 1/phi={1/PHI:.4f}")
    print(f"Energy improvement: phi^(-1/3)={PHI**(-1/3):.4f}")
