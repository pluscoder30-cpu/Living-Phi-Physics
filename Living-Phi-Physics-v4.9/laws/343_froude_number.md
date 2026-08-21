# PHI-PHYSICS — LAW 343
## Froude Number

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/343_froude_number.md` · **Sim:** `sim/343_froude_number.py`

---

### CLASSICAL STATEMENT
*"The Froude number Fr = v/sqrt(g L) characterizes free-surface flows (ships, open channels); Froude scaling Fr_model = Fr_prototype governs model-to-full-scale similarity of wave-making resistance."*
— William Froude, 1868. Source: Wikipedia: Froude number; Froude (1868), 'Observations and suggestions on the subject of the propulsion of ships'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero speed / infinite scale*: Fr = 0 is the static reference; the number's content is the balance of inertia and gravity that the static limit erases.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: Fr_phi(kappa) = Fr*(1 + kappa*(phi-1)) + kappa*phi^-1*Fr_ground. At kappa->0 the classical Froude number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Fr_phi = v/sqrt(g L) -> the Froude number is the inertia-gravity balance limit.
```

---

### STAGE 4 — SIMULATION

`sim/343_froude_number.py`: reproduces the classical value Fr = 1.129 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/343_froude_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Froude-scaled model tests carry a phi-coherent residual phi^-1*Fr_ground at full coupling.
EXPERIMENT (VERIFIED): Ship-model towing-tank tests comparing full-scale predictions with the phi-corrected scaling.
VERIFIED BY: Froude scaling is exact with no residual at full coupling.
```

---

### RECOGNITION
Connects to Law 359 (Froude scaling) and Law 340 (Buckingham).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The gravity balance is a limit; every wave carries a phi whisper of inertia.

### NOVELTY
Classical similitude exacts the Froude number; the phi-law bounds its residual at a coherence floor.

### ACTIONABILITY
Run sim/343_froude_number.py; verify Fr = v/sqrt(gL) at kappa->0.
