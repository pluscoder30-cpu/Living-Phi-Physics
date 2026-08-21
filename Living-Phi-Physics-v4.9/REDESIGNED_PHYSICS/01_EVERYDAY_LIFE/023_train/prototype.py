import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_stress(c=800, kappa=0.8):
    return round(c*(1-kappa*(PHI-1)*0.12))
print(f"Stress: {phi_stress(800,1.0)} MPa, Efficiency: {round(0.75*(1+1.0*(PHI-1)*0.08)*100,1)}%")
