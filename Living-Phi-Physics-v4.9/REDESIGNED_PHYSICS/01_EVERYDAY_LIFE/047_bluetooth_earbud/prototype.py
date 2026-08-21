import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_batt(c=6, kappa=0.8):
    return round(c*(1+kappa*(PHI-1))+kappa*PHI_INV*1, 1)
print(f"Battery: {phi_batt(6,1.0)} h")
