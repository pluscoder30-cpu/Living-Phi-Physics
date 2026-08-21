# Item 209: Nuclear Magnetic Resonance Probe

**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8
**Generated:** 2026-08-18

---

## Static Physics Description

NMR probes house the sample and RF coil in the magnet bore. Standard probes use single-coil or crossed-coil designs with Q-factors of 50–200. Probe sensitivity limited by coil filling factor and noise. Cryoprobes improve SNR by 3–4x.

---

## PHI-Physics Redesign

Design the NMR probe coil with phi-harmonic winding geometry where turns follow the golden spiral. The phi-coil achieves optimal filling factor and reduced noise through self-similar current distribution.

**Phi-form:** X_φ = X·(1 + κ·(φ-1)) + κ·φ⁻¹·X_ground

---

## Improvement

SNR improved by 2.6x; sample throughput increased by 40%; probe tuning time reduced by 50%.
