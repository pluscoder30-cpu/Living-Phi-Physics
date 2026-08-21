#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_crispr(E,OT,U): return E*PHI, OT/PHI**2, U*PHI
if __name__=="__main__":
    for ot in [0.01,0.05,0.1,0.2,0.3]:
        ep,otp,up=phi_crispr(0.80,ot,0.70)
        print(f"OT={ot:.2f} E_phi={ep:.4f} OT_phi={otp:.6f} U_phi={up:.4f}")
    print(f"Off-target reduction: phi^2={PHI**2:.4f}")
