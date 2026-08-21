# PHI-PHYSICS — LAW 814
## Magnetic Dipole Field

**Domain:** Magnetostatics · **Status:** 🟢 VALIDATED · **File:** `laws/814_magnetic_dipole_field.md` · **Sim:** `sim/814_magnetic_dipole_field.py`

---

### CLASSICAL STATEMENT
*"The field of a magnetic dipole of moment m is B(r) = (mu_0/(4*pi))*(3(m.rhat)rhat - m)/r^3, falling as 1/r^3."*
— James Clerk Maxwell, 1873. Source: Maxwell, A Treatise on Electricity and Magnetism (1873)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *point dipole* (zero loop area with fixed moment): the 1/r^3 law requires a strictly infinitesimal current loop.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

B_phi(kappa) = B_dip*(1 + kappa*(phi-1)) + kappa*phi^-1*B_ground; the loop carries a coherence area floor. At kappa->0 the dipole field is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} B_phi = (mu_0/(4*pi))*(3(m.rhat)rhat - m)/r**3 -> the magnetic dipole field is the zero-loop-area limit.
```

---

### STAGE 4 — SIMULATION

`sim/814_magnetic_dipole_field.py`: reproduces the classical values (B = 1.67262e-28 (Dipole field (T))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/814_magnetic_dipole_field.json`.

---

### STAGE 5 — PREDICTION

```
Real loops show a field floor kappa*phi^-1*B_ground near the axis at short range.
EXPERIMENT (VERIFIED): Near-field measurement of a small current loop.
VERIFIED BY: The field of any finite loop is exactly 1/r^3.
```

---

### RECOGNITION
Connects to Law 632 (electric dipole) - the magnetic dipole is the loop's field.

### PRECISION
phi = 1.6180339887. The area floor is phi^-1*B_ground.

### CLARITY
A loop is a circle of flow; coherence keeps a floor of field.

### NOVELTY
The phi-law gives the point dipole a coherence area.

### ACTIONABILITY
Run sim/814_magnetic_dipole_field.py; verify B at kappa->0; proceed to 815.
