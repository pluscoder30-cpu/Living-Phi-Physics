import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_cd(c=0.30, kappa=0.8):
    return max(c*(1-kappa*(PHI-1)*0.15), c*0.5)
def phi_mpg(c=30, kappa=0.8):
    return round((c/phi_cd(0.30,kappa)*0.30)*(1+kappa*(PHI-1)*0.1), 1)
print(f"CD: 0.30 -> {phi_cd(0.30,1.0):.3f}, MPG: {phi_mpg(30,1.0)}")
