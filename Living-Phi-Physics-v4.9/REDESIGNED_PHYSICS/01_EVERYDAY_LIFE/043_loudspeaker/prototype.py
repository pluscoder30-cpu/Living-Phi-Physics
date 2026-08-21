import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_resp(freqs, kappa=0.8):
    return [round(min(max(1/(1+(f/1000)**2)*(1+kappa*(PHI-1)*(1-abs(math.log10(f/1000))*0.3)),0.3),1.0),3) for f in freqs]
print(f"Response: {phi_resp([100,500,1000,5000,10000])}")
