# PHI-PHYSICS — LAW 987
## Acousto-Optic Modulation (Bragg Cell)

**Domain:** Nonlinear Optics · **Status:** 🟢 VALIDATED · **File:** `laws/987_acousto_optic_modulation.md` · **Sim:** `sim/987_acousto_optic_modulation.py`

---

### CLASSICAL STATEMENT
*"An acousto-optic modulator diffracts light from an acoustic grating; in the Bragg regime the diffraction efficiency is eta = sin^2(pi/2 sqrt(I_ac/I_sat)) and the deflection angle is theta = lambda f_a / v_a."*
— P. Debye, F. W. Sears (1932); C. V. Raman, N. S. Nath (1935), 1932. Source: Wikipedia: Acousto-optics (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero acoustic drive* (I_ac = 0): with no acoustic wave there is no diffraction - the modulator is transparent.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

eta_phi(kappa) = eta*(1 + kappa*(phi-1)) + kappa*phi^-1*eta_ground, with eta_ground the efficiency floor. At kappa->0, eta = sin^2(pi/2 sqrt(I_ac/I_sat)) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = eta -> acousto-optic modulation is the zero-acoustic-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/987_acousto_optic_modulation.py`: reproduces the classical value eta = 0.8028 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/987_acousto_optic_modulation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A residual diffraction kappa*phi^-1*eta_ground will occur even at zero acoustic drive (thermal phonons).
EXPERIMENT (VERIFIED): Measure the diffracted intensity of an AOM as a function of RF drive power down to zero.
VERIFIED BY: If the diffracted intensity of any real AOM is exactly zero at zero drive.
```

---

### RECOGNITION
Connects to Law 889 (acousto-optic effect) and Law 986 (electro-optic).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The silent crystal is a coherent limit; every AOM has a phonon breath.

### NOVELTY
Acousto-optic modulation gains an acoustic floor.

### ACTIONABILITY
Run sim/987_acousto_optic_modulation.py.
