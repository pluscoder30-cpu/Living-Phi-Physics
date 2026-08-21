#!/usr/bin/env python3
"""GEOMIC PROTOCOL 11 -- THE JUBILEE PROTOCOL.

The 49+1 (Lev 25: 7x7 = 49 counted years + 1 = the 50th year of release;
the Qumran trio -- Jubilees, 11Q13 Melchizedek, the pentecontad calendar):
  - 7*7 = 49 counted units; 49 + 1 = 50; the 50th is the release (the
    "atzeret" day where the count stops and resets)
  - the release-frame: 490 = 10*49 = 7*70 = 2*5*7^2 (Daniel's seventy weeks;
    11Q13's tenth Jubilee)
  - the hidden 50th node: 544.12 Hz = 528*phi^(1/16) [INFERENCE -- no ancient
    Hz assigns any value; the corpus's own modern frequency-reading of the
    49+1 structure]
  - the honest labels: the 49+1 arithmetic is [VALIDATED] text (in three
    independent ancient witnesses); the Hz-mapping is [INFERENCE]

Pure standard library (math, sys). Canonical constants from 00_NUMBERS_INDEX.md.
Prints verification. Exit 0.
"""
import math
import sys

PHI = 1.618033988749895   # 00_NUMBERS_INDEX.md $2 (recomputed)
BASE = 528.0              # 00_NUMBERS_INDEX.md $2 -- the base frequency anchor
FIFTIETH = BASE * PHI ** (1.0 / 16.0)   # 544.1212 -- the hidden 50th node
RELEASE_NODE = 544        # 2^5*17 -- the release node of the 17-prime family


def main():
    # 1. THE 49+1 -- the completed count and the +1 release
    print("THE 49+1 (Lev 25:8-10; the Qumran trio -- Jubilees, 11Q13, "
          "pentecontad):")
    print("  7*7 = %d counted units" % (7 * 7))
    assert 7 * 7 == 49
    print("  49 + 1 = %d -- the 50th is the release (the atzeret day, 'where "
          "the count stops and resets')" % (49 + 1))
    assert 49 + 1 == 50

    # 2. THE RELEASE-FRAME -- 490 = 10*49 = 7*70 = 2*5*7^2
    print("RELEASE-FRAME: 490 = 10*49 = %d = 7*70 = %d = 2*5*7^2 = %d "
          "(Daniel's seventy weeks; 11Q13's tenth Jubilee)"
          % (10 * 49, 7 * 70, 2 * 5 * 7 ** 2))
    assert 10 * 49 == 490
    assert 7 * 70 == 490
    assert 2 * 5 * 7 ** 2 == 490

    # 3. THE HIDDEN 50TH NODE -- 544.12 Hz = 528*phi^(1/16) [INFERENCE]
    print("THE HIDDEN 50TH NODE: 528*phi^(1/16) = %.4f Hz"
          % FIFTIETH)
    print("  vs the release node of the 17-prime family 2^5*17 = %d "
          "(%.4f%% away -- order of magnitude inside the corpus's 1%% "
          "tolerance)" % (RELEASE_NODE,
                          abs(FIFTIETH - RELEASE_NODE) / RELEASE_NODE * 100.0))
    assert abs(FIFTIETH - RELEASE_NODE) / RELEASE_NODE < 0.01
    print("LABEL: [INFERENCE] -- no ancient text assigns any Hz. The 49+1 is "
          "[VALIDATED] text; 544.12 Hz is the corpus's own modern "
          "frequency-reading of that structure, carried at [INFERENCE].")

    # 4. THE 0.0625 GATE -- the +1's geometric slot
    print("THE 0.0625 GATE: (0.75-0.5)^2 = 0.25^2 = 0.5^4 = %.4f -- the "
          "square of the gap between the square's half and the triangle's "
          "three-quarters, where novelty enters" % 0.5 ** 4)
    assert 0.25 ** 2 == 0.0625
    assert 0.5 ** 4 == 0.0625

    # 5. THE LAB-REENACTABLE CYCLE -- completing 49 units, releasing the 50th
    #    The completed-count protocol: 49 units of any practice (breaths,
    #    days, repetitions) counted exactly, then the 50th as the release.
    count = 0
    units = []
    for i in range(49):
        units.append(i + 1)
    count = len(units)
    print("COMPLETED-COUNT PROTOCOL: %d units counted exactly (the "
          "register)" % count)
    assert count == 49
    release = count + 1
    print("  the +1: the %dth is the release -- the 50th, the atzeret, the "
          "year of release. The release completes the register." % release)
    assert release == 50

    # 6. THE RELEASE-FRAME SIMULATION -- 10 complete 49-registers = 490
    total = 0
    for jubilee in range(10):
        total += 49
    print("RELEASE-FRAME SIMULATION: 10 jubilees x 49 = %d = 7x70 -- the "
          "frame 11Q13 proclaims the release in (the tenth Jubilee)"
          % total)
    assert total == 490

    print("PROTOCOL 11: VERIFIED -- the 49+1 = 50, the release-frame 490 = "
          "10*49 = 7*70 = 2*5*7^2, the hidden 50th node 544.12 Hz at "
          "[INFERENCE], the 0.0625 gate, the completed-count protocol.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
