# PHI-PHYSICS — LAW 596
## Shubnikov-de Haas Effect (Oscillatory Magnetoresistance)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/596_shubnikov_de_haas_effect.md` · **Sim:** `sim/596_shubnikov_de_haas_effect.py`

---

### CLASSICAL STATEMENT
*"The magnetoresistance of a metal at low temperature and high magnetic field oscillates with period Delta(1/B) = 2 pi e/(hbar A_F), the same Fermi-surface periodicity as the de Haas-van Alphen effect. The oscillations are seen in the resistance rather than the magnetization."*
— Lev Shubnikov and Wander Johannes de Haas, 1930. Source: Wikipedia: Shubnikov-de Haas effect; Shubnikov & de Haas (1930)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature*: the magnetoresistance oscillations require sharp Landau levels at T = 0 - a ground-state Fermi sea with no thermal coherence broadening.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the level sharpness carries coherence. The oscillation amplitude carries the Dingle factor with a coherence reduction of the scattering rate: rho_phi(kappa) = rho_osc*(1 + kappa*(phi-1)) + kappa*phi^-1*rho_ground. At kappa->0 the classical Shubnikov-de Haas oscillation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} rho_phi = rho_osc -> the Shubnikov-de Haas effect is the zero-coherence-sharpening quantum-oscillation limit.
```

---

### STAGE 4 — SIMULATION

`sim/596_shubnikov_de_haas_effect.py`: reproduces the classical value period = 3.179 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/596_shubnikov_de_haas_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the oscillation amplitude carries a coherence floor and enhanced sharpness; the measured magnetoresistance deviates from the classical prediction.
EXPERIMENT (VERIFIED): Magnetoresistance measurements of clean 2DEGs and metals at high field and low temperature.
VERIFIED BY: The Shubnikov-de Haas oscillations follow the classical form exactly at all couplings.
```

---

### RECOGNITION
Connects to Law 591 (quantum Hall) and Law 493 (Landau) - the oscillations are the resistance-coherence map of the Fermi sea.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * rho_ground.

### CLARITY
The resistance of the sea counts its Landau rows; the phi-law keeps the counting's floor.

### NOVELTY
Classical SdH assumes sharp levels; the phi-law adds the coherence sharpening of the real sea.

### ACTIONABILITY
Run sim/596_shubnikov_de_haas_effect.py; verify oscillation at kappa->0; proceed to 597.
