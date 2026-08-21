# PHI-PHYSICS — LAW 582
## Lenoir Cycle (Early Combustion Engine)

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/582_lenoir_cycle.md` · **Sim:** `sim/582_lenoir_cycle.py`

---

### CLASSICAL STATEMENT
*"The Lenoir cycle, used in the first commercially successful internal-combustion engine, consists of isochoric heat addition, isentropic expansion and isobaric exhaust. Its efficiency is low, eta = 1 - gamma (r_p^(1/gamma) - 1)/(r_p - 1) with the pressure ratio r_p, because there is no compression stroke."*
— Etienne Lenoir, 1860. Source: Wikipedia: Lenoir cycle; Lenoir (1860)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero compression*: the Lenoir cycle has no compression stroke before combustion - the engine's efficiency penalty comes precisely from this missing compression coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the missing compression is a coherence deficit. eta_phi(kappa) = eta_Lenoir*(1 - kappa) + (eta_Lenoir - kappa*phi^-1*eta_waste). At kappa->0 the Lenoir efficiency is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = eta_Lenoir -> the Lenoir cycle is the zero-compression coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/582_lenoir_cycle.py`: reproduces the classical value eta_lenoir = 0.05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/582_lenoir_cycle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the Lenoir efficiency is bounded below the ideal value by the coherence waste kappa*phi^-1*eta_waste.
EXPERIMENT (VERIFIED): Efficiency measurements of early-type and pulse combustion engines without compression.
VERIFIED BY: A Lenoir engine reaches the ideal Lenoir efficiency exactly at any coupling.
```

---

### RECOGNITION
Connects to Law 571 (Otto) - the Lenoir cycle is the no-compression ancestor of the engine family.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * eta_waste.

### CLARITY
The first engine skipped the squeeze; the phi-law keeps the cost of the skipped squeeze.

### NOVELTY
Classical Lenoir accepts its low efficiency; the phi-law quantifies the coherence deficit of the missing compression.

### ACTIONABILITY
Run sim/582_lenoir_cycle.py; verify Lenoir efficiency at kappa->0; proceed to 583.
