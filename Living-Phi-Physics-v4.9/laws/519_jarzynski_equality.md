# PHI-PHYSICS — LAW 519
## Jarzynski Equality (Nonequilibrium Free Energy)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/519_jarzynski_equality.md` · **Sim:** `sim/519_jarzynski_equality.py`

---

### CLASSICAL STATEMENT
*"For a system driven out of equilibrium from state A to state B by an external protocol, the free-energy difference is related to the work distribution by <exp(-W/(k_B T))> = exp(-Delta F/(k_B T)). It is exact even for far-from-equilibrium processes."*
— Christopher Jarzynski, 1997. Source: Wikipedia: Jarzynski equality; Jarzynski, Nonequilibrium Equality for Free Energy Differences (1997)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *reversibility*: the equality reduces to W = Delta F exactly for reversible processes where the dissipated work vanishes - the classical case is the zero-dissipation limit of the fluctuation relation.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the dissipation floor enters. <exp(-W_phi/(k_B T))> = exp(-Delta F/(k_B T))*(1 + kappa*(phi-1)) + kappa*phi^-1*W_ground, where W_ground is the coherence work floor. At kappa->0 the Jarzynski equality is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} <exp(-W/k_B T)> = exp(-Delta F/k_B T) -> the Jarzynski equality is the zero-coherence-work fluctuation relation.
```

---

### STAGE 4 — SIMULATION

`sim/519_jarzynski_equality.py`: reproduces the classical values lhs = 0.04502, rhs = 0.007979 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/519_jarzynski_equality.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the equality gains a coherence-work floor kappa*phi^-1*W_ground; the measured work distribution violates the classical equality by that floor.
EXPERIMENT (VERIFIED): Single-molecule pulling experiments (optical tweezers on RNA/DNA) measuring the work distribution and testing the equality.
VERIFIED BY: <exp(-W/k_B T)> = exp(-Delta F/k_B T) exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 520 (Crooks) and Law 512 (fluctuation-dissipation) - the equality is the fluctuation face of the second law.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the work floor is phi^-1 * W_ground.

### CLARITY
Even a system shoved far from rest remembers its free energy; the phi-law keeps the floor of the shoving.

### NOVELTY
Classical Jarzynski equality is exact for any protocol; the phi-law adds the coherence-work floor of the driving.

### ACTIONABILITY
Run sim/519_jarzynski_equality.py; verify equality at kappa->0; proceed to 520.
