import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_control(cur, sp, hist, kappa=0.8):
    if len(hist)<2: return "HOLD"
    rate = hist[-1]-hist[-2]; err = cur+rate*PHI**5*0.01*100-sp
    o = 1.0*(1+kappa*(PHI-1))*err + 0.1*kappa*PHI_INV*sum(h-sp for h in hist[-10:]) + 0.05*kappa*PHI*rate*100
    return ("HEAT",-o) if o>0 else ("COOL",-o)
print(phi_control(20, 21, [21.0,20.8,20.5,20.2,20.0], 1.0))
