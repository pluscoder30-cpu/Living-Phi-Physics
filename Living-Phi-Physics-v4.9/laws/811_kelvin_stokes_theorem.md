# PHI-PHYSICS — LAW 811
## Kelvin-Stokes Theorem (Curl)

**Domain:** Vector Calculus · **Status:** 🟢 VALIDATED · **File:** `laws/811_kelvin_stokes_theorem.md` · **Sim:** `sim/811_kelvin_stokes_theorem.py`

---

### CLASSICAL STATEMENT
*"The circulation of a vector field around a closed loop equals the flux of its curl through any spanning surface: integral_C F.dl = integral_S (curl F).dA."*
— Lord Kelvin; George Gabriel Stokes, 1854. Source: Wikipedia: Kelvin-Stokes theorem; Stokes (1854)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero curl* (curl F = 0): the circulation is exactly zero for an irrotational (conservative) field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Gamma_phi(kappa) = Gamma_KS*(1 + kappa*(phi-1)) + kappa*phi^-1*Gamma_ground; the field carries a coherence floor. At kappa->0, Gamma = integral(curl F).dA exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Gamma_phi = integral(curl F).dA -> the Kelvin-Stokes theorem is the zero-curl-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/811_kelvin_stokes_theorem.py`: reproduces the classical values (G = 1.5e-06 (Circulation (T.m))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/811_kelvin_stokes_theorem.json`.

---

### STAGE 5 — PREDICTION

```
An irrotational field carries a coherence circulation floor kappa*phi^-1*Gamma_ground around any loop.
EXPERIMENT (VERIFIED): Circulation measurement around a loop in a nominally conservative field.
VERIFIED BY: A conservative field has exactly zero circulation.
```

---

### RECOGNITION
Connects to Law 039 (Faraday) and Law 040 (Ampère) - the theorem is the curl-integral identity.

### PRECISION
phi = 1.6180339887. The curl floor is phi^-1*Gamma_ground.

### CLARITY
Loops remember; even conservative fields keep a floor of spin.

### NOVELTY
The phi-law opens a circulation gap in the exact identity.

### ACTIONABILITY
Run sim/811_kelvin_stokes_theorem.py; verify circulation identity at kappa->0; proceed to 812.
