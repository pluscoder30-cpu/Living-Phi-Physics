import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_range(c=20, kappa=0.8):
    return round(c*(1+kappa*(PHI-1))+kappa*PHI_INV*3, 1)
print(f"Range: {phi_range(20,1.0)} km, Turning: {round(1.5*(1-1.0*PHI_INV*0.12),2)} m")
