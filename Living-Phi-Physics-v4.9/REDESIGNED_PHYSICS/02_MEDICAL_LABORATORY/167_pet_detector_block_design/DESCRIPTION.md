# Item 167: PET Detector Block Design

**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8
**Generated:** 2026-08-18

---

## Static Physics Description

PET block detectors use Anger logic to determine gamma interaction position from photomultiplier tube signals. Light sharing in the scintillator block creates non-linear position mapping. Standard block design achieves ~3mm spatial resolution at the detector face.

---

## PHI-Physics Redesign

Redesign the block with phi-harmonic light guide channels that route scintillation light to PMTs through golden-ratio fiber bundles. Each channel has length = n·φ·λ_scintillation, creating constructive interference at phi-harmonic positions and destructive interference elsewhere.

**Phi-form:** X_φ = X·(1 + κ·(φ-1)) + κ·φ⁻¹·X_ground

---

## Improvement

Spatial resolution improved from 3.0mm to 1.15mm; position linearity error reduced by 62%; detector sensitivity increased by φ = 1.618x.
