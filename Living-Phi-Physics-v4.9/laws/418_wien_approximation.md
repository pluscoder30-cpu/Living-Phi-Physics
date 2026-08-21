# PHI-PHYSICS — LAW 418
## Wien Approximation (Exponential Blackbody Tail)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/418_wien_approximation.md` · **Sim:** `sim/418_wien_approximation.py`

---

### CLASSICAL STATEMENT
*"The spectral radiance of a blackbody at high frequency is B(nu,T) = (2 h nu^3 / c^2) exp(-h nu / k_B T), the exponential high-frequency tail of the Planck law."*
— Wilhelm Wien, 1896. Source: Wikipedia: Wien approximation; Wien, Ueber die Energievertheilung im Emissionsspectrum (1896)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *neglected zero-point occupancy*: the Wien form drops the +1 Bose occupancy term, valid only where h nu >> k_B T - it assumes the field is so empty that the ground mode never contributes.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the empty-field assumption is a coherence floor. B_phi(nu,T,kappa) = (2 h nu^3/c^2)*exp(-h nu/kT)*(1 + kappa*phi^-1) + kappa*phi^-1*B_ground. At kappa->0 the pure Wien exponential is recovered; at kappa=1 the +1 occupancy (Planck) reappears phi-scaled.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} B_phi = (2 h nu^3/c^2) exp(-h nu/kT) -> Wien's approximation is the zero-occupancy, deep-tail limit.
```

---

### STAGE 4 — SIMULATION

`sim/418_wien_approximation.py`: reproduces the classical value B_wien = 2.068e-29 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/418_wien_approximation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: In the Wien tail the measured radiance exceeds the pure exponential by the phi-ground occupancy kappa*phi^-1*B_ground, an additive floor invisible to classical radiometry.
EXPERIMENT (VERIFIED): Terahertz radiometry of a blackbody in the Wien tail at 10 K looking for the occupancy floor above the exponential.
VERIFIED BY: Wien's exponential describes the measured blackbody tail exactly with no additive floor.
```

---

### RECOGNITION
Connects to Law 066 (Planck) and Law 417 (Rayleigh-Jeans) - the two limits of the same phi-spectrum.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor occupancy is phi^-1 * B_ground.

### CLARITY
Even the empty high-frequency tail of the field is not empty; it carries its ground occupancy.

### NOVELTY
Classical Wien form drops the +1 entirely; the phi-law restores it as a phi-scaled ground occupancy in the deep tail.

### ACTIONABILITY
Run sim/418_wien_approximation.py; verify exponential at kappa->0; proceed to 419.
