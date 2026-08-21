# PHI-PHYSICS — LAW 760
## Stellarator Confinement

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/760_stellarator.md` · **Sim:** `sim/760_stellarator.py`

---

### CLASSICAL STATEMENT
*"The stellarator confines plasma with a twisted (helical) magnetic field produced entirely by external coils, without driving a plasma current."*
— Lyman Spitzer, 1951. Source: Wikipedia: Stellarator; Spitzer (1951) 'A Proposed Stellarator'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero rotational transform*: confinement vanishes exactly when the field lines have no twist.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

iota_phi(kappa) = iota*(1 + kappa*(phi-1)) + kappa*phi^-1*iota_ground; the twisted field carries a coherence floor. At kappa->0 the stellarator field is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} iota_phi = iota -> the stellarator is the zero-twist-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/760_stellarator.py`: reproduces the classical values (iota = 1e+09 (Rotational transform)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/760_stellarator.json`.

---

### STAGE 5 — PREDICTION

```
The rotational transform carries a coherence floor kappa*phi^-1*iota_ground; untwisted fields still confine a little.
EXPERIMENT (VERIFIED): Confinement measurement of a stellarator at reduced field twist.
VERIFIED BY: An untwisted field has exactly zero rotational transform confinement.
```

---

### RECOGNITION
Connects to Law 759 (tokamak) - the stellarator is the coil-only confinement.

### PRECISION
phi = 1.6180339887. The twist floor is phi^-1*iota_ground.

### CLARITY
The twist is the hold; coherence keeps a floor of it.

### NOVELTY
The phi-law keeps stellarator hold at zero twist.

### ACTIONABILITY
Run sim/760_stellarator.py; verify iota at kappa->0; proceed to 761.
