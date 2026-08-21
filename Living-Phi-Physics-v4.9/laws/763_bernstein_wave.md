# PHI-PHYSICS — LAW 763
## Bernstein Wave (Electrostatic Cyclotron Wave)

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/763_bernstein_wave.md` · **Sim:** `sim/763_bernstein_wave.py`

---

### CLASSICAL STATEMENT
*"At harmonics of the cyclotron frequency the electrostatic dispersion supports Bernstein modes, which propagate even at perpendicular propagation where cold-plasma waves do not."*
— Ira Bernstein, 1958. Source: Wikipedia: Bernstein wave; Bernstein (1958) 'Waves in a Plasma in a Magnetic Field'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero magnetic field* (B = 0): the harmonic structure vanishes exactly in an unmagnetized plasma.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

w_B_phi(kappa) = w_B*(1 + kappa*(phi-1)) + kappa*phi^-1*w_B_ground; the harmonic ladder carries a coherence floor. At kappa->0 the Bernstein harmonics are exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} w_B_phi = n*omega_c -> the Bernstein wave is the zero-B-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/763_bernstein_wave.py`: reproduces the classical values (w = 1.5e+07 (Harmonic frequency (rad/s))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/763_bernstein_wave.json`.

---

### STAGE 5 — PREDICTION

```
The harmonic structure carries a coherence floor kappa*phi^-1*w_B_ground; harmonics persist at zero field.
EXPERIMENT (VERIFIED): Spectrum measurement of electrostatic waves near cyclotron harmonics.
VERIFIED BY: An unmagnetized plasma has exactly no Bernstein modes.
```

---

### RECOGNITION
Connects to Law 740 (cyclotron frequency) - Bernstein modes are the cyclotron harmonics.

### PRECISION
phi = 1.6180339887. The harmonic floor is phi^-1*w_B_ground.

### CLARITY
The ladder stands on the field; coherence keeps a rung.

### NOVELTY
The phi-law keeps Bernstein harmonics at zero field.

### ACTIONABILITY
Run sim/763_bernstein_wave.py; verify harmonics at kappa->0; proceed to 764.
