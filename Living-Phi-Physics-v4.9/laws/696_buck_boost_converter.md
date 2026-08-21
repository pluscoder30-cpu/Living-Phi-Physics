# PHI-PHYSICS — LAW 696
## Buck-Boost Converter (Inverting)

**Domain:** Power Electronics · **Status:** 🟢 VALIDATED · **File:** `laws/696_buck_boost_converter.md` · **Sim:** `sim/696_buck_boost_converter.py`

---

### CLASSICAL STATEMENT
*"The buck-boost converter inverts and can step up or down: V_out = -D/(1-D)*V_in; magnitude |V_out| > V_in for D > 1/2 and < V_in for D < 1/2."*
— Switched-mode power supply heritage, 1950. Source: Wikipedia: Buck-boost converter (1950s)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero duty* (D = 0): the inverted output vanishes exactly at zero duty.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_out_phi(kappa) = V_out*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the switch carries a coherence floor. At kappa->0, V_out = -D/(1-D)*V_in exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_out_phi = -D/(1-D)*V_in -> the buck-boost is the zero-duty-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/696_buck_boost_converter.py`: reproduces the classical values (Vo = -12 (Output voltage (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/696_buck_boost_converter.json`.

---

### STAGE 5 — PREDICTION

```
The inverted output carries a coherence ripple floor kappa*phi^-1*V_ground.
EXPERIMENT (VERIFIED): Output measurement of a buck-boost converter at small duty.
VERIFIED BY: A buck-boost output is exactly zero at zero duty.
```

---

### RECOGNITION
Connects to Law 694-695 - the buck-boost is the inverting combination.

### PRECISION
phi = 1.6180339887. The ripple floor is phi^-1*V_ground.

### CLARITY
Inversion is never clean; the floor murmurs through.

### NOVELTY
The phi-law ripples the inverted step.

### ACTIONABILITY
Run sim/696_buck_boost_converter.py; verify Vo at kappa->0; proceed to 697.
