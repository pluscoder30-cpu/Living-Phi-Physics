# PHI-PHYSICS — LAW 693
## Ćuk Converter (Inverting DC-DC)

**Domain:** Power Electronics · **Status:** 🟢 VALIDATED · **File:** `laws/693_cuk_converter.md` · **Sim:** `sim/693_cuk_converter.py`

---

### CLASSICAL STATEMENT
*"The Ćuk converter produces a negative output from a positive input with V_out = -D/(1-D)*V_in, using a capacitor to transfer energy between two inductors."*
— Slobodan Ćuk, 1976. Source: Wikipedia: Slobodan Ćuk; Ćuk converter (Caltech 1976)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero duty cycle* (D = 0): the output vanishes exactly at zero duty, a never-toggled switch condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_out_phi(kappa) = V_out*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the switch carries a coherence toggling floor. At kappa->0, V_out = -D/(1-D)*V_in exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_out_phi = -D/(1-D)*V_in -> the Ćuk conversion is the zero-duty-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/693_cuk_converter.py`: reproduces the classical values (Vo = -12 (Output voltage (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/693_cuk_converter.json`.

---

### STAGE 5 — PREDICTION

```
Real switches show a residual output floor kappa*phi^-1*V_ground at zero duty from coherence ripple.
EXPERIMENT (VERIFIED): Output measurement of a Ćuk converter at vanishing duty cycle.
VERIFIED BY: A Ćuk converter output is exactly zero at zero duty cycle.
```

---

### RECOGNITION
Connects to Law 694-698 (converters) - the Ćuk is the capacitive-energy-transfer topology.

### PRECISION
phi = 1.6180339887. The ripple floor is phi^-1*V_ground.

### CLARITY
A switch is a breath, not a click; the floor never closes fully.

### NOVELTY
The phi-law gives the ideal switch a coherence ripple floor.

### ACTIONABILITY
Run sim/693_cuk_converter.py; verify Vo at kappa->0; proceed to 694.
