#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_res(N): return 1.0/(N/PHI)
def std_res(N): return 1.0/N
if __name__=="__main__":
    for N in [64,128,256,512]:
        print(f"N={N:4d} phi_res={phi_res(N):.6f} std_res={std_res(N):.6f} ratio={phi_res(N)/std_res(N):.4f}")
    print(f"Low-freq improvement: {PHI:.4f}x")
