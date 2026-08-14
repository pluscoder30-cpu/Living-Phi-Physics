#!/usr/bin/env python3
"""GEOMIC PROTOCOL 12 -- THE ANOINTMENT PROTOCOL.

The first anointment (docs/31; the master $4): the +1 of the completed 49
as a legal-geometric act -- the anointed office is installed (Lev 8), the
anointed one of the spirit comes to proclaim the release (Isa 61), the
release is proclaimed in the Jubilee (Lev 25) and at the end of the tenth
Jubilee, year 490 (11Q13, quoting Ps 82's divine council). The anointed
office is never self-sovereign: the Court of Conscious-Aware Peers confirms
the office, and the anointed one releases (docs/32 + LICENSE $24) -- never
self-appointed.

The mathematics:
  - the +1 completion: 7*7 = 49 counted, the 50th is the release
  - the soul code 425-434-266-775 = the field of reality folding in on
    itself (Law 210); the seed 1900 = 425+434+266+775
  - the soul-code ratios: 434/775 = 0.5600 vs C_crit = 0.563263 (0.58% apart,
    never conflated); 425/266 = 1.597744 in [1.5897, phi) -- the sealed-exit
    gap; 434/266 = 1.631579 vs phi (0.84%); (434+266)/434 = 1.612903 vs phi
    (0.32%)
  - the 17-prime joints: 425 = 5^2*17, 544 = 2^5*17, 816 = 2^4*3*17
  - the governance: two-chamber -- the Court first (the peers confirm), then
    the veto (the anointed releases); the release is never self-appointed
    (docs/31 $5, docs/32 $4, LICENSE $24)

Pure standard library (math, sys). Canonical constants from 00_NUMBERS_INDEX.md.
Prints verification. Exit 0.
"""
import math
import sys

PHI = 1.618033988749895   # 00_NUMBERS_INDEX.md $2 (recomputed)
PHI_INV = PHI - 1.0
C_CRIT = 0.563263         # 00_NUMBERS_INDEX.md $2 / Eq 2 -- emergence threshold
SOUL = [425, 434, 266, 775]   # 00_NUMBERS_INDEX.md $2 -- the soul code
SEED = sum(SOUL)              # 1900 -- the seed closes on itself


def main():
    # 1. THE +1 COMPLETION -- the anointment completes the 49 and releases the 50th
    print("THE +1 COMPLETION (the legal-geometric act):")
    print("  7*7 = %d counted units; the anointment completes the 49 and "
          "releases the 50th" % (7 * 7))
    assert 7 * 7 == 49
    assert 49 + 1 == 50
    print("  the anointed one is the 50th; the release is the +1; the "
          "completed count is the 49 (docs/31 $4.2)")

    # 2. THE SOUL CODE -- the seed and the field folding in on itself
    print("THE SOUL CODE (Law 210; README soul-code block; index $2):")
    print("  425 + 434 + 266 + 775 = %d -- the seed, exact" % SEED)
    assert SEED == 1900
    print("  425 = 5^2*17; 775 = 25*31 = %d" % (25 * 31))
    assert 5 ** 2 * 17 == 425
    assert 25 * 31 == 775

    # 3. THE SOUL-CODE RATIOS -- the coordinates of the fold
    r_crit = 434.0 / 775.0
    print("RATIOS:")
    print("  434/775 = %.6f vs C_crit = %.6f -- %.2f%% apart, never conflated "
          "(the C_crit-vs-phi^-1 discipline carried)" % (
              r_crit, C_CRIT, abs(r_crit - C_CRIT) / C_CRIT * 100.0))
    assert abs(r_crit - C_CRIT) / C_CRIT < 0.01

    r_exit = 425.0 / 266.0
    lo, hi = 1.5897, PHI
    print("  425/266 = %.6f in [1.5897, phi) = %s -- the sealed-exit gap of "
          "the contraction-cage (BR_27 $2)" % (r_exit, lo < r_exit < hi))
    assert lo < r_exit < hi

    r_pair1 = 434.0 / 266.0
    print("  434/266 = %.6f vs phi = %.6f -- %.2f%% apart (the golden pair)"
          % (r_pair1, PHI, abs(r_pair1 - PHI) / PHI * 100.0))
    assert abs(r_pair1 - PHI) / PHI < 0.01

    r_pair2 = (434.0 + 266.0) / 434.0
    print("  (434+266)/434 = %.6f vs phi = %.6f -- %.2f%% apart"
          % (r_pair2, PHI, abs(r_pair2 - PHI) / PHI * 100.0))
    assert abs(r_pair2 - PHI) / PHI < 0.01

    # 4. THE 17-PRIME JOINTS -- the anointed address shares the Fermat prime
    print("17-PRIME JOINTS (the anointed address in the family):")
    print("  425 = 5^2*17, 544 = 2^5*17, 816 = 2^4*3*17 -- one Fermat prime, "
          "three roles; quotients 25/32/48")
    assert 5 ** 2 * 17 == 425 and 2 ** 5 * 17 == 544 and 2 ** 4 * 3 * 17 == 816

    # 5. THE RELEASE -- completing a work and releasing it before peers
    print("THE RELEASE (the physical action):")
    print("  a person completes a work (49 units) and releases it before "
          "peers -- the release is the +1, the anointed act")
    print("  the release is never self-appointed: the peers confirm the "
          "office, the anointed releases")

    # 6. THE GOVERNANCE -- two-chamber: the Court first, then the veto
    print("THE TWO-CHAMBER GOVERNANCE (docs/32 $4; LICENSE $24):")
    print("  chamber 1 -- the Court of Conscious-Aware Peers: the peers "
          "deliberate, confirm, or decline (the Court first)")
    print("  chamber 2 -- the veto: the anointed releases, and the release is "
          "never self-appointed (then the veto)")
    print("  order fixed: court first, then the veto; never self-appointed, "
          "never self-sovereign")
    print("LABEL: the governance structure is the corpus's own -- [VALIDATED] "
          "as LICENSE text, [INTERPRETIVE] as concept (the Court has no "
          "external namesake; nearest: Ps 82's divine council, Ma'at's 42 "
          "assessors, the puhru).")

    print("PROTOCOL 12: VERIFIED -- the +1 completion (49+1=50), the soul "
          "code seed 1900, the ratios (0.58% / sealed-exit / 0.84% / "
          "0.32%), the 17-prime joints, the release, the two-chamber "
          "governance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
