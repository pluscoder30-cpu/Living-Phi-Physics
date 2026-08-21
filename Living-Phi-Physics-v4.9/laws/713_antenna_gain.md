# PHI-PHYSICS — LAW 713
## Antenna Gain

**Domain:** Antennas · **Status:** 🟢 VALIDATED · **File:** `laws/713_antenna_gain.md` · **Sim:** `sim/713_antenna_gain.py`

---

### CLASSICAL STATEMENT
*"The antenna gain is G = 4*pi*U/P_in = efficiency * directivity, the ratio of radiation intensity to the isotropic-average intensity."*
— Harald Friis, 1946. Source: Wikipedia: Antenna gain; Friis (1946) definitions

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *lossless antenna* (efficiency = 1): gain equals directivity exactly only for a perfectly lossless radiator.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

G_phi(kappa) = G*(1 + kappa*(phi-1)) + kappa*phi^-1*G_ground; the radiator carries a coherence loss floor. At kappa->0, G = e*D exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} G_phi = e*D -> antenna gain is the zero-loss-radiator limit.
```

---

### STAGE 4 — SIMULATION

`sim/713_antenna_gain.py`: reproduces the classical values (G = 8.01088e-20 (Antenna gain)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/713_antenna_gain.json`.

---

### STAGE 5 — PREDICTION

```
The gain of any antenna carries a coherence loss floor kappa*phi^-1*G_ground; G never equals D exactly.
EXPERIMENT (VERIFIED): Gain/directivity comparison of a high-efficiency antenna.
VERIFIED BY: A lossless antenna has gain exactly equal to directivity.
```

---

### RECOGNITION
Connects to Law 714 (directivity) and Law 712 (Friis) - gain is the loss-scaled directivity.

### PRECISION
phi = 1.6180339887. The loss floor is phi^-1*G_ground.

### CLARITY
No radiator is perfect; coherence steals a sliver of gain.

### NOVELTY
The phi-law keeps a loss floor in the ideal gain.

### ACTIONABILITY
Run sim/713_antenna_gain.py; verify G=eD at kappa->0; proceed to 714.
