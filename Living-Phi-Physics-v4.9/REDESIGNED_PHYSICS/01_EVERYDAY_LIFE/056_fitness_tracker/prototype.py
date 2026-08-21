import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"HR error: ±{max(round(5*(1-1.0*(PHI-1)*0.25),1),0.5)} bpm")
