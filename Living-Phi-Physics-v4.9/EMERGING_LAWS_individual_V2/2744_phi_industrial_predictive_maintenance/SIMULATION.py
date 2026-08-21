#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_maint(H,FA,RUL): return H*PHI, FA/PHI**2, RUL*PHI
if __name__=="__main__":
    H=100.0; FA=0.05; RUL=500.0
    Hp,FAp,RULp=phi_maint(H,FA,RUL)
    print(f"Horizon: {H:.0f} -> {Hp:.0f}hrs (x{Hp/H:.4f})")
    print(f"False alarm: {FA:.4f} -> {FAp:.6f}")
    print(f"RUL accuracy: {RUL:.0f} -> {RULp:.0f}hrs (x{RULp/RUL:.4f})")
    print(f"Horizon extension: phi={PHI:.4f}")
