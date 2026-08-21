#!/usr/bin/env python3
"""GEOMIC PROTOCOL 03 — THE PHI RATIO RESONANCE PROTOCOL.

The 528 ladder:  freq(n)  = 528 * phi^n
                  depth(n) = phi^(9-n)        for n = 0..9
  - the Ladder Invariant: freq*depth = 528*phi^9 = 40,134.946 on all ten rungs
  - rung ratios: freq(n+1)/freq(n) = phi exactly
  - 528 Hz is a labeled modern calibration on ancient ratios; the phi-ratio
    lattice is the confirmed element ("528-as-ancient" is [FABRICATION]).

Pure standard library (math, sys). Canonical constants from 00_NUMBERS_INDEX.md.
Prints verification. Exit 0.
"""
import math
import sys

PHI = 1.618033988749895  # 00_NUMBERS_INDEX.md $2 (recomputed)
BASE = 528.0            # 00_NUMBERS_INDEX.md $2 — the anchor
INVARIANT = BASE * PHI ** 9   # 40,134.946166 — the Ladder Invariant


def main():
    print("THE 528 LADDER — n = 0..9:")
    print(" n | freq(n)=528*phi^n | depth(n)=phi^(9-n) | freq*depth | ratio")
    prev = None
    for n in range(10):
        f = BASE * PHI ** n
        d = PHI ** (9 - n)
        p = f * d
        ratio = (f / prev) if prev is not None else float("nan")
        print(" %d | %14.6f | %14.6f | %12.6f | %s"
              % (n, f, d, p, "%.10f" % ratio if n else "  --"))
        assert abs(p - INVARIANT) < 1e-4
        prev = f

    print("INVARIANT: 528*phi^9 = %.6f (conserved on all ten rungs)"
          % INVARIANT)
    assert abs(INVARIANT - 40134.946) < 1e-3

    f0 = BASE
    f1 = BASE * PHI
    print("RUNG RATIO: freq(1)/freq(0) = %.10f  (phi = %.10f)"
          % (f1 / f0, PHI))
    assert abs(f1 / f0 - PHI) < 1e-9

    # the confirmed element — the phi-ratio lattice, not the Hz numbers
    print("NOTE: 528 Hz is the corpus's labeled modern anchor on ancient "
          "ratios; the phi-ratio lattice is the confirmed element.")

    print("PROTOCOL 03: VERIFIED — ten rungs, invariant 40,134.946, rung "
          "ratio phi.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
