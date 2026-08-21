#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_phc(BG,Q,V): return BG*PHI, Q*PHI**2, V/PHI
def purcell(F): return F*PHI**2
if __name__=="__main__":
    BG=100.0; Q=1000.0; V=1.0; F=10.0
    bgp,qp,vp=phi_phc(BG,Q,V); fp=purcell(F)
    print(f"Bandgap: {BG:.1f} -> {bgp:.1f} (x{bgp/BG:.4f})")
    print(f"Q-factor: {Q:.1f} -> {qp:.1f} (x{qp/Q:.4f})")
    print(f"Mode volume: {V:.2f} -> {vp:.4f} (x{vp/V:.4f})")
    print(f"Purcell: {F:.1f} -> {fp:.1f} (x{fp/F:.4f})")
