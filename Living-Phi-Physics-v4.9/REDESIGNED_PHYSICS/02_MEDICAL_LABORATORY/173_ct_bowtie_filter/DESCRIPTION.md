# Item 173: CT Bowtie Filter

**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.8
**Generated:** 2026-08-18

---

## Static Physics Description

CT bowtie filters shape the X-ray beam to compensate for patient attenuation variation across the field of view. Standard bowtie filters use aluminum or copper with a fixed geometry matched to an average patient. Non-uniform patient sizes cause dose inefficiency.

---

## PHI-Physics Redesign

Design a phi-curve bowtie filter where the thickness profile follows T(r) = T₀·(1 - (r/R)²)^{φ}. The phi-exponent creates optimal beam hardening correction because the filter attenuation matches the expected patient attenuation at φ-harmonic radial positions.

**Phi-form:** X_φ = X·(1 + κ·(φ-1)) + κ·φ⁻¹·X_ground

---

## Improvement

Beam hardening artifacts reduced by 38%; dose uniformity across FOV improved by 61.8%; patient size adaptation range increased by factor φ.
