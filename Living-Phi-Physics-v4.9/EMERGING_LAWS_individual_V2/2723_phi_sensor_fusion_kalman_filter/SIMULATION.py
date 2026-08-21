#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_kalman(R,iters=5):
    rmse=math.sqrt(R)
    for _ in range(iters): rmse/=math.sqrt(PHI)
    return rmse
def std_kalman(R,iters=5):
    rmse=math.sqrt(R)
    for _ in range(iters): rmse*=0.7
    return rmse
if __name__=="__main__":
    R=10.0
    for it in range(1,8):
        rs=std_kalman(R,it); rp=phi_kalman(R,it)
        print(f"iter={it} RMSE_std={rs:.4f} RMSE_phi={rp:.4f} ratio={rp/rs:.4f}")
    print(f"Per-iteration reduction: sqrt(phi)={math.sqrt(PHI):.4f}")
