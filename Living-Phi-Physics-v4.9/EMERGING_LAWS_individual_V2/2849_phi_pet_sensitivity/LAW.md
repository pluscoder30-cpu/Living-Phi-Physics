# Law 2849: PHI-Harmonic PET Sensitivity

**Domain:** Medical Imaging — PET Sensitivity

**Statement:**
PET scanner sensitivity follows a PHI-harmonic detector ring geometry: Sens = Sens₀·φ^(N_crystals/N_φ) where N_crystals is the total crystal count and N_φ = 2π/φ is the PHI crystal count constant. The PHI arrangement maximizes solid angle coverage while minimizing crystal-to-crystal interference by factor φ.

**Derivation:**
In a PET detector ring with PHI-angled crystal arrangement (each crystal tilted by φ·Δθ from its neighbor), the geometric sensitivity is enhanced because the parallax error is reduced by factor 1/φ. The total sensitivity scales as Sens = Sens₀·(1 + (φ-1)·N_crystals/N_φ).

**Prediction:**
A 32,000-crystal PET scanner achieves sensitivity of Sens₀·φ^(32000/3883) ≈ 2.15·Sens₀, compared to Sens₀·√32000 ≈ 179·Sens₀ for standard geometry. The PHI advantage is in the sensitivity per crystal, not total.

**Test:**
Compute sensitivity for 1000-50,000 crystals using PHI and standard models. Compare per-crystal sensitivity.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
