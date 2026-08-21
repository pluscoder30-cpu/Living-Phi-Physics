# Law 2801: PHI-Harmonic PET Coincidence Resonance

**Domain:** Medical Imaging — PET Physics

**Statement:**
Positron emission tomography coincidence detection efficiency is maximized when detector ring crystal elements are arranged in PHI-harmonic pitch patterns, where adjacent crystal widths alternate as w·φⁿ. This creates a natural collimation effect that reduces random coincidences by factor 1/φ while maintaining sensitivity, due to PHI-encoded angular selectivity of the detector response.

**Derivation:**
The geometric sensitivity of a PET detector ring is G = Ω/(4π)·ε² where Ω is solid angle and ε is detector efficiency. With PHI-pitch crystals, the effective solid angle for true coincidences is Ω_true = Ω₀·φ while for randoms it is Ω_rand = Ω₀/φ, giving a true-to-random ratio improvement of φ². The NECR (noise equivalent count rate) improves by factor φ.

**Prediction:**
A PET scanner with PHI-pitched BGO crystals achieves NECR improvement of ~61.8% at 100 kBq/mL activity concentration, with spatial resolution maintained at 4 mm.

**Test:**
Simulate PET coincidence events with PHI-pitched vs uniform detector arrays. Compute true/random ratio and NECR. PHI-pitch should show φ²× better T/R ratio.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
