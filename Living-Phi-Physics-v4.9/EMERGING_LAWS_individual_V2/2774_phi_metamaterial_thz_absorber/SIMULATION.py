#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_abs(A,BW,theta,P): return A*PHI, BW*PHI**2, theta*PHI, P*PHI
if __name__=="__main__":
    A=0.80; BW=1.0; theta=30.0; P=0.90
    Ap,BWp,thetap,Pp=phi_abs(A,BW,theta,P)
    print(f"Absorptance: {A:.4f} -> {Ap:.4f}")
    print(f"Bandwidth: {BW:.2f} -> {BWp:.4f} THz")
    print(f"Angular tolerance: {theta:.1f} -> {thetap:.2f} deg")
    print(f"Polarization: {P:.4f} -> {Pp:.4f}")
    print(f"Absorptance gain: phi={PHI:.4f}")
