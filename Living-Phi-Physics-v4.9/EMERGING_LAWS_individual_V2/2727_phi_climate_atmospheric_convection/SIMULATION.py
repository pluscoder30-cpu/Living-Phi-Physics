#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_hadley(W,dT): return W*PHI**(dT/PHI)
def feedback_amp(dT): return min(PHI,1+dT/PHI)
if __name__=="__main__":
    W=3000.0
    for dT in [0.0,1.0,1.5,2.0,3.0,4.0,5.0]:
        wp=phi_hadley(W,dT); fb=feedback_amp(dT)
        print(f"dT={dT:.1f}C W_phi={wp:.0f}km feedback={fb:.4f}")
    print(f"Feedback bound: phi={PHI:.4f}")
