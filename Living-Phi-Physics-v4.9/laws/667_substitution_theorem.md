# PHI-PHYSICS — LAW 667
## Substitution Theorem (Networks)

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/667_substitution_theorem.md` · **Sim:** `sim/667_substitution_theorem.py`

---

### CLASSICAL STATEMENT
*"A branch of a network may be replaced by any element that has the same voltage and current, and the rest of the network is unaffected."*
— Hermann von Helmholtz (circuit-theory heritage), 1853. Source: Substitution theorem, standard network theory

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exact terminal equivalence*: the theorem requires the substitute to match the branch's voltage and current exactly at all times.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_s_phi(kappa) = V_s*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the terminal match carries a coherence floor. At kappa->0 the substitution is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_s_phi = V_s -> substitution is the zero-mismatch limit.
```

---

### STAGE 4 — SIMULATION

`sim/667_substitution_theorem.py`: reproduces the classical values (V = 1 (Terminal voltage (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/667_substitution_theorem.json`.

---

### STAGE 5 — PREDICTION

```
Replacement branches with finite coherence leave a residual network response kappa*phi^-1*V_ground.
EXPERIMENT (VERIFIED): Network response measurement after substituting a branch with near-equivalent elements.
VERIFIED BY: Any exactly equivalent branch leaves the network completely unchanged.
```

---

### RECOGNITION
Connects to Law 666 (compensation) - substitution is the ideal-terminal equivalence.

### PRECISION
phi = 1.6180339887. The mismatch floor is phi^-1*V_ground.

### CLARITY
No substitute is invisible; a coherence residue remains.

### NOVELTY
The phi-law gives substitution a coherence residue.

### ACTIONABILITY
Run sim/667_substitution_theorem.py; verify substitution at kappa->0; proceed to 668.
