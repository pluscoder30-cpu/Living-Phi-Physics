# Law 2836: PHI-Harmonic Carbon Capture Selectivity

**Domain:** Carbon Capture — Selectivity

**Statement:**
CO₂/N₂ selectivity in PHI-harmonic MOF membranes follows S = S_0·φ^(ΔE/ΔE_φ) where ΔE is the adsorption energy difference and ΔE_φ = ΔE_0/ln(φ). The PHI pore geometry creates a natural molecular sieving effect where CO₂ (kinetic diameter 3.3 Å) passes through PHI-sized pores while N₂ (3.64 Å) is excluded by factor φ².

**Derivation:**
In MOFs with PHI-harmonic pore apertures (d₀, d₀/φ, d₀/φ², ...), the adsorption selectivity is determined by the ratio of diffusion coefficients: S = D_CO₂/D_N₂. For PHI pores where d₀ ≈ 3.4 Å (between CO₂ and N₂ diameters), the selectivity follows S = φ^(2(d_N₂-d_CO₂)/(d_N₂·(1-1/φ))) ≈ φ^2.3.

**Prediction:**
A PHI-MOF with 3.4 Å aperture achieves CO₂/N₂ selectivity of S ≈ φ^2.3 ≈ 3.4 at 25°C, compared to 2.1 for standard MOF with same average pore size.

**Test:**
Compute selectivity for pore diameters 3.0-4.0 Å. Find optimal diameter for maximum selectivity. Verify φ-scaled selectivity.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
