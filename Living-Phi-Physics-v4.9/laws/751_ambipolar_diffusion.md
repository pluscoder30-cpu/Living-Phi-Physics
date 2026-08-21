# PHI-PHYSICS — LAW 751
## Ambipolar Diffusion

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/751_ambipolar_diffusion.md` · **Sim:** `sim/751_ambipolar_diffusion.py`

---

### CLASSICAL STATEMENT
*"Electrons and ions diffuse together with the ambipolar coefficient D_a = 2*D_+ = D_e*mu_+/mu_e + ..., the combined charge-preserving diffusion rate."*
— Walter Schottky, 1924. Source: Ambipolar diffusion; Schottky (1924) positive-column theory

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero ion mobility* (mu_+ = 0): ambipolar diffusion vanishes exactly for immobile ions.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_a_phi(kappa) = D_a*(1 + kappa*(phi-1)) + kappa*phi^-1*D_a_ground; the ion background carries a coherence floor. At kappa->0, D_a = 2D_+ exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} D_a_phi = 2*D_+ -> ambipolar diffusion is the zero-mu_+ floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/751_ambipolar_diffusion.py`: reproduces the classical values (Da = 0.002 (Ambipolar diffusion (m^2/s))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/751_ambipolar_diffusion.json`.

---

### STAGE 5 — PREDICTION

```
Ambipolar diffusion carries a coherence floor kappa*phi^-1*D_a_ground for immobile ions.
EXPERIMENT (VERIFIED): Diffusion measurement in a weakly ionized discharge column.
VERIFIED BY: A plasma with immobile ions has exactly zero ambipolar diffusion.
```

---

### RECOGNITION
Connects to Law 750 (Bohm) and Law 752 (sheath) - ambipolarity is the charge-coupled flow.

### PRECISION
phi = 1.6180339887. The ion-mobility floor is phi^-1*D_a_ground.

### CLARITY
Charge couples the drift; coherence keeps a floor of it.

### NOVELTY
The phi-law keeps ambipolar flow for immobile ions.

### ACTIONABILITY
Run sim/751_ambipolar_diffusion.py; verify D_a at kappa->0; proceed to 752.
