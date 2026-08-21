import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
pat = [{"ring_s":round(2.0*PHI_INV**i,2),"pause_s":round(2.0*PHI_INV**(i+1),2)} for i in range(5)]
print(f"Pattern: {pat[:3]}")
