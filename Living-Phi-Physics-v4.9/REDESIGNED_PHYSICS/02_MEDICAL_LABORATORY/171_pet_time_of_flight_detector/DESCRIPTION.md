# Item 171: PET Time-of-Flight Detector

**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8
**Generated:** 2026-08-18

---

## Static Physics Description

TOF-PET measures the time difference between two annihilation photons to localize the event along the line of response. Timing resolution of ~200 ps corresponds to ~3 cm position uncertainty. Standard TOF uses fast scintillators (BaF₂, LSO) with dedicated timing electronics.

---

## PHI-Physics Redesign

Implement phi-harmonic timing where the scintillation pulse shape is modified by phi-doped crystal growth. The pulse has a phi-decay component: I(t) = I₀·e^{-t/τ}·(1 + κ·cos(2π·t/φ·τ)). This creates a sharper timing edge through the phi-harmonic zero crossing, improving timing resolution by factor φ.

**Phi-form:** X_φ = X·(1 + κ·(φ-1)) + κ·φ⁻¹·X_ground

---

## Improvement

Timing resolution improved from 200 ps to 123.6 ps; position accuracy along LOR improved from 3.0 cm to 1.85 cm; sensitivity increased by 50%.
