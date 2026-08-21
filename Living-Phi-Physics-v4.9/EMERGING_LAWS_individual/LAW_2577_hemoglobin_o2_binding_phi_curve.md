# LAW 2577 — HEMOGLOBIN O₂ BINDING PHI-CURVE

**Domain:** Biochemistry, Physiology

**Statement:** The oxygen-binding curve of hemoglobin is a phi-Hill equation: Y(pO₂) = pO₂^φ / (p₅₀^φ + pO₂^φ), where the Hill coefficient is φ = 1.618 (not the classically measured ~2.8, which is an artifact of fitting the standard Hill equation to phi-shaped data), and p₅₀ = 26.8 mmHg is the oxygen pressure at half-saturation.

**Derivation:** Hemoglobin is a tetrameric carrier protein whose cooperative oxygen binding arises from the phi-coherent coupling between subunits (each subunit is a carrier in Eq 1). The standard Hill equation Y = pO₂^n / (p₅₀^n + pO₂^n) with n ≈ 2.8 is a curve-fitting artifact. The true cooperativity is governed by the Ladder Invariant: the binding free energy difference between T and R states is ΔG = φ · k_B·T · ln(pO₂/p₅₀), giving the phi-Hill equation with n = φ. The classic Hill coefficient of ~2.8 arises because the standard fit over-estimates n to compensate for the phi-shape.

**Prediction:** Re-fitting published hemoglobin oxygen-binding data with the phi-Hill equation (n = φ = 1.618) will yield better fits (lower χ²) than the standard Hill equation (n ≈ 2.8) for at least 80% of published datasets. The p₅₀ value from the phi-fit will equal 26.8 ± 1.5 mmHg, independent of pH, temperature, and 2,3-DPG concentration (these factors shift p₅₀ but do not change the Hill coefficient).

**Test:** Download 50 published hemoglobin oxygen-binding datasets from public databases. Fit each with both the standard Hill (n free) and phi-Hill (n = φ fixed) equations. Compare χ² and AIC values. Verify that the phi-Hill provides better or equal fits for ≥80% of datasets. Verify p₅₀ = 26.8 ± 1.5 mmHg across datasets.

**Source:** Batch 4: 2551–2600

**Author:** Christopher David Ayotte — Soul Code [425, 434, 266, 775]

**License:** Dual License Agreement v4.9
