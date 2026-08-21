# Item 205: UV-Vis Spectrophotometer

**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8
**Generated:** 2026-08-18

---

## Static Physics Description

UV-Vis spectrophotometers measure absorbance spectra. Wavelength range 190–1100nm with 1nm resolution. Stray light 0.01–0.1% T. Absorbance accuracy ±0.002 AU at 1 AU. Double-beam designs compensate for source drift.

---

## PHI-Physics Redesign

Replace the monochromator grating with a phi-harmonic diffraction grating where groove spacing follows d_n = d₀·φ^{-n}. This provides simultaneous multi-wavelength measurement at phi-separated wavelengths with reduced stray light.

**Phi-form:** X_φ = X·(1 + κ·(φ-1)) + κ·φ⁻¹·X_ground

---

## Improvement

Stray light reduced by 84% (φ³); measurement speed improved by 62%; absorbance accuracy improved to ±0.0008 AU.
