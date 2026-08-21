#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_cons(N): return math.floor(N/PHI**2),(N-1)//3
if __name__=="__main__":
    for N in [7,10,15,21,50,100]:
        fp,fb=phi_cons(N); print(f"N={N:3d} f_phi={fp:2d} f_pbft={fb:2d} ratio={fp/fb:.3f}")
    print(f"Tolerance: N/phi^2={1/PHI**2:.4f}N")
