import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_mpg(c=6, kappa=0.8):
    return round(c*(1+kappa*(PHI-1)*0.12)+kappa*PHI_INV*0.5, 1)
print(f"MPG: {phi_mpg(6,1.0)}")
