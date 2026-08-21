#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_act(x): return math.tanh(x/PHI)+x/PHI
def phi_grad(x): return (1/math.cosh(x/PHI))**2/PHI+1/PHI
if __name__=="__main__":
    for x in [-5.0,-2.0,-1.0,0.0,1.0,2.0,5.0]:
        print(f"x={x:5.1f} sigma={phi_act(x):.4f} grad={phi_grad(x):.4f}")
    print(f"Grad at origin: {phi_grad(0):.4f}")
