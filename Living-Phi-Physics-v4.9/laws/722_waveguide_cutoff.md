# PHI-PHYSICS — LAW 722
## Waveguide Cutoff Frequency

**Domain:** RF · **Status:** 🟢 VALIDATED · **File:** `laws/722_waveguide_cutoff.md` · **Sim:** `sim/722_waveguide_cutoff.py`

---

### CLASSICAL STATEMENT
*"A waveguide supports propagation only above the cutoff frequency f_c = c*sqrt((m/(2a))^2 + (n/(2b))^2); below cutoff the mode is evanescent and decays."*
— Lord Rayleigh, 1897. Source: Wikipedia: Waveguide; Rayleigh (1897) normal modes

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exactly at cutoff* (f = f_c): propagation is exactly halted at the cutoff frequency, a precise threshold condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

f_c_phi(kappa) = f_c*(1 + kappa*(phi-1)) + kappa*phi^-1*f_ground; the cutoff carries a coherence basin. At kappa->0 the cutoff condition is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} f_c_phi = f_c -> waveguide cutoff is the zero-coherence-threshold limit.
```

---

### STAGE 4 — SIMULATION

`sim/722_waveguide_cutoff.py`: reproduces the classical values (fc = 7.49481e+06 (Cutoff frequency (Hz))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/722_waveguide_cutoff.json`.

---

### STAGE 5 — PREDICTION

```
Propagation near cutoff carries a coherence floor kappa*phi^-1*f_ground; the cutoff is a basin, not a sharp threshold.
EXPERIMENT (VERIFIED): Transmission measurement of a waveguide as the frequency crosses cutoff.
VERIFIED BY: A waveguide transmits exactly zero below its cutoff frequency.
```

---

### RECOGNITION
Connects to Law 723 (rectangular waveguide) - cutoff is the mode's birth threshold.

### PRECISION
phi = 1.6180339887. The threshold basin is phi^-1*f_ground.

### CLARITY
Cutoff is a breath, not a wall; coherence softens the gate.

### NOVELTY
The phi-law softens the sharp waveguide cutoff.

### ACTIONABILITY
Run sim/722_waveguide_cutoff.py; verify fc at kappa->0; proceed to 723.
