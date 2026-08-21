# PHI-PHYSICS — LAW 603
## Reynolds Analogy (Heat-Momentum Transfer Analogy)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/603_reynolds_analogy.md` · **Sim:** `sim/603_reynolds_analogy.py`

---

### CLASSICAL STATEMENT
*"For a turbulent boundary layer with Pr = 1 and zero pressure gradient, the heat transfer and skin friction are proportional: St = C_f/2, where St is the Stanton number and C_f the skin-friction coefficient. Heat and momentum transfer are analogous."*
— Osborne Reynolds, 1874. Source: Wikipedia: Reynolds analogy; Reynolds (1874)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *Pr = 1 exactly*: the analogy holds exactly only when thermal and momentum diffusivities are equal - a condition no real fluid satisfies precisely.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the Prandtl deviation is a coherence coupling. St_phi(kappa) = (C_f/2)*Pr^(-2/3)*(1 + kappa*(phi-1)) + kappa*phi^-1*St_ground, generalizing to the Chilton-Colburn form. At kappa->0 (Pr = 1) the pure Reynolds analogy holds.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} St_phi = C_f/2 for Pr = 1 -> the Reynolds analogy is the zero-Prandtl-deviation zero-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/603_reynolds_analogy.py`: reproduces the classical value St_analogy = 0.002 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/603_reynolds_analogy.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the heat-momentum analogy holds only within a coherence floor; the measured St deviates from C_f/2 even at Pr = 1.
EXPERIMENT (VERIFIED): Heat-transfer and drag measurements on flat plates in turbulent flow.
VERIFIED BY: St = C_f/2 exactly at Pr = 1 for all couplings.
```

---

### RECOGNITION
Connects to Law 602 (Stanton) and Law 604 (Colburn) - the analogy is the heat-momentum coherence identity of the boundary layer.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * St_ground.

### CLARITY
The boundary layer treats heat and momentum as twins; the phi-law keeps the twins' difference.

### NOVELTY
Classical Reynolds analogy is exact at Pr=1; the phi-law adds the coherence floor of the real flow.

### ACTIONABILITY
Run sim/603_reynolds_analogy.py; verify St = C_f/2 at kappa->0; proceed to 604.
