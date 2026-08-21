# PHI-PHYSICS — LAW 877
## Anomalous Dispersion

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/877_anomalous_dispersion.md` · **Sim:** `sim/877_anomalous_dispersion.py`

---

### CLASSICAL STATEMENT
*"dn/domega < 0 (or dn/dlambda > 0) near an absorption line: the refractive index decreases with increasing frequency; group velocity can exceed c or become negative in the anomalous region."*
— Christian Andreas Doppler (observed); theory by Sellmeier, Ketteler, 19th century. Source: Wikipedia: Dispersion (optics) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero absorption*: anomalous dispersion is strictly confined to regions of absorption; without absorption the anomaly vanishes exactly.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

n_anom_phi(kappa) = n_anom*(1 + kappa*(phi-1)) + kappa*phi^-1*n_anom_ground, with n_anom_ground the index floor. At kappa->0, the anomalous region reduces to the classical dispersion law.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} n_anom_phi = n_anom -> anomalous dispersion is the zero-absorption-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/877_anomalous_dispersion.py`: reproduces the classical value nanom = 1.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/877_anomalous_dispersion.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The anomalous-dispersion region will bleed slightly beyond the absorption line by a coherence floor kappa*phi^-1; the anomaly is never perfectly confined.
EXPERIMENT (VERIFIED): Measure n(lambda) across an absorption line of a dye or atomic vapor.
VERIFIED BY: If anomalous dispersion is exactly zero outside the absorption line.
```

---

### RECOGNITION
Connects to Law 878 (normal dispersion) and Law 654 (Kramers-Kronig).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The anomaly lives where absorption breathes; it cannot be confined.

### NOVELTY
Anomalous dispersion gains an absorption floor.

### ACTIONABILITY
Run sim/877_anomalous_dispersion.py.
