import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_resistance(r=0.03, load=15, kappa=0.8):
    return max(r*(1-kappa*PHI_INV*load/20), r*0.15)
for load in [5,10,15]:
    print(f"  {load}A: {phi_resistance(0.03,load,1.0)*1000:.2f} mohm")
