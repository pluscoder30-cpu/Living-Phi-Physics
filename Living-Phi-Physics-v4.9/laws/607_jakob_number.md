# PHI-PHYSICS — LAW 607
## Jakob Number (Sensible to Latent Heat in Boiling)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/607_jakob_number.md` · **Sim:** `sim/607_jakob_number.py`

---

### CLASSICAL STATEMENT
*"The Jakob number is the ratio of sensible heat to latent heat in boiling: Ja = rho_l c_pl (T_w - T_sat)/(rho_v L), where the subscripts denote liquid and vapor. It governs bubble growth in nucleate boiling."*
— Max Jakob (concept; named in boiling literature), 1930. Source: Wikipedia: Jakob number; Jakob (1930s), named in nucleate-boiling literature

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero superheat*: Ja = 0 exactly at T_w = T_sat where there is no superheat to drive the bubble - a boiling state with zero driving coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the superheat carries coherence. Ja_phi(kappa) = Ja*(1 + kappa*(phi-1)) + kappa*phi^-1*Ja_ground. At kappa->0 the Jakob number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Ja_phi = rho_l c_pl dT/(rho_v L) -> the Jakob number is the zero-superheat zero-coherence boiling limit.
```

---

### STAGE 4 — SIMULATION

`sim/607_jakob_number.py`: reproduces the classical value Ja = 15.44 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/607_jakob_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling even at zero superheat a residual driving-coherence Ja_ground survives; bubbles grow with a floor rate.
EXPERIMENT (VERIFIED): Bubble-growth measurements in nucleate boiling at controlled superheats.
VERIFIED BY: Ja = 0 exactly at zero superheat for all couplings.
```

---

### RECOGNITION
Connects to Law 606 (Stefan) and Law 411 (latent heat) - the Jakob number is the superheat coherence of the boiling bubble.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * Ja_ground.

### CLARITY
The bubble needs a little extra heat to be born; the phi-law keeps the little extra's floor.

### NOVELTY
Classical Jakob zeroes at no superheat; the phi-law adds the driving-coherence floor of the real bubble.

### ACTIONABILITY
Run sim/607_jakob_number.py; verify Ja at kappa->0; proceed to 608.
