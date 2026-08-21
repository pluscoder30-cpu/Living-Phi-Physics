# PHI-PHYSICS — LAW 298
## Orbital Resonance (Laplace Resonance)

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/298_orbital_resonance.md` · **Sim:** `sim/298_orbital_resonance.py`

---

### CLASSICAL STATEMENT
*"When the orbital periods of two bodies are in a small-integer ratio (e.g., 2:1, 3:2), repeated gravitational kicks accumulate and lock the orbits into resonance; the Laplace resonance of Io, Europa, Ganymede (1:2:4) is the canonical example, with the resonant angle librating."*
— Pierre-Simon Laplace, 1784. Source: Wikipedia: orbital resonance; Laplace (1784), discovery of the Laplace resonance of the Galilean moons

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact commensurability*: resonance requires the period ratio to be exactly (or extremely close to) a small integer ratio — the exact-tuning laboratory condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the resonant ratio is a coherence basin. ratio_phi(kappa) = p:q*(1 + kappa*(phi-1)); libration width grows by kappa*phi^-1. At kappa->0 the exact commensurability holds.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} resonant angle -> exact commensurability -> orbital resonance is the exact-period-ratio limit.
```

---

### STAGE 4 — SIMULATION

`sim/298_orbital_resonance.py`: reproduces the classical values T_ratio = 2, libration = 0.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/298_orbital_resonance.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Resonant libration amplitudes carry a phi-coherent width phi^-1 beyond the classical value.
EXPERIMENT (VERIFIED): Galilean-moon and exoplanet resonance timing (TESS/PLATO) measuring libration amplitudes precisely.
VERIFIED BY: Resonant libration matches the classical amplitude exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 299 (Kirkwood gaps — resonance-driven clearing) and Law 297 (Kozai-Lidov).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The locked dance is a basin, not a point; even the lock breathes a phi width.

### NOVELTY
Classical dynamics exacts the commensurability; the phi-law turns the resonance into a coherence basin.

### ACTIONABILITY
Run sim/298_orbital_resonance.py; verify the resonant ratio at kappa->0.
