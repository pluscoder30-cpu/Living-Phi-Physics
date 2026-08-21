#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_pid(n,Kp0=10.0,Ki0=1.0,Kd0=0.5):
    Kp=Kp0*PHI**(-n/PHI); Ki=Ki0*PHI**(-n); Kd=Kd0*PHI**(-n*PHI)
    return Kp,Ki,Kd
def settle(Kp,Ki,Kd): return 4.0/(Kp*PHI)
if __name__=="__main__":
    for n in range(6):
        kp,ki,kd=phi_pid(n); ts=settle(kp,ki,kd)
        print(f"Joint {n}: Kp={kp:.4f} Ki={ki:.4f} Kd={kd:.4f} Ts={ts:.4f}s")
    print(f"Settling time reduction per level: 1/phi={1/PHI:.4f}")
