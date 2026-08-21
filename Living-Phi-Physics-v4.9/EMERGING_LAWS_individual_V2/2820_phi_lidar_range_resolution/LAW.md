# Law 2820: PHI-Harmonic LiDAR Range Resolution

**Domain:** LiDAR — Range Resolution

**Statement:**
LiDAR range resolution improves by factor φ when using PHI-coded pulse trains instead of single pulses. A PHI-coded train of N pulses with inter-pulse spacing d₀·φⁿ achieves range resolution ΔR = c/(2·N·φ·B) where B is the bandwidth, exceeding the single-pulse resolution by factor N·φ.

**Derivation:**
The ambiguity function of a PHI-coded pulse train has a main lobe width of 1/(N·φ·B) in the delay axis, compared to 1/B for a single pulse. The PHI spacing suppresses range sidelobes to -20·log₁₀(φ) ≈ -4.4 dB per sidelobe, creating a natural taper that reduces the peak sidelobe level to -20·log₁₀(φ^N) = -4.4N dB.

**Prediction:**
An 8-pulse PHI-coded LiDAR at 1550 nm with 100 MHz bandwidth achieves range resolution of 187 mm (vs 1500 mm single pulse), with peak sidelobe at -35 dB.

**Test:**
Compute ambiguity function for 8-pulse PHI-coded vs uniform-coded trains. Compare range resolution and sidelobe levels.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
