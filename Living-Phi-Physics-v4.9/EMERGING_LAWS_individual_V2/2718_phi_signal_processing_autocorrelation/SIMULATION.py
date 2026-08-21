#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_zc(N): return int(N*PHI)
def td_res(fs):
    s=1.0/fs; return s, s/PHI
if __name__=="__main__":
    N=1000; fs=10000
    zc_s=N//2; zc_p=phi_zc(N)
    std_r,phi_r=td_res(fs)
    print(f"Zero crossings: std={zc_s} phi={zc_p} ratio={zc_p/zc_s:.4f}")
    print(f"TD resolution: std={std_r:.6f}s phi={phi_r:.6f}s imp={std_r/phi_r:.4f}x")
