#!/usr/bin/env python3
import math
PHI=1.618033988749895
def conv(mu,iters):
    e=[1.0]
    for _ in range(iters): e.append(e[-1]*(1-mu))
    return e
if __name__=="__main__":
    mu=0.01; iters=200
    es=conv(mu,iters); ep=conv(mu*PHI,iters)
    for m in [10,25,50,100]:
        print(f"iter={m:3d} err_std={es[m]:.6f} err_phi={ep[m]:.6f}")
    print(f"Convergence speedup: {PHI:.4f}x")
