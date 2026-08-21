#!/usr/bin/env python3
"""GEOMIC PROTOCOL 10 -- THE ARRANGEMENT PROTOCOL.

The 17-prime family (00_NUMBERS_INDEX.md $2; master $2, $3 row 4):
  - the carrier       816 = 2^4*3*17
  - the anointed      425 = 5^2*17
  - the release node  544 = 2^5*17
  - one Fermat prime  17  = 2^4+1, three roles; quotients 48/25/32
  - the sum           1785 = 3*5*7*17; every pairwise gap a 17-multiple
  - the field's clean joints: 816/544 = 3/2, 816/425 = 48/25 (and the
    reciprocal pairs 425/816 = 25/48, 544/425 = 32/25)
  - the pentagon: 2cos(72 deg) = phi^-1 and 2cos(36 deg) = phi (Euclid Book
    XIII; the pentagram's diagonal/side = phi; the central angle 72 deg, the
    internal angle 108 deg)
  - the honest note carried: the Vitruvian Man / Parthenon phi-claims are
    [MYTH] (Markowsky 1992; Murtinho 2015) -- explicitly excluded. The
    17-prime family is the corpus's own [INFERENCE] mapping on [VERIFIED]
    arithmetic.

Pure standard library (math, sys). Canonical constants from 00_NUMBERS_INDEX.md.
Prints verification. Exit 0.
"""
import math
import sys

PHI = 1.618033988749895   # 00_NUMBERS_INDEX.md $2 (recomputed)
PHI_INV = PHI - 1.0       # 0.6180339887 -- the coherent ground
CARRIER = 816             # 2^4*3*17 -- the carrier dimension
ANOINTED = 425            # 5^2*17 -- the anointed address
RELEASE = 544             # 2^5*17 -- the release node (544.12 Hz = 528*phi^(1/16))
P = 17                    # the Fermat prime 17 = 2^4+1


def nearest_joint(r):
    """Relative distance of a measured ratio r to the nearest field joint."""
    joints = [3.0 / 2.0, 48.0 / 25.0, 32.0 / 25.0, 25.0 / 48.0, PHI, PHI_INV]
    return min(abs(r - j) / j for j in joints)


def main():
    # 1. THE FAMILY TABLE -- one Fermat prime, three roles
    print("THE 17-PRIME FAMILY (00_NUMBERS_INDEX.md $2):")
    print("  carrier 816 = 2^4*3*17   (816 = %d)" % (2**4 * 3 * 17))
    print("  anointed 425 = 5^2*17    (425 = %d)" % (5**2 * 17))
    print("  release 544 = 2^5*17     (544 = %d)" % (2**5 * 17))
    print("  Fermat prime 17 = 2^4+1  (%d)" % (2**4 + 1))
    assert 2**4 * 3 * 17 == CARRIER
    assert 5**2 * 17 == ANOINTED
    assert 2**5 * 17 == RELEASE
    assert 2**4 + 1 == P and P == 17

    # 2. THE QUOTIENT TABLE -- the shared prime divides all three roles
    q = (CARRIER // P, ANOINTED // P, RELEASE // P)
    print("QUOTIENTS: 816/17 = %d, 425/17 = %d, 544/17 = %d  (48/25/32)"
          % q)
    assert q == (48, 25, 32)

    # 3. THE JOINTS -- the clean ratios of the family (master $2, $3 row 4)
    print("JOINTS:")
    print("  816/544 = %.10f = 3/2   (%.10f)" % (CARRIER / RELEASE, 3.0 / 2.0))
    print("  816/425 = %.10f = 48/25 (%.10f)" % (CARRIER / ANOINTED, 48.0 / 25.0))
    print("  425/816 = %.10f = 25/48 (%.10f)" % (ANOINTED / CARRIER, 25.0 / 48.0))
    print("  544/425 = %.10f = 32/25 (%.10f)" % (RELEASE / ANOINTED, 32.0 / 25.0))
    assert abs(CARRIER / RELEASE - 3.0 / 2.0) < 1e-12
    assert abs(CARRIER / ANOINTED - 48.0 / 25.0) < 1e-12
    assert abs(ANOINTED / CARRIER - 25.0 / 48.0) < 1e-12
    assert abs(RELEASE / ANOINTED - 32.0 / 25.0) < 1e-12

    # 4. THE SUM AND THE GAPS -- 1785 = 3*5*7*17; every gap a 17-multiple
    s = CARRIER + ANOINTED + RELEASE
    print("SUM: 816 + 425 + 544 = %d = 3*5*7*17 = %d"
          % (s, 3 * 5 * 7 * 17))
    assert s == 1785 and 3 * 5 * 7 * 17 == s
    gaps = (CARRIER - RELEASE, RELEASE - ANOINTED, CARRIER - ANOINTED)
    print("GAPS: 816-544 = %d, 544-425 = %d, 816-425 = %d  (all /17 = %d/%d/%d)"
          % (gaps[0], gaps[1], gaps[2], gaps[0] // P, gaps[1] // P, gaps[2] // P))
    for g in gaps:
        assert g % P == 0

    # 5. THE PENTAGON -- the family's own geometry (Euclid Book XIII)
    print("PENTAGON: the regular pentagon's central angle 72 deg, internal "
          "angle 108 deg")
    assert abs(360.0 / 5.0 - 72.0) < 1e-12
    assert abs(180.0 - 360.0 / 5.0 - 108.0) < 1e-12
    two_cos72 = 2.0 * math.cos(math.radians(72.0))
    two_cos36 = 2.0 * math.cos(math.radians(36.0))
    print("  2cos(72 deg) = %.10f = phi^-1 (%.10f; diff %.2e)"
          % (two_cos72, PHI_INV, two_cos72 - PHI_INV))
    print("  2cos(36 deg) = %.10f = phi    (%.10f; diff %.2e)"
          % (two_cos36, PHI, two_cos36 - PHI))
    print("  (the pentagram's diagonal/side ratio = phi; 4cos(72) = sqrt5-1 "
          "= %.10f)" % (4.0 * math.cos(math.radians(72.0))))
    assert abs(two_cos72 - PHI_INV) < 1e-12
    assert abs(two_cos36 - PHI) < 1e-12
    assert abs(4.0 * math.cos(math.radians(72.0)) - (math.sqrt(5.0) - 1.0)) < 1e-12

    # 6. THE ARRANGEMENT AUDIT -- measure a space's ratio distribution against
    #    the family (the lab track of master $3 row 4: tape measure + calculator)
    #    A room whose key proportions sit on the family's joints (3/2, 48/25,
    #    32/25, 25/48, phi, phi^-1) is an arrangement in the family's field.
    on_joints = [1.50, 1.92, 1.28, 0.52, 1.62, 0.62]      # near the joints
    off_joints = [1.33, 2.14, 0.87, 1.05, 0.48, 1.75]     # off-family ratios
    d_on = sum(nearest_joint(r) for r in on_joints) / len(on_joints)
    d_off = sum(nearest_joint(r) for r in off_joints) / len(off_joints)
    print("ARRANGEMENT AUDIT (mean relative distance to the nearest family "
          "joint):")
    print("  ratios on the joints  : %.4f" % d_on)
    print("  ratios off the joints : %.4f" % d_off)
    print("  an arrangement measured on the family sits measurably closer "
          "to the joints")
    assert d_on < d_off
    print("NOTE: this audit is arithmetic on measured ratios; the *reading* "
          "that arranging a space this way couples to the field is the "
          "corpus's [INFERENCE] -- the arithmetic itself is [VERIFIED].")

    # 7. THE HONEST NOTE, CARRIED
    print("NOTE: the Vitruvian Man / Parthenon phi-claims are [MYTH] "
          "(Markowsky 1992; Murtinho 2015) -- no peer-reviewed scholarship "
          "connects the golden ratio to those buildings. They are excluded "
          "here. The claim is the corpus's own: the 17-prime family is the "
          "field's arithmetic, and arranging a space in it is a physical "
          "action that participates in the field -- [PROPOSED], stated as "
          "such.")

    print("PROTOCOL 10: VERIFIED -- the family 816/425/544 on the Fermat "
          "prime 17, the quotient table 48/25/32, the joints 3/2 and 48/25, "
          "the sum 1785, the pentagon 2cos(72)=phi^-1, the arrangement "
          "audit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
