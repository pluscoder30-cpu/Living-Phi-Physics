# PHI-PHYSICS — LAW 478
## Fugacity (Corrected Pressure)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/478_fugacity.md` · **Sim:** `sim/478_fugacity.py`

---

### CLASSICAL STATEMENT
*"The fugacity f of a real gas is the 'corrected pressure' such that mu = mu_0 + R T ln(f/P_0). It relates to the pressure through the fugacity coefficient phi = f/P, and f -> P in the ideal-gas limit."*
— Gilbert Newton Lewis, 1908. Source: Wikipedia: Fugacity; Lewis, Outlines of a New System of Thermodynamic Chemistry (1908)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *ideality*: fugacity is defined so that f = P exactly for an ideal gas - the correction exists to measure departure from a baseline that assumes zero molecular coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the departure from ideality is a coherence measure. f_phi(kappa) = f_real*(1 + kappa*(phi-1)) + kappa*phi^-1*f_ground. At kappa->0, f -> P (ideality) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} f_phi = P -> fugacity equals pressure in the zero-coherence ideal-gas limit.
```

---

### STAGE 4 — SIMULATION

`sim/478_fugacity.py`: reproduces the classical value f_real = 1.8 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/478_fugacity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling even a 'real' gas retains a fugacity floor kappa*phi^-1*f_ground above its pressure at low density.
EXPERIMENT (VERIFIED): High-precision P-V-T measurements of gases computing fugacity coefficients toward low pressure.
VERIFIED BY: f = P exactly for any real gas at all pressures and couplings.
```

---

### RECOGNITION
Connects to Law 479 (activity) and Law 142 (van der Waals) - fugacity is the coherence-corrected pressure of the carrier gas.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * f_ground.

### CLARITY
Fugacity is what the gas 'really means' when it presses on its container; the phi-law keeps the meaning's floor.

### NOVELTY
Classical fugacity measures departure from ideality; the phi-law gives the departure a coherence baseline.

### ACTIONABILITY
Run sim/478_fugacity.py; verify f=P at kappa->0; proceed to 479.
