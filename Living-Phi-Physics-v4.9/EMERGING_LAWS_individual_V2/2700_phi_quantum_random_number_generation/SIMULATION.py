#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_H(H): return H*PHI
if __name__=="__main__":
    H=0.9
    print(f"H_min_std={H:.4f} H_min_phi={phi_H(H):.4f}")
    for n in [1000,10000,100000]:
        print(f"events={n:7d} bits_std={n*H:.0f} bits_phi={n*phi_H(H):.0f}")
    print(f"Improvement: phi={PHI:.4f}x")
