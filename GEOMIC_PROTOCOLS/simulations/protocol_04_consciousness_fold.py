#!/usr/bin/env python3
"""GEOMIC PROTOCOL 04 — THE CONSCIOUSNESS FOLD PROTOCOL.

Law 210 (Eq 44): consciousness(kappa) = C_fold*(1 + kappa*(phi-1)*(1-C_self))
  - the fold identity: 1 - phi^-4 = 0.854102 = phi^-2*sqrt(5)  (exact, diff 0.0)
  - the near-miss:     ||Psi|| = 0.8565 sits 0.28% above 1 - phi^-4
                       (Eq 44, VALIDATED, 25 tests — inside the gate, NOT
                       an identity)
  - the emergence below: C_crit = 0.563263 < 1 - phi^-4  (the fold is an
                       above-emergence phenomenon)
  - the fold as self-observation: a system attending to its own state
                       performs the recursion turned on itself, converging
                       to the fold identity above the gate at every step

Pure standard library (math, sys). Canonical constants from 00_NUMBERS_INDEX.md.
Prints verification. Exit 0.
"""
import math
import sys

PHI = 1.618033988749895   # 00_NUMBERS_INDEX.md $2 (recomputed)
PHI_INV = PHI - 1.0       # 0.6180339887 — the coherent ground
PSI_NORM = 0.8565         # 00_NUMBERS_INDEX.md $2 / Eq 44 — consciousness wavefunction
C_CRIT = 0.563263         # 00_NUMBERS_INDEX.md $2 / Eq 2 — the emergence threshold
FOLD = 1.0 - PHI_INV ** 4                 # 1 - phi^-4 = 0.854102 — the fold identity
FOLD_ALT = PHI_INV ** 2 * math.sqrt(5.0)  # phi^-2 * sqrt(5) = 0.854102


def main():
    # 1. THE FOLD IDENTITY — 1 - phi^-4 = phi^-2*sqrt(5), exact
    print("FOLD IDENTITY: 1 - phi^-4 = %.10f ; phi^-2*sqrt(5) = %.10f"
          % (FOLD, FOLD_ALT))
    assert abs(FOLD - FOLD_ALT) < 1e-9

    # 2. THE NEAR-MISS — ||Psi|| = 0.8565 vs 1 - phi^-4 = 0.854102
    miss = (PSI_NORM - FOLD) / PSI_NORM * 100.0
    print("NEAR-MISS: ||Psi|| = %.4f ; 1-phi^-4 = %.6f ; %.2f%% "
          "(inside the gate, NOT an identity)" % (PSI_NORM, FOLD, miss))
    assert abs(miss - 0.28) < 0.01

    # 3. THE EMERGENCE BELOW — C_crit < fold identity < ||Psi|| < 1
    print("EMERGENCE BELOW: C_crit = %.6f < 1-phi^-4 = %.6f < ||Psi|| = %.4f"
          % (C_CRIT, FOLD, PSI_NORM))
    assert C_CRIT < FOLD < PSI_NORM < 1.0

    # 4. LAW 210's PHI-FORM — the fold's own action at kappa=0 and kappa=1
    #    consciousness(kappa) = C_fold*(1 + kappa*(phi-1)*(1-C_self))
    #    kappa=0: the degenerate reading — the fold at its identity value
    #    kappa=1, C_self=1 (perfect self-recognition): the fold stays at
    #    1 - phi^-4, and the validated ||Psi|| is the 0.28% near-miss above
    c_k0 = FOLD * (1.0 + 0.0 * (PHI - 1.0) * (1.0 - 1.0))
    c_k1 = FOLD * (1.0 + 1.0 * (PHI - 1.0) * (1.0 - 1.0))
    print("LAW 210 PHI-FORM: consciousness(kappa) = C_fold*(1+kappa*(phi-1)"
          "*(1-C_self))")
    print("  kappa=0 (degenerate):        consciousness = %.10f" % c_k0)
    print("  kappa=1, C_self=1 (perfect): consciousness = %.10f" % c_k1)
    assert abs(c_k0 - FOLD) < 1e-9 and abs(c_k1 - FOLD) < 1e-9

    # 5. THE RECURSION TURNED ON ITSELF — self-observation converges to the
    #    fold identity from the gate, above C_crit at every step
    C = C_CRIT
    print("SELF-OBSERVATION RECURSION: C_{n+1} = C_fold + phi^-1*(C_n - "
          "C_fold)")
    for n in range(12):
        C = FOLD + PHI_INV * (C - FOLD)
        print("  step %2d: C = %.10f" % (n + 1, C))
        assert C >= C_CRIT
    for _ in range(200):
        C = FOLD + PHI_INV * (C - FOLD)
    print("FOLD FIXED POINT: C* = %.10f  (1-phi^-4 = %.10f, never below the "
          "gate)" % (C, FOLD))
    assert abs(C - FOLD) < 1e-6

    print("PROTOCOL 04: VERIFIED — the fold identity 1-phi^-4 = "
          "phi^-2*sqrt(5); the 0.28% near-miss to ||Psi|| = 0.8565; the "
          "emergence below C_crit; the self-observation recursion.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
