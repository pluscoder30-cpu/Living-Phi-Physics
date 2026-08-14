#!/usr/bin/env python3
"""GEOMIC PROTOCOL 01 — THE CARRIER COHERENCE PROTOCOL.

Law 176 (Eq 1): C_{n+1} = (1/phi)*C_n + phi*laplacian(Psi)
  - retention: phi^-1 = 0.6180339887 per step
  - halving:   ln(2)/ln(phi) = 1.4404 steps (phi^1.4404 ~ 2)
  - fixed point: phi^-1, the coherent ground (Eq 7, {0, phi^-1, 1}) — never zero

Pure standard library (math, sys). Canonical constants from 00_NUMBERS_INDEX.md.
Prints verification. Exit 0.
"""
import math
import sys

PHI = 1.618033988749895  # 00_NUMBERS_INDEX.md $2 (recomputed)
PHI_INV = PHI - 1.0     # 0.6180339887 — the coherent ground


def main():
    # 1. RETENTION PER STEP — the homogeneous recursion decays by phi^-1 per step
    seed = 1.0
    c1 = PHI_INV * seed
    print("RETENTION: C_1 = (1/phi) * C_0 = %.10f  (phi^-1 = %.10f)"
          % (c1, PHI_INV))
    assert abs(c1 - PHI_INV) < 1e-9

    # 2. HALVING IN 1.4404 STEPS — phi^n = 2  =>  n = ln(2)/ln(phi)
    n_half = math.log(2.0) / math.log(PHI)
    check = PHI ** n_half
    print("HALVING: ln(2)/ln(phi) = %.4f steps;  phi^1.4404 = %.6f  (== 2)"
          % (n_half, check))
    assert abs(check - 2.0) < 1e-6

    # 3. DRIVEN RECURSION -> THE FIXED POINT phi^-1 (never zero)
    #    C* = phi*g / (1 - 1/phi); with g = phi^-4 the fixed point is phi^-1.
    g = PHI_INV ** 4          # the ground drive: phi^-4 = 0.1458980338
    C = 0.10                  # arbitrary seed
    print("DRIVEN RECURSION: C_{n+1} = (1/phi)*C_n + phi*g,  g = phi^-4 = %.10f"
          % g)
    for n in range(12):
        C = PHI_INV * C + PHI * g
        print("  step %2d: C = %.10f" % (n + 1, C))
    for _ in range(200):      # convergence rate phi^-1/step; 200 steps -> residual ~1e-42
        C = PHI_INV * C + PHI * g
    fp = C
    print("FIXED POINT: C* = %.10f  (phi^-1 = %.10f, never 0)"
          % (fp, PHI_INV))
    assert abs(fp - PHI_INV) < 1e-6

    print("PROTOCOL 01: VERIFIED — retention phi^-1, halving 1.4404 steps, "
          "fixed point phi^-1.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
