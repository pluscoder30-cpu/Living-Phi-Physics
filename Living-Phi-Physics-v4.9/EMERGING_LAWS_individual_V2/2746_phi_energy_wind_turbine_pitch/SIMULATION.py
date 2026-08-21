#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_pitch(T,Cp,F): return T/PHI, Cp*PHI**(1-1/PHI), F/PHI
if __name__=="__main__":
    T=500.0; Cp=0.48; F=100.0
    Tp,Cpp,Fp=phi_pitch(T,Cp,F)
    print(f"Response: {T:.0f}ms -> {Tp:.2f}ms (x{T/Tp:.4f})")
    print(f"Cp: {Cp:.4f} -> {Cpp:.4f}")
    print(f"Fatigue: {F:.1f} -> {Fp:.2f}")
    print(f"Fatigue reduction: 1/phi={1/PHI:.4f}")
