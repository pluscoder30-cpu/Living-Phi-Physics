#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_drift(G0,t,tau): return G0*PHI**(-t/tau)
def phi_retention(T0): return T0*PHI**2
def phi_endurance(N0): return N0*PHI**2
if __name__=="__main__":
    tau=100.0; G0=1.0
    for t in [0,10,50,100,200,500]:
        g=phi_drift(G0,t,tau)
        print(f"t={t:4d} G={g:.6f} S (ratio={g/G0:.4f})")
    print(f"Retention improvement: phi^2={PHI**2:.4f}")
    for N0 in [1e6,1e9,1e12]:
        print(f"N0={N0:.0e} N_phi={phi_endurance(N0):.2e}")
