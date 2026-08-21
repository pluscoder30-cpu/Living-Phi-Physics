# Law 2845: PHI-Harmonic Radar Cross Section

**Domain:** Radar — Target Signature

**Statement:**
The radar cross section (RCS) of PHI-geometric targets follows σ(θ) = σ₀·φ^(2cos²θ) where θ is the aspect angle. PHI-shaped targets (e.g., golden rectangles, PHI spirals) exhibit RCS patterns with main lobe enhancement by factor φ² at broadside and nulls at PHI-spaced angles.

**Derivation:**
For a flat plate with PHI-modulated edges (edge segments at φ-spaced intervals), the scattered field is the sum of contributions from each segment: E_s = E₀·Σφ^(-n)·exp(jkn·d₀·sinθ). The magnitude squared gives σ ∝ |Σφ^(-n)·exp(jkn·d₀·sinθ)|², which peaks at θ = 0 with gain φ²/(1-1/φ²).

**Prediction:**
A 1 m² golden rectangle target has broadside RCS of σ₀·φ² ≈ 2.618σ₀, with first null at θ = arcsin(λ/(2d₀·φ)) ≈ 30° for d₀ = λ.

**Test:**
Compute RCS pattern for PHI-geometric vs rectangular target. Compare broadside RCS and null positions.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
