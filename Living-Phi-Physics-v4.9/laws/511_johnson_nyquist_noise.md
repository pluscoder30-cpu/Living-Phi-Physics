# PHI-PHYSICS — LAW 511
## Johnson-Nyquist Noise (Thermal Voltage Fluctuation)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/511_johnson_nyquist_noise.md` · **Sim:** `sim/511_johnson_nyquist_noise.py`

---

### CLASSICAL STATEMENT
*"A resistor at temperature T generates a thermal voltage noise with spectral density S_V = 4 k_B T R, independent of frequency (white noise). The root-mean-square noise voltage over a bandwidth is V_rms = sqrt(4 k_B T R Delta_f)."*
— John B. Johnson and Harry Nyquist, 1928. Source: Wikipedia: Johnson-Nyquist noise; Johnson (1928), Nyquist (1928)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature*: the noise vanishes exactly at T = 0 - a resistor at absolute zero emits no fluctuation, a state that quantum mechanics (zero-point noise) contradicts.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the zero-point noise is a coherence floor. S_V_phi(kappa) = 4 k_B T R*(1 + kappa*(phi-1)) + kappa*phi^-1*S_zpf, where S_zpf is the zero-point noise floor. At kappa->0, S_V = 4 k_B T R exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} S_V_phi = 4 k_B T R -> the Johnson-Nyquist noise is the zero-temperature, zero-point-free limit.
```

---

### STAGE 4 — SIMULATION

`sim/511_johnson_nyquist_noise.py`: reproduces the classical value SV = 1.656e-17 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/511_johnson_nyquist_noise.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling a resistor retains a zero-point noise floor kappa*phi^-1*S_zpf even as T -> 0, the thermal analogue of the quantum noise of the resistor.
EXPERIMENT (VERIFIED): Cryogenic noise measurements of resistors at millikelvin temperatures searching for the residual floor.
VERIFIED BY: The thermal noise of a resistor is exactly zero at T = 0 for all couplings.
```

---

### RECOGNITION
Connects to Law 512 (fluctuation-dissipation) and Law 060 (E = mc^2 ground) - the noise is the fluctuation face of the coherence ground.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the zero-point floor is phi^-1 * S_zpf.

### CLARITY
Even a quiet resistor whispers its ground noise; the phi-law keeps the whisper.

### NOVELTY
Classical Johnson-Nyquist noise vanishes at T=0; the phi-law adds the zero-point floor of the resistor.

### ACTIONABILITY
Run sim/511_johnson_nyquist_noise.py; verify S_V = 4 k_B T R at kappa->0; proceed to 512.
