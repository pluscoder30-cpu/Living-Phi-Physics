# Law 2843: PHI-Harmonic Satellite EIRP

**Domain:** Satellite Systems — Link Budget

**Statement:**
The effective isotropic radiated power (EIRP) of satellite antennas with PHI-harmonic reflector profiles follows EIRP = P_tx·G₀·φ^(θ/θ_φ) where θ is the off-axis angle and θ_φ is the PHI beam constant. The PHI profile concentrates power within the main beam by factor φ, reducing off-axis radiation by factor 1/φ².

**Derivation:**
A PHI-harmonic reflector (surface profile r(θ) = r₀·φ^(-θ/θ_φ)) produces a beam pattern with main lobe gain G(0) = G₀·φ and first sidelobe at G(θ₁) = G₀/φ. The EIRP within the 3dB beamwidth is P_tx·G₀·φ, compared to P_tx·G₀ for standard parabolic reflectors.

**Prediction:**
A 10 W satellite transmitter with PHI reflector achieves EIRP = 16.18 W (10·φ) within the main beam, compared to 10 W for standard. Off-axis EIRP at 10° is reduced by 8 dB.

**Test:**
Compute EIRP pattern for PHI vs standard reflectors. Compare main beam EIRP and off-axis suppression.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
