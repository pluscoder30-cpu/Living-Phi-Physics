import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI; C_CRIT = 0.563263
def phi_smoke_alarm(density, size, kappa=0.8):
    C = density*math.exp(-((size-0.5)**2)/0.5)*PHI_INV
    return C > C_CRIT*(1+kappa*(PHI-1)*0.05), round(min(C,1.0), 4)
for n,d,s in [("Smoke",0.8,0.3),("Steam",0.8,5.0),("Fire",1.0,0.2)]:
    a,C = phi_smoke_alarm(d,s,1.0); print(f"  {n}: C={C} Alarm={a}")
