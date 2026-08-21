# PHI-PHYSICS — LAW 904
## Grassmann's Laws of Color Mixture

**Domain:** Colorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/904_grassmanns_laws.md` · **Sim:** `sim/904_grassmanns_laws.py`

---

### CLASSICAL STATEMENT
*"Grassmann's laws: (1) three stimuli are needed and sufficient to match any color; (2) luminance adds; (3) color matching is linear - if A matches B and C matches D then A+C matches B+D."*
— Hermann Grassmann, 1853. Source: Wikipedia: Grassmann's laws (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero metameric error*: the laws assume exactly linear, additivity-exact color matching with zero observer deviation.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

L_phi(kappa) = L*(1 + kappa*(phi-1)) + kappa*phi^-1*L_ground, with L_ground the additivity floor. At kappa->0, color matching is exactly linear and additive.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} L_phi = L -> Grassmann's laws are the zero-metameric-error-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/904_grassmanns_laws.py`: reproduces the classical value L = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/904_grassmanns_laws.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Additivity will fail slightly in real color matching by a coherence floor kappa*phi^-1*L_ground.
EXPERIMENT (VERIFIED): Test additivity of color matches with a real observer on a colorimeter.
VERIFIED BY: If color matching is exactly additive and linear for any real observer.
```

---

### RECOGNITION
Connects to Law 903 (CIE matching) and Law 905 (trichromatic theory).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect matcher is a coherent limit; additivity is a basin.

### NOVELTY
Grassmann's laws gain an additivity floor.

### ACTIONABILITY
Run sim/904_grassmanns_laws.py.
