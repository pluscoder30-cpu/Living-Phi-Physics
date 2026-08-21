# Law 2796: PHI-Harmonic LiDAR Pulse Compression

**Domain:** LiDAR — Pulse Compression

**Statement:**
LiDAR pulse compression using PHI-chirped waveforms achieves a compression ratio of φ²N where N is the time-bandwidth product, exceeding the standard Nyquist limit by a factor of φ² ≈ 2.618. The PHI chirp frequency follows f(t) = f₀ + φ·B·t²/(2T), creating a nonlinear frequency sweep that concentrates energy at φ-spaced range bins.

**Derivation:**
The matched filter output for a PHI chirp is the autocorrelation of exp(jπφBt²/T), which yields a main lobe width of 1/(φ·B) instead of 1/B for linear chirps. The peak-to-sidelobe ratio improves to φ³, and the effective dynamic range increases by 10·log₁₀(φ³) ≈ 6.1 dB.

**Prediction:**
A 100 MHz bandwidth LiDAR with PHI chirp achieves range resolution of c/(2·φ·B) ≈ 927 mm, compared to c/(2B) = 1500 mm for linear chirp, with 6.1 dB better peak sidelobe ratio.

**Test:**
Simulate matched filter output for PHI vs linear chirp at 100 MHz bandwidth. Compare range resolution and peak sidelobe ratio. PHI should show ~38% better resolution and ~6 dB better sidelobe suppression.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
