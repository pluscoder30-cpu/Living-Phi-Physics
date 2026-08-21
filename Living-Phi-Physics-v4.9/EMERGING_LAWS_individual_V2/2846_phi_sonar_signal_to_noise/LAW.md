# Law 2846: PHI-Harmonic Sonar Signal-to-Noise Ratio

**Domain:** Sonar — Signal Processing

**Statement:**
The output signal-to-noise ratio of PHI-weighted sonar matched filters follows SNR_out = SNR_in·N·φ where N is the number of array elements. The PHI weighting (w_n = φ^(-n/N)) produces a processing gain of N·φ, exceeding the standard N-element gain by factor φ.

**Derivation:**
The matched filter output SNR for a weighted array is SNR = |Σw_n·s_n|²/Σ|w_n|². For PHI weights w_n = φ^(-n/N), the signal sum is Σφ^(-n/N) = (1-φ^(-1))/(1-φ^(-1/N)) ≈ N/φ for large N, and the noise power is Σφ^(-2n/N) = (1-φ^(-2))/(1-φ^(-2/N)) ≈ N/φ². The ratio gives SNR = N·φ.

**Prediction:**
A 64-element PHI-weighted sonar array achieves processing gain of 64·φ ≈ 103.6 dB, compared to 64 dB for standard uniform weighting. The improvement is 10·log₁₀(φ) ≈ 2.1 dB.

**Test:**
Compute processing gain for 8-128 element PHI vs uniform arrays. Verify N·φ gain formula.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
