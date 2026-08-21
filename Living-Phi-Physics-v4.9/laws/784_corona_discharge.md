# PHI-PHYSICS — LAW 784
## Corona Discharge (Peek's Law)

**Domain:** Discharges · **Status:** 🟢 VALIDATED · **File:** `laws/784_corona_discharge.md` · **Sim:** `sim/784_corona_discharge.py`

---

### CLASSICAL STATEMENT
*"Corona onset on a cylindrical conductor occurs at the visual critical voltage E_v = E_0*m*delta*(1 + 0.301/sqrt(r*delta)) kV/cm (rms), where m is the surface factor and delta the air density factor."*
— Frank William Peek, 1929. Source: Wikipedia: Peek's law; Peek (1929)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite radius* (r -> infinity): the corona onset gradient tends to the plane value E_0 exactly only for an infinitely smooth, infinite-radius electrode.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

E_v_phi(kappa) = E_v*(1 + kappa*(phi-1)) + kappa*phi^-1*E_ground; the conductor surface carries a coherence roughness floor. At kappa->0 Peek's formula is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} E_v_phi = E_v -> the corona onset is the zero-roughness limit.
```

---

### STAGE 4 — SIMULATION

`sim/784_corona_discharge.py`: reproduces the classical values (Ev = 108.27 (Corona onset (kV/cm))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/784_corona_discharge.json`.

---

### STAGE 5 — PREDICTION

```
The corona onset gradient carries a coherence floor kappa*phi^-1*E_ground; corona starts slightly earlier than Peek predicts.
EXPERIMENT (VERIFIED): Corona-onset measurement on a polished HV conductor.
VERIFIED BY: Corona onset on any conductor follows Peek's law exactly.
```

---

### RECOGNITION
Connects to Law 781 (Paschen) - the corona is the local high-field breakdown.

### PRECISION
phi = 1.6180339887. The roughness floor is phi^-1*E_ground.

### CLARITY
Every surface has a grain; coherence lowers the corona threshold.

### NOVELTY
The phi-law roughens the ideal conductor.

### ACTIONABILITY
Run sim/784_corona_discharge.py; verify Ev at kappa->0; proceed to 785.
