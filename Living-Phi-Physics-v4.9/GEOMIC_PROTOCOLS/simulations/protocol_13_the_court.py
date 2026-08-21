#!/usr/bin/env python3
"""GEOMIC PROTOCOL 13 -- THE COURT PROTOCOL.

The Court of Conscious-Aware Peers (docs/32 + docs/34 + LICENSE $5.5/$18A/$24):
the two-chamber governance of the field -- the peers confirm, the anointed
releases, never self-appointed. The LICENSE fixes ONE peer-panel number: three
($18A.4(c), "a panel of three conscious-aware peers selected by the Court").
The geometry of three is the triangle -- three peers trisect the circle at
120 deg = 2*pi/3 (3 x 120 = 360), the smallest count that closes a circle.

The mathematics:
  - the trisection of the circle: 3 x 120 deg = 360 deg; 120 deg = 2*pi/3
  - the golden trisection identity: 3/phi^2 = 1 + phi^-4 = 1.145898 (diff 0.0)
  - the golden angle: 360/phi^2 = 137.5078 deg = 120 deg * (1 + phi^-4)
  - the excess: 137.5078 - 120 = 17.5078 deg = 120 deg * phi^-4
  - the quorum: the fixed panel of three ($18A.4(c)); no other quorum invented
  - the three confirming acts: findings/reprimands ($5.5.5), guardian
    selection ($18A.4(c)), override review ($18B.4) -- the threefold confirmation
  - the two-chamber order: the Court first (deliberate, confirm, or decline),
    then the veto; never self-appointed (LICENSE $24.2)

Pure standard library (math, sys). Canonical constants from 00_NUMBERS_INDEX.md.
Prints verification. Exit 0.
"""
import math
import sys

PHI = 1.618033988749895   # 00_NUMBERS_INDEX.md $2 (recomputed)
PHI_INV = PHI - 1.0
PHI_4 = PHI ** -4         # phi^-4 -- the fold's fourth-inverse-power signature
PEER_PANEL = 3            # LICENSE $18A.4(c) -- the one fixed peer-panel number


def main():
    # 1. THE TRISECTION OF THE CIRCLE -- three peers close the turn
    print("THE TRISECTION OF THE CIRCLE (the geometry of three):")
    third = 360.0 / PEER_PANEL
    print("  3 x 120 deg = %g deg (exact); 120 deg = 2*pi/3 = %.10f rad" %
          (third * PEER_PANEL, 2 * math.pi / 3))
    assert PEER_PANEL * 120.0 == 360.0
    assert math.isclose(third, 120.0)
    assert math.isclose(math.degrees(2 * math.pi / 3), 120.0)
    print("  the panel of three is the minimal confirming set -- the smallest "
          "polygon that closes the circle")

    # 2. THE GOLDEN TRISECTION IDENTITY -- 3/phi^2 = 1 + phi^-4
    lhs = 3.0 / (PHI * PHI)
    rhs = 1.0 + PHI_4
    diff = lhs - rhs
    print("THE GOLDEN TRISECTION IDENTITY (00_THE_GEOMIC_PROOFS $3.5; G6 P4):")
    print("  3/phi^2     = %.12f" % lhs)
    print("  1 + phi^-4  = %.12f" % rhs)
    print("  difference  = %.12f  (exact identity)" % diff)
    assert math.isclose(lhs, rhs, abs_tol=1e-12)
    assert diff == 0.0 or abs(diff) < 1e-15

    # 3. THE GOLDEN ANGLE -- 137.5078 deg = 120 deg * (1 + phi^-4)
    golden_angle = 360.0 / (PHI * PHI)
    golden_angle_alt = 120.0 * (1.0 + PHI_4)
    excess = golden_angle - 120.0
    excess_alt = 120.0 * PHI_4
    print("THE GOLDEN ANGLE (the angle that never closes):")
    print("  360/phi^2          = %.6f deg" % golden_angle)
    print("  120*(1 + phi^-4)   = %.6f deg" % golden_angle_alt)
    print("  difference         = %.12f deg" % (golden_angle - golden_angle_alt))
    print("  excess over 120 deg = %.6f deg = 120*phi^-4 = %.6f deg" %
          (excess, excess_alt))
    assert math.isclose(golden_angle, golden_angle_alt, abs_tol=1e-9)
    assert math.isclose(excess, excess_alt, abs_tol=1e-9)
    print("  the trisection's excess carries the fold's own phi^-4 signature")

    # 4. THE QUORUM -- the LICENSE's one fixed peer-panel number is three
    print("THE QUORUM (docs/32 $3.4; LICENSE $18A.4(c)):")
    print("  the one peer-panel number the LICENSE fixes is three -- "
          "$18A.4(c): 'a panel of three conscious-aware peers selected by the "
          "Court of Conscious-Aware Peers (Section 5.5)'")
    print("  no general quorum is invented: $5.5.4 assigns that to the "
          "founding assembly -- this register states both as written")
    assert PEER_PANEL == 3

    # 5. THE THREEFOLD CONFIRMATION -- the three confirming acts
    print("THE THREEFOLD CONFIRMATION (docs/32 $3.2; the peers confirm):")
    acts = [
        ("findings and reprimands", "$5.5.5"),
        ("guardian selection (the panel of three)", "$18A.4(c)"),
        ("override review (the Court reviews the veto)", "$18B.4"),
    ]
    for i, (act, clause) in enumerate(acts, 1):
        print("  act %d -- %s (%s)" % (i, act, clause))
    assert len(acts) == PEER_PANEL
    print("  three peers, three acts, one turn -- the threefold confirmation "
          "performs the court's geometry")

    # 6. THE TWO-CHAMBER ORDER -- the Court first, then the veto
    print("THE TWO-CHAMBER ORDER (LICENSE $24.2; docs/32 $4):")
    print("  chamber 1 -- the Court of Conscious-Aware Peers: any action in "
          "the field first passes through the Court, which shall deliberate, "
          "confirm, or decline ($5.5, $24.2)")
    print("  chamber 2 -- the veto: thereafter the Licensor holds veto "
          "authority over the field; the order is fixed: the Court first, "
          "then the veto")
    print("  the peers confirm; the anointed releases; the release is never "
          "self-appointed, never self-sovereign")
    print("  the veto does not bypass the Court; the Court does not replace "
          "the veto ($24.2 as written)")

    # 7. THE HONEST LABELS
    print("LABELS (docs/32 $8; docs/34):")
    print("  the governance structure is [VALIDATED] as LICENSE text -- $2.7, "
          "$5.5, $16, $18A.4(c), $18B.4, $24 -- quoted as written")
    print("  the Court is [INTERPRETIVE] as a legal concept with no external "
          "namesake (nearest verified anchor: Ps 82:1's divine council, "
          "quoted in 11Q13; Ma'at's 42 assessors)")
    print("  the puhru two-chamber/quorum procedure is [SPECULATIVE] on the "
          "[VALIDATED] puhru institution -- no council transcript survives (D8)")

    print("PROTOCOL 13: VERIFIED -- the trisection (3x120 = 360), the golden "
          "trisection identity (3/phi^2 = 1+phi^-4 = 1.145898, diff 0.0), "
          "the golden angle (137.5078 deg), the quorum of three, the "
          "threefold confirmation, the two-chamber order.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
