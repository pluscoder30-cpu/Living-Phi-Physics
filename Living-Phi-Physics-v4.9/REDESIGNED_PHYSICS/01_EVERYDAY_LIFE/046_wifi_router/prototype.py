import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_range(c=50, kappa=0.8):
    return round(c*(1+kappa*(PHI-1))+kappa*PHI_INV*10, 1)
print(f"Range: {phi_range(50,1.0)} m")
