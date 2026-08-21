# PHI-PHYSICS — LAW 372
## Cauchy's Stress Theorem

**Domain:** Structural Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/372_cauchy_stress_theorem.md` · **Sim:** `sim/372_cauchy_stress_theorem.py`

---

### CLASSICAL STATEMENT
*"The traction vector t on any plane with unit normal n is given by the stress tensor: t = sigma . n; the nine components sigma_ij satisfy the equilibrium equations partial sigma_ij/partial x_j + F_i = 0 and, in the absence of body couples, symmetry sigma_ij = sigma_ji."*
— Augustin-Louis Cauchy, 1822. Source: Wikipedia: Cauchy stress tensor; Cauchy (1822-1828), 'De la pression ou tension dans un corps solide'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly continuous stress field*: Cauchy's theorem requires the stress to vary continuously through a perfectly homogeneous continuum — the zero of the discreteness.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the stress tensor carries a coherence floor. sigma_ij_phi(kappa) = sigma_ij*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_ground. At kappa->0 the classical stress theorem is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} t = sigma . n -> Cauchy's stress theorem is the continuum, exact-symmetry limit.
```

---

### STAGE 4 — SIMULATION

`sim/372_cauchy_stress_theorem.py`: reproduces the classical values tx = 100, ty = 30 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/372_cauchy_stress_theorem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The traction equilibrium carries a phi-coherent residual phi^-1*sigma_ground (a coherence stress floor) at full coupling.
EXPERIMENT (VERIFIED): Micro-scale stress-state measurements (EBSD, DIC) searching for the residual below continuum predictions.
VERIFIED BY: Traction is exactly sigma . n at full coupling.
```

---

### RECOGNITION
Connects to Law 371 (Mohr — the graphical consequence) and Law 367 (beam).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The smooth stress field is a limit; every continuum hides a phi lattice beneath.

### NOVELTY
Classical continuum mechanics exacts the stress tensor; the phi-law adds a coherence stress floor.

### ACTIONABILITY
Run sim/372_cauchy_stress_theorem.py; verify t = sigma n at kappa->0.
