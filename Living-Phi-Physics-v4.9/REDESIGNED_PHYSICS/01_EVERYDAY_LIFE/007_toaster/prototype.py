import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_toaster_profile(n=4, pw=1000):
    return [round(pw*math.exp(-(abs(i/(n-1)-0.5))**2/(2*(PHI_INV*0.5)**2)), 0) for i in range(n)]
def phi_toaster_efficiency(c=0.12, kappa=0.8):
    return min(c*(1+kappa*(PHI-1))+kappa*PHI_INV*0.05, 0.35)
print(f"Powers: {phi_toaster_profile()}")
print(f"Efficiency: 12% -> {phi_toaster_efficiency(0.12,1.0)*100:.1f}%")
