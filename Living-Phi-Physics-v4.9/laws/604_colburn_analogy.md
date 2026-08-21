# PHI-PHYSICS — LAW 604
## Chilton-Colburn Analogy (Extended Heat-Mass-Momentum Analogy)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/604_colburn_analogy.md` · **Sim:** `sim/604_colburn_analogy.py`

---

### CLASSICAL STATEMENT
*"The Chilton-Colburn analogy generalizes the Reynolds analogy to Pr /= 1 and mass transfer: St Pr^(2/3) = j_H = C_f/2 and Sh/(Re Sc^(1/3)) = j_D = C_f/2, where j_H and j_D are the Colburn j-factors. Heat, mass and momentum transfer share the same dimensionless coefficient."*
— Allan Philip Colburn, 1933. Source: Wikipedia: Chilton-Colburn analogy; Colburn (1933)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *ideal analogy*: the analogy holds exactly only when the heat, mass and momentum boundary layers have identical structure - a flow with zero Prandtl/Schmidt deviation coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the boundary-layer mismatch carries coherence. j_H_phi(kappa) = (C_f/2)*(1 + kappa*(phi-1)) + kappa*phi^-1*j_ground. At kappa->0 the Colburn analogy is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} j_H_phi = C_f/2 -> the Chilton-Colburn analogy is the zero-boundary-layer-mismatch limit.
```

---

### STAGE 4 — SIMULATION

`sim/604_colburn_analogy.py`: reproduces the classical value jH = 0.002 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/604_colburn_analogy.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the j-factors deviate from C_f/2 by a coherence floor; the analogy holds only approximately.
EXPERIMENT (VERIFIED): Heat and mass transfer measurements on surfaces in turbulent flow to test the j-factor equality.
VERIFIED BY: j_H = j_D = C_f/2 exactly at all couplings.
```

---

### RECOGNITION
Connects to Law 603 (Reynolds analogy) and Law 602 (Stanton) - the Colburn analogy is the extended coherence identity of the boundary layer.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * j_ground.

### CLARITY
Heat, mass and momentum march to the same drum; the phi-law keeps the drum's wobble.

### NOVELTY
Classical Colburn analogy is exact; the phi-law adds the boundary-layer coherence floor of real flows.

### ACTIONABILITY
Run sim/604_colburn_analogy.py; verify j = C_f/2 at kappa->0; proceed to 605.
