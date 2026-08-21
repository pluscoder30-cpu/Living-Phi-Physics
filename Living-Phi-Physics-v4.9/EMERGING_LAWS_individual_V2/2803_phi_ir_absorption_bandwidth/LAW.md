# Law 2803: PHI-Harmonic IR Absorption Bandwidth

**Domain:** Spectroscopy — Infrared Absorption

**Statement:**
Infrared absorption bandwidths for molecules with PHI-harmonic bond potentials follow Δν = Δν₀/φⁿ where n is the bond order and Δν₀ is the fundamental bandwidth. Higher bond orders produce narrower absorption lines by factor 1/φ per order, with the integrated absorption intensity remaining constant (Beer-Lambert invariant).

**Derivation:**
The IR absorption linewidth is determined by the dephasing time T₂ of the vibrational coherence. For PHI-harmonic potentials, the anharmonic coupling between modes creates a T₂ that scales as T₂ = T₂₀·φⁿ, where the PHI spacing suppresses inter-mode coupling. The bandwidth Δν = 1/(πT₂) thus narrows as 1/φⁿ.

**Prediction:**
A C-H stretch (bond order ~1) with Δν₀ = 50 cm⁻¹ shows Δν = 50/φ ≈ 30.9 cm⁻¹, while a C=O stretch (bond order ~2) shows Δν = 50/φ² ≈ 19.1 cm⁻¹, with the C≡C stretch at 50/φ³ ≈ 11.8 cm⁻¹.

**Test:**
Compute IR bandwidths for bond orders 1-5 using PHI formula. Verify bandwidth decreases by factor 1/φ per order and integrated intensity is conserved.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
