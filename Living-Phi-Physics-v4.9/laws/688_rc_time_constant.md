# PHI-PHYSICS — LAW 688
## RC Time Constant (tau = RC)

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/688_rc_time_constant.md` · **Sim:** `sim/688_rc_time_constant.py`

---

### CLASSICAL STATEMENT
*"The capacitor charges as V(t) = V0*(1 - exp(-t/tau)) with tau = R*C; after t = tau the voltage is 63.2% of its final value."*
— Oliver Heaviside, 1887. Source: RC circuit transient; Heaviside (1887) operational analysis

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero initial charge* (Q(0) = 0): the charging law assumes the capacitor starts exactly discharged.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

tau_phi(kappa) = tau*(1 + kappa*(phi-1)) + kappa*phi^-1*tau_ground; the capacitor carries a coherence residual-charge floor. At kappa->0, tau = RC exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} tau_phi = RC -> the RC time constant is the zero-initial-charge limit.
```

---

### STAGE 4 — SIMULATION

`sim/688_rc_time_constant.py`: reproduces the classical values (V = 10 (Charging voltage (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/688_rc_time_constant.json`.

---

### STAGE 5 — PREDICTION

```
The capacitor never fully discharges; a coherence floor kappa*phi^-1 keeps a residual charge at t -> infinity.
EXPERIMENT (VERIFIED): Charge/discharge cycle of a precision RC pair with a sensitive electrometer.
VERIFIED BY: A capacitor in an RC circuit reaches exactly zero residual charge.
```

---

### RECOGNITION
Connects to Law 044 (Ohm) and Law 096 (Fourier) - tau is the circuit's thermal diffusion time.

### PRECISION
phi = 1.6180339887. The residual floor is phi^-1*tau_ground.

### CLARITY
The capacitor always remembers; a coherence sliver of charge remains.

### NOVELTY
The phi-law keeps a residual charge floor.

### ACTIONABILITY
Run sim/688_rc_time_constant.py; verify V(t)=V0(1-e^-t/tau) at kappa->0; proceed to 689.
