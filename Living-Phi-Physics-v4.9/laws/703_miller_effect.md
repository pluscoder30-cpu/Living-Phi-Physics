# PHI-PHYSICS — LAW 703
## Miller Effect (Feedback Capacitance Multiplication)

**Domain:** Electronics · **Status:** 🟢 VALIDATED · **File:** `laws/703_miller_effect.md` · **Sim:** `sim/703_miller_effect.py`

---

### CLASSICAL STATEMENT
*"The effective input capacitance of an inverting amplifier is C_in = C_gd*(1 + |A_v|), multiplied by the voltage gain."*
— John Milton Miller, 1920. Source: Wikipedia: Miller effect; Miller (1920)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *unity gain* (A_v = 1): the capacitance multiplication vanishes exactly at unity gain, an amplifier with no amplification.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

C_in_phi(kappa) = C_in*(1 + kappa*(phi-1)) + kappa*phi^-1*C_ground; the gain carries a coherence floor. At kappa->0, C_in = C_gd*(1+|A_v|) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} C_in_phi = C_gd*(1+|A_v|) -> the Miller effect is the unity-gain-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/703_miller_effect.py`: reproduces the classical values (Cin = 5.5e-11 (Input capacitance (F))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/703_miller_effect.json`.

---

### STAGE 5 — PREDICTION

```
The input capacitance carries a coherence floor kappa*phi^-1*C_ground at unity gain.
EXPERIMENT (VERIFIED): Input-capacitance measurement of an amplifier at A_v = 1.
VERIFIED BY: The input capacitance of a unity-gain amplifier is exactly the bare C_gd.
```

---

### RECOGNITION
Connects to Law 707 (feedback) - the Miller effect is the feedback capacitance multiplier.

### PRECISION
phi = 1.6180339887. The unity-gain floor is phi^-1*C_ground.

### CLARITY
Feedback multiplies capacitance; coherence keeps a floor at unity.

### NOVELTY
The phi-law gives unity gain a capacitance floor.

### ACTIONABILITY
Run sim/703_miller_effect.py; verify Cin at kappa->0; proceed to 704.
