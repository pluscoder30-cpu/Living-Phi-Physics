import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
palm = round(0.1*(1+1.0*PHI_INV*0.1), 3)
tip = round(0.1*(1-1.0*PHI_INV*0.1), 3)
print(f"Palm: {palm} mm, Fingertip: {tip} mm")
