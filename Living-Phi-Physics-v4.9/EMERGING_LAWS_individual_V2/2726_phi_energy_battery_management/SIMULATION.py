#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_charge(Cmax,soc): return Cmax*PHI**(-soc/PHI)
def degrade_phi(cycles): return 1.0/(1+cycles/1000/PHI**2)
def degrade_std(cycles): return 1.0/(1+cycles/1000)
if __name__=="__main__":
    C=2.0
    for soc in [0.0,0.2,0.4,0.5,0.6,0.8,1.0]:
        cr=phi_charge(C,soc); print(f"SoC={soc:.1f} C_phi={cr:.4f}C")
    for c in [100,500,1000,2000]:
        ds=degrade_std(c); dp=degrade_phi(c)
        print(f"cycles={c:5d} cap_std={ds:.4f} cap_phi={dp:.4f} imp={dp/ds:.4f}")
    print(f"Degradation reduction target: phi^2={PHI**2:.4f}")
