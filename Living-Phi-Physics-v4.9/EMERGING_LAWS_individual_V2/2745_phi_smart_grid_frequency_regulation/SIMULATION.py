#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_freq(df,T,G): return df/PHI, T/PHI, G*PHI
if __name__=="__main__":
    df=0.5; T=200.0; G=5.0
    dfp,Tp,Gp=phi_freq(df,T,G)
    print(f"Freq deviation: {df:.2f}Hz -> {dfp:.4f}Hz")
    print(f"Response time: {T:.0f}ms -> {Tp:.2f}ms")
    print(f"Droop gain: {G:.2f} -> {Gp:.4f}")
    print(f"Deviation reduction: 1/phi={1/PHI:.4f}")
