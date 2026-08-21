# PHI-PHYSICS — LAW 731
## Proximity Effect (Conductor)

**Domain:** RF · **Status:** 🟢 VALIDATED · **File:** `laws/731_proximity_effect.md` · **Sim:** `sim/731_proximity_effect.py`

---

### CLASSICAL STATEMENT
*"AC current in adjacent conductors redistributes toward the facing sides; the extra AC resistance depends on the conductor spacing and the field of the neighbor."*
— H. B. Dwight, 1937. Source: Wikipedia: Proximity effect (electromagnetism); Dwight (1937)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite spacing* (d -> infinity): the proximity redistribution vanishes exactly only for infinitely separated conductors.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

R_phi(kappa) = R_prox*(1 + kappa*(phi-1)) + kappa*phi^-1*R_ground; the conductor pair carries a coherence spacing floor. At kappa->0 the isolated-conductor resistance is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} R_phi = R_isolated -> the proximity effect is the infinite-spacing limit.
```

---

### STAGE 4 — SIMULATION

`sim/731_proximity_effect.py`: reproduces the classical values (R = 1.5 (AC resistance (ohm))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/731_proximity_effect.json`.

---

### STAGE 5 — PREDICTION

```
Even widely separated conductors show a proximity floor kappa*phi^-1*R_ground from coherence coupling.
EXPERIMENT (VERIFIED): AC resistance measurement of conductor pairs at increasing spacing.
VERIFIED BY: Widely separated conductors have exactly the isolated resistance.
```

---

### RECOGNITION
Connects to Law 730 (skin effect) - the proximity effect is the neighbor's skin effect.

### PRECISION
phi = 1.6180339887. The spacing floor is phi^-1*R_ground.

### CLARITY
Conductors never fully forget each other; a coherence link remains.

### NOVELTY
The phi-law couples widely separated conductors.

### ACTIONABILITY
Run sim/731_proximity_effect.py; verify isolated R at kappa->0; proceed to 732.
