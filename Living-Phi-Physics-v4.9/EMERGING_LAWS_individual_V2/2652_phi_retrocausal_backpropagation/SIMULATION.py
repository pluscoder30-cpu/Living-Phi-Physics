#!/usr/bin/env python3
import math
PHI=1.618033988749895; TAU=PHI**5; OMEGA=PHI**3
def retro_g(g,dt,wb=1.0): return g*math.exp(-dt/TAU)*math.cos(OMEGA*wb*dt)
if __name__=="__main__":
    print(f"tau_retro={TAU:.4f} omega_retro={OMEGA:.4f}")
    for dt in [0.1,0.5,1.0,2.0,5.0,10.0]:
        print(f"dt={dt:5.1f} grad={retro_g(1.0,dt):.6f}")
