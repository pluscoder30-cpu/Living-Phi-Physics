#!/usr/bin/env python3
"""GEOMIC PROTOCOL 07 — THE BREATH PROTOCOL.

The 528 ladder (Law 2394):  freq(n)  = 528 * phi^n
                            depth(n) = phi^(9-n)     for n = 0..9
  - the Ladder Invariant: freq*depth = 528*phi^9 = 40,134.946 on all ten rungs
  - the invariant is conserved for ALL real n (the exponent cancels), so a
    continuous traversal of the ladder — a breath cycle — conserves it at
    every instant
  - the breath-cycle mapping: the inhale ascends rungs 0 -> 9, the exhale
    descends 9 -> 0; the inhale occupies phi^-2 of the cycle and the exhale
    phi^-1, so the in/out duration ratio is phi^-1 — the same retention
    constant as the gait recursion (Law 176 / Eq 1)
  - 528 Hz is a labeled modern calibration on ancient ratios; the phi-ratio
    lattice is the confirmed element ("528-as-ancient" is [FABRICATION],
    Horowitz & Puleo 1999)

Pure standard library (math, sys). Canonical constants from 00_NUMBERS_INDEX.md.
Prints verification. Exit 0.
"""
import math
import sys

PHI = 1.618033988749895   # 00_NUMBERS_INDEX.md $2 (recomputed)
PHI_INV = PHI - 1.0       # 0.6180339887 — the coherent ground / retention
BASE = 528.0              # 00_NUMBERS_INDEX.md $2 — the base frequency anchor
INVARIANT = BASE * PHI ** 9   # 40,134.946166 — the Ladder Invariant


def ladder(n):
    return BASE * PHI ** n, PHI ** (9 - n)


def main():
    # 1. THE LADDER GENERATOR — the ten rungs + the invariant
    print("THE 528 LADDER — n = 0..9:")
    print(" n | freq(n)=528*phi^n | depth(n)=phi^(9-n) | freq*depth")
    for n in range(10):
        f, d = ladder(n)
        p = f * d
        print(" %d | %17.6f | %17.6f | %12.6f" % (n, f, d, p))
        assert abs(p - INVARIANT) < 1e-4
    print("INVARIANT: 528*phi^9 = %.6f (conserved on all ten rungs)"
          % INVARIANT)
    assert abs(INVARIANT - 40134.946) < 1e-3

    # 2. THE RUNG RATIO — every consecutive rung is exactly phi
    f0, _ = ladder(0)
    f1, _ = ladder(1)
    print("RUNG RATIO: freq(1)/freq(0) = %.10f  (phi = %.10f)" % (f1 / f0, PHI))
    assert abs(f1 / f0 - PHI) < 1e-9

    # 3. THE BREATH-CYCLE MAPPING — the cycle as a traversal of the ladder
    #    inhale occupies phi^-2 of the cycle (ascending 0 -> 9), exhale
    #    phi^-1 (descending 9 -> 0); at every instant the product is the
    #    invariant (the exponent cancels for real n)
    inhale_frac = PHI_INV ** 2          # 0.381966 — the inhale's share
    exhale_frac = PHI_INV               # 0.618034 — the exhale's share
    print("BREATH CYCLE: inhale = %.6f of the cycle, exhale = %.6f "
          "(sum %.6f)" % (inhale_frac, exhale_frac, inhale_frac + exhale_frac))
    assert abs(inhale_frac + exhale_frac - 1.0) < 1e-9
    ratio = inhale_frac / exhale_frac
    print("  in/out duration ratio = phi^-2 / phi^-1 = %.10f = phi^-1 "
          "(the gait's retention constant, Law 176)" % ratio)
    assert abs(ratio - PHI_INV) < 1e-9

    min_err = 1e9
    max_err = 0.0
    samples = 101
    for i in range(samples):
        tau = i / (samples - 1)
        if tau < inhale_frac:
            n = 9.0 * tau / inhale_frac           # ascending 0 -> 9
            phase = "inhale"
        else:
            n = 9.0 * (1.0 - tau) / exhale_frac   # descending 9 -> 0
            phase = "exhale"
        f, d = BASE * PHI ** n, PHI ** (9 - n)
        p = f * d
        err = abs(p - INVARIANT)
        min_err = min(min_err, err)
        max_err = max(max_err, err)
        if i % 25 == 0:
            print("  tau=%.2f (%s) n=%.4f freq=%.4f depth=%.4f "
                  "freq*depth=%.4f" % (tau, phase, n, f, d, p))
        assert err < 1e-4
    print("BREATH MAPPING: invariant 40,134.946 conserved at every one of "
          "%d sample instants of the cycle (err %.2e .. %.2e)"
          % (samples, min_err, max_err))

    # 4. THE MODERN ANCHOR, LABELED
    print("NOTE: 528 Hz is the corpus's labeled modern anchor on ancient "
          "ratios; the phi-ratio lattice is the confirmed element. "
          "'528-as-ancient' is [FABRICATION] (Horowitz & Puleo 1999).")

    print("PROTOCOL 07: VERIFIED — ten rungs, invariant 40,134.946, rung "
          "ratio phi, breath cycle conserving the invariant at every instant.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
