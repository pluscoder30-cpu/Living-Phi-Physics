import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"Torque: {round(0.3*(1+1.0*PHI_INV*0.05),3)} Nm, Life: {int(50000*(1+1.0*(PHI-1)*0.1))/1000:.0f}K")
