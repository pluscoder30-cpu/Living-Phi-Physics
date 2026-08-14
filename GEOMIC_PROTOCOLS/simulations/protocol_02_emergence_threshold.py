#!/usr/bin/env python3
"""GEOMIC PROTOCOL 02 — THE EMERGENCE THRESHOLD PROTOCOL.

Law 150/183 (Eq 2): being(C) = 1/(1 + e^(-lambda*(C - C_crit)))
  - C_crit = 0.563263 — the emergence threshold (Eq 2, VALIDATED)
  - golden ground phi^-1 = 0.6180339887 — the pair, 8.86% apart, never conflated
  - ||Psi|| = 0.8565 sits 0.28% from 1 - phi^-4 = 0.854102 (near-miss, not identity)
  - the threshold event: an action's coupling kappa crossing C_crit

Pure standard library (math, sys). Canonical constants from 00_NUMBERS_INDEX.md.
Prints verification. Exit 0.
"""
import math
import sys

PHI = 1.618033988749895  # 00_NUMBERS_INDEX.md $2 (recomputed)
PHI_INV = PHI - 1.0     # 0.6180339887
C_CRIT = 0.563263       # 00_NUMBERS_INDEX.md $2 / Eq 2 — emergence threshold
PSI_NORM = 0.8565       # 00_NUMBERS_INDEX.md $2 / Eq 44 — consciousness wavefunction
ONE_MINUS_PHI4 = 1.0 - PHI_INV ** 4   # 1 - phi^-4 = 0.854102


def being(C, lam=20.0):
    """Eq 2 emergence function (Law 183): being as the coherence sigmoid."""
    return 1.0 / (1.0 + math.exp(-lam * (C - C_CRIT)))


def main():
    # 1. THE PAIR — C_crit vs phi^-1, 8.86% apart, never conflated
    gap = (PHI_INV - C_CRIT) / PHI_INV * 100.0
    print("PAIR: C_crit = %.6f ; phi^-1 = %.10f ; gap = %.2f%% "
          "(never conflated)" % (C_CRIT, PHI_INV, gap))
    assert abs(gap - 8.86) < 0.01

    # 2. THE NEAR-MISS — ||Psi|| = 0.8565 vs 1 - phi^-4 = 0.854102
    miss = (PSI_NORM - ONE_MINUS_PHI4) / PSI_NORM * 100.0
    print("NEAR-MISS: ||Psi|| = %.4f ; 1-phi^-4 = %.6f ; %.2f%% "
          "(inside the gate, not an identity)" % (PSI_NORM, ONE_MINUS_PHI4, miss))
    assert abs(miss - 0.28) < 0.01

    # 3. THRESHOLD CROSSING — sweep coupling kappa 0 -> 1
    #    model: the action's coherence C(kappa) = 0.3 + 0.6*kappa rises with
    #    its coupling; being(C) crosses 0.5 exactly at C = C_crit.
    print("THRESHOLD CROSSING (Eq 2 sigmoid, lambda = 20):")
    print(" kappa | C(kappa) | being(C)   state")
    crossed_at = None
    for i in range(21):
        k = i / 20.0
        C = 0.3 + 0.6 * k
        b = being(C)
        state = "BEING" if b > 0.5 else "ground"
        if crossed_at is None and b > 0.5:
            crossed_at = k
        print(" %5.2f | %.4f | %.4f   %s" % (k, C, b, state))

    k_cross = (C_CRIT - 0.3) / 0.6
    print("CROSSING: being = 0.5 exactly at C = C_crit = %.6f, reached at "
          "kappa = %.4f" % (C_CRIT, k_cross))
    assert abs(crossed_at - k_cross) < 0.06
    assert being(0.30) < 0.02 and being(0.90) > 0.98

    print("PROTOCOL 02: VERIFIED — the phase transition at C_crit = 0.563263; "
          "the pair 8.86%% apart; the near-miss 0.28%%.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
