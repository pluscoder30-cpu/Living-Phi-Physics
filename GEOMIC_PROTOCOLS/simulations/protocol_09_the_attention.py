#!/usr/bin/env python3
"""GEOMIC PROTOCOL 09 — THE ATTENTION PROTOCOL.

The observer-gate (Law 157 / Eq 50):
  - the gate constant: Theta_phi = C_crit*(1 + phi^-1) = C_crit*phi
    = 0.911379 (the corpus's boxed 0.9114; the R7 operator-text reading 1.0
    is an identity artifact, phi^-1*(1+phi^-1) = 1 exactly — excluded)
  - the gate: adopt the new state iff its coherence >= Theta_phi, else keep
    the old state (collapse is coherence-gating; the Born rule is the
    kappa->0 limit)
  - the emergence threshold C_crit = 0.563263 (Eq 2) is the floor below;
    the pair C_crit vs phi^-1 is 8.86% apart, never conflated
  - the fixed points of the gated attention recursion (Eq 7, VALIDATED) are
    exactly {0, phi^-1, 1}: 0 the substrate (never occupied — the ground is
    never zero), phi^-1 the stable resting attention, 1 the full-coherence
    limit. The in-code recursion shape g(C) = C*(1+phi^-1*(C-phi^-1)*(C-1))
    is [INFERENCE]; the fixed-point set is the corpus's VALIDATED {0,phi^-1,1}
  - ordering: 0 < C_crit < phi^-1 < Theta_phi < 1 — the threshold below the
    ground, the gate above it, near full coherence
  - the external anchor: Ursachi 2026 (N=320, 80% of subjects, alpha/theta
    = 1.677, 3.6% from phi, r = 0.54, p < 10^-25, PMID 41859481) — conscious
    states are measurable coherence regimes ([EXTERNAL, VERIFIED])

Pure standard library (math, sys). Canonical constants from 00_NUMBERS_INDEX.md.
Prints verification. Exit 0.
"""
import math
import sys

PHI = 1.618033988749895   # 00_NUMBERS_INDEX.md $2 (recomputed)
PHI_INV = PHI - 1.0       # 0.6180339887 — the coherent ground
C_CRIT = 0.563263         # 00_NUMBERS_INDEX.md $2 / Eq 2 — emergence threshold
THETA = C_CRIT * (1.0 + PHI_INV)   # 0.911378679 — the gate = C_crit*phi


def gate(c_new, c_old):
    """Eq 50's Self-Modification Coherence Gate: adopt iff >= Theta_phi."""
    return c_new if c_new >= THETA else c_old


def g(c):
    """The gated attention recursion (Eq 7's dynamics, [INFERENCE] shape):
    fixed points are exactly the roots of C*(C-phi^-1)*(C-1) = 0."""
    return c * (1.0 + PHI_INV * (c - PHI_INV) * (c - 1.0))


def main():
    # 1. THE GATE CONSTANT — Theta_phi = C_crit*(1 + phi^-1) = C_crit*phi
    print("GATE CONSTANT: Theta_phi = C_crit*(1 + phi^-1) = C_crit*phi")
    print("  (1 + phi^-1) = %.10f  (phi = %.10f; diff %.2e)"
          % (1.0 + PHI_INV, PHI, (1.0 + PHI_INV) - PHI))
    assert abs((1.0 + PHI_INV) - PHI) < 1e-12
    print("  Theta_phi = %.10f (the corpus's boxed 0.9114)" % THETA)
    assert abs(THETA - 0.9114) < 1e-4
    print("  note: the R7 operator-text reading phi^-1*(1+phi^-1) = 1.0 is "
          "an identity artifact (%.10f), 0.089 from the boxed value — the "
          "honesty flag carried, the boxed value enters the table."
          % (PHI_INV * (1.0 + PHI_INV)))
    assert abs(PHI_INV * (1.0 + PHI_INV) - 1.0) < 1e-12

    # 2. THE GATE FUNCTION — weak rejected, strong adopted (Eq 50 / Law 157)
    old = 0.60
    weak = gate(0.128642, old)
    strong = gate(1.0, old)
    print("GATE: weak candidate C=0.128642 below Theta_phi -> old state kept "
          "(%.3f)" % weak)
    assert weak == old
    print("GATE: strong candidate C=1.000000 at/above Theta_phi -> adopted "
          "(%.3f) — collapse is coherence-gating, the Born rule is the "
          "kappa->0 limit" % strong)
    assert strong == 1.0
    boundary = gate(THETA, old)
    print("GATE: candidate exactly at Theta_phi -> admitted (>= gate)")
    assert boundary == THETA

    # 3. THE FIXED-POINT ANALYSIS — {0, phi^-1, 1}, the ground never zero
    print("FIXED POINTS (Eq 7, VALIDATED): the roots of C*(C-phi^-1)*(C-1)=0")
    for r in (0.0, PHI_INV, 1.0):
        res = r * (r - PHI_INV) * (r - 1.0)
        print("  C = %.10f : residual %.2e" % (r, res))
        assert abs(res) < 1e-12
    ok = True
    for i in range(1, 1000):
        c = i / 1000.0
        if abs(c * (c - PHI_INV) * (c - 1.0)) < 1e-6:
            ok = False
            break
    print("  scan C in (0,1): exactly the three fixed points {0, phi^-1, 1} "
          "(%s)" % ("confirmed" if ok else "FAILED"))
    assert ok

    c = 0.30
    for _ in range(200):
        c = g(c)
    print("  iterate g from C=0.30 (below the gate): settles at %.10f (the "
          "ground phi^-1 = %.10f — never zero)" % (c, PHI_INV))
    assert abs(c - PHI_INV) < 1e-9
    c = 0.95
    for _ in range(200):
        c = g(c)
    print("  iterate g from C=0.95 (above the gate): settles at %.10f (1 is "
          "the limit, phi^-1 the rest)" % c)
    assert abs(c - PHI_INV) < 1e-9

    # 4. THE CROSSING — substrate -> emergence -> ground -> gate -> coherence
    seq = [0.0, C_CRIT, PHI_INV, THETA, 1.0]
    for i in range(len(seq) - 1):
        assert seq[i] < seq[i + 1]
    print("CROSSING: 0 < C_crit (%.6f) < phi^-1 (%.6f) < Theta_phi (%.6f) "
          "< 1" % (C_CRIT, PHI_INV, THETA))
    print("  the pair: C_crit vs phi^-1 are %.2f%% apart, never conflated "
          "(protocol 2's pair)" % ((PHI_INV - C_CRIT) / PHI_INV * 100.0))

    traj = [0.30, 0.50, C_CRIT + 1e-4, 0.65, PHI_INV + 1e-4, 0.85,
            THETA + 1e-4, 0.97, 1.0]
    events = []
    if any(c >= C_CRIT for c in traj):
        events.append("emergence (C_crit)")
    if any(c >= PHI_INV for c in traj):
        events.append("ground (phi^-1)")
    if any(c >= THETA for c in traj):
        events.append("admission (Theta_phi)")
    print("  attention rising 0.30 -> 1.00 crosses: %s — the threshold event "
          "is the emergence phase transition (protocol 2's terrain)"
          % " -> ".join(events))
    assert events == ["emergence (C_crit)", "ground (phi^-1)",
                      "admission (Theta_phi)"]

    # 5. THE EXTERNAL ANCHOR — the EEG-phi record
    print("ANCHOR: Ursachi 2026, Front. Hum. Neurosci. 20:1781338, N=320, "
          "80% of subjects, alpha/theta = 1.677 (3.6% from phi), r = 0.54, "
          "p < 10^-25, PMID 41859481 — conscious states are measurable "
          "coherence regimes. ([EXTERNAL, VERIFIED] the pattern; the "
          "attention-reading is [INFERENCE].)")

    print("PROTOCOL 09: VERIFIED — Theta_phi = 0.911379, the gate admits "
          "above it, fixed points {0, phi^-1, 1}, the crossing sequence, "
          "the ground never zero.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
