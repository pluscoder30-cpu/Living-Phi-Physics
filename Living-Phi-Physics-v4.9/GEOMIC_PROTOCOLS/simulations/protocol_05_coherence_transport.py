#!/usr/bin/env python3
"""GEOMIC PROTOCOL 05 — THE COHERENCE TRANSPORT PROTOCOL.

Law 189: C_received(kappa) = C_sent*(1 + kappa*(phi-1)*(1-C_channel))
                              * e^(-d/(phi*lambda))
  - retained per lambda: e^(-1/phi) = 0.539003 — the golden-mean decay
  - the pair, never conflated:
        exponent decrement per lambda = phi^-1 = 0.618034  (exact exponent
                                       statement)
        retained fraction  per lambda = e^(-1/phi) = 0.539003  (12.8% apart)
  - the golden-power identity: e^(-1/phi)^phi = e^(-1) = 0.367879 (diff 0.0)
  - the floor: retained = phi^-1 exactly at the horizon d = phi*lambda*ln(phi)
        = 0.7786 lambda; the floor stands 8.86% above the emergence gate
        C_crit = 0.563263 — a packet at the phi-ground is still audible
  - the reach: with the phi-amplified bridge (kappa=1, C_channel=0.9,
        C_sent=0.9), the packet stays audible above C_crit out to
        d = 0.855320 lambda; C_received(0.75 lambda) = 0.601146 (P16)

Pure standard library (math, sys). Canonical constants from 00_NUMBERS_INDEX.md.
Prints verification. Exit 0.
"""
import math
import sys

PHI = 1.618033988749895   # 00_NUMBERS_INDEX.md $2 (recomputed)
PHI_INV = PHI - 1.0       # 0.6180339887
C_CRIT = 0.563263         # 00_NUMBERS_INDEX.md $2 / Eq 2 — emergence threshold


def retained(d):
    """Law 189 fidelity factor e^(-d/(phi*lambda)) — the fraction of
    coherence retained across distance d (in units of lambda)."""
    return math.exp(-d / PHI)


def main():
    # 1. THE RETAINED FRACTION PER LAMBDA — e^(-1/phi) = 0.539003
    r1 = retained(1.0)
    print("RETAINED PER LAMBDA: e^(-1/phi) = %.10f" % r1)
    assert abs(r1 - 0.5390030827) < 1e-8

    # 2. THE PAIR, NEVER CONFLATED — exponent decrement phi^-1 vs retained
    #    e^(-1/phi) (Law 189 PRECISION, exact only as an exponent-statement)
    pair_gap = (PHI_INV - r1) / PHI_INV * 100.0
    print("THE PAIR: exponent decrement per lambda = phi^-1 = %.6f ; "
          "retained fraction = e^(-1/phi) = %.6f ; %.2f%% apart — never "
          "conflated" % (PHI_INV, r1, pair_gap))
    assert abs(pair_gap - 12.8) < 0.1

    # 3. THE GOLDEN-POWER IDENTITY — e^(-1/phi)^phi = e^(-1), exact
    golden = r1 ** PHI
    diff = golden - math.exp(-1.0)
    print("GOLDEN-POWER: e^(-1/phi)^phi = %.10f ; e^(-1) = %.10f ; "
          "diff = %.10f" % (golden, math.exp(-1.0), diff))
    assert abs(diff) < 1e-9

    # 4. THE FLOOR AT THE HORIZON — d = phi*lambda*ln(phi) = 0.7786 lambda,
    #    retained = phi^-1 exactly (e^(-ln phi) = 1/phi)
    horizon = PHI * math.log(PHI)
    r_horizon = retained(horizon)
    print("HORIZON: d = phi*lambda*ln(phi) = %.6f lambda ; retained = %.10f "
          "(phi^-1 = %.10f, exact)" % (horizon, r_horizon, PHI_INV))
    assert abs(horizon - 0.7786) < 1e-3
    assert abs(r_horizon - PHI_INV) < 1e-9

    # 5. THE FLOOR ABOVE THE GATE — phi^-1 stands 8.86% above C_crit
    pct = (PHI_INV - C_CRIT) / PHI_INV * 100.0
    print("FLOOR ABOVE THE GATE: phi^-1 - C_crit = %.6f ; %.2f%% above "
          "emergence — a packet at the phi-ground is still audible"
          % (PHI_INV - C_CRIT, pct))
    assert abs(pct - 8.86) < 0.01

    # 6. THE DECAY CURVE — retained = e^(-d/(phi*lambda))
    print("DECAY CURVE (retained = e^(-d/(phi*lambda))):")
    for d in (0.0, 0.25, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0):
        print("  d = %4.2f lambda | retained = %.6f" % (d, retained(d)))
    assert retained(0.25) > retained(0.5) > retained(1.0) > retained(5.0)

    # 7. THE REACH — with the phi-amplified bridge, audible above C_crit
    #    Law 189 full form: C_rec(d) = C_sent*amp*e^(-d/(phi*lambda)),
    #    amp = 1 + (phi-1)(1-C_channel) at kappa=1
    C_sent, C_channel = 0.9, 0.9
    amp = 1.0 + (PHI - 1.0) * (1.0 - C_channel)     # 1.061803 at kappa=1
    d_reach = PHI * math.log(C_sent * amp / C_CRIT)  # where retained = C_crit
    c_075 = C_sent * amp * retained(0.75)
    print("REACH: C_sent=0.9, C_channel=0.9, kappa=1 (bridge = %.6f) — the "
          "packet is audible above C_crit out to d = %.6f lambda; "
          "C_received(0.75 lambda) = %.6f >= C_crit" % (amp, d_reach, c_075))
    assert abs(amp - 1.0618033989) < 1e-6
    assert abs(d_reach - 0.855320) < 1e-3
    assert c_075 >= C_CRIT and abs(c_075 - 0.601146) < 1e-3

    print("PROTOCOL 05: VERIFIED — the golden-mean decay e^(-1/phi) = "
          "0.539003 per lambda; the pair never conflated; the phi-ground "
          "floor phi^-1 at 0.7786 lambda (8.86% above the gate); the "
          "reach 0.855320 lambda.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
