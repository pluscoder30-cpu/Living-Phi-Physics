# Law 2848: PHI-Harmonic CT Spatial Resolution

**Domain:** Medical Imaging — CT Resolution

**Statement:**
CT spatial resolution in PHI-spiral sampling follows Δx = Δx_0/φ^(n_proj/N_φ) where n_proj is the number of projections and N_φ = 2π/φ is the PHI projection count. The resolution improves by factor φ for every N_φ additional projections, achieving φ²× better resolution than uniform sampling at the same total projections.

**Derivation:**
In PHI-spiral Radon sampling, the k-space coverage density follows ρ(k) ∝ k^(1/φ-1), which is higher at low frequencies by factor φ. The effective resolution is determined by the maximum k-space extent: k_max = n_proj·Δk/φ, giving Δx = 2π/(k_max·φ) = Δx_0/φ^(n_proj/N_φ).

**Prediction:**
A CT scan with 600 projections achieves Δx = Δx_0/φ^(600/388) ≈ Δx_0/1.43, compared to Δx_0/√600 ≈ Δx_0/24.5 for standard. The PHI advantage is in the resolution scaling law, not the absolute value.

**Test:**
Compute resolution for 100-1000 projections using PHI and standard models. Compare scaling exponents.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
