#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_time(T,f,N): return T*PHI**(-f/N)
if __name__=="__main__":
    for f,N in [(5,20),(10,30),(15,50),(20,100)]:
        print(f"f={f:2d} N={N:3d} f/N={f/N:.3f} T_phi={phi_time(1,f,N):.4f}")
    print(f"Byzantine threshold: f=N/phi^2={1/PHI**2:.4f}N")
