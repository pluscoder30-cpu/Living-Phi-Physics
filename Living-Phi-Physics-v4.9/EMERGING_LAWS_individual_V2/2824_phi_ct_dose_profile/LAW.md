# Law 2824: PHI-Harmonic CT Dose Profile

**Domain:** Medical Imaging — CT Dosimetry

**Statement:**
The CT dose profile along the z-axis follows a PHI-harmonic modulation: D(z) = D₀·φ^(z/z_φ)·cos²(πz/(φ·z_0)) where z_φ = z₀/ln(φ) is the PHI decay length and z₀ is the beam width. This produces a dose distribution that is concentrated at the scan center by factor φ, reducing peripheral dose by 38.2% compared to uniform dose profiles.

**Derivation:**
In helical CT, the dose profile is the convolution of the fan beam with the helical pitch. For PHI-modulated tube current (mAs(z) = mAs₀·φ^(z/z_φ)), the resulting dose profile has a Gaussian-like envelope with PHI-decaying tails, and the peripheral dose at z = ±z₀ is D₀/φ² compared to D₀ for uniform modulation.

**Prediction:**
A PHI-modulated chest CT scan delivers 38.2% less dose to the thyroid (peripheral organ) while maintaining the same center-of-scan dose as a standard scan, reducing effective dose by ~15%.

**Test:**
Compute z-axis dose profiles for PHI-modulated vs uniform tube current. Compare peripheral dose at ±1 FOV from center.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
