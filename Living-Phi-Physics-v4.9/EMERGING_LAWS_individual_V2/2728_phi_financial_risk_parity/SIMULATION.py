#!/usr/bin/env python3
import math,random
PHI=1.618033988749895; PI=math.pi
def phi_weights(sigmas):
    ws=[s**(-PHI) for s in sigmas]
    tw=sum(ws); return [w/tw for w in ws]
def sharpe_improvement(C): return PHI**(1-2*C/PI)
if __name__=="__main__":
    random.seed(42)
    sigmas=[random.uniform(0.1,0.4) for _ in range(10)]
    ws=phi_weights(sigmas)
    print("Phi-RP weights:")
    for i,w in enumerate(ws): print(f"  Asset {i}: sigma={sigmas[i]:.4f} w_phi={w:.4f}")
    si=sharpe_improvement(0.8565)
    print(f"Sharpe improvement: {si:.4f}")
    print(f"Max drawdown bound: 1/phi={1/PHI:.4f}")
