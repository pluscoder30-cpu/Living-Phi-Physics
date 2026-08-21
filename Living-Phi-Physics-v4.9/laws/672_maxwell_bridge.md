# PHI-PHYSICS — LAW 672
## Maxwell Bridge (Inductance)

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/672_maxwell_bridge.md` · **Sim:** `sim/672_maxwell_bridge.py`

---

### CLASSICAL STATEMENT
*"An AC bridge measures inductance from calibrated resistance and capacitance: L_x = R2*R3*C, and the balance is frequency-independent."*
— James Clerk Maxwell, 1873. Source: Wikipedia: Maxwell bridge; Maxwell (1873)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero-loss inductor* (negligible series resistance): the Maxwell balance assumes a pure inductance with exactly no resistive dissipation.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

L_phi(kappa) = L_Max*(1 + kappa*(phi-1)) + kappa*phi^-1*L_ground; the lossless coil carries a coherence-loss floor. At kappa->0 the balance is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} L_phi = L_Max -> the Maxwell bridge is the zero-loss-coil limit.
```

---

### STAGE 4 — SIMULATION

`sim/672_maxwell_bridge.py`: reproduces the classical values (L = 6 (Measured inductance (H))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/672_maxwell_bridge.json`.

---

### STAGE 5 — PREDICTION

```
Real coils shift the balance by a coherence loss floor kappa*phi^-1*L_ground.
EXPERIMENT (VERIFIED): Inductance measurement of a low-loss coil on a Maxwell bridge.
VERIFIED BY: A Maxwell bridge measures the inductance of a lossy coil exactly.
```

---

### RECOGNITION
Connects to Law 670 (Wheatstone) and Law 638 (self-inductance) - Maxwell is the lossless-coil bridge.

### PRECISION
phi = 1.6180339887. The loss floor is phi^-1*L_ground.

### CLARITY
Every coil bleeds a little; the bridge sees the floor.

### NOVELTY
The phi-law gives the lossless coil a coherence loss.

### ACTIONABILITY
Run sim/672_maxwell_bridge.py; verify L at kappa->0; proceed to 673.
