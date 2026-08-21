#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_snap(O): return O/PHI
if __name__=="__main__":
    O=1.0; Op=phi_snap(O)
    for n in [100,500,1000,5000]:
        ts=O*n; tp=Op*n; print(f"txns={n:5d} T_std={ts:8.0f} T_phi={tp:8.0f} savings={(ts-tp)/ts*100:.1f}%")
    print(f"Overhead reduction: 1/phi={1/PHI:.4f}")
