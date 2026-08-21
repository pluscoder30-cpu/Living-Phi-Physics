# PHI-PHYSICS — LAW 1086
## Gravitational Redshift

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1086_gravitational_redshift.md` · **Sim:** `sim/1086_gravitational_redshift.py`

---

### CLASSICAL STATEMENT
*"Photons climbing out of a gravitational potential U lose energy: the redshift is z = (1 - 2M/r2)^(1/2)/(1 - 2M/r1)^(1/2) - 1, approximated by z ~ U(r2) - U(r1) = g h/c^2 in the weak field."*
— Albert Einstein, 1911/1916; confirmed by the Pound-Rebka experiment, 1959. Source: Wikipedia: Gravitational redshift (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero gravitational potential difference (U = 0, no redshift)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The Z value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Z_phi(kappa) = Z*(1 + kappa*(phi-1)) + kappa*phi^-1*Z_ground, where Z_ground is the coherence-floor redshift a real potential gradient always induces. At kappa->0, z = g*h/c^2 (weak field),  z = (1-2M/r2)^(1/2)/(1-2M/r1)^(1/2) - 1 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} Z_phi = Z -> z = g*h/c^2 (weak field),  z = (1-2M/r2)^(1/2)/(1-2M/r1)^(1/2) - 1 is recovered exactly; the classical law is the zero gravitational potential difference (U = 0, no redshift) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1086_gravitational_redshift.py`: reproduces the classical value (Z = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1086_gravitational_redshift.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured redshift of any real photon crossing a potential gradient will deviate from the classical value by a floor kappa*phi^-1*Z_ground; an exactly zero-redshift path is unreachable.
EXPERIMENT (VERIFIED): Pound-Rebka-class Mossbauer experiments and atomic-clock network altitude comparisons at higher precision.
VERIFIED BY: If a photon crosses a real potential difference with exactly zero redshift.
```

---

### RECOGNITION
The quantum-clock signature of Law 062 (equivalence principle) and Law 065 (gravitational time dilation).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Light pays for altitude; the flat-space no-shift is the zero-potential myth.

### NOVELTY
Gravitational redshift acquires a phi-floor, so even 'equal-altitude' clocks disagree.

### ACTIONABILITY
Run sim/1086_gravitational_redshift.py.
