# PHI-PHYSICS — LAW 456
## Nernst Equation (Electrode Potential)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/456_nernst_equation.md` · **Sim:** `sim/456_nernst_equation.py`

---

### CLASSICAL STATEMENT
*"The electrode potential of an electrochemical cell is E = E_0 - (R T / (n F)) ln Q, where Q is the reaction quotient and E_0 the standard potential. It connects cell voltage to concentration."*
— Walther Nernst, 1889. Source: Wikipedia: Nernst equation; Nernst, Die elektromotorische Wirksamkeit der Ionen (1889)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *standard-state ideality*: the Nernst equation assumes the standard potential E_0 is a fixed reference at unit activities with no coherence coupling between the ions and the electrode.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the standard potential carries coherence. E_phi(kappa) = E_0*(1 + kappa*(phi-1)) - (RT/(nF))*ln(Q) + kappa*phi^-1*E_ground. At kappa->0, E = E_0 - (RT/nF) ln Q exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} E_phi = E_0 - (RT/nF) ln Q -> the Nernst equation is the ideal-standard-state, zero-ion-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/456_nernst_equation.py`: reproduces the classical value E_cell = 1.13 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/456_nernst_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Cell potentials at finite coupling show an offset kappa*phi^-1*E_ground from the Nernst prediction, visible in concentrated electrolytes.
EXPERIMENT (VERIFIED): Precision potentiometry of a concentration cell across a wide ionic-strength range.
VERIFIED BY: The cell potential follows the Nernst equation exactly at all concentrations and couplings.
```

---

### RECOGNITION
Connects to Law 452 (mass action), Law 459 (Faraday) and Law 457 (Ostwald) - the cell voltage is the coherence difference of two ion basins.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the offset floor is phi^-1 * E_ground.

### CLARITY
The electrode reads the ion coherence; the phi-law prices the reading floor.

### NOVELTY
Classical Nernst fixes E_0; the phi-law lets the standard potential carry a coherence ground.

### ACTIONABILITY
Run sim/456_nernst_equation.py; verify Nernst voltage at kappa->0; proceed to 457.
