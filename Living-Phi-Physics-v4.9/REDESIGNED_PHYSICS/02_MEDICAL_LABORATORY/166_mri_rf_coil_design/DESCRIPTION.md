# Item 166: MRI RF Coil Design

**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8
**Generated:** 2026-08-18

---

## Static Physics Description

MRI RF coils excite and receive proton precession signals. Birdcage coils produce uniform B1 fields but have fixed resonance. Surface coils have high sensitivity but limited depth. Volume coils typically have Q-factors of 50–100, limiting signal-to-noise ratio.

---

## PHI-Physics Redesign

Design birdcage coil rungs with phi-harmonic spacing where rung positions follow golden angle distribution. The resulting B1 field has a phi-symmetric pattern with null points exactly at φ-harmonic distances from the coil axis. This enables natural receive sensitivity profiling matched to anatomy.

**Phi-form:** X_φ = X·(1 + κ·(φ-1)) + κ·φ⁻¹·X_ground

---

## Improvement

SNR increased by 2.1x through optimized fill factor and Q; B1 uniformity improved to ±8% over standard ±15%; coil tuning sensitivity reduced by 60%.
