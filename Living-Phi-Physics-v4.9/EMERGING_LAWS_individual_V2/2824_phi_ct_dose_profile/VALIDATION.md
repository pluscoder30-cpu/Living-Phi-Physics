# Validation: Law 2824 — PHI-Harmonic CT Dose Profile

**What it validates:** PHI modulation reduces peripheral CT dose by 38.2%.

**Equation tested:** D(z) = D₀·exp(-|z|/z_φ)·cos²(πz/(φz₀))

**Expected results:**
- Peripheral dose reduced by ~38.2%
- Center dose maintained
- PHI decay length = z₀/ln(φ)

**Test methodology:** Compute dose profiles for PHI and uniform modulation. Compare peripheral dose at ±z₀.

**Pass criteria:** Peripheral dose with PHI < uniform
