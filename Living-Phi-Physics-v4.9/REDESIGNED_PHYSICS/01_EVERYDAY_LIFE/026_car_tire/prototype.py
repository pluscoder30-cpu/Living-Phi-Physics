import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_rr(c=0.008, kappa=0.8):
    return round(c*(1-kappa*(PHI-1)*0.15), 4)
print(f"RR: 0.008 -> {phi_rr(0.008,1.0)}")
