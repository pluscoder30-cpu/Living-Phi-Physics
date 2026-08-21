import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_rw(c=1.0, kappa=0.8):
    return round(c*(1-kappa*(PHI-1)*0.18), 3)
print(f"Resistance: {phi_rw(1.0,1.0)}, Eff: {min(0.40/phi_rw(1.0,1.0),0.65)*100:.1f}%")
