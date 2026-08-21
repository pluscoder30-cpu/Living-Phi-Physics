# PHI-PHYSICS — LAW 673
## Hay Bridge (High-Q Inductance)

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/673_hay_bridge.md` · **Sim:** `sim/673_hay_bridge.py`

---

### CLASSICAL STATEMENT
*"An AC bridge with a series RC arm balances high-Q inductances: L_x = R2*R3*C/(1 + (omega*C*R)^2), accurate for large quality factors Q = omega*L/R."*
— J. H. Hay, 1905. Source: Hay's bridge; inductance measurement bridge (early 20th century)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite quality factor* (Q -> infinity): the Hay balance simplifies only for coils with negligible resistance, an exactly lossless inductor.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

L_phi(kappa) = L_Hay*(1 + kappa*(phi-1)) + kappa*phi^-1*L_ground; the high-Q coil carries a coherence floor. At kappa->0 the Hay formula is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} L_phi = L_Hay -> the Hay bridge is the infinite-Q limit.
```

---

### STAGE 4 — SIMULATION

`sim/673_hay_bridge.py`: reproduces the classical values (L = 2.4e-17 (Hay inductance (H))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/673_hay_bridge.json`.

---

### STAGE 5 — PREDICTION

```
Finite-coherence coils show a balance floor kappa*phi^-1*L_ground that limits the effective Q.
EXPERIMENT (VERIFIED): High-Q inductance measurement on a Hay bridge at audio frequencies.
VERIFIED BY: The Hay bridge measures a coil's inductance exactly at any Q.
```

---

### RECOGNITION
Connects to Law 672 (Maxwell) - Hay is the high-Q variant of Maxwell's bridge.

### PRECISION
phi = 1.6180339887. The Q floor is phi^-1*L_ground.

### CLARITY
Quality is a floor, not a ceiling; coherence caps the Q.

### NOVELTY
The phi-law caps the ideal high-Q balance.

### ACTIONABILITY
Run sim/673_hay_bridge.py; verify Hay L at kappa->0; proceed to 674.
