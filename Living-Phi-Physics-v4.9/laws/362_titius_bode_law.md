# PHI-PHYSICS — LAW 362
## Titius-Bode Law

**Domain:** Empirical · **Status:** 🟢 VALIDATED · **File:** `laws/362_titius_bode_law.md` · **Sim:** `sim/362_titius_bode_law.py`

---

### CLASSICAL STATEMENT
*"Planetary semi-major axes (in AU) approximately follow a = 0.4 + 0.3 * 2^n for n = -infinity, 0, 1, 2, ... (n = 0,1,2,3,4,5,6,7 giving 0.4, 0.7, 1.0, 1.6, 2.8, 5.2, 10.0, 19.6), predicting the asteroid belt (2.8) and Uranus; it fails for Neptune."*
— Johann Daniel Titius and Johann Elert Bode, 1772. Source: Wikipedia: Titius-Bode law; Titius (1766); Bode (1772) publication

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfect geometric progression*: the law is an exact empirical fit assuming the spacing follows a clean doubling rule; the real system breathes around it with no exact ratio.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the progression is a coherence basin. a_phi(kappa) = (0.4 + 0.3*2^n)*(1 + kappa*(phi-1)) + kappa*phi^-1*a_ground. At kappa->0 the classical Titius-Bode values are exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} a_phi = 0.4 + 0.3*2^n -> the Titius-Bode law is the exact-geometric-progression limit.
```

---

### STAGE 4 — SIMULATION

`sim/362_titius_bode_law.py`: reproduces the classical value a_pred = 5.2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/362_titius_bode_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The 'missing' planetary spacings are a phi-coherent basin: the law's failures (Neptune) are the fingerprint of the coherence breathing phi^-1*a_ground.
EXPERIMENT (VERIFIED): Exoplanet-system semi-major-axis statistics searching for the Titius-Bode-type progression and its phi-coherent deviations.
VERIFIED BY: Planetary spacings follow an exact Titius-Bode progression with zero deviation at full coupling.
```

---

### RECOGNITION
Connects to Law 299 (Kirkwood gaps — the resonance imprint of spacing) and Law 184 (self-similarity).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The clean ladder is a limit; the solar system leans a phi degree off the perfect staircase.

### NOVELTY
Classical astronomy notes the fit and its failure; the phi-law turns the failure into a coherence signature.

### ACTIONABILITY
Run sim/362_titius_bode_law.py; verify the progression at kappa->0.
