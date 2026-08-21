#!/usr/bin/env python3
import math,random
PHI=1.618033988749895
def resilience(f): return f*PHI
if __name__=="__main__":
    for f in [0.1,0.2,0.3,0.4,0.5]:
        print(f"Fail {f:.0%}: phi_resilience={resilience(f):.4f}")
    print(f"Resilience factor: phi={PHI:.4f}")
