import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_battery_ed(c=200, kappa=0.8):
    return c*(1+kappa*(PHI-1))*(1+kappa*PHI_INV*0.12)
def phi_sei_life(c=1000, kappa=0.8):
    return int(c * PHI**(kappa*3))
print(f"ED: 200 -> {phi_battery_ed(200,1.0):.0f} Wh/kg")
print(f"Cycles: 1000 -> {phi_sei_life(1000,1.0)}")
