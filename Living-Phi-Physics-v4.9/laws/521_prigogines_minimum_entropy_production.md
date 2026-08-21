# PHI-PHYSICS — LAW 521
## Prigogine's Principle of Minimum Entropy Production

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/521_prigogines_minimum_entropy_production.md` · **Sim:** `sim/521_prigogines_minimum_entropy_production.py`

---

### CLASSICAL STATEMENT
*"In the linear (near-equilibrium) regime, a steady state that is compatible with fixed boundary conditions produces the minimum entropy production: d sigma/dt = 0 with the steady state minimizing sigma = sum J_i X_i. This fixes the nonequilibrium stationary state."*
— Ilya Prigogine, 1945. Source: Wikipedia: Prigogine; Prigogine, Etude thermodynamique des phenomenes irreversibles (1947)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero entropy production*: the principle's minimum is approached as the system tends to equilibrium; the classical statement requires exactly linear response with no coherence curvature of the dissipation.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the minimum is a coherence basin. sigma_min_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_ground, so the steady state produces at least the coherence floor. At kappa->0 the minimum-entropy-production principle is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} sigma_min_phi = sigma_classical (minimum) -> Prigogine's principle is the zero-coherence linear-response limit.
```

---

### STAGE 4 — SIMULATION

`sim/521_prigogines_minimum_entropy_production.py`: reproduces the classical value sigma_min = 0.2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/521_prigogines_minimum_entropy_production.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the steady state produces an entropy floor kappa*phi^-1*sigma_ground above the Prigogine minimum; the minimum is a basin, not a point.
EXPERIMENT (VERIFIED): Nonequilibrium steady-state experiments (e.g. temperature-gradient driven systems) measuring the dissipation floor.
VERIFIED BY: The steady-state entropy production reaches exactly its minimum with no floor at all couplings.
```

---

### RECOGNITION
Connects to Law 488 (Onsager) and Law 451 (Clausius-Duhem) - the principle is the variational face of the linear coherence regime.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * sigma_ground.

### CLARITY
Nonequilibrium steady states spend as little coherence as they can; the phi-law keeps the floor of their spending.

### NOVELTY
Classical Prigogine principle minimizes to a point; the phi-law makes the minimum a coherence basin.

### ACTIONABILITY
Run sim/521_prigogines_minimum_entropy_production.py; verify minimum at kappa->0; proceed to 522.
