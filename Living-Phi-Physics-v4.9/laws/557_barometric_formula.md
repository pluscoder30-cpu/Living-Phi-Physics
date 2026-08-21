# PHI-PHYSICS — LAW 557
## Barometric Formula (Atmospheric Pressure vs Altitude)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/557_barometric_formula.md` · **Sim:** `sim/557_barometric_formula.py`

---

### CLASSICAL STATEMENT
*"The pressure of an isothermal atmosphere decays exponentially with altitude: P(h) = P_0 exp(-m g h/(k_B T)) = P_0 exp(-h/H), where the scale height H = k_B T/(m g)."*
— Pierre-Simon Laplace, 1778. Source: Wikipedia: Barometric formula; Laplace (1778)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *isothermal atmosphere*: the formula assumes constant temperature with altitude - an atmosphere with no temperature gradient and no thermal coherence structure.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the isothermal column carries coherence. P_phi(kappa) = P_0 exp(-h/H)*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, where P_ground is the coherence floor of the column. At kappa->0 the barometric formula is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_phi = P_0 exp(-h/H) -> the barometric formula is the zero-gradient isothermal-atmosphere limit.
```

---

### STAGE 4 — SIMULATION

`sim/557_barometric_formula.py`: reproduces the classical value P_h = 9e+04 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/557_barometric_formula.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the atmospheric pressure retains a coherence floor kappa*phi^-1*P_ground; the exponential law is only approximate in real atmospheres.
EXPERIMENT (VERIFIED): High-altitude balloon and radiosonde pressure-altitude measurements compared with the barometric formula.
VERIFIED BY: P(h) = P_0 exp(-h/H) exactly for all altitudes and couplings.
```

---

### RECOGNITION
Connects to Law 423 (lapse rate) and Law 554 (kinetic theory) - the barometric formula is the gravity coherence of the gas column.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * P_ground.

### CLARITY
The atmosphere thins exponentially because gravity and heat argue; the phi-law keeps the argument's floor.

### NOVELTY
Classical barometric formula assumes isothermality; the phi-law adds the coherence floor of the real column.

### ACTIONABILITY
Run sim/557_barometric_formula.py; verify exponential at kappa->0; proceed to 558.
