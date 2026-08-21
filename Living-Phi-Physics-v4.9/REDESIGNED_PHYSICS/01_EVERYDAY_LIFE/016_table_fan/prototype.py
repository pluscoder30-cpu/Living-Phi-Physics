import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_eff(speed):
    return min((0.15+0.25*speed)*(1+0.8*(PHI-1))+0.8*PHI_INV*0.05, 0.55)
for s in [0.25,0.5,0.75,1.0]:
    print(f"  {s*100:.0f}%: {phi_eff(s)*100:.0f}%")
