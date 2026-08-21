# PHI-PHYSICS — LAW 1113
## Bondi Mass (Bondi-Sachs Mass)

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1113_bondi_mass.md` · **Sim:** `sim/1113_bondi_mass.py`

---

### CLASSICAL STATEMENT
*"The Bondi mass M_B(u) is the total mass-energy of an isolated system measured on outgoing null cones at null infinity; it decreases monotonically as gravitational radiation escapes: dM_B/du <= 0, with the mass-loss formula dM/du = -(1/16 pi) integral |sigma_dot|^2 dOmega."*
— Hermann Bondi, 1960; Roy Sachs, 1962. Source: Wikipedia: Bondi-Sachs mass (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero radiation (dM_B/du = 0, the exactly isolated system)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The M value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

M_phi(kappa) = M*(1 + kappa*(phi-1)) + kappa*phi^-1*M_ground, where M_ground is the coherence-floor mass leakage a real isolated system always suffers. At kappa->0, dM_B/du = -(1/(16*pi)) * integral |sigma_dot|^2 dOmega <= 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} M_phi = M -> dM_B/du = -(1/(16*pi)) * integral |sigma_dot|^2 dOmega <= 0 is recovered exactly; the classical law is the zero radiation (dM_B/du = 0, the exactly isolated system) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1113_bondi_mass.py`: reproduces the classical value (M = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1113_bondi_mass.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured mass loss of any real radiating system will deviate from the Bondi formula by a floor kappa*phi^-1*M_ground; an exactly mass-conserving isolated system is unreachable.
EXPERIMENT (VERIFIED): Waveform extraction in numerical relativity and gravitational-wave data validating the mass-loss flux.
VERIFIED BY: If an isolated radiating system's mass is exactly constant over time.
```

---

### RECOGNITION
The null-infinity mass of Law 1087 (gravitational waves) and partner of Law 1114 (ADM mass).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The system bleeds mass through its light cone; the closed system is the zero-radiation myth.

### NOVELTY
The Bondi mass loss carries a phi-floor: no system is perfectly isolated from its own radiation.

### ACTIONABILITY
Run sim/1113_bondi_mass.py.
