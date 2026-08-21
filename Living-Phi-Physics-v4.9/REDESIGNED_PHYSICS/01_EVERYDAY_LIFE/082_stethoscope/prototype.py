import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"Gain: {round(10*(1+1.0*(PHI-1))+1.0*PHI_INV*2,1)} dB")
