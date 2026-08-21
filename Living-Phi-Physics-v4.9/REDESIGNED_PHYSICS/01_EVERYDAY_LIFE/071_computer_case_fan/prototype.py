import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
cfm = round(50*(1+1.0*(PHI-1)*0.1)); noise = round(25-1.0*PHI_INV*5,1)
print(f"CFM: {cfm}, Noise: {noise} dBA")
