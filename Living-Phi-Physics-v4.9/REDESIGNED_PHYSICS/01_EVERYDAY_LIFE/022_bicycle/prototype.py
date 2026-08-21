import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_dt(c=0.96, kappa=0.8):
    return min(c*(1+kappa*(PHI-1)*0.02)+kappa*PHI_INV*0.005, 0.995)
print(f"Drivetrain: 96% -> {phi_dt(0.96,1.0)*100:.1f}%")
