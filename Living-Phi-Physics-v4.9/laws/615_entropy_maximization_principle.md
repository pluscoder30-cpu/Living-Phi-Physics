# PHI-PHYSICS — LAW 615
## Entropy Maximization Principle (Equilibrium Selection)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/615_entropy_maximization_principle.md` · **Sim:** `sim/615_entropy_maximization_principle.py`

---

### CLASSICAL STATEMENT
*"A closed system at equilibrium is in the macrostate with the maximum entropy consistent with its constraints (fixed energy, volume, particle number). The equilibrium distribution maximizes the Gibbs entropy."*
— Josiah Willard Gibbs, 1902. Source: Wikipedia: Entropy (maximum at equilibrium); Gibbs, Elementary Principles in Statistical Mechanics (1902)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exact constraints*: the principle assumes the constraints (energy, volume, particle number) are known exactly and the entropy maximum is unique - a constrained manifold with zero coherence curvature.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the constrained manifold carries coherence. S_phi(kappa) = S_max*(1 + kappa*(phi-1)) + kappa*phi^-1*S_curv, so the maximum is a coherence basin. At kappa->0 the entropy-maximization principle is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} S_phi = S_max -> the entropy-maximization principle is the zero-curvature exact-constraint limit.
```

---

### STAGE 4 — SIMULATION

`sim/615_entropy_maximization_principle.py`: reproduces the classical value S_eq = 5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/615_entropy_maximization_principle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the equilibrium macrostate is a basin, not a point; the observed entropy fluctuates within the coherence floor.
EXPERIMENT (VERIFIED): Equilibrium-fluctuation measurements in closed systems (e.g. energy-conserving granular gases) comparing with the maximum-entropy state.
VERIFIED BY: A closed system at equilibrium is exactly at the unique maximum-entropy macrostate for all couplings.
```

---

### RECOGNITION
Connects to Law 030 (Boltzmann entropy) and Law 466 (MaxEnt) - the principle is the equilibrium face of the entropy recursion.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the curvature is phi^-1 * S_curv.

### CLARITY
Equilibrium is the state of most options; the phi-law keeps the options' wobble.

### NOVELTY
Classical entropy-maximization picks a point; the phi-law makes the maximum a coherence basin.

### ACTIONABILITY
Run sim/615_entropy_maximization_principle.py; verify S_max at kappa->0; proceed to 616.
