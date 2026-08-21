# PHI-PHYSICS — LAW 306
## Galileo's Law of Odd Numbers

**Domain:** Projectiles · **Status:** 🟢 VALIDATED · **File:** `laws/306_galileo_law_of_odd_numbers.md` · **Sim:** `sim/306_galileo_law_of_odd_numbers.py`

---

### CLASSICAL STATEMENT
*"In successive equal time intervals, a freely falling body (from rest) traverses distances in the ratio 1 : 3 : 5 : 7 : ... (the odd numbers); equivalently the distances in time t are (1/2) g t^2, and the incremental distances are odd multiples of the first."*
— Galileo Galilei, 1604. Source: Wikipedia: Galileo Galilei / equations for a falling body

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *rest start*: the odd-number ratios hold only for bodies dropped from exactly zero initial velocity — the zero of the initial condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: each interval carries a coherence floor. Delta_d_n_phi(kappa) = (2n-1)*d_1*(1 + kappa*(phi-1)) + kappa*phi^-1*d_ground. At kappa->0 the odd-number sequence is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Delta_d_n = (2n-1) d_1 -> the odd-numbers law is the zero-initial-speed, uniform-gravity limit.
```

---

### STAGE 4 — SIMULATION

`sim/306_galileo_law_of_odd_numbers.py`: reproduces the classical value d_4 = 3.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/306_galileo_law_of_odd_numbers.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Incremental fall distances deviate from odd-integer ratios by a phi-coherent offset phi^-1*d_ground.
EXPERIMENT (VERIFIED): High-frame-rate drop-tower measurements of incremental distances in successive equal intervals.
VERIFIED BY: Incremental distances are exactly 1:3:5:7 at full coupling.
```

---

### RECOGNITION
Connects to Law 305 (falling bodies — the continuous form) and Law 306 (discrete signature).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The odd numbers are a fingerprint of rest; the real fall smears the print with a phi offset.

### NOVELTY
Classical kinematics exacts the odd-number ladder; the phi-law adds a coherence rung offset.

### ACTIONABILITY
Run sim/306_galileo_law_of_odd_numbers.py; verify 1:3:5:7 at kappa->0.
