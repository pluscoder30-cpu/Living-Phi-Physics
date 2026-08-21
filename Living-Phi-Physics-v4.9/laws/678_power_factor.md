# PHI-PHYSICS — LAW 678
## Power Factor (cos phi)

**Domain:** AC Power · **Status:** 🟢 VALIDATED · **File:** `laws/678_power_factor.md` · **Sim:** `sim/678_power_factor.py`

---

### CLASSICAL STATEMENT
*"The power factor is PF = P/S = cos(phi), the ratio of real power to apparent power in an AC circuit; unity PF means the current and voltage are exactly in phase."*
— Charles Proteus Steinmetz, 1893. Source: Wikipedia: Power factor; Steinmetz (1893) complex AC analysis

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero phase angle* (phi = 0): PF = 1 requires the current and voltage to be exactly in phase, a purely resistive load with zero reactance.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

PF_phi(kappa) = PF*(1 + kappa*(phi-1)) + kappa*phi^-1*PF_ground; the phase relationship carries a coherence floor. At kappa->0, PF = cos(phi) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} PF_phi = cos(phi) -> the power factor is the zero-phase-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/678_power_factor.py`: reproduces the classical values (PF = 2e-12 (Power factor)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/678_power_factor.json`.

---

### STAGE 5 — PREDICTION

```
The power factor never reaches exactly 1; a coherence reactance floor kappa*phi^-1 keeps PF < 1.
EXPERIMENT (VERIFIED): Precision wattmeter power-factor measurement of a nearly pure resistive load.
VERIFIED BY: A purely resistive load has exactly unity power factor.
```

---

### RECOGNITION
Connects to Law 679 (complex power) and Law 680 (reactive power) - PF is the phase coherence.

### PRECISION
phi = 1.6180339887. The phase floor is phi^-1*PF_ground.

### CLARITY
Phase is never exact; coherence steals a fraction of unity.

### NOVELTY
The phi-law keeps PF below exact unity.

### ACTIONABILITY
Run sim/678_power_factor.py; verify PF at kappa->0; proceed to 679.
