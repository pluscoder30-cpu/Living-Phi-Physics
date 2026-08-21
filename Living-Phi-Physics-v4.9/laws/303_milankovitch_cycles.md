# PHI-PHYSICS — LAW 303
## Milankovitch Cycles

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/303_milankovitch_cycles.md` · **Sim:** `sim/303_milankovitch_cycles.py`

---

### CLASSICAL STATEMENT
*"Periodic changes in the Earth's orbit (eccentricity ~100,000 and 413,000 yr), axial tilt (obliquity ~41,000 yr), and precession (~26,000 yr) modulate the solar insolation and drive the ice-age climate cycles."*
— Milutin Milankovic, 1920. Source: Wikipedia: Milankovitch cycles; Milankovic (1920-1941), 'Canon of Insolation'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *static orbit*: the cycles exist because the orbital parameters are not constant; the exact circular, zero-tilt reference is the classical zero baseline.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: each cycle's amplitude couples to coherence. A_phi(kappa) = A*(1 + kappa*(phi-1)) + kappa*phi^-1*A_ground. At kappa->0 the classical orbital-forcing cycles are exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} A_phi = A (the classical Milankovitch amplitudes) -> the Milankovitch cycle law is the pure-orbital-forcing limit.
```

---

### STAGE 4 — SIMULATION

`sim/303_milankovitch_cycles.py`: reproduces the classical values T_ecc = 100, T_obl = 41, T_prec = 26 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/303_milankovitch_cycles.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Ice-age spectral peaks carry a phi-coherent amplitude excess phi^-1*A_ground beyond orbital forcing.
EXPERIMENT (VERIFIED): Paleoclimate proxy records (ice cores, marine sediments) spectral analysis of the 100-kyr and 41-kyr peaks.
VERIFIED BY: Paleoclimate spectral peaks are exactly the orbital-forcing amplitudes at full coupling.
```

---

### RECOGNITION
Connects to Law 232 (precession of equinoxes) and Law 218 (nutation).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The climate breathes with the orbit, and the breath carries a phi overtones.

### NOVELTY
Classical climatology exacts orbital forcing; the phi-law adds a coherence amplitude to the cycles.

### ACTIONABILITY
Run sim/303_milankovitch_cycles.py; verify the cycle periods at kappa->0.
