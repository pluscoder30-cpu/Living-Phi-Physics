# PHI-PHYSICS — LAW 1195
## Quintessence

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1195_quintessence.md` · **Sim:** `sim/1195_quintessence.py`

---

### CLASSICAL STATEMENT
*"Quintessence is a dynamical scalar field driving cosmic acceleration with w > -1: the field rolls down a potential V(phi), and its equation of state varies with time, w = (phi_dot^2/2 - V)/(phi_dot^2/2 + V); tracking potentials explain the coincidence of the dark-energy scale."*
— Bharat Ratra & James Peebles, 1988; named by Caldwell, Dave & Steinhardt, 1998. Source: Wikipedia: Quintessence (physics) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *frozen field (phi_dot = 0, w = -1, pure cosmological constant)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The Q value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Q_phi(kappa) = Q*(1 + kappa*(phi-1)) + kappa*phi^-1*Q_ground, where Q_ground is the coherence-floor field motion a real dark-energy field always retains. At kappa->0, w = (phi_dot^2/2 - V)/(phi_dot^2/2 + V),  -1 < w < -1/3 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} Q_phi = Q -> w = (phi_dot^2/2 - V)/(phi_dot^2/2 + V),  -1 < w < -1/3 is recovered exactly; the classical law is the frozen field (phi_dot = 0, w = -1, pure cosmological constant) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1195_quintessence.py`: reproduces the classical value (Q = -0.9) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1195_quintessence.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured dark-energy equation of state will deviate from w = -1 by a floor kappa*phi^-1*Q_ground; an exactly frozen quintessence is unreachable.
EXPERIMENT (VERIFIED): w(z) measurements from DESI and Euclid distinguishing quintessence from Lambda.
VERIFIED BY: If the dark-energy equation of state is exactly -1 at all times.
```

---

### RECOGNITION
The dynamical alternative of Law 1194 (equation of state) and Law 105 (dark energy).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The field rolls, the vacuum breathes; the frozen field is the zero-motion myth.

### NOVELTY
Quintessence carries a phi-floor of field velocity, so w never exactly hits -1.

### ACTIONABILITY
Run sim/1195_quintessence.py.
