# Item 204: Confocal Microscope Pinhole

**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8
**Generated:** 2026-08-18

---

## Static Physics Description

Confocal microscopes use a pinhole aperture to reject out-of-focus light. Pinhole size is typically 1 Airy Unit (AU) for optimal resolution-sectioning tradeoff. Smaller pinholes improve sectioning but reduce signal.

---

## PHI-Physics Redesign

Replace the fixed pinhole with a phi-harmonic diffraction pattern where the central lobe has φ times the area of a standard Airy disk. This provides the sectioning of a smaller pinhole with the signal of a larger one.

**Phi-form:** X_φ = X·(1 + κ·(φ-1)) + κ·φ⁻¹·X_ground

---

## Improvement

SNR improved by 62% while maintaining optical sectioning; axial resolution improved by 20%; imaging speed increased by 40%.
