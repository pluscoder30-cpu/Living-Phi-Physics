import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_nozzle_angles(n=8):
    return [round((360*i/n + 360*PHI_INV*(i%3)/n)%360, 1) for i in range(n)]
def phi_water(c=12, kappa=0.8):
    return max(c*(1-kappa*(PHI-1)*0.06), c*0.5)
print(f"Angles: {phi_nozzle_angles()}")
print(f"Water: 12L -> {phi_water(12,1.0):.1f}L")
