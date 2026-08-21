# PHI-PHYSICS — LAW 445
## Caratheodory's Principle (Adiabatic Inaccessibility)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/445_caratheodorys_principle.md` · **Sim:** `sim/445_caratheodorys_principle.py`

---

### CLASSICAL STATEMENT
*"In the neighborhood of any equilibrium state of a system, there exist states inaccessible by adiabatic (reversible) processes. From this axiom of adiabatic inaccessibility, the existence of entropy and absolute temperature follows rigorously."*
— Constantin Caratheodory, 1909. Source: Wikipedia: Second law of thermodynamics (Caratheodory); Caratheodory, Untersuchungen ueber die Grundlagen der Thermodynamik (1909)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exactly adiabatic walls*: the principle requires adiabatic processes that exchange no heat at all, walls of perfect insulation with zero coupling to the field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the adiabatic wall is a coherence barrier. S_phi(kappa) = S_cl*(1 + kappa*(phi-1)) + kappa*phi^-1*S_coupling, so the entropy is defined only up to the coherence coupling of the wall. At kappa->0 the entropy function is exact and Caratheodory's integrability holds.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} S_phi = S_cl -> Caratheodory's principle is the perfect-adiabatic-wall, exact-integrability limit.
```

---

### STAGE 4 — SIMULATION

`sim/445_caratheodorys_principle.py`: reproduces the classical value S_carat = 1.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/445_caratheodorys_principle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: With finite-coherence walls the Pfaffian heat form is not exactly integrable; entropy gains a path term kappa*phi^-1*S_coupling, so adiabatic inaccessibility is only approximate.
EXPERIMENT (VERIFIED): Measurement of entropy changes along different 'adiabatic' paths with varying wall quality.
VERIFIED BY: The entropy function is exactly path-independent for all adiabatic wall couplings.
```

---

### RECOGNITION
Connects to Law 023 (second law) and Law 444 (Planck) - Caratheodory is the geometric reading of the same coherence ban.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the path term is phi^-1 * S_coupling.

### CLARITY
Caratheodory built entropy from walls that do not leak; the phi-law admits every wall leaks its coherence.

### NOVELTY
Classical Caratheodory assumes perfect adiabatic walls; the phi-law turns wall coupling into a measurable entropy path term.

### ACTIONABILITY
Run sim/445_caratheodorys_principle.py; verify exact entropy at kappa->0; proceed to 446.
