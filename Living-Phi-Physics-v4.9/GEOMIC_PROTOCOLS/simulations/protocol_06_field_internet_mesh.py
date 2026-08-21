#!/usr/bin/env python3
"""GEOMIC PROTOCOL 06 — THE FIELD INTERNET MESH PROTOCOL.

Law 205 + Law 189: the mesh is phi-resonance bridges between carriers
  - the phi-bridge: 1 + phi^-1 = phi = 1.6180339887 (full-coupling bridge,
                    C_mesh = 0)
  - the mesh factor: 1 + (phi-1)*(1-C_mesh) = 1.0618033989 at C_mesh = 0.9,
                    kappa = 1 (the prototypes' coupling — the raw overlap
                    phi-amplified by 6.18%)
  - the port resonance: 8165 = 816*10+5 ; 816 = 2^4*3*17 ; 8165 mod 816 = 5 ;
                    8165 mod 17 = 5 ; 8165 = 5*1633 = 15*544+5 ; 544 = 2^5*17
  - the carrier that never closes: phi^2*816 = 2136.316 (fractional 0.316 —
                    the golden-angle residue; 360/phi^2 = 137.5078 deg)
  - the mesh recursion: the broadcast's coherence through N nodes
                    C_{n+1} = phi^-1 + phi^-1*(C_n - phi^-1) from C_0 = 1:
                    C_1 = 1 - phi^-4 = 0.854102, C_10 = 0.621140 -> phi^-1,
                    audible above C_crit through every node

Pure standard library (math, sys). Canonical constants from 00_NUMBERS_INDEX.md.
Prints verification. Exit 0.
"""
import math
import sys

PHI = 1.618033988749895   # 00_NUMBERS_INDEX.md $2 (recomputed)
PHI_INV = PHI - 1.0       # 0.6180339887
C_CRIT = 0.563263         # 00_NUMBERS_INDEX.md $2 / Eq 2 — emergence threshold
CARRIER = 816             # 00_NUMBERS_INDEX.md $2 — the 816D carrier = 2^4*3*17
PORT = 8165               # the field internet's gateway port = 816*10+5
RELEASE = 544             # 00_NUMBERS_INDEX.md $2 — the release node = 2^5*17


def main():
    # 1. THE PHI-BRIDGE — 1 + phi^-1 = phi (the full-coupling bridge)
    bridge = 1.0 + PHI_INV
    print("PHI-BRIDGE: 1 + phi^-1 = %.10f  (phi = %.10f)" % (bridge, PHI))
    assert abs(bridge - PHI) < 1e-9

    # 2. THE MESH FACTOR — 1 + (phi-1)*(1-C_mesh) at C_mesh = 0.9, kappa = 1
    C_mesh = 0.9
    mesh_factor = 1.0 + (PHI - 1.0) * (1.0 - C_mesh)
    pct = (mesh_factor - 1.0) * 100.0
    print("MESH FACTOR: 1 + (phi-1)*(1-C_mesh) = %.10f  (C_mesh=0.9, "
          "kappa=1 — the raw overlap phi-amplified by %.2f%%)"
          % (mesh_factor, pct))
    assert abs(mesh_factor - 1.0618033989) < 1e-6
    assert abs(pct - 6.18) < 0.01

    # 3. THE PORT RESONANCE — 8165 = 816*10+5, the carrier's own number
    print("PORT: 8165 = 816*10+5 ; 816 = 2^4*3*17 = %d ; 544 = 2^5*17 = %d"
          % (2 ** 4 * 3 * 17, 2 ** 5 * 17))
    assert 2 ** 4 * 3 * 17 == CARRIER and 2 ** 5 * 17 == RELEASE
    assert PORT == CARRIER * 10 + 5
    assert PORT % CARRIER == 5 and PORT % 17 == 5
    assert PORT == 5 * 1633 and PORT == 15 * RELEASE + 5
    print("  checks: 8165 mod 816 = 5 ; 8165 mod 17 = 5 ; 8165 = 5*1633 "
          "= 15*544+5 — all pass")

    # 4. THE CARRIER THAT NEVER CLOSES — phi^2*816 = 2136.316, residue 0.316
    travel = PHI ** 2 * CARRIER
    frac = travel - math.floor(travel)
    print("NEVER CLOSES: phi^2*816 = %.6f (fractional residue %.3f — the "
          "golden-angle traversal; 360/phi^2 = %.4f deg never closes)"
          % (travel, frac, 360.0 / PHI ** 2))
    assert abs(travel - 2136.316) < 1e-2
    assert abs(frac - 0.316) < 0.005
    assert abs(360.0 / PHI ** 2 - 137.5078) < 1e-3

    # 5. THE MESH RECURSION — the broadcast's coherence through N nodes
    #    C_{n+1} = phi^-1 + phi^-1*(C_n - phi^-1), from C_0 = 1 (the sent
    #    packet): relaxes toward the phi-ground, audible above the gate
    C = 1.0
    C = PHI_INV + PHI_INV * (C - PHI_INV)       # node 1
    c1 = C
    print("MESH RECURSION: C_{n+1} = phi^-1 + phi^-1*(C_n - phi^-1), "
          "from C_0 = 1 (the sent packet):")
    print("  node  1: C = %.6f" % c1)
    for n in range(2, 11):
        C = PHI_INV + PHI_INV * (C - PHI_INV)
        print("  node %2d: C = %.6f" % (n, C))
        assert C >= C_CRIT
    c10 = C
    for _ in range(200):
        C = PHI_INV + PHI_INV * (C - PHI_INV)
    print("BROADCAST: C_1 = %.6f (1-phi^-4 = %.6f) ; C_10 = %.6f ; fixed "
          "point = %.10f (the phi-ground, never below, audible above the "
          "gate through all N nodes)" % (c1, 1.0 - PHI_INV ** 4, c10, C))
    assert abs(c1 - (1.0 - PHI_INV ** 4)) < 1e-6
    assert abs(c10 - 0.621140) < 1e-3
    assert abs(C - PHI_INV) < 1e-6

    print("PROTOCOL 06: VERIFIED — the phi-bridge 1+phi^-1 = phi; the mesh "
          "factor 1.061803; the port 8165 = 816*10+5; the carrier that "
          "never closes (residue 0.316); the broadcast to the phi-ground.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
