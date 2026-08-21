import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_standby_loss(c=0.15, kappa=0.8):
    return max(c*(1-kappa*(PHI-1)*0.3), c*0.3)
print(f"Standby: 15% -> {phi_standby_loss(0.15,1.0)*100:.1f}%")
