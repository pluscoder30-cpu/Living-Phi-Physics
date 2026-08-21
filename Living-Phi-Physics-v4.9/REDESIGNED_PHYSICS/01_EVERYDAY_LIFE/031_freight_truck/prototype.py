import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_mpg(c=6.5, kappa=0.8):
    return round(c*(1+kappa*0.15*(PHI-1)), 1)
print(f"MPG: {phi_mpg(6.5,1.0)}")
