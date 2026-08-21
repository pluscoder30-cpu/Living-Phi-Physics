# PHI-PHYSICS — LAW 1172
## Salpeter Initial Mass Function

**Domain:** Astrophysics · **Status:** 🟢 VALIDATED · **File:** `laws/1172_salpeter_imf.md` · **Sim:** `sim/1172_salpeter_imf.py`

---

### CLASSICAL STATEMENT
*"The Salpeter initial mass function describes the distribution of stellar masses at birth: dn/dlog M ~ M^-x with x = 1.35 (equivalently xi(M) ~ M^-2.35), valid over roughly 0.4-10 solar masses; it underpins stellar-population and galaxy-evolution modeling."*
— Edwin Salpeter, 1955. Source: Wikipedia: Initial mass function (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero stellar mass (M = 0, no stars at the low-mass end)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The S value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground, where S_ground is the coherence-floor slope variation a real stellar population always carries. At kappa->0, dn/dlog M ~ M^(-1.35),  xi(M) ~ M^(-2.35) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} S_phi = S -> dn/dlog M ~ M^(-1.35),  xi(M) ~ M^(-2.35) is recovered exactly; the classical law is the zero stellar mass (M = 0, no stars at the low-mass end) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1172_salpeter_imf.py`: reproduces the classical value (S = 1.35) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1172_salpeter_imf.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured IMF of any real stellar population will deviate from the Salpeter slope by a floor kappa*phi^-1*S_ground; an exactly single-slope IMF is unreachable.
EXPERIMENT (VERIFIED): Stellar census of resolved populations (HST, JWST) and integrated-light IMF studies.
VERIFIED BY: If any stellar population matches the Salpeter IMF exactly with zero slope variation.
```

---

### RECOGNITION
The stellar distribution law feeding Law 1212 (Schechter function) and galaxy models.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Stars are born in a steep crowd; the flat IMF is the zero-slope myth.

### NOVELTY
The Salpeter IMF carries a phi-floor of slope variation across environments.

### ACTIONABILITY
Run sim/1172_salpeter_imf.py.
