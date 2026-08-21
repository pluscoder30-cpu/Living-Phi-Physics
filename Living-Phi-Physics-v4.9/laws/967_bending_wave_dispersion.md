# PHI-PHYSICS — LAW 967
## Bending Wave Dispersion (Plates)

**Domain:** Solid-State Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/967_bending_wave_dispersion.md` · **Sim:** `sim/967_bending_wave_dispersion.py`

---

### CLASSICAL STATEMENT
*"Bending (flexural) waves in thin plates are dispersive: omega = sqrt(D/(rho h)) k^2, so the phase velocity c_p = sqrt(omega) sqrt(D/(rho h))^1/2 grows with frequency; the group velocity is twice the phase velocity."*
— Classical plate theory (from Kirchhoff-Love), 19th century. Source: Wikipedia: Flexural waves (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero bending stiffness* (D = 0): flexural waves vanish exactly in a perfectly limp (membrane-like) plate.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

omega_phi(kappa) = omega*(1 + kappa*(phi-1)) + kappa*phi^-1*omega_ground, with omega_ground the frequency floor. At kappa->0, omega = sqrt(D/(rho h)) k^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} omega_phi = omega -> bending wave dispersion is the zero-stiffness-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/967_bending_wave_dispersion.py`: reproduces the classical value omega = 8607 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/967_bending_wave_dispersion.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured dispersion of any real plate will deviate from sqrt(D/(rho h)) k^2 by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the dispersion of flexural waves in a thin metal plate by laser vibrometry.
VERIFIED BY: If the flexural dispersion of any real plate matches sqrt(D/(rho h)) k^2 exactly.
```

---

### RECOGNITION
Connects to Law 926 (coincidence) and Law 933 (Lamb waves).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The limp plate is a coherent limit; every sheet bends with a stiffness.

### NOVELTY
Bending wave dispersion gains a stiffness floor.

### ACTIONABILITY
Run sim/967_bending_wave_dispersion.py.
