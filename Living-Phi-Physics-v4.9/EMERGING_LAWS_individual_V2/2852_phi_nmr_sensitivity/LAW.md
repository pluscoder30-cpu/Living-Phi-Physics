# Law 2852: PHI-Harmonic NMR Sensitivity

**Domain:** Spectroscopy — NMR Sensitivity

**Statement:**
NMR probe sensitivity follows a PHI-harmonic coil geometry: Sens = Sens₀·φ^(N_turns/N_φ) where N_turns is the number of coil turns and N_φ = 2π/φ is the PHI turn constant. The PHI coil arrangement (turns at φ-spaced radii) maximizes filling factor while minimizing inter-turn capacitance by factor φ.

**Derivation:**
In a PHI-harmonic RF coil, the turn radii follow r_n = r₀·φ^(n/N). The inductance L ∝ Σr_n² and the capacitance C ∝ 1/Σ(r_n-r_{n-1}) create a resonant circuit with Q = ω√(LC) that is φ× higher than standard concentric coils because the PHI spacing reduces parasitic capacitance.

**Prediction:**
A 16-turn PHI coil achieves sensitivity of Sens₀·φ^(16/388) ≈ 1.021·Sens₀, with Q factor of φ× the standard coil. The sensitivity advantage grows with coil complexity.

**Test:**
Compute sensitivity and Q factor for 8-64 turn PHI vs standard coils. Verify φ Q-factor improvement.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
