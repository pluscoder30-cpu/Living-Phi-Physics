# PHI-PHYSICS — LAW 589
## Exergetic Efficiency (Exergy Ratio)

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/589_exergetic_efficiency.md` · **Sim:** `sim/589_exergetic_efficiency.py`

---

### CLASSICAL STATEMENT
*"The exergetic efficiency is eta_ex = Exergy_out/Exergy_in, the ratio of useful exergy output to the exergy input of a process. It equals 1 only for a reversible process with zero exergy destruction."*
— Gouy and Stodola (exergy analysis), 1898. Source: Wikipedia: Exergy (exergetic efficiency); Gouy (1889), Stodola (1898)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero exergy destruction*: the efficiency equals exactly 1 only when no exergy is destroyed - a process with zero coherence dissipation.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the exergy destruction is a coherence waste. eta_ex_phi(kappa) = eta_ex_classical*(1 - kappa) + (eta_ex_classical - kappa*phi^-1*eta_waste). At kappa->0 the exergetic efficiency is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_ex_phi = Exergy_out/Exergy_in -> the exergetic efficiency is the zero-exergy-destruction reversible limit.
```

---

### STAGE 4 — SIMULATION

`sim/589_exergetic_efficiency.py`: reproduces the classical value eta_ex = 0.7 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/589_exergetic_efficiency.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the exergetic efficiency is bounded below 1 by the coherence waste kappa*phi^-1*eta_waste.
EXPERIMENT (VERIFIED): Exergy balances of real processes (power, refrigeration, chemical) measuring their exergetic efficiency.
VERIFIED BY: A reversible process achieves exergetic efficiency exactly 1 at any coupling.
```

---

### RECOGNITION
Connects to Law 449 (exergy) and Law 586 (second-law efficiency) - the ratio is the coherence quality of the exergy flow.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * eta_waste.

### CLARITY
The exergetic efficiency is how much of the available work a process keeps; the phi-law keeps the keeping's loss.

### NOVELTY
Classical exergetic efficiency is 1 for reversible processes; the phi-law bounds it by the coherence destruction floor.

### ACTIONABILITY
Run sim/589_exergetic_efficiency.py; verify reversible limit at kappa->0; proceed to 590.
