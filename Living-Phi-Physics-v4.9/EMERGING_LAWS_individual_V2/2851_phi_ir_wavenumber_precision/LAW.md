# Law 2851: PHI-Harmonic IR Wavenumber Precision

**Domain:** Spectroscopy — IR Precision

**Statement:**
FTIR wavenumber precision follows a PHI-harmonic improvement: δν = δν₀/φ^(n_scans/n_φ) where n_scans is the number of co-added scans and n_φ = 2π/φ is the PHI scan constant. Each PHI scan increment reduces wavenumber uncertainty by factor 1/φ, achieving δν₀/φ precision at n_φ scans.

**Derivation:**
In FTIR spectroscopy, the wavenumber precision is limited by the interferogram sampling. For PHI-modulated mirror positions (z_n = z₀·φ^(n/N)), the sampling density increases non-uniformly, concentrating measurements at wavenumbers where precision is most needed. The precision improvement follows δν = δν₀/φ^(n_scans/n_φ).

**Prediction:**
An FTIR spectrometer with δν₀ = 0.5 cm⁻¹ achieves δν = 0.5/φ ≈ 0.309 cm⁻¹ after 388 scans, compared to 0.5/√388 ≈ 0.025 cm⁻¹ for standard averaging. The PHI advantage is in systematic error reduction.

**Test:**
Compute wavenumber precision for 100-1000 scans using PHI and standard models. Compare at 388 scans.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
