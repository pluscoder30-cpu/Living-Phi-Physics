import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_stiffness(c=1.0, kappa=0.8):
    return c*(1+kappa*(PHI-1))+kappa*PHI_INV*c*0.1
print(f"Stiffness: {phi_stiffness(1.0,1.0):.2f}x")
