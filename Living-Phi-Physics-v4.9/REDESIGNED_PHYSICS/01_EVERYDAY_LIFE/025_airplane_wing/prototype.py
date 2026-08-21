import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_ld(c=15, kappa=0.8):
    return round(c*(1+kappa*(PHI-1))+kappa*PHI_INV*2, 1)
def phi_stall(c=16, kappa=0.8):
    return round(c+kappa*PHI_INV*4, 1)
print(f"L/D: {phi_ld(15,1.0)}, Stall: {phi_stall(16,1.0)} deg")
