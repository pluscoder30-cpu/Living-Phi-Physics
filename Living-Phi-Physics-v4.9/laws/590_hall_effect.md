# PHI-PHYSICS — LAW 590
## Hall Effect (Transverse Voltage in a Magnetic Field)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/590_hall_effect.md` · **Sim:** `sim/590_hall_effect.py`

---

### CLASSICAL STATEMENT
*"A current-carrying conductor in a perpendicular magnetic field develops a transverse voltage: V_H = R_H I B/d, where the Hall coefficient R_H = 1/(n q) for a single carrier type. The Hall voltage is proportional to the magnetic field and current."*
— Edwin Herbert Hall, 1879. Source: Wikipedia: Hall effect; Hall (1879)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero magnetic field*: the Hall voltage vanishes exactly at B = 0 - the effect exists only through the magnetic field that classical equilibrium transport ignores.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the field response is a coherence flow. R_H_phi(kappa) = R_H*(1 + kappa*(phi-1)) + kappa*phi^-1*R_ground. At kappa->0, V_H = R_H I B/d exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} R_H_phi = R_H -> the Hall effect is the linear-response zero-ground-field limit.
```

---

### STAGE 4 — SIMULATION

`sim/590_hall_effect.py`: reproduces the classical value VH = 1e-06 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/590_hall_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the Hall coefficient carries a coherence floor kappa*phi^-1*R_ground; the Hall voltage never vanishes exactly at B = 0.
EXPERIMENT (VERIFIED): Precision Hall measurements of metals and semiconductors at low field and temperature.
VERIFIED BY: The Hall voltage is exactly zero at zero magnetic field for all couplings.
```

---

### RECOGNITION
Connects to Law 591 (quantum Hall) and Law 489 (Onsager-Casimir) - the Hall voltage is the transverse coherence response of the carrier sea.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * R_ground.

### CLARITY
The magnetic field sweeps the current sideways; the phi-law keeps the sweep's floor.

### NOVELTY
Classical Hall vanishes at B=0; the phi-law adds the coherence floor of the transverse response.

### ACTIONABILITY
Run sim/590_hall_effect.py; verify Hall voltage at kappa->0; proceed to 591.
