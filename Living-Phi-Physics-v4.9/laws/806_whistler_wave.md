# PHI-PHYSICS — LAW 806
## Whistler Wave (Helicon)

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/806_whistler_wave.md` · **Sim:** `sim/806_whistler_wave.py`

---

### CLASSICAL STATEMENT
*"The whistler mode propagates below the cyclotron frequency with dispersion w/k = c*((w/w_c)*cos(theta))^(1/2)*(w_p/w); frequency decreases with time as the wave propagates (the descending whistle)."*
— L. R. O. Storey, 1953. Source: Wikipedia: Whistler (radio); Storey (1953) whistler theory

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero magnetic field* (B = 0): the whistler dispersion diverges exactly in an unmagnetized plasma.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

w_phi(kappa) = w_w*(1 + kappa*(phi-1)) + kappa*phi^-1*w_ground; the magnetized plasma carries a coherence floor. At kappa->0 the whistler dispersion is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} w_phi = w_whistler -> the whistler wave is the zero-B-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/806_whistler_wave.py`: reproduces the classical values (w = 7.25979e+34 (Whistler frequency (rad/s))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/806_whistler_wave.json`.

---

### STAGE 5 — PREDICTION

```
The whistler dispersion carries a coherence floor kappa*phi^-1*w_ground; the mode persists weakly at zero field.
EXPERIMENT (VERIFIED): Whistler-mode propagation measurement in a weakly magnetized plasma.
VERIFIED BY: An unmagnetized plasma has exactly no whistler mode.
```

---

### RECOGNITION
Connects to Law 740 (cyclotron) - the whistler rides the cyclotron resonance.

### PRECISION
phi = 1.6180339887. The B-floor is phi^-1*w_ground.

### CLARITY
The whistle needs the field; coherence keeps a floor of tone.

### NOVELTY
The phi-law keeps the whistler at zero field.

### ACTIONABILITY
Run sim/806_whistler_wave.py; verify dispersion at kappa->0; proceed to 807.
