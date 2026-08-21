import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"Attenuation: {round(20*(1-1.0*PHI_INV*0.1),1)} dB/100m")
