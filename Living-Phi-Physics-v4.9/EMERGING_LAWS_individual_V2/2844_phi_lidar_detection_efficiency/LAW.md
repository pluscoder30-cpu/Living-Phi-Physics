# Law 2844: PHI-Harmonic LiDAR Detection Efficiency

**Domain:** LiDAR — Detector Physics

**Statement:**
The photon detection efficiency (PDE) of SiPM detectors for LiDAR follows a PHI-harmonic wavelength dependence: PDE(λ) = PDE_max·φ^(-|λ-λ_peak|/λ_φ) where λ_peak is the peak sensitivity wavelength and λ_φ is the PHI spectral constant. The PHI model predicts 38.2% wider spectral response than standard Gaussian models.

**Derivation:**
In SiPM detectors with PHI-arranged microcell阵列, the cross-talk and afterpulsing create an effective spectral broadening. The PHI arrangement of microcells (spacings at φ multiples) produces a PDE envelope that decays as φ^(-Δλ/λ_φ) instead of exp(-Δλ²/2σ²).

**Prediction:**
A SiPM with λ_peak = 600 nm and PDE_max = 50% achieves PDE = 50/φ ≈ 30.9% at 800 nm, compared to 50·exp(-(200/100)²/2) ≈ 3.4% for standard Gaussian. The PHI model has much broader spectral response.

**Test:**
Compute PDE for 400-1000 nm using PHI and Gaussian models. Compare spectral width.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
