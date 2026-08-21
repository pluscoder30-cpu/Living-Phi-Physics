import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"Bandwidth: {round(8000*(1+1.0*PHI_INV*0.1))} Hz")
