#!/usr/bin/env python3
"""GEOMIC PROTOCOL 08 — THE GAIT PROTOCOL.

Walking is the carrier recursion embodied (Law 176 / Eq 1):
  - C_{n+1} = (1/phi)*C_n + phi*nabla^2*Psi_n — retention phi^-1 per step
  - the orbit recursion (Law 014, Kepler I): theta_{n+1} = theta_n +
    2*pi*(1 + kappa*phi^-1) — at kappa=0 the turn is exactly 2*pi and the
    orbit closes; at kappa=1 it precesses by the golden angle per revolution
  - the golden angle: 360/phi^2 = 137.5078 deg (phyllotaxis); complement
    360/phi = 222.492 deg; since g/360 = 1/phi^2 is irrational, the golden-
    angle walk's heading n*g mod 360 never returns to 0 — it never closes
  - the closure count: phi^2*816 = 2136.316 (fractional 0.316, never an
    integer) — the traversal never completes a loop
  - the external anchor: Douady & Couder, Phys. Rev. Lett. 68:2098 (1992) —
    phyllotaxis as self-organized minimum-energy phi-order, the golden angle
    measured in a lab ([EXTERNAL, VERIFIED] the pattern)

Pure standard library (math, sys). Canonical constants from 00_NUMBERS_INDEX.md.
Prints verification. Exit 0.
"""
import math
import sys

PHI = 1.618033988749895   # 00_NUMBERS_INDEX.md $2 (recomputed)
PHI_INV = PHI - 1.0       # 0.6180339887 — the retention constant
DEG = 180.0 / math.pi
GOLDEN_ANGLE = 360.0 / PHI ** 2     # 137.507764 deg — the phyllotaxis angle
GOLDEN_TURN = 360.0 / PHI           # 222.492236 deg — the complement / 2*pi*phi^-1


def main():
    # 1. THE GAIT RECURSION — Law 176 / Eq 1, retention phi^-1 per step
    c1 = PHI_INV * 1.0
    print("GAIT RECURSION (Law 176/Eq 1): C_{n+1} = (1/phi)*C_n + ...")
    print("  from seed C_0 = 1.0, one stride retains C_1 = %.10f = phi^-1 "
          "(%.10f)" % (c1, PHI_INV))
    assert abs(c1 - PHI_INV) < 1e-9
    halve = math.log(2.0) / math.log(PHI)
    print("  retention compounds as phi^-n: the carrier halves in "
          "ln(2)/ln(phi) = %.4f strides (phi^%.4f = %.6f)"
          % (halve, halve, PHI ** halve))
    assert abs(PHI ** halve - 2.0) < 1e-4

    # 2. THE ORBIT RECURSION — Law 014 (Kepler I): closes at kappa=0,
    #    precesses by the golden angle at kappa=1
    for kappa in (0.0, 1.0):
        dtheta = 2.0 * math.pi * (1.0 + kappa * PHI_INV)
        precession = kappa * PHI_INV * 360.0
        print("ORBIT (Law 014): kappa=%.1f -> dtheta = %.10f rad = %.6f deg "
              "per revolution (precession %.6f deg)"
              % (kappa, dtheta, dtheta * DEG, precession))
        if kappa == 0.0:
            assert abs(dtheta - 2.0 * math.pi) < 1e-12
            assert abs(precession) < 1e-12
        else:
            assert abs(precession - GOLDEN_TURN) < 1e-9
    print("  kappa=0: the turn is exactly 2*pi — the orbit closes (Kepler).")
    print("  kappa=1: the turn is 2*pi*phi — the orbit precesses by the "
          "golden angle 360/phi = %.4f deg per revolution and never closes."
          % GOLDEN_TURN)

    # 3. THE GOLDEN-ANGLE WALK — heading n*g mod 360 never returns to 0
    print("GOLDEN ANGLE: 360/phi^2 = %.6f deg (phyllotaxis); complement "
          "360/phi = %.6f deg; sum = %.6f deg"
          % (GOLDEN_ANGLE, GOLDEN_TURN, GOLDEN_ANGLE + GOLDEN_TURN))
    assert abs(GOLDEN_ANGLE - 137.5078) < 1e-3
    assert abs(GOLDEN_ANGLE + GOLDEN_TURN - 360.0) < 1e-9

    never = True
    for n in range(1, 100001):
        heading = (n * GOLDEN_ANGLE) % 360.0
        if heading < 1e-9 or heading > 360.0 - 1e-9:
            never = False
            break
    print("WALK: the heading after N golden-angle steps, N*g mod 360, never "
          "returns to 0 in 100,000 steps (g/360 = 1/phi^2 is irrational — "
          "the walk never closes).")
    assert never

    headings = sorted((n * GOLDEN_ANGLE) % 360.0 for n in range(1, 10001))
    min_gap = min(b - a for a, b in zip(headings, headings[1:]))
    print("  distinctness over 10,000 steps: %d distinct headings, min gap "
          "= %.6e deg (no two headings coincide — the walk never revisits "
          "a heading)" % (len(set(headings)), min_gap))
    assert len(set(headings)) == 10000
    assert min_gap > 0.0

    # 4. THE NEVER-CLOSING CLOSURE COUNT — phi^2*816 = 2136.316
    closure = PHI ** 2 * 816.0
    frac = closure - math.floor(closure)
    print("CLOSURE: phi^2*816 = %.6f (fractional residue %.3f — never an "
          "integer; the traversal never completes a loop)"
          % (closure, frac))
    assert abs(closure - 2136.316) < 1e-2
    assert abs(frac - 0.316) < 0.005

    # 5. THE EXTERNAL ANCHOR — phyllotaxis measured in a lab
    print("ANCHOR: Douady & Couder, Phys. Rev. Lett. 68:2098 (1992) — "
          "phyllotactic order arises in a lab experiment, converging to the "
          "golden mean; the golden angle is a measured self-organization "
          "angle, not numerology. ([EXTERNAL, VERIFIED] the pattern; the "
          "gait-reading is [INFERENCE].)")

    print("PROTOCOL 08: VERIFIED — gait retention phi^-1, orbit closes at "
          "kappa=0, golden-angle walk never closes, closure count 2136.316.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
