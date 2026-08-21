#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_stdp(eta,tau,M,C): return eta*PHI, tau*PHI, M*PHI**2, C*PHI**(1/PHI)
if __name__=="__main__":
    eta=0.01; tau=20.0; M=1.0; C=100.0
    etap,taup,Mp,Cp=phi_stdp(eta,tau,M,C)
    print(f"Learning rate: {eta:.4f} -> {etap:.4f}")
    print(f"Plasticity window: {tau:.1f} -> {taup:.2f}ms")
    print(f"Metaplasticity: {M:.2f} -> {Mp:.4f}")
    print(f"Capacity: {C:.1f} -> {Cp:.2f}")
    print(f"Metaplasticity: phi^2={PHI**2:.4f}")
