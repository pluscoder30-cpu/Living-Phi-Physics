import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"Reflectivity: {round(min(0.90*(1+1.0*PHI_INV*0.05),0.99)*100,1)}%")
