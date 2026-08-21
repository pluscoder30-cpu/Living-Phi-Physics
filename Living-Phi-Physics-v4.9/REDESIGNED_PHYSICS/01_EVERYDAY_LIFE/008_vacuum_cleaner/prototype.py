import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_nozzle_profile(d=3.5):
    return [round(d*(1+i/9*PHI_INV*0.4), 2) for i in range(10)]
def phi_suction_efficiency(c=0.18, kappa=0.8):
    return min(c*(1+kappa*(PHI-1))+kappa*PHI_INV*0.05, 0.50)
print(f"Nozzle: {phi_nozzle_profile()}")
print(f"Efficiency: 18% -> {phi_suction_efficiency(0.18,1.0)*100:.1f}%")
