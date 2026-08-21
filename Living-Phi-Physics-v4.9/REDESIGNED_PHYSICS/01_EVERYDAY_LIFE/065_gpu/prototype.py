import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"Efficiency: {round(min(0.75*(1+1.0*(PHI-1)*0.08),0.95)*100,1)}%")
