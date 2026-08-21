import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"Dose: {round(max(10*(1-1.0*(PHI-1)*0.15),5),1)} mGy")
