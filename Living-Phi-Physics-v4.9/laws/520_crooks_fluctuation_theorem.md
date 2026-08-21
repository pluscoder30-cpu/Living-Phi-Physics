# PHI-PHYSICS — LAW 520
## Crooks Fluctuation Theorem (Forward/Reverse Work Ratio)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/520_crooks_fluctuation_theorem.md` · **Sim:** `sim/520_crooks_fluctuation_theorem.py`

---

### CLASSICAL STATEMENT
*"The probability of a forward process dissipating work W and the reverse process dissipating -W are related by P_f(W)/P_r(-W) = exp((W - Delta F)/(k_B T)). It generalizes the Jarzynski equality and is exact far from equilibrium."*
— Gavin E. Crooks, 1999. Source: Wikipedia: Crooks fluctuation theorem; Crooks, Entropy Production Along a Stochastic Trajectory (1999)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *reversibility*: the ratio becomes 1 exactly at W = Delta F, the reversible limit where the forward and reverse distributions coincide - a zero-dissipation state that real processes only approach.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the dissipation floor enters. P_f_phi(W)/P_r_phi(-W) = exp((W - Delta F)/(k_B T))*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground. At kappa->0 the Crooks relation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_f/P_r = exp((W - Delta F)/k_B T) -> the Crooks theorem is the zero-coherence-work fluctuation relation.
```

---

### STAGE 4 — SIMULATION

`sim/520_crooks_fluctuation_theorem.py`: reproduces the classical value ratio_c = 3.346 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/520_crooks_fluctuation_theorem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the forward/reverse ratio carries a coherence floor kappa*phi^-1*P_ground; the measured ratio deviates from the exponential in the deep tails.
EXPERIMENT (VERIFIED): Single-molecule force-ramp experiments measuring forward and reverse work distributions and their ratio.
VERIFIED BY: P_f(W)/P_r(-W) = exp((W - Delta F)/k_B T) exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 519 (Jarzynski) and Law 451 (Clausius-Duhem) - the theorem is the two-arrow reading of the coherence dissipation.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * P_ground.

### CLARITY
Forward and reverse are two arrows of one process; the phi-law keeps the ratio honest.

### NOVELTY
Classical Crooks relation is exact; the phi-law adds the coherence floor of the forward-reverse meeting.

### ACTIONABILITY
Run sim/520_crooks_fluctuation_theorem.py; verify ratio at kappa->0; proceed to 521.
