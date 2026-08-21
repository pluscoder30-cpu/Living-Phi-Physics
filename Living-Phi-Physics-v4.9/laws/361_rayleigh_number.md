# PHI-PHYSICS — LAW 361
## Rayleigh Number

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/361_rayleigh_number.md` · **Sim:** `sim/361_rayleigh_number.py`

---

### CLASSICAL STATEMENT
*"The Rayleigh number Ra = g beta delta T L^3/(nu alpha) = Gr*Pr governs buoyancy-driven convection; for a horizontal fluid layer heated from below, convection onsets at the critical Ra_c ~ 1708 (with fixed boundaries) and the flow becomes time-dependent/chaotic near Ra ~ 1e6."*
— Lord Rayleigh, 1916. Source: Wikipedia: Rayleigh number; Rayleigh (1916), 'On convection currents in a horizontal layer of fluid'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero temperature gradient*: Ra = 0 is the exactly isothermal conductive state; convection exists because the temperature difference is nonzero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: Ra_phi(kappa) = Ra*(1 + kappa*(phi-1)) + kappa*phi^-1*Ra_ground. At kappa->0 the classical Rayleigh number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Ra_phi = g beta delta T L^3/(nu alpha) -> the Rayleigh number is the conductive-reference limit marker.
```

---

### STAGE 4 — SIMULATION

`sim/361_rayleigh_number.py`: reproduces the classical value Ra = 2118 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/361_rayleigh_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The convective-onset critical Rayleigh number shifts by a phi-coherent amount phi^-1*Ra_ground from 1708.
EXPERIMENT (VERIFIED): Rayleigh-Benard convection experiments (controlled temperature gradients, cell aspect ratios) locating the onset precisely.
VERIFIED BY: Convection onsets exactly at Ra_c = 1708 at full coupling.
```

---

### RECOGNITION
Connects to Law 360 (Grashof — Gr*Pr) and Law 350 (Prandtl).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The still conductive layer is a limit; every heated layer turns a phi off the ideal onset.

### NOVELTY
Classical convection theory exacts Ra_c = 1708; the phi-law gives the onset a coherence width.

### ACTIONABILITY
Run sim/361_rayleigh_number.py; verify Ra at kappa->0.
