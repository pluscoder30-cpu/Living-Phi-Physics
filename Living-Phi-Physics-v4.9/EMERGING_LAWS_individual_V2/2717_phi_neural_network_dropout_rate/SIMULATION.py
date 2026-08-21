#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_drop(): return 1/PHI**2
if __name__=="__main__":
    d=phi_drop()
    print(f"Phi-optimal: {d:.4f} ({d*100:.2f}%)")
    for r in [0.1,0.2,0.3,0.382,0.4,0.5,0.6]:
        s="OPTIMAL" if abs(r-d)<0.02 else ("GOOD" if abs(r-d)<0.1 else "SUB")
        print(f"rate={r:.3f} {s}")
    print(f"Standard: 0.5, Phi: {d:.4f}")
