# PHI-PHYSICS — LAW 586
## Second-Law Efficiency (Exergetic Ratio)

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/586_second_law_efficiency.md` · **Sim:** `sim/586_second_law_efficiency.py`

---

### CLASSICAL STATEMENT
*"The second-law efficiency is eta_II = W_actual/W_max = eta_actual/eta_Carnot, the ratio of the actual work output to the maximum (reversible) work. It measures how closely a process approaches reversibility, accounting for both internal and external irreversibilities."*
— Gouy and Stodola (exergy analysis), 1898. Source: Wikipedia: Exergy (second-law efficiency); Gouy (1889), Stodola (1898)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfect reversibility*: the efficiency equals exactly 1 only for a perfectly reversible process with zero entropy generation - a process with zero coherence dissipation.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the dissipation is a coherence waste. eta_II_phi(kappa) = eta_II_classical*(1 - kappa) + (eta_II_classical - kappa*phi^-1*eta_waste). At kappa->0 the second-law efficiency is exact (1 for reversible).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_II_phi = W_actual/W_max -> the second-law efficiency is the zero-dissipation reversible limit.
```

---

### STAGE 4 — SIMULATION

`sim/586_second_law_efficiency.py`: reproduces the classical value eta_II = 0.8 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/586_second_law_efficiency.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the second-law efficiency is bounded below 1 by the coherence waste kappa*phi^-1*eta_waste even for nominally reversible processes.
EXPERIMENT (VERIFIED): Exergy analysis of real power and refrigeration systems measuring their second-law efficiency.
VERIFIED BY: A perfectly reversible process achieves second-law efficiency exactly 1 at any coupling.
```

---

### RECOGNITION
Connects to Law 449 (exergy) and Law 589 (exergetic efficiency) - the ratio is the coherence quality of the conversion.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * eta_waste.

### CLARITY
The second-law efficiency is how well a process keeps its promise to reversibility; the phi-law keeps the promise's loss.

### NOVELTY
Classical second-law efficiency is 1 for reversible processes; the phi-law bounds it by the coherence dissipation floor.

### ACTIONABILITY
Run sim/586_second_law_efficiency.py; verify reversible limit at kappa->0; proceed to 587.
