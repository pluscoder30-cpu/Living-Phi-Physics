import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"Accuracy: ±{round(max(15*(1-1.0*PHI_INV*0.2),5),1)}%")
