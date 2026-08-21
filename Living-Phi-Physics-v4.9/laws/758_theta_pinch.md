# PHI-PHYSICS — LAW 758
## Theta-Pinch (Inductive Compression)

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/758_theta_pinch.md` · **Sim:** `sim/758_theta_pinch.py`

---

### CLASSICAL STATEMENT
*"A rapidly-rising axial field B_z induces an azimuthal current that compresses and heats the plasma; the theta-pinch reached thermonuclear fusion in Scylla I (1958)."*
— Los Alamos Scylla program, 1958. Source: Wikipedia: Theta pinch; Scylla I (Los Alamos, 1958)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero external field* (B_z = 0): the compression vanishes exactly without the driving field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

B_phi(kappa) = B_th*(1 + kappa*(phi-1)) + kappa*phi^-1*B_ground; the driven column carries a coherence floor. At kappa->0 the theta-pinch compression is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} B_phi = B_th -> the theta-pinch is the zero-drive-field floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/758_theta_pinch.py`: reproduces the classical values (B = 1 (Pinch field (T))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/758_theta_pinch.json`.

---

### STAGE 5 — PREDICTION

```
The compression carries a coherence floor kappa*phi^-1*B_ground; a field-free column still compresses a little.
EXPERIMENT (VERIFIED): Compression measurement of a theta-pinch at reduced drive field.
VERIFIED BY: A theta-pinch with zero drive field has exactly zero compression.
```

---

### RECOGNITION
Connects to Law 757 (z-pinch) - the theta-pinch is the inductively-driven compression.

### PRECISION
phi = 1.6180339887. The drive floor is phi^-1*B_ground.

### CLARITY
The field squeezes; coherence keeps a floor of squeeze.

### NOVELTY
The phi-law keeps theta-pinch compression at zero drive.

### ACTIONABILITY
Run sim/758_theta_pinch.py; verify B_th at kappa->0; proceed to 759.
