import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"IPC: {round(1.0*(1+1.0*(PHI-1))+1.0*PHI_INV*0.1,3)}, Thermal: {round(125*(1-1.0*PHI_INV*0.1),1)} W")
