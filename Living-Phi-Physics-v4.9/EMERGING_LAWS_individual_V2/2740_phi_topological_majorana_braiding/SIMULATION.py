#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_majorana(F,T,E,D):
    return F*PHI, T/PHI, E/PHI**2, D*PHI
if __name__=="__main__":
    F=0.999; T=100.0; E=1e-6; D=0.1
    Fp,Tp,Ep,Dp=phi_majorana(F,T,E,D)
    print(f"Fidelity: {F:.6f} -> {Fp:.6f}")
    print(f"Gate time: {T:.1f} -> {Tp:.2f}ns")
    print(f"Error rate: {E:.2e} -> {Ep:.2e}")
    print(f"Topological gap: {D:.4f} -> {Dp:.4f}")
    print(f"Error reduction: phi^2={PHI**2:.4f}")
