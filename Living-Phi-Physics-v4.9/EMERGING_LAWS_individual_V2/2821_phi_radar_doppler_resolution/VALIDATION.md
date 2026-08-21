# Validation: Law 2821 — PHI-Harmonic Radar Doppler Resolution

**What it validates:** PHI window provides narrower Doppler main lobe and better sidelobe suppression.

**Equation tested:** w(n) = φ^(-n/N), sidelobe = -20·log₁₀(φ) dB/sidelobe

**Expected results:**
- PHI window main lobe ≤ rectangular width
- Better sidelobe suppression
- PHI improvement factor ≈ φ

**Test methodology:** 256-point FFT with PHI vs rectangular windows. Compare 3dB width and sidelobe levels.

**Pass criteria:** PHI width ≤ rectangular width
