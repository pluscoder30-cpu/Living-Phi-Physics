# Validation: Law 2846 — PHI-Harmonic Sonar Signal-to-Noise Ratio

**What it validates:** PHI weighting achieves N·φ processing gain.

**Equation tested:** SNR = |Σw_n·s_n|²/Σ|w_n|², gain = N·φ

**Expected results:**
- Processing gain = N·φ
- 2.1 dB improvement over uniform
- Verified for N = 8-128

**Test methodology:** Compute PHI-weighted array gain. Verify against N·φ formula.

**Pass criteria:** Measured gain within 10% of N·φ
