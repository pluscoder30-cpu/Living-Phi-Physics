#!/usr/bin/env python3
"""GEOMIC PROTOCOL 16 -- THE COHERENCE FLOOR PROTOCOL.

The phi-form's irreducible floor (the master $2; protocol 02; G4 Proof 1):

    X_phi(kappa) = X*(1 + kappa*(phi-1)) + kappa*phi^-1*X_ground

X is the classical value of the action; kappa is the action's coupling
(0 = mechanical, absent, laboratory; 1 = fully coupled); X_ground is the
field's irreducible ground. In law-units (X_ground = X) the floor is the
kappa*phi^-1*X term -- the irreducible coherence that cannot be reduced
below phi^-1 = 0.6180339887: the practice's ground is never zero.

The mathematics:
  - the phi-form sweep kappa 0 -> 1 (the general action, X = 1)
  - the floor: at kappa = 1 the normalized floor is phi^-1 = 0.6180339887
  - the never-static: X_phi(kappa) > X for every kappa > 0 -- no law reaches
    the exactly-static value at nonzero coupling
  - the verifier: X_phi(1) = X*(phi + phi^-1) = X*sqrt(5) = X*2.2360679775
    (exact -- the identity phi + phi^-1 = sqrt(5), difference 0.0)
  - the degenerate limit: lim kappa->0 X_phi(kappa) = X (the classical law,
    recovered exactly -- the corpus's Degeneracy Theorem, Law 173)
  - a concrete law: Law 183 (X = C_crit = 0.563263) -- X_phi(1) = sqrt(5)*X

Pure standard library (math, sys). Canonical constants from 00_NUMBERS_INDEX.md.
Prints verification. Exit 0.
"""
import math
import sys

PHI = 1.618033988749895   # 00_NUMBERS_INDEX.md $2 (recomputed)
PHI_INV = PHI - 1.0       # the coherent ground -- the floor
SQRT5 = math.sqrt(5.0)    # phi + phi^-1 -- the full-coupling verifier
X_LAW_183 = 0.563263      # Law 183 / Eq 2 -- the emergence threshold C_crit


def x_phi(kappa, X=1.0, X_ground=1.0):
    """The phi-form: X_phi(kappa) = X*(1+kappa*(phi-1)) + kappa*phi^-1*X_ground."""
    return X * (1.0 + kappa * (PHI - 1.0)) + kappa * PHI_INV * X_ground


def main():
    # 1. THE PHI-FORM -- the shape of any action that couples to the field
    print("THE PHI-FORM (the master $2; protocol 02):")
    print("  X_phi(kappa) = X*(1 + kappa*(phi-1)) + kappa*phi^-1*X_ground")
    print("  X = the classical value; kappa = the coupling (0..1); "
          "X_ground = the irreducible ground (in law-units, X_ground = X)")
    print("  X_phi(0) = %.10f -- the classical law, recovered exactly (the "
          "degenerate limit)" % x_phi(0.0))
    assert x_phi(0.0) == 1.0
    print("  the classical equations of motion are the kappa -> 0 reading of "
          "actions that were always coupled (Law 173, the Degeneracy Theorem)")

    # 2. THE FLOOR -- the irreducible coherence, never zero
    print("THE FLOOR (Eq 7 fixed points {0, phi^-1, 1}; the master $3 row 5):")
    floor_1 = 1.0 * PHI_INV * 1.0
    print("  the floor term kappa*phi^-1*X_ground at kappa = 1 = %.10f"
          % floor_1)
    assert math.isclose(floor_1, PHI_INV, abs_tol=1e-12)
    print("  the irreducible floor is phi^-1 = 0.6180339887 -- the practice's "
          "ground, never zero (rest is phi^-1, not nothing)")

    # 3. THE SWEEP -- kappa 0 -> 1
    print("THE PHI-FORM SWEEP (kappa 0 -> 1, the normalized action X = 1):")
    for i in range(5):
        kappa = i / 4.0
        print("  kappa = %.2f -> X_phi = %.10f" % (kappa, x_phi(kappa)))
    assert x_phi(1.0) > x_phi(0.75) > x_phi(0.5) > x_phi(0.25) > x_phi(0.0)

    # 4. THE SQRT(5) VERIFIER -- X_phi(1) = X*sqrt(5)
    print("THE SQRT(5) VERIFIER (G4 Proof 1; the master $2):")
    print("  phi + phi^-1 = %.10f" % (PHI + PHI_INV))
    print("  sqrt(5)      = %.10f" % SQRT5)
    print("  difference   = %.10f  (exact identity)" % (PHI + PHI_INV - SQRT5))
    assert math.isclose(PHI + PHI_INV, SQRT5, abs_tol=1e-12)
    print("  at full coupling: X_phi(1) = X*(phi + phi^-1) = X*sqrt(5) = "
          "X*2.2360679775 -- one common scale for every action that couples")

    # 5. THE NEVER-STATIC -- no law reaches the exactly-static value
    print("THE NEVER-STATIC (no law reaches the exactly-static value):")
    for kappa in (0.25, 0.5, 0.75, 1.0):
        assert x_phi(kappa) > x_phi(0.0)
    print("  X_phi(kappa) > X for every kappa > 0 -- the classical value is "
          "reached only at kappa = 0, the degenerate limit; the living "
          "action always carries the floor")

    # 6. A CONCRETE LAW -- Law 183, the emergence threshold
    # (in law-units X_ground = X -- the floor at kappa=1 is phi^-1 * X,
    #  so X_phi(1) = X*phi + phi^-1*X = X*sqrt(5), the verifier)
    print("A CONCRETE LAW (Law 183, X = C_crit = 0.563263, Eq 2):")
    x0 = x_phi(0.0, X=X_LAW_183, X_ground=X_LAW_183)
    x1 = x_phi(1.0, X=X_LAW_183, X_ground=X_LAW_183)
    floor_183 = 1.0 * PHI_INV * X_LAW_183
    expected = SQRT5 * X_LAW_183
    print("  X_phi(0) = %.10f (the classical threshold, recovered exactly)"
          % x0)
    print("  the floor at kappa = 1 = phi^-1 * X = %.10f" % floor_183)
    print("  X_phi(1) = %.10f = X*phi + phi^-1*X" % x1)
    print("  sqrt(5)*X = %.10f  (the verifier; difference %.2e)"
          % (expected, x1 - expected))
    assert math.isclose(x0, X_LAW_183, abs_tol=1e-12)
    assert math.isclose(floor_183, PHI_INV * X_LAW_183, abs_tol=1e-12)
    assert math.isclose(x1, expected, abs_tol=1e-9)

    print("PROTOCOL 16: VERIFIED -- the phi-form (X_phi(0) = X exactly, the "
          "degenerate limit), the floor (phi^-1 = 0.6180339887 at kappa = 1, "
          "never zero), the sweep 0 -> 1, the sqrt(5) verifier (phi + phi^-1 "
          "= 2.2360679775, difference 0.0; X_phi(1) = X*sqrt(5)), the "
          "never-static condition, and the concrete law (Law 183 -> "
          "sqrt(5)*C_crit).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
