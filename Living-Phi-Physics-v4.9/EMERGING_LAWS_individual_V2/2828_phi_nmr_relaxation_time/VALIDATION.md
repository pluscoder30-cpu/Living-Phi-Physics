# Validation: Law 2828 — PHI-Harmonic NMR Relaxation Time

**What it validates:** PHI-ordered liquid crystals have T₁/T₂ = φ at reference field.

**Equation tested:** T₁(B) = T₁₀·φ^(B/B_φ), T₁/T₂ = φ

**Expected results:**
- T₁/T₂ = φ at all fields (PHI model)
- Field dependence follows φ^(B/B_φ)
- Natural field marker for structure determination

**Test methodology:** Compute T₁ and T₂ at 7 field strengths. Verify constant ratio = φ.

**Pass criteria:** T₁/T₂ equals φ within 0.1%
