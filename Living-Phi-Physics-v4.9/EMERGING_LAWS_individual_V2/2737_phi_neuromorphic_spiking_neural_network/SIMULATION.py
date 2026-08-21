#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_snn(dt,I,E,C):
    return dt/PHI, I*PHI**2, E/PHI, C*PHI**(1-1/PHI)
if __name__=="__main__":
    for dt in [1.0,5.0,10.0,50.0]:
        dtp,Ip,Ep,Cp=phi_snn(dt,1e6,1e-12,1e9)
        print(f"dt={dt:.1f}ms dt_phi={dtp:.4f}ms I_phi={Ip:.2e} E_phi={Ep:.2e}")
    print(f"Energy reduction: 1/phi={1/PHI:.4f}")
    print(f"Information gain: phi^2={PHI**2:.4f}")
