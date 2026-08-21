import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_oven_element_spacing(width=60, n=6):
    sp = width/(n-1)
    return [0.0]+[round(min(sp*i*(1+PHI_INV*i/n), width), 1) for i in range(1, n)]
def phi_thermal_uniformity(c=0.70, kappa=0.8):
    return min(c*(1+kappa*(PHI-1))+kappa*PHI_INV*0.5, 0.99)
print(f"Positions: {phi_oven_element_spacing()}")
print(f"Uniformity: 70% -> {phi_thermal_uniformity(0.70, 1.0)*100:.1f}%")
