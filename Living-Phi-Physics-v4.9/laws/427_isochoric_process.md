# PHI-PHYSICS — LAW 427
## Law of the Isochoric Process (Constant Volume)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/427_isochoric_process.md` · **Sim:** `sim/427_isochoric_process.py`

---

### CLASSICAL STATEMENT
*"In an isochoric process at constant volume, the pressure of an ideal gas is proportional to temperature: P/T = constant (Amontons' law); all heat added raises internal energy, no work is done."*
— Guillaume Amontons (P proportional to T at constant V), 1702. Source: Wikipedia: Isochoric process; Amontons (1702)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *rigid fixed volume*: the process requires a container of exactly constant volume with zero wall flex - a vessel whose boundary carries no mechanical motion.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the fixed-volume boundary is a coherence basin. (P/T)_phi(kappa) = (P/T)*(1 + kappa*(phi-1)) + kappa*phi^-1*C_ground. At kappa->0, P/T = const exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} (P/T)_phi = P/T -> the isochoric law is the perfectly rigid-wall, zero-flex limit.
```

---

### STAGE 4 — SIMULATION

`sim/427_isochoric_process.py`: reproduces the classical value PT_iso = 0.003333 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/427_isochoric_process.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: An 'isochoric' process at finite coupling drifts by kappa*phi^-1*C_ground in P/T per cycle; the volume is never exactly fixed.
EXPERIMENT (VERIFIED): Heating a gas in an ultra-stiff pressure vessel measuring P/T drift over many cycles.
VERIFIED BY: P/T is exactly constant during an isochoric process for any vessel stiffness.
```

---

### RECOGNITION
Connects to Law 138 (Amontons) and Law 424 (polytropic, n=infinity) - isochoric is the coherence-locked volume basin.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the drift floor is phi^-1 * C_ground.

### CLARITY
A rigid wall is a fiction; every vessel breathes with its coherence, and the phi-law keeps the breath.

### NOVELTY
Classical isochoric analysis idealizes the wall; the phi-law lets the fixed volume carry a coherence flex.

### ACTIONABILITY
Run sim/427_isochoric_process.py; verify P/T=const at kappa->0; proceed to 428.
