import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"Read: {round(37.0*(1+1.0*(PHI-1)*0.005)+1.0*PHI_INV*0.1,2)} C, Accuracy: ±{round(max(0.1*(1-1.0*PHI_INV*0.3),0.02),3)} C")
