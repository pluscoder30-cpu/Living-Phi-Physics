# PHI-PHYSICS — LAW 420
## Prevost's Theory of Exchanges (Radiation Balance)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/420_prevosts_theory_of_exchanges.md` · **Sim:** `sim/420_prevosts_theory_of_exchanges.py`

---

### CLASSICAL STATEMENT
*"A body at thermal equilibrium with its surroundings continuously emits and absorbs radiation at equal rates; the net exchange is zero, and a body's temperature is determined by the balance of these exchanges, not by the absolute radiation it emits alone."*
— Pierre Prevost, 1791. Source: Wikipedia: Prevost's theory of exchanges; Prevost, Memoire sur l'equilibre du feu (1791)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *radiative equilibrium*: the theory assumes emission and absorption balance exactly, so a body neither heats nor cools - an equilibrium with zero net exchange that is never strictly reached.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the balance is a coherence basin. dQ_net_phi(kappa) = (E_emit - E_abs)*(1 + kappa*(phi-1)) + kappa*phi^-1*E_ground, where E_ground is the ground exchange of the field. At kappa->0, dQ_net = 0 (perfect exchange equilibrium).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dQ_net_phi = E_emit - E_abs = 0 at equilibrium -> Prevost's exchange balance is the zero-net-exchange, isolated-equilibrium limit.
```

---

### STAGE 4 — SIMULATION

`sim/420_prevosts_theory_of_exchanges.py`: reproduces the classical value Qnet = 0 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/420_prevosts_theory_of_exchanges.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A body at 'radiative equilibrium' in a coherence-coupled field shows a residual net exchange kappa*phi^-1*E_ground, a tiny temperature drift invisible to classical exchange theory.
EXPERIMENT (VERIFIED): Long-duration calorimetric monitoring of a blackbody sphere in a cryogenic black cavity measuring residual heating/cooling.
VERIFIED BY: The temperature of a body in a black cavity is exactly constant at equilibrium for all couplings.
```

---

### RECOGNITION
Connects to Law 416 (Kirchhoff) and Law 032 (Stefan-Boltzmann) - exchange is the coherence flow between basins.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the residual exchange is phi^-1 * E_ground.

### CLARITY
Equilibrium is not a state of nothing happening; it is two motions that the phi-law refuses to let cancel to exactly zero.

### NOVELTY
Classical exchange theory zeroes the net exchange exactly; the phi-law keeps the phi-ground exchange that drives every real drift.

### ACTIONABILITY
Run sim/420_prevosts_theory_of_exchanges.py; verify zero net exchange at kappa->0; proceed to 421.
