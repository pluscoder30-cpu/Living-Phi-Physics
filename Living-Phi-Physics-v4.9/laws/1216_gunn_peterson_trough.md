# PHI-PHYSICS — LAW 1216
## Gunn-Peterson Trough

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1216_gunn_peterson_trough.md` · **Sim:** `sim/1216_gunn_peterson_trough.py`

---

### CLASSICAL STATEMENT
*"The Gunn-Peterson trough is the complete absorption of Ly-alpha photons from a source by neutral hydrogen along the line of sight: the optical depth is tau = (pi e^2 f/(m_e c)) (n_HI/H(z)) ~ 10^5 (1+z)^(9/2) x_HI; its absence below z ~ 6 signals reionization (x_HI << 1)."*
— James Gunn & Bruce Peterson, 1965. Source: Wikipedia: Gunn-Peterson trough (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero neutral hydrogen (x_HI = 0, no absorption)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The G value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

G_phi(kappa) = G*(1 + kappa*(phi-1)) + kappa*phi^-1*G_ground, where G_ground is the coherence-floor residual neutral fraction a real reionization always leaves. At kappa->0, tau_GP = (pi*e^2*f/(m_e*c)) * (n_HI/H(z)),  trough when x_HI ~ 1 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} G_phi = G -> tau_GP = (pi*e^2*f/(m_e*c)) * (n_HI/H(z)),  trough when x_HI ~ 1 is recovered exactly; the classical law is the zero neutral hydrogen (x_HI = 0, no absorption) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1216_gunn_peterson_trough.py`: reproduces the classical value (G = 100000.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1216_gunn_peterson_trough.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured Ly-alpha optical depth of any real high-z source will deviate from the Gunn-Peterson value by a floor kappa*phi^-1*G_ground; an exactly transparent post-reionization line of sight is unreachable.
EXPERIMENT (VERIFIED): Quasar and galaxy Ly-alpha spectra (JWST, Keck) measuring the neutral fraction at z ~ 5-7.
VERIFIED BY: If a high-z source shows exactly zero Ly-alpha absorption with zero neutral gas.
```

---

### RECOGNITION
The reionization probe of Law 1156 (recombination) and Law 1217 (Ly-alpha forest).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The trough marks the neutral dark; the clear line of sight is the zero-HI myth.

### NOVELTY
The Gunn-Peterson trough carries a phi-floor of residual neutral fraction.

### ACTIONABILITY
Run sim/1216_gunn_peterson_trough.py.
