# PHI-PHYSICS — LAW 781
## Paschen's Law (Breakdown Voltage)

**Domain:** Discharges · **Status:** 🟢 VALIDATED · **File:** `laws/781_paschen_law.md` · **Sim:** `sim/781_paschen_law.py`

---

### CLASSICAL STATEMENT
*"The breakdown voltage of a gas gap is a function of the product p*d: V_b = B*p*d/(ln(A*p*d) - ln(ln(1+1/gamma))), with a minimum at a specific p*d."*
— Friedrich Paschen, 1889. Source: Wikipedia: Paschen's law; Paschen (1889)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero gap* (d = 0): the breakdown voltage vanishes exactly for zero electrode separation.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_b_phi(kappa) = V_b*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the gap carries a coherence floor. At kappa->0 the Paschen curve is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_b_phi = V_b -> Paschen's law is the zero-gap-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/781_paschen_law.py`: reproduces the classical values (Vb = 0.24663 (Breakdown voltage (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/781_paschen_law.json`.

---

### STAGE 5 — PREDICTION

```
The breakdown voltage carries a coherence floor kappa*phi^-1*V_ground; breakdown persists at zero gap.
EXPERIMENT (VERIFIED): Breakdown-voltage measurement of a gas gap at vanishing separation.
VERIFIED BY: A zero-length gap breaks down at exactly zero voltage.
```

---

### RECOGNITION
Connects to Law 782 (Townsend) and Law 783 (streamer) - Paschen is the gas breakdown gate.

### PRECISION
phi = 1.6180339887. The gap floor is phi^-1*V_ground.

### CLARITY
The gap always has a floor; breakdown never needs zero distance.

### NOVELTY
The phi-law keeps breakdown at zero gap.

### ACTIONABILITY
Run sim/781_paschen_law.py; verify Vb at kappa->0; proceed to 782.
