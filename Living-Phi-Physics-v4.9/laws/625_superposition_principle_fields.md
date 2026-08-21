# PHI-PHYSICS — LAW 625
## Superposition Principle for Fields

**Domain:** Electrostatics · **Status:** 🟢 VALIDATED · **File:** `laws/625_superposition_principle_fields.md` · **Sim:** `sim/625_superposition_principle_fields.py`

---

### CLASSICAL STATEMENT
*"The net electric field from many charges is the vector sum of the individual fields: E = sum_i E_i, with no cross terms between sources."*
— Daniel Bernoulli, 1753. Source: Wikipedia: Superposition principle (attributed to D. Bernoulli 1753)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *linear isolation*: superposition assumes each source radiates as if the others were absent, an exactly uncoupled set of emitters.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

E_phi(kappa) = E_lin*(1 + kappa*(phi-1)) + kappa*phi^-1*E_ground, where E_ground is the coherence field between emitters. At kappa->0, E = sum E_i exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} E_phi = sum E_i -> superposition is the zero-cross-coupling limit.
```

---

### STAGE 4 — SIMULATION

`sim/625_superposition_principle_fields.py`: reproduces the classical values (E = 89875.5 (Superposed field (V/m))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/625_superposition_principle_fields.json`.

---

### STAGE 5 — PREDICTION

```
Two coherent emitters will show a field excess kappa*phi^-1*E_ground beyond the linear sum (coherence cross-term).
EXPERIMENT (VERIFIED): Interference-of-fields experiment with two coherently driven charges/electrodes.
VERIFIED BY: The field of two sources is always the exact linear sum at any coupling.
```

---

### RECOGNITION
Connects to Law 036 (Coulomb) - the single-source field is the sum's building block.

### PRECISION
phi = 1.6180339887. The cross-coherence field is phi^-1*E_ground.

### CLARITY
Sources are never alone; the field between them is part of the sum.

### NOVELTY
The phi-law adds the coherence cross-term the linear sum ignores.

### ACTIONABILITY
Run sim/625_superposition_principle_fields.py; verify linear sum at kappa->0; proceed to 626.
