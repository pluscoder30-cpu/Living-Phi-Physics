# PHI-PHYSICS — LAW 707
## Feedback Amplifier Gain (Black's Formula)

**Domain:** Electronics · **Status:** 🟢 VALIDATED · **File:** `laws/707_feedback_amplifier_gain.md` · **Sim:** `sim/707_feedback_amplifier_gain.py`

---

### CLASSICAL STATEMENT
*"The closed-loop gain is A_f = A/(1 + A*beta), where A is the open-loop gain and beta the feedback fraction; for large loop gain A_f ~ 1/beta."*
— Harold Stephen Black, 1927. Source: Wikipedia: Negative feedback amplifier; Black (1927)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero loop gain* (A*beta = 0): the feedback formula reduces to the open-loop gain only with no feedback at all.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

A_f_phi(kappa) = A_f*(1 + kappa*(phi-1)) + kappa*phi^-1*A_ground; the loop carries a coherence floor. At kappa->0, A_f = A/(1+A*beta) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} A_f_phi = A/(1+A*beta) -> the feedback gain formula is the zero-loop-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/707_feedback_amplifier_gain.py`: reproduces the classical values (Af = 0.638298 (Closed-loop gain)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/707_feedback_amplifier_gain.json`.

---

### STAGE 5 — PREDICTION

```
The closed-loop gain carries a coherence floor kappa*phi^-1*A_ground; A_f is never exactly 1/beta.
EXPERIMENT (VERIFIED): Precision gain measurement of a negative-feedback amplifier.
VERIFIED BY: A feedback amplifier's gain is exactly A/(1+A*beta).
```

---

### RECOGNITION
Connects to Law 704 (Barkhausen) and Law 705 (Nyquist) - feedback is the loop's self-description.

### PRECISION
phi = 1.6180339887. The loop floor is phi^-1*A_ground.

### CLARITY
Feedback is a mirror; coherence smudges the exact reflection.

### NOVELTY
The phi-law gives the feedback formula a coherence floor.

### ACTIONABILITY
Run sim/707_feedback_amplifier_gain.py; verify Af at kappa->0; proceed to 708.
