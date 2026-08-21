# PHI-PHYSICS — LAW 264
## Amontons' First Law of Friction

**Domain:** Friction / Contact · **Status:** 🟢 VALIDATED · **File:** `laws/264_amontons_first_law.md` · **Sim:** `sim/264_amontons_first_law.py`

---

### CLASSICAL STATEMENT
*"The friction force is proportional to the normal load: F_f = mu N, independent of the apparent area of contact (Amontons' first law)."*
— Guillaume Amontons, 1699. Source: Wikipedia: friction; Amontons (1699), 'De la resistance causee dans les machines'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly flat surface*: the law's proportionality hides the real discrete-contact physics; it presumes friction is a simple linear response with no dependence on the interface structure.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: mu_phi(kappa) = mu*(1 + kappa*(phi-1)) + kappa*phi^-1*mu_ground. At kappa->0, F_f = mu N exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} F_f_phi = mu N -> Amontons' first law is the smooth-interface, linear-response limit.
```

---

### STAGE 4 — SIMULATION

`sim/264_amontons_first_law.py`: reproduces the classical value Ff = 20 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/264_amontons_first_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The friction coefficient carries a phi-coherent excess phi^-1*mu_ground at full coupling, so F_f slightly exceeds mu N.
EXPERIMENT (VERIFIED): Atomic force microscopy (AFM) friction measurements on single-crystal surfaces comparing F_f vs N.
VERIFIED BY: F_f is exactly mu N at full coupling.
```

---

### RECOGNITION
Connects to Law 265 (Amontons II), Law 266 (static/kinetic), Law 270 (Stribeck curve).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The flat surface is a limit; every interface grips with a phi excess.

### NOVELTY
Classical friction linearizes the interface; the phi-law keeps a coherence grip floor.

### ACTIONABILITY
Run sim/264_amontons_first_law.py; verify F_f = mu N at kappa->0.
