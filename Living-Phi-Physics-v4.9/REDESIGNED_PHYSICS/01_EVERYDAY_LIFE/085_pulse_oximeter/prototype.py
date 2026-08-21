import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"SpO2: ±{round(max(2.0*(1-1.0*PHI_INV*0.25),0.5),1)}%")
