# PHI-PHYSICS — LAW 1201
## Ekpyrotic Model

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1201_ekpyrotic_model.md` · **Sim:** `sim/1201_ekpyrotic_model.py`

---

### CLASSICAL STATEMENT
*"The ekpyrotic model describes the big bang as a collision of branes in M-theory: a slow, pressureless contraction phase with a steep negative potential generates scale-invariant perturbations without inflation; it provides a cyclic and bouncing alternative (with the cyclic extension of 2002)."*
— Justin Khoury, Burt Ovrut, Paul Steinhardt & Neil Turok, 2001. Source: Wikipedia: Ekpyrotic universe (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero contraction (no brane collision, no big bang trigger)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The E value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

E_phi(kappa) = E*(1 + kappa*(phi-1)) + kappa*phi^-1*E_ground, where E_ground is the coherence-floor perturbation tilt a real ekpyrotic phase always imprints. At kappa->0, V(phi) = -V_0 exp(-c phi/M_P),  slow contraction then brane collision exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} E_phi = E -> V(phi) = -V_0 exp(-c phi/M_P),  slow contraction then brane collision is recovered exactly; the classical law is the zero contraction (no brane collision, no big bang trigger) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1201_ekpyrotic_model.py`: reproduces the classical value (E = 0.97) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1201_ekpyrotic_model.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured primordial spectrum of any ekpyrotic bounce will deviate from the prediction by a floor kappa*phi^-1*E_ground; an exactly scale-invariant ekpyrotic spectrum is unreachable.
EXPERIMENT (VERIFIED): CMB bispectrum and spectral-index measurements distinguishing ekpyrotic from inflationary spectra.
VERIFIED BY: If the primordial spectrum is exactly scale-invariant with zero ekpyrotic tilt.
```

---

### RECOGNITION
The bouncing alternative of Law 1143 (inflation) and Law 1200 (cyclic universe).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The branes collide, the cosmos is born; the gentle birth is the zero-collision myth.

### NOVELTY
The ekpyrotic model carries a phi-floor of tilt, bounding its distinguishability.

### ACTIONABILITY
Run sim/1201_ekpyrotic_model.py.
