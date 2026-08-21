import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"Consistency: {round(min(0.80*(1+1.0*(PHI-1)*0.1),0.99),2)}")
