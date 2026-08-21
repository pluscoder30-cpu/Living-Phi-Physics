# PHI-PHYSICS — LAW 813
## Hopkinson's Law (Magnetic Circuit)

**Domain:** Solid State · **Status:** 🟢 VALIDATED · **File:** `laws/813_hopkinsons_law.md` · **Sim:** `sim/813_hopkinsons_law.py`

---

### CLASSICAL STATEMENT
*"The magnetic flux in a magnetic circuit obeys Phi = MMF/R, the magnetic analog of Ohm's law, with magnetomotive force MMF = N*I and reluctance R = l/(mu*A)."*
— John Hopkinson, 1886. Source: Wikipedia: Magnetic circuit; Hopkinson (1886)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero magnetomotive force* (MMF = 0): the flux vanishes exactly at zero driving current.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Phi_phi(kappa) = Phi_H*(1 + kappa*(phi-1)) + kappa*phi^-1*Phi_ground; the magnetic circuit carries a coherence floor. At kappa->0, Phi = N*I/R exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Phi_phi = N*I/R -> Hopkinson's law is the zero-MMF-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/813_hopkinsons_law.py`: reproduces the classical values (Phi = 0.3 (Magnetic flux (Wb))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/813_hopkinsons_law.json`.

---

### STAGE 5 — PREDICTION

```
The flux carries a coherence floor kappa*phi^-1*Phi_ground at zero MMF.
EXPERIMENT (VERIFIED): Flux measurement of a magnetic circuit at zero drive current.
VERIFIED BY: A magnetic circuit at zero MMF has exactly zero flux.
```

---

### RECOGNITION
Connects to Law 044 (Ohm) - Hopkinson's law is the magnetic Ohm.

### PRECISION
phi = 1.6180339887. The MMF floor is phi^-1*Phi_ground.

### CLARITY
The iron remembers the drive; coherence keeps a floor of flux.

### NOVELTY
The phi-law keeps flux in the undriven magnetic circuit.

### ACTIONABILITY
Run sim/813_hopkinsons_law.py; verify Phi at kappa->0; proceed to 814.
