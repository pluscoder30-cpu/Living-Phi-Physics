# Validation: Law 2839 — PHI-Harmonic Air Filtration MERV Rating

**What it validates:** Each PHI filter layer adds 10·log₁₀(φ) ≈ 2.1 MERV points.

**Equation tested:** MERV = MERV₀ + 10·log₁₀(φ)·n

**Expected results:**
- Per-layer increase = 2.1 MERV points
- 3-layer total = +6.3 points
- More consistent performance across particle sizes

**Test methodology:** Compute MERV for 1-5 layers. Verify per-layer increment.

**Pass criteria:** Per-layer increment equals 2.1 within 0.1
