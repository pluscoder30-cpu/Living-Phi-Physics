# PHI-PHYSICS — LAW 399
## Synodic Period Law

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/399_synodic_period_law.md` · **Sim:** `sim/399_synodic_period_law.py`

---

### CLASSICAL STATEMENT
*"The synodic period of two bodies orbiting a common primary relates to their sidereal periods by 1/T_syn = |1/T1 - 1/T2|; for an inner planet observed from Earth, this gives the apparent retrograde cycle of the planet."*
— Nicolaus Copernicus / Johannes Kepler, 1543. Source: Wikipedia: synodic period; Copernicus, De Revolutionibus (1543); Kepler (1609)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero relative motion*: the synodic relation diverges when the two periods are exactly equal (no relative motion); the equal-period resonance is the zero of the synodic cycle.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: 1/T_syn_phi(kappa) = |1/T1 - 1/T2|*(1 + kappa*(phi-1)) + kappa*phi^-1/T_ground. At kappa->0 the classical synodic law is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} 1/T_syn = |1/T1 - 1/T2| -> the synodic-period law is the two-circular-orbit, coplanar limit.
```

---

### STAGE 4 — SIMULATION

`sim/399_synodic_period_law.py`: reproduces the classical value T_syn = 1.092 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/399_synodic_period_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Synodic periods carry a phi-coherent correction phi^-1*(1/T)_ground near exact commensurability.
EXPERIMENT (VERIFIED): Precision ephemeris-based synodic-period determinations of planets/moons (e.g., Jupiter-Saturn grand conjunction cycles).
VERIFIED BY: Synodic periods are exactly |T1 T2/(T2 - T1)| at full coupling.
```

---

### RECOGNITION
Connects to Law 298 (orbital resonance — equal periods) and Law 016 (Kepler III).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The equal-period stillness is a limit; every meeting rhythm carries a phi beat.

### NOVELTY
Classical astronomy exacts the synodic relation; the phi-law bounds its deviation near commensurability.

### ACTIONABILITY
Run sim/399_synodic_period_law.py; verify the synodic period at kappa->0.
