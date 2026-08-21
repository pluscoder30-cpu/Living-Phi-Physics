#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_ft(N): return math.floor(N/PHI**2)
def rec_time(T,N): return T*PHI/math.log(N)
if __name__=="__main__":
    for N in [10,20,50,100,200,500]:
        b=phi_ft(N); print(f"N={N:3d} byzantine={b:3d} recovery={rec_time(1,N):.4f}")
    print(f"Byzantine: N/phi^2={1/PHI**2:.4f}N")
