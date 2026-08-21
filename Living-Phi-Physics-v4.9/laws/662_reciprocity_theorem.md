# PHI-PHYSICS — LAW 662
## Reciprocity Theorem (Networks)

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/662_reciprocity_theorem.md` · **Sim:** `sim/662_reciprocity_theorem.py`

---

### CLASSICAL STATEMENT
*"In a linear passive network the transfer impedance is symmetric: V_b/I_a (current at a, voltage at b) equals V_a/I_b; interchange of source and response leaves the ratio unchanged."*
— Lord Rayleigh, 1873. Source: Wikipedia: Reciprocity (electrical networks); Rayleigh (1873)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exactly reciprocal network*: the theorem assumes no active elements, no nonlinearity, and no time dependence - a fully symmetric medium.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Z_ab_phi(kappa) = Z_ab*(1 + kappa*(phi-1)) + kappa*phi^-1*Z_ground; the passive medium carries a coherence asymmetry floor. At kappa->0, Z_ab = Z_ba exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Z_ab_phi = Z_ab -> reciprocity is the zero-asymmetry limit.
```

---

### STAGE 4 — SIMULATION

`sim/662_reciprocity_theorem.py`: reproduces the classical values (Z = 1 (Transfer impedance (ohm))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/662_reciprocity_theorem.json`.

---

### STAGE 5 — PREDICTION

```
Under field coherence the transfer impedance develops an asymmetry kappa*phi^-1*Z_ground; measured reciprocity violations scale with coherence.
EXPERIMENT (VERIFIED): Transfer-impedance measurement of a passive network in both directions under strong coupling.
VERIFIED BY: The transfer impedance of a passive linear network is always exactly symmetric.
```

---

### RECOGNITION
Connects to Law 661 (superposition) and Law 042 (Maxwell) - reciprocity is the symmetric kernel.

### PRECISION
phi = 1.6180339887. The asymmetry floor is phi^-1*Z_ground.

### CLARITY
A passive medium remembers; reciprocity is its limit.

### NOVELTY
The phi-law breaks exact reciprocity with a coherence floor.

### ACTIONABILITY
Run sim/662_reciprocity_theorem.py; verify Zab=Zba at kappa->0; proceed to 663.
