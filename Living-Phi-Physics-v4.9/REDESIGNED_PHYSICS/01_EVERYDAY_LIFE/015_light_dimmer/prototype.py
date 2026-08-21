import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI; C_CRIT = 0.563263
def phi_dimmer(dial, kappa=0.8):
    C = dial
    return 0.0 if C < C_CRIT*kappa else min((C/C_CRIT)**PHI, 1.0)
for d in [0.0,0.2,0.4,0.6,0.8,1.0]:
    print(f"  {d:.1f}: {phi_dimmer(d,1.0)*100:.0f}%")
