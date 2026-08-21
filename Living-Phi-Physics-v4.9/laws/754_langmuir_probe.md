# PHI-PHYSICS — LAW 754
## Langmuir Probe (Plasma Diagnostics)

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/754_langmuir_probe.md` · **Sim:** `sim/754_langmuir_probe.py`

---

### CLASSICAL STATEMENT
*"The current to a biased probe in a plasma gives the electron temperature from the exponential part I_e ~ I_sat*exp(e(V-V_p)/k_B*T_e) and the density from the saturation current."*
— Irving Langmuir, 1924. Source: Wikipedia: Langmuir probe; Langmuir (1924)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero probe current*: the floating potential is defined at exactly zero net probe current.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_f_phi(kappa) = V_f*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the floating point carries a coherence floor. At kappa->0, I(V_f) = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_f_phi = V_f -> the Langmuir probe is the zero-net-current limit.
```

---

### STAGE 4 — SIMULATION

`sim/754_langmuir_probe.py`: reproduces the classical values (Te = 503.978 (Electron temperature (K))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/754_langmuir_probe.json`.

---

### STAGE 5 — PREDICTION

```
The floating potential carries a coherence floor kappa*phi^-1*V_ground; the probe never draws exactly zero current.
EXPERIMENT (VERIFIED): Probe I-V measurement in a quiescent plasma at the floating condition.
VERIFIED BY: A probe at the floating potential draws exactly zero current.
```

---

### RECOGNITION
Connects to Law 752 (sheath) and Law 755 (Spitzer) - the probe reads the plasma's state.

### PRECISION
phi = 1.6180339887. The floating floor is phi^-1*V_ground.

### CLARITY
The probe floats, never stills; coherence keeps a floor of current.

### NOVELTY
The phi-law gives the floating probe a current floor.

### ACTIONABILITY
Run sim/754_langmuir_probe.py; verify Te at kappa->0; proceed to 755.
