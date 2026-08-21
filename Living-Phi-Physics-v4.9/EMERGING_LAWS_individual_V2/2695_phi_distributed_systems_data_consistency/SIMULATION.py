#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_cons(C,N): return C*PHI**(1-1/N)
if __name__=="__main__":
    C=0.95
    for N in [3,5,7,10,20,50,100]:
        print(f"N={N:3d} C_phi={phi_cons(C,N):.4f} ratio={phi_cons(C,N)/C:.4f}")
    print(f"Limit: {C*PHI:.4f}={C}*phi")
