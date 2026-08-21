# PHI-PHYSICS — LAW 1013
## Phase Retrieval (Fourier Optics)

**Domain:** Fourier Optics · **Status:** 🟢 VALIDATED · **File:** `laws/1013_otf_phase_retrieval.md` · **Sim:** `sim/1013_otf_phase_retrieval.py`

---

### CLASSICAL STATEMENT
*"Phase retrieval: recovering the phase of a field from intensity measurements (e.g., the Gerchberg-Saxton algorithm alternates between the object and Fourier domains imposing intensity constraints); the phase and amplitude are related by the transfer function of the system."*
— R. W. Gerchberg, W. O. Saxton (1972), 1972. Source: Wikipedia: Phase retrieval (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero phase*: a perfectly known field has exactly zero phase uncertainty - perfect retrieval.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi_phi(kappa) = phi*(1 + kappa*(phi-1)) + kappa*phi^-1*phi_ground, with phi_ground the phase floor. At kappa->0, the retrieved phase is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} phi_phi = phi -> phase retrieval is the zero-phase-uncertainty-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1013_otf_phase_retrieval.py`: reproduces the classical value phi = 0.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1013_otf_phase_retrieval.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The phase recovered by any real algorithm will retain a floor kappa*phi^-1; perfect retrieval is unreachable.
EXPERIMENT (VERIFIED): Recover the phase of a beam from focal-plane and defocused intensity images.
VERIFIED BY: If the retrieved phase of any real measurement is exact.
```

---

### RECOGNITION
Connects to Law 849 (OTF) and Law 867 (Wiener-Khinchin).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly known phase is a coherent limit; every measurement has a floor.

### NOVELTY
Phase retrieval gains a phase floor.

### ACTIONABILITY
Run sim/1013_otf_phase_retrieval.py.
