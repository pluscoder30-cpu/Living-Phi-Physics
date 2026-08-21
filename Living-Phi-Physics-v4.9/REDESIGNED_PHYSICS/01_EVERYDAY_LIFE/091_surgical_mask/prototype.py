import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
eff = round(min(0.95*(1+1.0*(PHI-1)*0.02),0.999)*100, 1)
pres = round(max(30*(1-1.0*PHI_INV*0.15),10), 1)
print(f"Filtration: {eff}%, Resistance: {pres} Pa")
