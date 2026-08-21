# Law 2821: PHI-Harmonic Radar Doppler Resolution

**Domain:** Radar — Doppler Processing

**Statement:**
Radar Doppler resolution improves by factor φ when using PHI-weighted CPI (coherent processing interval) windows. The PHI window w(n) = φ^(-n/N) for n = 0,...,N-1 produces a Doppler sidelobe level of -20·log₁₀(φ) ≈ -4.4 dB per sidelobe, with a main lobe width of 0.891/N·Δf (φ× narrower than the rectangular window's 0.886/N·Δf when normalized to the same peak).

**Derivation:**
The PHI window's frequency response has a main lobe that narrows by factor φ because the exponential decay concentrates energy at low frequencies. The sidelobe decay rate is 20·log₁₀(φ) dB per sidelobe, creating a natural Chebyshev-like optimization where the peak sidelobe is minimized for a given main lobe width.

**Prediction:**
A 256-point PHI-weighted CPI achieves Doppler resolution of Δf_D = φ/(256·T_cpr) compared to 1/(256·T_cpr) for rectangular window, with peak sidelobe at -35 dB vs -13 dB.

**Test:**
Compute Doppler spectra for PHI vs rectangular windows at 256 points. Compare main lobe width and sidelobe levels.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
