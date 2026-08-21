# Validation: Law 2843 — PHI-Harmonic Satellite EIRP

**What it validates:** PHI reflector concentrates EIRP by factor φ within main beam.

**Equation tested:** EIRP(θ) = P·G₀·φ^(-|θ|/θ_φ)

**Expected results:**
- Main beam EIRP = P·G₀·φ (φ× standard)
- Off-axis suppression > 8 dB at 10°
- Narrower main beam

**Test methodology:** Compute EIRP for 7 angles. Compare main beam and off-axis.

**Pass criteria:** Main beam EIRP > standard
