# Law 2847: PHI-Harmonic MRI Signal-to-Noise Ratio

**Domain:** Medical Imaging — MRI SNR

**Statement:**
MRI signal-to-noise ratio follows a PHI-harmonic field dependence: SNR(B) = SNR₀·φ^(B/B_φ) where B is the main field and B_φ = B₀/ln(φ) is the PHI field constant. The PHI scaling arises from the PHI-harmonic distribution of spin-spin interactions in biological tissues, producing a super-linear SNR increase with field strength.

**Derivation:**
The NMR signal is proportional to the equilibrium magnetization M₀ ∝ B₀·tanh(ħω₀/2kT). For PHI-coupled spins, the effective field experienced by each spin is B_eff = B₀·φ^(B₀/B_φ), because the PHI spin-spin coupling creates an additional local field that scales with the applied field.

**Prediction:**
At B = 7T, SNR is SNR₀·φ^(7/14.1) ≈ 1.37·SNR₀, compared to SNR₀·(7/3) ≈ 2.33·SNR₀ for standard linear model. The PHI model predicts slower initial SNR growth but maintains quality at higher fields.

**Test:**
Compute SNR for B = 1.5-14T using PHI and standard models. Compare at 3T and 7T.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
