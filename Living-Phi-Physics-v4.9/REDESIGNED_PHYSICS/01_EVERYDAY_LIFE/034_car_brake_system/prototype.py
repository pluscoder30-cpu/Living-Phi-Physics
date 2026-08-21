import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"Mu: {round(0.42*(1+1.0*(PHI-1)*0.1)+1.0*PHI_INV*0.02,3)}, Vent: {round(1.0*(1+1.0*(PHI-1)),2)}x")
