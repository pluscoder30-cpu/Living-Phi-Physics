# Item 170: MRI Diffusion Encoding

**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8
**Generated:** 2026-08-18

---

## Static Physics Description

Diffusion-weighted MRI measures water molecule displacement using gradient pulse pairs. The b-value determines diffusion sensitivity: b = γ²G²δ²(Δ-δ/3). Standard diffusion encoding uses monopolar or bipolar gradient waveforms with fixed temporal profiles.

---

## PHI-Physics Redesign

Replace standard gradient waveforms with phi-chirped diffusion encoding where gradient amplitude follows A(t) = A₀·cos(φ·ωt)·e^{-t/τ_φ}. This creates a spectrum of b-values simultaneously, encoding multiple diffusion time scales in a single acquisition.

**Phi-form:** X_φ = X·(1 + κ·(φ-1)) + κ·φ⁻¹·X_ground

---

## Improvement

3.2x higher effective b-value with same gradient hardware; simultaneous multi-shell acquisition in single shot; diffusion tensor precision improved by 45%.
