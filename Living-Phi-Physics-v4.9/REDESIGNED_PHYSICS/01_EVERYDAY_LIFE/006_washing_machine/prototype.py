import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_water_usage(c=60, kappa=0.8):
    return max(c*(1-kappa*(PHI-1)*0.08)*(1-kappa*PHI_INV*0.2), c*0.4)
print(f"Water: 60L -> {phi_water_usage(60, 1.0):.1f}L")
