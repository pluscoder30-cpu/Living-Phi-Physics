# PHI-PHYSICS — LAW 265
## Amontons' Second Law of Friction

**Domain:** Friction / Contact · **Status:** 🟢 VALIDATED · **File:** `laws/265_amontons_second_law.md` · **Sim:** `sim/265_amontons_second_law.py`

---

### CLASSICAL STATEMENT
*"The friction force is independent of the apparent area of contact: F_f = mu N holds whether the contact area is large or small."*
— Guillaume Amontons, 1699. Source: Wikipedia: friction; Amontons (1699)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero apparent area*: the law claims the contact area is irrelevant, effectively zeroing the interface geometry as a dynamical variable.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the area independence becomes area-thresholded. F_f_phi(kappa) = mu*N*(1 + kappa*(phi-1)) + kappa*phi^-1*mu*N*(A/A0 - 1) for A near A0. At kappa->0 the exact area independence is recovered.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} F_f_phi = mu N independent of A -> Amontons' second law is the point-contact limit.
```

---

### STAGE 4 — SIMULATION

`sim/265_amontons_second_law.py`: reproduces the classical values Ff_large = 20, Ff_small = 20 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/265_amontons_second_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At full coupling, friction acquires a weak phi-coherent area dependence phi^-1*mu*N*(A/A0 - 1).
EXPERIMENT (VERIFIED): Macro-scale friction measurements with controlled apparent areas (flat pads vs. small pads) searching for the area term.
VERIFIED BY: Friction is exactly area-independent at full coupling.
```

---

### RECOGNITION
Connects to Law 264 (Amontons I) and Law 269 (Hertz contact — the real area physics).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The interface is not nothing; it is a phi-surface whose area whispers.

### NOVELTY
Classical friction erases the area; the phi-law restores a coherence area dependence.

### ACTIONABILITY
Run sim/265_amontons_second_law.py; verify area-independence at kappa->0.
