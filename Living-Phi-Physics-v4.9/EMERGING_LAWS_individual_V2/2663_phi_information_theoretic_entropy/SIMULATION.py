#!/usr/bin/env python3
import math
PHI=1.618033988749895; LP=math.log(PHI)
def H_s(p): return -sum(x*math.log(x) for x in p if x>0)
def H_p(p): return -sum(x*math.log(x)/LP for x in p if x>0)
if __name__=="__main__":
    for name,ps in [("Fair",[0.5,0.5]),("Skewed",[0.9,0.1]),("Uniform4",[0.25]*4)]:
        print(f"{name:10s}: H_std={H_s(ps):.4f} H_phi={H_p(ps):.4f} ratio={H_p(ps)/H_s(ps):.4f}")
    print(f"H_phi_max=1/log(phi)={1/LP:.4f}")
