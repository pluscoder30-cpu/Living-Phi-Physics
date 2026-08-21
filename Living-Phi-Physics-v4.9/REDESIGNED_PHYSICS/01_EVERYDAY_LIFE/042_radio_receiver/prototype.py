import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_sens(c=-100, kappa=0.8):
    return round(c+kappa*(PHI-1)*8, 1)
def phi_q(c=100, kappa=0.8):
    return round(c*(1+kappa*(PHI-1)))
print(f"Sensitivity: {phi_sens(-100,1.0)} dBm, Q: {phi_q(100,1.0)}")
