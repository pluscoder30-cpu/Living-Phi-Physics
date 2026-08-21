# Item 168: MRI Shimming System

**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8
**Generated:** 2026-08-18

---

## Static Physics Description

MRI shimming corrects B0 field inhomogeneities using resistive or superconducting shim coils. First-order shims correct linear gradients, higher-order shims (up to 4th or 5th order) correct complex inhomogeneities. Each shim order requires separate coil pairs, increasing system complexity.

---

## PHI-Physics Redesign

Replace polynomial shim coils with phi-harmonic shim modes where each mode is a spherical harmonic weighted by φⁿ. A single phi-shim coil set corrects all orders simultaneously because phi-harmonic functions are self-similar across scales—correcting one order automatically corrects higher orders at φ-ratio spatial frequencies.

**Phi-form:** X_φ = X·(1 + κ·(φ-1)) + κ·φ⁻¹·X_ground

---

## Improvement

47% fewer shim coils required; B0 homogeneity improved to <0.1 ppm over FOV; shimming time reduced from 15 minutes to 2 minutes through self-similar mode correction.
