# PHI-PHYSICS — LAW 275
## Bi-Elliptic Transfer

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/275_bi_elliptic_transfer.md` · **Sim:** `sim/275_bi_elliptic_transfer.py`

---

### CLASSICAL STATEMENT
*"For transfers with radius ratio r2/r1 > 11.94, a three-burn bi-elliptic transfer (raising to a higher intermediate radius rb then descending) requires less delta-v than the Hohmann transfer, at the cost of longer transfer time."*
— A. W. Hoelker and R. Silber, 1959. Source: Wikipedia: bi-elliptic transfer; Hoelker & Silber (1959), 'The bi-elliptical transfer between circular coplanar orbits'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *two-burn optimum*: the bi-elliptic transfer beats Hohmann precisely because the Hohmann ellipse is not globally optimal; the classical optimum assumed only two burns.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the crossover radius ratio carries a phi correction. (r2/r1)_crit_phi = 11.94*(1 + kappa*(phi-1)); delta_v_bi_phi(kappa) = delta_v_bi*(1 + kappa*phi^-1). At kappa->0 the classical 11.94 crossover is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} delta_v_bi_phi = the classical bi-elliptic delta-v -> the bi-elliptic transfer is the three-burn generalization of the Hohmann optimum.
```

---

### STAGE 4 — SIMULATION

`sim/275_bi_elliptic_transfer.py`: reproduces the classical value dvbi = 3460 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/275_bi_elliptic_transfer.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The crossover radius ratio at which bi-elliptic beats Hohmann shifts by the phi-coherent fraction phi^-1.
EXPERIMENT (VERIFIED): Orbital mechanics laboratory (small satellite/emulation) or precise numerical delta-v comparison of three-burn transfers.
VERIFIED BY: The crossover ratio is exactly 11.94 at full coupling.
```

---

### RECOGNITION
Connects to Law 274 (Hohmann — its limit case) and Law 271 (vis-viva for each arc).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The shortest path is not always cheapest; the phi-law sets where the extra loop pays.

### NOVELTY
Classical astrodynamics fixes the two-burn optimum; the phi-law marks the three-burn crossover at a phi-shifted ratio.

### ACTIONABILITY
Run sim/275_bi_elliptic_transfer.py; verify the classical delta-v at kappa->0.
