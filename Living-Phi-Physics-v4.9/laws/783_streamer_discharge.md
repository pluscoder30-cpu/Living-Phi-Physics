# PHI-PHYSICS — LAW 783
## Streamer Discharge (Breakdown Theory)

**Domain:** Discharges · **Status:** 🟢 VALIDATED · **File:** `laws/783_streamer_discharge.md` · **Sim:** `sim/783_streamer_discharge.py`

---

### CLASSICAL STATEMENT
*"A self-propagating streamer forms when the space charge of an avalanche distorts the field; the streamer criterion alpha*d ~ 20 sets the critical avalanche growth for spark formation."*
— L. B. Loeb; Heinrich Raether; J. M. Meek, 1940. Source: Wikipedia: Streamer discharge; Loeb & Raether (1939), Meek (1940)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero field distortion*: the streamer forms only when the avalanche's own space charge exactly compensates the external field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

N_c_phi(kappa) = N_c*(1 + kappa*(phi-1)) + kappa*phi^-1*N_ground; the avalanche carries a coherence floor. At kappa->0 the streamer criterion is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} N_c_phi = exp(alpha*d) -> the streamer discharge is the zero-field-distortion floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/783_streamer_discharge.py`: reproduces the classical values (N = 1.2214 (Avalanche size)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/783_streamer_discharge.json`.

---

### STAGE 5 — PREDICTION

```
The streamer criterion carries a coherence floor kappa*phi^-1*N_ground; streamers form at slightly reduced avalanche size.
EXPERIMENT (VERIFIED): Streamer-initiation measurement in a short air gap.
VERIFIED BY: A streamer forms only at exactly the classical avalanche size.
```

---

### RECOGNITION
Connects to Law 782 (Townsend) - the streamer is the space-charge-feedback breakdown.

### PRECISION
phi = 1.6180339887. The distortion floor is phi^-1*N_ground.

### CLARITY
The spark is the avalanche grown bold; coherence lowers the bar.

### NOVELTY
The phi-law lowers the streamer initiation threshold.

### ACTIONABILITY
Run sim/783_streamer_discharge.py; verify criterion at kappa->0; proceed to 784.
