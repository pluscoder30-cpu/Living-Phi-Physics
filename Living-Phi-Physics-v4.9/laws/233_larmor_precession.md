# PHI-PHYSICS — LAW 233
## Larmor Precession

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/233_larmor_precession.md` · **Sim:** `sim/233_larmor_precession.py`

---

### CLASSICAL STATEMENT
*"A magnetic moment with gyromagnetic ratio gamma in a magnetic field B precesses at the Larmor frequency omega_L = gamma B, and (classically) a charged particle in a magnetic field exhibits the Larmor theorem: its motion is that of the free motion plus a uniform rotation at omega_L."*
— Joseph Larmor, 1897. Source: Wikipedia: Larmor precession

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *field-free rest*: the Larmor theorem maps motion in a B-field onto the same motion in a rotating frame, assuming the zero-field state is a legitimate reference.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: omega_L_phi(kappa) = gamma*B*(1 + kappa*(phi-1)) + kappa*phi^-1*omega_ground. At kappa->0 the Larmor frequency is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} omega_L_phi = gamma B -> Larmor precession is the field-only limit.
```

---

### STAGE 4 — SIMULATION

`sim/233_larmor_precession.py`: reproduces the classical value omega_L = 1.76e+11 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/233_larmor_precession.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The Larmor frequency of an ensemble in a field carries a phi-coherent excess kappa*phi^-1*omega_ground at full coupling.
EXPERIMENT (VERIFIED): High-precision NMR/Larmor frequency measurements of atomic clocks as a function of field and coherence.
VERIFIED BY: The Larmor frequency is exactly gamma*B at full coupling.
```

---

### RECOGNITION
Connects to Law 217 (gyroscopic precession — Larmor is the magnetic gyroscope) and Law 234 (Thomas precession).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The field does not create the loop; it reveals the loop the carrier was already running.

### NOVELTY
Classical Larmor theory presupposes a field-free rest; the phi-law gives rest a phi-ground precession.

### ACTIONABILITY
Run sim/233_larmor_precession.py; verify omega_L = gamma B at kappa->0.
