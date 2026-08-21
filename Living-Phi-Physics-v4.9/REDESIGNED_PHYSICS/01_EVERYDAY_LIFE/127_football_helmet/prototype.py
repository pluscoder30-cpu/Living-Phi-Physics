import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"Absorption: {round(min(0.75*(1+1.0*(PHI-1)*0.1),0.95),2)}")
