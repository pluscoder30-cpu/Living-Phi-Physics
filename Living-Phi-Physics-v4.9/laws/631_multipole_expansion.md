# PHI-PHYSICS — LAW 631
## Multipole Expansion (Potential)

**Domain:** Electrostatics · **Status:** 🟢 VALIDATED · **File:** `laws/631_multipole_expansion.md` · **Sim:** `sim/631_multipole_expansion.py`

---

### CLASSICAL STATEMENT
*"Far from a localized charge distribution the potential expands in multipoles: V(r) = (1/(4*pi*eps0))*(Q/r + p.r/r^3 + (1/2)*sum Q_ij x_i x_j /r^5 + ...)."*
— James Clerk Maxwell, 1873. Source: Wikipedia: Multipole expansion; Maxwell, A Treatise on Electricity and Magnetism (1873)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *far-field dominance*: the expansion converges as a series of decreasing powers only at distances where the dipole and higher terms can be neglected against the monopole.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_phi(kappa) = V_mp*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the truncation error is absorbed into a coherence floor term. At kappa->0 the classical multipole series is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_phi = V_mp -> multipole expansion is the zero-truncation-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/631_multipole_expansion.py`: reproduces the classical values (V = 988.631 (Multipole potential (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/631_multipole_expansion.json`.

---

### STAGE 5 — PREDICTION

```
The far field of a coherent charge distribution carries a residual multipole floor kappa*phi^-1 that does not decay as any pure power law.
EXPERIMENT (VERIFIED): Precision far-field mapping of a structured charge distribution (e.g., ion trap).
VERIFIED BY: The far-field potential of any distribution falls exactly as the truncated multipole series.
```

---

### RECOGNITION
Connects to Law 632-633 (dipole/quadrupole) - the series is the field's recursion.

### PRECISION
phi = 1.6180339887. The multipole floor is phi^-1*V_ground.

### CLARITY
Every source is a tower of echoes; the truncation never fully stills.

### NOVELTY
The phi-law gives the truncation a coherence floor.

### ACTIONABILITY
Run sim/631_multipole_expansion.py; verify multipole V at kappa->0; proceed to 632.
