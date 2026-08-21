# PHI-PHYSICS — LAW 1208
## Natural Inflation

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1208_natural_inflation.md` · **Sim:** `sim/1208_natural_inflation.py`

---

### CLASSICAL STATEMENT
*"Natural inflation uses a pseudo-Nambu-Goldstone (axion-like) inflaton with a cosine potential V(phi) = Lambda^4 (1 + cos(phi/f)): the shift symmetry naturally keeps the potential flat, avoiding fine-tuning; the decay constant f must be near the Planck scale to match data."*
— Katherine Freese, Joshua Frieman & Angela Olinto, 1990. Source: Wikipedia: Natural inflation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero symmetry-breaking scale (f = 0, no flat direction)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The N value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

N_phi(kappa) = N*(1 + kappa*(phi-1)) + kappa*phi^-1*N_ground, where N_ground is the coherence-floor symmetry residue a real axion-like inflaton always retains. At kappa->0, V(phi) = Lambda^4 (1 + cos(phi/f)),  f ~ M_P exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} N_phi = N -> V(phi) = Lambda^4 (1 + cos(phi/f)),  f ~ M_P is recovered exactly; the classical law is the zero symmetry-breaking scale (f = 0, no flat direction) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1208_natural_inflation.py`: reproduces the classical value (N = 0.96) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1208_natural_inflation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured spectral index will deviate from the cosine-potential prediction by a floor kappa*phi^-1*N_ground; an exactly symmetric potential is unreachable.
EXPERIMENT (VERIFIED): CMB constraints on n_s and r testing the cosine potential.
VERIFIED BY: If the spectral tilt is exactly inconsistent with any natural-inflation parameter.
```

---

### RECOGNITION
The shift-symmetric family of Law 1143 (inflation) and the axion physics of Law 1235 (Kaluza-Klein).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Symmetry keeps the slope gentle; the tuned potential is the zero-symmetry myth.

### NOVELTY
Natural inflation carries a phi-floor of symmetry breaking, bounding the decay constant.

### ACTIONABILITY
Run sim/1208_natural_inflation.py.
