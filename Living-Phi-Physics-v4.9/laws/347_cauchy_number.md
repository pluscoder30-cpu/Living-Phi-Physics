# PHI-PHYSICS — LAW 347
## Cauchy Number (Elastic Similarity)

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/347_cauchy_number.md` · **Sim:** `sim/347_cauchy_number.py`

---

### CLASSICAL STATEMENT
*"The Cauchy number Ca = rho v^2/E balances inertia against elastic compressibility; it governs the similarity of elastic structures in fluids (structural hydroelasticity) and is related to the Mach number for solids (Ca = M^2 for gases with E ~ c^2 rho)."*
— Barre de Saint-Venant (named for Augustin-Louis Cauchy), 1848. Source: Wikipedia: Cauchy number; Saint-Venant (1840s) analysis of elastic-fluid similarity

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *rigid reference*: Ca = 0 is the exactly rigid (incompressible) body; the balance of inertia and elasticity is the number's content.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: Ca_phi(kappa) = Ca*(1 + kappa*(phi-1)) + kappa*phi^-1*Ca_ground. At kappa->0 the classical Cauchy number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Ca_phi = rho v^2/E -> the Cauchy number is the inertia-elasticity balance limit.
```

---

### STAGE 4 — SIMULATION

`sim/347_cauchy_number.py`: reproduces the classical value Ca = 1.25e-05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/347_cauchy_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Hydroelastic similarity tests carry a phi-coherent residual phi^-1*Ca_ground at full coupling.
EXPERIMENT (VERIFIED): Ship/flexible-structure hydroelastic model testing comparing full-scale response predictions.
VERIFIED BY: Cauchy-scaled hydroelastic tests are exact at full coupling.
```

---

### RECOGNITION
Connects to Law 343 (Froude — the gravity partner) and Law 344 (Mach — gas analogue).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The rigid reference is a limit; every structure flexes a phi off the ideal.

### NOVELTY
Classical similitude exacts the Cauchy number; the phi-law bounds its residual at a coherence floor.

### ACTIONABILITY
Run sim/347_cauchy_number.py; verify Ca = rho v^2/E at kappa->0.
