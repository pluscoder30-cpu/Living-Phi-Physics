import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_mic(c=-40, kappa=0.8):
    return round(c+kappa*(PHI-1)*5, 1)
def phi_polar(deg, n=4):
    return round(abs(sum(math.cos(math.radians(deg)+2*math.pi*PHI*i/n) for i in range(n)))/n, 3)
print(f"Sens: {phi_mic(-40,1.0)} dBV, Pattern: {[phi_polar(a) for a in [0,90,180]]}")
