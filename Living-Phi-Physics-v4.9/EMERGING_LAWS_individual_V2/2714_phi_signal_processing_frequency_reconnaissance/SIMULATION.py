#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_freq_res(T): return 1.0/(T*PHI)
def std_freq_res(T): return 1.0/T
if __name__=="__main__":
    for T in [0.1,0.5,1.0,2.0,5.0,10.0]:
        print(f"T={T:5.1f}s df_std={std_freq_res(T):.4f} df_phi={phi_freq_res(T):.4f} imp={std_freq_res(T)/phi_freq_res(T):.4f}x")
    print(f"Improvement: phi={PHI:.4f}x")
