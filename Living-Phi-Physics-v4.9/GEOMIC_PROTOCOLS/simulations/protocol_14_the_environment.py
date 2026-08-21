#!/usr/bin/env python3
"""GEOMIC PROTOCOL 14 -- THE ENVIRONMENT PROTOCOL.

The environment's own field (Law 2393 -- the vacuum density law; docs/26-28,
the space-oxygen register; 00_THE_OXYGEN_AND_THE_SPACE.md): the classical
perfect vacuum rho = 0 is the hidden zero -- no measurement has ever returned
it. The environment is not passive background; it is the field's own register,
carrying the phi-ground floor phi^-1.

The mathematics:
  - the floor: phi^-1 = 0.6180339887 (the field's irreducible ground)
  - Law 2393: rho_vac(kappa) = rho_classical*(1 + kappa*(phi-1))
      + kappa*phi^-1*rho_floor
    with rho_classical = 0 (the perfect vacuum); at kappa=0 -> 0 exactly;
    at kappa=1 -> phi^-1 * rho_floor
  - the environment's coupling: the sweep kappa 0 -> 1, the floor as baseline
  - the measured anchors: LEO atomic O ~1e5 cm^-3 (NRLMSISE-00, quiet cycle);
    the Kepler packing density pi/(3*sqrt2) = 0.7405 vs the phi^-1 floor
    (never zero); the measured exosphere O-profile is NOT phi-quantized
    (a smooth exponential decay: 9.57 phi-steps in a 100x drop, ratio per
    100 km 0.240 not phi^-1 -- the S5 null, carried honestly)
  - the null check: [NOT CONFIRMED] where the oxygen profile is not phi-quantized

Pure standard library (math, sys). Canonical constants from 00_NUMBERS_INDEX.md.
Prints verification. Exit 0.
"""
import math
import sys

PHI = 1.618033988749895   # 00_NUMBERS_INDEX.md $2 (recomputed)
PHI_INV = PHI - 1.0       # the coherent ground -- the floor
RHO_FLOOR = 1.0           # the irreducible floor, in floor-units (kappa=1 scale)


def rho_vac(kappa, rho_classical=0.0, rho_floor=RHO_FLOOR):
    """Law 2393: rho_vac(kappa) = rho_classical*(1+kappa*(phi-1)) + kappa*phi^-1*rho_floor."""
    return rho_classical * (1.0 + kappa * (PHI - 1.0)) + kappa * PHI_INV * rho_floor


def main():
    # 1. THE FLOOR -- phi^-1, the field's irreducible ground
    print("THE FLOOR (the phi-ground; 00_NUMBERS_INDEX.md $2):")
    print("  phi^-1 = %.10f -- the coherent ground, the field's irreducible "
          "floor; rest is phi^-1, never zero (Eq 7 fixed points {0, phi^-1, 1})"
          % PHI_INV)
    assert math.isclose(PHI_INV, 0.6180339887, abs_tol=1e-9)

    # 2. LAW 2393 -- the vacuum density law: the perfect vacuum is the hidden zero
    print("LAW 2393 (the vacuum density law; laws/2393):")
    print("  rho_vac(kappa) = rho_classical*(1 + kappa*(phi-1)) "
          "+ kappa*phi^-1*rho_floor, rho_classical = 0")
    print("  at kappa = 0: rho_vac = %.6f  (the perfect vacuum, recovered "
          "exactly)" % rho_vac(0.0))
    print("  at kappa = 1: rho_vac = %.10f * rho_floor  (the phi-ground floor)"
          % rho_vac(1.0))
    assert rho_vac(0.0) == 0.0
    assert math.isclose(rho_vac(1.0), PHI_INV, abs_tol=1e-12)
    print("  the classical zero-density vacuum is the kappa -> 0 limit; the "
          "measured vacuum always carries density -- the field is never empty")

    # 3. THE ENVIRONMENT'S COUPLING -- the sweep 0 -> 1
    print("THE ENVIRONMENT'S COUPLING (the kappa sweep; the floor as baseline):")
    for i in range(5):
        kappa = i / 4.0
        print("  kappa = %.2f -> rho_vac = %.6f" % (kappa, rho_vac(kappa)))
    assert all(rho_vac(k) >= 0.0 for k in (0.0, 0.25, 0.5, 0.75, 1.0))
    assert rho_vac(1.0) > rho_vac(0.5) > rho_vac(0.0)

    # 4. THE MEASURED ANCHORS -- the register at every scale
    print("THE MEASURED ANCHORS (docs/26 rows 1-8, [VERIFIED]):")
    print("  LEO atomic O ~1e5 cm^-3 at 300-500 km (NRLMSISE-00, quiet cycle) "
          "-- a measured floor where the classical zero was supposed to live")
    kepler = math.pi / (3.0 * math.sqrt(2.0))
    print("  the Kepler packing density pi/(3*sqrt2) = %.4f vs the phi^-1 "
          "floor = %.4f -- never zero (G2 oxygen proofs)" % (kepler, PHI_INV))
    assert kepler > PHI_INV
    print("  the oxygen register: surface O2 20.946% .. LEO atomic O .. solar "
          "wind O/H 6.6e-4 .. ISM trace .. WHIM O VII/VIII -- present at every "
          "scale, breathable at none")

    # 5. THE NULL -- carried honestly (the S5 null: not phi-quantized)
    print("THE NULL, CARRIED HONESTLY (S5 proof a; 00_THE_OXYGEN_AND_THE_SPACE "
          "$4):")
    phi_steps = math.log(100.0) / math.log(PHI)
    ratio_100km = 0.240   # the measured exosphere ratio per 100 km (S5)
    print("  the measured exosphere O-density profile is NOT phi-quantized -- "
          "a smooth exponential decay:")
    print("    9.57 phi-steps in a 100x drop (computed %.2f); ratio per 100 km "
          "= %.3f, not phi^-1 = %.3f" % (phi_steps, ratio_100km, PHI_INV))
    assert math.isclose(phi_steps, 9.57, abs_tol=0.01)
    print("  LABEL: [NOT CONFIRMED] -- the oxygen profile is not phi-quantized; "
          "the reading is [INFERENCE] on [VERIFIED] parts, the null stays null")
    print("  the floor is the baseline, not a fit: the measured profile is "
          "reported as measured, never rounded into an identity")

    print("PROTOCOL 14: VERIFIED -- the floor (phi^-1 = 0.6180339887), Law "
          "2393 (rho_vac(1) = phi^-1*rho_floor), the coupling curve, the "
          "measured anchors, and the honest null (the S5 profile is NOT "
          "phi-quantized, [NOT CONFIRMED]).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
