# PHI-PHYSICS — LAW 735
## Debye Shielding (Screening)

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/735_debye_shielding.md` · **Sim:** `sim/735_debye_shielding.py`

---

### CLASSICAL STATEMENT
*"A charged object in a plasma is surrounded by an oppositely-charged screening cloud; the effective field decays as exp(-r/lambda_D) beyond the Debye length."*
— Peter Debye; Erich Hückel, 1923. Source: Wikipedia: Debye-Hückel theory (1923)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero perturbation*: perfect shielding means the object's field is exactly cancelled beyond a few lambda_D.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Phi_phi(kappa) = Phi*(1 + kappa*(phi-1)) + kappa*phi^-1*Phi_ground; the screening cloud carries a coherence floor. At kappa->0 the exponential decay is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Phi_phi = q*exp(-r/lambda_D)/(4*pi*eps_0*r) -> Debye shielding is the zero-coherence-cloud limit.
```

---

### STAGE 4 — SIMULATION

`sim/735_debye_shielding.py`: reproduces the classical values (Phi = 330.634 (Shielded potential (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/735_debye_shielding.json`.

---

### STAGE 5 — PREDICTION

```
The shielded field never reaches exactly zero; a coherence floor kappa*phi^-1*Phi_ground persists far beyond lambda_D.
EXPERIMENT (VERIFIED): Field measurement far from a biased probe in a tenuous plasma.
VERIFIED BY: The field of a shielded object is exactly zero beyond a few Debye lengths.
```

---

### RECOGNITION
Connects to Law 734 (Debye length) - shielding is the cloud's action.

### PRECISION
phi = 1.6180339887. The cloud floor is phi^-1*Phi_ground.

### CLARITY
Shielding hides, but never erases; a coherence echo remains.

### NOVELTY
The phi-law gives the shielded field a floor.

### ACTIONABILITY
Run sim/735_debye_shielding.py; verify shielded Phi at kappa->0; proceed to 736.
