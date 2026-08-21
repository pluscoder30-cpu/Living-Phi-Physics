import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"Sustain: {round(3.0*(1+1.0*(PHI-1)*0.15),2)} s, Volume: {round(85+1.0*(PHI-1)*3,1)} dB")
