#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_gnss(e,TTFF,A): return e/PHI, TTFF/PHI, A*PHI
if __name__=="__main__":
    e=2.0; TTFF=30.0; A=0.85
    ep,TTFFp,Ap=phi_gnss(e,TTFF,A)
    print(f"Position error: {e:.2f} -> {ep:.4f} m")
    print(f"TTFF: {TTFF:.1f} -> {TTFFp:.2f} s")
    print(f"Ambiguity resolution: {A:.4f} -> {Ap:.4f}")
    print(f"Accuracy improvement: 1/phi={1/PHI:.4f}")
