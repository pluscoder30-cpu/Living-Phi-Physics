# Item 172: MRI Surface Coil Array

**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8
**Generated:** 2026-08-18

---

## Static Physics Description

MRI surface coil arrays use multiple small coils placed close to the anatomy for high SNR. Elements are decoupled using overlapping, capacitive networks, or low-input-impedance preamps. Standard arrays have 8–32 elements with uniform overlap.

---

## PHI-Physics Redesign

Arrange surface coil elements in a phi-spiral pattern where element overlap follows the golden ratio. Decoupling is achieved naturally because phi-separated coils have minimal mutual inductance. The coil array sensitivity profile follows the consciousness field: S(r) = S₀·(1 + κ·(φ-1))·e^{-r²/2σ²_φ}.

**Phi-form:** X_φ = X·(1 + κ·(φ-1)) + κ·φ⁻¹·X_ground

---

## Improvement

SNR improved by 48% through optimized fill factor and reduced noise correlation; nearest-neighbor decoupling improved by 62%.
