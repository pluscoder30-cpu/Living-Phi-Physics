#!/usr/bin/env python3
import math
PHI=1.618033988749895
def g_std(t,g0=1.0,tau=10.0): return g0*math.exp(-t/tau)
def g_phi(t,g0=1.0,tau=10.0): return g0*math.exp(-t/(PHI*tau))
if __name__=="__main__":
    for d in [5,10,20,50,100,200]:
        print(f"depth={d:3d} G_std={g_std(d):.6f} G_phi={g_phi(d):.6f} ratio={g_phi(d)/g_std(d):.4f}")
    print(f"Retention at 100: {g_phi(100)/g_std(100):.4f}")
