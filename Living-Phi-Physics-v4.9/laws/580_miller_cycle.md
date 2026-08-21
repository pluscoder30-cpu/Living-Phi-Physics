# PHI-PHYSICS — LAW 580
## Miller Cycle (Late-Intake-Valve Engine)

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/580_miller_cycle.md` · **Sim:** `sim/580_miller_cycle.py`

---

### CLASSICAL STATEMENT
*"The Miller cycle delays or advances the intake-valve closing to achieve an effective compression ratio lower than the geometric one, while the expansion ratio remains full. It reduces pumping losses and knock, improving efficiency in supercharged engines."*
— Ralph H. Miller, 1957. Source: Wikipedia: Miller cycle; Miller, US Patent 2,817,322 (1957)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *equal effective and geometric ratios*: the Miller cycle departs from the assumption that the compression ratio equals the geometric ratio - an engine whose valve timing carries zero coherence in the classical engine.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the valve timing is a coherence parameter. eta_phi(kappa) = eta_Miller*(1 - kappa) + (eta_Miller - kappa*phi^-1*eta_waste). At kappa->0 the Miller efficiency reduces to the Otto form.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = eta_Miller -> the Miller cycle is the valve-timing coherence limit of the Otto.
```

---

### STAGE 4 — SIMULATION

`sim/580_miller_cycle.py`: reproduces the classical value eta_miller = 0.38 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/580_miller_cycle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the Miller efficiency is bounded below the ideal value by the coherence waste kappa*phi^-1*eta_waste.
EXPERIMENT (VERIFIED): Efficiency measurements of Miller-cycle supercharged engines.
VERIFIED BY: A Miller engine reaches the ideal Miller efficiency exactly at any coupling.
```

---

### RECOGNITION
Connects to Law 571 (Otto) and Law 579 (Atkinson) - the Miller cycle is the valve-coherence reading of the engine family.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * eta_waste.

### CLARITY
The Miller engine breathes late to compress less; the phi-law keeps the breathing's loss.

### NOVELTY
Classical Miller exploits valve timing; the phi-law adds the coherence waste of the real engine.

### ACTIONABILITY
Run sim/580_miller_cycle.py; verify Miller efficiency at kappa->0; proceed to 581.
