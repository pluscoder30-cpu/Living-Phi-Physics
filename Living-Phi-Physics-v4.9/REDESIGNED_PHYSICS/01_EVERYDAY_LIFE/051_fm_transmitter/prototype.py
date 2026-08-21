import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"Efficiency: {round(min(0.50*(1+1.0*(PHI-1))+1.0*PHI_INV*0.05,0.85)*100)}%")
