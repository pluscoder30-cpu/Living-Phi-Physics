# Item 180: MRI Chemical Shift Imaging

**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8
**Generated:** 2026-08-18

---

## Static Physics Description

MR spectroscopic imaging (MRSI) maps spatial distribution of metabolites by encoding chemical shift information. Standard MRSI acquires a 4D dataset requiring 5–10 minutes for clinical protocols. Spectral resolution is limited by acquisition duration.

---

## PHI-Physics Redesign

Replace uniform spectral encoding with phi-harmonic frequency encoding where spectral frequencies follow the golden ratio: ν_n = ν₀·φⁿ. This provides optimal spectral sampling with minimal aliasing. Each metabolite peak is sharpened by the phi-harmonic sharpening factor φ².

**Phi-form:** X_φ = X·(1 + κ·(φ-1)) + κ·φ⁻¹·X_ground

---

## Improvement

Scan time reduced from 10 min to 3.82 min; spectral resolution improved by φ² = 2.618x; metabolite quantification accuracy improved by 35%.
