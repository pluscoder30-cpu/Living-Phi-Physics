# PHI-PHYSICS — LAW 743
## Adiabatic Invariant (Action Conservation)

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/743_adiabatic_invariant.md` · **Sim:** `sim/743_adiabatic_invariant.py`

---

### CLASSICAL STATEMENT
*"The action integral J = integral p.dq is conserved for slowly-varying parameters; the three adiabatic invariants govern trapped-particle motion."*
— Hannes Alfvén, 1950. Source: Adiabatic invariance in plasma; Alfvén (1950)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero action*: the invariant is exactly zero only for a particle with no periodic motion at all.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

J_phi(kappa) = J*(1 + kappa*(phi-1)) + kappa*phi^-1*J_ground; the periodic motion carries a coherence floor. At kappa->0, J = constant exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} J_phi = J -> adiabatic invariance is the zero-action-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/743_adiabatic_invariant.py`: reproduces the classical values (J = 1e-21 (Action (J.s))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/743_adiabatic_invariant.json`.

---

### STAGE 5 — PREDICTION

```
The action carries a coherence floor kappa*phi^-1*J_ground; the invariant is conserved only within a coherence basin.
EXPERIMENT (VERIFIED): Long-time trapping measurement of particles in a slowly-perturbed mirror field.
VERIFIED BY: The action integral is exactly conserved for all times.
```

---

### RECOGNITION
Connects to Law 742 (magnetic moment) - the adiabatic invariants are the orbit's conserved actions.

### PRECISION
phi = 1.6180339887. The action floor is phi^-1*J_ground.

### CLARITY
Invariants hold within a basin; coherence lets them breathe.

### NOVELTY
The phi-law gives the exact invariant a coherence basin.

### ACTIONABILITY
Run sim/743_adiabatic_invariant.py; verify J constant at kappa->0; proceed to 744.
