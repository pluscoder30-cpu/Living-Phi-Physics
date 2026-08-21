#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_smooth(kappa_max,jerk_std):
    kp=kappa_max/PHI; jp=jerk_std/PHI**2; ep=1.0/PHI
    return kp,jp,ep
if __name__=="__main__":
    k=0.5; j=10.0
    kp,jp,ep=phi_smooth(k,j)
    print(f"kappa_std={k:.4f} kappa_phi={kp:.4f} ratio={kp/k:.4f}")
    print(f"jerk_std={j:.4f} jerk_phi={jp:.4f} reduction={j/jp:.4f}x")
    print(f"goal_dev_std=1.0 goal_phi={ep:.4f} ratio={ep:.4f}")
    print(f"Jerk reduction target: phi^2={PHI**2:.4f}")
