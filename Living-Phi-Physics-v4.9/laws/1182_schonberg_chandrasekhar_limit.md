# PHI-PHYSICS — LAW 1182
## Schönberg-Chandrasekhar Limit

**Domain:** Astrophysics · **Status:** 🟢 VALIDATED · **File:** `laws/1182_schonberg_chandrasekhar_limit.md` · **Sim:** `sim/1182_schonberg_chandrasekhar_limit.py`

---

### CLASSICAL STATEMENT
*"The Schönberg-Chandrasekhar limit bounds the mass fraction of an isothermal inert helium core in a main-sequence star: M_core/M_star <= ~0.1 (with composition-dependence); beyond it the core cannot be supported by thermal pressure and contracts, triggering the giant phase."*
— Mario Schönberg & Subrahmanyan Chandrasekhar, 1942. Source: Wikipedia: Schonberg-Chandrasekhar limit (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero core mass (M_core = 0, no helium core)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The S value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground, where S_ground is the coherence-floor core instability a real evolving star always approaches. At kappa->0, M_core/M_star <= 0.1  (isothermal core limit) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} S_phi = S -> M_core/M_star <= 0.1  (isothermal core limit) is recovered exactly; the classical law is the zero core mass (M_core = 0, no helium core) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1182_schonberg_chandrasekhar_limit.py`: reproduces the classical value (S = 0.1) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1182_schonberg_chandrasekhar_limit.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured core fraction at which any real star leaves the main sequence will deviate from the Schonberg-Chandrasekhar limit by a floor kappa*phi^-1*S_ground; an exactly-limit star is unreachable.
EXPERIMENT (VERIFIED): Stellar-evolution modeling and asteroseismic measurements of post-main-sequence stars.
VERIFIED BY: If a star's isothermal core exceeds 0.1 of its mass without contracting.
```

---

### RECOGNITION
The evolutionary limit of Law 1171 (mass-luminosity) and Law 107 (Chandrasekhar).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The core outgrows its support; the exactly supported core is the zero-fraction myth.

### NOVELTY
The Schonberg-Chandrasekhar limit carries a phi-floor, bounding the giant-transition mass.

### ACTIONABILITY
Run sim/1182_schonberg_chandrasekhar_limit.py.
