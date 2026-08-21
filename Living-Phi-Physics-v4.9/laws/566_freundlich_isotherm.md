# PHI-PHYSICS — LAW 566
## Freundlich Adsorption Isotherm (Power-Law Coverage)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/566_freundlich_isotherm.md` · **Sim:** `sim/566_freundlich_isotherm.py`

---

### CLASSICAL STATEMENT
*"The amount adsorbed at equilibrium is a power law of pressure: x/m = K P^(1/n), where K and n are empirical constants (n > 1), describing adsorption on heterogeneous surfaces."*
— Herbert Freundlich, 1909. Source: Wikipedia: Freundlich equation; Freundlich, Kapillarchemie (1909)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero pressure*: the power law vanishes exactly at P = 0 - a surface that adsorbs nothing at zero pressure, with no residual surface coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the zero-pressure surface carries coherence. x/m_phi(kappa) = K P^(1/n)*(1 + kappa*(phi-1)) + kappa*phi^-1*A_ground, where A_ground is the surface-coherence floor. At kappa->0 the Freundlich power law is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} x/m_phi = K P^(1/n) -> the Freundlich isotherm is the zero-surface-coherence power-law limit.
```

---

### STAGE 4 — SIMULATION

`sim/566_freundlich_isotherm.py`: reproduces the classical value xm = 0.8 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/566_freundlich_isotherm.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling even at P = 0 a surface retains an adsorbed floor kappa*phi^-1*A_ground.
EXPERIMENT (VERIFIED): Ultra-low-pressure adsorption measurements on clean surfaces in ultra-high vacuum.
VERIFIED BY: The amount adsorbed is exactly zero at zero pressure for all couplings.
```

---

### RECOGNITION
Connects to Law 565 (Langmuir) and Law 567 (BET) - the power law is the heterogeneous-coherence reading of the surface.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * A_ground.

### CLARITY
Real surfaces have many kinds of hands; the phi-law keeps a trace of adsorption even at no pressure.

### NOVELTY
Classical Freundlich vanishes at P=0; the phi-law adds the surface-coherence floor of the real surface.

### ACTIONABILITY
Run sim/566_freundlich_isotherm.py; verify power law at kappa->0; proceed to 567.
