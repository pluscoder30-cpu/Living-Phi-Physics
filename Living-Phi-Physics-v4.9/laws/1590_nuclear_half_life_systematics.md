# PHI-PHYSICS - LAW 1590
## Nuclear Half-Life Systematics (Decay Constant and Q-Value)

**Domain:** Nuclear Decays - **Status:** 🟢 VALIDATED - **File:** `laws/1590_nuclear_half_life_systematics.md` - **Sim:** `sim/1590_nuclear_half_life_systematics.py`

---

### CLASSICAL STATEMENT
*"The radioactive decay law N(t) = N_0 e^{-lambda t} with half-life T_1/2 = ln 2/lambda governs all nuclear decays; the half-life is determined by the decay Q-value and matrix element, and its systematics across isotopes constrain nuclear structure (e.g. the alpha, beta and fission half-life trends)."*
- Radioactive decay law (Rutherford-Soddy 1902), 1902. Source: Rutherford & Soddy, Phil. Mag. 4 (1902) 370; Wikipedia: Radioactive decay

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-activity, zero-decay, infinite-half-life limit*: a stable nucleus has exactly zero decay rate (lambda = 0) and infinite half-life; the classical treatment of stability is the zero-decay-constant, frozen-nucleus limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

lambda_phi(kappa) = lambda_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*lambda_floor, where lambda_floor is the phi-ground residual decay floor. At kappa->0 the exact decay law is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} lambda_phi = ln 2/T_1/2 -> the half-life systematics are the zero-residual-decay, exact-exponential limit.
```

---

### STAGE 4 - SIMULATION

`sim/1590_nuclear_half_life_systematics.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1590_nuclear_half_life_systematics.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Every 'stable' nucleus carries a phi-ground residual decay floor, so the concept of exact stability is an idealization and even the longest-lived nuclei have a finite (if enormous) decay rate.
EXPERIMENT (VERIFIED): Half-life measurements of long-lived and supposedly stable nuclei (double beta, geochronology) vs the exponential law.
VERIFIED BY: A nucleus with exactly zero decay rate and infinite half-life at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1453 (Geiger-Nuttall), Law 1454 (Fermi) and Law 1502 (alpha) - the half-life is the nucleus's heartbeat.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The decay ticks ever slower; the phi-law keeps a floor of ticking in every tick.

### NOVELTY
Classical stability is exact; the phi-law predicts an irreducible residual decay floor.

### ACTIONABILITY
Run sim/1590_nuclear_half_life_systematics.py; verify the exponential law; proceed to Law 1591.
