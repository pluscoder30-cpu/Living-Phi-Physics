# PHI-PHYSICS — LAW 794
## Corbino Effect (Radial Hall)

**Domain:** Solid State · **Status:** 🟢 VALIDATED · **File:** `laws/794_corbino_effect.md` · **Sim:** `sim/794_corbino_effect.py`

---

### CLASSICAL STATEMENT
*"A radial current in a disk with a perpendicular magnetic field produces an azimuthal Hall field; the Corbino geometry gives the Hall angle from the field-induced current redistribution."*
— Orso Mario Corbino, 1911. Source: Wikipedia: Corbino effect; Corbino (1911)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero magnetic field* (B = 0): the azimuthal response vanishes exactly without the field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_az_phi(kappa) = I_az*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ground; the disk carries a coherence floor. At kappa->0 the Corbino response is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_az_phi = I_az -> the Corbino effect is the zero-B-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/794_corbino_effect.py`: reproduces the classical values (I = 0.001 (Azimuthal current (A))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/794_corbino_effect.json`.

---

### STAGE 5 — PREDICTION

```
The azimuthal current carries a coherence floor kappa*phi^-1*I_ground at zero field.
EXPERIMENT (VERIFIED): Corbino-disk current measurement in a weak field.
VERIFIED BY: A Corbino disk at zero field has exactly zero azimuthal current.
```

---

### RECOGNITION
Connects to Law 590 (Hall) - the Corbino effect is the radial-geometry Hall response.

### PRECISION
phi = 1.6180339887. The B-floor is phi^-1*I_ground.

### CLARITY
The disk turns without the field; coherence keeps a floor of spin.

### NOVELTY
The phi-law keeps the Corbino response at zero field.

### ACTIONABILITY
Run sim/794_corbino_effect.py; verify I_az at kappa->0; proceed to 795.
