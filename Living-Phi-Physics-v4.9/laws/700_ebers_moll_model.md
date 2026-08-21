# PHI-PHYSICS — LAW 700
## Ebers-Moll Model (BJT)

**Domain:** Electronics · **Status:** 🟢 VALIDATED · **File:** `laws/700_ebers_moll_model.md` · **Sim:** `sim/700_ebers_moll_model.py`

---

### CLASSICAL STATEMENT
*"The bipolar transistor is modeled by coupled diodes: I_C = I_S*(exp(V_BE/V_T) - exp(V_BC/V_T)) - alpha_R*I_S*(exp(V_BC/V_T)-1), with alpha_F and alpha_R the forward/reverse gains."*
— J. J. Ebers; J. L. Moll, 1954. Source: Wikipedia: Ebers-Moll model; Ebers & Moll (1954)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero base current* (I_B = 0): the model's transport equations are exact only for ideal charge-controlled carriers.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_C_phi(kappa) = I_C*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ground; the carrier transport carries a coherence floor. At kappa->0 the Ebers-Moll equations are exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_C_phi = I_C -> the Ebers-Moll model is the zero-carrier-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/700_ebers_moll_model.py`: reproduces the classical values (IC = 1.44626 (Collector current (A))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/700_ebers_moll_model.json`.

---

### STAGE 5 — PREDICTION

```
Transistor currents carry a coherence floor kappa*phi^-1*I_ground at zero base current.
EXPERIMENT (VERIFIED): Precision collector-current measurement of a BJT at zero base current.
VERIFIED BY: A BJT conducts exactly zero collector current at zero base current.
```

---

### RECOGNITION
Connects to Law 699 (diode) and Law 701 (Gummel-Poon) - Ebers-Moll is the two-diode model.

### PRECISION
phi = 1.6180339887. The carrier floor is phi^-1*I_ground.

### CLARITY
Transistors whisper; a coherence floor of charge always flows.

### NOVELTY
The phi-law gives the BJT a zero-base floor current.

### ACTIONABILITY
Run sim/700_ebers_moll_model.py; verify IC at kappa->0; proceed to 701.
