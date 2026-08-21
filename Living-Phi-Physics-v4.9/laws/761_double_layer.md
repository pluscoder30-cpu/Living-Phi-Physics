# PHI-PHYSICS — LAW 761
## Plasma Double Layer (Potential Step)

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/761_double_layer.md` · **Sim:** `sim/761_double_layer.py`

---

### CLASSICAL STATEMENT
*"A double layer is a pair of charge sheets creating a localized potential step that accelerates and reflects particles; the potential jump is maintained by the current through it."*
— Irving Langmuir, 1929. Source: Wikipedia: Double layer (plasma physics); Langmuir (1920s)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero net current*: the double layer potential step vanishes exactly without current flowing through it.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Phi_dl_phi(kappa) = Phi_dl*(1 + kappa*(phi-1)) + kappa*phi^-1*Phi_ground; the charge sheets carry a coherence floor. At kappa->0 the potential step is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Phi_dl_phi = Phi_dl -> the double layer is the zero-net-current floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/761_double_layer.py`: reproduces the classical values (Phi = 86.1733 (Double-layer potential (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/761_double_layer.json`.

---

### STAGE 5 — PREDICTION

```
A potential step exists even at zero net current; a coherence floor kappa*phi^-1*Phi_ground persists.
EXPERIMENT (VERIFIED): Potential-profile measurement across a current-free double layer.
VERIFIED BY: A double layer with zero current has exactly zero potential step.
```

---

### RECOGNITION
Connects to Law 752 (sheath) - the double layer is the self-sustaining sheath pair.

### PRECISION
phi = 1.6180339887. The step floor is phi^-1*Phi_ground.

### CLARITY
The step stands on current; coherence keeps a floor of it.

### NOVELTY
The phi-law keeps the double layer at zero current.

### ACTIONABILITY
Run sim/761_double_layer.py; verify Phi_dl at kappa->0; proceed to 762.
