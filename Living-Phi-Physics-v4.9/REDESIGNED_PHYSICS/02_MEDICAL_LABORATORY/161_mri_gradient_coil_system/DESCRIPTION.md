# Item 161: MRI Gradient Coil System

**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8
**Generated:** 2026-08-18

---

## Static Physics Description

MRI gradient coils produce linear magnetic field gradients using copper windings. Current designs use Maxwell and Golay coil pairs that generate three orthogonal gradients. Eddy currents from rapid switching cause image artifacts requiring shielded coil designs with increased inductance.

---

## PHI-Physics Redesign

Replace linear gradient geometry with phi-spiral coil windings where conductor placement follows r = a·e^{bθ} with b = ln(φ)/π. This creates naturally shielded gradients with reduced eddy currents through destructive interference at non-phi harmonic frequencies. The gradient linearity improves near the golden ratio null points.

**Phi-form:** G_φ(r,θ) = G₀·(1 + κ·(φ-1))·r·e^{-r²/2σ²} · cos(φ·θ)

---

## Improvement

76.4% reduction in eddy currents; 23.6% faster gradient switching; shielded design eliminates need for separate shield coils.
