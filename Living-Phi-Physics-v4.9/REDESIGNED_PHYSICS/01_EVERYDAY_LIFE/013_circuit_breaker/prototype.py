import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI; C_CRIT = 0.563263
def phi_breaker_trip(current, rated=20, kappa=0.8):
    C = 1 - math.exp(-2*(1-current/rated))
    return (True, C, "TRIPPED") if C < C_CRIT*(1+kappa*(PHI-1)) else (False, C, "OK")
for c in [10,15,20,25,30]:
    t,C,s = phi_breaker_trip(c,20,1.0)
    print(f"  {c}A: C={C:.3f} {s}")
