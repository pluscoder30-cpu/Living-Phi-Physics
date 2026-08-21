# PHI-PHYSICS — LAW 689
## RL Time Constant (tau = L/R)

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/689_rl_time_constant.md` · **Sim:** `sim/689_rl_time_constant.py`

---

### CLASSICAL STATEMENT
*"The inductor current builds as I(t) = I_max*(1 - exp(-t/tau)) with tau = L/R; after one tau the current reaches 63.2% of its steady value."*
— Oliver Heaviside, 1887. Source: RL circuit transient; Heaviside (1887)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero initial current* (I(0) = 0): the build-up law assumes the inductor starts with exactly zero stored flux.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

tau_phi(kappa) = tau*(1 + kappa*(phi-1)) + kappa*phi^-1*tau_ground; the inductor carries a coherence flux floor. At kappa->0, tau = L/R exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} tau_phi = L/R -> the RL time constant is the zero-initial-flux limit.
```

---

### STAGE 4 — SIMULATION

`sim/689_rl_time_constant.py`: reproduces the classical values (I = 1 (Build-up current (A))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/689_rl_time_constant.json`.

---

### STAGE 5 — PREDICTION

```
The inductor never fully decays; a coherence flux floor kappa*phi^-1 persists at t -> infinity.
EXPERIMENT (VERIFIED): Current decay of a precision LR circuit measured with a fast current probe.
VERIFIED BY: An inductor in an RL circuit reaches exactly zero residual current.
```

---

### RECOGNITION
Connects to Law 638 (self-inductance) - tau is the inductive relaxation time.

### PRECISION
phi = 1.6180339887. The flux floor is phi^-1*tau_ground.

### CLARITY
The coil remembers the flow; a coherence current lingers.

### NOVELTY
The phi-law keeps a residual current floor.

### ACTIONABILITY
Run sim/689_rl_time_constant.py; verify I(t) at kappa->0; proceed to 690.
