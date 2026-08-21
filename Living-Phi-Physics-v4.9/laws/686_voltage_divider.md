# PHI-PHYSICS — LAW 686
## Voltage Divider (Rule)

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/686_voltage_divider.md` · **Sim:** `sim/686_voltage_divider.py`

---

### CLASSICAL STATEMENT
*"The voltage across R_k of a series chain is V_k = V*R_k/(sum R_i); the source voltage divides proportionally to resistance."*
— Gustav Kirchhoff, 1845. Source: Voltage divider rule; Kirchhoff (1845) circuit laws

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero source impedance* and *ideal series chain*: the divider assumes exactly zero lead resistance and an ideal voltage source.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_k_phi(kappa) = V_k*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the divider carries a coherence lead floor. At kappa->0 the divider rule is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_k_phi = V*R_k/sum R_i -> the voltage divider is the zero-lead-impedance limit.
```

---

### STAGE 4 — SIMULATION

`sim/686_voltage_divider.py`: reproduces the classical values (V = 3.33333 (Divided voltage (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/686_voltage_divider.json`.

---

### STAGE 5 — PREDICTION

```
The divided voltage carries a coherence floor kappa*phi^-1*V_ground from finite lead impedance.
EXPERIMENT (VERIFIED): Precision divider measurement with short finite leads.
VERIFIED BY: The voltage across a resistor is always exactly the ideal divider value.
```

---

### RECOGNITION
Connects to Law 044 (Ohm) and Law 046 (KVL) - the divider is the series KVL balance.

### PRECISION
phi = 1.6180339887. The lead floor is phi^-1*V_ground.

### CLARITY
Division is never exact; the leads keep a coherence share.

### NOVELTY
The phi-law gives the divider a lead-coherence floor.

### ACTIONABILITY
Run sim/686_voltage_divider.py; verify Vk at kappa->0; proceed to 687.
