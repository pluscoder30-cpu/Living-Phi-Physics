import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"Comfort: {round(min(0.6*(1+1.0*(PHI-1)*0.2),0.95),2)}")
