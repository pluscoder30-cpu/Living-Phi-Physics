import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_heater_layout(w=50, n=5):
    return [round(w*i/(n-1)*(1+PHI_INV*0.1*math.sin(2*math.pi*i/n)), 1) for i in range(n)]
def phi_comfort(c=0.65, kappa=0.8):
    return min(c*(1+kappa*(PHI-1))+kappa*PHI_INV*0.15, 0.99)
print(f"Layout: {phi_heater_layout()}")
print(f"Comfort: 65% -> {phi_comfort(0.65,1.0)*100:.0f}%")
