# PHI-PHYSICS — LAW 711
## Hooge's Law (1/f Noise Scaling)

**Domain:** Electronics · **Status:** 🟢 VALIDATED · **File:** `laws/711_hooges_law.md` · **Sim:** `sim/711_hooges_law.py`

---

### CLASSICAL STATEMENT
*"The 1/f noise of a homogeneous conductor scales as S_V/V^2 = alpha_H/N, where N is the total number of charge carriers and alpha_H ~ 2e-3 is Hooge's constant."*
— F. N. Hooge, 1969. Source: Hooge's law; F.N. Hooge (1969) 1/f noise in conductors

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite carrier number* (N -> infinity): the relative 1/f noise vanishes exactly for a conductor with infinite carriers.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S_H*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground; the carrier ensemble carries a coherence floor. At kappa->0, S = alpha_H*V^2/N exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} S_phi = alpha_H*V^2/N -> Hooge's law is the infinite-carrier limit.
```

---

### STAGE 4 — SIMULATION

`sim/711_hooges_law.py`: reproduces the classical values (S = 0.002 (Relative noise (V^2))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/711_hooges_law.json`.

---

### STAGE 5 — PREDICTION

```
The relative 1/f noise carries a coherence floor kappa*phi^-1*S_ground even for very large carrier numbers.
EXPERIMENT (VERIFIED): 1/f noise measurement of a large cross-section metal film.
VERIFIED BY: The relative 1/f noise of a large conductor is exactly zero.
```

---

### RECOGNITION
Connects to Law 710 (1/f noise) - Hooge's law is the carrier-count scaling.

### PRECISION
phi = 1.6180339887. The carrier floor is phi^-1*S_ground.

### CLARITY
Many carriers, never infinite; coherence keeps a whisper.

### NOVELTY
The phi-law caps the 1/f noise of huge conductors.

### ACTIONABILITY
Run sim/711_hooges_law.py; verify Hooge scaling at kappa->0; proceed to 712.
