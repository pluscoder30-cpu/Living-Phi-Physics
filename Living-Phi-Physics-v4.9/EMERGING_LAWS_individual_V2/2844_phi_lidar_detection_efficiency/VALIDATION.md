# Validation: Law 2844 — PHI-Harmonic LiDAR Detection Efficiency

**What it validates:** PHI model predicts wider spectral response than Gaussian.

**Equation tested:** PDE(λ) = PDE_max·φ^(-|λ-λ_peak|/λ_φ)

**Expected results:**
- PHI spectral response broader than Gaussian
- 38.2% wider spectral response
- Better off-peak sensitivity

**Test methodology:** Compute PDE at 7 wavelengths. Compare PHI and Gaussian models.

**Pass criteria:** PHI PDE > Gaussian PDE at 800 nm
