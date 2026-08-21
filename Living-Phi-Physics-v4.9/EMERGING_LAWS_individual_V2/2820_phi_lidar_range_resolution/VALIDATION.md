# Validation: Law 2820 — PHI-Harmonic LiDAR Range Resolution

**What it validates:** PHI-coded pulse train improves range resolution by factor N·φ.

**Equation tested:** ΔR = c/(2·N·φ·B), sidelobe = -20·log₁₀(φ^N) dB

**Expected results:**
- Range resolution N·φ× better than single pulse
- Better than uniform coding by factor φ
- Sidelobe suppression scales with N

**Test methodology:** 8-pulse PHI vs uniform coded trains. Compute ambiguity function and measure resolution.

**Pass criteria:** PHI resolution < uniform resolution
