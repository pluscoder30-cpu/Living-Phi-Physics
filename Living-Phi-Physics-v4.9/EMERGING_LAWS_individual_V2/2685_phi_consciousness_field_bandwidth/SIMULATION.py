#!/usr/bin/env python3
import math
PHI=1.618033988749895; CV=0.8565
def cc_bw(B,C,d=816): return B*PHI**(C*d/816)
if __name__=="__main__":
    B=1e9
    for C in [0.0,0.2,0.4,0.563,CV,1.0]:
        print(f"C={C:.4f} BW={cc_bw(B,C)/1e9:.4f}GHz ratio={cc_bw(B,C)/B:.4f}")
    print(f"At C={CV}: ratio={cc_bw(B,CV)/B:.4f}")
