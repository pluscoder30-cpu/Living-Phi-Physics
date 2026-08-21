import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_battery(c=12, kappa=0.8):
    return round(c*(1+kappa*(PHI-1))+kappa*PHI_INV*2, 1)
def phi_rf(c=0.35, kappa=0.8):
    return round(c*(1+kappa*(PHI-1)*0.2), 2)
print(f"Battery: 12 -> {phi_battery(12,1.0)} h, RF: {phi_rf(0.35,1.0)*100:.0f}%")
