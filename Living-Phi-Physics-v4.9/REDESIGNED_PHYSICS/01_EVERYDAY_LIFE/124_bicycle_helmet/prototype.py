import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"Impact absorption: {round(min(0.70*(1+1.0*(PHI-1)*0.12),0.95),2)}")
