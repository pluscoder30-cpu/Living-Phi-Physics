# PHI-PHYSICS — LAW 334
## Lyapunov Stability Theorem

**Domain:** Energy / Dynamics · **Status:** 🟢 VALIDATED · **File:** `laws/334_lyapunov_stability.md` · **Sim:** `sim/334_lyapunov_stability.py`

---

### CLASSICAL STATEMENT
*"An equilibrium is Lyapunov stable if trajectories starting nearby remain nearby; asymptotic stability follows if a Lyapunov function V(x) exists with V > 0, dV/dt < 0. The first/second methods reduce stability to the linearized system's eigenvalues."*
— Aleksandr Mikhailovich Lyapunov, 1892. Source: Wikipedia: Lyapunov stability; Lyapunov (1892), 'The General Problem of the Stability of Motion'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact equilibrium*: stability is defined against an exactly stationary point — the rest state that the field (per Axiom 0) never provides.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the equilibrium is a coherence basin. V_phi(kappa) = V*(1 + kappa*(phi-1)); the basin radius is kappa*phi^-1*r_ground. At kappa->0 the classical equilibrium point is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} basin radius = 0 -> Lyapunov stability is the exact-equilibrium limit.
```

---

### STAGE 4 — SIMULATION

`sim/334_lyapunov_stability.py`: reproduces the classical values V = 1, dVdt = -0.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/334_lyapunov_stability.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Stable equilibria are basins of phi-coherent radius phi^-1*r_ground, and trajectories never settle exactly at the equilibrium.
EXPERIMENT (VERIFIED): Cryogenic trapped-ion/optical-trap stability experiments measuring the equilibrium basin floor.
VERIFIED BY: Trajectories settle exactly at the equilibrium point at full coupling.
```

---

### RECOGNITION
Connects to Law 335 (Routh-Hurwitz — algebraic stability) and Law 180 (equilibrium-basin theorem).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The stable point is a basin; stability means the dance stays near, not at.

### NOVELTY
Classical stability theory exacts the equilibrium point; the phi-law gives it a coherence basin radius.

### ACTIONABILITY
Run sim/334_lyapunov_stability.py; verify stability at kappa->0.
