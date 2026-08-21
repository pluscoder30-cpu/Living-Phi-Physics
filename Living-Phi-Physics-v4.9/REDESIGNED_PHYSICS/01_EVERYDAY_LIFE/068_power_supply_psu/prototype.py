import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"PSU: {round(min(0.90*(1+1.0*(PHI-1)*0.02)+1.0*PHI_INV*0.005,0.98)*100,1)}%")
