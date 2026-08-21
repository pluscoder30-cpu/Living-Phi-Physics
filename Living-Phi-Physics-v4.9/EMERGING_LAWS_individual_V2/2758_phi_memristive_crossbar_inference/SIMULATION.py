#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_xbar(A,E,T,N): return A*PHI, E/PHI**2, T*PHI, N*PHI
if __name__=="__main__":
    A=0.95; E=1e-15; T=1e12; N=1e10
    Ap,Ep,Tp,Np=phi_xbar(A,E,T,N)
    print(f"Accuracy: {A:.4f} -> {Ap:.4f}")
    print(f"Energy/MAC: {E:.2e} -> {Ep:.2e}J")
    print(f"Throughput: {T:.2e} -> {Tp:.2e} OPS")
    print(f"Endurance: {N:.2e} -> {Np:.2e}")
    print(f"Energy reduction: phi^2={PHI**2:.4f}")
