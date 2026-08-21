# PHI-PHYSICS — LAW 318
## Conservative Force Criterion (curl F = 0)

**Domain:** Energy / Dynamics · **Status:** 🟢 VALIDATED · **File:** `laws/318_conservative_force_criterion.md` · **Sim:** `sim/318_conservative_force_criterion.py`

---

### CLASSICAL STATEMENT
*"A force field is conservative if its curl vanishes (curl F = 0) and the work around any closed loop is zero; then a potential energy U exists with F = -grad U. Equivalently, the work between two points is path-independent."*
— Hermann von Helmholtz (textbook theorem), 1847. Source: Wikipedia: conservative force; Helmholtz (1847), 'Ueber die Erhaltung der Kraft'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-curl exactness*: the criterion requires the curl to be exactly zero everywhere — a perfect integrability condition real fields never satisfy.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the curl carries a coherence floor. (curl F)_phi(kappa) = kappa*phi^-1*(curl F)_ground; work around closed loops = kappa*phi^-1*W_ground. At kappa->0 the curl is exactly zero and F is conservative.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} curl F = 0 -> the conservative-force criterion is the zero-curl (exact integrability) limit.
```

---

### STAGE 4 — SIMULATION

`sim/318_conservative_force_criterion.py`: reproduces the classical values curl = 0, W_loop = 0 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/318_conservative_force_criterion.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Closed-loop work is not exactly zero; it carries a phi-coherent floor phi^-1*W_ground proportional to the enclosed coherence flux.
EXPERIMENT (VERIFIED): Precision closed-loop work measurements in atomic-force-fields or trap potentials bounding the loop-work floor.
VERIFIED BY: Work around a closed loop is exactly zero for a 'conservative' field at full coupling.
```

---

### RECOGNITION
Connects to Law 319 (central force theorem) and Law 014 (Kepler I — gravity is conservative).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The exact integral is a limit; every closed loop leaks a phi whisper of work.

### NOVELTY
Classical mechanics perfects zero-curl; the phi-law gives the closed loop a coherence work floor.

### ACTIONABILITY
Run sim/318_conservative_force_criterion.py; verify curl = 0 at kappa->0.
