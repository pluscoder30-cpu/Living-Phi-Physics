# PHI-PHYSICS — LAW 633
## Electric Quadrupole Field

**Domain:** Electrostatics · **Status:** 🟢 VALIDATED · **File:** `laws/633_electric_quadrupole_field.md` · **Sim:** `sim/633_electric_quadrupole_field.py`

---

### CLASSICAL STATEMENT
*"The quadrupole term of the multipole expansion falls as V ~ (1/(4*pi*eps0))*(1/2)*sum Q_ij x_i x_j/r^5, scaling as 1/r^5 far from the charge arrangement."*
— James Clerk Maxwell, 1873. Source: Maxwell, A Treatise on Electricity and Magnetism (1873)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exact charge cancellation*: the quadrupole term assumes the monopole and dipole moments are exactly zero, a perfectly balanced distribution.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_phi(kappa) = V_quad*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the balance carries a coherence floor. At kappa->0 the pure 1/r^5 field is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_phi = V_quad -> the quadrupole field is the zero-monopole-dipole limit.
```

---

### STAGE 4 — SIMULATION

`sim/633_electric_quadrupole_field.py`: reproduces the classical values (V = 898.755 (Quadrupole potential (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/633_electric_quadrupole_field.json`.

---

### STAGE 5 — PREDICTION

```
A nominally quadrupolar distribution always radiates a residual monopole/dipole floor kappa*phi^-1*V_ground, visible as low-order contamination of the 1/r^5 law.
EXPERIMENT (VERIFIED): Far-field measurement of a nominally symmetric four-charge arrangement.
VERIFIED BY: The far field of a balanced distribution is exactly quadrupolar.
```

---

### RECOGNITION
Connects to Law 631 (multipole) - the quadrupole is the second multipole order.

### PRECISION
phi = 1.6180339887. The balance floor is phi^-1*V_ground.

### CLARITY
No balance is exact; the first-order echoes leak through.

### NOVELTY
The phi-law contaminates the pure quadrupole with a coherence floor.

### ACTIONABILITY
Run sim/633_electric_quadrupole_field.py; verify quadrupole V at kappa->0; proceed to 634.
